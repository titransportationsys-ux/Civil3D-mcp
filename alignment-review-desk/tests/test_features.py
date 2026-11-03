"""Checks for the v1.9 additions: DRAFT file names, sign-indicator symbol, schedule table, layer-count re-read,
junction numbering, project workbook.  python tests/test_features.py"""
import json, math, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from engine import adapters, project


def _run(*a):
    return subprocess.run([sys.executable, "-m", "engine.run", *a], cwd=ROOT, capture_output=True, text=True)


def _rural(extra_ov=None, extra_args=()):
    out = tempfile.mkdtemp()
    ov = json.load(open(os.path.join(HERE, "overrides_rural_dxf.json")))
    ov.update(extra_ov or {})
    ovp = os.path.join(out, "ov.json")
    json.dump(ov, open(ovp, "w"))
    r = _run("--input", "tests/networks/rural_highway.dxf", "--layers", "C-ROAD-CL", "--settings", "tests/settings_default.json",
             "--overrides", ovp, "--out", out, *extra_args)
    assert r.returncode == 0, r.stdout + r.stderr
    return out, r


def test_draft_names():
    out, _ = _rural()
    names = os.listdir(out)
    for n in names:
        if n.startswith("rural_highway"):
            assert "_DRAFT_" in n, n


def test_indicator_and_table():
    import ezdxf
    j = [{"id": "J01", "type": "roundabout", "control": "roundabout", "plan": "plain words", "e": 100.0, "n": 200.0},
         {"id": "D01", "type": "cul-de-sac", "control": "none", "e": 150.0, "n": 50.0}]
    out, _ = _rural({"junctions": j, "schedule_table_origin": [5000, 6000]})
    doc = ezdxf.readfile(os.path.join(out, "rural_highway_DRAFT_Signing.dxf"))
    msp = doc.modelspace()
    circ = [c for c in msp.query("CIRCLE") if c.dxf.layer == "TI-Signs" and abs(c.dxf.radius - 0.6) < 1e-9]
    assert {(round(c.dxf.center.x, 3), round(c.dxf.center.y, 3)) for c in circ} == {(100.0, 201.2), (150.0, 51.2)}
    title = [t for t in msp.query("TEXT") if "JUNCTION AND DEAD-END SCHEDULE (DRAFT)" in t.dxf.text]
    assert len(title) == 1 and abs(title[0].dxf.height - 2.6) < 1e-9
    cells = [t for t in msp.query("TEXT") if t.dxf.layer == "TI-Text" and abs(t.dxf.height - 2.0) < 1e-9
             and t.dxf.insert.x >= 5000 and 5000 < t.dxf.insert.y < 6001]
    assert {"No.", "Type", "Control / plan", "E", "N", "J01", "D01"} <= {t.dxf.text for t in cells}
    assert not doc.audit().has_errors


def test_no_junctions_no_extras():
    import ezdxf
    out, _ = _rural()
    msp = ezdxf.readfile(os.path.join(out, "rural_highway_DRAFT_Signing.dxf")).modelspace()
    assert not [t for t in msp.query("TEXT") if "SCHEDULE (DRAFT)" in t.dxf.text]


def test_layer_counts_compare():
    out, _ = _rural()
    snap = os.path.join(out, "layer_counts.json")
    assert os.path.exists(snap)
    out2 = tempfile.mkdtemp()
    old = json.load(open(snap))
    lay = next(iter(old))
    t = next(iter(old[lay]))
    old[lay][t] += 1
    p = os.path.join(out2, "old.json")
    json.dump(old, open(p, "w"))
    _, r = _rural(extra_args=("--compare-counts", p))
    assert "INPUT CHANGED" in r.stdout and lay in r.stdout
    assert adapters.compare_counts(json.load(open(snap)), json.load(open(snap))) == []


def test_numbering():
    items = [{"type": "cul-de-sac", "e": 0, "n": 5}, {"type": "T-junction", "e": 0, "n": 10}, {"type": "roundabout", "e": 0, "n": 1},
             {"type": "T-junction", "e": 0, "n": 30}, {"type": "hammerhead dead end", "e": 0, "n": 50}]
    got = [(i["id"], i["type"], i["n"]) for i in project.number_junctions(items)]
    assert got == [("J01", "roundabout", 1), ("J02", "T-junction", 30), ("J03", "T-junction", 10),
                   ("D01", "hammerhead dead end", 50), ("D02", "cul-de-sac", 5)]


def test_workbook():
    import openpyxl
    d = tempfile.mkdtemp()
    p = project.new_project(d, "TL00", "Wyte")
    assert "DRAFT" in os.path.basename(p)
    wb = openpyxl.load_workbook(p)
    assert wb.sheetnames == ["Settings", "Inputs", "Questions", "Junctions", "Runs", "Rulebook"]
    assert all("DRAFT" in wb[s]["A1"].value and "ا" in wb[s]["A2"].value for s in wb.sheetnames)
    assert set(os.listdir(os.path.join(d, "TL00_Wyte"))) == set(project.SUBDIRS)


def test_link_names():
    from engine import adapters
    from engine.data import apply_overrides
    net = adapters.load(os.path.join(HERE, "networks", "urban_grid.geojson"))
    names = net.link_names()
    assert all("-" in n for n in names.values()) and len(set(names.values())) == len(names)
    lid = next(iter(net.links))
    assert net.resolve_link(names[lid]) == lid and net.resolve_link(lid) == lid
    a, b = net.links[lid].a, net.links[lid].b
    assert net.resolve_link(f"{net.node_label(b)}-{net.node_label(a)}".lower()) in (lid, None)
    apply_overrides(net, {"links": {names[lid]: {"class": "collector"}}}, {})
    assert net.links[lid].props["class"] == "collector"


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
            print("ok", n)
