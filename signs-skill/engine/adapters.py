"""Input adapters: every format becomes a CNM Network.

Supported in v1: GeoJSON (incl. OSM/overpass GeoJSON exports), CSV/XLSX link+node tables,
DXF centrelines (ezdxf). DWG: convert to DXF first (AutoCAD / ODA File Converter).
"""
from __future__ import annotations
import csv
import json
import math
import os
import re
from typing import Dict, List, Optional, Tuple

from .cnm import Link, Network
from .geom import arc_to_points

# ---------------------------------------------------------------- field mapping
DEFAULT_MAP = {
    # canonical : accepted source names (case-insensitive)
    "id": ["id", "link_id", "linkid", "fid", "osm_id"],
    "name": ["name", "street", "road_name"],
    "class": ["class", "road_class", "fclass", "functional_class", "highway"],
    "speed_kmh": ["speed_kmh", "speed", "maxspeed", "posted_speed", "speed_limit"],
    "lanes": ["lanes", "lanes_per_dir", "lanes_dir"],
    "oneway": ["oneway", "one_way"],
    "divided": ["divided", "median"],
    "aadt": ["aadt", "adt", "volume"],
    "urban": ["urban", "is_urban", "area"],
    "curb": ["curb", "kerb"],
    "lane_width_m": ["lane_width_m", "lane_width"],
    "superelevation": ["superelevation", "e", "emax"],
    "sight_restricted": ["sight_restricted"],
    "control": ["control", "control_type", "traffic_control"],
    "stop_approaches": ["stop_approaches", "minor_approaches"],
    "hidden": ["hidden"],
    "type": ["type", "poi", "kind"],
    "school_zone": ["school_zone", "school_zone_designated"],
    "markings": ["markings", "has_markings"],
    "lanes_total": ["lanes_total", "total_lanes"],
    "code": ["code", "sign_code", "mutcd_code", "mutcd"],
    "facing": ["facing", "faces", "direction_faced"],
    "legend": ["legend", "text"],
    "boundary": ["boundary", "site_boundary", "gate"],
    "entry_speed_kmh": ["entry_speed_kmh", "entry_speed"],
    "exit_control": ["exit_control"],
    "yield_here_signs": ["yield_here_signs", "stop_here_signs", "r1_5"],
    # hazard points (rulebooks/<code>/hazards.yaml)
    "tracks": ["tracks", "num_tracks", "n_tracks"],
    "signals_gates": ["signals_gates", "active_crossing", "gates"],
    "structure": ["structure", "structure_type"],
    "clear_width_m": ["clear_width_m", "clear_width", "bridge_width_m"],
    "heavy_commercial": ["heavy_commercial", "high_truck_share"],
    "clearance_m": ["clearance_m", "vertical_clearance_m", "clearance"],
    "advisory_kmh": ["advisory_kmh", "advisory_speed", "advisory"],
    "grade_pct": ["grade_pct", "grade"],
    "length_m": ["length_m", "grade_length_m"],
    "bus_not_visible": ["bus_not_visible"],
    "emergency_signal": ["emergency_signal"],
}

OSM_CLASS = {
    "motorway": "freeway", "motorway_link": "freeway", "trunk": "expressway", "trunk_link": "expressway",
    "primary": "arterial", "primary_link": "arterial", "secondary": "arterial", "secondary_link": "arterial",
    "tertiary": "collector", "tertiary_link": "collector", "unclassified": "local", "residential": "local",
    "living_street": "local", "service": "local",
}
CLASS_ALIASES = {"principal arterial": "arterial", "minor arterial": "arterial", "major": "arterial",
                 "minor": "local", "local road": "local", "highway": "expressway", "motorway": "freeway"}
CONTROL_ALIASES = {"signal": "signal", "signalised": "signal", "signalized": "signal", "traffic_signals": "signal",
                   "all_way_stop": "stop_all", "allway": "stop_all", "stop_all": "stop_all", "awsc": "stop_all",
                   "two_way_stop": "stop_minor", "twsc": "stop_minor", "stop": "stop_minor", "stop_minor": "stop_minor",
                   "yield": "yield", "give_way": "yield", "roundabout": "roundabout", "none": "none",
                   "uncontrolled": "none"}


def _truthy(v):
    if isinstance(v, bool):
        return v
    if v is None:
        return None
    s = str(v).strip().lower()
    if s in ("1", "true", "yes", "y", "t", "-1"):
        return True
    if s in ("0", "false", "no", "n", "f", ""):
        return False
    return None


def _num(v):
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return v
    m = re.search(r"-?\d+(\.\d+)?", str(v))
    if not m:
        return None
    x = float(m.group(0))
    if "mph" in str(v).lower():
        x *= 1.609344
    return x


def normalise_props(raw: Dict, fmap: Optional[Dict] = None) -> Tuple[Dict, Dict]:
    fmap = {**DEFAULT_MAP, **(fmap or {})}
    low = {str(k).lower(): v for k, v in raw.items()}
    out, src = {}, {}
    for canon, names in fmap.items():
        for n in names:
            if n.lower() in low and low[n.lower()] not in (None, ""):
                out[canon] = low[n.lower()]
                src[canon] = "input"
                break
    # types
    if "class" in out:
        c = str(out["class"]).strip().lower()
        out["class"] = OSM_CLASS.get(c, CLASS_ALIASES.get(c, c))
    for k in ("speed_kmh", "entry_speed_kmh", "aadt", "lane_width_m", "superelevation", "tracks", "clear_width_m",
              "clearance_m", "advisory_kmh", "grade_pct", "length_m"):
        if k in out:
            out[k] = _num(out[k])
    if "lanes" in out:
        n = _num(out["lanes"])
        out["lanes"] = int(n) if n else None
    for k in ("oneway", "divided", "urban", "curb", "sight_restricted", "hidden", "school_zone", "markings", "yield_here_signs", "boundary",
              "signals_gates", "heavy_commercial", "bus_not_visible", "emergency_signal"):
        if k in out:
            if k == "urban" and str(out[k]).lower() in ("urban", "rural"):
                out[k] = str(out[k]).lower() == "urban"
            else:
                out[k] = _truthy(out[k])
    if "control" in out:
        out["control"] = CONTROL_ALIASES.get(str(out["control"]).strip().lower(), str(out["control"]).strip().lower())
    if "stop_approaches" in out and isinstance(out["stop_approaches"], str):
        out["stop_approaches"] = [s.strip() for s in re.split(r"[;,]", out["stop_approaches"]) if s.strip()]
    return out, src


# ---------------------------------------------------------------- GeoJSON
def _lonlat_to_xy(coords, epsg: int):
    try:
        from pyproj import Transformer
    except ImportError as e:
        raise RuntimeError("Geographic coordinates need pyproj to project to metres") from e
    tr = Transformer.from_crs(4326, epsg, always_xy=True)
    return [tr.transform(x, y) for x, y in coords]


def _is_geographic(fc) -> bool:
    """Longitude/latitude only if the file says so (CRS84/4326) or EVERY line vertex fits in +-180/+-90
    (a single vertex near the origin of a local site grid must not decide it)."""
    name = str(((fc.get("crs") or {}).get("properties") or {}).get("name", "")).upper()
    if name:
        return "4326" in name or "CRS84" in name
    seen = False
    for f in fc.get("features", []):
        g = f.get("geometry") or {}
        if g.get("type") == "LineString":
            for c in g.get("coordinates") or []:
                seen = True
                if abs(c[0]) > 180 or abs(c[1]) > 90:
                    return False
    return seen


def read_geojson(path: str, fmap: Optional[Dict] = None, target_epsg: Optional[int] = None) -> Network:
    with open(path, encoding="utf-8") as fh:
        fc = json.load(fh)
    geo = _is_geographic(fc)
    if geo and not target_epsg:
        raise RuntimeError("Input is in longitude/latitude. Give the project EPSG (e.g. 22992) so it can be projected.")
    net = Network()
    net.source = os.path.basename(path)
    net.crs = f"EPSG:{target_epsg}" if geo else (fc.get("crs", {}).get("properties", {}).get("name"))
    pts = []
    for i, f in enumerate(fc.get("features", [])):
        g = f.get("geometry") or {}
        props, src = normalise_props(f.get("properties") or {}, fmap)
        t = g.get("type")
        parts = []
        if t == "LineString":
            parts = [g["coordinates"]]
        elif t == "MultiLineString":
            parts = g["coordinates"]
        elif t == "Point":
            xy = g["coordinates"][:2]
            if geo:
                xy = _lonlat_to_xy([xy], target_epsg)[0]
            pts.append((tuple(xy), props))
            continue
        for j, cs in enumerate(parts):
            cs = [tuple(c[:2]) for c in cs]
            if geo:
                cs = _lonlat_to_xy(cs, target_epsg)
            lid = str(props.get("id") or f"L{i + 1:04d}") + (f"_{j + 1}" if len(parts) > 1 else "")
            if lid in net.links:
                lid = f"{lid}_{i}"
            p = dict(props)
            p["id"] = lid
            net.links[lid] = Link(lid, list(cs), p, dict(src))
    net.build_topology(node_points=pts)
    return net


# ---------------------------------------------------------------- CSV / XLSX
def _rows(path: str, sheet: Optional[str] = None) -> List[Dict]:
    if path.lower().endswith((".xlsx", ".xlsm")):
        from openpyxl import load_workbook
        wb = load_workbook(path, data_only=True, read_only=True)
        ws = wb[sheet] if sheet else wb.worksheets[0]
        it = ws.iter_rows(values_only=True)
        hdr = [str(h).strip() if h is not None else "" for h in next(it)]
        return [dict(zip(hdr, r)) for r in it if any(v not in (None, "") for v in r)]
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def _parse_wkt_line(s: str) -> List[Tuple[float, float]]:
    nums = re.findall(r"(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)", s)
    return [(float(a), float(b)) for a, b in nums]


def read_table(links_path: str, nodes_path: Optional[str] = None, fmap: Optional[Dict] = None,
               links_sheet: Optional[str] = None, nodes_sheet: Optional[str] = None) -> Network:
    """Links table needs either a WKT column (geometry/wkt) or x1,y1,x2,y2 columns
    (optionally 'vertices' as 'x y; x y; ...'). Nodes table: id, x, y, control, ..."""
    net = Network()
    net.source = os.path.basename(links_path)
    for i, r in enumerate(_rows(links_path, links_sheet)):
        low = {str(k).lower(): v for k, v in r.items()}
        cs = None
        for k in ("wkt", "geometry", "geom", "shape"):
            if low.get(k):
                cs = _parse_wkt_line(str(low[k]))
        if not cs and low.get("x1") not in (None, ""):
            cs = [(float(low["x1"]), float(low["y1"]))]
            if low.get("vertices"):
                cs += [tuple(map(float, v.split())) for v in str(low["vertices"]).split(";") if v.strip()]
            cs.append((float(low["x2"]), float(low["y2"])))
        if not cs or len(cs) < 2:
            continue
        props, src = normalise_props(r, fmap)
        lid = str(props.get("id") or f"L{i + 1:04d}")
        props["id"] = lid
        net.links[lid] = Link(lid, cs, props, src)
    pts = []
    if nodes_path:
        for r in _rows(nodes_path, nodes_sheet):
            low = {str(k).lower(): v for k, v in r.items()}
            if low.get("x") in (None, ""):
                continue
            props, _ = normalise_props(r, fmap)
            pts.append(((float(low["x"]), float(low["y"])), props))
    net.build_topology(node_points=pts)
    return net


# ---------------------------------------------------------------- DXF
def dxf_layers(path: str) -> Dict[str, int]:
    import ezdxf
    doc = ezdxf.readfile(path)
    counts: Dict[str, int] = {}
    for e in doc.modelspace():
        if e.dxftype() in ("LINE", "LWPOLYLINE", "POLYLINE", "ARC"):
            counts[e.dxf.layer] = counts.get(e.dxf.layer, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def dxf_entity_counts(path: str) -> Dict[str, Dict[str, int]]:
    """Entity counts by layer and type (all model-space entities), for the re-read check before every run."""
    import ezdxf
    out: Dict[str, Dict[str, int]] = {}
    for e in ezdxf.readfile(path).modelspace():
        d = out.setdefault(e.dxf.layer, {})
        d[e.dxftype()] = d.get(e.dxftype(), 0) + 1
    return {k: dict(sorted(v.items())) for k, v in sorted(out.items())}


def compare_counts(old: Dict, new: Dict) -> List[str]:
    """Differences between two dxf_entity_counts() snapshots, as readable lines (empty = identical)."""
    diff = []
    for lay in sorted(set(old) | set(new)):
        a, b = old.get(lay, {}), new.get(lay, {})
        for t in sorted(set(a) | set(b)):
            if a.get(t, 0) != b.get(t, 0):
                diff.append(f"layer {lay} {t}: {a.get(t, 0)} -> {b.get(t, 0)}")
    return diff


def read_dxf(path: str, centreline_layers: List[str], node_layer: Optional[str] = None,
             join_tol: float = 0.5, tee_tol: float = 12.0, exclude: Optional[List[str]] = None) -> Network:
    """Read centrelines from the given layers. Attributes come from the overrides file
    (keyed by link id = 'H' + DXF handle) or from the questionnaire."""
    import ezdxf
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    net = Network()
    net.source = os.path.basename(path)
    lays = {l.upper() for l in centreline_layers}
    for e in msp:
        if e.dxf.layer.upper() not in lays:
            continue
        t = e.dxftype()
        cs: List[Tuple[float, float]] = []
        if t == "LINE":
            cs = [(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)]
        elif t == "LWPOLYLINE":
            pts = list(e.get_points("xyb"))
            if e.closed:
                pts.append(pts[0])
            cs = [(pts[0][0], pts[0][1])]
            for k in range(len(pts) - 1):
                cs += arc_to_points((pts[k][0], pts[k][1]), (pts[k + 1][0], pts[k + 1][1]), pts[k][2])
        elif t == "POLYLINE":
            cs = [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]
        elif t == "ARC":
            c, r = e.dxf.center, e.dxf.radius
            a0, a1 = math.radians(e.dxf.start_angle), math.radians(e.dxf.end_angle)
            if a1 < a0:
                a1 += 2 * math.pi
            n = max(2, int(math.degrees(a1 - a0) / 5) + 1)
            cs = [(c.x + r * math.cos(a0 + (a1 - a0) * k / n), c.y + r * math.sin(a0 + (a1 - a0) * k / n)) for k in range(n + 1)]
        if len(cs) >= 2:
            lid = "H" + e.dxf.handle
            net.links[lid] = Link(lid, cs, {"id": lid, "layer": e.dxf.layer}, {})
    pts = []
    if node_layer:
        for e in msp:
            if e.dxf.layer.upper() == node_layer.upper() and e.dxftype() in ("POINT", "INSERT", "CIRCLE"):
                p = e.dxf.location if e.dxftype() == "POINT" else (e.dxf.insert if e.dxftype() == "INSERT" else e.dxf.center)
                props = {}
                if e.dxftype() == "INSERT":
                    for a in e.attribs:
                        props[a.dxf.tag.lower()] = a.dxf.text
                pts.append(((p.x, p.y), normalise_props(props)[0]))
    for x in exclude or []:
        net.links.pop(x, None)
    net.snap_tees(tee_tol)
    net.build_topology(snap=join_tol, node_points=pts)
    # capture drawing style for the writer
    net.style = capture_dxf_style(doc, centreline_layers)  # type: ignore[attr-defined]
    return net


def capture_dxf_style(doc, centreline_layers: List[str]) -> Dict:
    """Guess the office layer convention (prefix and separator) and text style from the input."""
    names = [l.dxf.name for l in doc.layers]
    ref = centreline_layers[0] if centreline_layers else (names[0] if names else "C-ROAD-CL")
    sep = "-" if "-" in ref else ("_" if "_" in ref else "-")
    parts = ref.split(sep)
    prefix = parts[0] if len(parts) > 1 and len(parts[0]) <= 3 else ""
    upper = ref.upper() == ref
    styles = [s.dxf.name for s in doc.styles]
    text_style = "Standard" if "Standard" in styles else (styles[0] if styles else "Standard")
    heights = [e.dxf.height for e in doc.modelspace().query("TEXT")][:200]
    th = sorted(heights)[len(heights) // 2] if heights else 1.0
    return {"sep": sep, "prefix": prefix, "upper": upper, "text_style": text_style, "text_height": th,
            "units": doc.header.get("$INSUNITS", 6)}


# ---------------------------------------------------------------- dispatch
def load(path: str, **kw) -> Network:
    ext = os.path.splitext(path)[1].lower()
    if ext in (".geojson", ".json"):
        return read_geojson(path, kw.get("fmap"), kw.get("epsg"))
    if ext in (".csv", ".xlsx", ".xlsm"):
        return read_table(path, kw.get("nodes"), kw.get("fmap"), kw.get("links_sheet"), kw.get("nodes_sheet"))
    if ext == ".dxf":
        layers = kw.get("layers")
        if not layers:
            raise RuntimeError("DXF input needs the centreline layer name(s). Found layers: " +
                               ", ".join(f"{k} ({v})" for k, v in list(dxf_layers(path).items())[:15]))
        return read_dxf(path, layers, kw.get("node_layer"), tee_tol=kw.get("tee_tol", 12.0),
                        exclude=kw.get("exclude"))
    if ext == ".dwg":
        raise RuntimeError("DWG must be converted to DXF first (AutoCAD SAVEAS DXF, or ODA File Converter).")
    raise RuntimeError(f"Unsupported input format: {ext}")


# ---------------------------------------------------------------- measured attributes
def measure_widths(net: Network, dxf_path: str, edge_layers: List[str], step: float = 10.0,
                   max_half: float = 20.0) -> Dict[str, Dict]:
    """Carriageway width per link from edge-of-pavement / kerb lines: median of left+right
    distances from the centreline, sampled every `step` m away from junctions."""
    import ezdxf
    from statistics import median
    from .geom import point_along, heading, dist as _d
    doc = ezdxf.readfile(dxf_path)
    lays = {x.upper() for x in edge_layers}
    segs = []
    for e in doc.modelspace():
        if e.dxf.layer.upper() not in lays:
            continue
        try:
            path = ezdxf.path.make_path(e)
            pts = [(v.x, v.y) for v in path.flattening(0.2)]
        except Exception:
            continue
        segs += [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]

    def ray(p, h, side):
        # distance along the perpendicular (side=+1 right, -1 left) to the nearest edge segment
        dx, dy = side * math.sin(h), -side * math.cos(h)
        best = None
        for a, b in segs:
            ex, ey = b[0] - a[0], b[1] - a[1]
            den = dx * ey - dy * ex
            if abs(den) < 1e-9:
                continue
            t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den
            u = ((a[0] - p[0]) * dy - (a[1] - p[1]) * dx) / den
            if 0.3 < t <= max_half and 0 <= u <= 1 and (best is None or t < best):
                best = t
        return best

    out = {}
    for l in net.links.values():
        L = l.length
        ws, ls, rs = [], [], []
        s = 15.0
        while s < L - 15.0:
            p, h = point_along(l.coords, s)
            r, lf = ray(p, h, 1), ray(p, h, -1)
            if r and lf:
                ws.append(r + lf)
                rs.append(r)
                ls.append(lf)
            s += step
        if ws:
            out[l.id] = {"width_m": round(median(ws), 2), "right_m": round(median(rs), 2),
                         "left_m": round(median(ls), 2), "samples": len(ws)}
    return out


def load_edges(path: str, layers: List[str]) -> List:
    """Kerb / edge-of-pavement segments from a DXF, used to keep signs off the carriageway and parking bays."""
    import ezdxf
    doc = ezdxf.readfile(path)
    lays = {x.upper() for x in layers}
    segs = []
    for e in doc.modelspace():
        if e.dxf.layer.upper() not in lays:
            continue
        try:
            pts = [(v.x, v.y) for v in ezdxf.path.make_path(e).flattening(0.2)]
        except Exception:
            continue
        segs += [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    return segs
