"""Write a readable rule book (Markdown) from a rulebook folder.

    python -m engine.rulebook_doc --code mutcd_11e --out Rulebook_MUTCD_11e.md

Sign pictures are referenced as symbols/<code>.png next to the output file; copy the
rulebook's symbols/ folder beside it (the export bundle does this).
"""
from __future__ import annotations
import argparse
import csv
import os
from datetime import date

import yaml

from .rulebook import CLASS_OF, HERE

FIELDS = {
    "class": "road class (freeway, expressway, arterial, collector, local)",
    "speed_kmh": "posted speed on the approach (km/h)", "aadt": "traffic volume (veh/day)",
    "urban": "urban street (true/false)", "lanes": "lanes per direction", "lanes_total": "total lanes",
    "width_ft": "traveled-way width (ft)", "oneway": "one-way link", "divided": "divided road",
    "diff_kmh": "posted speed minus curve advisory speed (km/h)", "advisory_kmh": "curve advisory speed (km/h)",
    "chart_a": "Table 2C-4 Chart A result (Required / Recommended / Optional)",
    "reduction_kmh": "drop in speed limit at a change point (km/h)", "suppress_sign": "second curve of a reverse pair",
    "school_zone": "school zone designated by statute", "tracks": "number of tracks at a grade crossing",
    "signals_gates": "grade crossing has flashing-light signals or gates", "clear_width_m": "roadway horizontal clearance on the structure (m)",
    "structure": "bridge / culvert / underpass", "heavy_commercial": "high share of commercial vehicles",
    "clearance_m": "vertical clearance (m)", "statutory_height_m": "statutory maximum vehicle height (m)",
    "advisory_kmh": "advisory speed set for the point (km/h)", "grade_pct": "downgrade (%)", "length_m": "downgrade length (m)",
    "bus_not_visible": "stopped school bus not visible for adequate distance", "emergency_signal": "emergency-vehicle signal present",
    "role": "major or entering roadway", "equal": "both roadways of the same class", "to_two_lane": "section after is two-lane two-way",
    "lane_width_m": "lane width (m)", "curve_sign": "curve sign chosen from geometry", "yield_here_signs": "Yield Here To Pedestrians signs installed",
    "sight_restricted": "control not visible for sufficient distance", "degree": "number of legs at the node",
}
TRIGGERS = {
    "INT-STOP-2WAY": "Minor-road STOP approach", "INT-STOP-AWAY": "All-way STOP approach",
    "INT-YIELD": "YIELD approach", "INT-SIGNAL": "Signalised approach", "INT-ROUNDABOUT": "Roundabout entry",
    "INT-UNCONTROLLED-MAJOR": "Major road at an uncontrolled junction", "CURVE": "Horizontal curve",
    "SPEED-ZONE": "Speed limit change point", "AFTER-MAJOR-INT": "Beyond a major intersection",
    "ONE-WAY-CROSSING": "Road meeting a one-way street", "ONE-WAY-EXIT": "Exit end of a one-way street",
    "LANE-DROP": "Lane drop", "PED-XING-MIDBLOCK": "Mid-block crosswalk", "SCHOOL": "School",
    "MARK-LINK": "Every road link (markings)", "BOUNDARY-ENTRY": "Site entry (gate, external road not drawn)",
    "DIVIDED-BEGIN": "Divided section begins (not at an intersection)", "DIVIDED-END": "Divided section ends (not at an intersection)",
    "ONEWAY-TO-TWOWAY": "One-way street becomes two-way", "MERGE": "Two one-way roadways converge, no added lane",
    "ADDED-LANE": "Two one-way roadways converge with an added lane",
}


def _csv(path):
    with open(path, encoding="utf-8") as fh:
        lines = list(fh)
    notes = [l[1:].strip() for l in lines if l.startswith("#")]
    rows = list(csv.DictReader([l for l in lines if not l.startswith("#")]))
    return notes, rows


def _table(rows, cols, heads=None):
    heads = heads or cols
    out = ["| " + " | ".join(heads) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join(str(r.get(c, "") or "—").replace("|", "/") for c in cols) + " |")
    return "\n".join(out)


def _cond(expr):
    s = str(expr)
    for k in FIELDS:
        s = s.replace(f"t['{k}']", k).replace(f"t.get('{k}')", k)
    return s.replace(" and ", " AND ").replace(" or ", " OR ").replace("not ", "NOT ")


def build(code="mutcd_11e"):
    d = os.path.join(HERE, "rulebooks", code)
    meta = yaml.safe_load(open(os.path.join(d, "code.yaml"), encoding="utf-8"))
    hp = os.path.join(d, "hazards.yaml")
    hz = (yaml.safe_load(open(hp, encoding="utf-8")) or {}).get("hazards", {}) if os.path.exists(hp) else {}
    for k, v in hz.items():
        TRIGGERS.setdefault("HAZ-" + k.upper(), f"Hazard point `type: {k}`: {v.get('label', k)}")
    rules = yaml.safe_load(open(os.path.join(d, "rules.yaml"), encoding="utf-8"))["rules"]
    _, devs = _csv(os.path.join(d, "devices.csv"))
    dev = {r["code"]: r for r in devs}
    mnotes, marks = _csv(os.path.join(d, "markings.csv"))
    L = []
    L.append(f"# Rule book: {meta['name']}")
    L.append("")
    L.append(f"T&I Transportation Systems, road signing skill. Generated {date.today():%d %b %Y} from `rulebooks/{code}/`. "
             f"Rulebook status: **{meta.get('status')}** (results are DRAFT until a T&I engineer signs it off).")
    L.append("")
    L.append("## 1. How to read this rule book")
    L.append("")
    L.append("Every device the skill places comes from one rule below. A rule fires on a *trigger* found in the road network, "
             "checks its *conditions*, and gets a class from the MUTCD wording:")
    L.append("")
    L.append(_table([{"w": "Standard (\"shall\")", "c": "Mandatory"}, {"w": "Guidance (\"should\")", "c": "Recommended"},
                     {"w": "Option (\"may\")", "c": "Optional"}, {"w": "Study (engineering study decides)", "c": "Conditional"}],
                    ["w", "c"], ["MUTCD wording", "Class in the skill"]))
    L.append("")
    L.append("Speed conditions are in km/h, converted AASHTO-style (a 5 mph step = 10 km/h; 30 mph = 50 km/h; 45 mph = 70 km/h). "
             "Where a rule lists several conditions, the first one that is true sets the class.")
    L.append("")
    L.append("Condition names: " + "; ".join(f"`{k}` = {v}" for k, v in FIELDS.items()) + ".")
    L.append("")
    # ---- rules grouped by trigger
    L.append("## 2. Rules by trigger")
    L.append("")
    order = []
    for r in rules:
        for tg in (r["trigger"] if isinstance(r["trigger"], list) else [r["trigger"]]):
            if tg not in order:
                order.append(tg)
    for tg in order:
        L.append(f"### {TRIGGERS.get(tg, tg)} (`{tg}`)")
        L.append("")
        for r in rules:
            tgs = r["trigger"] if isinstance(r["trigger"], list) else [r["trigger"]]
            if tgs[0] != tg:
                continue
            dv = r["device"]
            name = dev.get(dv, {}).get("official_name") or next((m["name"] for m in marks if m["code"] == dv), "")
            if r["trigger"] == "SIGN-REQUEST":
                dv, name = "any code", "Any MUTCD sign placed by the designer (`type: sign`, `code`)"
            elif str(dv).startswith("{") and "warn_symbol" in str(dv):
                dv, name = "W2-1 / W2-2 / W2-4", "Cross Road / Side Road / T-Intersection (chosen from the junction layout)"
            elif str(dv).startswith("{") and "curve_sign" in str(dv):
                dv, name = "W1-1 / W1-2 / W1-3 / W1-4", "Turn / Curve / Reverse Turn / Reverse Curve (chosen from geometry)"
            elif str(dv).startswith("{"):
                import re as _re
                cs = _re.findall(r"'([A-Z]+\d+-\d+[A-Za-z]*)'", str(dv))
                dv, name = " / ".join(reversed(cs)), " / ".join(dev.get(c, {}).get("official_name", "") for c in reversed(cs)) + " (chosen from the point data)"
            pic = dev.get(str(dv), {}).get("symbol")
            L.append(f"**{dv} {name}** · rule `{r['id']}`" + (f" · also fires on {', '.join(tgs[1:])}" if len(tgs) > 1 else ""))
            L.append("")
            if pic:
                L.append(f"![{dv}]({pic})")
                L.append("")
            if str(r["provision"]).startswith("{"):
                L.append("- Default class: from the sign's own MUTCD paragraph (sign catalog default class)")
            else:
                L.append(f"- Default class: **{CLASS_OF[r['provision']]}** ({r['provision']})")
            if r.get("when"):
                L.append(f"- Applies when: `{_cond(r['when'])}`")
            for alt in r.get("provision_if") or []:
                L.append(f"- If `{_cond(alt['when'])}` → **{CLASS_OF[alt['provision']]}** ({alt['provision']})")
            pl = r.get("placement") or {}
            if pl:
                L.append("- Placement: " + ", ".join(f"{k} = {v}" for k, v in pl.items()))
            for c in r.get("companions") or []:
                if isinstance(c, str):
                    L.append(f"- Plaque on the same post: {c} (same class as the sign)")
                else:
                    s = f"- Plaque on the same post: **{c['device']}**, default {CLASS_OF[c.get('provision', r['provision'])]}"
                    for alt in c.get("provision_if") or []:
                        s += f"; if `{_cond(alt['when'])}` → {CLASS_OF[alt['provision']]}"
                    L.append(s + (f" ({c['clause']})" if c.get("clause") else ""))
            if r.get("study"):
                L.append(f"- Study that decides it: {r['study']}")
            L.append(f"- MUTCD: {r.get('clause', '')}")
            L.append(f"- Clause wording checked against the manual text: {'yes' if not r.get('verify', True) else 'not yet (sizes and tables it uses are verified)'}")
            L.append("")
    if hz:
        L.append("### Hazard point types")
        L.append("")
        L.append("Mark a hazard as a point with `type` set to one of these; the engine asks for any listed attribute that is missing. "
                 "Advance distance: Table 2C-3 Condition B, using the point's `advisory_kmh` column when given, otherwise the 0 mph "
                 "(potential stop) column.")
        L.append("")
        L.append("| type | What it marks | Direction | Attributes the engine asks for |")
        L.append("|---|---|---|---|")
        for k, v in hz.items():
            L.append(f"| `{k}` | {v.get('label', '')} | {'ask (fwd/rev/both)' if v.get('facing') == 'ask' else 'both'} | "
                     + ("; ".join(f"`{a}`" for a in (v.get('props') or {})) or "—") + " |")
        L.append("")
    # ---- sign catalog
    L.append("## 3. Sign catalog")
    L.append("")
    L.append("Sizes in inches (width x height) by road type, from MUTCD Tables 2B-1, 2C-1 and 7B-1. Pictures from the manual's figures.")
    L.append("")
    L.append("| Sign | Code | Official name | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Source |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in devs:
        pic = f"![{r['code']}]({r['symbol']})" if r.get("symbol") else ""
        L.append("| " + " | ".join([pic, r["code"], r["official_name"]] + [r.get(k) or "—" for k in
                 ("conv_single", "conv_multi", "expressway", "freeway", "minimum", "oversized")] +
                 [(r.get("size_source") or "") + ("; picture: " + r["symbol_source"] if r.get("symbol_source") else "")]) + " |")
    L.append("")
    # ---- markings
    L.append("## 4. Pavement markings")
    L.append("")
    L.append(_table(marks, ["code", "name", "color", "pattern", "width_in", "unit", "clause"],
                    ["Code", "Name", "Colour", "Pattern", "Width (in)", "Unit", "MUTCD"]))
    L.append("")
    L.append("> " + " ".join(mnotes[1:]) if len(mnotes) > 1 else "")
    L.append("")
    # ---- tables
    L.append("## 5. Tables used by the engine")
    L.append("")
    tdir = os.path.join(d, "tables")
    titles = {"advance_placement.csv": "Table 2C-3 Advance placement of warning signs (feet; speeds mph)",
              "curve_devices.csv": "Table 2C-4 Chart B Devices by speed differential",
              "chevron_spacing.csv": "Table 2C-5 Chevron spacing",
              "mounting.csv": "Mounting height and lateral offset (2A.15 / 2A.16)",
              "passing_sight.csv": "Table 3B-1 Minimum passing sight distance"}
    for fn in ["advance_placement.csv", "curve_devices.csv", "chevron_spacing.csv", "mounting.csv", "passing_sight.csv"]:
        notes, rows = _csv(os.path.join(tdir, fn))
        L.append(f"### {titles[fn]}")
        L.append("")
        if rows:
            L.append(_table(rows, list(rows[0].keys())))
        L.append("")
        for n in notes:
            L.append(f"> {n}")
        L.append("")
    L.append("Table 2C-4 Chart A (need for curve devices) is applied in code: freeways/expressways Required; arterial or collector "
             "under 1,000 AADT Optional, 1,000-2,999 Recommended, 3,000-3,999 Required without markings / Recommended with markings, "
             "4,000+ Required; all other roads Optional. Table 2C-6 (Advisory Speed plaque) is applied through the W13-1P plaque rule.")
    L.append("")
    # ---- status
    L.append("## 6. Verification status")
    L.append("")
    L.append(str(meta.get("notes", "")).strip())
    L.append("")
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", default="mutcd_11e")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    open(a.out, "w", encoding="utf-8").write(build(a.code))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
