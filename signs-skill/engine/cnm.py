"""Common Network Model (CNM): the format-neutral road network every adapter produces.

Links are digitised centrelines in projected metres. A link is two-way unless `oneway`
is true, in which case traffic flows in digitised direction (first vertex -> last vertex).

Link properties (canonical names; adapters map source fields onto these):
  id, name, class (freeway|expressway|arterial|collector|local), speed_kmh (posted),
  lanes (per direction), oneway (bool), divided (bool), aadt, urban (bool), curb (bool),
  lane_width_m (default 3.65), superelevation (e, default 0.06 rural / 0.04 urban),
  sight_restricted (bool, optional), shoulder_m
Node properties (from Point features that sit on link ends):
  id, control (signal|stop_all|stop_minor|yield|roundabout|none),
  stop_approaches (list of link ids under STOP/YIELD for stop_minor|yield),
  sight_restricted (bool), hidden (bool)
Point-of-interest properties (Point features not on link ends):
  type (crosswalk|school|rail), name
Every attribute keeps its source: 'input' | 'override' | 'default' | 'derived'.
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .geom import Pt, dist, length, heading

CLASS_RANK = {"freeway": 5, "expressway": 4, "arterial": 3, "collector": 2, "local": 1}


@dataclass
class Link:
    id: str
    coords: List[Pt]
    props: Dict = field(default_factory=dict)
    src: Dict[str, str] = field(default_factory=dict)
    a: str = ""  # start node id
    b: str = ""  # end node id

    def get(self, k, default=None):
        v = self.props.get(k)
        return default if v is None or v == "" else v

    @property
    def length(self) -> float:
        return length(self.coords)

    @property
    def lanes(self) -> int:
        return int(self.get("lanes", 1))

    @property
    def lane_w(self) -> float:
        return float(self.get("lane_width_m", 3.65))

    @property
    def oneway(self) -> bool:
        return bool(self.get("oneway", False))

    @property
    def divided(self) -> bool:
        return bool(self.get("divided", False))

    @property
    def urban(self) -> bool:
        return bool(self.get("urban", True))

    @property
    def rank(self) -> int:
        return CLASS_RANK.get(str(self.get("class", "local")), 1)

    def width_total(self) -> float:
        dirs = 1 if self.oneway else 2
        return self.lanes * dirs * self.lane_w

    def half_width_dir(self) -> float:
        """Distance from centreline to the right edge for one direction of travel."""
        if self.oneway:
            return self.lanes * self.lane_w / 2
        return self.lanes * self.lane_w


@dataclass
class Node:
    id: str
    xy: Pt
    props: Dict = field(default_factory=dict)
    links: List[str] = field(default_factory=list)

    @property
    def degree(self) -> int:
        return len(self.links)

    def get(self, k, default=None):
        v = self.props.get(k)
        return default if v is None or v == "" else v


@dataclass
class POI:
    id: str
    xy: Pt
    props: Dict = field(default_factory=dict)


@dataclass
class Approach:
    """Travel along `link` towards `node`. `path` runs from far upstream to the node
    (extended across degree-2 continuations so advance distances are available)."""
    link: Link
    node: Node
    path: List[Pt]
    links_upstream: List[str]

    @property
    def key(self) -> str:
        return f"{self.link.id}>{self.node.id}"


def _seg_x(a, b, c, d):
    """Intersection point of segments ab and cd, or None."""
    rx, ry = b[0] - a[0], b[1] - a[1]
    sx, sy = d[0] - c[0], d[1] - c[1]
    den = rx * sy - ry * sx
    if abs(den) < 1e-12:
        return None
    t = ((c[0] - a[0]) * sy - (c[1] - a[1]) * sx) / den
    u = ((c[0] - a[0]) * ry - (c[1] - a[1]) * rx) / den
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (a[0] + t * rx, a[1] + t * ry)
    return None


def _ray_hit(p, h, pl, max_d):
    """First intersection of the ray from p (heading h) with polyline pl within max_d, else None."""
    import math
    dx, dy = math.cos(h), math.sin(h)
    best = None
    for i in range(len(pl) - 1):
        a, b = pl[i], pl[i + 1]
        ex, ey = b[0] - a[0], b[1] - a[1]
        den = dx * ey - dy * ex
        if abs(den) < 1e-12:
            continue
        t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den
        u = ((a[0] - p[0]) * dy - (a[1] - p[1]) * dx) / den
        if 0 <= t <= max_d and 0 <= u <= 1 and (best is None or t < best[0]):
            best = (t, (p[0] + t * dx, p[1] + t * dy))
    return best[1] if best else None


class Network:
    def __init__(self):
        self.links: Dict[str, Link] = {}
        self.nodes: Dict[str, Node] = {}
        self.pois: Dict[str, POI] = {}
        self.crs: Optional[str] = None
        self.source: str = ""
        self.assumptions: List[str] = []
        self.curves: List = []
        self.style: Dict = {}

    # ------------------------------------------------------------ build
    def snap_tees(self, tol: float = 12.0, end_tol: float = 1.0):
        """Join T-junctions drawn as a free end stopping short of (or touching) another centreline:
        the free end is extended to its projection and the other link is split there.
        Every join is logged in self.assumptions."""
        from .geom import project_point, point_along
        ends = [(l.id, 0) for l in self.links.values()] + [(l.id, -1) for l in self.links.values()]
        splits: Dict[str, List[float]] = {}
        moves = []
        for lid, k in ends:
            p = self.links[lid].coords[k]
            if any(dist(p, o.coords[j]) <= end_tol for o in self.links.values() for j in (0, -1) if o.id != lid):
                continue
            best = None
            for o in self.links.values():
                if o.id == lid:
                    continue
                s, d = project_point(o.coords, p)
                if d <= tol and (best is None or d < best[1]):
                    best = (o.id, d, s)
            if best:
                o = self.links[best[0]]
                q, _ = point_along(o.coords, best[2])
                # prefer extending the free end along its own direction (no kink) when that meets the other link
                L_ = self.links[lid].coords
                a0, a1 = (L_[1], L_[0]) if k == 0 else (L_[-2], L_[-1])
                qx = _ray_hit(a1, heading(a0, a1), o.coords, 2.5 * tol)
                if qx is not None:
                    q = qx
                    best = (best[0], dist(p, q), project_point(o.coords, q)[0])
                moves.append((lid, k, q, best))
                if 1.0 < best[2] < o.length - 1.0:
                    splits.setdefault(o.id, []).append(q)
        for lid, k, q, (oid, d, s) in moves:
            l = self.links[lid]
            # does the other link actually cross this one near its free end (overshoot)? then trim, don't extend
            hit = None
            o = self.links.get(oid)
            if o is not None:
                for i in range(len(o.coords) - 1):
                    for j in range(len(l.coords) - 1):
                        x = _seg_x(o.coords[i], o.coords[i + 1], l.coords[j], l.coords[j + 1])
                        if x is not None:
                            s_on_l = project_point(l.coords, x)[0]
                            near_end = s_on_l <= tol if k == 0 else (l.length - s_on_l) <= tol
                            if near_end:
                                hit = (x, s_on_l)
            if hit:
                x, s_on_l = hit
                acc, pts = 0.0, l.coords
                sta = [0.0]
                for i in range(len(pts) - 1):
                    sta.append(sta[-1] + dist(pts[i], pts[i + 1]))
                if k == 0:
                    l.coords = [x] + [pts[i] for i in range(len(pts)) if sta[i] > s_on_l + 0.01]
                else:
                    l.coords = [pts[i] for i in range(len(pts)) if sta[i] < s_on_l - 0.01] + [x]
                self.assumptions.append(f"T-junction: {lid} overshoots {oid} by {d:.1f} m; trimmed at the crossing")
                q = x
                # re-point the split for the other link at the crossing
                if oid in splits:
                    splits[oid] = [x if dist(v, q) < tol + 1 else v for v in splits[oid]]
                continue
            if d > 0.01:
                if k == 0:
                    l.coords.insert(0, q)
                else:
                    l.coords.append(q)
            self.assumptions.append(f"T-junction: end of {lid} joined to {oid} (gap {d:.1f} m)")
        for oid, qs in splits.items():
            o = self.links.pop(oid)
            cuts = sorted(set(round(project_point(o.coords, q)[0], 2) for q in qs))
            pieces, prev_s = [], 0.0
            from .geom import point_along as pa
            pts = o.coords
            acc = [0.0]
            for i in range(len(pts) - 1):
                acc.append(acc[-1] + dist(pts[i], pts[i + 1]))
            bounds = [0.0] + cuts + [acc[-1]]
            for n in range(len(bounds) - 1):
                s0, s1 = bounds[n], bounds[n + 1]
                seg = [pa(pts, s0)[0]] + [pts[i] for i in range(len(pts)) if s0 < acc[i] < s1] + [pa(pts, s1)[0]]
                nid = f"{oid}-{n + 1}"
                p = dict(o.props)
                p["id"] = nid
                p["parent"] = oid
                self.links[nid] = Link(nid, seg, p, dict(o.src))
            self.assumptions.append(f"{oid} split into {len(bounds) - 1} links at T-junction(s)")
        return self

    def build_topology(self, snap: float = 1.0, node_points: Optional[List[Tuple[Pt, Dict]]] = None,
                       node_snap: float = 8.0):
        """Create nodes at link ends (snapping within `snap` m) and attach node attributes
        from `node_points` (within `node_snap` m). Points not near a node become POIs."""
        ends: List[Tuple[Pt, str, str]] = []
        for l in self.links.values():
            ends.append((l.coords[0], l.id, "a"))
            ends.append((l.coords[-1], l.id, "b"))
        clusters: List[List] = []
        for p, lid, which in ends:
            for c in clusters:
                if dist(c[0], p) <= snap:
                    c[1].append((lid, which))
                    break
            else:
                clusters.append([p, [(lid, which)]])
        self.nodes = {}
        for i, (p, members) in enumerate(clusters):
            nid = f"N{i + 1:03d}"
            n = Node(nid, p)
            for lid, which in members:
                setattr(self.links[lid], which, nid)
                if lid not in n.links:
                    n.links.append(lid)
                # snap the link end exactly onto the node
                l = self.links[lid]
                if which == "a":
                    l.coords[0] = p
                else:
                    l.coords[-1] = p
            self.nodes[nid] = n
        for k, (p, props) in enumerate(node_points or []):
            best, bd = None, 1e18
            for n in self.nodes.values():
                d = dist(n.xy, p)
                if d < bd:
                    best, bd = n, d
            if best is not None and bd <= node_snap and props.get("type") in (None, "", "node", "intersection"):
                pid = props.get("id")
                best.props.update({k2: v for k2, v in props.items() if k2 not in ("type",)})
                if pid:
                    best.props["label"] = pid
            else:
                pid = str(props.get("id") or f"P{k + 1:03d}")
                self.pois[pid] = POI(pid, p, props)
        # translate stop_approaches given as labels/ids of links (keep as is)
        return self

    # ------------------------------------------------------------ queries
    def node_label(self, nid: str) -> str:
        n = self.nodes[nid]
        return str(n.props.get("label") or nid)

    def other_end(self, lid: str, nid: str) -> str:
        l = self.links[lid]
        return l.b if l.a == nid else l.a

    def towards(self, lid: str, nid: str) -> List[Pt]:
        """Link geometry oriented to finish at node nid."""
        l = self.links[lid]
        return list(l.coords) if l.b == nid else list(reversed(l.coords))

    def can_travel_towards(self, lid: str, nid: str) -> bool:
        l = self.links[lid]
        return (not l.oneway) or l.b == nid

    def continuation(self, nid: str, from_lid: str) -> Optional[str]:
        n = self.nodes[nid]
        if n.degree == 2:
            others = [x for x in n.links if x != from_lid]
            return others[0] if others else None
        return None

    def approach(self, lid: str, nid: str, max_ext: float = 700.0) -> Approach:
        path = self.towards(lid, nid)
        ups = [lid]
        far = self.other_end(lid, nid)
        cur = lid
        while length(path) < max_ext:
            nxt = self.continuation(far, cur)
            if not nxt or nxt in ups or not self.can_travel_towards(nxt, far):
                break
            seg = self.towards(nxt, far)
            path = seg[:-1] + path
            ups.append(nxt)
            cur = nxt
            far = self.other_end(nxt, far)
        return Approach(self.links[lid], self.nodes[nid], path, ups)

    def approaches(self, nid: str) -> List[Approach]:
        return [self.approach(lid, nid) for lid in self.nodes[nid].links if self.can_travel_towards(lid, nid)]

    def departure(self, lid: str, nid: str) -> List[Pt]:
        return list(reversed(self.towards(lid, nid)))

    def crossing_half_width(self, nid: str, except_lid: str) -> float:
        w = 0.0
        for lid in self.nodes[nid].links:
            if lid == except_lid:
                continue
            w = max(w, self.links[lid].width_total() / 2)
        return w

    def approach_angle_ok(self, nid: str) -> bool:
        return True
