"""Extract the review page's data from DXF files and the rulebook (writes data.json).

  python dashboard/extract_data.py --network-dxf Wyte.dxf --signing-dxf Wyte_Signing_1.dxf --out dashboard/data.json

--network-dxf   the input drawing: centreline, kerb, parking and building layers (defaults are the Wyte layer names)
--signing-dxf   the engine's signing drawing: sign blocks on one layer, a label beside each sign on another
Run from the project folder. Needs ezdxf and the engine package (see SKILL.md).
"""
import argparse, csv, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import ezdxf
from ezdxf import path as ezpath
from engine import adapters, signs_master as sm
from engine.rulebook import Rulebook

r1 = lambda v: round(float(v), 1)


def dp(pts, tol):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]; dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1e-9; md, mi = 0, 0
    for i in range(1, len(pts) - 1):
        dd = abs((pts[i][0] - a[0]) * dy - (pts[i][1] - a[1]) * dx) / L
        if dd > md: md, mi = dd, i
    return dp(pts[:mi + 1], tol)[:-1] + dp(pts[mi:], tol) if md > tol else [a, b]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--network-dxf", required=True); ap.add_argument("--signing-dxf", required=True)
    ap.add_argument("--out", default=os.path.join(HERE, "data.json"))
    ap.add_argument("--centreline", default="TI - CL"); ap.add_argument("--kerb", default="TI - CW")
    ap.add_argument("--parking", default="TI - Parking"); ap.add_argument("--buildings", default="TI - BM")
    ap.add_argument("--sign-layer", default="TI-Signs"); ap.add_argument("--label-layer", default="TI-Text")
    ap.add_argument("--label-regex", default=r"^[A-Z]\d+(-\d+[A-Za-z]*)? S\d+$")
    a = ap.parse_args()
    net = adapters.load(a.network_dxf, layers=[a.centreline], tee_tol=12.0); names = net.link_names()
    nodes = {n.id: {"l": net.node_label(n.id), "x": r1(n.xy[0]), "y": r1(n.xy[1]), "d": n.degree} for n in net.nodes.values()}
    links = [{"id": l.id, "n": names[l.id], "a": l.a, "b": l.b, "p": [[r1(x), r1(y)] for x, y in l.coords]} for l in net.links.values()]
    msp = ezdxf.readfile(a.network_dxf).modelspace()

    def layer_polys(name):
        out = []
        for e in msp:
            if e.dxf.layer != name or e.dxftype() not in ("LINE", "LWPOLYLINE", "ARC", "POLYLINE"): continue
            try: pts = [(v.x, v.y) for v in ezpath.make_path(e).flattening(0.25)]
            except Exception: continue
            pts = dp(pts, 0.12)
            if len(pts) > 1: out.append([[r1(x), r1(y)] for x, y in pts])
        return out
    sg = ezdxf.readfile(a.signing_dxf).modelspace()
    rx = re.compile(a.label_regex)
    data = {"file": os.path.basename(a.signing_dxf), "nodes": nodes, "links": links, "kerb": layer_polys(a.kerb), "park": layer_polys(a.parking),
            "bm": [[r1(e.dxf.insert.x), r1(e.dxf.insert.y)] for e in msp.query("INSERT") if e.dxf.layer == a.buildings],
            "ins": [[e.dxf.name, r1(e.dxf.insert.x), r1(e.dxf.insert.y), round(e.dxf.rotation, 1)] for e in sg.query("INSERT") if e.dxf.layer == a.sign_layer],
            "lab": [[e.dxf.text.strip(), r1(e.dxf.insert.x), r1(e.dxf.insert.y)] for e in sg.query("TEXT") if e.dxf.layer == a.label_layer and rx.match(e.dxf.text.strip())]}
    sec = {}
    try:
        with open(os.path.join(ROOT, "rulebooks", "mutcd_11e", "sign_catalog.json"), encoding="utf-8") as fh:
            sec = {k: v.get("section", "") for k, v in json.load(fh).items()}
    except OSError: pass
    mut, egy = sm.load_catalog("mutcd_11e"), sm.load_catalog("egypt")
    data["cat"] = [[c, r["official_name"], r["family"], sec.get(c, ""), r.get("shape", "")] for c, r in mut.items()]
    data["egy"] = [[c, r["ti_blocks"]] for c, r in egy.items()]
    data["mlinks"] = [[r["master_id"], r["mutcd_code"], r["when"], r["egypt_code"], r["shc_code"], r["ti_block"], r["match"], r["approved"], r["approved_by"], r["note"]] for r in sm.load_links()]
    with open(os.path.join(ROOT, "styles", "ti_details", "block_map.csv"), encoding="utf-8") as fh:
        data["bmap"] = [[r["mutcd_code"], r["when"], r["block"]] for r in csv.DictReader(l for l in fh if not l.startswith("#")) if r["approved"].lower() == "yes"]
    rb = Rulebook("mutcd_11e"); data["rb"] = {"code": "mutcd_11e", "status": rb.meta.get("status"), "name": rb.meta.get("name")}
    with open(a.out, "w", encoding="utf-8") as fh: json.dump(data, fh, separators=(",", ":"), ensure_ascii=False)
    print("wrote", a.out, len(data["ins"]), "signs,", len(data["lab"]), "labels,", len(links), "links")


if __name__ == "__main__":
    main()
