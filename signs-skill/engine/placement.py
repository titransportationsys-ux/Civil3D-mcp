"""Placement engine: turns resolved rules into positioned devices, then QA (spacing, conflicts)."""
from __future__ import annotations
import math
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional

from .cnm import Network
from .geom import (dist, heading, length, m_from_ft, offset_point, point_along, mph, kmh)
from .rulebook import CLASS_ORDER, Rulebook
from .triggers import Trigger

FAMILY_KEY = {"regulatory": "reg", "warning": "warn", "school": "warn"}
PRIORITY = {"regulatory": 0, "school": 1, "warning": 2}


@dataclass
class Device:
    id: str
    code: str
    name: str
    kind: str                 # sign | marking
    family: str
    cls: str                  # Mandatory | Recommended | Optional | Conditional
    provision: str
    clause: str
    rule_id: str
    trigger: str
    where: str
    link: str = ""
    node: str = ""
    x: Optional[float] = None
    y: Optional[float] = None
    side: str = ""
    offset_m: Optional[float] = None
    height_m: Optional[float] = None
    back_m: Optional[float] = None
    azimuth_deg: Optional[float] = None
    size: str = ""
    legend: str = ""
    orientation: str = ""
    support: str = ""
    companions: str = ""
    quantity: Optional[float] = None
    unit: str = ""
    geometry: Optional[List] = None     # for markings (polyline)
    confidence: str = "High"
    study: str = ""
    notes: List[str] = field(default_factory=list)
    code_source: str = ""
    verify: bool = True

    def row(self) -> Dict:
        d = asdict(self)
        d["notes"] = "; ".join(self.notes)
        d.pop("geometry", None)
        return d


def size_class(net: Network, lid: str, setting: str) -> str:
    if setting and setting != "auto":
        return {"conventional": "conv_single"}.get(setting, setting)
    l = net.links[lid]
    c = str(l.get("class", "local"))
    if c == "freeway":
        return "freeway"
    if c == "expressway":
        return "expressway"
    return "conv_multi" if l.lanes >= 2 else "conv_single"


def mount_context(net: Network, lid: str) -> str:
    l = net.links[lid]
    if str(l.get("class")) in ("freeway", "expressway"):
        return "freeway"
    return "urban" if l.urban else "rural"


class Placer:
    def __init__(self, net: Network, rb: Rulebook, settings: Dict):
        self.net, self.rb, self.st = net, rb, settings
        self.devs: List[Device] = []
        self.n = 0
        self.supports = 0
        self.side_sign = -1 if settings.get("drive") == "left" else 1
        self.seen_markings = set()
        self.log: List[str] = []

    # --------------------------------------------------------------- helpers
    def _id(self, kind):
        self.n += 1
        return f"{'S' if kind == 'sign' else 'M'}{self.n:04d}"

    def _catalog(self, code, kind):
        if kind == "marking":
            m = self.rb.markings.get(code, {})
            return m.get("name", code), "markings"
        d = self.rb.devices.get(code, {})
        return d.get("official_name") or d.get("name", code), d.get("family", "warning")

    def _legend(self, code, legend, t):
        """Legend text: explicit legend wins; else the catalog template ({speed} filled from context)."""
        if legend:
            return legend
        tpl = self.rb.devices.get(code, {}).get("legend", "")
        if "{speed}" in tpl:
            v = t.get("new_kmh") or t.get("speed_kmh")
            return tpl.replace("{speed}", self._speed_legend(float(v))) if v else tpl
        return tpl

    def _orientation(self, code, side, t, extra=None):
        if self.rb.devices.get(code, {}).get("orientation") != "lr":
            return ""
        if extra:
            return extra
        if code == "W16-7P":
            return "arrow down-left (toward crossing)" if side == "right" else "arrow down-right (toward crossing)"
        if code in ("W4-2",):
            return "CONFIRM which lane ends (left or right)"
        o = t.get("orientation", "")
        return o if o else "CONFIRM left/right"

    def _kerb(self, p, h, sgn, window):
        """Distance from centreline point p to the outermost kerb/edge line on side sgn within `window` m
        (outermost, so a splitter-island edge or bay line is passed over). None if no edge data or no hit."""
        segs = getattr(self.net, "edges", None)
        if not segs:
            return None
        dx, dy = sgn * math.sin(h), -sgn * math.cos(h)
        hits = []
        for a, b in segs:
            ex, ey = b[0] - a[0], b[1] - a[1]
            den = dx * ey - dy * ex
            if abs(den) < 1e-12:
                continue
            t = ((a[0] - p[0]) * ey - (a[1] - p[1]) * ex) / den
            u = ((a[0] - p[0]) * dy - (a[1] - p[1]) * dx) / den
            if 0.3 < t <= window and 0 <= u <= 1:
                hits.append(t)
        return max(hits) if hits else None

    def _sign_at(self, path, back, lid, side, conf_notes, fixed=False, max_back=None):
        """Point `back` metres before the end of path, offset to `side`. With kerb lines loaded, the offset is
        measured from the real kerb; a sign at the stop line is slid upstream off a kerb return."""
        L = length(path)
        s = L - back
        notes = []
        if s < 0:
            notes.append(f"advance distance not available: needed {back:.0f} m, approach is {L:.0f} m; placed at start of approach")
            s = 0
        l = self.net.links[lid]
        ctx = mount_context(self.net, lid)
        mnt = self.rb.mount(ctx)
        sgn = self.side_sign if side in ("right", "outside_right") else -self.side_sign
        nominal = l.half_width_dir() if (side != "left" or l.oneway) else l.lanes * l.lane_w
        window = nominal + 3.5 + float(l.get("shoulder_m", 0) or 0)
        p, h = point_along(path, s)
        k = self._kerb(p, h, sgn, window)
        if fixed and getattr(self.net, "edges", None):
            # at the junction the kerb return curves away: slide upstream (within 50 ft of the intersected edge,
            # 2B.18) to the first point where the kerb is straight and at least 3/4 of the nominal half-width out
            s0, found = s, False
            lim = max(L - (max_back if max_back else back + 15.0), 0)
            s_try = s
            while s_try >= lim:
                pt, ht = point_along(path, s_try)
                k1 = self._kerb(pt, ht, sgn, window)
                pu, hu = point_along(path, max(s_try - 5, 0))
                k2 = self._kerb(pu, hu, sgn, window)
                if k1 is not None and k2 is not None and k1 >= 0.75 * nominal and abs(k1 - k2) < 0.3:
                    s, p, h, k, found = s_try, pt, ht, k1, True
                    break
                s_try -= 0.5
            if found and s0 - s > 0.01:
                conf_notes.append(f"moved {s0 - s:.1f} m upstream to clear the kerb return")
            elif not found:
                conf_notes.append("no straight kerb found within 50 ft of the junction: check position on plan")
                self._low = True
        if k is not None:
            off = k + mnt["offset_m"]
            conf_notes.append(f"offset from drawn kerb ({k:.2f} m from centreline)")
        else:
            off = nominal + float(l.get("shoulder_m", 0) or 0) + mnt["offset_m"]
            if getattr(self.net, "edges", None):
                conf_notes.append("no kerb line found: nominal offset used")
        q = offset_point(p, h, sgn * off)
        az = (90 - math.degrees(h + math.pi)) % 360  # sign face azimuth (compass, faces oncoming traffic)
        return q, az, round(off, 2), mnt, notes, round(L - s, 1)

    def add_sign(self, trg: Trigger, res: Dict, code: str, path, back, side, legend="", extra_notes=None,
                 conf="High", support=None):
        lid = trg.t.get("link")
        name, fam = self._catalog(code, "sign")
        kn = []
        fixed = (trg.approach is not None and abs(back - trg.back_m) < 0.01 and
                 res["rule"].get("placement", {}).get("kind") in ("at_stop_line",))
        maxb = (self.net.crossing_half_width(trg.approach.node.id, trg.approach.link.id) + 15.2) if fixed else None
        q, az, off, mnt, notes, back_eff = self._sign_at(path, back, lid, side, kn, fixed, maxb)
        extra_notes = list(extra_notes or []) + kn
        sc = size_class(self.net, lid, self.st.get("size", "auto"))
        if support is None:
            self.supports += 1
            support = f"P{self.supports:04d}"
        orient = self._orientation(code, side, trg.t, getattr(self, "_orient_override", None))
        if code == "R2-1" and legend and not legend.startswith("SPEED LIMIT"):
            legend = f"SPEED LIMIT {legend}"
        if code.startswith("R6-") and legend.startswith("arrow "):
            orient, legend = f"arrow points {legend.split()[1]}", "ONE WAY"
        d = Device(self._id("sign"), code, name, "sign", fam, res["class"], res["provision"], res["clause"],
                   res["rule"]["id"], trg.trigger, trg.where, link=lid, node=str(trg.t.get("node", "")),
                   x=round(q[0], 3), y=round(q[1], 3), side=side, offset_m=off,
                   height_m=mnt["height_m"], back_m=back_eff, azimuth_deg=round(az, 1),
                   size=self.rb.size(code, sc), legend=self._legend(code, legend, trg.t), orientation=orient,
                   support=support,
                   companions="", confidence=conf, study=res.get("study", ""),
                   notes=list(notes) + list(extra_notes or []) + [f"mount: {mnt['clause']}"],
                   code_source=self.rb.code, verify=res.get("verify", True))
        if notes or getattr(self, "_low", False):
            d.confidence = "Low"
        self._low = False
        d._path, d._side = path, side
        d._fixed = (trg.approach is not None and back <= (trg.back_m + 0.01) and
                    res["rule"].get("placement", {}).get("kind") in ("at_stop_line", "at_node_facing_cross", "at_exit_end"))
        d._grp = (trg.approach.key if trg.approach else trg.where, side)
        self.devs.append(d)
        keep = self.st.get("_keep")
        for cr in res.get("companions", []) or []:
            if isinstance(cr, str):
                cr = {"device": cr, "provision": d.provision, "class": d.cls, "clause": d.clause}
            comp = cr["device"]
            if keep and cr["class"] not in keep:
                self.log.append(f"{comp} with {d.id} {d.code} not placed: {cr['class']} ({cr['clause']}) "
                                f"is below the selected level")
                continue
            cname, cfam = self._catalog(comp, "sign")
            pq = Device(self._id("sign"), comp, cname, "sign", cfam, cr["class"], cr["provision"], cr["clause"], d.rule_id,
                        d.trigger, d.where, link=d.link, node=d.node, x=d.x, y=d.y, side=d.side,
                        offset_m=d.offset_m, height_m=d.height_m,
                        back_m=d.back_m, azimuth_deg=d.azimuth_deg, size=self.rb.size(comp, sc), support=d.support,
                        legend=(self._speed_legend(float(cr["legend"]), advisory=True) if isinstance(cr.get("legend"), (int, float))
                                and not isinstance(cr.get("legend"), bool) else self._legend(comp, cr.get("legend", "") or "", trg.t)), orientation=self._orientation(comp, side, trg.t),
                        confidence=d.confidence, notes=[f"plaque below {d.id} {d.code}"], code_source=self.rb.code,
                        verify=d.verify)
            pq._companion_of = d
            self.devs.append(pq)
            d.companions = ", ".join(x for x in (d.companions, comp) if x)
            try:
                ph = float(pq.size.split("x")[1]) * 0.0254 if pq.size else 0.3
            except (IndexError, ValueError):
                ph = 0.3
            d.height_m = round((d.height_m or 0) + ph + 0.05, 2)
            d.notes.append(f"bottom raised {ph + 0.05:.2f} m for plaque {comp} below (2A.15)")
        return d

    def add_marking(self, trg: Trigger, res: Dict, code: str, qty: float, unit: str, geom=None, key=None,
                    extra_notes=None):
        if key:
            if key in self.seen_markings:
                return None
            self.seen_markings.add(key)
        name, _ = self._catalog(code, "marking")
        d = Device(self._id("marking"), code, name, "marking", "markings", res["class"], res["provision"],
                   res["clause"], res["rule"]["id"], trg.trigger, trg.where, link=str(trg.t.get("link", "")),
                   node=str(trg.t.get("node", "")), quantity=round(qty, 1), unit=unit, geometry=geom,
                   study=res.get("study", ""), notes=list(extra_notes or []), code_source=self.rb.code,
                   verify=res.get("verify", True))
        self.devs.append(d)
        return d

    # --------------------------------------------------------------- placement kinds
    def place(self, trg: Trigger, res: Dict):
        pl = res["rule"].get("placement", {})
        kind = pl.get("kind")
        code = res["device"]
        side = pl.get("side", "right")
        t = trg.t
        if isinstance(side, str) and side.startswith("{"):
            from .rulebook import _safe_eval
            side = _safe_eval(side.strip("{}"), t)
        legend = trg.extra.get("legend", "") or (t.get("legend", "") if trg.trigger == "SIGN-REQUEST" else "") or res.get("legend", "")
        if code in ("R2-1",) and legend and str(legend).replace(".", "").isdigit():
            legend = self._speed_legend(float(legend))
        if kind == "at_stop_line":
            self.add_sign(trg, res, code, trg.approach.path, trg.back_m, side, legend)
        elif kind == "at_point":
            sides = ["right", "left"] if side == "both" else [side]
            if trg.extra.get("at_intersection") and trg.depart:
                # change point is an intersection: post the new limit just beyond it (2B.21)
                dd = self.net.crossing_half_width(trg.approach.node.id, trg.approach.link.id) + 30.0
                path = trg.depart
                if length(path) > dd + 5:
                    trg.t["link"] = trg.extra.get("dn_link", trg.t["link"])
                    self.add_sign(trg, res, code, path, length(path) - dd, "right", legend,
                                  [f"{dd:.0f} m beyond the intersection"])
                    trg.t["link"] = trg.approach.link.id
                return
            add = float(pl.get("back_add_m", 0) or 0)
            pnotes = [pl["note"]] if pl.get("note") else []
            for sd in sides:
                self.add_sign(trg, res, code, trg.approach.path, trg.back_m + add, sd, legend, pnotes,
                              pl.get("confidence", "High"))
        elif kind == "advance":
            spd = t["speed_kmh"]
            adv = pl.get("advisory_mph", 0)
            if isinstance(adv, str):
                from .rulebook import _safe_eval
                adv = _safe_eval(adv, t)
            d, note = self.rb.advance_distance_m(spd, pl.get("condition", "B"), adv)
            notes = [f"advance {d:.0f} m ({note})"]
            leg = legend
            if code in ("W3-5",):
                leg = self._speed_legend(t["new_kmh"])
            comp_legend = ""
            if code.startswith("W1-") and code != "W1-8":
                comp_legend = self._speed_legend(t["advisory_kmh"], advisory=True)
                notes.append(f"advisory speed {comp_legend} from R={t['radius_m']} m, e={t['e']} "
                             f"(FHWA ball-bank method approximation; confirm with ball-bank study)")
            conf = "Medium" if code.startswith("W1-") else pl.get("confidence", "High")
            if pl.get("note"):
                notes.append(pl["note"])
            dv = self.add_sign(trg, res, code, trg.approach.path, trg.back_m + d, side, leg, notes, conf)
            if comp_legend:
                for pq in self.devs:
                    if getattr(pq, "_companion_of", None) is dv and pq.code == "W13-1P":
                        pq.legend = comp_legend
        elif kind == "along_curve":
            pt_back = trg.extra["pt_back"]
            pc_back = trg.back_m
            sp = self.rb.chevron_spacing_m(advisory_kmh=t["advisory_kmh"]) * float(pl.get("spacing_scale", 1.0))
            outside = "right" if t["turn"] == "left" else "left"
            n = max(2, int((pc_back - pt_back) / sp) + 1)
            first = None
            for k in range(n + 1):
                b = pc_back - k * sp
                if b < pt_back - 1:
                    break
                dv = self.add_sign(trg, res, code, trg.approach.path, b, outside, "",
                                   [f"spacing {sp:.0f} m (Table 2C-5)"], "Medium")
                first = first or dv
        elif kind == "curve_outside":
            # one sign on the outside of the curve, in line with approaching traffic (W1-6, 2C.10-04)
            pt_back, pc_back = trg.extra["pt_back"], trg.back_m
            b = pc_back - min(0.5 * (pc_back - pt_back), 0.5 * t["radius_m"])
            outside = "right" if t["turn"] == "left" else "left"
            self.add_sign(trg, res, code, trg.approach.path, b, outside, "",
                          ["on the outside of the curve in line with approaching traffic (2C.10-04); check visibility on site (2C.10-07)"],
                          "Medium")
        elif kind == "downstream":
            path = trg.depart
            dd = float(pl.get("distance_m", 60))
            if length(path) < dd + 5:
                return
            s_back = length(path) - dd
            q_path = list(path)
            v = t.get(pl["legend"]) if pl.get("legend") else t["speed_kmh"]
            self.add_sign(trg, res, code, q_path, s_back, side, self._speed_legend(v),
                          [f"{dd:.0f} m inside the boundary; adjust to the gate position"] if trg.trigger == "BOUNDARY-ENTRY" else None)
        elif kind == "at_node_facing_cross":
            ap = trg.approach
            o = self.net.links[trg.extra["oneway_link"]]
            # near-right corner of the crossing approach, and far-left corner
            arrow = "left" if math.sin(trg.extra["flow_heading"] - heading(ap.path[-2], ap.path[-1])) > 0 else "right"
            node = ap.node
            tee = node.degree == 3
            ctl = str(node.props.get("control", "") if hasattr(node, "props") else "").lower()
            extra = []
            if ctl == "signal":
                extra.append("signalised: may instead go near the signal faces, on the signal pole, mast arm or span wire (2B.49-10)")
            self.add_sign(trg, res, code, ap.path, max(o.width_total() / 2 + 1.5, 3), "right",
                          f"arrow {arrow}", ["near-right corner (2B.49-09); position approximate, adjust on plan"] + extra, "Low")
            p, h = ap.path[-1], heading(ap.path[-2], ap.path[-1])
            far = (p[0] + math.cos(h) * (o.width_total() / 2 + 3), p[1] + math.sin(h) * (o.width_total() / 2 + 3))
            where_far = ("far side facing the stem approach (T-intersection, 2B.49-11)" if tee
                         else "far-left corner (2B.49-09)")
            self.add_sign(trg, res, code, ap.path + [far], 0.0, "left", f"arrow {arrow}",
                          [f"{where_far}; position approximate, adjust on plan"] + extra, "Low")
        elif kind == "at_exit_end":
            path = trg.depart  # travels against flow, away from the node
            node = self.net.nodes[trg.extra["node"]]
            hw = self.net.crossing_half_width(node.id, t["link"])
            s = hw + 3.0
            if length(path) < s + 1:
                return
            # sign faces traffic that would enter the one-way link from the node
            sub = [path[0], point_along(path, s)[0]]
            for sd in ("right", "left"):
                self.add_sign(trg, res, code, sub, 0.0, sd, "", ["faces traffic entering against the one-way flow"], "Medium")
        elif kind == "stop_line":
            ap = trg.approach
            l = ap.link
            w = l.half_width_dir() if not l.oneway else l.lanes * l.lane_w
            p, h = point_along(ap.path, length(ap.path) - trg.back_m)
            a = offset_point(p, h, 0 if not l.oneway else -self.side_sign * w / 2)
            b = offset_point(a, h, self.side_sign * w)
            self.add_marking(trg, res, code, w, "m", [a, b], key=(code, ap.key))
        elif kind == "lane_symbol":
            # one symbol per approach lane before the point (e.g. RXR opposite the W10-1 sign, 8C.02-08)
            l = self.net.links[t["link"]]
            n = l.lanes if l.lanes else 1
            if pl.get("condition"):
                d, note = self.rb.advance_distance_m(t["speed_kmh"], pl["condition"], pl.get("advisory_mph", 0))
                where = f"{d:.0f} m before the point ({note})"
            else:
                where = f"{float(pl.get('back_add_m', 0) or 0):.0f} m before the point"
            geom = None
            if trg.approach is not None:
                dd = d if pl.get("condition") else float(pl.get("back_add_m", 0) or 0)
                ap = trg.approach
                L_ = length(ap.path)
                pp, hh = point_along(ap.path, max(0.0, L_ - trg.back_m - dd))
                w = l.half_width_dir() if not l.oneway else l.lanes * l.lane_w
                a = offset_point(pp, hh, 0 if not l.oneway else -self.side_sign * w / 2)
                geom = [a, offset_point(a, hh, self.side_sign * w)]
            self.add_marking(trg, res, code, n, "ea", geom,
                             key=(code, trg.extra.get("poi"), trg.approach.key if trg.approach else ""),
                             extra_notes=[f"{n} symbol(s), one per approach lane, {where}"]
                             + ([pl["note"]] if pl.get("note") else []))
        elif kind == "crosswalk":
            if trg.approach and trg.trigger.startswith("INT"):
                l = trg.approach.link
                self.add_marking(trg, res, code, 3.0 * l.width_total(), "m2", None,
                                 key=(code, trg.approach.key.split(">")[1], l.id),
                                 extra_notes=[f"3.0 m wide across {self.net.link_name(l.id)}"])
            else:
                l = self.net.links[t["link"]]
                self.add_marking(trg, res, code, 3.0 * l.width_total(), "m2", None,
                                 key=(code, trg.extra.get("poi")), extra_notes=["mid-block crosswalk, 3.0 m wide"])
        elif kind == "taper":
            l = trg.approach.link
            W, S = l.lane_w, t["speed_kmh"]          # metric forms: 45 mph ~ 70 km/h (AASHTO)
            Lm = W * S / 1.6 if S >= 70 else W * S * S / 155
            self.add_marking(trg, res, code, Lm, "m", None, key=(code, trg.approach.key),
                             extra_notes=[f"taper L = {'WS/1.6' if S >= 70 else 'WS^2/155'} = {Lm:.0f} m "
                                          f"(3B.12 L=WS / WS^2/60 in metric form)"])
        elif kind == "link_line":
            self._link_line(trg, res, code, pl.get("offset"))
        elif kind == "link_note":
            self.add_marking(trg, res, code, self.net.links[t["link"]].length, "m", None,
                             key=(code, t["link"]), extra_notes=["study item: survey passing sight distance"])

    def _speed_legend(self, v_kmh: float, advisory=False) -> str:
        if self.st.get("units") == "us":
            v = int(round(mph(v_kmh) / 5) * 5)
            return f"{v} MPH"
        step = 10
        v = int(math.floor(v_kmh / step) * step) if advisory else int(round(v_kmh))
        return f"{v} km/h"

    def _link_line(self, trg, res, code, which):
        l = self.net.links[trg.t["link"]]
        trim = 0.0
        for nid in (l.a, l.b):
            if self.net.nodes[nid].degree >= 3:
                trim += self.net.crossing_half_width(nid, l.id) + 1.2
        Lnet = max(l.length - trim, 0)
        dirs = 1 if l.oneway else 2
        if which == "center":
            self.add_marking(trg, res, code, Lnet, "m", None, key=(code, l.id),
                             extra_notes=["pattern (solid/broken) per passing zones; double solid assumed until no-passing study"])
        elif which == "right_edge":
            self.add_marking(trg, res, "EL-SW", Lnet * dirs, "m", None, key=("EL-SW", l.id),
                             extra_notes=[f"{dirs} edge line(s)"])
            if l.oneway or l.divided:
                self.add_marking(trg, res, "EL-SY", Lnet, "m", None, key=("EL-SY", l.id),
                                 extra_notes=["left edge line on one-way / divided roadway"])
        elif which == "lane_lines":
            n = (l.lanes - 1) * dirs
            if n > 0:
                self.add_marking(trg, res, code, Lnet * n, "m", None, key=(code, l.id),
                                 extra_notes=[f"{n} lane line(s); painted length = 25% (10 ft / 30 ft pattern)"])


# ------------------------------------------------------------------ QA
def qa_spacing(placer: "Placer", min_m: float) -> List[str]:
    """Keep min spacing between separate supports along one approach and side (Table 2C-3 note 6).
    Lower-priority signs move upstream; every move is logged on the device."""
    log = []
    groups: Dict[tuple, List[Device]] = {}
    for d in placer.devs:
        if d.kind != "sign" or d.code in ("W1-8", "DELINEATOR") or d.back_m is None or not hasattr(d, "_grp"):
            continue
        groups.setdefault(d._grp, []).append(d)
    for key, g in groups.items():
        g.sort(key=lambda d: (d.back_m, PRIORITY.get(d.family, 3)))
        for i in range(1, len(g)):
            prev, cur = g[i - 1], g[i]
            gap = cur.back_m - prev.back_m
            if prev.support == cur.support or gap >= min_m or getattr(cur, "_fixed", False):
                continue
            if cur.code == prev.code and abs(gap) < 1:
                continue
            shift = min_m - gap
            q, az, off, mnt, notes, back_eff = placer._sign_at(cur._path, cur.back_m + shift, cur.link, cur._side, [])
            cur.x, cur.y, cur.back_m = round(q[0], 3), round(q[1], 3), back_eff
            cur.notes.append(f"moved {shift:.0f} m upstream to keep {min_m:.0f} m from {prev.id} ({prev.code})")
            if notes:
                cur.notes += notes
                cur.confidence = "Low"
            elif cur.confidence == "High":
                cur.confidence = "Medium"
            log.append(f"{cur.id} {cur.code} at {cur.where}: moved {shift:.0f} m upstream (spacing to {prev.id} {prev.code})")
    return log


def qa_conflicts(devs: List[Device], net: Network) -> List[str]:
    issues = []
    by_node: Dict[str, set] = {}
    for d in devs:
        if d.code in ("R1-1", "R1-2") and d.node:
            by_node.setdefault(d.node, set()).add(d.code)
    for n, codes in by_node.items():
        if {"R1-1", "R1-2"} <= codes:
            issues.append(f"{n}: STOP and YIELD on the same intersection - check 2B.06-09 (not on conflicting approaches)")
    for n in net.nodes.values():
        if n.props.get("control") == "signal":
            lab = net.node_label(n.id)
            if any(d.node == lab and d.code in ("R1-1", "R1-2") for d in devs):
                issues.append(f"{lab}: STOP/YIELD at a signal - 2B.06-08")
    return issues
