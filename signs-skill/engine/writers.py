"""Output writers: sign schedule (xlsx), GeoJSON, DXF (style-matched), report (docx), dashboard JSON."""
from __future__ import annotations
import json
import math
import os
from collections import Counter, defaultdict
from typing import Dict, List

from .placement import Device

CLASSES = ["Mandatory", "Conditional", "Recommended", "Optional"]


def load_brand() -> Dict:
    """T&I brand kit (brand/brand.yaml): colours, font, logo, report template. Falls back to the same palette."""
    import os, yaml
    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "brand")
    b = {"font": "Arial", "colors": {"primary_green": "019945", "light_green": "40B273", "charcoal": "434343",
                                     "mid_gray": "6E6E6E", "black": "000000", "neutral_tint": "F4F6F5"}}
    fp = os.path.join(root, "brand.yaml")
    if os.path.exists(fp):
        b.update(yaml.safe_load(open(fp, encoding="utf-8")) or {})
    for k in ("logo", "report_template"):
        if b.get(k):
            b[k] = os.path.join(root, b[k])
            if not os.path.exists(b[k]):
                b[k] = None
    return b


# ------------------------------------------------------------------ xlsx
def _symbol(rb, code):
    """Path of the sign picture cropped from the manual, or None."""
    import os
    if rb is None:
        return None
    rel = (rb.devices.get(code) or {}).get("symbol") or ""
    fp = os.path.join(rb.dir, rel) if rel else ""
    return fp if fp and os.path.exists(fp) else None


def _xl_image(fp, max_px):
    from openpyxl.drawing.image import Image as XLImage
    from PIL import Image as PILImage
    with PILImage.open(fp) as im:
        w, h = im.size
    img = XLImage(fp)
    k = max_px / max(w, h)
    img.width, img.height = int(w * k), int(h * k)
    return img


def write_schedule(path: str, devs: List[Device], meta: Dict, questions: List[Dict], log: List[str],
                   audit: List[Dict] | None = None, rb=None, style_pack=None):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter as L

    B = load_brand()
    C = B["colors"]
    F = B.get("font", "Arial")
    hdr = Font(name=F, bold=True, color="FFFFFF", size=10)
    fill = PatternFill("solid", fgColor=C["primary_green"])
    band = PatternFill("solid", fgColor=C["neutral_tint"])
    body = Font(name=F, size=10, color=C["black"])
    cls_fill = {"Mandatory": "F8CBAD", "Conditional": "D9D9D9", "Recommended": "FFE699", "Optional": "DDEBF7"}
    wb = Workbook()

    def sheet(title, cols, rows, widths=None):
        ws = wb.create_sheet(title)
        for i, c in enumerate(cols, 1):
            cell = ws.cell(row=1, column=i, value=c)
            cell.font, cell.fill = hdr, fill
            cell.alignment = Alignment(wrap_text=True, vertical="center")
        for r, row in enumerate(rows, 2):
            for i, v in enumerate(row, 1):
                cell = ws.cell(row=r, column=i, value=v)
                cell.font = body
                if r % 2 == 1:
                    cell.fill = band
                cell.alignment = Alignment(vertical="top", wrap_text=isinstance(v, str) and len(v) > 40)
        for i, w in enumerate(widths or [], 1):
            ws.column_dimensions[L(i)].width = w
        ws.row_dimensions[1].height = 30          # fixed, so pictures anchored below sit in their own rows
        ws.freeze_panes = "B2"
        if rows:
            ws.auto_filter.ref = f"A1:{L(len(cols))}{len(rows) + 1}"
        return ws

    # summary
    ws = wb.active
    ws.title = "Summary"
    ws.sheet_view.showGridLines = False
    if B.get("logo"):
        try:
            from openpyxl.drawing.image import Image as XLImage
            from PIL import Image as PImage
            im = XLImage(B["logo"])
            w0, h0 = PImage.open(B["logo"]).size
            im.width, im.height = 300, int(300 * h0 / w0)
            ws.add_image(im, "A1")
        except Exception:
            pass
    ws["A5"] = "Sign schedule"
    ws["A5"].font = Font(name=F, size=16, bold=True, color=C["primary_green"])
    ws["A6"] = f"{meta.get('Project', '')} · T&I Consulting Engineers · DRAFT for engineer review"
    ws["A6"].font = Font(name=F, size=10, color=C["mid_gray"])
    r = 8
    for k, v in meta.items():
        ws.cell(row=r, column=1, value=k).font = Font(name=F, bold=True, size=10, color=C["charcoal"])
        ws.cell(row=r, column=2, value=str(v)).font = body
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Devices by class").font = Font(name=F, bold=True, size=12, color=C["charcoal"])
    r += 1
    signs = [d for d in devs if d.kind == "sign"]
    marks = [d for d in devs if d.kind == "marking"]
    for c in CLASSES:
        ws.cell(row=r, column=1, value=c).font = body
        ws.cell(row=r, column=2, value=sum(1 for d in signs if d.cls == c)).font = body
        ws.cell(row=r, column=3, value="signs/plaques").font = body
        ws.cell(row=r, column=4, value=sum(1 for d in marks if d.cls == c)).font = body
        ws.cell(row=r, column=5, value="marking items").font = body
        r += 1
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 60

    def mm(sz):
        try:
            return " x ".join(str(int(round(float(v) * 25.4 / 50.0) * 50)) for v in sz.split("x"))
        except ValueError:
            return ""

    cols = ["ID", "Code", "Sign", "Name", "Class", "Provision", "Clause", "Legend", "Orientation", "Size (in)", "Size (mm, rounded)", "Support", "Location",
            "Link", "Node", "Side", "Dist. to ref (m)", "X", "Y", "Offset (m)", "Height to bottom (m)",
            "Azimuth (deg)", "Confidence", "Study needed", "Notes", "Rule", "Verify vs manual"]
    if style_pack:
        cols += ["T&I block", "Fixation detail", "Post", "Base"]
    rows = [[d.id, d.code, "", d.name, d.cls, d.provision, d.clause, d.legend, d.orientation, d.size, mm(d.size), d.support, d.where, d.link, d.node,
             d.side, d.back_m, d.x, d.y, d.offset_m, d.height_m, d.azimuth_deg, d.confidence, d.study,
             "; ".join(d.notes), d.rule_id, "yes" if d.verify else ""] for d in signs]
    if style_pack:
        for r, d in zip(rows, signs):
            fx = fixation_for(style_pack, d)
            plaque = d.code.endswith("P") and d.support
            r += [pack_block_for(style_pack, d) or "MUTCD symbol",
                  ("on the sign's post" if plaque else fx["detail"]), ("" if plaque else fx["post"]), ("" if plaque else fx["base"])]
    s = sheet("Signs", cols, rows, [8, 9, 11, 24, 13, 11, 34, 18, 22, 11, 14, 9, 34, 10, 8, 7, 10, 12, 12, 9, 10, 9, 11, 30, 60, 24, 8]
              + ([16, 34, 34, 34] if style_pack else []))
    for i, d in enumerate(signs, 2):
        s.cell(row=i, column=5).fill = PatternFill("solid", fgColor=cls_fill.get(d.cls, "FFFFFF"))
        fp = _symbol(rb, d.code)
        if fp:
            s.add_image(_xl_image(fp, 56), f"C{i}")
            s.row_dimensions[i].height = 46

    # sign catalog: one row per sign type used, with the picture from the manual
    used = []
    for d in signs:
        if d.code not in used:
            used.append(d.code)
    if rb is not None and used:
        cat_rows = []
        for c in used:
            dv = rb.devices.get(c, {})
            cat_rows.append([c, "", dv.get("official_name", ""), dv.get("shape", ""), dv.get("color", ""),
                             dv.get("conv_single", ""), dv.get("conv_multi", ""), dv.get("expressway", ""), dv.get("freeway", ""),
                             dv.get("minimum", ""), dv.get("oversized", ""), dv.get("size_source", ""), dv.get("symbol_source", ""),
                             sum(1 for d in signs if d.code == c)])
        cs = sheet("Sign catalog", ["Code", "Sign", "Official name (MUTCD)", "Shape", "Colour", "Single lane (in)", "Multi-lane (in)",
                                    "Expressway (in)", "Freeway (in)", "Minimum (in)", "Oversized (in)", "Size source",
                                    "Picture source", "Qty in design"], cat_rows,
                   [10, 16, 30, 11, 12, 10, 10, 10, 10, 10, 10, 30, 28, 9])
        for i, c in enumerate(used, 2):
            fp = _symbol(rb, c)
            if fp:
                cs.add_image(_xl_image(fp, 90), f"B{i}")
            cs.row_dimensions[i].height = 72
        note_r = len(used) + 3
        cs.cell(row=note_r, column=1, value="Pictures and sizes from the MUTCD 11th Edition (FHWA, Dec 2023), a public-domain US government "
                                            "publication; sizes checked against Tables 2B-1, 2C-1 and 7B-1.").font = Font(name=F, italic=True, size=9)

    cols = ["ID", "Code", "Name", "Class", "Provision", "Clause", "Quantity", "Unit", "Location", "Link", "Node",
            "Study needed", "Notes", "Verify vs manual"]
    rows = [[d.id, d.code, d.name, d.cls, d.provision, d.clause, d.quantity, d.unit, d.where, d.link, d.node,
             d.study, "; ".join(d.notes), "yes" if d.verify else ""] for d in marks]
    sheet("Markings", cols, rows, [8, 10, 32, 13, 11, 36, 10, 6, 34, 10, 8, 30, 50, 8])

    # BOQ
    boq = defaultdict(lambda: [0, "", "", set()])
    for d in devs:
        if d.cls == "Conditional":
            continue
        k = (d.kind, d.code, d.size if d.kind == "sign" else d.unit)
        boq[k][0] += 1 if d.kind == "sign" else (d.quantity or 0)
        boq[k][1] = d.name
        boq[k][3].add(d.cls)
    sup = len({d.support for d in signs if d.support and d.cls != "Conditional"})
    rows = [[k[0], k[1], v[1], k[2] if k[0] == "sign" else "", round(v[0], 1), "no." if k[0] == "sign" else k[2],
             ", ".join(sorted(v[3], key=CLASSES.index))] for k, v in sorted(boq.items())]
    rows.append(["support", "POST", "Sign support (post + foundation)", "", sup, "no.", "per sign location"])
    sheet("BOQ", ["Item", "Code", "Description", "Size (in)", "Quantity", "Unit", "Classes included"], rows,
          [9, 12, 38, 10, 10, 6, 30])

    cond = [[d.id, d.code, d.name, d.where, d.study] for d in devs if d.cls == "Conditional"]
    sheet("Studies needed", ["ID", "Code", "Name", "Location", "Study that decides it"], cond, [8, 12, 28, 40, 70])
    sheet("Pending data", ["Question id", "Topic", "Question", "Items", "Suggested"],
          [[q["id"], q["topic"], q["question"], q["items"], q.get("suggested", "")] for q in questions],
          [16, 20, 60, 50, 20])
    sheet("QA log", ["Entry"], [[x] for x in log], [140])
    if audit is not None:
        sheet("Audit findings", ["Finding", "Code", "Required ID", "Existing ID", "Class", "Distance (m)", "Location", "Note"],
              [[a["finding"], a["code"], a.get("req", ""), a.get("existing", ""), a.get("cls", ""), a.get("dist", ""),
                a.get("where", ""), a.get("note", "")] for a in audit], [22, 10, 10, 12, 13, 10, 40, 50])
    wb.save(path)


# ------------------------------------------------------------------ geojson
def write_geojson(path: str, devs: List[Device], crs: str | None):
    feats = []
    for d in devs:
        props = d.row()
        if d.kind == "sign" and d.x is not None:
            g = {"type": "Point", "coordinates": [d.x, d.y]}
        elif d.geometry:
            g = {"type": "LineString", "coordinates": [list(p) for p in d.geometry]}
        else:
            continue
        feats.append({"type": "Feature", "geometry": g, "properties": props})
    fc = {"type": "FeatureCollection", "features": feats}
    if crs:
        fc["crs"] = {"type": "name", "properties": {"name": crs}}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(fc, fh, indent=1)


# ------------------------------------------------------------------ dxf
SHAPES = {
    "octagon": [(math.cos(math.radians(22.5 + 45 * k)), math.sin(math.radians(22.5 + 45 * k))) for k in range(8)],
    "triangle": [(0, -1), (0.866, 0.5), (-0.866, 0.5)],
    "diamond": [(0, 1), (1, 0), (0, -1), (-1, 0)],
    "square": [(-0.8, -0.8), (0.8, -0.8), (0.8, 0.8), (-0.8, 0.8)],
    "rectangle": [(-0.6, -0.9), (0.6, -0.9), (0.6, 0.9), (-0.6, 0.9)],
    "pentagon": [(0, 1), (0.95, 0.31), (0.59, -0.81), (-0.59, -0.81), (-0.95, 0.31)],
    "circle": None,
}
ACI = {"red": 1, "yellow": 2, "white": 7, "fluorescent_yellow_green": 3}


def _layer(style: Dict, name: str) -> str:
    sep = style.get("sep", "-")
    parts = [p for p in [style.get("prefix", ""), *name.split("-")] if p]
    n = sep.join(parts)
    return n.upper() if style.get("upper", True) else n


def write_dxf(path: str, devs: List[Device], rb, style: Dict | None = None, base_dxf: str | None = None,
              scale: float = 1.0):
    import ezdxf
    style = style or {"sep": "-", "prefix": "", "upper": True, "text_style": "Standard", "text_height": 1.0}
    doc = ezdxf.readfile(base_dxf) if base_dxf else ezdxf.new("R2018", setup=True)
    if not base_dxf:
        doc.header["$INSUNITS"] = 6
    msp = doc.modelspace()
    th = float(style.get("text_height") or 1.0) * scale
    lay = {"regulatory": _layer(style, "SIGN-REG"), "warning": _layer(style, "SIGN-WARN"),
           "school": _layer(style, "SIGN-SCHL"), "markings": _layer(style, "MARK"), "label": _layer(style, "SIGN-TEXT"),
           "cond": _layer(style, "SIGN-STUDY")}
    cols = {"regulatory": 1, "warning": 2, "school": 3, "markings": 7, "label": 7, "cond": 8}
    for k, n in lay.items():
        if n not in doc.layers:
            doc.layers.add(n, color=cols[k])
    made = set()
    for d in devs:
        if d.kind != "sign" or d.x is None:
            continue
        cat = rb.devices.get(d.code, {})
        shape = cat.get("shape", "square")
        bname = f"SIGN_{shape.upper()}"
        if bname not in made and bname not in doc.blocks:
            blk = doc.blocks.new(bname)
            pts = SHAPES.get(shape)
            if pts is None:
                blk.add_circle((0, 0), 0.8)
            else:
                blk.add_lwpolyline(pts, close=True)
            blk.add_line((0, -1), (0, -2.2))
            blk.add_attdef("CODE", (1.2, 0.2), dxfattribs={"height": 0.45})
            blk.add_attdef("ID", (1.2, -0.5), dxfattribs={"height": 0.35})
            made.add(bname)
        layer = lay["cond"] if d.cls == "Conditional" else lay.get(d.family, lay["warning"])
        rot = (90 - (d.azimuth_deg or 0)) % 360 + 90
        ins = msp.add_blockref(bname, (d.x, d.y), dxfattribs={"layer": layer, "xscale": scale, "yscale": scale,
                                                               "zscale": scale, "rotation": rot,
                                                               "color": ACI.get(cat.get("color", ""), 256)})
        ins.add_auto_attribs({"CODE": d.code, "ID": d.id})
    for d in devs:
        if d.kind == "marking" and d.geometry:
            msp.add_lwpolyline(d.geometry, dxfattribs={"layer": lay["markings"]})
    doc.saveas(path)


# ------------------------------------------------------------------ report
def write_report(path: str, devs: List[Device], meta: Dict, questions: List[Dict], log: List[str],
                 conflicts: List[str], rb_meta: Dict, audit: List[Dict] | None = None, rb=None):
    """Signing report on the T&I report template (brand/TI_Report_Template.docx): cover page, brand headings,
    green-header tables with neutral banding, callout boxes."""
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from datetime import date

    B = load_brand()
    C = B["colors"]
    FONT = B.get("font", "Arial")
    rgb = lambda h: RGBColor.from_string(h.upper())
    tpl = B.get("report_template")
    doc = Document(tpl) if tpl else Document()
    body = doc.element.body
    if tpl:
        # cover: fill the placeholders; body: drop the sample content after the cover section break
        for p in doc.paragraphs[:9]:
            t = p.text.strip()
            rep = {"REPORT TITLE": f"SIGNING {'AUDIT' if audit is not None else 'DESIGN'} REPORT",
                   "Subtitle or project name goes here": f"{meta.get('Project', '')}: road signs and pavement markings",
                   "Prepared by T&I Consulting Engineers": "Prepared by T&I Consulting Engineers · DRAFT for engineer review",
                   "Month 2026": date.today().strftime("%B %Y")}
            if t in rep and p.runs:
                p.runs[0].text = rep[t]
                for r_ in p.runs[1:]:
                    r_.text = ""
        cut = None
        for i, el in enumerate(list(body)):
            if el.tag == qn("w:p") and el.find(qn("w:pPr") + "/" + qn("w:sectPr")) is not None:
                cut = i
                break
        if cut is not None:
            for el in list(body)[cut + 1:]:
                if el.tag != qn("w:sectPr"):
                    body.remove(el)

    def run_fmt(run, size=10.5, bold=False, color=None, italic=False):
        run.font.name = FONT
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = rgb(color or C["black"])

    def sty(name):
        for st in doc.styles:
            if st.name and st.name.lower() == name.lower():
                return st
        return None

    def H1(text):
        p = doc.add_paragraph(style=sty("Heading 1"))
        run_fmt(p.add_run(text), 16, True, C["primary_green"])
        return p

    def H2(text):
        p = doc.add_paragraph(style=sty("Heading 2"))
        run_fmt(p.add_run(text), 12, True, C["charcoal"])
        return p

    def P(text, size=10.5, color=None, italic=False):
        p = doc.add_paragraph()
        run_fmt(p.add_run(text), size, False, color, italic)
        return p

    def bullet(text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.6)
        p.paragraph_format.first_line_indent = Cm(-0.4)
        p.paragraph_format.space_after = Pt(2)
        run_fmt(p.add_run("•  " + text), 10.5)
        return p

    def shade(cell, hex_):
        tcPr = cell._tc.get_or_add_tcPr()
        sh = OxmlElement("w:shd")
        sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hex_)
        tcPr.append(sh)

    def borders(tbl, color="DDDDDD"):
        tblPr = tbl._tbl.tblPr
        b = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{edge}")
            e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:color"), color)
            b.append(e)
        tblPr.append(b)

    def table(headers, rows, widths=None):
        t = doc.add_table(rows=1, cols=len(headers))
        borders(t)
        for i, h in enumerate(headers):
            c = t.rows[0].cells[i]
            c.text = ""
            run_fmt(c.paragraphs[0].add_run(str(h)), 10, True, "FFFFFF")
            shade(c, C["primary_green"])
        for k, row in enumerate(rows):
            cells = t.add_row().cells
            for i, v in enumerate(row):
                if isinstance(v, tuple) and v and v[0] == "img":
                    cells[i].paragraphs[0].add_run().add_picture(v[1], height=Cm(1.4))
                else:
                    run_fmt(cells[i].paragraphs[0].add_run("" if v is None else str(v)), 10)
                if k % 2 == 1:
                    shade(cells[i], C["neutral_tint"])
        if widths:
            for row in t.rows:
                for i, w in enumerate(widths):
                    row.cells[i].width = Cm(w)
        doc.add_paragraph()
        return t

    def callout(label, text):
        t = doc.add_table(rows=1, cols=1)
        c = t.rows[0].cells[0]
        shade(c, C["neutral_tint"])
        tcPr = c._tc.get_or_add_tcPr()
        b = OxmlElement("w:tcBorders")
        for edge, val, sz, col in (("left", "single", "24", C["primary_green"]), ("top", "nil", "0", "auto"),
                                   ("bottom", "nil", "0", "auto"), ("right", "nil", "0", "auto")):
            e = OxmlElement(f"w:{edge}")
            e.set(qn("w:val"), val); e.set(qn("w:sz"), sz); e.set(qn("w:color"), col)
            b.append(e)
        tcPr.append(b)
        p = c.paragraphs[0]
        run_fmt(p.add_run(label + " "), 10.5, True)
        run_fmt(p.add_run(text), 10.5)
        doc.add_paragraph()

    n = [0]

    def sec(title):
        n[0] += 1
        H1(f"{n[0]}. {title}")

    callout("Status: DRAFT for engineer review.",
            f"Rulebook: {rb_meta.get('name')} ({rb_meta.get('id')}), status '{rb_meta.get('status')}'. Every device lists the "
            "clause it comes from; values marked 'verify' must be checked against the printed manual before issue.")
    sec("Run settings")
    table(["Item", "Value"], [[k, v] for k, v in meta.items()], [5.5, 11])
    sec("Results by class")
    table(["Class", "Signs & plaques", "Marking items"],
          [[c, sum(1 for d in devs if d.kind == "sign" and d.cls == c), sum(1 for d in devs if d.kind == "marking" and d.cls == c)]
           for c in CLASSES], [5.5, 5, 5])
    P("Mandatory = code says 'shall' (Standard). Recommended = 'should' (Guidance). Optional = 'may' (Option). "
      "Conditional = depends on a study listed below.", 9, C["mid_gray"])
    by_code = Counter((d.code, d.name, d.cls) for d in devs if d.kind == "sign")
    sec("Signs by type")
    rows = []
    for (code, name, cls), k in sorted(by_code.items(), key=lambda kv: (CLASSES.index(kv[0][2]), kv[0][0])):
        fp = _symbol(rb, code)
        rows.append([("img", fp) if fp else "", code, name, cls, k])
    table(["Sign", "Code", "Name", "Class", "Count"], rows, [2.2, 2.2, 6.5, 3.2, 1.8])
    if rb is not None:
        P("Sign pictures are taken from the MUTCD 11th Edition figures (FHWA, public domain).", 9, C["mid_gray"], True)
    studies = [d for d in devs if d.cls == "Conditional"]
    if studies:
        sec("Studies needed")
        table(["Device", "Code", "Location", "Study"], [[d.id, d.code, d.where, d.study] for d in studies[:80]], [2, 2, 5.5, 7])
    if questions:
        sec("Pending data")
        for q in questions:
            bullet(f"{q['topic']}: {q['question']} ({q['items']})")
    if conflicts:
        sec("Conflicts to check")
        for c in conflicts:
            bullet(c)
    asm = [x for x in log if x.startswith("ASSUMPTION: ")]
    if asm:
        sec("Assumptions and provisional inputs")
        for x in asm:
            bullet(x.replace("ASSUMPTION: ", ""))
    log = [x for x in log if not x.startswith("ASSUMPTION: ")]
    if log:
        sec("Adjustments made")
        for x in log[:150]:
            bullet(x.replace("NOTE: ", ""))
    if audit is not None:
        sec("Audit findings")
        table(["Finding", "Count"], [[k, v] for k, v in Counter(a["finding"] for a in audit).items()], [10, 3])
    sec("Limitations of this version")
    for s_ in ["Guide/directional signs and temporary traffic control are not designed in this version.",
               "Advisory curve speeds are computed from geometry (FHWA ball-bank approximation); confirm with a ball-bank or GPS study.",
               "Sight distance is not computed; 'Ahead' signs are Conditional until sight distance is confirmed.",
               "One-way corner sign positions are approximate."]:
        bullet(s_)
    sec("Sign-off")
    table(["Prepared by", "Checked by", "Approved by", "Date"], [["", "", "", ""]], [4.2, 4.2, 4.2, 3.4])
    doc.save(path)


def dashboard_result(devs: List[Device], questions: List[Dict], outputs: List[str], issues: List[str]) -> Dict:
    c = Counter(d.cls for d in devs if d.kind == "sign")
    return {"status": "waiting" if questions else "done",
            "counts": {"mandatory": c.get("Mandatory", 0), "recommended": c.get("Recommended", 0),
                       "optional": c.get("Optional", 0), "conditional": c.get("Conditional", 0),
                       "pending": len(questions)},
            "issues": " ".join(issues)[:1500], "outputs": "\n".join(outputs)}


def write_id_map(base: str, net, base_dxf: str | None = None):
    """Label every link and node id so an engineer can answer the data questions."""
    from .geom import point_along, length
    feats = []
    names = net.link_names()
    for l in net.links.values():
        feats.append({"type": "Feature", "geometry": {"type": "LineString", "coordinates": [list(p) for p in l.coords]},
                      "properties": {"name": names[l.id], "id": l.id, **{k: v for k, v in l.props.items() if k != "id"}}})
    for n in net.nodes.values():
        feats.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": list(n.xy)},
                      "properties": {"id": n.id, "label": net.node_label(n.id), "degree": n.degree,
                                     "control": n.props.get("control")}})
    with open(base + ".geojson", "w", encoding="utf-8") as fh:
        json.dump({"type": "FeatureCollection", "features": feats}, fh, indent=1)
    if base_dxf:
        import ezdxf
        doc = ezdxf.readfile(base_dxf)
        msp = doc.modelspace()
        lay = "SIGN-IDS"
        if lay not in doc.layers:
            doc.layers.add(lay, color=6)
        th = float(getattr(net, "style", {}).get("text_height", 2.5) or 2.5) * 1.5
        for l in net.links.values():
            p, _ = point_along(l.coords, length(l.coords) / 2)
            msp.add_text(names[l.id], dxfattribs={"layer": lay, "height": th}).set_placement(p)
        for n in net.nodes.values():
            msp.add_circle(n.xy, th, dxfattribs={"layer": lay})
            msp.add_text(net.node_label(n.id), dxfattribs={"layer": lay, "height": th}).set_placement((n.xy[0] + th, n.xy[1] + th))
        doc.saveas(base + ".dxf")


# ------------------------------------------------------------------ T&I style pack (layers, line types, blocks, details)
def load_style_pack(name: str | None):
    """Load styles/<name>/ (style.yaml, template.dxf, block_map.csv). None or 'none' -> None."""
    import os, csv, yaml
    if not name or str(name).lower() == "none":
        return None
    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "styles", name)
    if not os.path.isdir(root):
        return None
    sp = yaml.safe_load(open(os.path.join(root, "style.yaml"), encoding="utf-8"))
    sp["dir"] = root
    sp["template_path"] = os.path.join(root, sp.get("template", "template.dxf"))
    rows = []
    bm = os.path.join(root, "block_map.csv")
    if os.path.exists(bm):
        with open(bm, encoding="utf-8") as fh:
            rows = list(csv.DictReader(l for l in fh if not l.startswith("#")))
    sp["block_map"] = rows
    return sp


def pack_block_for(sp, d) -> str:
    """Approved T&I block for a device, or ''."""
    if not sp:
        return ""
    for r in sp.get("block_map", []):
        if r.get("mutcd_code") != d.code or str(r.get("approved", "")).strip().lower() not in ("yes", "y", "true"):
            continue
        w = (r.get("when") or "").strip()
        if w.startswith("orient="):
            if w.split("=", 1)[1].lower() not in (d.orientation or "").lower():
                continue
        elif w.startswith("legend="):
            if w.split("=", 1)[1].strip().lower() != (d.legend or "").strip().lower():
                continue
        return r["block"]
    return ""


def fixation_for(sp, d) -> Dict:
    fx = (sp or {}).get("fixation") or {}
    det = fx.get("details", {})
    name = det.get(d.code) or det.get(d.family) or det.get("warning", "")
    return {"detail": name, "post": fx.get("post", ""), "base": fx.get("base", ""),
            "height": fx.get("height_to_bottom_m")}


def draw_sign_indicator(msp, x: float, y: float, layer: str, scale: float = 1.0):
    """Generic sign-position marker (build spec 10.3): circle r 0.6 m centred 1.2 m north of the point, plus a
    2.4 x 0.5 m bar rotated -20 degrees centred 0.6 m south of the point. Colour 7, no text."""
    import math
    msp.add_circle((x, y + 1.2 * scale), 0.6 * scale, dxfattribs={"layer": layer, "color": 7})
    cx, cy, a = x, y - 0.6 * scale, math.radians(-20)
    pts = []
    for dx, dy in ((-1.2, -0.25), (1.2, -0.25), (1.2, 0.25), (-1.2, 0.25)):
        dx, dy = dx * scale, dy * scale
        pts.append((cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)))
    msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": layer, "color": 7})


SCHEDULE_COLS = ("No.", "Type", "Control / plan", "E", "N")


def draw_schedule_table(msp, junctions: List[Dict], origin, layer: str, tstyle: str, scale: float = 1.0) -> Dict:
    """Junction and dead-end schedule table (build spec 10.4): title at 2.6, five columns, text 2.0, rows 4.0 m.
    `origin` is the top-left corner (E, N). Column widths follow the longest text in each column."""
    th, row_h = 2.0 * scale, 4.0 * scale
    rows = [[str(j.get("id", "")), str(j.get("type", "")),
             " / ".join(x for x in (str(j.get("control") or ""), str(j.get("plan") or "")) if x),
             f"{float(j['e']):.1f}", f"{float(j['n']):.1f}"] for j in junctions]
    cells = [list(SCHEDULE_COLS)] + rows
    widths = [max(len(r[c]) for r in cells) * th * 0.8 + 2 * scale for c in range(5)]
    x0, y0 = float(origin[0]), float(origin[1])
    ea = {"layer": layer, "style": tstyle}
    msp.add_text("JUNCTION AND DEAD-END SCHEDULE (DRAFT)", height=2.6 * scale, dxfattribs={**ea, "insert": (x0, y0 + 3 * scale)})
    total_w, total_h = sum(widths), row_h * len(cells)
    for i in range(len(cells) + 1):
        y = y0 - i * row_h
        msp.add_line((x0, y), (x0 + total_w, y), dxfattribs={"layer": layer})
    xs = [x0]
    for w in widths:
        xs.append(xs[-1] + w)
    for x in xs:
        msp.add_line((x, y0), (x, y0 - total_h), dxfattribs={"layer": layer})
    for i, r in enumerate(cells):
        for c, t in enumerate(r):
            msp.add_text(t, height=th, dxfattribs={**ea, "insert": (xs[c] + scale, y0 - (i + 1) * row_h + (row_h - th) / 2)})
    return {"x0": x0, "y0": y0, "w": total_w, "h": total_h}


def write_dxf_styled(path: str, devs: List[Device], rb, sp: Dict, base_dxf: str | None = None,
                     scale: float = 1.0, junctions: List[Dict] | None = None, table_origin=None,
                     draft: bool = True) -> List[str]:
    """DXF in the T&I style pack. Returns notes for the QA log.

    `junctions` (optional, from overrides `junctions`): confirmed junction / dead-end points
    {id, type, control, plan, e, n}. When given, a sign-indicator symbol is drawn at each point and the
    schedule table is added. `table_origin` [E, N] overrides the default place (right of the design, above the details).
    Chevron and arrow (TI-614..619, L13-n) placement is NOT implemented: see SKILL.md open items."""
    import ezdxf
    from ezdxf.addons import Importer
    from ezdxf import bbox
    notes = []
    doc = ezdxf.readfile(base_dxf) if base_dxf else ezdxf.new("R2018", setup=True)
    if not base_dxf:
        doc.header["$INSUNITS"] = 6
    tpl = ezdxf.readfile(sp["template_path"])
    # dimensions and multileaders lose their geometry blocks when copied: explode them into lines and text first
    for e in list(tpl.modelspace().query("DIMENSION MULTILEADER")):
        try:
            e.explode()
        except Exception:
            tpl.modelspace().delete_entity(e)
    imp = Importer(tpl, doc)
    imp.import_tables("*")
    L = sp.get("layers", {})
    lay_sign, lay_study = L.get("sign", "TI-Signs"), L.get("study", "TI-Signs")
    lay_lab, lay_mark = L.get("label", "TI-Text"), L.get("marking", "TI-MARKING")
    for n in (lay_sign, lay_study, lay_lab, lay_mark):
        if n not in doc.layers:
            doc.layers.add(n)
    for name, lt in (sp.get("added_linetypes") or {}).items():
        if name not in doc.linetypes:
            doc.linetypes.add(name, pattern=lt["pattern"], description=lt.get("description", name))
    # which template blocks are needed
    use = {}
    for d in devs:
        if d.kind == "sign" and d.x is not None:
            b = pack_block_for(sp, d)
            if b and b in tpl.blocks:
                use[d.id] = b
    for b in sorted(set(use.values())):
        imp.import_block(b, rename=False)
    # standard details from the template model space
    skip = set((sp.get("details") or {}).get("skip_layers", []))
    tmsp = tpl.modelspace()
    det_ents = [e for e in tmsp if e.dxf.layer not in skip]
    msp = doc.modelspace()
    before = set(e.dxf.handle for e in msp)
    base_ext = bbox.extents(msp, fast=True) if base_dxf else None
    imp.import_entities(det_ents, msp)
    imp.finalize()
    th = float(sp.get("text_height", 2.0)) * scale
    tstyle = sp.get("text_style", "Standard") if sp.get("text_style", "Standard") in doc.styles else "Standard"
    made = set()
    xs = [d.x for d in devs if d.x is not None] + [p[0] for d in devs if d.geometry for p in d.geometry]
    ys = [d.y for d in devs if d.y is not None] + [p[1] for d in devs if d.geometry for p in d.geometry]
    if base_ext is not None and base_ext.has_data:
        xs.append(base_ext.extmax.x)
        ys.append(base_ext.extmin.y)
    det_top = None
    # move the imported details beside the design
    new = [e for e in msp if e.dxf.handle not in before]
    if new and xs:
        try:
            tb = bbox.extents(det_ents, fast=True)
            gap = float((sp.get("details") or {}).get("gap_m", 100))
            dx = max(xs) + gap - tb.extmin.x
            dy = min(ys) - tb.extmin.y
            m = ezdxf.math.Matrix44.translate(dx, dy, 0)
            moved = 0
            for e in new:
                try:
                    e.transform(m)
                    moved += 1
                except Exception:
                    msp.delete_entity(e)
            msp.add_text("T&I STANDARD SIGN AND MARKING DETAILS", height=8.0,
                         dxfattribs={"layer": lay_lab, "style": tstyle,
                                     "insert": (tb.extmin.x + dx, tb.extmax.y + dy + 15)})
            det_top, det_x = tb.extmax.y + dy + 15 + 8.0, tb.extmin.x + dx
            notes.append(f"T&I standard details placed {gap:.0f} m right of the design ({moved} entities)")
        except Exception as ex:
            notes.append(f"T&I details not placed: {ex}")
    for d in devs:
        if d.kind != "sign" or d.x is None:
            continue
        rot = (90 - (d.azimuth_deg or 0)) % 360 + 90
        layer = lay_study if d.cls == "Conditional" else lay_sign
        bname = use.get(d.id)
        if bname:
            ins = msp.add_blockref(bname, (d.x, d.y), dxfattribs={"layer": layer, "xscale": scale, "yscale": scale,
                                                                   "zscale": scale, "rotation": rot})
        else:
            cat = rb.devices.get(d.code, {})
            shape = cat.get("shape", "square")
            bname = f"MUTCD_{shape.upper()}"
            if bname not in made and bname not in doc.blocks:
                blk = doc.blocks.new(bname)
                pts = SHAPES.get(shape)
                if pts is None:
                    blk.add_circle((0, 0), 0.8)
                else:
                    blk.add_lwpolyline(pts, close=True)
                blk.add_line((0, -1), (0, -2.2))
                made.add(bname)
            ins = msp.add_blockref(bname, (d.x, d.y), dxfattribs={"layer": layer, "xscale": scale, "yscale": scale,
                                                                 "zscale": scale, "rotation": rot,
                                                                 "color": ACI.get(cat.get("color", ""), 256)})
        if d.cls == "Conditional":
            ins.dxf.color = 8
        msp.add_text(f"{d.code} {d.id}", height=th, dxfattribs={"layer": lay_lab, "style": tstyle,
                     "insert": (d.x + 1.5 * scale, d.y + 0.5 * scale)})
    if draft and xs and ys:
        msp.add_text(f"DRAFT - rulebook {rb.code} status: {rb.meta.get('status')} - not for issue", height=4.0 * scale,
                     dxfattribs={"layer": lay_lab, "style": tstyle, "insert": (min(xs), max(ys) + 25 * scale)})
    if junctions:
        bad = [j for j in junctions if j.get("e") is None or j.get("n") is None]
        junctions = [j for j in junctions if j not in bad]
        if bad:
            notes.append("junction rows without E/N skipped: " + ", ".join(str(j.get("id")) for j in bad))
        for j in junctions:
            draw_sign_indicator(msp, float(j["e"]), float(j["n"]), lay_sign, scale)
        if table_origin:
            org = table_origin
        elif xs:
            org = (max(xs) + float((sp.get("details") or {}).get("gap_m", 100)),
                   max(ys + ([det_top] if det_top else [])) + 30 * scale)
        else:
            org = (junctions[0]["e"], junctions[0]["n"]) if junctions else (0, 0)
        box = draw_schedule_table(msp, junctions, org, lay_lab, tstyle, scale)
        notes.append(f"sign-indicator symbols at {len(junctions)} junction/dead-end points; schedule table at "
                     f"E {box['x0']:.0f}, N {box['y0']:.0f} (Zoom Extents includes it)")
    lts = sp.get("marking_linetypes") or {}
    for d in devs:
        if d.kind == "marking" and d.geometry:
            m = rb.markings.get(d.code, {})
            pat = "left_edge" if d.code == "EL-SY" else m.get("pattern", "solid")
            lt = lts.get(pat, "Continuous")
            if lt not in doc.linetypes:
                lt = "Continuous"
            col = 2 if m.get("color") == "yellow" else 7
            msp.add_lwpolyline(d.geometry, dxfattribs={"layer": lay_mark, "linetype": lt, "color": col})
    notes.append(f"T&I sign blocks used: {len(use)} of {sum(1 for d in devs if d.kind == 'sign')} signs "
                 f"(block_map.csv rows approved: {sum(1 for r in sp.get('block_map', []) if str(r.get('approved','')).lower() in ('yes','y','true'))})")
    doc.saveas(path)
    return notes
