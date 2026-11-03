"""Project folder and control workbook (build spec sections 3, 4 and 4.2).

  python -m engine.project new --root Projects --code TL00 --name Wyte [--client X] [--location Y]

Creates Projects/<CODE>_<Name>/{00_Control,01_Input,02_Runs,03_Outputs} and the bilingual (English / Arabic)
control workbook. The workbook is DRAFT-named while no rulebook is signed. No value is filled in for the user:
settings the user has not given stay empty.
"""
from __future__ import annotations
import argparse
import os
import re
import sys
from typing import Dict, List

from .writers import load_brand

SUBDIRS = ("00_Control", "01_Input", "02_Runs", "03_Outputs")

# sheet -> (English title, Arabic title, [(English header, Arabic header), ...])
SHEETS = {
    "Settings": ("Settings", "الإعدادات", [("Setting", "الإعداد"), ("Value", "القيمة"), ("Note", "ملاحظة")]),
    "Inputs": ("Inputs", "المدخلات", [("Name", "الاسم"), ("Role", "الدور"), ("Format", "الصيغة"), ("CRS", "نظام الإحداثيات"),
                                      ("Path", "المسار"), ("Status", "الحالة")]),
    "Questions": ("Questions", "الأسئلة", [("Id", "الرمز"), ("Topic", "الموضوع"), ("Question", "السؤال"), ("Items", "العناصر"),
                                           ("Suggested answer", "الإجابة المقترحة"), ("Status", "الحالة"), ("Answer", "الإجابة"),
                                           ("Source", "المصدر")]),
    "Junctions": ("Junctions", "التقاطعات", [("Junction ID", "رمز التقاطع"), ("Type", "النوع"), ("Engine node ID", "رمز العقدة"),
                                             ("E", "شرقي"), ("N", "شمالي"), ("Traffic management plan", "خطة إدارة المرور"),
                                             ("Type of control", "نوع التحكم"), ("Stop approaches", "المداخل الخاضعة للتوقف"),
                                             ("Sight restricted", "الرؤية مقيدة"), ("Notes", "ملاحظات")]),
    "Runs": ("Runs", "التشغيلات", [("Run id", "رمز التشغيل"), ("Date", "التاريخ"), ("Settings", "الإعدادات"),
                                   ("Mandatory", "إلزامي"), ("Recommended", "موصى به"), ("Optional", "اختياري"),
                                   ("Conditional", "مشروط"), ("Pending", "معلق"), ("Issues", "ملاحظات"),
                                   ("Outputs", "المخرجات"), ("Status", "الحالة")]),
    "Rulebook": ("Rulebook", "كتاب القواعد", [("Code", "المدونة"), ("Status", "الحالة"), ("Verified", "مُتحقق"),
                                              ("Unverified", "غير مُتحقق"), ("Last review", "آخر مراجعة")]),
}
SETTINGS_ROWS = ["Project code", "Project name", "Client", "Location", "Speed limit (km/h)", "Drive side", "Code", "Families",
                 "Level", "Units", "Size", "Environment", "Missing-data rule", "Outputs", "EPSG", "Tolerance (tol)",
                 "Drawing style (ti or input)"]
SETTINGS_AR = ["رمز المشروع", "اسم المشروع", "العميل", "الموقع", "السرعة المقررة (كم/س)", "جهة السير", "المدونة", "العائلات",
               "المستوى", "الوحدات", "المقاس", "البيئة", "قاعدة البيانات الناقصة", "المخرجات", "EPSG", "التسامح", "نمط الرسم"]
JUNCTION_TYPES = ("roundabout", "T-junction", "crossing", "hammerhead dead end", "cul-de-sac", "other")
CONTROLS = ("signal", "stop_all", "stop_minor", "yield", "roundabout", "none")


def safe(s: str) -> str:
    return re.sub(r"[^\w\-]+", "_", s.strip()).strip("_")


def number_junctions(items: List[Dict]) -> List[Dict]:
    """Label junctions J01.. and dead ends D01.. (spec 4.2). Order: roundabouts, T-junctions, then the rest;
    north to south (larger N first) inside a group. Dead ends (hammerhead / cul-de-sac) get D labels.
    Each item needs `type`, `e`, `n`; the input is not changed. Another order the user gives wins: pass `id` already set."""
    def group(t: str) -> int:
        t = (t or "").lower()
        return 0 if t == "roundabout" else 1 if t.startswith("t-junction") else 3 if t in ("hammerhead dead end", "cul-de-sac") else 2
    out, cj, cd = [], 0, 0
    for it in sorted(items, key=lambda i: (group(i.get("type")), -float(i["n"]))):
        it = dict(it)
        if not it.get("id"):
            if group(it.get("type")) == 3:
                cd += 1
                it["id"] = f"D{cd:02d}"
            else:
                cj += 1
                it["id"] = f"J{cj:02d}"
        out.append(it)
    return out


def build_workbook(path: str, code: str, name: str, meta: Dict | None = None, rulebook_status: str = "extracting"):
    from openpyxl import Workbook
    from openpyxl.drawing.image import Image as XLImage
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation
    B = load_brand()
    C, font = B["colors"], B.get("font", "Arial")
    hdr_fill = PatternFill("solid", fgColor=C["primary_green"])
    band = PatternFill("solid", fgColor=C["neutral_tint"])
    wb = Workbook()
    wb.remove(wb.active)
    status_line = f"DRAFT - rulebook status: {rulebook_status}"
    logo = os.path.join(os.path.dirname(__file__), "..", "brand", B.get("logo", "TI_Logo.png"))
    for key, (en, ar, cols) in SHEETS.items():
        ws = wb.create_sheet(key)
        ws.sheet_view.rightToLeft = False
        ws["A1"] = f"{code}_{name} - {en} (DRAFT)"
        ws["A1"].font = Font(name=font, size=14, bold=True, color=C["primary_green"])
        ws["A2"] = f"{ar} (مسودة)"
        ws["A2"].font = Font(name=font, size=12, bold=True, color=C["charcoal"])
        ws["A3"] = status_line
        ws["A3"].font = Font(name=font, size=9, color=C["mid_gray"])
        for i, (e, a) in enumerate(cols, 1):
            c = ws.cell(row=5, column=i, value=f"{e}\n{a}")
            c.font = Font(name=font, bold=True, color="FFFFFF")
            c.fill = hdr_fill
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
            ws.column_dimensions[c.column_letter].width = 26 if key != "Questions" or i not in (3, 7) else 48
        ws.row_dimensions[5].height = 32
        for r in range(6, 6 + 40):
            if r % 2 == 1:
                for i in range(1, len(cols) + 1):
                    ws.cell(row=r, column=i).fill = band
        ws.freeze_panes = "A6"
        try:
            img = XLImage(logo)
            img.height, img.width = 40, int(40 * img.width / img.height) if img.height else 220
            ws.add_image(img, f"{chr(64 + min(len(cols), 8))}1")
        except Exception:
            pass
    # Settings: row labels in both languages; the user's own values only
    ws = wb["Settings"]
    vals = {"Project code": code, "Project name": name, "Drive side": "right"}
    vals.update(meta or {})
    for i, (en, ar) in enumerate(zip(SETTINGS_ROWS, SETTINGS_AR)):
        r = 6 + i
        ws.cell(row=r, column=1, value=f"{en} / {ar}").font = Font(name=font, bold=True, color=C["charcoal"])
        ws.cell(row=r, column=2, value=vals.get(en))
    ws.cell(row=6 + len(SETTINGS_ROWS) + 1, column=1, value="Open questions / أسئلة مفتوحة").font = Font(name=font, bold=True)
    ws.cell(row=6 + len(SETTINGS_ROWS) + 1, column=2, value='=COUNTIF(Questions!F:F,"open")')
    ws.cell(row=6 + SETTINGS_ROWS.index("Drive side"), column=3, value="Right-hand traffic (Egypt) unless the project says otherwise")
    # drop-downs
    wj = wb["Junctions"]
    for rng, lst in (("B6:B200", JUNCTION_TYPES), ("G6:G200", CONTROLS), ("I6:I200", ("yes", "no"))):
        dv = DataValidation(type="list", formula1='"' + ",".join(lst) + '"', allow_blank=True)
        wj.add_data_validation(dv)
        dv.add(rng)
    dv = DataValidation(type="list", formula1='"open,answered"', allow_blank=True)
    wb["Questions"].add_data_validation(dv)
    dv.add("F6:F500")
    dv = DataValidation(type="list", formula1='"queued,waiting,running,done,failed"', allow_blank=True)
    wb["Runs"].add_data_validation(dv)
    dv.add("K6:K200")
    wr = wb["Rulebook"]
    wr["A6"], wr["B6"] = "mutcd_11e", rulebook_status
    wb.save(path)


def new_project(root: str, code: str, name: str, **meta) -> str:
    folder = os.path.join(root, f"{safe(code)}_{safe(name)}")
    for s in SUBDIRS:
        os.makedirs(os.path.join(folder, s), exist_ok=True)
    path = os.path.join(folder, "00_Control", f"{safe(code)}_{safe(name)}_Control_DRAFT.xlsx")
    if os.path.exists(path):
        raise FileExistsError(f"{path} exists; not overwritten")
    from .rulebook import Rulebook
    st = Rulebook("mutcd_11e").meta.get("status", "extracting")
    build_workbook(path, code, name, {k.replace("_", " ").capitalize(): v for k, v in meta.items() if v}, st)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser(description="Create a signing project folder and control workbook")
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new")
    n.add_argument("--root", required=True)
    n.add_argument("--code", required=True)
    n.add_argument("--name", required=True)
    n.add_argument("--client")
    n.add_argument("--location")
    a = ap.parse_args(argv)
    print("wrote", new_project(a.root, a.code, a.name, client=a.client, location=a.location))
    return 0


if __name__ == "__main__":
    sys.exit(main())
