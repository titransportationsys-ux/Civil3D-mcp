# MUTCD 11th Ed. rulebook – engineer review checklist

The values below were extracted from the public FHWA 11th Edition chapter PDFs (Dec 2023) through a
summarising web reader, not from a clean text copy. Check each item against the printed manual, tick it,
and then set `status: signed` in `rulebooks/mutcd_11e/code.yaml` (and on the dashboard's Codes page).

| # | File | What to check | Source |
|---|------|---------------|--------|
| 1 | tables/advance_placement.csv | Every value of Table 2C-3, Condition A and B (0-80 mph columns) | Ch. 2C, Table 2C-3 |
| 2 | tables/curve_devices.csv + rules.yaml CURVE rules | Table 2C-4 Chart A (roadway type / AADT >= 1,000 test) and Chart B device thresholds (5/10/15/20 mph) | 2C.06, Table 2C-4 |
| 3 | tables/chevron_spacing.csv | Table 2C-5 spacing by advisory speed / radius | 2C.08, Table 2C-5 |
| 4 | tables/mounting.csv | 5 ft rural / 7 ft urban heights; 12 ft from edge of traveled way; urban offset from curb (engine uses 2 ft) | 2A.15, 2A.16 |
| 5 | devices.csv | Sign sizes for every code (rows marked "assumed" need the real table value; S1-1 from Chapter 7B) | Tables 2B-1, 2C-1, 7B-1 |
| 6 | rules.yaml STOP/YIELD | Placement near side right; optional left sign for 2+ lanes; ALL-WAY plaque shall | 2B.04, 2B.18 |
| 7 | rules.yaml Stop/Yield/Signal Ahead | Standard when control not visible for sufficient distance | 2C.35 |
| 8 | rules.yaml Speed limit | R2-1 at change points (shall), beyond major intersections (should); W3-5 threshold 10 mph | 2B.21, 2C.40 |
| 9 | rules.yaml ONE WAY / DO NOT ENTER | Provision level and exact sections (2B.46-2B.49) | 2B.46-2B.49 |
| 10 | rules.yaml Roundabout / Circular Intersection | Section numbers and provision level | 2B, 2C |
| 11 | rules.yaml School | School Advance Warning assembly provision and section | Chapter 7B |
| 12 | rules.yaml markings | Centre line (3B.02 thresholds 6,000 / 4,000 / 3,000 ADT), edge line (3B.10), lane lines, stop line 4-30 ft, crosswalks (3C.02), lane-reduction taper (3B.12) | Part 3 |
| 13 | tables/passing_sight.csv | Table 3B-1 (used for the no-passing study item) | Table 3B-1 |
| 14 | engine/triggers.py | Advisory speed method: f = 0.21 / 0.18 / 0.15 for <25 / 25-30 / >=35 mph | FHWA advisory speed procedure |

## Confirmed from T&I's copy of the manual (30 Sep 2026)

| Item | Source supplied by T&I | Result in the rulebook |
|------|------------------------|------------------------|
| W13-1P Advisory Speed plaque | Table 2C-6 (Use of Advisory Speed Plaque) | Own class by differential: 10 km/h Optional, 20 Recommended, 30+ Mandatory |
| Speed units | T&I instruction: "convert mph to kph, as in AASHTO" | All speed conditions in km/h, 10 km/h steps; advisory floored to 10 km/h; taper WS/1.6 or WS^2/155 at 70 km/h |
| ONE WAY R6-1/R6-2 | 2B.49 full text | Mandatory at roads/alleys meeting a one-way; near-right + far-left (09); T far side (11); signal note (10); duplicate signs fixed. Divided highways (03-05) not automated |
| W11-2 Pedestrian Crossing | 2C.55 two Option paragraphs | Advance W11-2 Optional; W11-2 + W16-7P at the crosswalk Optional only with Yield Here To Pedestrians signs (yield_here_signs) |
| Centre line | 3B.02 full text | Added 3+ lanes (shall), under 16 ft = Conditional (judgment), Optional only 16 ft+ |
| Edge line | 3B.10 full text | Already matched; text recorded, tests added |
| Chevron spacing | Table "2C-6" Typical Spacing of Chevron Alignment Signs | Values matched; km/h bands 20/50/70/100 added |

Still open: row 14 (advisory speed friction values), rows 1, 2, 4, 5 (tables not yet confirmed from the manual),
and the numbering of the two pages both labelled Table 2C-6. Assumptions to confirm: advance W11-2 distance
(Table 2C-3 Cond. B 0 mph), W16-7P class, 25 km/h differential treated as the 10 mph row.

## Verified against T&I's MUTCD 11th Edition PDF (30 Sep 2026)

Source: `MUTCD 11thedition.pdf` (1,161 pages) in T&I's Codes for Claude folder. Tables parsed from the PDF text and compared field by field.

| Item | Result |
|------|--------|
| Sign sizes and names, Tables 2B-1, 2C-1, 7B-1 (27 signs + W16-9P) | All match. S1-1: removed an expressway size (Table 7B-1 has no such column) |
| Table 2C-3 advance placement (14 speeds, Conditions A and B) | All match |
| Table 2C-4 Charts A and B | Match |
| Table 2C-5 chevron spacing | Match. In the 11th Ed. chevron spacing is Table 2C-5; the screenshot labelled 2C-6 was the 2009 numbering |
| Table 2C-6 Advisory Speed plaque | Match (2C.59-03 Standard) |
| Mounting 2A.15 / lateral offset 2A.16 | Match (5 ft rural, 7 ft urban, 12 ft; urban 2 ft is the T&I default, code minimum 1 ft per 2A.16-10) |
| Turn vs Curve, 2C.07-02 | 30 mph advisory = 50 km/h threshold in the engine: match |

Rule changes from the PDF text:
- W16-7P below a post-mounted W11-2 at the crossing: Standard (2C.55-04), was inheriting Optional.
- Advance W11-2: AHEAD (W16-9P) plaque added as Guidance (2C.55-03).
- W11-2 at crosswalk: cites 2C.55-08 and 2B.19-09 (same text in both); 2B.19-10 noted.
- W13-1P: 2C.59-05 (Standard) noted, advisory speed must come from an engineering study.
- W3-5 legend: the 11th Ed. W3-5 is a symbol sign (arrow over a speed limit panel).

Sign pictures: `rulebooks/mutcd_11e/symbols/<code>.png`, cropped from the manual figures (2B-1, 2B-3, 2B-10, 2B-13, 2C-1, 2C-8, 2C-10, 2C-11, 2C-15, 2C-16, 7B-1); shown in the Signs sheet, a Sign catalog sheet and the report.

Still open: advisory speed friction values (FHWA-SA-11-22, not in the MUTCD); delineator spacing (Chapter 3G) not checked.
