"""Code-neutral trigger detection. Finds WHERE a device may be needed; never names a sign.

Every trigger carries an Approach (travel towards a node) and `back_m`, the reference
distance measured back from that node along the approach (stop line, curve start, point).
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .cnm import Approach, Network
from .geom import dist, heading, length, mph, norm_angle, project_point, m_from_ft

WARN_SYMBOL = {4: "W2-1", 3: "W2-2"}


@dataclass
class Trigger:
    trigger: str
    t: Dict                          # context for rule expressions
    approach: Optional[Approach] = None
    back_m: float = 0.0              # reference point, metres back from approach node
    depart: Optional[List] = None    # departure path (for downstream placements)
    extra: Dict = field(default_factory=dict)
    where: str = ""


def _ctx(net: Network, lid: str) -> Dict:
    l = net.links[lid]
    sp = float(l.get("speed_kmh", 50))
    return {"link": lid, "class": str(l.get("class", "local")), "speed_kmh": sp, "speed_mph": mph(sp),
            "lanes": l.lanes, "oneway": l.oneway, "divided": l.divided, "urban": l.urban,
            "aadt": float(l.get("aadt", 0) or 0), "width_ft": l.width_total() / 0.3048,
            "sight_restricted": l.props.get("sight_restricted"),
            "lanes_total": int(l.props.get("lanes_total") or ((l.lanes or 1) * (1 if l.oneway else 2)))}


def stop_line_back(net: Network, nid: str, lid: str, crosswalk: bool = False) -> float:
    hw = net.crossing_half_width(nid, lid)
    back = hw + 1.2 + (3.0 if crosswalk else 0.0)        # 4 ft minimum (3B.19)
    return min(back, hw + 9.1)                            # 30 ft maximum


# ------------------------------------------------------------------ curves
@dataclass
class Curve:
    link: str
    s0: float           # PC station in digitised direction
    s1: float           # PT station
    delta: float        # signed total deflection (rad), + = left (CCW) in digitised direction
    radius: float

    @property
    def length(self):
        return self.s1 - self.s0


def detect_curves(coords, min_delta_deg=8.0, max_radius=1500.0, max_vertex_deg=45.0) -> List[Curve]:
    n = len(coords)
    if n < 3:
        return []
    seg = [dist(coords[i], coords[i + 1]) for i in range(n - 1)]
    sta = [0.0]
    for s in seg:
        sta.append(sta[-1] + s)
    defl = [0.0] * n
    for i in range(1, n - 1):
        if seg[i - 1] <= 0 or seg[i] <= 0:
            continue
        defl[i] = norm_angle(heading(coords[i], coords[i + 1]) - heading(coords[i - 1], coords[i]))
    groups, cur = [], []
    for i in range(1, n - 1):
        d = defl[i]
        ok = math.radians(0.3) <= abs(d) <= math.radians(max_vertex_deg)
        if ok:
            r_loc = min(seg[i - 1], seg[i]) / abs(d)   # shorter side: a long tangent must not hide the PC vertex
            ok = r_loc < max_radius * 1.5
        if ok and cur and (d > 0) != (defl[cur[-1]] > 0):
            groups.append(cur)
            cur = []
        if ok:
            cur.append(i)
        elif cur:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    out = []
    for g in groups:
        delta = sum(defl[i] for i in g)
        if abs(delta) < math.radians(min_delta_deg):
            continue
        # PC..PT between the first and last deflecting vertex. When the source polyline carries
        # PC/PT vertices (arcs from CAD), their half-step deflection makes sum(defl) = true delta.
        s0 = sta[g[0]]
        s1 = sta[g[-1]]
        if len(g) >= 2:
            inner = [seg[i] for i in range(g[0], g[-1])]
            avg = sum(inner) / len(inner)
            if abs(defl[g[0]]) > 0.75 * abs(delta) / len(g) * 1.5:   # no PC vertex: extend half a step
                s0 -= min(avg / 2, seg[g[0] - 1])
            if abs(defl[g[-1]]) > 0.75 * abs(delta) / len(g) * 1.5:
                s1 += min(avg / 2, seg[g[-1]])
        if len(g) == 1:
            # single angle point: treat as a short curve over the adjacent half segments
            s0 = sta[g[0]] - min(seg[g[0] - 1] / 2, 15)
            s1 = sta[g[0]] + min(seg[g[0]] / 2, 15)
        L = max(s1 - s0, 1.0)
        R = L / abs(delta)
        if R <= max_radius:
            out.append(Curve("", s0, s1, delta, R))
    return out


def chart_a_level(cls: str, aadt: float, has_markings=None) -> str:
    """MUTCD 11th Ed. Table 2C-4 Chart A. has_markings None = unknown -> treated as 'without markings'
    (the stricter row)."""
    if cls in ("freeway", "expressway"):
        return "Required"
    if cls in ("arterial", "collector"):
        if aadt < 1000:
            return "Optional"
        if aadt < 3000:
            return "Recommended"
        if aadt < 4000:
            return "Recommended" if has_markings is True else "Required"
        return "Required"
    return "Optional"


F_BALLBANK = [(35, 0.15), (25, 0.18), (0, 0.21)]   # FHWA advisory-speed practice (12/14/16 deg ball-bank)


def _advisory_raw_mph(radius_m: float, e: float, posted_mph: float) -> float:
    r_ft = radius_m / 0.3048
    v = posted_mph
    for lo, f in F_BALLBANK:
        v = math.sqrt(15.0 * r_ft * (e + f))
        if v >= lo:
            break
    return min(v, posted_mph)


def advisory_mph(radius_m: float, e: float, posted_mph: float) -> float:
    """US customary: floored to 5 mph."""
    return max(5.0, math.floor(_advisory_raw_mph(radius_m, e, posted_mph) / 5.0) * 5.0)


def advisory_kmh(radius_m: float, e: float, posted_kmh: float) -> float:
    """Metric (AASHTO practice): floored to 10 km/h, never above the posted speed."""
    v = _advisory_raw_mph(radius_m, e, mph(posted_kmh)) * 1.609344
    return max(10.0, min(float(posted_kmh), math.floor(v / 10.0 + 1e-9) * 10.0))


# ------------------------------------------------------------------ main
def junction_kind(net: Network, nid: str):
    """'split' (two carriageways meet a two-way road), 'merge' (2 one-way in, 1 out) or 'diverge' (1 in, 2 out):
    3-leg nodes that are not intersections, so no intersection control applies."""
    n = net.nodes[nid]
    if n.degree != 3:
        return None
    ls = [net.links[x] for x in n.links]
    ow = [l for l in ls if l.oneway]
    inc = sum(1 for l in ow if l.b == nid)
    out = sum(1 for l in ow if l.a == nid)
    if len(ow) == 2 and inc == 1 and out == 1:
        # the two carriageways leave the node on the same side (a one-way street passing through does not)
        h = [heading(*net.departure(l.id, nid)[:2]) for l in ow]
        if abs(norm_angle(h[0] - h[1])) < math.radians(60):
            return "split"
        return None
    if len(ow) == 3 and inc == 2 and out == 1:
        return "merge"
    if len(ow) == 3 and inc == 1 and out == 2:
        return "diverge"
    return None


def through_pairs(net: Network, nid: str):
    """(upstream link, downstream link) pairs that continue straight through node nid (<= 35 deg)."""
    n = net.nodes[nid]
    out = []
    for lid in n.links:
        if not net.can_travel_towards(lid, nid):
            continue
        p = net.towards(lid, nid)
        h_in = heading(p[-2], p[-1])
        best, bd = None, math.radians(35)
        for other in n.links:
            if other == lid:
                continue
            o = net.links[other]
            if o.oneway and o.a != nid:
                continue
            q = net.departure(other, nid)
            dd = abs(norm_angle(heading(q[0], q[1]) - h_in))
            if dd < bd:
                best, bd = o, dd
        if best is not None:
            out.append((net.links[lid], best))
    return out


def detect(net: Network, settings: Dict) -> List[Trigger]:
    trig: List[Trigger] = []
    # ------------ site boundary (compound gate / external road not in the drawing)
    for n in net.nodes.values():
        if n.degree != 1 or not n.props.get("boundary"):
            continue
        lid = n.links[0]
        label = net.node_label(n.id)
        ex = str(n.props.get("exit_control", "") or "").lower()
        if ex in ("stop", "yield"):
            t = _ctx(net, lid)
            t.update({"node": label, "degree": 1, "hidden": None, "boundary": True,
                      "sight_restricted": n.props.get("sight_restricted", False)})
            ap = net.approach(lid, n.id)
            trig.append(Trigger("INT-STOP-2WAY" if ex == "stop" else "INT-YIELD", t, ap,
                                stop_line_back(net, n.id, lid), where=f"{label} exit to external road / gate"))
        sp = n.props.get("entry_speed_kmh")
        if sp:
            t = _ctx(net, lid)
            t.update({"node": label, "new_kmh": float(sp)})
            trig.append(Trigger("BOUNDARY-ENTRY", t, None, 0.0, depart=net.departure(lid, n.id),
                                extra={"legend": f"{int(float(sp))}"}, where=f"{label} entry from external road / gate"))
    # ------------ intersections
    for n in net.nodes.values():
        if n.degree < 3 or junction_kind(net, n.id):
            continue
        ctl = n.props.get("control", "none")
        label = net.node_label(n.id)
        ranks = {lid: net.links[lid].rank for lid in n.links}
        minr, maxr = min(ranks.values()), max(ranks.values())
        sa = n.props.get("stop_approaches") or []
        sa = [str(x) for x in sa]
        for ap in net.approaches(n.id):
            t = _ctx(net, ap.link.id)
            t.update({"node": label, "degree": n.degree, "hidden": n.props.get("hidden"),
                      "sight_restricted": n.props.get("sight_restricted", t.get("sight_restricted"))})
            where = f"{label} approach from {net.link_name(ap.link.id)}"
            if ctl == "stop_all":
                trig.append(Trigger("INT-STOP-AWAY", t, ap, stop_line_back(net, n.id, ap.link.id), where=where))
            elif ctl in ("stop_minor", "yield"):
                minor = (ap.link.id in sa) if sa else (ranks[ap.link.id] == minr and minr < maxr)
                if minor:
                    code = "INT-STOP-2WAY" if ctl == "stop_minor" else "INT-YIELD"
                    trig.append(Trigger(code, t, ap, stop_line_back(net, n.id, ap.link.id), where=where))
            elif ctl == "signal":
                trig.append(Trigger("INT-SIGNAL", t, ap, stop_line_back(net, n.id, ap.link.id, crosswalk=True), where=where))
            elif ctl == "roundabout":
                icr = float(n.props.get("inscribed_radius_m") or 0)
                back = icr + 1.2 if icr else stop_line_back(net, n.id, ap.link.id)
                trig.append(Trigger("INT-ROUNDABOUT", t, ap, back, where=where))
            else:
                if ranks[ap.link.id] == maxr and minr < maxr:
                    through = sum(1 for lid in n.links if ranks[lid] == maxr) >= 2
                    t["warn_symbol"] = "W2-1" if n.degree >= 4 else ("W2-2" if through else "W2-4")
                    if t["warn_symbol"] == "W2-2":
                        side_l = [x for x in n.links if ranks[x] < maxr]
                        if side_l:
                            q = net.departure(side_l[0], n.id)
                            h_in = heading(ap.path[-2], ap.path[-1])
                            t["orientation"] = "left" if norm_angle(heading(q[0], q[1]) - h_in) > 0 else "right"
                    trig.append(Trigger("INT-UNCONTROLLED-MAJOR", t, ap, 0.0, where=where))
        # speed limit reminder after major intersections
        cross_ok = len([1 for lid in n.links if net.links[lid].rank >= 2]) >= 3
        if ctl == "signal" or (maxr >= 3 and cross_ok):
            for lid in n.links:
                l = net.links[lid]
                if l.rank >= 3 and ((not l.oneway) or l.a == n.id) and l.get("speed_kmh"):
                    t = _ctx(net, lid)
                    t["node"] = label
                    trig.append(Trigger("AFTER-MAJOR-INT", t, None, 0.0, depart=net.departure(lid, n.id),
                                        extra={"legend": f"{int(l.get('speed_kmh'))}"}, where=f"after {label} on {lid}"))
        # one-way
        thr = {(u.id, d.id) for u, d in through_pairs(net, n.id)}
        # one set of signs per one-way street: a one-way drawn as two links through the node counts once
        ow_links, seen_ow = [], set()
        for x in n.links:
            o = net.links[x]
            if not o.oneway or x in seen_ow:
                continue
            ow_links.append(o)
            seen_ow.add(x)
            for y in n.links:
                oy = net.links[y]
                if oy.oneway and y != x and ((x, y) in thr or (y, x) in thr or
                                             (o.get("name") and o.get("name") == oy.get("name"))):
                    seen_ow.add(y)
        for o in ow_links:
            for ap in net.approaches(n.id):
                if ap.link.id in seen_ow and ap.link.oneway and (ap.link.id == o.id or (ap.link.id, o.id) in thr or (o.id, ap.link.id) in thr):
                    continue
                if ap.link.id == o.id or (ap.link.id, o.id) in thr or (ap.link.oneway and ap.link.get("name") and ap.link.get("name") == o.get("name")):
                    continue
                t = _ctx(net, ap.link.id)
                t["node"] = label
                trig.append(Trigger("ONE-WAY-CROSSING", t, ap, 0.0,
                                    extra={"oneway_link": o.id, "flow_heading": heading(*(o.coords[:2]))},
                                    where=f"{label}: {ap.link.id} crossing one-way {o.id}"))
    def _split_join(nid):
        return junction_kind(net, nid) == "split"
    for o in net.links.values():
        if o.oneway and net.nodes[o.b].degree >= 2 and not _split_join(o.b):
            t = _ctx(net, o.id)
            t["node"] = net.node_label(o.b)
            trig.append(Trigger("ONE-WAY-EXIT", t, None, 0.0, depart=list(reversed(o.coords)),
                                extra={"node": o.b}, where=f"exit end of one-way {o.id} at {t['node']}"))
    # ------------ through movements (any node): speed change, lane drop
    for n in net.nodes.values():
        for up, dn in through_pairs(net, n.id):
            s_up, s_dn = up.get("speed_kmh"), dn.get("speed_kmh")
            ap = net.approach(up.id, n.id)
            if s_up and s_dn and abs(float(s_up) - float(s_dn)) >= 5:
                t = _ctx(net, up.id)
                t.update({"new_kmh": float(s_dn), "new_mph": mph(float(s_dn)), "node": net.node_label(n.id),
                          "reduction_kmh": float(s_up) - float(s_dn)})
                tg = Trigger("SPEED-ZONE", t, ap, 0.0, depart=net.departure(dn.id, n.id),
                             extra={"legend": f"{int(float(s_dn))}", "at_intersection": n.degree >= 3,
                                    "dn_link": dn.id}, where=f"speed change {up.id}->{dn.id}")
                trig.append(tg)
            if up.lanes > dn.lanes:
                t = _ctx(net, up.id)
                t["lanes_after"] = dn.lanes
                trig.append(Trigger("LANE-DROP", t, ap, 0.0, where=f"lane drop {up.id}->{dn.id}"))
    # ------------ cross-section changes (not at intersections): divided / undivided, one-way to two-way (2C.20, 2C.21, 2C.51)
    for n in net.nodes.values():
        if n.degree == 2:
            for up, dn in through_pairs(net, n.id):
                ap = net.approach(up.id, n.id)
                t = _ctx(net, up.id)
                t["node"] = net.node_label(n.id)
                t["to_two_lane"] = (not dn.oneway) and int(dn.props.get("lanes_total") or (dn.lanes or 1) * 2) == 2
                if not up.oneway and not dn.oneway and not up.divided and dn.divided:
                    trig.append(Trigger("DIVIDED-BEGIN", t, ap, 0.0, where=f"divided section begins {up.id}->{dn.id}"))
                elif not up.oneway and not dn.oneway and up.divided and not dn.divided:
                    trig.append(Trigger("DIVIDED-END", t, ap, 0.0, where=f"divided section ends {up.id}->{dn.id}"))
                elif up.oneway and not dn.oneway:
                    trig.append(Trigger("ONEWAY-TO-TWOWAY", t, ap, 0.0, where=f"one-way becomes two-way {up.id}->{dn.id}"))
        elif n.degree == 3:
            ls = [net.links[x] for x in n.links]
            ow = [l for l in ls if l.oneway]
            tw = [l for l in ls if not l.oneway]
            if junction_kind(net, n.id) == "split":
                inc = [l for l in ow if l.b == n.id]
                out = [l for l in ow if l.a == n.id]
                if len(inc) == 1 and len(out) == 1:
                    # two carriageways of a divided road meeting a two-way road (split / join node)
                    T = tw[0]
                    t = _ctx(net, T.id)
                    t["node"] = net.node_label(n.id)
                    trig.append(Trigger("DIVIDED-BEGIN", t, net.approach(T.id, n.id), 0.0,
                                        where=f"divided section begins {T.id}->{out[0].id}"))
                    t = _ctx(net, inc[0].id)
                    t["node"] = net.node_label(n.id)
                    t["to_two_lane"] = int(T.props.get("lanes_total") or (T.lanes or 1) * 2) == 2
                    trig.append(Trigger("DIVIDED-END", t, net.approach(inc[0].id, n.id), 0.0,
                                        where=f"divided section ends {inc[0].id}->{T.id}"))
            if len(ow) == 3:
                inc = [l for l in ls if l.b == n.id]
                out = [l for l in ls if l.a == n.id]
                if len(inc) == 2 and len(out) == 1:
                    o = out[0]
                    q = net.departure(o.id, n.id)
                    h_out = heading(q[0], q[1])

                    def dev(l):
                        p_ = net.towards(l.id, n.id)
                        return abs(norm_angle(heading(p_[-2], p_[-1]) - h_out))
                    major, ent = sorted(inc, key=dev)
                    if major.rank < ent.rank:
                        major, ent = ent, major
                    pm = net.towards(major.id, n.id)
                    pe = net.towards(ent.id, n.id)
                    hx, hy = pm[-1][0] - pm[-2][0], pm[-1][1] - pm[-2][1]
                    ex, ey = pe[-2][0] - pe[-1][0], pe[-2][1] - pe[-1][1]
                    side = "left" if hx * ey - hy * ex > 0 else "right"
                    added = (o.lanes or 1) >= (major.lanes or 1) + (ent.lanes or 1)
                    code = "ADDED-LANE" if added else "MERGE"
                    for role, l in (("major", major), ("entering", ent)):
                        t = _ctx(net, l.id)
                        t.update({"node": net.node_label(n.id), "role": role, "merge_side": side if role == "major" else
                                  ("left" if side == "right" else "right"), "equal": major.rank == ent.rank,
                                  "orientation": f"entering roadway from the {side}" if role == "major" else
                                  f"major roadway on the {'left' if side == 'right' else 'right'}"})
                        trig.append(Trigger(code, t, net.approach(l.id, n.id), 0.0,
                                            where=f"{code.lower()} {ent.id} into {major.id} ({role})"))
    # ------------ curves
    for l in net.links.values():
        curves = detect_curves(l.coords)
        L = l.length
        for c in curves:
            c.link = l.id
        net.curves.extend(curves)
        for direction in ("fwd", "rev"):
            if direction == "rev" and l.oneway:
                continue
            end_node = l.b if direction == "fwd" else l.a
            ap = net.approach(l.id, end_node)
            seq = []
            for c in curves:
                if direction == "fwd":
                    pc_back, pt_back, dlt = L - c.s0 + 0.0, L - c.s1, c.delta
                else:
                    pc_back, pt_back, dlt = c.s1, c.s0, -c.delta
                seq.append((pc_back, pt_back, dlt, c))
            seq.sort(key=lambda x: -x[0])  # in travel order (furthest from node first)
            e_default = 0.04 if l.urban else 0.06
            e = float(l.get("superelevation", e_default))
            posted_kmh = float(l.get("speed_kmh", 50))
            for k, (pc_back, pt_back, dlt, c) in enumerate(seq):
                adv_kmh = advisory_kmh(c.radius, e, posted_kmh)
                adv = mph(adv_kmh)                  # for the US-unit tables (2C-3, 2C-5)
                diff_kmh = posted_kmh - adv_kmh
                t = _ctx(net, l.id)
                chart_a = chart_a_level(t["class"], t["aadt"], l.props.get("markings"))
                sign = "W1-1" if adv_kmh <= 50 else "W1-2"   # 30 mph ~ 50 km/h
                reverse_next = False
                if k + 1 < len(seq):
                    nxt = seq[k + 1]
                    if (nxt[2] > 0) != (dlt > 0) and (pt_back - nxt[0]) < m_from_ft(600):
                        reverse_next = True
                        sign = "W1-3" if adv_kmh <= 50 else "W1-4"
                suppressed = k > 0 and getattr(seq[k - 1][3], "_rev_" + direction, False)
                if reverse_next:
                    setattr(c, "_rev_" + direction, True)
                t.update({"radius_m": round(c.radius, 1), "deflection_deg": round(math.degrees(abs(dlt)), 1),
                          "advisory_mph": adv, "advisory_kmh": adv_kmh, "diff_kmh": diff_kmh, "chart_a": chart_a, "orientation": "left" if dlt > 0 else "right",
                          "curve_sign": sign, "turn": "left" if dlt > 0 else "right", "e": e,
                          "suppress_sign": suppressed})
                trig.append(Trigger("CURVE", t, ap, pc_back, extra={"pt_back": pt_back, "aadt_known": l.get("aadt") is not None},
                                    where=f"curve on {l.id} ({direction}), R={c.radius:.0f} m"))
    # ------------ points of interest
    for p in net.pois.values():
        typ = str(p.props.get("type", "")).lower()
        if typ == "sign" and p.props.get("code"):
            code = str(p.props["code"]).strip().upper().replace("P", "P")
            best = None
            for l in net.links.values():
                s_, d_ = project_point(l.coords, p.xy)
                if best is None or d_ < best[2]:
                    best = (l, s_, d_)
            if not best or best[2] > 60:
                continue
            l, s_, _ = best
            facing = str(p.props.get("facing") or "fwd").lower()
            dirs = ["fwd", "rev"] if facing == "both" else (["rev"] if facing in ("rev", "b-a", "ba") else ["fwd"])
            for direction in dirs:
                end_node = l.b if direction == "fwd" else l.a
                back = (l.length - s_) if direction == "fwd" else s_
                t = _ctx(net, l.id)
                cat = (getattr(net, "sign_catalog", {}) or {}).get(code, {})
                t.update({"code": code, "request_provision": cat.get("default_provision", "Option"),
                          "request_basis": cat.get("default_basis", ""), "legend": p.props.get("legend", "")})
                trig.append(Trigger("SIGN-REQUEST", t, net.approach(l.id, end_node), back, extra={"poi": p.id},
                                    where=f"requested {code} at {p.id} on {l.id} ({direction})"))
            continue
        hz = getattr(net, "hazard_types", {}) or {}
        if typ in hz:
            best = None
            for l in net.links.values():
                s_, d_ = project_point(l.coords, p.xy)
                if best is None or d_ < best[2]:
                    best = (l, s_, d_)
            if not best or best[2] > 60:
                continue
            l, s_, _ = best
            facing = str(p.props.get("facing") or "both").lower()
            if facing == "both":
                dirs = ["fwd"] if l.oneway else ["fwd", "rev"]
            else:
                dirs = ["rev"] if facing in ("rev", "b-a", "ba") else ["fwd"]
            for direction in dirs:
                end_node = l.b if direction == "fwd" else l.a
                back = (l.length - s_) if direction == "fwd" else s_
                t = _ctx(net, l.id)
                for k, v in p.props.items():
                    if k not in t and k not in ("type", "id"):
                        t[k] = v
                t.update({"hazard": typ, "poi": p.id, "direction": direction,
                          "lane_width_m": float(l.props.get("lane_width_m") or getattr(l, "lane_w", 3.65) or 3.65)})
                trig.append(Trigger("HAZ-" + typ.upper(), t, net.approach(l.id, end_node), back, extra={"poi": p.id},
                                    where=f"{typ.replace('_', ' ')} {p.id} on {l.id} ({direction})"))
            continue
        if typ not in ("crosswalk", "school"):
            continue
        best = None
        for l in net.links.values():
            s, d = project_point(l.coords, p.xy)
            if best is None or d < best[2]:
                best = (l, s, d)
        if not best or best[2] > 60:
            continue
        l, s, _ = best
        near_node = min(s, l.length - s)
        if typ == "crosswalk" and near_node < 25:
            continue  # at an intersection: handled by intersection markings
        for direction in ("fwd", "rev"):
            if direction == "rev" and l.oneway:
                continue
            end_node = l.b if direction == "fwd" else l.a
            back = (l.length - s) if direction == "fwd" else s
            t = _ctx(net, l.id)
            code = "PED-XING-MIDBLOCK" if typ == "crosswalk" else "SCHOOL"
            t["school_zone"] = p.props.get("school_zone")
            if code == "PED-XING-MIDBLOCK":
                t["orientation"] = "points to crossing"
                t["yield_here_signs"] = bool(p.props.get("yield_here_signs"))
            trig.append(Trigger(code, t, net.approach(l.id, end_node), back, extra={"poi": p.id},
                                where=f"{typ} {p.id} on {l.id} ({direction})"))
    # ------------ base markings
    for l in net.links.values():
        t = _ctx(net, l.id)
        trig.append(Trigger("MARK-LINK", t, None, 0.0, extra={"link": l.id}, where=f"link {l.id}"))
    return trig
