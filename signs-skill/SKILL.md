---
name: road-signing
description: Design or audit traffic signs and pavement markings for an urban road network to MUTCD 11th Edition (and, when extracted, the Egyptian code and other codes), using the T&I detail drawing style, T&I sign blocks, the control workbook and the signing engine. Use for any road-signing, junction-control, dead-end or marking request.
---

# Road signing skill (T&I Transportation Systems)

Authority for every detail: `docs/Signs_Skill_Build_Instructions.md` (the build specification; section numbers below refer to it).
Every device is tagged Mandatory / Recommended / Optional / Conditional with its clause. The engine produces a draft; a T&I engineer signs off.

## 1. Where things are

- Skill root: `signs-skill/` (`engine/`, `rulebooks/<code>/`, `styles/ti_details/`, `brand/`, `refs/`, `tests/`, `docs/`).
- Laptop: root `D:\0T&I AI Work\Signs\`; engine `_Engine\Signs-Skill\`; brand `Brand\`; projects `Projects\<CODE>_<Name>\`. Keep paths configurable.
- Project folder: `00_Control/` (control workbook), `01_Input/` (copy of the drawing, never edit the original), `02_Runs/<date>_run<n>/`, `03_Outputs/<date>_<name>/`.
  Create with `python -m engine.project new --root Projects --code TL00 --name Wyte` (bilingual EN/AR workbook, `..._Control_DRAFT.xlsx`).
  Sheets: Settings, Inputs, Questions, Junctions, Runs, Rulebook.
- Junction numbers: `engine.project.number_junctions` (roundabouts, then T-junctions, then others, north to south; dead ends D01..).
- MUTCD text: `refs/MUTCD_11th_Edition.md` (page markers; `grep -n "Section 2B.18"`). The PDF stays authoritative.
- Readable rulebooks: `python -m engine.rulebook_doc` and `python -m engine.rulebook_full_doc`; `docs/` holds the last copies.
- Windows: `$env:PYTHONUTF8=1` before any run; Python 3.13; run from inside `signs-skill` as `python -m engine.run ...`.
  Packages: ezdxf pyproj openpyxl pyyaml python-docx Pillow matplotlib. DWG cannot be read: ask for a DXF export.

## 2. Codes and rulebooks

- `rulebooks/mutcd_11e/`: the main guide. `code.yaml` status is `extracting` until a T&I engineer signs off, so **all output is DRAFT**:
  the word DRAFT is in every output file name, sheet title, drawing title and report header.
- `rulebooks/egypt/` and `rulebooks/shc/`: **scaffolds only** (`code.yaml` status `extracting`; `devices.csv` holds the Egyptian numbers seen on the T&I details sheet with names and clauses EMPTY; the SHC catalog is empty). Egyptian values cannot be read until the scanned Arabic PDF (Code 104, Part 2) is in the project, and SHC needs its source. Do not write names, clauses or rules for them without that source. Say so and ask.
- **Master sign list** (`signs_master/master_links.csv`, `engine/signs_master.py`): a crosswalk between MUTCD, Egyptian and SHC signs for reuse across projects. Each code keeps its own catalog (names, clauses, sizes from that code only); the link table says which signs are the same device, with `match` (same | check | none) and `approved` (only a T&I engineer approves; seeded from the 28 approved block-map rows, 'for now'). Never match by look-alike; Egyptian numbers taken from T&I block names stay `egypt_code_verified = no` until read from the printed code. `python -m engine.signs_master validate` enforces these rules; `... export --out Master_Signs_DRAFT.xlsx` writes the bilingual workbook (only when the user asks).
- Provision map: Standard = Mandatory, Guidance = Recommended, Option = Optional, Study = Conditional.
- Egyptian clauses use Egyptian numbering only (e.g. 5-2-3). Never put a MUTCD number in an Egyptian field, or the reverse. Egyptian sign codes are numeric (302, 403, 456...), marking codes L-series; a MUTCD equivalent goes only in a reference column.

## 3. T&I detail drawing and block map

- Style pack `styles/ti_details/` (`template.dxf`, `style.yaml`, `block_map.csv`): layers TI-Signs, TI-Text, TI-MARKING, TI-DETAILS; text style JEREC (XARB for Arabic), height 2.0; dim style TI 1000; the T&I details are copied 100 m right of the design.
- `block_map.csv`: only rows with `approved = yes` insert a T&I block; others draw the engine symbol. 28 rows approved, 13 are `check` rows T&I must still confirm. Block name `speed hump` must match the name inside `template.dxf` exactly.
- Sign-indicator symbol (10.3, implemented): circle r 0.6 m at 1.2 m north of the point plus a 2.4 x 0.5 m bar rotated -20 degrees at 0.6 m south, TI-Signs, colour 7, no text. Drawn at the confirmed junction/dead-end points only.
- Schedule table in the DXF (10.4, implemented): title "JUNCTION AND DEAD-END SCHEDULE (DRAFT)" (2.6), 5 columns (No., Type, Control / plan, E, N), text 2.0, rows 4.0 m, on TI-Text.
  Feed both through `overrides.json`: `"junctions": [{"id","type","control","plan","e","n"}]` and optional `"schedule_table_origin": [E, N]`.
  Default place: right of the design, above the T&I details. After a run, check in AutoCAD with Zoom Extents.
- Chevron and arrow placement (10.5, TI-614..619, L13-1..6) and detail callouts (10.6) are **not implemented**. The DXF must not claim to follow the house method. See section 9.

## 4. Input handling

- DXF: list layers with `from engine.adapters import dxf_layers`. Use only the layers the user names; confirm the centreline layer when there is more than one candidate. Pass the kerb layer with `--edge-layers` (else signs sit on the centreline offset by half width and are Low confidence). Read with ezdxf, never as text.
- GeoJSON/OSM needs the project EPSG. CSV/XLSX: links table (`id`, vertices) and optional nodes table.
- **Re-read before every run** (5.3): the engine writes `layer_counts.json` into the run folder; pass the last run's file with `--compare-counts`. Any change is reported as INPUT CHANGED; do not reuse old junction numbers or coordinates until the user re-confirms them.
- Topology (6): 1 m node snap, 12 m T-snap, 8 m node points. Intersection = 3+ legs, excluding split/merge nodes of one-way carriageways. Dead-end shape (hammerhead / cul-de-sac) and free ends are confirmed by the user from screenshots.

## 5. Workflow

1. Read the project (control workbook). 2. Get inputs; re-read the drawing (section 4). 3. Check the code and its status. 4. Write `settings.json`
(mode, code, families, level, units, drive=`right`, size, env, missing, outputs, epsg, tol, style). 5. Write `overrides.json` from the user's answers only
(all_links, by_class, links, all_nodes, nodes, pois, exclude_links, junctions, `_sources`; mark provisional answers PROVISIONAL; speeds in km/h).
6. Run:
```
python -m engine.run --input <file> --settings settings.json --overrides overrides.json --out <outdir> --project "<name>" \
    --layers "<centreline>" --edge-layers "<kerb>" [--compare-counts <last layer_counts.json>] [--inventory existing.geojson] [--epsg 22992] [--dxf] [--allow-partial]
```
7. Exit codes: 0 done (read `result.json`); 2 missing data (read `questions.json` and `network_ids.*`, show the questions as a list with their `eng-*` ids, record answers in the Questions sheet, rerun); 3 input problem (ask).
   **Links are named node-to-node by default** (`N009-N010`); the engine id follows in brackets only for traceability. Questions, the id map (label at the arc-length midpoint), the schedule and every figure or table shown to the user use that form. `overrides.json` accepts either form as a key (`\"links\": {\"N009-N010\": {...}}`, `stop_approaches`), in either direction; a name that matches no link is ignored and logged. Parallel links between the same two nodes get `~<engine id>` appended. `--allow-partial` only when the user explicitly skips a question; record each skipped question.
8. Report counts, Conditional items, Low-confidence devices, spacing moves, DRAFT status. **Deliver files only when asked** (below).
9. After a major task, offer `/explain-usage` and ask first. End every chat with a handoff: decisions, current state, next steps.

## 6. Rules that must not be broken

1. Never fill missing data silently. Ask. A skipped value stays empty and is reported as skipped.
2. Every output says DRAFT while the rulebook is not signed off.
3. Egyptian clauses use Egyptian numbering only.
4. Guide signs and temporary traffic control are not in v1 (guide signs need a destinations list).
5. Sight distance is not computed: Stop, Yield and Signal Ahead are Conditional until `sight_restricted` is confirmed.
6. Advisory curve speeds (FHWA ball-bank, f = 0.21/0.18/0.15, floor 10 km/h) need a ball-bank or GPS study before issue.
7. Speeds in km/h (5 mph = 10 km/h; 30 mph = 50; 45 mph = 70). Chevron bands 20/50/70/100 km/h. Hazard distances use Table 2C-3 Condition B (state it as an engine assumption).
8. A DXF block, label or figure reference is a cross-check, never a verified value, until the printed code confirms it.
9. Do not write sign schedules (.xlsx), GeoJSON, DXF or report (.docx) files for the user until asked; confirm once before sending.
10. `--allow-partial` only when the user explicitly skips a question. 11. Re-read the input before every run and compare layer counts. 12. Old junction coordinates are not reused without that check.
- Grade crossings: W10-1 Mandatory on every approach (user removes it where 8B.06-01 applies); Crossbuck 4.6 m + half gauge before the track.
- Not automated (place by hand or as `type: sign` points): ONE WAY / Keep Right at divided crossings (2B.49), Yield Here To Pedestrians (2B.19), BEGIN/END ONE WAY, roundabout island signs, parking, W10-2/3/4, W12-2a.
- **Placement rules and workflow**: `docs/Sign_Placement_Rules.md` (stations, offsets, heights, spacing, QA, the 81 rules, and the manual-placement method). MUTCD values only; Egyptian and SHC placement values must come from their own sources.
- Roundabouts need `inscribed_radius_m` from the user; school zones need `school_zone: true` only where designated by statute.

## 7. Adding another code

Copy `rulebooks/mutcd_11e/` to `rulebooks/<code>/`; keep file names and columns; replace values and clauses from that code only; set `traffic_side` and `status: extracting`.
Triggers and placement are shared. Run `python tests/test_engine.py`, `python tests/test_verification.py`, `python tests/test_features.py` and `python tests/test_master.py`.
Rule authoring: `provision_if` first match wins; `companions` as code or `{device, provision, ...}`; new hazard = `hazards.yaml` entry + rule with trigger `HAZ-<TYPE>`; record the source in each `clause`; `verify: false` until T&I confirms.

## 8. Verification status (28 Oct 2026)

- MUTCD 11e checked against the T&I PDF: sign names and sizes (Tables 2B-1, 2C-1, 7B-1), Tables 2C-3 to 2C-6, mounting and offsets (2A.15, 2A.16), 2B.49, 2C.55, 3B.02, 3B.10.
  Open: advisory friction values (FHWA-SA-11-22), delineator spacing (Chapter 3G), 54 unverified rules (`verify: false`).
- Egyptian code: scaffold only, nothing verified. Status stays `extracting` until a T&I engineer signs off.
- Tests: `test_engine.py` 6/6, `test_verification.py` 74/74, `test_features.py` 7/7, `test_master.py` 5/5.

## 9. Open items

1. Egyptian PDF upload, then extraction (Egyptian numbering). 2. Egyptian sign numbers are now in the master list as unverified labels (204, 305-307, 324-325, 405 and others); read their names from the printed code, then set `egypt_code_verified`. 3. Confirm the 13 `check` block-map rows.
4. SHC (KSA): re-attach the five snaps; separate rulebook; no look-alike matching. 5. **Chevron/arrow placement (TI-614..619, L13-1..6): not implemented, awaiting the user's rule** (see the handoff notes). 6. Confirm the sign-indicator placement rule for future areas.
7. Rename `sprrd hump` to `speed hump` in the laptop template and map together. 8. Replace the plain-word traffic-management column with sign codes after the rulebook check.
9. Wyte AADT (18 links skipped). 10. Wyte roundabout J01 radius (10 m, taken from the ring). 11. Confirm collector run H2F451-1..5 and major link N009-N010. 12. Real building placement (TI - Buildings, layer TI - BM).
13. Guide signs need a destinations list. 14. Engineer verification of 54 rules. 15. Dashboard (`Signs_Dashboard.html`) not built.
