"""Overrides (answers to data questions) and the missing-data pre-scan.

The engine never fills a gap silently. `prescan` lists every attribute a run needs that the
network does not have; the run stops and writes questions.json until overrides answer them.
"""
from __future__ import annotations
import json
from typing import Dict, List

from .cnm import Network

LINK_REQUIRED = {
    "class": ("Road class", "What is the functional class of each road (freeway, expressway, arterial, collector, local)?"),
    "speed_kmh": ("Posted speed", "What is the posted speed limit (km/h) on each road? One value per road class is fine."),
    "lanes": ("Lanes per direction", "How many through lanes per direction does each road have?"),
    "oneway": ("One-way roads", "Which roads are one-way? (Digitised direction = direction of travel.)"),
}
LINK_FOR_CURVES = {"aadt": ("Traffic volume (AADT)", "What is the AADT on roads with curves? MUTCD Table 2C-4 Chart A uses it to decide whether curve signs are required.")}
LINK_FOR_MARKINGS = {"aadt": ("Traffic volume (AADT)", "What is the AADT on each road? Centre and edge line requirements (3B.02, 3B.10) depend on it.")}
LINK_CONTEXT = {"urban": ("Urban or rural", "Is each road urban (kerbed, pedestrians, parking) or rural? It sets mounting height and lateral offset.")}


def load_overrides(path: str | None) -> Dict:
    if not path:
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def apply_overrides(net: Network, ov: Dict, settings: Dict):
    env = settings.get("env") or ["auto"]
    single_env = [e for e in env if e != "auto"]
    for l in net.links.values():
        layers = [ov.get("all_links", {}), ov.get("by_class", {}).get(str(l.props.get("class")), {}),
                  ov.get("links", {}).get(l.id, {})]
        for layer in layers:
            for k, v in (layer or {}).items():
                l.props[k] = v
                l.src[k] = "override"
        if "urban" not in l.props or l.props.get("urban") is None:
            if len(single_env) == 1 and single_env[0] in ("urban", "local"):
                l.props["urban"], l.src["urban"] = True, "settings"
            elif len(single_env) == 1 and single_env[0] in ("rural", "freeway"):
                l.props["urban"], l.src["urban"] = False, "settings"
            elif l.props.get("curb") is not None:
                l.props["urban"], l.src["urban"] = bool(l.props["curb"]), "derived"
    labels = {net.node_label(n): n for n in net.nodes}
    for n in net.nodes.values():
        for k, v in (ov.get("all_nodes") or {}).items():
            if n.degree >= 3 and n.props.get(k) in (None, ""):
                n.props[k] = v
    for key, vals in (ov.get("nodes") or {}).items():
        nid = key if key in net.nodes else labels.get(key)
        if nid:
            net.nodes[nid].props.update(vals)
    for pid, vals in (ov.get("pois") or {}).items():
        if pid in net.pois:
            net.pois[pid].props.update(vals)


def prescan(net: Network, settings: Dict, has_curves: bool) -> List[Dict]:
    """Return questions in dashboard format: {id, topic, question, items, suggested}."""
    qs: List[Dict] = []
    fam = set(settings.get("families") or [])

    def ask(attr, topic, text, items, suggested=""):
        if items:
            qs.append({"id": f"eng-{attr}", "topic": topic, "question": text,
                       "items": ", ".join(items[:60]) + (f" (+{len(items) - 60} more)" if len(items) > 60 else ""),
                       "suggested": suggested})

    need = dict(LINK_REQUIRED)
    need.update(LINK_CONTEXT)
    if "mark" in fam:
        need.update(LINK_FOR_MARKINGS)
    elif has_curves and "warn" in fam:
        need.update(LINK_FOR_CURVES)
    for attr, (topic, text) in need.items():
        missing = [l.id for l in net.links.values() if l.props.get(attr) in (None, "")]
        sug = {"oneway": "none are one-way", "lanes": "1"}.get(attr, "")
        ask(attr, topic, text, missing, sug)
    # intersections
    from .triggers import junction_kind
    nctl = [net.node_label(n.id) for n in net.nodes.values() if n.degree >= 3 and not n.props.get("control")
            and not junction_kind(net, n.id)]
    ask("control", "Intersection control",
        "What is the control type at each intersection: signal, stop_all, stop_minor, yield, roundabout or none?", nctl)
    amb = []
    for n in net.nodes.values():
        if n.props.get("control") in ("stop_minor", "yield") and not n.props.get("stop_approaches"):
            ranks = [net.links[l].rank for l in n.links]
            if len(set(ranks)) == 1:
                amb.append(net.node_label(n.id))
    rb_ = [net.node_label(n.id) for n in net.nodes.values()
           if n.props.get("control") == "roundabout" and not n.props.get("inscribed_radius_m")]
    ask("inscribed_radius_m", "Roundabout size",
        "What is the inscribed circle radius (centre to outer edge of the circulating roadway, m) of each roundabout? "
        "YIELD signs and yield lines go at the entry, on that circle.", rb_)
    ask("stop_approaches", "Minor approaches",
        "At these STOP/YIELD intersections all roads have the same class. Which approaches (link ids) are stop- or yield-controlled?", amb)
    # hazard points: attributes the hazard's rules need (rulebooks/<code>/hazards.yaml)
    hz = getattr(net, "hazard_types", {}) or {}
    for typ, spec in hz.items():
        pts = [p for p in net.pois.values() if str(p.props.get("type", "")).lower() == typ]
        if not pts:
            continue
        for attr, text in (spec.get("props") or {}).items():
            miss = [p.id for p in pts if p.props.get(attr) in (None, "")]
            ask(f"haz-{typ}-{attr}", spec.get("label", typ), text + " Answer per point id under overrides `pois`.", miss)
        if spec.get("facing") == "ask":
            miss = [p.id for p in pts if str(p.props.get("facing") or "").lower() not in ("fwd", "rev", "both")]
            ask(f"haz-{typ}-facing", spec.get("label", typ),
                "Which traffic direction does this point apply to: fwd, rev (relative to the drawn direction of the "
                "nearest road link) or both?", miss)
    return qs
