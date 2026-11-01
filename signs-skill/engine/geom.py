"""Small planar geometry helpers (projected metres). No external dependencies."""
from __future__ import annotations
import math
from typing import List, Tuple

Pt = Tuple[float, float]
FT = 0.3048


def ft(m: float) -> float:
    return m / FT


def m_from_ft(f: float) -> float:
    return f * FT


def mph(kmh: float) -> float:
    return kmh / 1.609344


def kmh(mph_: float) -> float:
    return mph_ * 1.609344


def dist(a: Pt, b: Pt) -> float:
    return math.hypot(b[0] - a[0], b[1] - a[1])


def length(pl: List[Pt]) -> float:
    return sum(dist(pl[i], pl[i + 1]) for i in range(len(pl) - 1))


def heading(a: Pt, b: Pt) -> float:
    return math.atan2(b[1] - a[1], b[0] - a[0])


def norm_angle(a: float) -> float:
    while a > math.pi:
        a -= 2 * math.pi
    while a < -math.pi:
        a += 2 * math.pi
    return a


def point_along(pl: List[Pt], s: float) -> Tuple[Pt, float]:
    """Point at distance s from the start of polyline pl, plus heading there (radians).
    s is clamped to [0, length]."""
    if s <= 0:
        return pl[0], heading(pl[0], pl[1])
    acc = 0.0
    for i in range(len(pl) - 1):
        seg = dist(pl[i], pl[i + 1])
        if seg <= 0:
            continue
        if acc + seg >= s:
            t = (s - acc) / seg
            p = (pl[i][0] + t * (pl[i + 1][0] - pl[i][0]), pl[i][1] + t * (pl[i + 1][1] - pl[i][1]))
            return p, heading(pl[i], pl[i + 1])
        acc += seg
    return pl[-1], heading(pl[-2], pl[-1])


def offset_point(p: Pt, hdg: float, right_m: float) -> Pt:
    """Offset a point perpendicular to heading. Positive = right of travel, negative = left."""
    return (p[0] + right_m * math.sin(hdg), p[1] - right_m * math.cos(hdg))


def offset_polyline(pl: List[Pt], right_m: float) -> List[Pt]:
    out = []
    for i, p in enumerate(pl):
        if i == 0:
            h = heading(pl[0], pl[1])
        elif i == len(pl) - 1:
            h = heading(pl[-2], pl[-1])
        else:
            h1 = heading(pl[i - 1], pl[i])
            h2 = heading(pl[i], pl[i + 1])
            h = h1 + norm_angle(h2 - h1) / 2
        out.append(offset_point(p, h, right_m))
    return out


def project_point(pl: List[Pt], p: Pt) -> Tuple[float, float]:
    """Return (station along pl, perpendicular distance) of the closest point to p."""
    best = (0.0, float("inf"))
    acc = 0.0
    for i in range(len(pl) - 1):
        a, b = pl[i], pl[i + 1]
        seg = dist(a, b)
        if seg <= 0:
            continue
        t = ((p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1])) / (seg * seg)
        t = max(0.0, min(1.0, t))
        q = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
        d = dist(p, q)
        if d < best[1]:
            best = (acc + t * seg, d)
        acc += seg
    return best


def arc_to_points(start: Pt, end: Pt, bulge: float, max_seg_deg: float = 5.0) -> List[Pt]:
    """DXF bulge arc from start to end, returned as interior+end points."""
    if abs(bulge) < 1e-9:
        return [end]
    theta = 4 * math.atan(bulge)  # included angle, signed
    chord = dist(start, end)
    r = chord / (2 * math.sin(abs(theta) / 2))
    mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    h = heading(start, end)
    d = math.sqrt(max(r * r - (chord / 2) ** 2, 0.0))
    # centre lies to the left for positive bulge (counter-clockwise)
    sgn = 1 if bulge > 0 else -1
    if abs(theta) > math.pi:
        d = -d
    c = (mid[0] - sgn * d * math.sin(h), mid[1] + sgn * d * math.cos(h))
    a0 = math.atan2(start[1] - c[1], start[0] - c[0])
    n = max(2, int(math.degrees(abs(theta)) / max_seg_deg) + 1)
    pts = []
    for k in range(1, n + 1):
        a = a0 + theta * k / n
        pts.append((c[0] + r * math.cos(a), c[1] + r * math.sin(a)))
    pts[-1] = end
    return pts


def densify(pl: List[Pt], step: float = 5.0) -> List[Pt]:
    out = [pl[0]]
    for i in range(len(pl) - 1):
        a, b = pl[i], pl[i + 1]
        n = max(1, int(dist(a, b) // step))
        for k in range(1, n + 1):
            t = k / n
            out.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    return out
