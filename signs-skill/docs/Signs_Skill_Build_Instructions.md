# Signs Skill: Complete Build Instructions for Claude Code

Owner: T&I Transportation Systems (Yarah-B)
Status: working draft, written 28 Oct 2026 from the Wyte (TL00) pilot.
Purpose: give Claude Code every detail it needs to build the road-signing skill as a reusable artifact. The skill must work for any urban area and be extendable to other network types and codes, following the same method as the Wyte pilot.

---

## 0. Ground rules (apply to every step)

1. **Never invent a value.** If an input is missing, ask the user. A value the user skips (for example AADT) stays empty and is reported as skipped.
2. **Every output is DRAFT** until a T&I engineer signs off the rulebook (`code.yaml` status = `signed`). Put the word DRAFT in every file name, sheet title, drawing title and report header.
3. **Deliver only when asked.** Do not write sign schedules (.xlsx), GeoJSON, DXF or report (.docx) files to the user's folder or the chat until the user asks. Report counts and issues first.
4. **Ask before a deliverable.** Before any file goes to the user, confirm once. After a major task, offer the user `/explain-usage` and ask for confirmation first.
5. **Handoff at the end of each chat:** decisions, current state, next steps.
6. **Never copy a value between codes.** An Egyptian clause or sign number must never carry a MUTCD number, and the reverse.
7. **Right-hand traffic** is the default (Egypt). Set `drive` to `right` unless the project says otherwise.

---

## 1. Environment

### 1.1 Laptop (Windows)
- Root folder: `D:\0T&I AI Work\Signs\`
- Engine zip: `D:\0T&I AI Work\Signs\_Engine\Signs-Skill_v1.8.zip` (also in `D:\0T&I AI Work\Codes for Claude\Signs-Skill\`)
- Extracted engine: `D:\0T&I AI Work\Signs\_Engine\Signs-Skill\`
- Brand: `D:\0T&I AI Work\Signs\Brand\` (holds `TI_Logo_Lockup.png`; the logo is the full lock-up on white, never Primary Green)
- MUTCD 11th Edition PDF: `D:\Yarah Basyoni\0T&I AI Work\Codes for Claude\` (authoritative text)
- Projects: `D:\0T&I AI Work\Signs\Projects\<CODE>_<Name>\`

### 1.2 Python and PowerShell
- Python 3.13 (not 3.16 alpha).
- In PowerShell, before any engine run: `$env:PYTHONUTF8=1` (without it, Unicode output crashes on Windows with a charmap error).
- Packages: `pip install ezdxf pyproj openpyxl pyyaml python-docx Pillow matplotlib --break-system-packages` (the last flag applies in the sandbox; on Windows use a normal venv).
- Run engine commands from inside the `Signs-Skill` folder, with `PYTHONPATH` set to that folder, as `python -m engine.run ...`.

### 1.3 Sandbox (for Claude Code work)
- Chromium and Playwright are pre-installed; do not reinstall them.
- Arial is not installed in the sandbox. Use a substitute font in preview images and say so.
- DWG cannot be read here. Ask the user for a DXF export (AutoCAD `SAVEAS`, "AutoCAD 2018 DXF", or ODA File Converter).

---

## 2. Repository layout (the artifact Claude Code builds)

```
signs-skill/
  SKILL.md                      # the skill instructions (see section 13)
  engine/
    __init__.py
    adapters.py                 # input readers: GeoJSON, CSV/XLSX, DXF; property normalisation; control aliases
    cnm.py                      # Common Network Model: Link, Node, POI, Approach, Network
    data.py                     # overrides loading and application; prescan (questions)
    geom.py                     # geometry helpers, feet/metre conversion
    triggers.py                 # detect triggers: intersections, curves, roundabouts, hazards, speed changes
    placement.py                # Placer: sign positions, offsets, orientation, companions, QA
    rulebook.py                 # Rulebook loader: rules.yaml, devices.csv, markings.csv, tables/, code.yaml
    rulebook_doc.py             # readable rulebook (Markdown)
    rulebook_full_doc.py        # full readable rulebook (Markdown and HTML)
    run.py                      # command line entry point (section 9)
    writers.py                  # XLSX schedule, GeoJSON, DXF, DOCX report, dashboard result JSON
  rulebooks/
    mutcd_11e/                  # main guide (signed status in code.yaml)
      code.yaml  rules.yaml  devices.csv  markings.csv  hazards.yaml  sign_catalog.json
      tables/ advance_placement.csv  chevron_spacing.csv  curve_devices.csv  mounting.csv  passing_sight.csv
    egypt/                      # scaffold until the Egyptian code is extracted (section 12)
  styles/ti_details/
    template.dxf                # T&I detail drawing (copy of "ACAD-Signs & Markings Details EGY & KSA.dxf")
    style.yaml                  # layers, text style, dim style, marking line types
    block_map.csv               # MUTCD code -> T&I block, with match and approved columns
  brand/
    brand.yaml  TI_Logo.png  TI_Report_Template.docx
  refs/
    MUTCD_11th_Edition.md       # full text with page markers (search with grep -n)
  tests/
    test_engine.py              # 6 tests, must pass
    test_verification.py        # 74 hand-checked cases, must pass
    settings_default.json  settings_audit.json  overrides_rural_dxf.json  make_networks.py
```

Keep this layout when the skill is reused for another area. Only the project folder changes.

---

## 3. Project folder layout (per project, for example `TL00_Wyte`)

```
Projects/<CODE>_<Name>/
  00_Control/   <CODE>_<Name>_Control.xlsx     # sheets: Settings, Inputs, Questions, Junctions, Runs, Rulebook
  01_Input/     the input drawing or network (copy, never edit the original)
  02_Runs/      <date>_run<n>/                  # settings.json, overrides.json, network_ids.*, questions.json, result.json
  03_Outputs/   <date>_<name>/                  # only after the user asks: sign schedule, GeoJSON, DXF, report
```

The project code is the user's code (for example `TL00`). Project name comes from the input file name, unless the user says otherwise.

---

## 4. Control workbook (`<CODE>_<Name>_Control.xlsx`)

Build with openpyxl. English and Arabic side by side (each sheet has an English title and an Arabic title; column headers are in both languages). Use Arial, Primary Green #019945 for headers, Neutral Tint #F4F6F5 for banding, Charcoal #434343 for secondary headings. Run `recalc.py` (LibreOffice) after writing formulas; expect 0 errors.

### 4.1 Sheets
- **Settings**: project code, name, client, location, speed limit (km/h), drive side, code, families, level, units, size, environment, missing-data rule, outputs, EPSG, tolerance (tol), drawing style (`ti` or `input`).
- **Inputs**: name, role, format, CRS, path, status.
- **Questions**: id, topic, question, items, suggested answer, status (open or answered), answer, source (skill or user).
- **Junctions**: one row per junction or dead end. Columns: Junction ID, type (roundabout, T-junction, crossing, hammerhead dead end, cul-de-sac, other), engine node ID, E, N, traffic management plan (plain words for now; MUTCD code later), type of control (signal, stop_all, stop_minor, yield, roundabout, none), stop approaches (link names), sight restricted (yes or no), notes.
- **Runs**: run id, date, settings, counts (mandatory, recommended, optional, conditional, pending), issues, outputs, status (queued, waiting, running, done, failed).
- **Rulebook**: code, status, verified count, unverified count, last review date.

### 4.2 Junction numbering (method used for Wyte)
- Number roundabouts first, then T-junctions, then dead ends. Within a group, number north to south (larger N first), unless the user gives a different order.
- Use the labels J01 to Jnn for junctions and D01 to Dnn for dead ends.

---

## 5. Input handling

### 5.1 DXF (the pilot format)
- Centreline layer: find with `from engine.adapters import dxf_layers; print(dxf_layers('file.dxf'))`. Confirm the layer with the user when more than one candidate exists.
- Only the layers the user lists are used. Ignore every other layer.
- Edge-of-carriageway layer (kerbs): pass it with `--edge-layers`. Signs are then offset from the drawn kerb. Without it, signs are placed on the centreline offset by the half width and marked Low confidence.
- Building layer for sight obstruction: the user names it (Wyte: TI - BM, block `TI - Buildings`).
- Reading the file: `ezdxf.readfile`. Supported entities: LINE, LWPOLYLINE (with bulges), POLYLINE, ARC, POINT, INSERT (for nodes), CIRCLE. Do not read the DXF as text (it can be 400,000+ lines).
- The centreline layer can be closed (a roundabout ring) or open (a road).

### 5.2 Other formats
- GeoJSON or OSM: needs the project EPSG (settings `epsg`).
- CSV or XLSX: links table with `id`, `x1 y1; x2 y2` vertices, and optional nodes table with `id, x, y, control`.
- DWG: ask for a DXF export.

### 5.3 Re-reading a changed file
- The laptop file can change between sessions. Re-read it before every run:
  1. Stage the file from the laptop (or copy it into the scratch folder).
  2. Recount entities by layer and type.
  3. Compare the new layer counts with the previous run. Report any change before using the old junction numbers.
- In the Wyte pilot, the file changed between sessions; the earlier J02–J04 crossing points were superseded. Never reuse junction coordinates from an old run without this check.

---

## 6. Network topology (engine behaviour)

- Node snapping: link ends within 1 m of each other join.
- T-junction snapping: a link end within 12 m of another link's segment joins it as a T (`tee_tol`).
- Node points (POINT or INSERT on a node layer) attach to a link end within 8 m.
- Intersection = a node with 3 or more legs, excluding the split, merge and diverge nodes of one-way carriageways.
- Roundabout = a closed centreline ring, with arms joining the ring. Set control `roundabout` on the centre node and `yield` on the arm entries.
- Dead end = a node with one leg. Classify by shape: hammerhead (T-shaped head) or cul-de-sac (round bulb). Classification is manual, confirmed by the user from screenshots.
- Free ends that are not dead ends (for example a road that continues off-drawing, or a road that continues along the main road) are confirmed by the user and excluded from the dead-end list.

---

## 7. Questions and overrides

### 7.1 Question flow
1. Run the engine (section 9). Exit 2 means missing data. The engine writes `questions.json` and `network_ids.*`.
2. Show the questions to the user as a list. Each question has an id (`eng-*`), a topic, the question text and the affected items.
3. Record each answer in the workbook's Questions sheet (status answered, source user).
4. Translate answers into `overrides.json` (section 7.2).
5. Rerun. Repeat until exit 0. Use `--allow-partial` only when the user explicitly skips a question. Record every skipped question in the Questions sheet and in `result.json`.

### 7.2 Overrides schema (`overrides.json`)

```json
{
  "all_links":  {"class": "local", "speed_kmh": 30, "lanes": 2, "oneway": false, "urban": true},
  "by_class":   {"arterial": {"speed_kmh": 60}},
  "links":      {"H2F451-1": {"class": "collector"}},
  "all_nodes":  {},
  "nodes": {
    "N011": {"control": "roundabout", "inscribed_radius_m": 10},
    "N001": {"control": "stop_minor", "stop_approaches": ["H2F451-3"]},
    "N015": {"control": "yield", "stop_approaches": ["H2F3A2-4"]}
  },
  "pois": {},
  "exclude_links": [],
  "_sources": {"speed_kmh": "posted 30 km/h (user)"}
}
```

- Link attributes: class (freeway, expressway, arterial, collector, local), speed_kmh, lanes (per direction), lanes_total (uneven roads such as 2+1 only), oneway, divided, aadt, urban, curb, lane_width_m, superelevation, sight_restricted, markings.
- Node controls: signal, stop_all, stop_minor, yield, roundabout, none.
- `stop_approaches` lists the link IDs on the minor arms of a stop- or yield-controlled node.
- `inscribed_radius_m` on a roundabout node: centre to the outer edge of the circulating roadway. Ask the user; do not take it from the centreline without confirmation.
- `school_zone: true` only when a school zone is designated by statute.
- `yield_here_signs: true` at mid-block crosswalks where Yield Here To Pedestrians signs (2B.19) are installed.
- `boundary: true`, `entry_speed_kmh`, `exit_control` at site gates.
- Points: `{"type": "sign", "code": "<code>", "facing": "...", "legend": "..."}`. Unknown codes are rejected and logged.
- Hazards: `"pois": {"<id>": {"type": "<hazard type>", ...}}`, with the types from `hazards.yaml`.
- Provisional answers: add a `_sources` entry containing the word PROVISIONAL. The engine reports them.

### 7.3 Link naming for the user
- Engine link IDs look like `H2F451-1` (a handle plus a split number). Show them to the user in node-to-node form: `from-node-to-to-node` (for example `N009-N010`). Use this form in every figure and table shown to the user.
- Put the node-to-node name next to the engine ID in the id map, so the user can point to a link by its ends.
- Labels in figures: place the name at the midpoint of the link by arc length (not by vertex index).

---

## 8. Triggers, placement and devices

- Triggers (`triggers.py`): intersection controls, curves (advisory speeds from geometry), roundabouts, speed changes, hazards, dead ends, school zones, grade crossings, lane drops and merges.
- Placement (`placement.py`): signs are placed on the path at a set distance from the trigger (advance placement from `tables/advance_placement.csv`), offset to the side set by the device rule (right side for right-hand traffic), oriented by the device's orientation rule. Companion plaques are placed on the same support.
- Curve advisory speed: FHWA ball-bank approximation with friction f = 0.21, 0.18 and 0.15, floored at 10 km/h. Always tell the user to confirm with a ball-bank or GPS study before issue.
- Speed units: km/h throughout. Speed conversions use the AASHTO-style steps (5 mph = 10 km/h; 30 mph = 50 km/h; 45 mph = 70 km/h).
- Chevron spacing bands: 20, 50, 70, 100 km/h.
- Hazard advance distances: Table 2C-3 Condition B. Use the point's `advisory_kmh` when given, otherwise the 0 mph column. State this as an engine assumption (2C.04-03).
- Grade crossing: W10-1 is Mandatory on every approach. The user removes it by hand where an 8B.06-01 exception applies. The Crossbuck is placed 4.6 m (15 ft) plus half gauge before the track; confirm the railway's clearance.
- Not automated (place by hand or as `type: sign` points): ONE WAY and Keep Right at divided-highway crossings (2B.49-03 to 05), Yield Here To Pedestrians signs (2B.19), BEGIN and END ONE WAY, roundabout island signs, parking, W10-2/3/4 parallel-highway signs, W12-2a overhead clearance signs.
- Stop, Yield and Signal Ahead signs are Conditional until sight is confirmed (`sight_restricted` true or false). Sight distance is not computed in v1.
- Guide signs and temporary traffic control are not designed in v1. Report them as "not in this version" if their families are selected. Guide signs need a destinations list.

---

## 9. Running the engine

### 9.1 Command
From the `Signs-Skill` folder:

```
python -m engine.run --input <file> --settings settings.json --overrides overrides.json ^
    --out <outdir> --project "<name>" --layers "<centreline layer>" --edge-layers "<kerb layer>" ^
    [--inventory existing.geojson] [--epsg 22992] [--dxf] [--allow-partial]
```

Windows: use `^` for line continuation in cmd, or put the command on one line in PowerShell.

### 9.2 Settings object (`settings.json`)

```json
{"mode": "design", "code": "mutcd_11e", "families": ["reg", "warn", "mark", "delin", "supp"],
 "level": "opt", "units": "metric", "drive": "right", "size": "auto", "env": ["auto"],
 "missing": "batch", "outputs": ["same", "xlsx", "report", "boq"], "epsg": "22992", "tol": 15,
 "style": "ti"}
```

- `mode`: design or audit (audit compares against an existing inventory).
- `level`: mand (Mandatory and Conditional only), rec (adds Recommended), opt (adds Optional).
- `style`: `ti` (default, T&I details) or `input` (keeps the input's layers).

### 9.3 Exit codes
- 0: design done. Read `result.json` for status, counts, issues and outputs.
- 2: missing data. Read `questions.json` and `network_ids.*`, then ask the user (section 7.1).
- 3: input problem (the message is printed). Ask the user.

### 9.4 Outputs (when the user asks)
- `<project>_Sign_Schedule.xlsx`: device list with ID, code, class, provision, clause, position, offset, orientation, legend, confidence.
- `<project>_Signs.geojson`: sign points with the same attributes.
- `<project>_Signing.dxf`: signs and markings on T&I layers, with the T&I details beside the design.
- `<project>_Report.docx`: report on the T&I report template, with the DRAFT header.
- All files carry the word DRAFT and the rulebook status.

---

## 10. Drawing style and T&I blocks

### 10.1 Style pack (`styles/ti_details/style.yaml`)
- Layers: sign TI-Signs; study (Conditional devices, colour 8 grey) TI-Signs; labels TI-Text; markings TI-MARKING; details TI-DETAILS.
- Text style JEREC (swisscl.ttf) for TI-Text; XARB for Arabic text. Text height 2.0.
- Dimension style TI 1000.
- Marking line types: solid and double solid (Continuous), broken 3 m / 9 m (TI-BRK 3-9), dotted 0.9 m / 2.7 m (TI-DOT 0.9-2.7), high visibility (PEDESTRIAN_0_5_0_5), left edge (TI-LE), study (DASHED).
- The T&I standard details are copied 100 m to the right of the design.

### 10.2 Block map (`styles/ti_details/block_map.csv`)
- Columns: mutcd_code, when (optional condition), block (T&I block name), block_meaning, match (same or check), approved (yes or no).
- Only rows with approved = yes are used. Others draw the engine's own symbol.
- `same` rows: same meaning and shape family. `check` rows: close equivalents that T&I must confirm.
- As of 28 Oct 2026: all 28 rows approved, including 13 `check` rows, "for now". Revisit list: T&I to confirm the 13 `check` rows.
- Block name `speed hump` (renamed from `sprrd hump`). The name must match the block inside `template.dxf` exactly. Rename both together. Check that the block inserts after a run.

### 10.3 Sign-indicator symbol
- Generic marker for any sign position (not a sign itself, not a speed hump).
- Geometry: circle of radius 0.6 m, centre 1.2 m north of the point; tilted bar 2.4 m by 0.5 m, rotated -20 degrees, centred 0.6 m south of the point. Both on TI-Signs, colour 7 (white on dark background). No text.
- Placed at the confirmed junction and dead-end points only, unless the user says otherwise.

### 10.4 Schedule table in the DXF
- Title: "JUNCTION AND DEAD-END SCHEDULE (DRAFT)", text height 2.6.
- Table: 5 columns (No., Type, Control / plan, E, N), 2.0 text height, row height 4.0 m, on TI-Text, placed clear of the drawing (for Wyte: top right, starting at E 198790, N 752330).
- Verify placement in AutoCAD with Zoom Extents, which includes the table.

### 10.5 Chevrons and arrows (not yet implemented)
- T&I detail blocks: TI-614 (chevron block, 12 inserts), TI-615 to TI-619 (arrows, about 6 units long; labels ARROW 615 to 619).
- Arrow labels: ARROW (L13-1) to (L13-6) in the detail drawing.
- The engine does not place these yet. The DXF output must not claim to follow the house chevron and arrow method until this is built.
- The house method is in the T&I detail drawing's CHEVRON DETAILS and ARROWS DETAILS sheets. Read them from the template with ezdxf (not as text).

### 10.6 Detail-style callouts (from the SHC snaps)
- Each sign or arrow has a leader line ending in a small white detail marker (post and base symbol with a triangular pointer). Use this convention for T&I style output. Not yet implemented.

---

## 11. Sign catalogue and naming

### 11.1 MUTCD (main guide, in use)
- Codes: letter-number (R, W, M, G, S, D, etc.), for example R1-1 (STOP), R1-2 (YIELD), W1-6 (large arrow), W2-4 (T-junction), W17-1 (speed hump warning).
- Sign sizes and names: Tables 2B-1, 2C-1, 7B-1 (checked against the T&I MUTCD PDF on 12 Oct 2026).
- Clause references: MUTCD numbering (for example 2B.18, 2C.04).

### 11.2 Egyptian code (scaffold, not yet extracted)
- Source: Egyptian Code for Urban and Rural Roads Works, Code 104 (Ecp-2020), Part 2: Traffic Engineering. HBRC, ministerial decree 860 of 2020 (second update).
- The project copy is a scanned Arabic PDF with no text layer. The body starts at about PDF page 24. Until the PDF is in the project, no Egyptian value can be extracted. Say so and ask for it.
- Chapter map: 5 signs (5-1 general; 5-2 regulatory; 5-3 warning; 5-4 guide; 5-5 informational sizes; 5-6 directional). 6 markings (6-1 classes and colours; 6-2 transverse; 6-3 longitudinal; 6-4 other; 6-5 roundabouts; 6-6 typical layouts).
- Egyptian sign codes are numeric (for example 302 yield, 302+329 yield with roundabout ahead, 204 parking, 305/306/307 mandatory directions, 324/325 turns, 402/403/405 warnings with 403 the T-junction, 456 chevron board). Map each code to its official name from the printed code. Record a MUTCD equivalent only in a reference column.
- Egyptian marking codes: L-series (L2-1c, L4-1a, L5-1a, L8-1, L12-2, L13-1 to L13-6 arrows, L17-1, L18-1).
- Clause references: Egyptian numbering (for example 5-2-3). Never MUTCD numbers in an Egyptian field.
- Visual reference: the T&I signs details sheet (signs 302, 302+329, 204, 305, 306, 307, 324, 325, 402, 403, 405, 456).

### 11.3 KSA (SHC) signs (not yet mapped)
- Five snaps were sent (names 1792922182857_image.png to 1792922667716_image.png) but could not be read in the session. Re-attach them, then map the SHC signs.
- Do not match SHC signs to MUTCD or Egyptian codes by look-alike.

---

## 12. Rulebooks and extension to other codes

### 12.1 Rulebook files (every code uses the same file names and columns)
- `code.yaml`: name, status (extracting, checked, signed), traffic side, source document, reviewer, review date.
- `rules.yaml`: one entry per rule: id, trigger, device, provision (Standard, Guidance, Option or Study), provision_if, clause, verify (true or false), companions, placement (kind, side), legend, notes.
- `devices.csv`: code, name, family (regulatory, warning, guide, school, marking, delineator), shape, colour, sizes by class, orientation (lr or none), clause.
- `markings.csv`: code, name, class, colour, line type, width, clause.
- `hazards.yaml`: the hazard types (MUTCD has 34).
- `tables/`: advance_placement.csv, chevron_spacing.csv, curve_devices.csv, mounting.csv, passing_sight.csv.

### 12.2 Provision mapping
- Standard = Mandatory, Guidance = Recommended, Option = Optional, Study = Conditional.

### 12.3 Adding a new code (for example another Gulf manual)
1. Copy `rulebooks/mutcd_11e/` to `rulebooks/<code>/`.
2. Keep file names and column headers. Replace values and clause references from that code only.
3. Set `traffic_side` and `status: extracting`.
4. Triggers and placement are shared. Change the engine only if the code has a trigger MUTCD lacks.
5. Run `python tests/test_engine.py` and `python tests/test_verification.py`.

### 12.4 Verification status (28 Oct 2026)
- MUTCD 11e: checked against the T&I PDF for sign names and sizes, tables 2C-3 to 2C-6, mounting and offsets (2A.15, 2A.16), 2B.49, 2C.55, 3B.02, 3B.10. Still open: advisory speed friction values (FHWA-SA-11-22) and delineator spacing (Chapter 3G).
- Egyptian code: scaffold only. The detail drawing was reviewed for labels, fixing details and arrow blocks. No value is verified.
- Rulebook status stays `extracting` until a T&I engineer signs off.

---

## 13. The SKILL.md (what Claude Code writes)

Front matter:

```
---
name: road-signing
description: Design or audit traffic signs and pavement markings for an urban road network to MUTCD 11th Edition (and, when extracted, the Egyptian code and other codes), using the T&I detail drawing style, T&I sign blocks, the control workbook and the signing engine. Use for any road-signing, junction-control, dead-end or marking request.
---
```

Body sections, in this order:
1. Where things are (folder paths, the control workbook, the engine).
2. Codes and rulebooks (status of each, DRAFT rule).
3. The T&I detail drawing and block map (section 10).
4. Input handling (section 5).
5. Workflow: read project, get inputs, check code, write settings, write overrides, run engine, handle exits, deliver only when asked, report counts (section 9 and 7).
6. Rules that must not be broken (section 14).
7. Adding another code (section 12.3).
8. Verification status (section 12.4).
9. Open items (section 15).

---

## 14. Rules that must not be broken

1. Never fill missing data silently. Ask.
2. Every output says DRAFT while the rulebook is not signed off.
3. Egyptian clauses use Egyptian numbering only.
4. Guide signs and temporary traffic control are not in v1.
5. Sight distance is not computed in v1. Stop, Yield and Signal Ahead are Conditional until sight is confirmed.
6. Advisory curve speeds need a ball-bank or GPS study before issue.
7. Speeds in km/h. Chevron bands 20, 50, 70, 100 km/h.
8. Do not treat any DXF block, label or figure reference as a verified value. It is a cross-check until the printed code confirms it.
9. Deliver files only when asked. Confirm before sending.
10. Use `--allow-partial` only when the user explicitly skips a question. Record every skipped item.
11. Re-read the laptop input before every run and compare layer counts.
12. Junction coordinates from an old run are not reused without the re-read check.

---

## 15. Open items (revisit list, as of 28 Oct 2026)

1. Egyptian code: user to upload the Egyptian PDF into the project; then extract sign and marking rules (Egyptian numbering).
2. Egyptian sign numbers: add the other numbers from the signs details sheet (204, 305–307, 324–325, 405) to the block map labels; check names against the printed code.
3. T&I block map: confirm the 13 `check` rows.
4. SHC (KSA) signs: re-attach the five snaps; map the SHC signs; add the SHC code set as a separate rulebook.
5. Chevron and arrow placement: implement TI-614 to TI-619 and L13-1 to L13-6 placement in the DXF output.
6. Sign-indicator symbol placement: applied at 12 Wyte points (J01–J06, D01–D05, D07). Confirm the placement rule for future areas.
7. Speed hump block: rename `sprrd hump` to `speed hump` in the laptop template and map together (done in the scratch copy only).
8. Junctions sheet: replace the plain-word traffic management column with MUTCD (or Egyptian) sign codes after the rulebook check.
9. AADT: 18 Wyte links are missing AADT (skipped by the user). Provide values when available.
10. Roundabout inscribed radius: confirm 10 m for J01 (taken from the centreline ring).
11. Road classes: confirm the collector run (H2F451-1 to -5) and the major link N009-N010 (H2F465).
12. Real building location: TI - Buildings block (layer TI - BM) placement pending.
13. Guide signs: need a destinations list before they can be designed.
14. Engineer verification of the 54 unverified MUTCD rules (rules.yaml verify = false).
15. Dashboard (Signs_Dashboard.html): not yet built; depends on run.json and review JSON.

---

## 16. Reuse for another urban area (checklist)

1. Create the project folder (section 3) and the control workbook (section 4).
2. Re-read the input drawing (section 5.3). Find the centreline and kerb layers. Ask the user to confirm them.
3. Build the network and junction list (section 6). Number junctions (section 4.2).
4. Ask the user for: speed limit, road classes, junction controls and traffic management plan, dead-end types, sight restrictions, AADT, roundabout sizes, school zones, crossings, hazards.
5. Write the overrides (section 7.2) from the answers only.
6. Run the engine (section 9). Resolve every exit-2 question.
7. Check the block map (section 10.2) and the style pack (section 10.1).
8. Place the sign-indicator symbols and the schedule table if the user wants them (sections 10.3 and 10.4).
9. Report counts, Conditional items, Low-confidence devices, spacing moves and DRAFT status (section 9.4).
10. Deliver only when asked. Confirm before sending.
11. Handoff at the end of the chat. Offer `/explain-usage` after the major task and ask for confirmation.

---

## 17. Acceptance tests before the skill is used on a real project

1. `python tests/test_engine.py`: 6 of 6 pass.
2. `python tests/test_verification.py`: 74 of 74 pass. On Windows, set `$env:PYTHONUTF8=1` first.
3. The Wyte pilot (TL00) re-run gives the same junction list (J01–J06, D01–D05, D07) and the same counts as the last accepted run, unless the drawing has changed.
4. A new area: the engine stops with questions, not silent defaults, when data is missing.
5. Every output file name and sheet has DRAFT and the rulebook status.
6. No Egyptian field contains a MUTCD clause, and the reverse.
7. Block map: only approved rows are inserted. Check the inserted block count.
