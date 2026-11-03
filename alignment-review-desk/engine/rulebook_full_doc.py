"""Full MUTCD sign rule book: every sign in the manual, grouped by its governing section.

    python -m engine.rulebook_full_doc --out Rulebook_MUTCD_11e_Full.md [--html Rulebook_MUTCD_11e_Full.html]

Built from rulebooks/<code>/sign_catalog.json (sizes from the MUTCD size tables, provisions from
the section text, pictures in symbols/). The HTML version embeds small pictures so it opens anywhere.
"""
from __future__ import annotations
import argparse
import base64
import io
import json
import os
import re
from collections import OrderedDict, defaultdict
from datetime import date

from .rulebook import HERE

PARTS = {"1": "Part 1 General", "2": "Part 2 Signs", "3": "Part 3 Markings", "4": "Part 4 Highway Traffic Signals",
         "5": "Part 5 Automated Vehicles", "6": "Part 6 Temporary Traffic Control", "7": "Part 7 School Areas",
         "8": "Part 8 Railroad and Light Rail Grade Crossings", "9": "Part 9 Bicycle Facilities"}
CHAPTERS = {"2A": "General", "2B": "Regulatory Signs", "2C": "Warning Signs and Object Markers", "2D": "Guide Signs, Conventional Roads",
            "2E": "Guide Signs, Freeways and Expressways", "2F": "Toll Road Signs", "2G": "Preferential and Managed Lane Signs",
            "2H": "General Information Signs", "2I": "General Service Signs", "2J": "Specific Service Signs",
            "2K": "Tourist-Oriented Directional Signs", "2L": "Changeable Message Signs", "2M": "Recreational and Cultural Interest Area Signs",
            "2N": "Emergency Management Signing", "6G": "TTC Regulatory Signs", "6H": "TTC Warning Signs", "6I": "TTC Guide Signs",
            "7B": "School Signs", "8B": "Grade Crossing Signs and Markings", "9B": "Bicycle Regulatory Signs", "9C": "Bicycle Warning Signs",
            "9D": "Bicycle Guide Signs"}
COLS = [("single_lane", "Single lane"), ("multi_lane", "Multi-lane"), ("conventional", "Conventional"),
        ("expressway", "Expressway"), ("freeway", "Freeway"), ("freeway_expressway", "Fwy/Expwy"),
        ("minimum", "Minimum"), ("oversized", "Oversized"), ("off_roadway", "Off-roadway"), ("roadway", "Roadway")]
TAG = {"Mandatory": "**[M]**", "Recommended": "**[R]**", "Optional": "[O]", "Note": "[S]"}


def _key(code):
    m = re.match(r'([A-Z]+)(\d+)-(\d+)(.*)', code)
    return (m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)) if m else (code, 0, 0, '')


def _sec_key(s):
    m = re.match(r'(\d)([A-Z])\.(\d+)', s or "9Z.99")
    return (int(m.group(1)), m.group(2), int(m.group(3))) if m else (9, "Z", 99)


def _thumb(path, h=64):
    try:
        from PIL import Image
        im = Image.open(path).convert("RGB")
        im.thumbnail((h * 3, h))
        buf = io.BytesIO(); im.save(buf, "PNG", optimize=True)
        return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return ""


def build(code="mutcd_11e", embed=False):
    d = os.path.join(HERE, "rulebooks", code)
    cat = json.load(open(os.path.join(d, "sign_catalog.json"), encoding="utf-8"))
    import csv
    with open(os.path.join(d, "devices.csv"), encoding="utf-8") as fh:
        dev = {r["code"]: r for r in csv.DictReader(l for l in fh if not l.startswith("#"))}
    pic = {}
    for c in cat:
        p = (dev.get(c) or {}).get("symbol") or ""
        fp = os.path.join(d, p) if p else ""
        if fp and os.path.exists(fp):
            pic[c] = _thumb(fp) if embed else p
    # group signs by primary section
    groups = defaultdict(list)
    for c, e in cat.items():
        groups[e.get("section") or "—"].append(c)
    L = []
    n_sign = len(cat)
    n_pic = len(pic)
    L.append("# Rule book: every sign in the MUTCD 11th Edition")
    L.append("")
    L.append(f"T&I Transportation Systems, road signing skill. Generated {date.today():%d %b %Y}. {n_sign} signs and plaques, "
             f"{n_pic} with a picture from the manual. Results are DRAFT until a T&I engineer signs the rulebook off.")
    L.append("")
    L.append("## How to read it")
    L.append("")
    L.append("- Signs are grouped under the MUTCD section that governs them; each group shows its signs, then the section's rules once.")
    L.append("- Rule tags: **[M]** Mandatory (Standard, \"shall\"), **[R]** Recommended (Guidance, \"should\"), [O] Optional (Option, \"may\"), [S] Support (information).")
    L.append("- A paragraph marked ◆ names the sign(s) shown after it; unmarked paragraphs apply to the whole group.")
    L.append("- *Default class* is the class the engine gives a sign placed by the designer: the strongest paragraph that says the sign "
             "shall / should / may be used (its reference is shown). The real need always depends on the condition in that paragraph.")
    L.append("- Sizes are inches (width x height; diamond and square signs are side x side) from the MUTCD size tables. Other contexts "
             "(work zones, grade crossings, bicycle facilities) are listed under *Also sized in*.")
    L.append("- Automatic placement: signs the engine places from the network carry *Auto*; all others are placed by the designer "
             "as a point with `type: sign` and `code`, and the engine sizes, classes, mounts and schedules them.")
    L.append("")
    # automatic coverage
    import yaml
    rules = yaml.safe_load(open(os.path.join(d, "rules.yaml"), encoding="utf-8"))["rules"]
    auto = set()
    for r in rules:
        if r["trigger"] == "SIGN-REQUEST":
            continue
        dv = str(r["device"])
        if dv.startswith("{") and "warn_symbol" in dv:
            auto |= {"W2-1", "W2-2", "W2-4"}
        elif dv.startswith("{") and "curve_sign" in dv:
            auto |= {"W1-1", "W1-2", "W1-3", "W1-4"}
        elif dv.startswith("{"):
            auto |= set(re.findall(r"'([A-Z]+\d+-\d+[A-Za-z]*)'", dv))
        else:
            auto.add(dv)
        for cp in r.get("companions") or []:
            auto.add(cp if isinstance(cp, str) else cp["device"])
    auto = {a for a in auto if a in cat}
    # contents
    L.append("## Contents")
    L.append("")
    secs = sorted(groups, key=_sec_key)
    cur_ch = None
    for s in secs:
        ch = s[:2]
        if ch != cur_ch:
            L.append(f"- **{ch} {CHAPTERS.get(ch, '')}**")
            cur_ch = ch
        t = cat[groups[s][0]].get("section_title", "")
        L.append(f"  - [{s} {t}](#sec-{s.replace('.', '-')}) ({len(groups[s])})")
    L.append("")
    cur_part = None
    cur_ch = None
    for s in secs:
        codes = sorted(groups[s], key=_key)
        e0 = cat[codes[0]]
        if s[:1] != cur_part:
            cur_part = s[:1]
            L.append(f"## {PARTS.get(cur_part, 'Other')}")
            L.append("")
        if s[:2] != cur_ch:
            cur_ch = s[:2]
            L.append(f"### Chapter {cur_ch} {CHAPTERS.get(cur_ch, '')}")
            L.append("")
        L.append(f"<a id=\"sec-{s.replace('.', '-')}\"></a>")
        L.append(f"#### Section {s} {e0.get('section_title', '')}")
        L.append("")
        # sign table
        used_cols = [k for k, _ in COLS if any((cat[c]['sizes'].get(cat[c]['primary_table'], {}) or {}).get(k) for c in codes)]
        hdr = ["Sign", "Code", "Name", "Default class"] + [lab for k, lab in COLS if k in used_cols] + ["Size table", "Also sized in"]
        L.append("| " + " | ".join(hdr) + " |")
        L.append("|" + "---|" * len(hdr))
        for c in codes:
            e = cat[c]
            sz = e['sizes'].get(e['primary_table'], {}) or {}
            img = ""
            if c in pic:
                img = f"<img src=\"{pic[c]}\" alt=\"{c}\" height=\"48\">" if embed else f"![{c}]({pic[c]})"
            dc = f"{e.get('default_class', '')}" + (f" ({e['default_basis']})" if e.get('default_basis') else "")
            if c in auto:
                dc += " · *Auto*"
            also = ", ".join(f"{t.replace('Table ', '')}" for t in e['sizes'] if t != e['primary_table'])
            tbl = f"{e['primary_table'].replace('Table ', '')} p.{e['table_pages'].get(e['primary_table'], '')}" if e['primary_table'] else "text"
            row = [img, f"**{c}**", e['name'].replace("|", "/"), dc] + [(sz.get(k) or "—") for k in used_cols] + [tbl, also or "—"]
            L.append("| " + " | ".join(row) + " |")
        L.append("")
        # provisions: union over the group, de-duplicated, in section/paragraph order
        seen = OrderedDict()
        for c in codes:
            for p in cat[c]['provisions']:
                k = (p['section'], p['para'])
                if k not in seen:
                    seen[k] = {"p": p, "named": set()}
                if p.get('names_sign'):
                    seen[k]["named"].add(c)
        by_sec = defaultdict(list)
        for (sec, para), v in seen.items():
            by_sec[sec].append(v)
        for sec in sorted(by_sec, key=_sec_key):
            items = sorted(by_sec[sec], key=lambda v: v["p"]["para"])
            if sec != s:
                L.append(f"*Also governed by Section {sec}:*")
                L.append("")
            for v in items:
                p = v["p"]
                mark = ""
                if v["named"] and len(v["named"]) < len(codes):
                    mark = " ◆ " + ", ".join(sorted(v["named"], key=_key))
                pg = f" (p.{p['page']})" if p.get('page') else ""
                chk = " ⚠ check" if "CHECK" in (p.get('check') or "") else ""
                L.append(f"- {TAG[p['class']]} {sec}-{p['para']}{pg}{mark}: {p['text']}{chk}")
            L.append("")
    return "\n".join(L)


def to_html(md_text, title="Rule book: every MUTCD sign"):
    import markdown
    body = markdown.markdown(md_text, extensions=["tables"])
    css = ("body{font-family:Arial,Helvetica,sans-serif;max-width:1200px;margin:0 auto;padding:16px;color:#15201B;background:#fff;line-height:1.45}"
           "h1{background:#0A6B47;color:#fff;padding:14px 18px;border-radius:8px}h2{border-bottom:3px solid #0A6B47;margin-top:2em}"
           "h3{color:#0A6B47;margin-top:1.6em}h4{background:#EEF3F0;padding:6px 10px;border-radius:4px;margin-top:1.8em}"
           "table{border-collapse:collapse;width:100%;font-size:.85rem;display:block;overflow-x:auto;margin:8px 0}"
           "th{background:#0A6B47;color:#fff;text-align:left;padding:5px 7px}td{border-bottom:1px solid #D3DDD8;padding:5px 7px;vertical-align:middle}"
           "li{margin:3px 0;font-size:.92rem}code{background:#EEF3F0;padding:1px 4px}")
    return (f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{title}</title><style>{css}</style></head><body>{body}</body></html>')


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", default="mutcd_11e")
    ap.add_argument("--out", required=True)
    ap.add_argument("--html")
    a = ap.parse_args(argv)
    open(a.out, "w", encoding="utf-8").write(build(a.code))
    print("wrote", a.out)
    if a.html:
        open(a.html, "w", encoding="utf-8").write(to_html(build(a.code, embed=True)))
        print("wrote", a.html)


if __name__ == "__main__":
    main()
