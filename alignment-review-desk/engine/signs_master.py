"""Master sign list: a crosswalk between the MUTCD, Egyptian and SHC sign sets (T&I, reused across projects).

  python -m engine.signs_master validate
  python -m engine.signs_master export --out master_signs_DRAFT.xlsx

Design: each code keeps its own catalog (rulebooks/<code>/devices.csv: names, clauses, sizes from that code's source only).
`signs_master/master_links.csv` holds the links between them. A link is `approved` only when a T&I engineer has approved it;
no link is made by look-alike, and no value is ever copied from one code into another (build spec rules 6 and 8).
"""
from __future__ import annotations
import argparse
import csv
import json
import os
import re
import sys
from typing import Dict, List

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINKS = os.path.join(HERE, "signs_master", "master_links.csv")
MUTCD_CODE = re.compile(r"^[A-Z]{1,2}\d+(-\d+[A-Za-z]*)?(P)?$")
EGY_CODE = re.compile(r"^(\d{3}(\+\d{3})?|L\d+-\d+[a-z]?)$")
MUTCD_CLAUSE = re.compile(r"\b\d[A-Z]\.\d+")           # e.g. 2B.18
EGY_CLAUSE = re.compile(r"^\d+(-\d+)+$")                # e.g. 5-2-3
MATCH = ("same", "check", "none")


def _csv(path: str) -> List[Dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(ln for ln in fh if not ln.startswith("#")))


def load_links() -> List[Dict]:
    return _csv(LINKS)


def load_catalog(code: str) -> Dict[str, Dict]:
    """Per-code catalog keyed by that code's own sign code."""
    return {r["code"]: r for r in _csv(os.path.join(HERE, "rulebooks", code, "devices.csv")) if r.get("code")}


def template_blocks() -> set:
    import ezdxf
    tpl = ezdxf.readfile(os.path.join(HERE, "styles", "ti_details", "template.dxf"))
    return {b.name for b in tpl.blocks}


def validate(check_blocks: bool = True) -> List[str]:
    """Return a list of problems (empty = the master list obeys the rules)."""
    errs: List[str] = []
    mutcd, egy, shc = load_catalog("mutcd_11e"), load_catalog("egypt"), load_catalog("shc")
    blocks = template_blocks() if check_blocks else None
    seen, ids = {}, set()
    for r in load_links():
        i = r["master_id"]
        if i in ids:
            errs.append(f"{i}: duplicate master_id")
        ids.add(i)
        m, e, s, b = r["mutcd_code"], r["egypt_code"], r["shc_code"], r["ti_block"]
        if m:
            if not MUTCD_CODE.match(m):
                errs.append(f"{i}: '{m}' in mutcd_code is not a MUTCD code")
            elif m not in mutcd:
                errs.append(f"{i}: MUTCD code {m} is not in the MUTCD catalog")
        if e:
            if MUTCD_CODE.match(e) and not EGY_CODE.match(e):
                errs.append(f"{i}: '{e}' in egypt_code looks like a MUTCD code (codes are never mixed)")
            elif not EGY_CODE.match(e):
                errs.append(f"{i}: '{e}' in egypt_code is not an Egyptian code (expected 3 digits or L-series)")
            elif e not in egy:
                errs.append(f"{i}: Egyptian code {e} is not in rulebooks/egypt/devices.csv")
        if s and s not in shc:
            errs.append(f"{i}: SHC code {s} is not in rulebooks/shc/devices.csv")
        if blocks is not None and b and b not in blocks:
            errs.append(f"{i}: T&I block '{b}' is not in the template")
        if r["match"] not in MATCH:
            errs.append(f"{i}: match must be one of {MATCH}")
        if r["match"] in ("same", "check") and sum(1 for x in (m, e, s, b) if x) < 2:
            errs.append(f"{i}: match '{r['match']}' needs at least two of MUTCD / Egyptian / SHC code and T&I block")
        if r["approved"] == "yes":
            if r["match"] == "none":
                errs.append(f"{i}: approved link has match 'none'")
            if not (r["approved_by"] and r["approved_date"]):
                errs.append(f"{i}: approved link needs approved_by and approved_date")
            if s and not (m or e):
                errs.append(f"{i}: SHC link without another code")
            key = (m, r["when"])
            if m and key in seen:
                errs.append(f"{i}: approved MUTCD {m} ({r['when'] or 'any'}) already linked in {seen[key]}")
            seen[key] = i
        if e and r["egypt_code_verified"] != "yes" and "not checked" not in r["note"] and "not yet read" not in r["note"]:
            errs.append(f"{i}: Egyptian code is unverified but the note does not say so")
    for code, cat in (("egypt", egy), ("shc", shc)):
        for c, row in cat.items():
            cl = (row.get("clause") or "").strip()
            if cl and (MUTCD_CLAUSE.search(cl) or not EGY_CLAUSE.match(cl)) and code == "egypt":
                errs.append(f"egypt catalog {c}: clause '{cl}' is not Egyptian numbering (MUTCD numbers are never used here)")
    return errs


def rows_for_export() -> List[Dict]:
    """One row per link, then one row per MUTCD sign that has no link yet. Names and clauses are looked up from
    each code's own catalog; nothing is copied between codes."""
    mutcd, egy, shc = load_catalog("mutcd_11e"), load_catalog("egypt"), load_catalog("shc")
    sections = {}
    try:
        with open(os.path.join(HERE, "rulebooks", "mutcd_11e", "sign_catalog.json"), encoding="utf-8") as fh:
            sections = {k: v.get("section", "") for k, v in json.load(fh).items()}
    except OSError:
        pass
    out, linked = [], set()
    for r in load_links():
        m, e, s = r["mutcd_code"], r["egypt_code"], r["shc_code"]
        linked.add(m)
        out.append({"id": r["master_id"], "family": mutcd.get(m, {}).get("family", ""), "mutcd": m,
                    "mutcd_name": mutcd.get(m, {}).get("official_name", ""), "mutcd_clause": sections.get(m, ""),
                    "mutcd_when": r["when"], "egy": e, "egy_ar": egy.get(e, {}).get("name_ar", ""),
                    "egy_en": egy.get(e, {}).get("name_en", ""), "egy_clause": egy.get(e, {}).get("clause", ""),
                    "shc": s, "shc_name": shc.get(s, {}).get("name_en", ""), "block": r["ti_block"], "match": r["match"],
                    "approved": r["approved"], "by": r["approved_by"], "note": r["note"]})
    for m, c in mutcd.items():
        if m not in linked:
            out.append({"id": "", "family": c.get("family", ""), "mutcd": m, "mutcd_name": c.get("official_name", ""),
                        "mutcd_clause": sections.get(m, ""), "mutcd_when": "", "egy": "", "egy_ar": "", "egy_en": "",
                        "egy_clause": "", "shc": "", "shc_name": "", "block": "", "match": "", "approved": "", "by": "", "note": ""})
    return out


HEAD = [("id", "Master ID\nالرمز", 9), ("family", "Family\nالفئة", 22), ("mutcd", "MUTCD code", 11), ("mutcd_name", "MUTCD name", 34),
        ("mutcd_clause", "MUTCD clause", 10), ("mutcd_when", "Condition", 20), ("egy", "Egyptian code\nالكود المصري", 12),
        ("egy_ar", "Egyptian name (AR)\nالاسم", 28), ("egy_en", "Egyptian name (EN)", 28), ("egy_clause", "Egyptian clause\nالبند", 12),
        ("shc", "SHC code", 10), ("shc_name", "SHC name", 24), ("block", "T&I block", 16), ("match", "Match", 8),
        ("approved", "Approved", 9), ("by", "Approved by", 24), ("note", "Note", 60)]


def export_xlsx(path: str, status: str = "extracting"):
    from openpyxl import Workbook
    from openpyxl.drawing.image import Image as XL
    from openpyxl.styles import Alignment, Font, PatternFill
    from .writers import load_brand
    B = load_brand()
    C, font = B["colors"], B.get("font", "Arial")
    rows = rows_for_export()
    wb = Workbook()
    ws = wb.active
    ws.title = "Master list"
    ws["A1"] = "Master sign list: MUTCD / Egyptian / SHC - DRAFT"
    ws["A1"].font = Font(name=font, size=14, bold=True, color=C["primary_green"])
    ws["A2"] = "قائمة اللافتات الرئيسية - مسودة"
    ws["A2"].font = Font(name=font, size=12, bold=True, color=C["charcoal"])
    ws["A3"] = (f"Rulebook status: {status}. Each name and clause comes from that code's own catalog. A link is approved only by a T&I engineer; "
                "Egyptian numbers come from T&I block names and are not yet checked against the printed code; SHC is empty until its source is provided.")
    ws["A3"].font = Font(name=font, size=9, color=C["mid_gray"])
    for i, (_, h, w) in enumerate(HEAD, 1):
        c = ws.cell(row=5, column=i, value=h)
        c.font = Font(name=font, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=C["primary_green"])
        c.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[c.column_letter].width = w
    ws.row_dimensions[5].height = 34
    for k, r in enumerate(rows):
        for i, (key, _, _) in enumerate(HEAD, 1):
            c = ws.cell(row=6 + k, column=i, value=r[key])
            c.font = Font(name=font, size=10)
            if r["id"] and k % 2 == 0:
                c.fill = PatternFill("solid", fgColor=C["neutral_tint"])
    ws.freeze_panes = "D6"
    ws.auto_filter.ref = f"A5:{ws.cell(row=5, column=len(HEAD)).column_letter}{5 + len(rows)}"
    try:
        im = XL(os.path.join(HERE, "brand", B.get("logo", "TI_Logo.png")))
        im.width, im.height = 150, 28
        ws.add_image(im, "L1")
    except Exception:
        pass
    wb.save(path)
    return len(rows)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Master sign list (MUTCD / Egyptian / SHC crosswalk)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    e = sub.add_parser("export")
    e.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "validate":
        errs = validate()
        print("\n".join(errs) if errs else "master list OK")
        return 1 if errs else 0
    from .rulebook import Rulebook
    n = export_xlsx(a.out, Rulebook("mutcd_11e").meta.get("status", "extracting"))
    print("wrote", a.out, f"({n} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
