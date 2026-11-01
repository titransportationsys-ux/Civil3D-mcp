"""Regression checks: python -m pytest tests -q   (or python tests/test_engine.py)"""
import json, math, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from engine.rulebook import Rulebook
from engine.triggers import detect_curves, advisory_mph

rb = Rulebook("mutcd_11e")

def test_advance_table():
    d, _ = rb.advance_distance_m(88.5, "A")            # 55 mph -> 990 ft
    assert abs(d - 990 * 0.3048) < 0.1
    d, _ = rb.advance_distance_m(64.4, "B", 0)         # 40 mph, stop -> 305 ft
    assert abs(d - 305 * 0.3048) < 0.1
    d, n = rb.advance_distance_m(48.3, "B", 20)        # 30 mph, 20 mph advisory -> N/A -> 100 ft
    assert abs(d - 30.48) < 0.1 and "N/A" in n
    d, _ = rb.advance_distance_m(60, "B", 0)           # 37.3 mph rounds UP to 40 mph row (conservative)
    assert abs(d - 305 * 0.3048) < 0.1

def test_sizes_and_mount():
    assert rb.size("R1-1", "conv_single") == "30x30"
    assert rb.size("R1-1", "conv_multi") == "36x36"
    assert rb.mount("rural")["height_m"] == round(5 * 0.3048, 2)
    assert rb.mount("urban")["height_m"] == round(7 * 0.3048, 2)

def test_curve_detection():
    arc = [(150 * math.cos(math.radians(-90 + 80 * k / 24)), 150 + 150 * math.sin(math.radians(-90 + 80 * k / 24))) for k in range(25)]
    pts = [(-600, 0)] + arc + [(arc[-1][0] + 100 * math.cos(math.radians(80)), arc[-1][1] + 100 * math.sin(math.radians(80)))]
    cs = detect_curves(pts)
    assert len(cs) == 1 and abs(cs[0].radius - 150) / 150 < 0.05 and cs[0].delta > 0

def test_advisory():
    assert advisory_mph(150, 0.06, 56) == 35   # sqrt(15*492*0.21)=39.4 -> 35
    assert advisory_mph(1000, 0.06, 56) == 55

def _run(*a):
    return subprocess.run([sys.executable, "-m", "engine.run", *a], cwd=ROOT, capture_output=True, text=True)

def test_urban_end_to_end():
    out = tempfile.mkdtemp()
    r = _run("--input", "tests/networks/urban_grid.geojson", "--settings", "tests/settings_default.json", "--out", out)
    assert r.returncode == 0, r.stdout + r.stderr
    fc = json.load(open(os.path.join(out, "urban_grid_DRAFT_Signs.geojson")))
    signs = [f["properties"] for f in fc["features"] if f["properties"]["kind"] == "sign"]
    stops = [s for s in signs if s["code"] == "R1-1" and s["cls"] == "Mandatory"]
    assert len([s for s in stops if s["node"] == "INT-5"]) == 3            # all-way stop, 3 legs
    assert all(s["code"] != "R1-1" or s["node"] != "INT-1" for s in signs)  # none at the signal
    assert any(s["code"] == "R1-2" and s["node"] == "INT-7" for s in signs)
    assert sum(1 for s in signs if s["code"] == "R5-1") == 4
    assert any(s["code"] == "R2-1" and s["legend"] == "SPEED LIMIT 80 km/h" for s in signs)
    assert all(s["clause"] for s in signs)

def test_missing_data_stops():
    out = tempfile.mkdtemp()
    r = _run("--input", "tests/networks/rural_highway.dxf", "--layers", "C-ROAD-CL", "--settings", "tests/settings_default.json", "--out", out)
    assert r.returncode == 2
    qs = json.load(open(os.path.join(out, "questions.json")))
    assert {q["id"] for q in qs} >= {"eng-speed_kmh", "eng-class", "eng-control"}

if __name__ == "__main__":
    for k, v in list(globals().items()):
        if k.startswith("test_"):
            v(); print("ok", k)
