"""Rulebook loader and resolver. One folder per code; the engine never hard-codes a code's values."""
from __future__ import annotations
import csv
import math
import os
from typing import Dict, List, Optional

import yaml

from .geom import mph as to_mph, ft as to_ft, m_from_ft

CLASS_OF = {"Standard": "Mandatory", "Guidance": "Recommended", "Option": "Optional",
            "Support": "Note", "Study": "Conditional"}
CLASS_ORDER = {"Mandatory": 0, "Conditional": 1, "Recommended": 2, "Optional": 3, "Note": 4}

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _csv(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.startswith("#")]
    return list(csv.DictReader(lines))


def _safe_eval(expr, t: Dict):
    if isinstance(expr, (int, float, bool)):
        return expr
    return eval(str(expr), {"__builtins__": {}}, {"t": t, "mph": to_mph, "ft": to_ft, "min": min, "max": max, "int": int, "round": round, "float": float, "str": str,
                                                  "abs": abs, "True": True, "False": False, "None": None})


class Rulebook:
    def __init__(self, code: str, root: Optional[str] = None):
        self.dir = os.path.join(root or os.path.join(HERE, "rulebooks"), code)
        if not os.path.isdir(self.dir):
            raise RuntimeError(f"No rulebook for code '{code}' (looked in {self.dir})")
        with open(os.path.join(self.dir, "code.yaml"), encoding="utf-8") as fh:
            self.meta = yaml.safe_load(fh)
        with open(os.path.join(self.dir, "rules.yaml"), encoding="utf-8") as fh:
            self.rules = yaml.safe_load(fh)["rules"]
        self.devices = {r["code"]: r for r in _csv(os.path.join(self.dir, "devices.csv"))}
        self.markings = {r["code"]: r for r in _csv(os.path.join(self.dir, "markings.csv"))}
        t = os.path.join(self.dir, "tables")
        self.advance = _csv(os.path.join(t, "advance_placement.csv"))
        self.chevron = _csv(os.path.join(t, "chevron_spacing.csv"))
        self.mounting = {r["context"]: r for r in _csv(os.path.join(t, "mounting.csv"))}
        self.code = code
        import json as _json
        cp = os.path.join(self.dir, "sign_catalog.json")
        self.sign_catalog = _json.load(open(cp, encoding="utf-8")) if os.path.exists(cp) else {}
        hp = os.path.join(self.dir, "hazards.yaml")
        self.hazards = (yaml.safe_load(open(hp, encoding="utf-8")) or {}).get("hazards", {}) if os.path.exists(hp) else {}

    # ------------------------------------------------------------ rules
    def rules_for(self, trigger: str) -> List[Dict]:
        out = []
        for r in self.rules:
            tr = r["trigger"]
            if (isinstance(tr, list) and trigger in tr) or tr == trigger:
                out.append(r)
        return out

    def resolve(self, trigger: str, t: Dict) -> List[Dict]:
        """Return resolved device requirements for a trigger context."""
        res = []
        for r in self.rules_for(trigger):
            try:
                if r.get("when") and not _safe_eval(r["when"], t):
                    continue
            except (KeyError, TypeError):
                continue
            prov = r["provision"]
            if isinstance(prov, str) and prov.startswith("{"):
                prov = _safe_eval(prov.strip("{}"), t)
            for alt in r.get("provision_if", []) or []:
                try:
                    if _safe_eval(alt["when"], t):
                        prov = alt["provision"]
                        break
                except (KeyError, TypeError):
                    continue
            comps = []
            for c in r.get("companions", []) or []:
                if isinstance(c, str):  # plain code: same provision as the main sign
                    comps.append({"device": c, "provision": prov, "class": CLASS_OF[prov],
                                  "clause": r.get("clause", "")})
                    continue
                if c.get("when"):
                    try:
                        if not _safe_eval(c["when"], t):
                            continue
                    except (KeyError, TypeError):
                        continue
                cp = c.get("provision", prov)
                for alt in c.get("provision_if", []) or []:
                    try:
                        if _safe_eval(alt["when"], t):
                            cp = alt["provision"]
                            break
                    except (KeyError, TypeError):
                        continue
                cl = c.get("legend", "")
                if isinstance(cl, str) and cl.startswith("{"):
                    try:
                        cl = _safe_eval(cl.strip("{}"), t)
                    except (KeyError, TypeError, ValueError):
                        cl = ""
                comps.append({"device": c["device"], "provision": cp, "class": CLASS_OF[cp],
                              "clause": c.get("clause", r.get("clause", "")), "legend": cl})
            dev = r["device"]
            if isinstance(dev, str) and dev.startswith("{"):
                dev = _safe_eval(dev.strip("{}"), t)
            leg = r.get("legend", "")
            if isinstance(leg, str) and leg.startswith("{"):
                try:
                    leg = _safe_eval(leg.strip("{}"), t)
                except (KeyError, TypeError, ValueError):
                    leg = ""
            res.append({"rule": r, "device": dev, "legend": leg, "provision": prov, "class": CLASS_OF[prov],
                        "clause": (_safe_eval(r["clause"].strip("{}"), t) if str(r.get("clause", "")).startswith("{") else r.get("clause", "")), "study": r.get("study", ""),
                        "companions": comps, "kind": r.get("kind", "sign"),
                        "verify": bool(r.get("verify", False))})
        return res

    # ------------------------------------------------------------ tables
    def advance_distance_m(self, speed_kmh: float, condition: str, advisory_mph: Optional[float] = None):
        """Table lookup. Speed is rounded UP to the next 5 mph row (conservative);
        advisory speed rounded DOWN to the table column (conservative). Returns (metres, note)."""
        s = to_mph(speed_kmh)
        rows = sorted(self.advance, key=lambda r: int(r["speed_mph"]))
        row = rows[-1]
        for r in rows:
            if int(r["speed_mph"]) >= s - 0.1:
                row = r
                break
        if condition.upper() == "A":
            return m_from_ft(float(row["cond_a"])), f"Table 2C-3 Cond. A @ {row['speed_mph']} mph"
        adv = max(0.0, float(advisory_mph or 0))
        col = int(math.floor(adv / 10.0) * 10)
        v = row.get(f"b{col}", "")
        if v in ("", None):
            return m_from_ft(100.0), f"Table 2C-3 Cond. B @ {row['speed_mph']}/{col} mph: N/A -> 100 ft (note 5/6)"
        return m_from_ft(float(v)), f"Table 2C-3 Cond. B @ {row['speed_mph']}/{col} mph"

    def chevron_spacing_m(self, advisory_mph: float = None, advisory_kmh: float = None) -> float:
        """Chevron spacing by advisory speed. Metric input uses the table's km/h bands (AASHTO pairing)."""
        for r in self.chevron:
            if advisory_kmh is not None and r.get("advisory_max_kmh"):
                if advisory_kmh <= float(r["advisory_max_kmh"]) + 1e-6:
                    return m_from_ft(float(r["spacing_ft"]))
            elif advisory_mph is not None and advisory_mph <= float(r["advisory_max_mph"]):
                return m_from_ft(float(r["spacing_ft"]))
        return m_from_ft(200.0)

    def mount(self, context: str) -> Dict:
        r = self.mounting.get(context) or self.mounting["rural"]
        return {"height_m": round(m_from_ft(float(r["min_height_ft"])), 2),
                "offset_m": round(m_from_ft(float(r["lateral_offset_ft"])), 2),
                "offset_ref": r["offset_reference"],
                "clause": f"{r['height_clause']} ({r['height_provision']}); {r['offset_clause']} ({r['offset_provision']})"}

    def size(self, code: str, size_class: str) -> str:
        d = self.devices.get(code)
        if not d:
            return ""
        order = {"conv_single": ["conv_single", "conv_multi", "expressway"],
                 "conv_multi": ["conv_multi", "expressway", "conv_single"],
                 "expressway": ["expressway", "freeway", "conv_multi", "conv_single"],
                 "freeway": ["freeway", "expressway", "oversized", "conv_multi"],
                 "minimum": ["minimum", "conv_single"], "oversized": ["oversized", "freeway", "expressway"]}
        for k in order.get(size_class, ["conv_single"]):
            if d.get(k):
                return d[k]
        return ""
