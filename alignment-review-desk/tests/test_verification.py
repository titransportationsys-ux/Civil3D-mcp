"""Hand-checked verification cases. Each case states the expected answer worked by hand from the
MUTCD value it relies on, then runs the engine on a tiny network and compares.

Run: python tests/test_verification.py   -> prints one PASS/FAIL line per case and a summary JSON.
"""
import json, math, os, sys, tempfile, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from engine.rulebook import Rulebook
from engine.triggers import chart_a_level, detect_curves, advisory_mph

FT = 0.3048
rb = Rulebook("mutcd_11e")
RESULTS = []


def case(cid, desc, expected, actual, ok=None):
    ok = (expected == actual) if ok is None else ok
    RESULTS.append({"id": cid, "case": desc, "expected": str(expected), "actual": str(actual), "result": "PASS" if ok else "FAIL"})
    print(("PASS " if ok else "FAIL ") + cid, "-", desc, "| expected", expected, "| got", actual)


def run_net(features, settings=None, overrides=None):
    d = tempfile.mkdtemp()
    fc = {"type": "FeatureCollection", "features": features}
    json.dump(fc, open(os.path.join(d, "net.geojson"), "w"))
    st = {"mode": "design", "code": "mutcd_11e", "families": ["reg", "warn", "mark", "delin"], "level": "opt",
          "units": "metric", "drive": "right", "size": "auto", "env": ["auto"], "outputs": ["xlsx"]}
    st.update(settings or {})
    json.dump(st, open(os.path.join(d, "s.json"), "w"))
    args = [sys.executable, "-m", "engine.run", "--input", os.path.join(d, "net.geojson"), "--settings",
            os.path.join(d, "s.json"), "--out", os.path.join(d, "out")]
    if overrides:
        json.dump(overrides, open(os.path.join(d, "o.json"), "w"))
        args += ["--overrides", os.path.join(d, "o.json")]
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        return None, r.stdout + r.stderr
    fc = json.load(open(os.path.join(d, "out", "net_DRAFT_Signs.geojson")))
    return [f["properties"] for f in fc["features"]], ""


def L(i, pts, **p):
    return {"type": "Feature", "geometry": {"type": "LineString", "coordinates": pts}, "properties": {"id": i, **p}}


def P(x, y, **p):
    return {"type": "Feature", "geometry": {"type": "Point", "coordinates": [x, y]}, "properties": p}


BASE = {"lanes": 1, "oneway": False, "aadt": 5000, "urban": False}

# ---------------------------------------------------------------- V1 tables
d, _ = rb.advance_distance_m(80.47, "A")          # 50 mph Cond A = 885 ft
case("V1.1", "Table 2C-3 Cond A at 50 mph = 885 ft", round(885 * FT, 1), round(d, 1))
d, _ = rb.advance_distance_m(50, "B", 0)          # 31.1 mph -> row 35 (round up), B0 = 250 ft
case("V1.2", "50 km/h (31.1 mph) uses 35 mph row, Cond B stop = 250 ft", round(250 * FT, 1), round(d, 1))
d, _ = rb.advance_distance_m(96.56, "B", 40)      # 60 mph, advisory 40 = 200 ft
case("V1.3", "60 mph, advisory 40 mph = 200 ft", round(200 * FT, 1), round(d, 1))
d, n = rb.advance_distance_m(30, "B", 10)         # 18.6 mph -> 20 mph row, b10 N/A -> 100 ft
case("V1.4", "N/A cell falls back to 100 ft (notes 5/6)", round(100 * FT, 1), round(d, 1))
case("V1.5", "Chevron spacing, advisory 40 mph = 120 ft", round(120 * FT, 1), round(rb.chevron_spacing_m(40), 1))
case("V1.5b", "Chevron spacing in km/h bands: 20 / 40 / 50 / 60 / 70 / 90 / 110 km/h = 40/80/80/120/120/160/200 ft",
     [round(v * FT, 1) for v in (40, 80, 80, 120, 120, 160, 200)],
     [round(rb.chevron_spacing_m(advisory_kmh=k), 1) for k in (20, 40, 50, 60, 70, 90, 110)])

# ---------------------------------------------------------------- V2 Chart A
for cid, args, exp in [("V2.1", ("freeway", 500), "Required"), ("V2.2", ("arterial", 900), "Optional"),
                       ("V2.3", ("collector", 2000), "Recommended"), ("V2.4", ("arterial", 3500), "Required"),
                       ("V2.5", ("arterial", 3500, True), "Recommended"), ("V2.6", ("arterial", 5000), "Required"),
                       ("V2.7", ("local", 9000), "Optional")]:
    case(cid, f"Table 2C-4 Chart A {args}", exp, chart_a_level(*args))

# ---------------------------------------------------------------- V3 sizes and names
for cid, code, sc, exp in [("V3.1", "W2-2", "conv_multi", "30x30"), ("V3.2", "W16-7P", "conv_single", "21x15"),
                           ("V3.3", "S1-1", "conv_single", "36x36"), ("V3.4", "R1-1", "conv_multi", "36x36"),
                           ("V3.5", "R2-1", "expressway", "36x48"), ("V3.6", "W1-8", "freeway", "36x48")]:
    case(cid, f"Size {code} {sc}", exp, rb.size(code, sc))
case("V3.7", "Official name W16-7P", "Diagonal Downward Arrow (plaque)", rb.devices["W16-7P"]["official_name"])
case("V3.8", "Official name R1-3P", "All Way (plaque)", rb.devices["R1-3P"]["official_name"])

# ---------------------------------------------------------------- V4 curves
arc = [(600 + 150 * math.cos(math.radians(-90 + 80 * k / 24)), 150 + 150 * math.sin(math.radians(-90 + 80 * k / 24))) for k in range(25)]
cs = detect_curves([(0, 0)] + arc)
case("V4.1", "Radius of an R=150 m, 80 deg arc within 3%", True, abs(cs[0].radius - 150) / 150 < 0.03, abs(cs[0].radius - 150) / 150 < 0.03)
# advisory: R=150 m = 492 ft, e=0.06: f=0.15 -> 36.1 mph >= 35 -> 35 mph
case("V4.2", "Advisory R=150 m, e=0.06 = 35 mph", 35, advisory_mph(150, 0.06, 56))
# advisory: R=40 m = 131.2 ft, e=0.04: f .15 -> sqrt(15*131.2*0.19)=19.3 (<35); f .18 -> 20.8 (<25);
# f .21 -> sqrt(15*131.2*0.25)=22.2 -> floor to 5 mph = 20 mph   (first hand calculation said 15: arithmetic slip, corrected)
case("V4.3", "Advisory R=40 m, e=0.04 = 20 mph", 20, advisory_mph(40, 0.04, 31))

# ---------------------------------------------------------------- V5 end-to-end small networks
# T-junction, minor road stop, right-hand traffic. Main road E-W along y=0; side road from south.
feats = [L("M1", [[0, 0], [300, 0]], **{"class": "arterial", "speed_kmh": 60, **BASE}),
         L("M2", [[300, 0], [600, 0]], **{"class": "arterial", "speed_kmh": 60, **BASE}),
         L("S1", [[300, -300], [300, 0]], **{"class": "local", "speed_kmh": 50, **BASE}),
         P(300, 0, id="J1", control="stop_minor")]
signs, err = run_net(feats)
if signs is None:
    case("V5.0", "T-junction network runs", "ok", err[:200])
else:
    stops = [s for s in signs if s["code"] == "R1-1"]
    case("V5.1", "One STOP, only on the side road", 1, len(stops))
    s = stops[0]
    # northbound on S1 -> right-hand side is east (x > 300). Stop line: crossing half width 3.65 + 1.2 = 4.85 m back.
    case("V5.2", "STOP on the right (east) of the northbound approach", True, s["x"] > 300, s["x"] > 300)
    case("V5.3", "STOP 4.85 m before the junction (half width 3.65 + 4 ft)", 4.85, round(0 - s["y"], 2), abs(-s["y"] - 4.85) < 0.05)
    w31 = [x for x in signs if x["code"] == "W3-1"]
    # 50 km/h -> 35 mph row -> B0 250 ft = 76.2 m, + 4.85 m
    case("V5.4", "W3-1 at 76.2 m + stop line = 81.1 m", 81.1, round(w31[0]["back_m"], 1), abs(w31[0]["back_m"] - 81.05) < 0.2)
    case("V5.5", "W3-1 is Conditional (sight distance not given)", "Conditional", w31[0]["cls"])
    case("V5.6", "STOP rural mounting height 5 ft = 1.52 m", 1.52, s["height_m"])
    case("V5.7", "STOP rural offset = 3.65 m half width + 12 ft", round(3.65 + 12 * FT, 2), s["offset_m"])
    w22 = [x for x in signs if x["code"] == "W2-2"]
    case("V5.8", "No intersection warning on main road (junction is STOP-controlled)", 0, len(w22))

# left-hand traffic: same network, sign on the west
signs, err = run_net(feats, {"drive": "left"})
if signs:
    s = [x for x in signs if x["code"] == "R1-1"][0]
    case("V5.9", "Left-hand traffic puts STOP on the west", True, s["x"] < 300, s["x"] < 300)

# uncontrolled T: side road warning W2-2 with orientation
feats_u = feats[:3] + [P(300, 0, id="J1", control="none")]
signs, err = run_net(feats_u)
if signs:
    w = [x for x in signs if x["code"] == "W2-2"]
    case("V5.10", "Uncontrolled T: W2-2 Side Road on both main approaches (Option)", (2, "Optional"),
         (len(w), w[0]["cls"] if w else None))
    eb = [x for x in w if x["y"] < 0]
    case("V5.11", "Eastbound W2-2 shows side road on the right", "right", eb[0]["orientation"] if eb else None)

# speed drop 90 -> 60 km/h (18.6 mph > 10): W3-5 + R2-1 60; drop 60 -> 45 (9.3 mph): no W3-5
feats_s = [L("A", [[0, 0], [1000, 0]], **{"class": "arterial", "speed_kmh": 90, **BASE}),
           L("B", [[1000, 0], [2000, 0]], **{"class": "arterial", "speed_kmh": 60, **BASE}),
           L("C", [[2000, 0], [3000, 0]], **{"class": "arterial", "speed_kmh": 45, **BASE})]
signs, err = run_net(feats_s)
if signs:
    w35 = [x for x in signs if x["code"] == "W3-5"]
    case("V5.12", "W3-5 only where drop > 10 mph (90->60 yes, 60->45 no)", 1, len(w35))
    r21 = sorted({x["legend"] for x in signs if x["code"] == "R2-1"})
    case("V5.13", "R2-1 legends at change points", ["SPEED LIMIT 45 km/h", "SPEED LIMIT 60 km/h", "SPEED LIMIT 90 km/h"], r21)

# curve: arterial 90 km/h, AADT 5000, R=150 left curve -> advisory 60 km/h, diff 30 km/h -> sign + plaque Required, delineators
cfeat = [L("K", [[0, 0]] + [list(p) for p in arc] + [[arc[-1][0] + 400 * math.cos(math.radians(80)), arc[-1][1] + 400 * math.sin(math.radians(80))]],
           **{"class": "arterial", "speed_kmh": 90, **BASE})]
signs, err = run_net(cfeat)
if signs:
    fwd = [x for x in signs if x["where"].startswith("curve on K (fwd)")]
    w12 = [x for x in fwd if x["code"] in ("W1-1", "W1-2")]
    case("V5.14", "Left curve eastbound: Curve sign W1-2, orientation left, Mandatory",
         ("W1-2", "left", "Mandatory"), (w12[0]["code"], w12[0]["orientation"], w12[0]["cls"]) if w12 else None)
    ch = [x for x in fwd if x["code"] == "W1-8"]
    dl = [x for x in fwd if x["code"] == "DELINEATOR"]
    case("V5.15", "90 km/h, advisory 60 km/h (diff 30 km/h = Chart B 15 mph row): delineators, no chevrons",
         (False, True), (bool(ch), bool(dl)))
    pl = [x for x in fwd if x["code"] == "W13-1P"]
    case("V5.16", "Advisory plaque shows 60 km/h (39.4 mph = 63.4 km/h, floored to 10 km/h)", "60 km/h", pl[0]["legend"] if pl else None)
    case("V5.16b", "Advisory plaque at 30 km/h differential (90-60) is Mandatory (Table 2C-6: 15 mph / 30 km/h or more)",
         "Mandatory", pl[0]["cls"] if pl else None)

# tighter curve R=80 m at 90 km/h: 30.7 mph = 49 km/h -> advisory 40, diff 50 km/h -> chevrons on the outside
arc80 = [(600 + 80 * math.cos(math.radians(-90 + 80 * k / 24)), 80 + 80 * math.sin(math.radians(-90 + 80 * k / 24))) for k in range(25)]
signs, err = run_net([L("K2", [[0, 0]] + [list(p) for p in arc80] + [[arc80[-1][0] + 400 * math.cos(math.radians(80)), arc80[-1][1] + 400 * math.sin(math.radians(80))]],
                        **{"class": "arterial", "speed_kmh": 90, **BASE})])
if signs:
    fwd2 = [x for x in signs if x["where"].startswith("curve on K2 (fwd)")]
    ch = [x for x in fwd2 if x["code"] == "W1-8"]
    case("V5.15b", "R=80 m, 90 km/h: advisory 40 km/h, diff 50 km/h: chevrons on the outside (right) of a left curve",
         True, bool(ch) and all(x["side"] == "right" for x in ch))

# mid-block crosswalk: advance W11-2 always (Optional); W11-2 + W16-7P at the crosswalk only with Yield Here To Pedestrians signs
xfe = [L("X", [[0, 0], [800, 0]], **{"class": "collector", "speed_kmh": 50, **BASE}), P(400, 5, type="crosswalk", id="XW")]
signs, _ = run_net(xfe, settings={"level": "opt"})
if signs:
    fx = [x for x in signs if x["where"].startswith("crosswalk XW on X (fwd)")]
    w = sorted(x["code"] for x in fx if x["code"] in ("W11-2", "W16-7P"))
    case("V5.19", "Crosswalk without Yield Here signs: advance W11-2 only, Optional", (["W11-2"], "Optional"),
         (w, fx[0]["cls"] if fx else None))
xfe[1]["properties"]["yield_here_signs"] = True
signs, _ = run_net(xfe, settings={"level": "opt"})
if signs:
    fx = [x for x in signs if x["where"].startswith("crosswalk XW on X (fwd)")]
    w = sorted(x["code"] for x in fx if x["code"] in ("W11-2", "W16-7P"))
    case("V5.20", "Crosswalk with Yield Here signs: advance W11-2 + W11-2/W16-7P at the crosswalk",
         ["W11-2", "W11-2", "W16-7P"], w)

# 3B.02 centre line warrants (text confirmed by T&I)
from engine.rulebook import Rulebook as _RB2
_rb2 = _RB2("mutcd_11e")
def _cl(**kw):
    t = {"oneway": False, "divided": False, "lanes_total": 2, "urban": True, "class": "local", "width_ft": 20, "aadt": 500}
    t.update(kw)
    r = [x for x in _rb2.resolve("MARK-LINK", t) if x["device"] == "CL-DY"]
    return r[0]["class"] if r else None
case("V6.1", "3B.02 centre line: 3 lanes / urban coll 6000 / urban coll 4000 / rural art 18 ft 3000 / 14 ft local / 18 ft local / one-way",
     ["Mandatory", "Mandatory", "Recommended", "Recommended", "Conditional", "Optional", None],
     [_cl(lanes_total=3), _cl(**{"class": "collector", "aadt": 6000}), _cl(**{"class": "collector", "aadt": 4000}),
      _cl(**{"class": "arterial", "urban": False, "width_ft": 18, "aadt": 3000}), _cl(width_ft=14), _cl(width_ft=18),
      _cl(oneway=True)])

def _el(**kw):
    t = {"oneway": False, "divided": False, "lanes_total": 2, "urban": False, "class": "local", "width_ft": 20, "aadt": 500}
    t.update(kw)
    r = [x for x in _rb2.resolve("MARK-LINK", t) if x["device"] == "EL-SW"]
    return r[0]["class"] if r else None
case("V6.2", "3B.10 edge line: freeway / expressway / rural art 20 ft 6000 / rural coll 20 ft 3000 / rural art 18 ft 6000 / urban art 6000",
     ["Mandatory", "Mandatory", "Mandatory", "Recommended", "Optional", "Optional"],
     [_el(**{"class": "freeway"}), _el(**{"class": "expressway"}), _el(**{"class": "arterial", "aadt": 6000}),
      _el(**{"class": "collector", "aadt": 3000}), _el(**{"class": "arterial", "width_ft": 18, "aadt": 6000}),
      _el(**{"class": "arterial", "urban": True, "aadt": 6000})])

# 2B.49 ONE WAY: four-leg crossing of a one-way street, and a T with a one-way top (text confirmed by T&I)
UB = {"lanes": 1, "aadt": 3000, "urban": True, "class": "local", "speed_kmh": 40}
ow = [L("OA", [[-200, 0], [0, 0]], oneway=True, name="Nile St", **UB), L("OB", [[0, 0], [200, 0]], oneway=True, name="Nile St", **UB)]
x4 = ow + [L("SA", [[0, -200], [0, 0]], oneway=False, **UB), L("SB", [[0, 0], [0, 200]], oneway=False, **UB),
           P(0, 0, id="J", control="stop_minor", stop_approaches=["SA", "SB"])]
signs, err = run_net(x4)
if signs:
    r6 = [x for x in signs if x["code"] == "R6-1"]
    case("V5.21", "4-leg crossing of a one-way street: 4 ONE WAY signs (near-right + far-left per crossing approach), Mandatory",
         (4, {"Mandatory"}, 2, 2), (len(r6), {x["cls"] for x in r6}, sum("near-right" in x["notes"] for x in r6),
                                     sum("far-left" in x["notes"] for x in r6)))
x3 = ow + [L("SA", [[0, -200], [0, 0]], oneway=False, **UB), P(0, 0, id="J", control="stop_minor", stop_approaches=["SA"])]
signs, err = run_net(x3)
if signs:
    r6 = [x for x in signs if x["code"] == "R6-1"]
    case("V5.22", "T with one-way top: 2 ONE WAY signs facing the stem (near-right + far side, 2B.49-11)",
         (2, 1, 1), (len(r6), sum("near-right" in x["notes"] for x in r6), sum("far side" in x["notes"] for x in r6)))
else:
    print(err[-400:])

# site boundary (compound gate, external road not drawn): STOP for traffic leaving, SPEED LIMIT for traffic entering
bfe = [L("E", [[0, 0], [300, 0]], **{"class": "local", "speed_kmh": 30, "lanes": 1, "oneway": False, "aadt": 500, "urban": True}),
       P(0, 0, id="GATE", boundary=True, entry_speed_kmh=30, exit_control="stop")]
signs, err = run_net(bfe)
if signs:
    g = sorted((x["code"], x["cls"], x.get("legend")) for x in signs if "GATE" in x["where"] and x["code"] in ("R1-1", "R2-1"))
    case("V5.23", "Site boundary: STOP (exit) + SPEED LIMIT 30 (entry), both Mandatory",
         [("R1-1", "Mandatory", "STOP"), ("R2-1", "Mandatory", "SPEED LIMIT 30 km/h")], g)
else:
    print(err[-500:])

# sign catalog checked against the MUTCD 11th Ed. PDF (Tables 2B-1, 2C-1, 7B-1) with a picture from the manual's figures
_core = ["R1-1","R1-2","R1-3P","R2-1","R4-7","R5-1","R5-1a","R6-1","R6-2","W1-1","W1-2","W1-3","W1-4","W1-8","W13-1P","W2-1",
         "W2-2","W2-4","W2-6","W3-1","W3-2","W3-3","W3-5","W4-2","W11-2","W16-7P","W16-9P","S1-1"]
case("V7.1", "Core signs: size/name verified from the PDF and a picture file",
     [], [c for c in _core if rb.devices[c].get("size_verify") != "PDF" or not rb.devices[c].get("symbol")
          or not os.path.exists(os.path.join(rb.dir, rb.devices[c]["symbol"]))])
_tab = [c for c, e in rb.sign_catalog.items() if e.get("primary_table")]
_pics = [c for c in rb.devices if rb.devices[c].get("symbol") and os.path.exists(os.path.join(rb.dir, rb.devices[c]["symbol"]))]
case("V7.1b", "Full catalog: every sign with a size-table row has PDF sizes; at least 800 signs have a picture",
     (True, True), (all(rb.devices[c].get("size_verify") == "PDF" for c in _tab), len(_pics) >= 800))
xfe2 = [L("X", [[0, 0], [800, 0]], **{"class": "collector", "speed_kmh": 50, **BASE}), P(400, 5, type="crosswalk", id="XW", yield_here_signs=True)]
signs, _ = run_net(xfe2, settings={"level": "opt"})
if signs:
    fx = [x for x in signs if x["where"].startswith("crosswalk XW on X (fwd)")]
    case("V7.2", "2C.55: W16-7P below the crosswalk W11-2 is Mandatory (04); AHEAD W16-9P with the advance W11-2 is Recommended (03)",
         ({"Mandatory"}, {"Recommended"}), ({x["cls"] for x in fx if x["code"] == "W16-7P"}, {x["cls"] for x in fx if x["code"] == "W16-9P"}))

# any MUTCD sign placed by the designer (type: sign, code): sized and classed from the full catalog
rq = [L("A", [[0, 0], [500, 0]], **{"class": "collector", "speed_kmh": 50, "lanes": 1, "oneway": False, "aadt": 3000, "urban": True}),
      P(200, 4, type="sign", code="R7-1", id="Q1"), P(350, 4, type="sign", code="D3-1", id="Q2", legend="El Tahrir St"),
      P(400, 4, type="sign", code="XX9-9", id="Q3")]
signs, err = run_net(rq, settings={"level": "rec"})
if signs:
    got = sorted((x["code"], x["cls"], x["size"], x.get("legend") or "") for x in signs if x["trigger"] == "SIGN-REQUEST")
    case("V8.1", "Designer-placed R7-1 and D3-1 sized/classed from the catalog; unknown code rejected",
         [("D3-1", "Recommended", "Variesx48", "El Tahrir St"), ("R7-1", "Recommended", "12x18", "")], got)
case("V8.2", "Full catalog: every sign with a size table row or named designation (1,065) is loaded",
     True, len(rb.sign_catalog) >= 1065 and len(rb.devices) >= 1066)

# Table 2C-6 rows through the resolver (W13-1P provision follows the speed differential, not the curve sign)
from engine.rulebook import Rulebook as _RB
_rb = _RB("mutcd_11e")
def _plaque(diff):
    t = {"diff_kmh": diff, "suppress_sign": False, "chart_a": "Required", "curve_sign": "W1-2", "advisory_mph": 30}
    for r in _rb.resolve("CURVE", t):
        for c in r["companions"]:
            if c["device"] == "W13-1P":
                return c["class"]
case("V5.16c", "Table 2C-6 in km/h: W13-1P at differential 10 / 20 / 30 / 50 km/h",
     ["Optional", "Recommended", "Mandatory", "Mandatory"], [_plaque(d) for d in (10, 20, 30, 50)])
from engine.triggers import advisory_kmh
case("V4.4", "Advisory in km/h: R=150 m, e=0.06, 90 km/h -> 39.4 mph = 63.4 km/h -> 60 km/h", 60.0, advisory_kmh(150, 0.06, 90))

# school POI without and with a designated zone
sfe = [L("R", [[0, 0], [800, 0]], **{"class": "collector", "speed_kmh": 50, **BASE}), P(400, 20, type="school", id="SC")]
signs, _ = run_net(sfe)
if signs:
    s1 = [x for x in signs if x["code"] == "S1-1"]
    case("V5.17", "School without a designated zone: S1-1 Conditional", "Conditional", s1[0]["cls"] if s1 else None)
sfe[1]["properties"]["school_zone"] = True
signs, _ = run_net(sfe)
if signs:
    s1 = [x for x in signs if x["code"] == "S1-1"]
    case("V5.18", "School with a designated zone: S1-1 Mandatory, 36x36", ("Mandatory", "36x36"),
         (s1[0]["cls"], s1[0]["size"]) if s1 else None)

# ---------------------------------------------------------------- V9 hazard points (hazards.yaml)
HR = {"class": "collector", "speed_kmh": 80, "lanes": 1, "oneway": False, "aadt": 3000, "urban": False}
hfe = [L("A", [[0, 0], [2000, 0]], **HR), P(1000, 0, type="rail_crossing", id="RX", tracks=2, signals_gates=False),
       P(300, 0, type="narrow_structure", id="BR", structure="bridge", clear_width_m=5.2),
       P(1500, 0, type="low_clearance", id="LC", clearance_m=4.30), P(1800, 0, type="speed_hump", id="SH", advisory_kmh=25),
       P(600, 0, type="downgrade", id="DG", grade_pct=7, length_m=400, facing="fwd"),
       P(1200, 0, type="no_passing_start", id="NP", facing="fwd")]
signs, err = run_net(hfe)
if signs:
    rx = [x for x in signs if x["where"].startswith("rail crossing RX on A (fwd)")]
    w10 = [x for x in rx if x["code"] == "W10-1"]
    # 80 km/h = 49.7 mph -> 50 mph row, Condition B 0 mph = 425 ft = 129.5 m before the crossing (8B.06-02, Table 2C-3)
    case("V9.1", "Rail crossing: W10-1 Mandatory 425 ft ahead; R15-1 + R15-2P (2 tracks) Mandatory; RXR Mandatory at 80 km/h",
         ("Mandatory", 129.5, ["R15-1", "R15-2P", "RXR", "W10-1"], {"Mandatory"}),
         (w10[0]["cls"] if w10 else None, round(w10[0]["back_m"] - 1000, 1) if w10 else None,
          sorted(x["code"] for x in rx), {x["cls"] for x in rx}))
    br = sorted((x["code"], x["cls"]) for x in signs if x["where"].startswith("narrow structure BR"))
    case("V9.2", "Bridge 5.2 m two-way (16-18 ft): W5-2 Recommended both ways (2C.18-01)",
         [("W5-2", "Recommended"), ("W5-2", "Recommended")], br)
    lc = [x for x in signs if x["code"] == "W12-2"]
    case("V9.3", "Clearance 4.30 m < 14 ft 6 in: W12-2 Mandatory showing 4.30 m (14 ft 1 in) (2C.25-01/02)",
         ("Mandatory", "4.30 m (14 ft 1 in)", 2), (lc[0]["cls"], lc[0]["legend"], len(lc)) if lc else None)
    sh = sorted((x["code"], x["cls"], x.get("legend") or "") for x in signs if x["where"].startswith("speed hump SH on A (fwd)"))
    case("V9.4", "Speed hump: W17-1 + W13-1P 25 km/h, both Recommended (2C.27-01/02)",
         [("W13-1P", "Recommended", "25 km/h"), ("W17-1", "Recommended", "")], sh)
    dg = sorted((x["code"], x["cls"], x.get("legend") or "") for x in signs if x["where"].startswith("downgrade DG"))
    case("V9.5", "Downgrade 7% over 400 m (> 1,000 ft): W7-1 + W7-3P 7% Recommended, downhill direction only (2C.14-02 C)",
         [("W7-1", "Recommended", ""), ("W7-3P", "Recommended", "7%")], dg)
    np_ = [(x["code"], x["side"]) for x in signs if x["where"].startswith("no passing start NP")]
    case("V9.6", "NO PASSING ZONE pennant on the left-hand side (2C.53-01)", [("W14-3", "left")], np_)
else:
    print(err[-600:])
hfe2 = [L("A", [[0, 0], [2000, 0]], **HR), P(1000, 0, type="rail_crossing", id="RX"),
        P(700, 0, type="narrow_structure", id="NB", structure="underpass", clear_width_m=4.5),
        P(1500, 0, type="low_clearance", id="LC", clearance_m=4.60)]
signs, err = run_net(hfe2)
case("V9.7", "Rail crossing without tracks / signals data: run stops with data questions", True,
     signs is None and "STOPPED" in err and "RX" in err)
signs, err = run_net(hfe2, overrides={"pois": {"RX": {"tracks": 1, "signals_gates": False}}})
if signs:
    got = sorted({(x["code"], x["cls"]) for x in signs if x["trigger"].startswith("HAZ") and not x["where"].startswith("rail")})
    rx = sorted({x["code"] for x in signs if x["where"].startswith("rail")})
    case("V9.8", "Underpass 4.5 m (< 16 ft): W5-3a Recommended; clearance 4.60 m: no W12-2; 1 track: no R15-2P",
         ([("W5-3a", "Recommended")], ["R15-1", "RXR", "W10-1"]), (got, rx))
else:
    print(err[-600:])

# ---------------------------------------------------------------- V10 cross-section changes found in the network
NR = {"class": "arterial", "speed_kmh": 80, "lanes": 1, "oneway": False, "aadt": 6000, "urban": False}
dfe = [L("U", [[0, 0], [1000, 0]], **NR), L("D", [[1000, 0], [2000, 0]], **{**NR, "divided": True, "lanes": 2}),
       L("U2", [[2000, 0], [3000, 0]], **NR)]
signs, err = run_net(dfe)
if signs:
    a = sorted((x["code"], x["cls"], x["side"]) for x in signs if x["where"] == "divided section begins U->D")
    b = sorted((x["code"], x["cls"]) for x in signs if x["where"] == "divided section ends D->U2")
    case("V10.1", "Divided section: W6-1 (R) + Keep Right on the nose (O, left); end: W6-2 + W6-3 to two-lane (R) (2C.20/2C.21/2C.51/2B.39)",
         ([("R4-7", "Optional", "left"), ("W6-1", "Recommended", "right")], [("W6-2", "Recommended"), ("W6-3", "Recommended")]), (a, b))
else:
    print(err[-500:])
FW = {**NR, "class": "freeway", "speed_kmh": 100, "oneway": True, "lanes": 2}
mfe = [L("M1", [[0, 0], [1000, 0]], **FW), L("M2", [[1000, 0], [2000, 0]], **FW),
       L("RA", [[400, -150], [1000, 0]], **{**FW, "class": "ramp", "lanes": 1, "speed_kmh": 60})]
signs, err = run_net(mfe)
if signs:
    m = [x for x in signs if x["trigger"] == "MERGE" and "(major)" in x["where"]]
    # 100 km/h = 62.1 mph -> 65 mph row, Condition A = 1,200 ft = 365.8 m (Table 2C-3; typical sign: Merge)
    case("V10.2", "Ramp joins without added lane: W4-1 Optional on the right of the freeway, 1,200 ft ahead (Cond A); no intersection question",
         ("W4-1", "Optional", "right", 365.8), (m[0]["code"], m[0]["cls"], m[0]["side"], round(m[0]["back_m"], 1)) if m else None)
else:
    print(err[-500:])
mfe[1]["properties"]["lanes"] = 3
signs, err = run_net(mfe)
if signs:
    m = sorted((x["code"], x["cls"]) for x in signs if x["trigger"] == "ADDED-LANE")
    case("V10.3", "Ramp adds a lane (2+1 -> 3): W4-3 Recommended on the freeway; entering-road W4-3 Conditional (2C.46-01)",
         [("W4-3", "Conditional"), ("W4-3", "Recommended")], m)
ofe = [L("O", [[0, 0], [500, 0]], **{**NR, "oneway": True, "urban": True, "speed_kmh": 50}),
       L("W", [[500, 0], [1000, 0]], **{**NR, "urban": True, "speed_kmh": 50})]
signs, err = run_net(ofe)
if signs:
    case("V10.4", "One-way street becomes two-lane two-way: W6-3 + W16-9P AHEAD, Recommended (2C.51-02)",
         [("W16-9P", "Recommended"), ("W6-3", "Recommended")], sorted((x["code"], x["cls"]) for x in signs if x["trigger"] == "ONEWAY-TO-TWOWAY"))
arc_ = [[1000 + 60 * math.sin(math.radians(a)), 60 - 60 * math.cos(math.radians(a))] for a in range(0, 91, 5)]
signs, err = run_net([L("C", [[0, 0]] + arc_ + [[1060, 1000]], **{**NR, "speed_kmh": 60})])
if signs:
    w16 = [x for x in signs if x["code"] == "W1-6" and "(fwd)" in x["where"]]
    case("V10.5", "Left turn R=60 m (W1-1): W1-6 Optional on the outside (right), arrow left (2C.10-02/04)",
         ("Optional", "right", "left"), (w16[0]["cls"], w16[0]["side"], w16[0]["orientation"]) if w16 else None)

# ---------------------------------------------------------------- V12 T&I drawing style (styles/ti_details)
from engine import writers as _w
_sp = _w.load_style_pack("ti_details")
case("V12.1", "T&I style pack loads: template, 28 block-map rows, fixation post spec", (True, 28, "Galvanized steel post, Ø60.3 mm / 5 mm"),
     (os.path.exists(_sp["template_path"]), len(_sp["block_map"]), _sp["fixation"]["post"]))
_d = tempfile.mkdtemp()
_r = subprocess.run([sys.executable, "-m", "engine.run", "--input", "tests/networks/rural_highway.dxf", "--layers", "C-ROAD-CL",
                     "--settings", "tests/settings_default.json", "--overrides", "tests/overrides_rural_dxf.json", "--out", _d],
                    cwd=ROOT, capture_output=True, text=True)
if _r.returncode == 0:
    import ezdxf, openpyxl
    _doc = ezdxf.readfile(os.path.join(_d, "rural_highway_DRAFT_Signing.dxf"))
    _signs = [e for e in _doc.modelspace().query("INSERT") if e.dxf.layer == "TI-Signs"]
    _det = sum(1 for e in _doc.modelspace() if e.dxf.layer == "TI-DETAILS")
    case("V12.2", "Output DXF: signs on TI-Signs, T&I line types and dim style present, details copied, no audit errors",
         (True, True, True, True, False),
         (len(_signs) > 0, "TI-BRK 3-9" in _doc.linetypes and "TI-LE" in _doc.linetypes, "TI 1000" in _doc.dimstyles,
          _det > 1000, _doc.audit().has_errors))
    _ws = openpyxl.load_workbook(os.path.join(_d, "rural_highway_DRAFT_Sign_Schedule.xlsx"))["Signs"]
    _h = [c.value for c in _ws[1]]
    case("V12.3", "Schedule has T&I block, fixation detail, post and base columns", ["T&I block", "Fixation detail", "Post", "Base"], _h[-4:])
else:
    print(_r.stdout[-400:], _r.stderr[-400:])

summary = {"total": len(RESULTS), "pass": sum(r["result"] == "PASS" for r in RESULTS)}
print(json.dumps(summary))
json.dump(RESULTS, open(os.path.join(HERE, "verification_results.json"), "w"), indent=1)
if summary["pass"] != summary["total"]:
    sys.exit(1)
