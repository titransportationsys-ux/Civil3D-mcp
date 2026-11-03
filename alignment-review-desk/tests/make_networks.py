"""Build synthetic benchmark networks (projected metres, EPSG 22992-like offsets)."""
import json, math, os
X0, Y0 = 640000.0, 810000.0
HERE = os.path.dirname(os.path.abspath(__file__))

def L(id_, pts, **p):
    return {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[X0 + x, Y0 + y] for x, y in pts]},
            "properties": {"id": id_, **p}}

def P(x, y, **p):
    return {"type": "Feature", "geometry": {"type": "Point", "coordinates": [X0 + x, Y0 + y]}, "properties": p}

def arc(cx, cy, r, a0, a1, n=24):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]

# ---------------- urban grid: 3x2 blocks, arterial E-W, collectors/locals N-S
art = dict(**{"class": "arterial", "speed_kmh": 60, "lanes": 2, "oneway": False, "aadt": 18000, "urban": True, "curb": True})
col = dict(**{"class": "collector", "speed_kmh": 50, "lanes": 1, "oneway": False, "aadt": 6500, "urban": True, "curb": True})
loc = dict(**{"class": "local", "speed_kmh": 40, "lanes": 1, "oneway": False, "aadt": 1200, "urban": True, "curb": True})
F = []
xs = [0, 250, 500, 750]
# arterial y=0, segmented at intersections; speed changes to 80 east of x=750
for i in range(3):
    F.append(L(f"A{i+1}", [(xs[i], 0), (xs[i+1], 0)], name="Main Arterial", **art))
F.append(L("A4", [(750, 0), (1300, 0)], name="Main Arterial east", **{**art, "speed_kmh": 80, "urban": False, "curb": False}))
F.append(L("A0", [(-400, 0), (0, 0)], name="Main Arterial west", **art))
# collector y=250 parallel
for i in range(3):
    F.append(L(f"C{i+1}", [(xs[i], 250), (xs[i+1], 250)], name="North Collector", **col))
# N-S streets
F.append(L("S1a", [(0, -300), (0, 0)], name="West St", **col))
F.append(L("S1b", [(0, 0), (0, 250)], name="West St", **col))
F.append(L("S2a", [(250, -300), (250, 0)], name="School Rd", **loc))
F.append(L("S2b", [(250, 0), (250, 250)], name="School Rd", **loc))
F.append(L("S3b", [(500, 250), (500, 0)], name="One-way St", **{**loc, "oneway": True}))  # flows south
F.append(L("S4b", [(750, 0), (750, 250)], name="East St", **loc))
F.append(L("S1c", [(0, 250), (0, 450)], name="West St", **col))
F.append(L("S2c", [(250, 250), (250, 450)], name="School Rd", **loc))
F.append(L("S3c", [(500, 450), (500, 250)], name="One-way St", **{**loc, "oneway": True}))
F.append(L("S4c", [(750, 250), (750, 450)], name="East St", **loc))
# nodes
F.append(P(0, 0, id="INT-1", control="signal"))
F.append(P(250, 0, id="INT-2", control="stop_minor"))
F.append(P(500, 0, id="INT-3", control="stop_minor"))
F.append(P(750, 0, id="INT-4", control="none"))
F.append(P(0, 250, id="INT-5", control="stop_all"))
F.append(P(250, 250, id="INT-6", control="stop_minor"))
F.append(P(500, 250, id="INT-7", control="yield", stop_approaches="S3c"))
F.append(P(750, 250, id="INT-8", control="stop_minor"))
F.append(P(260, -150, type="school", id="SCH-1", name="Primary school"))
F.append(P(375, 250, type="crosswalk", id="XW-1"))
with open(os.path.join(HERE, "networks", "urban_grid.geojson"), "w") as fh:
    json.dump({"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:22992"}}, "features": F}, fh, indent=1)

# ---------------- rural highway: tangent, R=150 m left curve, short tangent, R=180 m right curve (reverse), lane drop
rur = dict(**{"class": "arterial", "speed_kmh": 90, "lanes": 1, "oneway": False, "aadt": 4200, "urban": False})
pts = [(0, 0), (600, 0)]
c1 = arc(600, 150, 150, -90, -10)                 # left curve, 80 deg
pts += c1[1:]
end1 = pts[-1]
h = math.radians(80)
t2 = (end1[0] + 60 * math.cos(h), end1[1] + 60 * math.sin(h))
pts.append(t2)
# right curve radius 180 turning 70 deg
cx, cy = t2[0] + 180 * math.cos(h - math.pi / 2), t2[1] + 180 * math.sin(h - math.pi / 2)
a0 = math.degrees(h + math.pi / 2)
c2 = arc(cx, cy, 180, a0, a0 - 70)
pts += c2[1:]
e2 = pts[-1]
h2 = math.radians(10)
pts.append((e2[0] + 800 * math.cos(h2), e2[1] + 800 * math.sin(h2)))
R = [L("R1", pts, name="Rural Road 12", **rur)]
e3 = pts[-1]
R.append(L("R2", [e3, (e3[0] + 900, e3[1] + 150)], name="Rural Road 12 (two-lane section)", **{**rur, "lanes": 2, "speed_kmh": 100}))
e4 = R[-1]["geometry"]["coordinates"][-1]
R.append(L("R3", [(e4[0] - X0, e4[1] - Y0), (e4[0] - X0 + 700, e4[1] - Y0 + 100)], name="Rural Road 12 (merge)", **{**rur, "lanes": 1, "speed_kmh": 100}))
for f in R:
    if f["properties"]["id"] == "R1":
        continue
for f in R[1:]:
    pass
# fix R2 coords (already absolute) -> convert first R2 coordinate to absolute consistently
R[1]["geometry"]["coordinates"] = [[X0 + e3[0], Y0 + e3[1]], [X0 + e3[0] + 900, Y0 + e3[1] + 150]]
e4 = R[1]["geometry"]["coordinates"][-1]
R[2]["geometry"]["coordinates"] = [e4, [e4[0] + 700, e4[1] + 100]]
# side road T at km 0.3
R.append(L("SR1", [(300, -400), (300, 0)], name="Farm road", **{"class": "local", "speed_kmh": 60, "lanes": 1, "oneway": False, "aadt": 300, "urban": False}))
R[0]["geometry"]["coordinates"] = [[X0 + x, Y0 + y] for x, y in pts]
# split R1 at x=300 so the side road meets a node
coords = R[0]["geometry"]["coordinates"]
R[0]["geometry"]["coordinates"] = [coords[0], [X0 + 300, Y0]]
R.insert(1, L("R1b", [(300, 0)] + [(x, y) for x, y in pts[1:]], name="Rural Road 12", **rur))
R.append(P(300, 0, id="T-1", control="stop_minor"))
with open(os.path.join(HERE, "networks", "rural_highway.geojson"), "w") as fh:
    json.dump({"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:22992"}}, "features": R}, fh, indent=1)
print("ok")
