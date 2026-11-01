"""Master sign list checks: python tests/test_master.py"""
import csv, os, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from engine import signs_master as sm


def test_seed_is_valid():
    assert sm.validate() == []


def test_seed_matches_block_map():
    bm = [r for r in csv.DictReader(l for l in open(os.path.join(ROOT, "styles/ti_details/block_map.csv"), encoding="utf-8")
                                    if not l.startswith("#")) if r["approved"].lower() == "yes"]
    links = {(r["mutcd_code"], r["when"], r["ti_block"]) for r in sm.load_links() if r["mutcd_code"]}
    assert {(r["mutcd_code"], r["when"], r["block"]) for r in bm} == links


def _with(rows_edit):
    orig = sm.load_links
    sm.load_links = lambda: rows_edit(orig())
    try:
        return sm.validate(check_blocks=False)
    finally:
        sm.load_links = orig


def test_rejects_mixed_codes():
    def e(rows):
        rows[0] = dict(rows[0], egypt_code="R1-1")
        return rows
    assert any("looks like a MUTCD code" in x for x in _with(e))
    def e2(rows):
        rows[0] = dict(rows[0], mutcd_code="301")
        return rows
    assert any("not a MUTCD code" in x for x in _with(e2))


def test_approval_needs_signoff_and_no_shc_without_catalog():
    def e(rows):
        rows[0] = dict(rows[0], approved_by="", approved_date="")
        return rows
    assert any("needs approved_by" in x for x in _with(e))
    def e2(rows):
        rows[0] = dict(rows[0], shc_code="S-1")
        return rows
    assert any("not in rulebooks/shc" in x for x in _with(e2))


def test_export_pulls_names_from_own_catalog():
    import openpyxl
    p = os.path.join(tempfile.mkdtemp(), "m.xlsx")
    n = sm.export_xlsx(p)
    ws = openpyxl.load_workbook(p)["Master list"]
    assert n > 1000 and "DRAFT" in ws["A1"].value
    r = next(r for r in ws.iter_rows(min_row=6, values_only=True) if r[2] == "R1-1")
    assert r[3] == "Stop" and r[6] == "301" and r[7] in (None, "") and r[10] in (None, "")   # no Egyptian/SHC name invented


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
            print("ok", n)
