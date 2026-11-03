"""Run the signing engine.

  python -m engine.run --input network.geojson --settings settings.json --out outdir \
      [--overrides answers.json] [--inventory existing_signs.geojson] [--layers C-ROAD-CL] [--epsg 22992]

settings.json uses the dashboard's run-settings object (mode, code, families, level, units, drive, size, ...).
Exit code 0 = design done, 2 = stopped for missing data (see questions.json).
"""
from __future__ import annotations
import argparse
import json
import os
import sys
from datetime import datetime

from . import adapters
from .data import apply_overrides, load_overrides, prescan
from .geom import m_from_ft
from .placement import FAMILY_KEY, Placer, qa_conflicts, qa_spacing
from .rulebook import CLASS_ORDER, Rulebook
from .triggers import detect, detect_curves
from . import writers

LEVEL_KEEP = {"mand": {"Mandatory", "Conditional"},
              "rec": {"Mandatory", "Conditional", "Recommended"},
              "opt": {"Mandatory", "Conditional", "Recommended", "Optional"}}
DEFAULT_SETTINGS = {"mode": "design", "code": "mutcd_11e", "families": ["reg", "warn", "mark", "delin"],
                    "level": "rec", "units": "metric", "drive": "right", "size": "auto", "env": ["auto"],
                    "missing": "batch", "outputs": ["same", "xlsx", "report"], "tol": 15, "consolidate": True}


def family_of(rb: Rulebook, code: str, kind: str) -> str:
    if kind == "marking":
        return "mark"
    if code == "DELINEATOR":
        return "delin"
    return FAMILY_KEY.get(rb.devices.get(code, {}).get("family", "warning"), "warn")


def audit(devs, inventory_path: str, tol: float):
    with open(inventory_path, encoding="utf-8") as fh:
        fc = json.load(fh)
    exist = []
    for i, f in enumerate(fc.get("features", [])):
        g = f.get("geometry") or {}
        if g.get("type") != "Point":
            continue
        p = f.get("properties") or {}
        code = str(p.get("code") or p.get("sign_code") or p.get("mutcd") or "").strip().upper()
        exist.append({"id": str(p.get("id") or f"E{i + 1:04d}"), "code": code, "xy": g["coordinates"][:2],
                      "condition": p.get("condition", ""), "used": False})
    out = []
    import math
    for d in devs:
        if d.kind != "sign" or d.x is None or d.cls == "Conditional":
            continue
        best, bd = None, 1e9
        for e in exist:
            if e["used"] or e["code"] != d.code.upper():
                continue
            dd = math.hypot(e["xy"][0] - d.x, e["xy"][1] - d.y)
            if dd < bd:
                best, bd = e, dd
        if best and bd <= tol:
            best["used"] = True
            f = "Present" if not best["condition"] or str(best["condition"]).lower() in ("good", "ok") else "Present - condition"
            out.append({"finding": f, "code": d.code, "req": d.id, "existing": best["id"], "cls": d.cls,
                        "dist": round(bd, 1), "where": d.where, "note": str(best["condition"])})
        else:
            out.append({"finding": f"Missing - {d.cls}", "code": d.code, "req": d.id, "cls": d.cls, "where": d.where,
                        "note": f"nearest same-code sign {bd:.0f} m away" if best else "no sign of this code nearby"})
    for e in exist:
        if not e["used"]:
            out.append({"finding": "Not required by design - review", "code": e["code"], "existing": e["id"],
                        "note": "may be redundant, misplaced beyond tolerance, or serve a condition not in the data"})
    return out


def run(args) -> int:
    settings = dict(DEFAULT_SETTINGS)
    if args.settings:
        with open(args.settings, encoding="utf-8") as fh:
            settings.update(json.load(fh))
    os.makedirs(args.out, exist_ok=True)
    rb = Rulebook(settings.get("code", "mutcd_11e"))
    kw = {"epsg": args.epsg or (int(settings["epsg"]) if str(settings.get("epsg", "")).isdigit() else None),
          "layers": args.layers.split(",") if args.layers else None, "nodes": args.nodes,
          "node_layer": args.node_layer, "tee_tol": args.tee_tol,
          "exclude": (load_overrides(args.overrides).get("exclude_links") if args.overrides else None)}
    try:
        net = adapters.load(args.input, **kw)
    except RuntimeError as e:
        print(f"INPUT PROBLEM: {e}")
        return 3
    if args.input.lower().endswith(".dxf"):
        # Re-read check (build spec 5.3): snapshot entity counts by layer; compare with the last run when given.
        counts = adapters.dxf_entity_counts(args.input)
        with open(os.path.join(args.out, "layer_counts.json"), "w", encoding="utf-8") as fh:
            json.dump(counts, fh, indent=1, ensure_ascii=False)
        if args.compare_counts:
            with open(args.compare_counts, encoding="utf-8") as fh:
                diff = adapters.compare_counts(json.load(fh), counts)
            if diff:
                net.assumptions.append("INPUT CHANGED since the last run - old junction numbers and coordinates are "
                                       "NOT reused until re-confirmed: " + "; ".join(diff))
                print("INPUT CHANGED since the last run:\n - " + "\n - ".join(diff))
            else:
                net.assumptions.append("input drawing layer counts match the last run")
    if args.edge_layers and args.input.lower().endswith(".dxf"):
        net.edges = adapters.load_edges(args.input, args.edge_layers.split(","))
        net.assumptions.append(f"sign offsets measured from kerb lines on layer(s) {args.edge_layers}")
    if not net.crs and settings.get("epsg"):
        net.crs = f"EPSG:{settings['epsg']}"
    ov = load_overrides(args.overrides)
    apply_overrides(net, ov, settings)
    net.hazard_types = rb.hazards
    has_curves = any(detect_curves(l.coords) for l in net.links.values())
    questions = prescan(net, settings, has_curves)
    project = args.project or settings.get("project", os.path.splitext(os.path.basename(args.input))[0])
    meta = {"Project": project, "Status": "DRAFT for engineer review", "Input": net.source, "CRS": net.crs or "as input", "Governing code": rb.meta["name"],
            "Rulebook status": rb.meta.get("status"), "Mode": settings.get("mode"), "Level": settings.get("level"),
            "Families": ", ".join(settings.get("families", [])), "Units": settings.get("units"),
            "Traffic side": settings.get("drive"), "Links": len(net.links), "Intersections (3+ legs)":
            sum(1 for n in net.nodes.values() if n.degree >= 3), "Run at": datetime.now().strftime("%Y-%m-%d %H:%M")}
    if questions and not args.allow_partial:
        with open(os.path.join(args.out, "questions.json"), "w", encoding="utf-8") as fh:
            json.dump(questions, fh, indent=1, ensure_ascii=False)
        res = writers.dashboard_result([], questions, [], [f"{len(questions)} data question(s) open; design not started."])
        with open(os.path.join(args.out, "result.json"), "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1)
        writers.write_id_map(os.path.join(args.out, "network_ids"), net,
                             args.input if args.input.lower().endswith(".dxf") else None)
        print(f"STOPPED: {len(questions)} data question(s). See questions.json and network_ids.* for link/node ids")
        for q in questions:
            print(f" - {q['topic']}: {q['items']}")
        return 2
    # ---------------- design
    net.sign_catalog = rb.sign_catalog
    trig = detect(net, settings)
    fams = set(settings.get("families") or [])
    keep = LEVEL_KEEP.get(settings.get("level", "rec"), LEVEL_KEEP["rec"])
    settings["_keep"] = sorted(keep)
    placer = Placer(net, rb, settings)
    skipped = {"family": 0, "level": 0}
    for tg in trig:
        for res in rb.resolve(tg.trigger, tg.t):
            fam = family_of(rb, res["device"], res["kind"])
            if tg.trigger == "SIGN-REQUEST":
                if res["device"] not in rb.devices:
                    net.assumptions.append(f"requested sign {res['device']} is not in the MUTCD catalog; not placed")
                    continue
                placer.place(tg, res)
                continue
            if fam not in fams:
                skipped["family"] += 1
                continue
            if res["class"] not in keep:
                skipped["level"] += 1
                continue
            placer.place(tg, res)
    log = qa_spacing(placer, m_from_ft(float(rb.meta.get("min_sign_spacing_ft", 100))))
    notv1 = [f for f in fams if f in ("guide", "ttc", "supp")]
    if notv1:
        net.assumptions.append("families not designed in this version: " + ", ".join(notv1))
    for k, v in (ov.get("_sources") or {}).items():
        net.assumptions.append(f"input {k}: {v}")
    log = [f"ASSUMPTION: {a}" for a in net.assumptions] + [f"NOTE: {x}" for x in placer.log] + log
    for d in placer.devs:
        c = getattr(d, "_companion_of", None)
        if c is not None:
            d.x, d.y, d.back_m = c.x, c.y, c.back_m
    conflicts = qa_conflicts(placer.devs, net)
    devs = placer.devs
    aud = None
    if settings.get("mode") in ("audit", "both"):
        if not args.inventory:
            print("Audit mode needs --inventory")
            return 2
        aud = audit(devs, args.inventory, float(settings.get("tol", 15)))
    # ---------------- outputs
    # Every output file is DRAFT until the rulebook is signed off (build spec section 0, rule 2).
    draft = "" if rb.meta.get("status") == "signed" else "_DRAFT"
    base = os.path.join(args.out, project.replace(" ", "_") + draft)
    outs = []
    write_questions = questions  # only non-empty when --allow-partial
    sp = writers.load_style_pack(args.style_pack or settings.get("style_pack")
                                 or ("none" if settings.get("style") == "input" else "ti_details"))
    if sp:
        meta["Drawing style"] = sp.get("name", "")
        fx = (sp.get("fixation") or {}).get("height_to_bottom_m")
        if fx:
            low_h = sorted({d.height_m for d in devs if d.kind == "sign" and d.height_m and d.height_m > float(fx) + 0.005})
            if low_h:
                log.append(f"ASSUMPTION: T&I fixation detail shows {fx:.2f} m to the sign bottom; MUTCD mounting (2A.15) needs "
                           f"up to {max(low_h):.2f} m on this run. The schedule heights follow the MUTCD; check the detail.")
    writers.write_schedule(base + "_Sign_Schedule.xlsx", devs, meta, write_questions, log + conflicts, aud, rb=rb, style_pack=sp)
    outs.append(base + "_Sign_Schedule.xlsx")
    writers.write_geojson(base + "_Signs.geojson", devs, net.crs)
    outs.append(base + "_Signs.geojson")
    if args.input.lower().endswith(".dxf") or "dxf" in (settings.get("outputs") or []) or args.dxf:
        if sp:
            log += [f"NOTE: {x}" for x in writers.write_dxf_styled(base + "_Signing.dxf", devs, rb, sp,
                    args.input if args.input.lower().endswith(".dxf") else None, args.symbol_scale,
                    junctions=ov.get("junctions"), table_origin=ov.get("schedule_table_origin"),
                    draft=bool(draft))]
        else:
            writers.write_dxf(base + "_Signing.dxf", devs, rb, net.style or None,
                              args.input if args.input.lower().endswith(".dxf") else None, args.symbol_scale)
        outs.append(base + "_Signing.dxf")
    if "report" in (settings.get("outputs") or ["report"]):
        writers.write_report(base + "_Report.docx", devs, meta, write_questions, log, conflicts, rb.meta, aud, rb=rb)
        outs.append(base + "_Report.docx")
    issues = []
    if rb.meta.get("status") != "signed":
        issues.append(f"Rulebook {rb.code} not signed off: results are DRAFT.")
    low = sum(1 for d in devs if d.confidence == "Low")
    if low:
        issues.append(f"{low} device(s) Low confidence.")
    moves = [x for x in log if not x.startswith(("ASSUMPTION: ", "NOTE: "))]
    if moves:
        issues.append(f"{len(moves)} spacing adjustment(s).")
    if any("PROVISIONAL" in x for x in log):
        issues.append("Uses PROVISIONAL inputs (see QA log).")
    issues += conflicts
    res = writers.dashboard_result(devs, write_questions, [os.path.basename(o) for o in outs], issues)
    with open(os.path.join(args.out, "result.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res["counts"]), "|", " ".join(issues))
    for o in outs:
        print("wrote", o)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Road signing design/audit engine")
    ap.add_argument("--input", required=True)
    ap.add_argument("--settings")
    ap.add_argument("--overrides")
    ap.add_argument("--inventory")
    ap.add_argument("--nodes", help="nodes table for CSV/XLSX input")
    ap.add_argument("--layers", help="DXF centreline layer(s), comma separated")
    ap.add_argument("--node-layer", dest="node_layer")
    ap.add_argument("--edge-layers", dest="edge_layers", help="DXF kerb/edge-of-pavement layer(s): signs are offset from these")
    ap.add_argument("--epsg", type=int)
    ap.add_argument("--tee-tol", dest="tee_tol", type=float, default=12.0,
                    help="max gap (m) for joining a centreline end to another centreline as a T-junction")
    ap.add_argument("--compare-counts", dest="compare_counts",
                    help="layer_counts.json from the last run; any change in the input drawing is reported")
    ap.add_argument("--project")
    ap.add_argument("--out", default="out")
    ap.add_argument("--dxf", action="store_true", help="also write DXF when input is not DXF")
    ap.add_argument("--symbol-scale", dest="symbol_scale", type=float, default=1.0)
    ap.add_argument("--style-pack", dest="style_pack",
                    help="drawing style pack in styles/ (default: settings style_pack, else ti_details; 'none' = match input)")
    ap.add_argument("--allow-partial", dest="allow_partial", action="store_true",
                    help="design anyway and list missing data as pending (not the default: the skill asks first)")
    return run(ap.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
