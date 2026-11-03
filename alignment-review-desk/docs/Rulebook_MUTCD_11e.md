# Rule book: Manual on Uniform Traffic Control Devices, 11th Edition

T&I Transportation Systems, road signing skill. Generated 12 Oct 2026 from `rulebooks/mutcd_11e/`. Rulebook status: **extracting** (results are DRAFT until a T&I engineer signs it off).

## 1. How to read this rule book

Every device the skill places comes from one rule below. A rule fires on a *trigger* found in the road network, checks its *conditions*, and gets a class from the MUTCD wording:

| MUTCD wording | Class in the skill |
|---|---|
| Standard ("shall") | Mandatory |
| Guidance ("should") | Recommended |
| Option ("may") | Optional |
| Study (engineering study decides) | Conditional |

Speed conditions are in km/h, converted AASHTO-style (a 5 mph step = 10 km/h; 30 mph = 50 km/h; 45 mph = 70 km/h). Where a rule lists several conditions, the first one that is true sets the class.

Condition names: `class` = road class (freeway, expressway, arterial, collector, local); `speed_kmh` = posted speed on the approach (km/h); `aadt` = traffic volume (veh/day); `urban` = urban street (true/false); `lanes` = lanes per direction; `lanes_total` = total lanes; `width_ft` = traveled-way width (ft); `oneway` = one-way link; `divided` = divided road; `diff_kmh` = posted speed minus curve advisory speed (km/h); `advisory_kmh` = advisory speed set for the point (km/h); `chart_a` = Table 2C-4 Chart A result (Required / Recommended / Optional); `reduction_kmh` = drop in speed limit at a change point (km/h); `suppress_sign` = second curve of a reverse pair; `school_zone` = school zone designated by statute; `tracks` = number of tracks at a grade crossing; `signals_gates` = grade crossing has flashing-light signals or gates; `clear_width_m` = roadway horizontal clearance on the structure (m); `structure` = bridge / culvert / underpass; `heavy_commercial` = high share of commercial vehicles; `clearance_m` = vertical clearance (m); `statutory_height_m` = statutory maximum vehicle height (m); `grade_pct` = downgrade (%); `length_m` = downgrade length (m); `bus_not_visible` = stopped school bus not visible for adequate distance; `emergency_signal` = emergency-vehicle signal present; `role` = major or entering roadway; `equal` = both roadways of the same class; `to_two_lane` = section after is two-lane two-way; `lane_width_m` = lane width (m); `curve_sign` = curve sign chosen from geometry; `yield_here_signs` = Yield Here To Pedestrians signs installed; `sight_restricted` = control not visible for sufficient distance; `degree` = number of legs at the node.

## 2. Rules by trigger

### All-way STOP approach (`INT-STOP-AWAY`)

**R1-1 Stop** · rule `MUTCD.2B.04.ALLWAY`

![R1-1](symbols/R1-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_stop_line, side = right
- Plaque on the same post: R1-3P (same class as the sign)
- MUTCD: 2B.04-04 (R1-3P shall be mounted below each STOP sign); 2B.18-01
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Minor-road STOP approach (`INT-STOP-2WAY`)

**R1-1 Stop** · rule `MUTCD.2B.18.STOP`

![R1-1](symbols/R1-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_stop_line, side = right
- MUTCD: 2B.18-01/02 (near side, right-hand side, as close as practicable)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**R1-1 Stop** · rule `MUTCD.2B.18.STOP-LEFT` · also fires on INT-STOP-AWAY

![R1-1](symbols/R1-1.png)

- Default class: **Optional** (Option)
- Applies when: `lanes >= 2 OR oneway`
- Placement: kind = at_stop_line, side = left
- MUTCD: 2B.18-17 (additional STOP sign on left for 2+ approach lanes)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**SL Stop line** · rule `MUTCD.3B.19.STOPLINE` · also fires on INT-STOP-AWAY, INT-SIGNAL

- Default class: **Recommended** (Guidance)
- Placement: kind = stop_line
- MUTCD: 3B.19 (4-30 ft from edge of intersecting traveled way; 12-24 in wide)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W3-1 Stop Ahead** · rule `MUTCD.2C.35.STOPAHEAD` · also fires on INT-STOP-AWAY

![W3-1](symbols/W3-1.png)

- Default class: **Conditional** (Study)
- If `sight_restricted is True` → **Mandatory** (Standard)
- If `sight_restricted is False` → **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = stop_line, side = right
- Study that decides it: Is the STOP sign visible for sufficient distance (Table 2C-3, Condition B 0 mph)? If not, W3-1 is mandatory.
- MUTCD: 2C.35-01 (shall be installed where the primary device is not visible for a sufficient distance)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Signalised approach (`INT-SIGNAL`)

**W3-3 Signal Ahead** · rule `MUTCD.2C.35.SIGNALAHEAD`

![W3-3](symbols/W3-3.png)

- Default class: **Conditional** (Study)
- If `sight_restricted is True` → **Mandatory** (Standard)
- If `sight_restricted is False` → **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = stop_line, side = right
- Study that decides it: Are the signal faces visible for sufficient distance? If not, W3-3 is mandatory.
- MUTCD: 2C.35-01
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**CW Crosswalk** · rule `MUTCD.3C.02.CROSSWALK-SIGNAL`

- Default class: **Recommended** (Guidance)
- Placement: kind = crosswalk
- MUTCD: 3C.02-01 (crosswalk markings should be installed at signalized locations)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### YIELD approach (`INT-YIELD`)

**R1-2 Yield** · rule `MUTCD.2B.10.YIELD`

![R1-2](symbols/R1-2.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_stop_line, side = right
- MUTCD: 2B.18-01/02
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**YL Yield line (shark teeth)** · rule `MUTCD.3B.19.YIELDLINE` · also fires on INT-ROUNDABOUT

- Default class: **Optional** (Option)
- Placement: kind = stop_line
- MUTCD: 3B.19-08/10 (yield line only with a YIELD sign)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W3-2 Yield Ahead** · rule `MUTCD.2C.35.YIELDAHEAD`

![W3-2](symbols/W3-2.png)

- Default class: **Conditional** (Study)
- If `sight_restricted is True` → **Mandatory** (Standard)
- If `sight_restricted is False` → **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = stop_line, side = right
- Study that decides it: Is the YIELD sign visible for sufficient distance? If not, W3-2 is mandatory.
- MUTCD: 2C.35-01
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Roundabout entry (`INT-ROUNDABOUT`)

**R1-2 Yield** · rule `MUTCD.2B.ROUNDABOUT.YIELD`

![R1-2](symbols/R1-2.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_stop_line, side = right
- MUTCD: 2B.10-05 (YIELD shall be used at the entrance to a roundabout)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W2-6 Circular Intersection** · rule `MUTCD.2C.ROUNDABOUT.W2-6`

![W2-6](symbols/W2-6.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = stop_line, side = right
- MUTCD: 2C.41-02 (Circular Intersection sign may be installed)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Major road at an uncontrolled junction (`INT-UNCONTROLLED-MAJOR`)

**W2-1 / W2-2 / W2-4 Cross Road / Side Road / T-Intersection (chosen from the junction layout)** · rule `MUTCD.2C.41.INTWARN`

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = node, side = right
- MUTCD: 2C.41-01 (Cross Road / Side Road / T-Intersection signs may be used)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Horizontal curve (`CURVE`)

**W1-1 / W1-2 / W1-3 / W1-4 Turn / Curve / Reverse Turn / Reverse Curve (chosen from geometry)** · rule `MUTCD.2C.06.CURVE-SIGN`

- Default class: **Recommended** (Guidance)
- Applies when: `diff_kmh >= 10 AND NOT suppress_sign`
- If `diff_kmh < 20` → **Optional** (Option)
- If `chart_a == 'Required'` → **Mandatory** (Standard)
- If `chart_a == 'Recommended'` → **Recommended** (Guidance)
- If `chart_a == 'Optional'` → **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = t['advisory_mph'], from = curve_start, side = right
- Plaque on the same post: **W13-1P**, default Optional; if `diff_kmh >= 30` → Mandatory; if `diff_kmh >= 20` → Recommended (2C.59-03 (Standard) and Table 2C-6 (differential 5 mph / 10 km/h Optional, 10 mph / 20 km/h Recommended, 15 mph / 30 km/h or more Required). 2C.59-05 (Standard): not installed until the advisory speed is set by an engineering study. Verified from the MUTCD 11th Ed. PDF, manual p.196)
- MUTCD: 2C.06, Table 2C-4 Chart A (need by roadway type and AADT) and Chart B (devices); sign choice 2C.07-02/03. Advisory plaque per Table 2C-6
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W1-8 Chevron Alignment** · rule `MUTCD.2C.08.CHEVRONS`

![W1-8](symbols/W1-8.png)

- Default class: **Recommended** (Guidance)
- Applies when: `diff_kmh >= 40`
- If `chart_a == 'Required'` → **Mandatory** (Standard)
- If `chart_a == 'Optional'` → **Optional** (Option)
- Placement: kind = along_curve, side = outside
- MUTCD: 2C.08, Table 2C-4 Chart B (20 mph / 40 km/h or more: chevrons), Table 2C-5 spacing
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**DELINEATOR Delineator (single yellow retroreflector)** · rule `MUTCD.2C.06.DELINEATORS`

- Default class: **Recommended** (Guidance)
- Applies when: `30 <= diff_kmh < 40`
- If `chart_a == 'Required'` → **Mandatory** (Standard)
- If `chart_a == 'Optional'` → **Optional** (Option)
- Placement: kind = along_curve, side = outside, spacing_scale = 0.5
- MUTCD: Table 2C-4 Chart B (15 mph / 30 km/h: delineators); Chapter 3G delineator spacing
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W1-6 One-Direction Large Arrow** · rule `MUTCD.2C.10.LARGE-ARROW`

![W1-6](symbols/W1-6.png)

- Default class: **Optional** (Option)
- Applies when: `curve_sign in ('W1-1', 'W1-3') AND NOT suppress_sign`
- Placement: kind = curve_outside
- MUTCD: 2C.10-02 (Option): a One-Direction Large Arrow (W1-6) sign may be used to supplement a Turn (W1-1) or Reverse Turn (W1-3) sign to emphasize the abrupt curvature. 2C.10-04 (Standard): if used, installed on the outside of the turn in line with and about at right angles to approaching traffic. 2C.10-05 (Standard): not where there is no alignment change. Manual p.159
- Clause wording checked against the manual text: yes

### Speed limit change point (`SPEED-ZONE`)

**R2-1 Speed Limit** · rule `MUTCD.2B.21.SPEED-CHANGE`

![R2-1](symbols/R2-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_point, side = right
- MUTCD: 2B.21-14 (at points of change from one speed limit to another)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W3-5 Reduced Speed Limit Ahead** · rule `MUTCD.2C.40.REDUCED-AHEAD`

![W3-5](symbols/W3-5.png)

- Default class: **Recommended** (Guidance)
- Applies when: `reduction_kmh >= 20`
- Placement: kind = advance, condition = B, advisory_mph = t['new_mph'], from = point, side = right
- MUTCD: 2C.40-01 (should be used where the limit is reduced by more than 10 mph; metric 20 km/h or more)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Site entry (gate, external road not drawn) (`BOUNDARY-ENTRY`)

**R2-1 Speed Limit** · rule `MUTCD.2B.21.SITE-ENTRY`

![R2-1](symbols/R2-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = downstream, distance_m = 15, side = right, legend = new_kmh
- MUTCD: 2B.21-14 (at points of change from one speed limit to another): posted limit at the site entry, just inside the gate
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Beyond a major intersection (`AFTER-MAJOR-INT`)

**R2-1 Speed Limit** · rule `MUTCD.2B.21.SPEED-REMIND`

![R2-1](symbols/R2-1.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = downstream, distance_m = 60, side = right
- MUTCD: 2B.21-17 (beyond major intersections)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Road meeting a one-way street (`ONE-WAY-CROSSING`)

**R6-1 One Way** · rule `MUTCD.2B.49.ONEWAY`

![R6-1](symbols/R6-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_node_facing_cross, side = both_far
- MUTCD: 2B.49 (text confirmed by T&I 30 Sep 2026). 01/02 shall: ONE WAY parallel to the one-way street at all alleys and roadways that intersect it. 09 unsignalised: near-right and far-left corners facing traffic entering or crossing. 10 signalised: near signal faces or as 09. 11 T-intersection with one-way top: near-right and far side facing the stem. 03/04 divided highways, 05 far-right option, 06 interchange omission, 12 roundabout island, 14 R6-6/R6-7: not automated
- Clause wording checked against the manual text: yes

### Exit end of a one-way street (`ONE-WAY-EXIT`)

**R5-1 Do Not Enter** · rule `MUTCD.2B.46.DONOTENTER`

![R5-1](symbols/R5-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_exit_end, side = both
- MUTCD: 2B.46 DO NOT ENTER where entry is prohibited
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Lane drop (`LANE-DROP`)

**W4-2 Lane Ends** · rule `MUTCD.2C.47.LANE-ENDS`

![W4-2](symbols/W4-2.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = A, from = point, side = right
- MUTCD: 2C.47 Lane Ends
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**LDRP Lane drop dotted line (wide)** · rule `MUTCD.3B.12.LANE-REDUCTION`

- Default class: **Mandatory** (Standard)
- Placement: kind = taper
- MUTCD: 3B.12 lane-reduction transition; taper L = WS/1.6 (>= 70 km/h) or WS^2/155 (< 70 km/h), metric form of WS / WS^2/60 at 45 mph, Guidance 08
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Mid-block crosswalk (`PED-XING-MIDBLOCK`)

**CW Crosswalk** · rule `MUTCD.3C.02.CROSSWALK-MIDBLOCK`

- Default class: **Mandatory** (Standard)
- Placement: kind = crosswalk
- MUTCD: 3C.02-05 (crosswalk markings shall be provided at legally established non-intersection crosswalks)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**W11-2 Pedestrian** · rule `MUTCD.2C.55.PED-ADVANCE`

![W11-2](symbols/W11-2.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = point, side = right
- Plaque on the same post: **W16-9P**, default Recommended (2C.55-03 (Guidance): if used in advance of a pedestrian crossing, W11-2 should be supplemented with an AHEAD (W16-9P) or XX FEET (W16-2P) plaque. Verified from the MUTCD 11th Ed. PDF, manual p.192)
- MUTCD: 2C.55-01 (Option): Non-Vehicular Warning signs may be used to alert road users in advance of locations where unexpected entries into the roadway might occur. Verified from the MUTCD 11th Ed. PDF, manual p.192. 2C.55-05 (Standard): not on an approach controlled by STOP or YIELD. Distance: Table 2C-3 Condition B, 0 mph column (engine assumption, potential stop)
- Clause wording checked against the manual text: yes

**W11-2 Pedestrian** · rule `MUTCD.2C.55.PED-AT-CROSSWALK`

![W11-2](symbols/W11-2.png)

- Default class: **Optional** (Option)
- Applies when: `yield_here_signs`
- Placement: kind = at_point, side = right
- Plaque on the same post: **W16-7P**, default Mandatory (2C.55-04 (Standard): a post-mounted W11-2 at the crossing point shall have a W16-7P plaque mounted below it (not used if the sign is overhead). Verified from the MUTCD 11th Ed. PDF, manual p.192)
- MUTCD: 2C.55-08 and 2B.19-09 (Option): W11-2 may be placed overhead or post-mounted with a W16-7P plaque at the crosswalk where Yield Here To (Stop Here For) Pedestrians signs have been installed in advance of the crosswalk. 2B.19-10 (Standard): the Yield Here To sign shall not be on the same post. Verified from the MUTCD 11th Ed. PDF, manual pp.81, 193. Needs yield_here_signs: true on the crosswalk
- Clause wording checked against the manual text: yes

### School (`SCHOOL`)

**S1-1 School** · rule `MUTCD.7B.SCHOOL-ADVANCE`

![S1-1](symbols/S1-1.png)

- Default class: **Conditional** (Study)
- If `school_zone is True` → **Mandatory** (Standard)
- Placement: kind = advance, condition = A, from = point, side = right
- Study that decides it: Is a school zone designated under State or local statute here? If yes, S1-1 is mandatory at the start of the zone (7B.02-04).
- MUTCD: 7B.02-04 (S1-1 shall identify the beginning of a designated school zone)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### Every road link (markings) (`MARK-LINK`)

**CL-DY Center line double solid yellow** · rule `MUTCD.3B.02.CENTERLINE`

- Default class: **Optional** (Option)
- Applies when: `NOT oneway AND NOT divided`
- If `lanes_total >= 3` → **Mandatory** (Standard)
- If `urban AND class in ('arterial','collector') AND width_ft >= 20 AND aadt >= 6000` → **Mandatory** (Standard)
- If `urban AND class in ('arterial','collector') AND width_ft >= 20 AND aadt >= 4000` → **Recommended** (Guidance)
- If `(NOT urban) AND class in ('arterial','collector') AND width_ft >= 18 AND aadt >= 3000` → **Recommended** (Guidance)
- If `width_ft < 16` → **Conditional** (Study)
- Placement: kind = link_line, offset = center
- Study that decides it: Traveled way under 16 ft (4.9 m): decide by engineering judgment (edge encroachment, parked vehicles, encroachment into the opposing lane), 3B.02-03
- MUTCD: 3B.02 (text confirmed by T&I 30 Sep 2026). 01 shall: urban arterial/collector, 20 ft+, ADT 6000+; any 3+ lane undivided two-way road. 02 should: urban arterial/collector 20 ft+ ADT 4000+; rural arterial/collector 18 ft+ ADT 3000+; elsewhere where an engineering study shows a need. 03 under 16 ft engineering judgment. 04 may: other two-way 16 ft+. 05 ADT may be an engineering estimate
- Clause wording checked against the manual text: yes

**EL-SW Edge line solid white** · rule `MUTCD.3B.10.EDGELINE`

- Default class: **Optional** (Option)
- If `class in ('freeway','expressway')` → **Mandatory** (Standard)
- If `(NOT urban) AND class == 'arterial' AND width_ft >= 20 AND aadt >= 6000` → **Mandatory** (Standard)
- If `(NOT urban) AND class in ('arterial','collector') AND width_ft >= 20 AND aadt >= 3000` → **Recommended** (Guidance)
- Placement: kind = link_line, offset = right_edge
- MUTCD: 3B.10 (text confirmed by T&I 30 Sep 2026). 01 shall: freeways, expressways, rural arterials 20 ft+ ADT 6000+. 02 should: rural arterials/collectors 20 ft+ ADT 3000+; elsewhere where an engineering study shows a need. 03 should not where a study or judgment shows it decreases safety. 04 may: with or without centre line. 05 may be excluded by judgment where edges are delineated by curbs, parking or other markings. 06 outside edge of a marked bike lane may be omitted. 07 may be used to keep traffic off weak shoulders
- Clause wording checked against the manual text: yes

**LL-BW Lane line broken white** · rule `MUTCD.3B.04.LANELINE`

- Default class: **Recommended** (Guidance)
- Applies when: `lanes >= 2`
- If `class in ('freeway',)` → **Mandatory** (Standard)
- Placement: kind = link_line, offset = lane_lines
- MUTCD: 3B.06-02 (shall on freeways and Interstates); 3B.06-03 (should on 2+ adjacent lanes same direction)
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

**NO-PASSING-STUDY No-passing zone survey (study item)** · rule `MUTCD.3B.NOPASS`

- Default class: **Conditional** (Study)
- Applies when: `(NOT urban) AND (NOT oneway) AND (NOT divided) AND lanes == 1`
- Placement: kind = link_note
- Study that decides it: Passing sight distance survey against Table 3B-1 to locate no-passing zones.
- MUTCD: 3B.02/3B.03 no-passing zones, Table 3B-1
- Clause wording checked against the manual text: not yet (sizes and tables it uses are verified)

### SIGN-REQUEST (`SIGN-REQUEST`)

**any code Any MUTCD sign placed by the designer (`type: sign`, `code`)** · rule `MUTCD.CATALOG.SIGN-REQUEST`

- Default class: from the sign's own MUTCD paragraph (sign catalog default class)
- Placement: kind = at_point, side = right
- MUTCD: {'Designer-placed. Class basis: MUTCD ' + (t['request_basis'] or 'no use paragraph names this sign (Optional)') + '; full provisions in the rule book'}
- Clause wording checked against the manual text: yes

### Hazard point `type: rail_crossing`: Highway-rail grade crossing (point on the track centre) (`HAZ-RAIL_CROSSING`)

**W10-1 Grade Crossing Advance Warning** · rule `MUTCD.8B.06.W10-1`

![W10-1](symbols/W10-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 8B.06-01 (Standard): a W10-1 sign shall be used on each highway in advance of every grade crossing, except A. approach from a parallel highway < 100 ft away with W10-2/3/4 used; B. low-volume low-speed roads over infrequently used tracks with flagging; C. business areas with active crossing control; D. no effective display possible; E. LRT crossings without Crossbucks. 8B.06-02 (Standard): placed per 2C.04 and Table 2C-3. Manual p.1001. Remove it by hand where an exception applies
- Clause wording checked against the manual text: yes

**W10-1 Grade Crossing Advance Warning** · rule `MUTCD.8B.06.W10-1-LEFT`

![W10-1](symbols/W10-1.png)

- Default class: **Optional** (Option)
- Applies when: `oneway OR divided`
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = left
- MUTCD: 8B.06-04 (Option): on divided highways and one-way streets, an additional W10-1 sign may be installed on the left-hand side of the roadway. Manual p.1001
- Clause wording checked against the manual text: yes

**R15-1 Grade Crossing (Crossbuck)** · rule `MUTCD.8B.03.CROSSBUCK`

![R15-1](symbols/R15-1.png)

- Default class: **Mandatory** (Standard)
- Placement: kind = at_point, side = right, back_add_m = 5.4, confidence = Medium, note = placed 15 ft (4.6 m) before the nearest rail (stopping point, 8B.03-16) plus half the track gauge; railroad clearance per 8B.03-10; centre about 9 ft (2.7 m) high (8B.03-11)
- Plaque on the same post: **R15-2P**, default Mandatory (8B.03-06 (Standard): if there are two or more tracks, the number of tracks shall be indicated on a supplemental Number of Tracks (R15-2P) plaque mounted below the Crossbuck sign. Manual p.993)
- MUTCD: 8B.03-03 (Standard): as a minimum, one Crossbuck sign shall be used on each highway approach to every highway-rail grade crossing. 8B.03-07 (Standard): installed on the right-hand side of the highway on each approach. Manual p.993
- Clause wording checked against the manual text: yes

**RXR Grade crossing X and RR symbol with transverse lines** · rule `MUTCD.8C.02.RXR`

- Default class: **Optional** (Option)
- If `signals_gates OR speed_kmh >= 60` → **Mandatory** (Standard)
- Placement: kind = lane_symbol, condition = B, advisory_mph = 0, note = a portion of the X opposite the W10-1 sign (8C.02-08); no-passing marking on two-lane two-way roads with centre lines (8C.02-01)
- MUTCD: 8C.02-02 (Standard): grade crossing pavement markings shall be placed in each approach lane on all paved approaches where signals or automatic gates are located, and at all other grade crossings where the posted or statutory speed is 40 mph (60 km/h) or higher. 8C.02-03/04: not required below 40 mph or in urban areas if the Diagnostic Team finds other devices suitable. Manual p.1009
- Clause wording checked against the manual text: yes

### Hazard point `type: narrow_structure`: Bridge, culvert or underpass narrower than the approach (`HAZ-NARROW_STRUCTURE`)

**W5-3 / W5-3a One Lane Bridge / One Lane Underpass (chosen from the point data)** · rule `MUTCD.2C.19.ONE-LANE-STRUCTURE`

- Default class: **Recommended** (Guidance)
- Applies when: `NOT oneway AND (clear_width_m < 4.88 OR (clear_width_m < 5.49 AND heavy_commercial))`
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.19-01 (Guidance): a ONE LANE BRIDGE (W5-3) sign should be used on two-way roadways in advance of any bridge or culvert with a roadway horizontal clearance A. less than 16 ft (4.88 m), B. less than 18 ft (5.49 m) when commercial vehicles are a high proportion of traffic, or C. 18 ft or less where approach sight distance is below Table 2C-3 Condition A (check C by hand). 2C.19-02: W5-3a for an underpass. 2C.19-04 (Option): may be omitted on low-volume rural roads with adequate sight distance. Manual p.170
- Clause wording checked against the manual text: yes

**W5-2 / W5-2a Narrow Bridge / Narrow Underpass (chosen from the point data)** · rule `MUTCD.2C.18.NARROW-STRUCTURE`

- Default class: **Recommended** (Guidance)
- Applies when: `NOT (NOT oneway AND (clear_width_m < 4.88 OR (clear_width_m < 5.49 AND heavy_commercial))) AND ((NOT oneway AND clear_width_m <= 5.49) OR clear_width_m < lanes_total * lane_width_m)`
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.18-01 (Guidance): a NARROW BRIDGE (W5-2) sign should be used in advance of any bridge or culvert with a two-way roadway horizontal clearance of 16 to 18 ft (4.88-5.49 m), or a clearance less than the width of the approach travel lanes; W5-2a for an underpass. 2C.18-02: add object markers, delineators and/or markings. 2C.18-04 (Option): may be omitted on low-volume rural roads with adequate sight distance. Manual p.170
- Clause wording checked against the manual text: yes

### Hazard point `type: road_narrows`: Abrupt pavement narrowing where opposing vehicles cannot pass together (`HAZ-ROAD_NARROWS`)

**W5-1 Road Narrows** · rule `MUTCD.2C.17.ROAD-NARROWS`

![W5-1](symbols/W5-1.png)

- Default class: **Recommended** (Guidance)
- If `class == 'local' AND speed_kmh <= 50` → **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.17-01 (Guidance): a ROAD NARROWS (W5-1) sign should be used in advance of a transition on two-lane roads where the pavement width is reduced abruptly so that opposing vehicles cannot travel through the narrow portion together. 2C.17-02 (Option): may be omitted on low-volume local streets with speed limits of 30 mph (50 km/h) or less. Manual pp.169-170
- Clause wording checked against the manual text: yes

### Hazard point `type: low_clearance`: Structure with low vertical clearance (`HAZ-LOW_CLEARANCE`)

**W12-2 Low Clearance Advance** · rule `MUTCD.2C.25.LOW-CLEARANCE`

![W12-2](symbols/W12-2.png)

- Default class: **Mandatory** (Standard)
- Applies when: `clearance_m < 4.42 OR (statutory_height_m AND clearance_m < statutory_height_m + 0.305)`
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = legend = measured clearance rounded down (2C.25-02); reduce up to 3 in (75 mm) where frost action occurs; add a W12-2 with distance plaque at the last detour point (2C.25-04)
- MUTCD: 2C.25-01 (Standard): the W12-2 sign shall be used to warn of vertical clearances less than 14 ft 6 in (4.42 m), or less than 12 in above the statutory maximum vehicle height, whichever is greater (set statutory_height_m on the point). 2C.25-02 (Guidance): display the actual clearance to the nearest inch not exceeding it. Manual p.172
- Clause wording checked against the manual text: yes

### Hazard point `type: speed_hump`: Speed hump or speed table (`HAZ-SPEED_HUMP`)

**W17-1 Speed Hump** · rule `MUTCD.2C.27.SPEED-HUMP`

![W17-1](symbols/W17-1.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W13-1P**, default Recommended (2C.27-02 (Guidance): if used, the SPEED HUMP sign should be supplemented by an Advisory Speed plaque. 2C.27-03 (Option): in a series, the plaque may be left off all but the first sign. Manual p.173)
- MUTCD: 2C.27-01 (Guidance): the SPEED HUMP (W17-1) sign should be used in advance of a vertical deflection in the roadway designed to limit the speed of traffic. 2C.27-04 (Option): legend SPEED BUMP may be used. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: bump`: Sharp rise in the road profile (`HAZ-BUMP`)

**W8-1 Bump or Dip** · rule `MUTCD.2C.26.BUMP`

![W8-1](symbols/W8-1.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W13-1P**, default Optional (2C.26-02 (Option): may be supplemented with an Advisory Speed plaque. Manual p.173)
- MUTCD: 2C.26-01 (Guidance): BUMP (W8-1) and DIP (W8-2) signs should be used in advance of a sharp rise or depression in the profile of the road. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: dip`: Sharp depression in the road profile (`HAZ-DIP`)

**W8-2 Bump or Dip** · rule `MUTCD.2C.26.DIP`

![W8-2](symbols/W8-2.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W13-1P**, default Optional (2C.26-02 (Option): may be supplemented with an Advisory Speed plaque. Manual p.173)
- MUTCD: 2C.26-01 (Guidance): BUMP (W8-1) and DIP (W8-2) signs should be used in advance of a sharp rise or depression in the profile of the road. 2C.26-03 (Guidance): the DIP sign should not be used for a short depression that might momentarily hide a vehicle; treat that as a no-passing zone (2C.26-04). Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: pavement_ends`: Paved surface changes to gravel or earth (point at the change) (`HAZ-PAVEMENT_ENDS`)

**W8-3 Pavement Ends** · rule `MUTCD.2C.28.PAVEMENT-ENDS`

![W8-3](symbols/W8-3.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W13-1P**, default Optional (2C.28-02 (Option): an Advisory Speed plaque may be used when the change requires a reduced speed. Manual p.173)
- MUTCD: 2C.28-01 (Guidance): a PAVEMENT ENDS (W8-3) sign should be used where a paved surface changes to either a gravel treated surface or an earth road surface. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: downgrade`: Start of a steep downgrade (point at the top) (`HAZ-DOWNGRADE`)

**W7-1 Hill** · rule `MUTCD.2C.14.HILL`

![W7-1](symbols/W7-1.png)

- Default class: **Conditional** (Study)
- If `(grade_pct >= 5 AND length_m > 914) OR (grade_pct >= 6 AND length_m > 610) OR (grade_pct >= 7 AND length_m > 305) OR (grade_pct >= 8 AND length_m > 229) OR (grade_pct >= 9 AND length_m > 152)` → **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W7-3P**, default Conditional (2C.14-02 (Guidance): the Hill sign and grade (W7-3P) plaque used in combination, or W7-1a alone. Manual p.167)
- Study that decides it: Do the grade, length, curvature or crash history require special precautions (2C.14-01, 2C.14-03)? If yes, W7-1 with W7-3P is Recommended.
- MUTCD: 2C.14-02 (Guidance): the Hill sign with W7-3P plaque should be installed in advance of downgrades of A. 5% longer than 3,000 ft (914 m), B. 6% > 2,000 ft (610 m), C. 7% > 1,000 ft (305 m), D. 8% > 750 ft (229 m), or E. 9% > 500 ft (152 m); 2C.14-03 also for steeper grades or where crashes show a need. 2C.14-04: repeat with W7-3aP/W7-3bP about every mile on long grades. Manual p.167
- Clause wording checked against the manual text: yes

### Hazard point `type: school_bus_stop`: School bus stop (`HAZ-SCHOOL_BUS_STOP`)

**S3-1 School Bus Stop Ahead** · rule `MUTCD.7B.04.SCHOOL-BUS-STOP`

![S3-1](symbols/S3-1.png)

- Default class: **Conditional** (Study)
- If `bus_not_visible is True` → **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = point, side = right
- Study that decides it: Is a stopped school bus not visible to road users for an adequate distance, with no chance to relocate the stop (7B.04-01)?
- MUTCD: 7B.04-01 (Guidance): the School Bus Stop Ahead (S3-1) sign should be installed in advance of locations where a stopped school bus is not visible to road users for an adequate distance and there is no opportunity to relocate the stop. Manual p.978
- Clause wording checked against the manual text: yes

### Hazard point `type: truck_crossing`: Truck entrance or crossing (`HAZ-TRUCK_CROSSING`)

**W11-10 Truck** · rule `MUTCD.2C.54.TRUCK`

![W11-10](symbols/W11-10.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W16-9P**, default Optional (2C.54-07 (Option): AHEAD / XX FEET plaques may be mounted below. Manual p.191)
- MUTCD: 2C.54-01 (Option): Vehicular Traffic Warning signs may be used to alert road users to locations where unexpected entries into the roadway by trucks, bicycles, farm vehicles, emergency vehicles or other vehicles might occur. 2C.54-03 (Guidance): only where sight distance is restricted or the entry is unexpected. 2C.54-10 (Standard): not on an approach controlled by STOP or YIELD. Manual pp.191-192
- Clause wording checked against the manual text: yes

### Hazard point `type: farm_vehicles`: Farm vehicle entrance or crossing (`HAZ-FARM_VEHICLES`)

**W11-5 Farm Vehicle** · rule `MUTCD.2C.54.FARM`

![W11-5](symbols/W11-5.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W16-9P**, default Optional (2C.54-07 (Option): AHEAD / XX FEET plaques may be mounted below. Manual p.191)
- MUTCD: 2C.54-01 (Option): Vehicular Traffic Warning signs may be used to alert road users to locations where unexpected entries into the roadway by trucks, bicycles, farm vehicles, emergency vehicles or other vehicles might occur. 2C.54-03 (Guidance): only where sight distance is restricted or the entry is unexpected. 2C.54-10 (Standard): not on an approach controlled by STOP or YIELD. Manual pp.191-192
- Clause wording checked against the manual text: yes

### Hazard point `type: bicycle_crossing`: Unexpected bicycle entry or crossing (`HAZ-BICYCLE_CROSSING`)

**W11-1 Bicycle** · rule `MUTCD.2C.54.BICYCLE`

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W16-9P**, default Optional (2C.54-07 (Option): AHEAD / XX FEET plaques may be mounted below. Manual p.191)
- MUTCD: 2C.54-01 (Option): Vehicular Traffic Warning signs may be used to alert road users to locations where unexpected entries into the roadway by trucks, bicycles, farm vehicles, emergency vehicles or other vehicles might occur. 2C.54-03 (Guidance): only where sight distance is restricted or the entry is unexpected. 2C.54-10 (Standard): not on an approach controlled by STOP or YIELD. Manual pp.191-192
- Clause wording checked against the manual text: yes

### Hazard point `type: emergency_station`: Emergency vehicle station (fire, ambulance) (`HAZ-EMERGENCY_STATION`)

**W11-8 Emergency Vehicle** · rule `MUTCD.2C.54.EMERGENCY`

![W11-8](symbols/W11-8.png)

- Default class: **Optional** (Option)
- If `emergency_signal is True` → **Mandatory** (Standard)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- Plaque on the same post: **W11-12P**, default Mandatory (2C.54-14 (Standard): the W11-8 sign with the EMERGENCY SIGNAL AHEAD (W11-12P) plaque shall be placed in advance of all emergency-vehicle traffic control signals. Manual p.192)
- MUTCD: 2C.54-14 (Standard): W11-8 with W11-12P shall be placed in advance of all emergency-vehicle traffic control signals. 2C.54-15 (Option): W11-8 may be used in advance of an emergency-vehicle station with no such signal. Manual p.192
- Clause wording checked against the manual text: yes

### Hazard point `type: deer_crossing`: Deer or wild animal crossing area (`HAZ-DEER_CROSSING`)

**W11-3 Deer** · rule `MUTCD.2C.55.DEER`

![W11-3](symbols/W11-3.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.55-01 (Option): Non-Vehicular Warning signs may be used to alert road users in advance of locations where unexpected entries into the roadway might occur. 2C.55-05 (Standard): not on an approach controlled by STOP or YIELD. Manual p.192
- Clause wording checked against the manual text: yes

### Hazard point `type: cattle_crossing`: Cattle or livestock crossing (`HAZ-CATTLE_CROSSING`)

**W11-4 Cattle** · rule `MUTCD.2C.55.CATTLE`

![W11-4](symbols/W11-4.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.55-01 (Option): Non-Vehicular Warning signs may be used to alert road users in advance of locations where unexpected entries into the roadway might occur. 2C.55-05 (Standard): not on an approach controlled by STOP or YIELD. Manual p.192
- Clause wording checked against the manual text: yes

### Hazard point `type: equestrian_crossing`: Horse riders crossing (`HAZ-EQUESTRIAN_CROSSING`)

**W11-7 Equestrian** · rule `MUTCD.2C.55.EQUESTRIAN`

![W11-7](symbols/W11-7.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.55-01 (Option): Non-Vehicular Warning signs may be used to alert road users in advance of locations where unexpected entries into the roadway might occur. 2C.55-05 (Standard): not on an approach controlled by STOP or YIELD. Manual p.192
- Clause wording checked against the manual text: yes

### Hazard point `type: playground`: Designated children's playground next to the road (`HAZ-PLAYGROUND`)

**W15-1 Playground** · rule `MUTCD.2C.56.PLAYGROUND`

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.56-01 (Option): the Playground (W15-1) sign may be used to give advance warning of a designated children's playground next to the road. 2C.56-03 (Guidance): if access needs a road crossing, consider crosswalk markings and a Non-Vehicular Warning sign. Manual p.194
- Clause wording checked against the manual text: yes

### Hazard point `type: slippery`: Start of an unexpectedly slippery section (`HAZ-SLIPPERY`)

**W8-5 Slippery When Wet** · rule `MUTCD.2C.30.SLIPPERY`

![W8-5](symbols/W8-5.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals along the affected section (2C.30-07)
- MUTCD: 2C.30-01 to 06 (Option): Surface Condition signs (W8-5 Slippery When Wet, W8-7 Loose Gravel, W8-8 Rough Road, W8-13 Bridge Ices Before Road, W8-14 Fallen Rocks) may be used to warn of the condition. 2C.30-07 (Guidance): when used, place in advance of the affected section (Table 2C-3) and repeat at intervals where the condition exists. Manual p.175
- Clause wording checked against the manual text: yes

### Hazard point `type: bridge_ices`: Bridge that ices before the road (`HAZ-BRIDGE_ICES`)

**W8-13 Bridge Ices Before Road** · rule `MUTCD.2C.30.BRIDGE-ICES`

![W8-13](symbols/W8-13.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = may be removed or covered in seasons when not relevant (2C.30-05)
- MUTCD: 2C.30-01 to 06 (Option): Surface Condition signs (W8-5 Slippery When Wet, W8-7 Loose Gravel, W8-8 Rough Road, W8-13 Bridge Ices Before Road, W8-14 Fallen Rocks) may be used to warn of the condition. 2C.30-07 (Guidance): when used, place in advance of the affected section (Table 2C-3) and repeat at intervals where the condition exists. Manual p.175
- Clause wording checked against the manual text: yes

### Hazard point `type: fallen_rocks`: Area where rocks often fall onto the road (`HAZ-FALLEN_ROCKS`)

**W8-14 Fallen Rocks** · rule `MUTCD.2C.30.FALLEN-ROCKS`

![W8-14](symbols/W8-14.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals along the affected section (2C.30-07)
- MUTCD: 2C.30-01 to 06 (Option): Surface Condition signs (W8-5 Slippery When Wet, W8-7 Loose Gravel, W8-8 Rough Road, W8-13 Bridge Ices Before Road, W8-14 Fallen Rocks) may be used to warn of the condition. 2C.30-07 (Guidance): when used, place in advance of the affected section (Table 2C-3) and repeat at intervals where the condition exists. Manual p.175
- Clause wording checked against the manual text: yes

### Hazard point `type: loose_gravel`: Loose gravel on the road surface (`HAZ-LOOSE_GRAVEL`)

**W8-7 Loose Gravel** · rule `MUTCD.2C.30.LOOSE-GRAVEL`

![W8-7](symbols/W8-7.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals along the affected section (2C.30-07)
- MUTCD: 2C.30-01 to 06 (Option): Surface Condition signs (W8-5 Slippery When Wet, W8-7 Loose Gravel, W8-8 Rough Road, W8-13 Bridge Ices Before Road, W8-14 Fallen Rocks) may be used to warn of the condition. 2C.30-07 (Guidance): when used, place in advance of the affected section (Table 2C-3) and repeat at intervals where the condition exists. Manual p.175
- Clause wording checked against the manual text: yes

### Hazard point `type: rough_road`: Rough road surface (`HAZ-ROUGH_ROAD`)

**W8-8 Rough Road** · rule `MUTCD.2C.30.ROUGH-ROAD`

![W8-8](symbols/W8-8.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals along the affected section (2C.30-07)
- MUTCD: 2C.30-01 to 06 (Option): Surface Condition signs (W8-5 Slippery When Wet, W8-7 Loose Gravel, W8-8 Rough Road, W8-13 Bridge Ices Before Road, W8-14 Fallen Rocks) may be used to warn of the condition. 2C.30-07 (Guidance): when used, place in advance of the affected section (Table 2C-3) and repeat at intervals where the condition exists. Manual p.175
- Clause wording checked against the manual text: yes

### Hazard point `type: flooding`: Section that often floods (`HAZ-FLOODING`)

**W8-18 Road May Flood** · rule `MUTCD.2C.34.FLOOD`

![W8-18](symbols/W8-18.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.34-01 (Option): the ROAD MAY FLOOD (W8-18) sign may be used where a section of roadway is subject to frequent flooding; a Depth Gauge (W8-19) may also be installed in the section (2C.34-02 Guidance: at the deepest point, in addition to W8-18). Manual p.176
- Clause wording checked against the manual text: yes

### Hazard point `type: gusty_winds`: Section with strong wind gusts (`HAZ-GUSTY_WINDS`)

**W8-21 Gusty Winds Area** · rule `MUTCD.2C.34.GUSTY-WINDS`

![W8-21](symbols/W8-21.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.34-03 (Option): the GUSTY WINDS AREA (W8-21) sign may be used where wind gusts strong enough to affect trucks and high vehicles frequently occur. Manual p.176
- Clause wording checked against the manual text: yes

### Hazard point `type: fog`: Section where fog often reduces visibility (`HAZ-FOG`)

**W8-22 Fog Area** · rule `MUTCD.2C.34.FOG`

![W8-22](symbols/W8-22.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.34-04 (Option): the FOG AREA (W8-22) sign may be used where fog frequently reduces visibility; a NEXT XX MILES (W7-3aP) plaque may be mounted below. Manual p.176
- Clause wording checked against the manual text: yes

### Hazard point `type: soft_shoulder`: Soft shoulder (`HAZ-SOFT_SHOULDER`)

**W8-4 Soft Shoulder** · rule `MUTCD.2C.29.SOFT-SHOULDER`

![W8-4](symbols/W8-4.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals where the condition continues (2C.29-07)
- MUTCD: 2C.29-01 (Option): the SOFT SHOULDER (W8-4) sign may be used to warn of a soft shoulder. 2C.29-07 (Guidance): repeat at intervals where the condition continually exists. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: low_shoulder`: Shoulder lower than the travel lane (3 in / 75 mm or less) (`HAZ-LOW_SHOULDER`)

**W8-9 Low Shoulder** · rule `MUTCD.2C.29.LOW-SHOULDER`

![W8-9](symbols/W8-9.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals where the condition continues (2C.29-07)
- MUTCD: 2C.29-02 (Option): the LOW SHOULDER (W8-9) sign may be used where the shoulder is lower than the travel lane by 3 in (75 mm) or less. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: shoulder_dropoff`: Unprotected shoulder drop-off deeper than 3 in (75 mm) (`HAZ-SHOULDER_DROPOFF`)

**W8-17 Shoulder Drop-Off** · rule `MUTCD.2C.29.DROP-OFF`

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals where the condition continues (2C.29-07)
- Plaque on the same post: **W8-17P**, default Optional (2C.29-04 (Option): a SHOULDER DROP-OFF (W8-17P) plaque may be mounted below the W8-17 sign. Manual p.173)
- MUTCD: 2C.29-03 (Guidance): the Shoulder Drop Off (W8-17) sign should be used where an unprotected shoulder drop-off next to the travel lane exceeds 3 in (75 mm) for a significant continuous length, based on engineering judgment. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: no_shoulder`: Road section with no shoulder (`HAZ-NO_SHOULDER`)

**W8-23 No Shoulder** · rule `MUTCD.2C.29.NO-SHOULDER`

![W8-23](symbols/W8-23.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right, note = repeat at intervals where the condition continues (2C.29-07)
- MUTCD: 2C.29-05 (Option): the NO SHOULDER (W8-23) sign may be used to warn that a shoulder does not exist along a portion of the roadway. Manual p.173
- Clause wording checked against the manual text: yes

### Hazard point `type: shoulder_ends`: Shoulder ends (`HAZ-SHOULDER_ENDS`)

**W8-25 Shoulder Ends** · rule `MUTCD.2C.29.SHOULDER-ENDS`

![W8-25](symbols/W8-25.png)

- Default class: **Optional** (Option)
- Placement: kind = advance, condition = B, advisory_mph = mph(t['advisory_kmh']) if t.get('advisory_kmh') else 0, from = point, side = right
- MUTCD: 2C.29-06 (Option): the SHOULDER ENDS (W8-25) sign may be used to warn that a shoulder is ending. Manual p.175
- Clause wording checked against the manual text: yes

### Hazard point `type: no_passing_start`: Start of a no-passing zone (two-lane road) (`HAZ-NO_PASSING_START`)

**W14-3 No Passing Zone** · rule `MUTCD.2C.53.NO-PASSING-ZONE`

![W14-3](symbols/W14-3.png)

- Default class: **Optional** (Option)
- Placement: kind = at_point, side = left
- MUTCD: 2C.53-01 (Standard): when used, the NO PASSING ZONE (W14-3) pennant shall be installed on the left-hand side of the roadway at the beginning of no-passing zones identified by pavement markings or DO NOT PASS signs or both. Use itself is optional. Manual p.190
- Clause wording checked against the manual text: yes

### Hazard point `type: dead_end`: Entrance to a street that ends without meeting another street (`HAZ-DEAD_END`)

**W14-1 ROAD ENDS Signs** · rule `MUTCD.2C.24.DEAD-END`

- Default class: **Optional** (Option)
- Placement: kind = at_point, side = right, note = post as near as practicable to the entry point, or far enough ahead to let drivers turn at the nearest street (2C.24-04)
- MUTCD: 2C.24-01 (Option): the DEAD END (W14-1) sign may be used at the entrance to a single road or street that terminates without intersecting another street. 2C.24-04 (Guidance): post as near as practicable to the entry point. 2C.24-08 (Standard): W8-26/W8-26a shall not replace it. Manual p.171
- Clause wording checked against the manual text: yes

### Hazard point `type: no_outlet`: Entrance to a road network with no other exit (`HAZ-NO_OUTLET`)

**W14-2 Dead End, No Outlet** · rule `MUTCD.2C.24.NO-OUTLET`

![W14-2](symbols/W14-2.png)

- Default class: **Optional** (Option)
- Placement: kind = at_point, side = right, note = post as near as practicable to the entry point, or far enough ahead to let drivers turn at the nearest street (2C.24-04)
- MUTCD: 2C.24-01 (Option): the NO OUTLET (W14-2) sign may be used at the entrance to a road or road network from which there is no other exit. 2C.24-04 (Guidance): post as near as practicable to the entry point. Manual p.171
- Clause wording checked against the manual text: yes

### Divided section begins (not at an intersection) (`DIVIDED-BEGIN`)

**W6-1 Divided Highway** · rule `MUTCD.2C.20.DIVIDED-HIGHWAY`

![W6-1](symbols/W6-1.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = node, side = right
- MUTCD: 2C.20-01 (Guidance): a Divided Highway (W6-1) sign should be used on the approaches to a section of highway (not an intersection or junction) where the opposing flows of traffic are separated by a median or other physical barrier. 2C.20-02 (Standard): not instead of a Keep Right sign on the median nose. Manual p.170
- Clause wording checked against the manual text: yes

**R4-7 Keep Right** · rule `MUTCD.2B.39.KEEP-RIGHT-NOSE`

![R4-7](symbols/R4-7.png)

- Default class: **Optional** (Option)
- Placement: kind = at_point, side = left, confidence = Medium, note = on the face of or just in front of the median nose so traffic passes to its right (2B.39-04); R4-7c only on noses narrower than 4 ft / 1.2 m (2B.39-10/11)
- MUTCD: 2B.39-01 (Option): the Keep Right (R4-7) sign may be used where traffic must pass only to the right of a roadway feature or obstruction. 2B.39-02 (Guidance): where it is not readily apparent that traffic must keep right, it should be used. 2B.39-03 (Standard): at the start of a median, as close as practicable to the approach end. Manual pp.102-104
- Clause wording checked against the manual text: yes

### Divided section ends (not at an intersection) (`DIVIDED-END`)

**W6-2 Divided Highway Ends** · rule `MUTCD.2C.21.DIVIDED-ENDS`

![W6-2](symbols/W6-2.png)

- Default class: **Recommended** (Guidance)
- Placement: kind = advance, condition = B, advisory_mph = 0, from = node, side = right
- MUTCD: 2C.21-01 (Guidance): a Divided Highway Ends (W6-2) sign should be used in advance of the end of a section of physically divided highway (not an intersection or junction) as a warning of two-way traffic ahead. Manual p.170
- Clause wording checked against the manual text: yes

**W6-3 Two-Way Traffic** · rule `MUTCD.2C.51.TWO-WAY-TRAFFIC`

![W6-3](symbols/W6-3.png)

- Default class: **Recommended** (Guidance)
- Applies when: `to_two_lane`
- Placement: kind = at_point, side = right, back_add_m = 30, note = near the transition, downstream of the W6-2 sign
- MUTCD: 2C.21-02 (Guidance): the Two-Way Traffic (W6-3) sign should be used to give warning and notice of the transition to a two-lane, two-way section. 2C.51-01 (Guidance): W6-3 should be used to warn of a transition from a multi-lane divided section to a two-lane, two-way section. Manual pp.170, 189
- Clause wording checked against the manual text: yes

### One-way street becomes two-way (`ONEWAY-TO-TWOWAY`)

**W6-3 Two-Way Traffic** · rule `MUTCD.2C.51.ONEWAY-TO-TWOWAY`

![W6-3](symbols/W6-3.png)

- Default class: **Recommended** (Guidance)
- Applies when: `to_two_lane`
- Placement: kind = advance, condition = B, advisory_mph = 0, from = node, side = right
- Plaque on the same post: **W16-9P**, default Recommended (2C.51-02 (Guidance): W6-3 with an AHEAD (W16-9P) plaque. Manual p.189)
- MUTCD: 2C.51-02 (Guidance): a Two-Way Traffic (W6-3) sign with an AHEAD (W16-9P) plaque should be used to warn road users of a transition from a one-way street to a two-lane, two-way section (Figure 2B-18). Manual p.189
- Clause wording checked against the manual text: yes

### Two one-way roadways converge, no added lane (`MERGE`)

**W4-1 Merge** · rule `MUTCD.2C.45.MERGE-MAJOR`

![W4-1](symbols/W4-1.png)

- Default class: **Optional** (Option)
- Applies when: `role == 'major'`
- If `equal` → **Recommended** (Guidance)
- Placement: kind = advance, condition = A, from = node, side = {t['merge_side']}
- MUTCD: 2C.45-01 (Option): a Merge (W4-1) sign may be used to warn road users on the major roadway of merging movements where lanes from two roadways converge as a single lane. 2C.45-03/04 (Guidance): on the side where merging traffic will be met, symbol oriented to that side. 2C.45-06 (Guidance): on each roadway where two roadways of about equal importance converge. 2C.45-08 (Standard): not instead of a Lane Ends (W4-2) sign. Table 2C-3 Condition A (typical sign: Merge). Manual pp.182-183
- Clause wording checked against the manual text: yes

**W4-1 Merge** · rule `MUTCD.2C.45.MERGE-ENTERING`

![W4-1](symbols/W4-1.png)

- Default class: **Optional** (Option)
- Applies when: `role == 'entering'`
- If `equal` → **Recommended** (Guidance)
- Placement: kind = advance, condition = A, from = node, side = right, note = use W4-5 (Entering Roadway Merge) if the entering roadway curves before the merge (2C.45-05)
- MUTCD: 2C.45-02 (Option): a Merge sign may also be installed on the entering roadway. 2C.45-06 (Guidance): on each roadway where two roadways of about equal importance converge. Manual p.183
- Clause wording checked against the manual text: yes

### Two one-way roadways converge with an added lane (`ADDED-LANE`)

**W4-3 Added Lane** · rule `MUTCD.2C.46.ADDED-LANE-MAJOR`

![W4-3](symbols/W4-3.png)

- Default class: **Recommended** (Guidance)
- Applies when: `role == 'major'`
- Placement: kind = advance, condition = A, from = node, side = {t['merge_side']}
- MUTCD: 2C.46-01 (Guidance): the Added Lane (W4-3) sign should be installed in advance of a point where two roadways converge and merging movements are not required. 2C.46-02 (Guidance): on the major roadway, on the side from which the entering roadway converges, symbol oriented to that side. Manual p.183
- Clause wording checked against the manual text: yes

**W4-3 Added Lane** · rule `MUTCD.2C.46.ADDED-LANE-ENTERING`

![W4-3](symbols/W4-3.png)

- Default class: **Conditional** (Study)
- Applies when: `role == 'entering'`
- Placement: kind = advance, condition = A, from = node, side = right, note = use W4-6 (Entering Roadway Added Lane) if the entering roadway curves before converging (2C.46-03)
- Study that decides it: Is the Added Lane sign on the major roadway visible from the entering roadway? If not, a second W4-3 should be placed on the entering roadway (2C.46-01).
- MUTCD: 2C.46-01 (Guidance): when possible the Added Lane sign should be visible from both roadways; if not, an Added Lane sign should be placed on the side of each roadway. Manual p.183
- Clause wording checked against the manual text: yes

### Hazard point types

Mark a hazard as a point with `type` set to one of these; the engine asks for any listed attribute that is missing. Advance distance: Table 2C-3 Condition B, using the point's `advisory_kmh` column when given, otherwise the 0 mph (potential stop) column.

| type | What it marks | Direction | Attributes the engine asks for |
|---|---|---|---|
| `rail_crossing` | Highway-rail grade crossing (point on the track centre) | both | `tracks`; `signals_gates` |
| `narrow_structure` | Bridge, culvert or underpass narrower than the approach | both | `structure`; `clear_width_m` |
| `road_narrows` | Abrupt pavement narrowing where opposing vehicles cannot pass together | both | — |
| `low_clearance` | Structure with low vertical clearance | both | `clearance_m` |
| `speed_hump` | Speed hump or speed table | both | `advisory_kmh` |
| `bump` | Sharp rise in the road profile | both | — |
| `dip` | Sharp depression in the road profile | both | — |
| `pavement_ends` | Paved surface changes to gravel or earth (point at the change) | ask (fwd/rev/both) | — |
| `downgrade` | Start of a steep downgrade (point at the top) | ask (fwd/rev/both) | `grade_pct`; `length_m` |
| `school_bus_stop` | School bus stop | both | `bus_not_visible` |
| `truck_crossing` | Truck entrance or crossing | both | — |
| `farm_vehicles` | Farm vehicle entrance or crossing | both | — |
| `emergency_station` | Emergency vehicle station (fire, ambulance) | both | `emergency_signal` |
| `bicycle_crossing` | Unexpected bicycle entry or crossing | both | — |
| `deer_crossing` | Deer or wild animal crossing area | both | — |
| `cattle_crossing` | Cattle or livestock crossing | both | — |
| `equestrian_crossing` | Horse riders crossing | both | — |
| `playground` | Designated children's playground next to the road | both | — |
| `slippery` | Start of an unexpectedly slippery section | both | — |
| `bridge_ices` | Bridge that ices before the road | both | — |
| `fallen_rocks` | Area where rocks often fall onto the road | both | — |
| `loose_gravel` | Loose gravel on the road surface | both | — |
| `rough_road` | Rough road surface | both | — |
| `flooding` | Section that often floods | both | — |
| `gusty_winds` | Section with strong wind gusts | both | — |
| `fog` | Section where fog often reduces visibility | both | — |
| `soft_shoulder` | Soft shoulder | both | — |
| `low_shoulder` | Shoulder lower than the travel lane (3 in / 75 mm or less) | both | — |
| `shoulder_dropoff` | Unprotected shoulder drop-off deeper than 3 in (75 mm) | both | — |
| `no_shoulder` | Road section with no shoulder | both | — |
| `shoulder_ends` | Shoulder ends | ask (fwd/rev/both) | — |
| `no_passing_start` | Start of a no-passing zone (two-lane road) | ask (fwd/rev/both) | — |
| `dead_end` | Entrance to a street that ends without meeting another street | ask (fwd/rev/both) | — |
| `no_outlet` | Entrance to a road network with no other exit | ask (fwd/rev/both) | — |

## 3. Sign catalog

Sizes in inches (width x height) by road type, from MUTCD Tables 2B-1, 2C-1 and 7B-1. Pictures from the manual's figures.

| Sign | Code | Official name | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Source |
|---|---|---|---|---|---|---|---|---|---|
| ![R1-1](symbols/R1-1.png) | R1-1 | Stop | 30x30 | 36x36 | 36x36 | — | 30x30 | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-1, manual p.74 |
| ![R1-2](symbols/R1-2.png) | R1-2 | Yield | 36x36x36 | 48x48x48 | 48x48x48 | 60x60x60 | 30x30x30 | — | Table 2B-1, manual p.68; picture: Figure 2B-1, manual p.74 |
| ![R1-3P](symbols/R1-3P.png) | R1-3P | All Way (plaque) | 18x6 | 18x6 | — | — | — | 30x12 | Table 2B-1, manual p.68; picture: Figure 2B-1, manual p.74 |
| ![R2-1](symbols/R2-1.png) | R2-1 | Speed Limit | 24x30 | 30x36 | 36x48 | 48x60 | 18x24 | 30x36 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R4-7](symbols/R4-7.png) | R4-7 | Keep Right | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R5-1](symbols/R5-1.png) | R5-1 | Do Not Enter | 30x30 | 36x36 | 36x36 | 48x48 | — | 36x36 | Table 2B-1, manual p.70; picture: Figure 2B-13, manual p.109 |
| ![R5-1a](symbols/R5-1a.png) | R5-1a | Wrong Way | 36x24 | 42x30 | 36x24 | 42x30 | 30x18 | 42x30 | Table 2B-1, manual p.70; picture: Figure 2B-13, manual p.109 |
| ![R6-1](symbols/R6-1.png) | R6-1 | One Way | 36x12 | 48x18 | 48x18 | 48x18 | — | 72x24 | Table 2B-1, manual p.70; picture: Figure 2B-13, manual p.109 |
| ![R6-2](symbols/R6-2.png) | R6-2 | One Way | 24x30 | 30x36 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.70; picture: Figure 2B-13, manual p.109 |
| ![W1-1](symbols/W1-1.png) | W1-1 | Turn | 30x30 | 36x36 | 36x36 | 36x36 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-2](symbols/W1-2.png) | W1-2 | Curve | 30x30 | 36x36 | 36x36 | 36x36 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-3](symbols/W1-3.png) | W1-3 | Reverse Turn | 30x30 | 36x36 | 36x36 | 36x36 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-4](symbols/W1-4.png) | W1-4 | Reverse Curve | 30x30 | 36x36 | 36x36 | 36x36 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-8](symbols/W1-8.png) | W1-8 | Chevron Alignment | 18x24 | 18x24 | 30x36 | 36x48 | — | 24x30 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W13-1P](symbols/W13-1P.png) | W13-1P | Advisory Speed (plaque) | 18x18 | 18x18 | 24x24 | 30x30 | — | 30x30 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W2-1](symbols/W2-1.png) | W2-1 | Cross Road | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-9/2C-10, manual p.179 |
| ![W2-2](symbols/W2-2.png) | W2-2 | Side Road | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-9/2C-10, manual p.179 |
| ![W2-4](symbols/W2-4.png) | W2-4 | T-Intersection | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-9/2C-10, manual p.179 |
| ![W2-6](symbols/W2-6.png) | W2-6 | Circular Intersection | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-9/2C-10, manual p.179 |
| ![W3-1](symbols/W3-1.png) | W3-1 | Stop Ahead | 30x30 | 30x30 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
| ![W3-2](symbols/W3-2.png) | W3-2 | Yield Ahead | 30x30 | 30x30 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
| ![W3-3](symbols/W3-3.png) | W3-3 | Signal Ahead | 30x30 | 30x30 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
| ![W3-5](symbols/W3-5.png) | W3-5 | Reduced Speed Limit Ahead | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-9/2C-10, manual p.179 |
| ![W4-2](symbols/W4-2.png) | W4-2 | Lane Ends | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W11-2](symbols/W11-2.png) | W11-2 | Pedestrian | 30x30 | 36x36 | 36x36 | — | — | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W16-7P](symbols/W16-7P.png) | W16-7P | Diagonal Downward Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-9P](symbols/W16-9P.png) | W16-9P | Ahead (plaque) | 24x12 | 24x12 | 30x18 | — | — | 30x18 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![S1-1](symbols/S1-1.png) | S1-1 | School | 36x36 | 36x36 | — | — | 30x30 | 48x48 | Table 7B-1, manual p.971; picture: Figure 7B-1, manual p.973 |
|  | DELINEATOR | Delineator (single yellow retroreflector) | 3x3 | 3x3 | 3x3 | 3x3 | — | — | not verified |
| ![D1-1](symbols/D1-1.png) | D1-1 | Destination (1 line) | Variesx18 | Variesx18 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-9, manual p.233 |
|  | D1-1a | Destination and Distance (1 line) | Variesx18 | Variesx18 | — | — | — | — | Table 2D-1, manual p.207 |
| ![D1-1b](symbols/D1-1b.png) | D1-1b | Bicycle Destination Signs | Variesx6 | Variesx6 | — | — | Variesx6 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D1-1c](symbols/D1-1c.png) | D1-1c | Bicycle Destination (1 line) | Variesx6 | Variesx6 | — | — | Variesx6 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D1-1d](symbols/D1-1d.png) | D1-1d | Circular Intersection Destination (1 line) | Variesx18 | Variesx18 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-9, manual p.239 |
|  | D1-1e | Circular Intersection Departure Guide | Variesx42 | Variesx42 | — | — | — | — | Table 2D-1, manual p.207 |
| ![D1-2](symbols/D1-2.png) | D1-2 | Destination (2 lines) | Variesx30 | Variesx30 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-9, manual p.233 |
| ![D1-2a](symbols/D1-2a.png) | D1-2a | Destination and Distance (2 lines) | Variesx30 | Variesx30 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-9, manual p.233 |
| ![D1-2b](symbols/D1-2b.png) | D1-2b | Bicycle Destination (2 lines) | Variesx12 | Variesx12 | — | — | Variesx12 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D1-2c](symbols/D1-2c.png) | D1-2c | Bicycle Destination (2 lines) | Variesx12 | Variesx12 | — | — | Variesx12 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D1-2d](symbols/D1-2d.png) | D1-2d | Circular Intersection Destination (2 lines) | Variesx30 | Variesx30 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-9, manual p.239 |
| ![D1-3](symbols/D1-3.png) | D1-3 | Destination (3 lines) | Variesx42 | Variesx42 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.233 |
| ![D1-3a](symbols/D1-3a.png) | D1-3a | Destination and Distance (3 lines) | Variesx42 | Variesx42 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.233 |
| ![D1-3b](symbols/D1-3b.png) | D1-3b | Bicycle Destination (3 lines) | Variesx18 | Variesx18 | — | — | Variesx18 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D1-3c](symbols/D1-3c.png) | D1-3c | Bicycle Destination (3 lines) | Variesx18 | Variesx18 | — | — | Variesx18 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D1-3d](symbols/D1-3d.png) | D1-3d | Circular Intersection Destination (3 lines) | Variesx42 | Variesx42 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.239 |
| ![D1-5](symbols/D1-5.png) | D1-5 | Circular Intersection Diagrammatic Destination | Variesx72 | Variesx72 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.239 |
| ![D1-5a](symbols/D1-5a.png) | D1-5a | Circular Intersection Diagrammatic Destination, | Variesx78 | Variesx78 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.239 |
| ![D2-1](symbols/D2-1.png) | D2-1 | Distance (1 line) | Variesx18 | Variesx18 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.233 |
| ![D2-1a](symbols/D2-1a.png) | D2-1a | Bike Route Destination and Distance (1 Line) | Variesx12 | Variesx12 | — | — | Variesx12 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D2-2](symbols/D2-2.png) | D2-2 | Distance (2 lines) | Variesx30 | Variesx30 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.233 |
| ![D2-2a](symbols/D2-2a.png) | D2-2a | Bike Route Destination and Distance (2 Lines) | Variesx15 | Variesx15 | — | — | Variesx15 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D2-3](symbols/D2-3.png) | D2-3 | Distance (3 lines) | Variesx42 | Variesx42 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.233 |
| ![D2-3a](symbols/D2-3a.png) | D2-3a | Bike Route Destination and Distance (3 Lines) | Variesx18 | Variesx18 | — | — | Variesx18 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D3-1](symbols/D3-1.png) | D3-1 | Street Name (1 line) | Variesx48 | Variesx48 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-14, manual p.247 |
| ![D3-1a](symbols/D3-1a.png) | D3-1a | Street Name (1 line) | Variesx48 | Variesx48 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-14, manual p.247 |
|  | D3-2 | Advance Street Name (2 lines) | Variesx54 | Variesx54 | — | — | — | — | Table 2D-1, manual p.208 |
| ![D4-1](symbols/D4-1.png) | D4-1 | Parking Area Directional | 30x24 | 30x24 | — | — | 18x15 | — | Table 2D-1, manual p.208; picture: Figure 2D-14, manual p.247 |
| ![D4-2](symbols/D4-2.png) | D4-2 | Park - Ride | 30x36 | 30x36 | — | — | 24x30 | 36x48 | Table 2D-1, manual p.208; picture: Figure 2D-14, manual p.247 |
| ![D4-3](symbols/D4-3.png) | D4-3 | Bicycle Parking Area Directional | 18x12 | 18x12 | — | — | 18x12 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1070 |
| ![D4-4](symbols/D4-4.png) | D4-4 | Bicycle-Sharing Station Directional | 12x18 | 12x18 | — | — | 12x18 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1071 |
| ![D4-4a](symbols/D4-4a.png) | D4-4a | Bicycle Lockers Directional | 12x18 | 12x18 | — | — | 12x18 | — | Table 9A-1, manual p.1050; picture: Figure 9D-1, manual p.1071 |
| ![D5-1](symbols/D5-1.png) | D5-1 | Rest Area Advance | 78x36 | 78x36 | 132x60(F) | 132x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-1a](symbols/D5-1a.png) | D5-1a | Rest Area Advance Direction | 78x36 | 78x36 | 132x60(F) | 132x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-2](symbols/D5-2.png) | D5-2 | Rest Area Entrance Direction | 78x36 | 78x36 | 132x66(F) | 132x66(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-2a](symbols/D5-2a.png) | D5-2a | Rest Area Gore | 42x48 | 42x48 | 78x78(F) | 78x78(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-5](symbols/D5-5.png) | D5-5 | Rest Area Directional | 42x48 | 42x48 | — | — | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-6](symbols/D5-6.png) | D5-6 | Next Rest Area | 78x54 | 78x54 | 132x78(F) | 132x78(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
|  | D5-7 | Rest Area Tourist Info Center Advance | 90x72 | 90x72 | 156x108(F) | 156x108(F) | — | — | Table 2I-1, manual p.476 |
|  | D5-7a | Rest Area Tourist Info Center | 90x72 | 90x72 | 156x108(F) | 156x108(F) | — | — | Table 2I-1, manual p.476 |
|  | D5-8 | Rest Area Tourist Info Center Entrance Direction | 84x72 | 84x72 | 138x108(F) | 138x108(F) | — | — | Table 2I-1, manual p.476 |
| ![D5-9](symbols/D5-9.png) | D5-9 | Parking Area Advance | 96x36 | 96x36 | 162x60(F) | 162x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-9a](symbols/D5-9a.png) | D5-9a | Parking Area Entrance Direction | 96x36 | 96x36 | 162x60(F) | 162x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-9b](symbols/D5-9b.png) | D5-9b | Parking Area Gore | 62x48 | 62x48 | 108x78(F) | 108x78(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-10](symbols/D5-10.png) | D5-10 | Picnic Area (Roadside Table, Roadside | 84x36 | 84x36 | 144x60(F) | 144x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-10a](symbols/D5-10a.png) | D5-10a | Picnic Area (Roadside Table, Roadside | 84x36 | 84x36 | 144x60(F) | 144x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-10b](symbols/D5-10b.png) | D5-10b | Picnic Area (Roadside Table, Roadside | 54x48 | 54x48 | 92x78(F) | 92x78(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-11](symbols/D5-11.png) | D5-11 | Scenic Area (Scenic View, Scenic | 84x36 | 84x36 | 144x60(F) | 144x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-11a](symbols/D5-11a.png) | D5-11a | Scenic Area (Scenic View, Scenic | 84x36 | 84x36 | 144x60(F) | 144x60(F) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-11b](symbols/D5-11b.png) | D5-11b | Overlook) Gore | 54x48 | 54x48 | 76x66(E) | 76x66(E) | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
|  | D5-12 | Interstate Oasis | — | — | 198x60(F) | 198x60(F) | — | — | Table 2I-1, manual p.476 |
|  | D5-12aP | Interstate Oasis (plaque) | — | — | 114x48 | 114x48 | — | — | Table 2I-1, manual p.476 |
|  | D5-12b | Interstate Oasis Directional | — | — | 48x36 | 48x36 | — | — | Table 2I-1, manual p.476 |
| ![D5-13](symbols/D5-13.png) | D5-13 | Brake Check Area Advance | 96x54 | 96x54 | 132x66 | 132x66 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-14](symbols/D5-14.png) | D5-14 | Brake Check Area Entrance Direction | 96x54 | 96x54 | 132x78 | 132x78 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-15](symbols/D5-15.png) | D5-15 | Chain-Up Area Advance | 72x54 | 72x54 | 102x66 | 102x66 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
| ![D5-16](symbols/D5-16.png) | D5-16 | Chain-Up Area Entrance Direction | 72x54 | 72x54 | 102x78 | 102x78 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-5, manual p.485 |
|  | D8-1 | Advance Weigh Station Distance | 78x60 | 78x60 | — | — | 60x48 | 96x72 | Table 2D-1, manual p.208 |
|  | D8-1a | Weigh Station Ahead | 66x48 | 66x48 | — | — | 48x36 | — | Table 2D-1, manual p.208 |
|  | D8-2 | Weigh Station Advance Direction | 84x72 | 84x72 | — | — | 66x54 | 108x90 | Table 2D-1, manual p.208 |
|  | D8-3 | Weigh Station Entrance Direction | 66x60 | 66x60 | — | — | 48x42 | 84x78 | Table 2D-1, manual p.208 |
| ![D9-1](symbols/D9-1.png) | D9-1 | Telephone | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-2](symbols/D9-2.png) | D9-2 | Hospital | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-3](symbols/D9-3.png) | D9-3 | Camping | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-4](symbols/D9-4.png) | D9-4 | Litter Container | 24x30 | 24x30 | 36x48 | 36x48 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-6](symbols/D9-6.png) | D9-6 | International Symbol of Accessibility | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-6P](symbols/D9-6P.png) | D9-6P | Van Accessible (plaque) | 18x9 | 18x9 | — | — | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-7](symbols/D9-7.png) | D9-7 | Gas | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-8](symbols/D9-8.png) | D9-8 | Food | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-9](symbols/D9-9.png) | D9-9 | Lodging | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-10](symbols/D9-10.png) | D9-10 | Tourist Information | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-11](symbols/D9-11.png) | D9-11 | Diesel Fuel | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-11a](symbols/D9-11a.png) | D9-11a | Alternative Fuel - Compressed Natural Gas | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-11b](symbols/D9-11b.png) | D9-11b | Electric Vehicle Charging | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
| ![D9-11bP](symbols/D9-11bP.png) | D9-11bP | Electric Vehicle Charging (plaque) | 24x18 | 24x18 | 30x24 | 30x24 | — | — | Table 2I-1, manual p.476; picture: Figure 2I-1, manual p.478 |
|  | D9-11c | Alternative Fuel - Ethanol | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.476 |
| ![D9-11d](symbols/D9-11d.png) | D9-11d | Alternative Fuel - Liquefied Natural Gas | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-11e](symbols/D9-11e.png) | D9-11e | Alternative Fuel - Liquefied Petroleum Gas | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-11f](symbols/D9-11f.png) | D9-11f | Alternative Fuel - Hydrogen | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-11g](symbols/D9-11g.png) | D9-11g | Alternative Fuel - Biofuel | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-12](symbols/D9-12.png) | D9-12 | RV Sanitary Station | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-13](symbols/D9-13.png) | D9-13 | Emergency Medical Services | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-13aP](symbols/D9-13aP.png) | D9-13aP | Hospital (plaque) | 24x12 | 24x12 | 30x12 | 30x12 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-13bP](symbols/D9-13bP.png) | D9-13bP | Ambulance Station (plaque) | 24x12 | 24x12 | 30x15 | 30x15 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-13cP](symbols/D9-13cP.png) | D9-13cP | Emergency Medical Care (plaque) | 24x18 | 24x18 | 30x24 | 30x24 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-13dP](symbols/D9-13dP.png) | D9-13dP | Trauma Center (plaque) | 24x12 | 24x12 | 30x15 | 30x15 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-14](symbols/D9-14.png) | D9-14 | Police | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-16](symbols/D9-16.png) | D9-16 | Truck Parking | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-16aP](symbols/D9-16aP.png) | D9-16aP | Truck External Power (plaque) | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
|  | D9-16b | Truck Parking Availability - Exit Number | Variesx144 | Variesx144 | Variesx144 | Variesx144 | — | — | Table 2I-1, manual p.477 |
|  | D9-16c | Truck Parking Availability - Distance | Variesx144 | Variesx144 | Variesx144 | Variesx144 | — | — | Table 2I-1, manual p.477 |
|  | D9-16d | Signing for Truck Parking Availability (D9-16b through D9-16e) | — | — | — | — | — | — | section text |
|  | D9-16e | Signing for Truck Parking Availability (D9-16b through D9-16e) | — | — | — | — | — | — | section text |
|  | D9-17P | Next Services Advance (plaque) | 72x24 | 72x24 | 114x30 | 114x30 | — | — | Table 2I-1, manual p.477 |
|  | D9-17a | Next EV Charging | — | — | — | — | — | — | section text |
|  | D9-18 |  | 108x84 | 108x84 | — | — | — | — | Table 2I-1, manual p.477 |
|  | D9-18a | General Services with Exit Number | 72x60 | 72x60 | 102x84(E) | 102x84(E) | — | — | Table 2I-1, manual p.477 |
|  | D9-18b |  | 108x84 | 108x84 | — | — | — | — | Table 2I-1, manual p.477 |
|  | D9-18c | General Services with Action Message | 72x60 | 72x60 | 102x84(E) | 102x84(E) | — | — | Table 2I-1, manual p.477 |
|  | D9-18dP | Rural Interchange General Services | — | — | 120x36 | 120x36 | — | — | Table 2I-1, manual p.477 |
|  | D9-18eP | Rural Interchange General Services | — | — | Variesx24 | Variesx24 | — | — | Table 2I-1, manual p.477 |
|  | D9-18fP | Rural Interchange General Services | — | — | Variesx42 | Variesx42 | — | — | Table 2I-1, manual p.477 |
|  | D9-19 | Alternative Fuels Corridor | 24x24 | 24x24 | 36x36 | 36x36 | — | — | Table 2H-1, manual p.461 |
|  | D9-19aP | Alternative Fuels Corridor (1 line) (plaque) | 30x9 | 30x9 | 42x12 | 42x12 | — | — | Table 2H-1, manual p.461 |
|  | D9-19bP | Alternative Fuels Corridor (2 lines) (plaque) | 30x12 | 30x12 | 42x18 | 42x18 | — | — | Table 2H-1, manual p.461 |
| ![D9-20](symbols/D9-20.png) | D9-20 | Pharmacy | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-20aP](symbols/D9-20aP.png) | D9-20aP | 24-Hour (plaque) | 24x12 | 24x12 | 30x12 | 30x12 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-21](symbols/D9-21.png) | D9-21 | Telecommunications Device for the Deaf | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D9-22](symbols/D9-22.png) | D9-22 | Wireless Internet | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-1, manual p.478 |
| ![D10-1](symbols/D10-1.png) | D10-1 | Reference Location (1 digit) | 10x18 | 10x18 | 12x24 | 12x24 | — | — | Table 2H-1, manual p.461; picture: Figure 9D-1, manual p.1071 |
| ![D10-1a](symbols/D10-1a.png) | D10-1a | Intermediate Reference Location (2 digits) | 10x27 | 10x27 | 12x36 | 12x36 | — | — | Table 2H-1, manual p.461; picture: Figure 9D-1, manual p.1071 |
| ![D10-2](symbols/D10-2.png) | D10-2 | Reference Location (2 digits) | 10x27 | 10x27 | 12x36 | 12x36 | — | — | Table 2H-1, manual p.461; picture: Figure 9D-1, manual p.1071 |
| ![D10-2a](symbols/D10-2a.png) | D10-2a | Intermediate Reference Location (3 digits) | 10x36 | 10x36 | 12x48 | 12x48 | — | — | Table 2H-1, manual p.461; picture: Figure 9D-1, manual p.1071 |
| ![D10-3](symbols/D10-3.png) | D10-3 | Reference Location (3 digits) | 10x36 | 10x36 | 12x48 | 12x48 | — | — | Table 2H-1, manual p.461; picture: Figure 9D-1, manual p.1071 |
| ![D10-3a](symbols/D10-3a.png) | D10-3a | Intermediate Reference Location (4 digits) | 10x48 | 10x48 | 12x60 | 12x60 | — | — | Table 2H-1, manual p.461; picture: Figure 9D-1, manual p.1071 |
|  | D10-4 | Enhanced Reference Location | 18x54 | 18x54 | — | — | — | — | Table 2H-1, manual p.461 |
|  | D10-5 | Intermediate Enhanced Reference Location | 18x60 | 18x60 | — | — | — | — | Table 2H-1, manual p.461 |
| ![D11-1](symbols/D11-1.png) | D11-1 | Bike Route | 24x18 | 24x18 | — | — | 24x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-1bP](symbols/D11-1bP.png) | D11-1bP | Bike Route (plaque) | 18x6 | 18x6 | — | — | 18x6 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
|  | D11-1c | Bike Route with Destination | 24x18 | 24x18 | — | — | 24x18 | — | Table 9A-1, manual p.1051 |
| ![D11-10a](symbols/D11-10a.png) | D11-10a | Shared-Use Path Destination (1 line) | — | — | — | — | Variesx6 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-10b](symbols/D11-10b.png) | D11-10b | Shared-Use Path Destination (2 lines) | — | — | — | — | Variesx12 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-10c](symbols/D11-10c.png) | D11-10c | Shared-Use Path Destination (3 lines) | — | — | — | — | Variesx18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-10d](symbols/D11-10d.png) | D11-10d | Shared-Use Path Destination and Distance (1 line) | — | — | — | — | Variesx6 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-10e](symbols/D11-10e.png) | D11-10e | Shared-Use Path Destination and | — | — | — | — | Variesx12 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-10f](symbols/D11-10f.png) | D11-10f | Shared-Use Path Destination and | — | — | — | — | Variesx18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1071 |
| ![D11-11](symbols/D11-11.png) | D11-11 | Bicycles Directional | — | — | — | — | 18x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![D11-12](symbols/D11-12.png) | D11-12 | Pedestrians Directional | — | — | — | — | 18x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![D11-13](symbols/D11-13.png) | D11-13 | Skaters Directional | — | — | — | — | 18x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![D11-14](symbols/D11-14.png) | D11-14 | Equestrians Directional | — | — | — | — | 18x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![D11-20](symbols/D11-20.png) | D11-20 | Two-Stage Bicycle Turn Box Advance | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![D11-20a](symbols/D11-20a.png) | D11-20a | Two-Stage Bicycle Turn Box | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![D12-1](symbols/D12-1.png) | D12-1 | Radio - Weather Information | 84x48 | 84x48 | 132x84 | 132x84 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-8, manual p.488 |
|  | D12-1a | Radio - Traffic Information | 96x48 | 96x48 | 120x60 | 120x60 | — | — | Table 2I-1, manual p.477 |
|  | D12-1bP | Urgent Message When Flashing (plaque) | 84x30 | 84x30 | 108x36 | 108x36 | — | — | Table 2I-1, manual p.477 |
| ![D12-2](symbols/D12-2.png) | D12-2 | Carpool Information | 60x42 | 60x42 | 96x66 | 96x66 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-8, manual p.488 |
| ![D12-3](symbols/D12-3.png) | D12-3 | Channel 9 Monitored | 84x48 | 84x48 | 132x84 | 132x84 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-8, manual p.488 |
| ![D12-4](symbols/D12-4.png) | D12-4 | Emergency Call 911 | 66x30 | 66x30 | 96x48 | 96x48 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-8, manual p.488 |
|  | D12-5 | Travel Info Call 511 (pictograph) | 48x60 | 48x60 | 66x72 | 66x72 | — | — | Table 2I-1, manual p.477 |
| ![D12-5a](symbols/D12-5a.png) | D12-5a | Travel Info Call 511 | 48x36 | 48x36 | 66x48 | 66x48 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-8, manual p.488 |
| ![D12-6](symbols/D12-6.png) | D12-6 | Roadside Assistance | 60x42 | 60x42 | 78x54 | 78x54 | — | — | Table 2I-1, manual p.477; picture: Figure 2I-8, manual p.488 |
| ![D13-1](symbols/D13-1.png) | D13-1 | Crossover | 60x30 | 60x30 | — | — | — | 78x42 | Table 2D-1, manual p.208; picture: Figure 2D-26, manual p.263 |
| ![D13-2](symbols/D13-2.png) | D13-2 | Crossover | 60x30 | 60x30 | — | — | — | 78x42 | Table 2D-1, manual p.208; picture: Figure 2D-26, manual p.263 |
|  | D13-3 | Freeway Entrance | 48x30 | 48x30 | — | — | — | — | Table 2D-1, manual p.208 |
|  | D13-3a | Freeway Entrance (Directional) | 48x42 | 48x42 | — | — | — | — | Table 2D-1, manual p.208 |
| ![D15-1](symbols/D15-1.png) | D15-1 | Combination Lane Use / Destination | Variesx96 | Variesx96 | — | — | — | — | Table 2D-1, manual p.208; picture: Figure 2D-9, manual p.233 |
| ![D17-1](symbols/D17-1.png) | D17-1 | Next Truck Lane | 42x48 | 42x48 | — | — | — | 60x66 | Table 2D-1, manual p.208; picture: Figure 2D-26, manual p.263 |
| ![D17-2](symbols/D17-2.png) | D17-2 | Advance Truck Lane | 42x42 | 42x42 | — | — | — | 60x54 | Table 2D-1, manual p.208; picture: Figure 2D-26, manual p.263 |
| ![D17-3](symbols/D17-3.png) | D17-3 | Next Passing Lane | 42x48 | 42x48 | — | — | — | 60x66 | Table 2D-1, manual p.208; picture: Figure 2D-26, manual p.263 |
| ![D17-4](symbols/D17-4.png) | D17-4 | Advance Passing Lane | 42x42 | 42x42 | — | — | — | 60x54 | Table 2D-1, manual p.208; picture: Figure 2D-26, manual p.263 |
| ![D17-5](symbols/D17-5.png) | D17-5 | Advance Emergency Turn-Out | 60x36 | 60x36 | — | — | — | 78x54 | Table 2D-1, manual p.208; picture: Figure 2D-29, manual p.266 |
| ![D17-6](symbols/D17-6.png) | D17-6 | Emergency Turn-Out (Directional) | 60x36 | 60x36 | — | — | — | 78x60 | Table 2D-1, manual p.208; picture: Figure 2D-29, manual p.266 |
| ![D17-7](symbols/D17-7.png) | D17-7 | Advance Slow Vehicle Turn-Out | 72x36 | 72x36 | — | — | — | 96x54 | Table 2D-1, manual p.208; picture: Figure 2D-29, manual p.266 |
|  | E1-1 | Interchange Advance Guide (1 destination) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E1-2 | Interchange Advance Guide (2 destinations) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E1-3 | Interchange Advance Guide (3 destinations) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E1-5P | 1-, 2-Digit Exit Number | 114x30 | 114x30 | — | — | 114x30 | — | Table 2E-1, manual p.294 |
|  | E1-5aP | LEFT | 132x30 | 132x30 | — | — | 132x30 | — | Table 2E-1, manual p.294 |
|  | E1-5bP | Left Exit Number | 138x30 | 138x30 | — | — | 138x30 | — | Table 2E-1, manual p.294 |
|  | E1-5cP | 3-Digit Exit Number (with single-letter suffix) | 156x30 | 156x30 | — | — | 156x30 | — | Table 2E-1, manual p.294 |
|  | E1-5dP | 1-, 2-Digit Exit Number (with dual-letter suffix) | 168x30 | 168x30 | — | — | 168x30 | — | Table 2E-1, manual p.294 |
|  | E1-5eP | 3-Digit Exit Number (with dual-letter suffix) | 186x30 | 186x30 | — | — | 186x30 | — | Table 2E-1, manual p.294 |
|  | E1-5fP | 1-, 2-Digit Exit Number | 114x54 | 114x54 | — | — | 114x54 | — | Table 2E-1, manual p.294 |
|  | E1-5gP | 3-Digit Exit Number | 132x54 | 132x54 | — | — | 132x54 | — | Table 2E-1, manual p.294 |
|  | E1-5hP | 1-, 2-Digit Exit Number (with single-letter suffix) | 138x54 | 138x54 | — | — | 138x54 | — | Table 2E-1, manual p.294 |
|  | E1-5iP | 3-Digit Exit Number (with single-letter suffix) | 156x54 | 156x54 | — | — | 156x54 | — | Table 2E-1, manual p.294 |
|  | E1-5jP | 1-, 2-Digit Exit Number (with dual-letter suffix) | 168x54 | 168x54 | — | — | 168x54 | — | Table 2E-1, manual p.294 |
|  | E1-5kP | 3-Digit Exit Number (with dual-letter suffix) | 186x54 | 186x54 | — | — | 186x54 | — | Table 2E-1, manual p.294 |
|  | E1-5mP | Left (plaque) | 72x30 | 72x30 | — | — | 72x30 | — | Table 2E-1, manual p.294 |
|  | E2-1P | Next Exit (1 line) (plaque) | Variesx24 | Variesx24 | — | — | Variesx24 | — | Table 2E-1, manual p.294 |
|  | E2-1aP | Next Exit (2 lines) (plaque) | Variesx36 | Variesx36 | — | — | Variesx36 | — | Table 2E-1, manual p.294 |
|  | E3-1 | Supplemental (1 destination) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E3-2 | Supplemental (2 destinations) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E4-1 | Exit Direction (1 destination) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E4-2 | Exit Direction (2 destinations) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E4-3 | Exit Direction (3 destinations) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E5-1 | Exit Gore | 72x60 | 72x60 | — | — | 72x60 | — | Table 2E-1, manual p.294 |
|  | E5-1a | Exit Gore | 156x60 | 156x60 | — | — | 156x60 | — | Table 2E-1, manual p.294 |
|  | E5-1bP | Exit Gore Number | 120x30 | 120x30 | — | — | 120x30 | — | Table 2E-1, manual p.294 |
|  | E5-1c | Narrow Exit Gore | 60x90 | 60x90 | — | — | 60x90 | — | Table 2E-1, manual p.294 |
| ![E5-2](symbols/E5-2.png) | E5-2 | Exit Open | 48x36 | 48x36 | 48x36 | 48x36 | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![E5-2a](symbols/E5-2a.png) | E5-2a | Exit Closed | 48x36 | 48x36 | 48x36 | 48x36 | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![E5-3](symbols/E5-3.png) | E5-3 | Exit Only | 48x36 | 48x36 | 48x36 | 48x36 | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
|  | E6-1 | Pull-Through | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E6-1a | Pull-Through (Destination) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E6-2 | Pull-Through (Down Arrows) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.294 |
|  | E6-2a | Pull-Through (Destination, Down Arrows) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E7-1 | Post-Interchange Distance | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E7-2 | Post-Interchange Distance | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E7-3 | Post-Interchange Distance | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E7-4 | Post-Interchange Travel Time | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E7-5 | Distance and Travel Time | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E7-6 | Comparative Travel Time | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
| ![E8-1](symbols/E8-1.png) | E8-1 | Preferential Lane Entrance Gore | — | — | 48x96 | 48x96 | — | — | Table 2G-1, manual p.408; picture: Figure 2G-6, manual p.421 |
| ![E8-1a](symbols/E8-1a.png) | E8-1a | Preferential Lane Intermediate | — | — | 48x84 | 48x84 | — | — | Table 2G-1, manual p.408; picture: Figure 2G-6, manual p.421 |
| ![E8-2](symbols/E8-2.png) | E8-2 | Preferential Lane Entrance | — | — | 228x72 | 228x72 | — | — | Table 2G-1, manual p.408; picture: Figure 2G-6, manual p.421 |
| ![E8-2a](symbols/E8-2a.png) | E8-2a | Preferential Lane Entrance | — | — | 186x108 | 186x108 | — | — | Table 2G-1, manual p.408; picture: Figure 2G-6, manual p.421 |
|  | E8-3 | Preferential Lane Entrance Advance | — | — | 186x96 | 186x96 | — | — | Table 2G-1, manual p.408 |
| ![E8-4](symbols/E8-4.png) | E8-4 | Preferential Lane Direct Exit Gore | — | — | 60x78 | 60x78 | — | — | Table 2G-1, manual p.408; picture: Figure 2G-14, manual p.431 |
|  | E8-5 | Intermediate Egress Direction | — | — | Variesx90 | Variesx90 | — | — | Table 2G-1, manual p.408 |
|  | E8-6 | AdvanceGuide | — | — | Variesx84 | Variesx84 | — | — | Table 2G-1, manual p.408 |
|  | E9-1 | Interchange Sequence (2 interchanges) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E9-2 | Interchange Sequence (3 interchanges) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E9-3 | Next Exits (1 destination) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E9-3a | Next Exits (2 destinations) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E9-4 | Community Interchanges (2 interchanges) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E9-5 | Community Interchanges (3 interchanges) | Varies | Varies | — | — | Varies | — | Table 2E-1, manual p.295 |
|  | E11-1 | Exit Only (with arrow) | 174x36 | 174x36 | — | — | 174x36 | — | Table 2E-1, manual p.295 |
|  | E11-1a | Exit | 66x18 | 66x18 | — | — | 66x18 | — | Table 2E-1, manual p.295 |
|  | E11-1b | Only | 66x18 | 66x18 | — | — | 66x18 | — | Table 2E-1, manual p.295 |
|  | E11-1c | Exit Only | 120x18 | 120x18 | — | — | 120x18 | — | Table 2E-1, manual p.295 |
|  | E11-1d | Exit Only (with arrow) | 174x36 | 174x36 | — | — | 174x36 | — | Table 2E-1, manual p.295 |
|  | E11-1e | Exit Only (with two arrows) | 222x36 | 222x36 | — | — | 222x36 | — | Table 2E-1, manual p.295 |
|  | E11-1f | Exit Only (with two arrows) | 222x36 | 222x36 | — | — | 222x36 | — | Table 2E-1, manual p.295 |
|  | E11-2 | Left (panel) | 60x18 | 60x18 | — | — | 60x18 | — | Table 2E-1, manual p.295 |
|  | E13-2 | Exit Direction Advisory Speed (panel) | 162x24 | 162x24 | — | — | 162x24 | — | Table 2E-1, manual p.295 |
| ![EM1-1](symbols/EM1-1.png) | EM1-1 | Evacuation Route | 24x24 | 24x24 | — | — | 24x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM1-1a](symbols/EM1-1a.png) | EM1-1a | Use of the specific Evacuation Route | — | — | — | — | — | — | section text; picture: Figure 2N-1, manual p.531 |
| ![EM1-2](symbols/EM1-2.png) | EM1-2 | Evacuation Route | 24x24 | 24x24 | — | — | 24x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM2-1](symbols/EM2-1.png) | EM2-1 | Area Closed | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM2-2](symbols/EM2-2.png) | EM2-2 | Traffic Control Point | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM2-3](symbols/EM2-3.png) | EM2-3 | Maintain Top Safe Speed | 24x30 | 24x30 | — | — | 24x30 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM2-4](symbols/EM2-4.png) | EM2-4 | Permit Required | 24x30 | 24x30 | — | — | 24x30 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM3-1](symbols/EM3-1.png) | EM3-1 | MEDICAL CENTER | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM3-1a](symbols/EM3-1a.png) | EM3-1a | WELFARE CENTER | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM3-1b](symbols/EM3-1b.png) | EM3-1b | REGISTRATION CENTER | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM3-1c](symbols/EM3-1c.png) | EM3-1c | DECONTAMINATION CENTER | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM4-1](symbols/EM4-1.png) | EM4-1 | EMERGENCY | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM4-1a](symbols/EM4-1a.png) | EM4-1a | HURRICANE | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM4-1b](symbols/EM4-1b.png) | EM4-1b | FALLOUT | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
| ![EM4-1c](symbols/EM4-1c.png) | EM4-1c | CHEMICAL | 30x24 | 30x24 | — | — | 30x24 | — | Table 2N-1, manual p.532; picture: Figure 2N-1, manual p.531 |
|  | EM-1a | Evacuation Route | 24x24 | 24x24 | — | — | 24x24 | — | Table 2N-1, manual p.532 |
| ![G20-1](symbols/G20-1.png) | G20-1 | Road Work Next XX Miles | 36x18 | 36x18 | 48x24 | 48x24 | — | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
| ![G20-2](symbols/G20-2.png) | G20-2 | End Road Work | 36x18 | 36x18 | 48x24 | 48x24 | — | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
| ![G20-4](symbols/G20-4.png) | G20-4 | Pilot Car Follow Me | 36x18 | 36x18 | — | — | — | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
|  | G20-5aP | Work Zone (plaque) | 24x18 | 24x18 | 30x24 | 30x24 | — | — | Table 6G-1, manual p.796 |
|  | I1-1 | Traffic Signal Speed | 24x36 | 24x36 | — | — | — | — | Table 2H-1, manual p.461 |
|  | I2-1 | Jurisdictional Boundary Signs | — | — | — | — | — | — | section text |
|  | I2-2 | Geographical Feature | Variesx36 | Variesx36 | — | — | — | — | Table 2H-1, manual p.461 |
|  | I2-3 | Grade Separation Identification | — | — | Variesx18 | Variesx18 | — | — | Table 2H-1, manual p.461 |
|  | I2-3a | Grade Separation Identification (2 lines) | — | — | Variesx24 | Variesx24 | — | — | Table 2H-1, manual p.461 |
|  | I2-4 | Future Interstate Corridor | 54x36 | 54x36 | 72x48 | 72x48 | — | — | Table 2H-1, manual p.461 |
|  | I2-4a | Future I-XX Corridor | 48x36 | 48x36 | 66x48 | 66x48 | — | — | Table 2H-1, manual p.461 |
|  | I2-5 | Project Information | 96x48 | 96x48 | 156x72 | 156x72 | — | — | Table 2H-1, manual p.461 |
|  | I3-5 | Airport | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2H-1, manual p.461 |
|  | I3-6 | Bus Station | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2H-1, manual p.461 |
|  | I3-7 | Train Station | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2H-1, manual p.461 |
|  | I3-8 | Light Rail Transit Station | 24x24 | 24x24 | — | — | — | — | Table 2H-1, manual p.461 |
|  | I3-9 | Vehicle Ferry Terminal | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2H-1, manual p.461 |
|  | I3-10 | Passenger Only Ferry Terminal | 24x24 | 24x24 | 30x30 | 30x30 | — | — | Table 2H-1, manual p.461 |
|  | I3-10P | Ferry (plaque) | 24x12 | 24x12 | 30x18 | 30x18 | — | — | Table 2H-1, manual p.461 |
|  | I4-1 | Library | 24x24 | 24x24 | — | — | — | — | Table 2H-1, manual p.461 |
|  | I4-2 | Recycling Center | 30x36 | 30x36 | — | — | — | — | Table 2H-1, manual p.461 |
|  | I13-1 | Emergency Notification | 12x9 | 12x9 | — | — | 12x9 | — | Table 8B-1, manual p.995 |
|  | I13-2 | Push to Exit | 18x9 | 18x9 | — | — | 18x9 | — | Table 8B-1, manual p.995 |
|  | I20-1 | Acknowledgment | 36x30 | 36x30 | 72x48 | 72x48 | — | — | Table 2H-1, manual p.461 |
|  | I20-2 | Acknowledgment | 36x30 | 36x30 | 72x48 | 72x48 | — | — | Table 2H-1, manual p.461 |
|  | I20-3 | Acknowledgment | 42x24 | 42x24 | 96x36 | 96x36 | — | — | Table 2H-1, manual p.461 |
|  | I20-4 | Acknowledgment - Rest Area | 56x36 | 56x36 | 72x48 | 72x48 | — | — | Table 2H-1, manual p.461 |
|  | I20-4a | Acknowledgment - Welcome Center | 56x36 | 56x36 | 72x48 | 72x48 | — | — | Table 2H-1, manual p.461 |
|  | I20-5P | Acknowledgment Signs and Plaques (I20 Series) | — | — | — | — | — | — | section text |
| ![M1-1](symbols/M1-1.png) | M1-1 | Interstate Route (1 or 2 digits) | 30x24 | 30x24 | — | — | — | 45x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-1a](symbols/M1-1a.png) | M1-1a | Interstate Route (1 or 2 digits) | 30x24 | 30x24 | — | — | — | 45x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-2](symbols/M1-2.png) | M1-2 | Loop | 30x24 | 30x24 | — | — | — | 45x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-3](symbols/M1-3.png) | M1-3 | Spur | 30x24 | 30x24 | — | — | — | 45x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-4](symbols/M1-4.png) | M1-4 | U.S. Route (1 or 2 digits) | 30x24 | 30x24 | — | — | — | 45x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-5](symbols/M1-5.png) | M1-5 | State Route (1 or 2 digits) | 30x24 | 30x24 | — | — | — | 45x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-6](symbols/M1-6.png) | M1-6 | County Route | 24x24 | 24x24 | — | — | — | 36x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-7](symbols/M1-7.png) | M1-7 | Forest Route | 24x24 | 24x24 | — | — | 18x18 | 36x36 | Table 2D-1, manual p.207; picture: Figure 2D-4, manual p.217 |
| ![M1-8](symbols/M1-8.png) | M1-8 | State or Local Bicycle Route | 18x24 | 18x24 | — | — | 12x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![M1-8a](symbols/M1-8a.png) | M1-8a | State or Local Bicycle Route | 18x24 | 18x24 | — | — | 12x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![M1-8b](symbols/M1-8b.png) | M1-8b | Non-Numbered Bicycle Route | 18x18 | 18x18 | — | — | 12x12 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![M1-8c](symbols/M1-8c.png) | M1-8c | Non-Numbered Bicycle Route | 18x18 | 18x18 | — | — | 12x12 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
| ![M1-9](symbols/M1-9.png) | M1-9 | U.S. Bicycle Route | 18x24 | 18x24 | — | — | 12x18 | — | Table 9A-1, manual p.1051; picture: Figure 9D-1, manual p.1072 |
|  | M1-10 | Eisenhower Interstate System | 36x36 | 36x36 | — | — | 36x36 | — | Table 2E-1, manual p.295 |
|  | M1-10a | Eisenhower Interstate System | 36x36 | 36x36 | — | — | 36x36 | — | Table 2E-1, manual p.295 |
| ![M2-1P](symbols/M2-1P.png) | M2-1P | Junction (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M2-2](symbols/M2-2.png) | M2-2 | Combination Junction (2 route signs) | 60x48 | 60x48 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M3-1P](symbols/M3-1P.png) | M3-1P | Cardinal Direction (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M3-2P](symbols/M3-2P.png) | M3-2P | Cardinal Direction (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M3-3P](symbols/M3-3P.png) | M3-3P | Cardinal Direction (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M3-4P](symbols/M3-4P.png) | M3-4P | Cardinal Direction (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-1P](symbols/M4-1P.png) | M4-1P | Alternate (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-1aP](symbols/M4-1aP.png) | M4-1aP | Alternate (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-2P](symbols/M4-2P.png) | M4-2P | By-Pass (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-3P](symbols/M4-3P.png) | M4-3P | Business (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-4P](symbols/M4-4P.png) | M4-4P | Truck (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-5P](symbols/M4-5P.png) | M4-5P | To (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-6P](symbols/M4-6P.png) | M4-6P | End (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-7P](symbols/M4-7P.png) | M4-7P | Temporary (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-7aP](symbols/M4-7aP.png) | M4-7aP | Temporary (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
| ![M4-8P](symbols/M4-8P.png) | M4-8P | Bicycle Route Auxiliary Signs (plaque) | 12x6 | 12x6 | — | — | 12x6 | — | Table 9A-1, manual p.1051; picture: Figure 6I-1, manual p.812 |
| ![M4-8a](symbols/M4-8a.png) | M4-8a | End Detour | 24x18 | 24x18 | 24x18 | 24x18 | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-8bP](symbols/M4-8bP.png) | M4-8bP | End (plaque) | 24x12 | 24x12 | 24x12 | 24x12 | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-9](symbols/M4-9.png) | M4-9 | Detour | 30x24 | 30x24 | 48x36 | 48x36 | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-9a](symbols/M4-9a.png) | M4-9a | Bike/Pedestrian Detour | 30x24 | 30x24 | — | — | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-9b](symbols/M4-9b.png) | M4-9b | Pedestrian Detour | 30x24 | 30x24 | — | — | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-9c](symbols/M4-9c.png) | M4-9c | Bike Detour (with arrow) | 30x24 | 30x24 | — | — | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-10](symbols/M4-10.png) | M4-10 | Detour | 48x18 | 48x18 | — | — | — | — | Table 6I-1, manual p.811; picture: Figure 6I-1, manual p.812 |
| ![M4-11](symbols/M4-11.png) | M4-11 | Emergency Route | 30x30 | 30x30 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-37, manual p.280 |
|  | M4-11a | Emergency Route | 30x30 | 30x30 | — | — | — | — | Table 2D-1, manual p.207 |
| ![M4-11bP](symbols/M4-11bP.png) | M4-11bP | Emergency Route To (plaque) | 30x18 | 30x18 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-37, manual p.280 |
| ![M4-11cP](symbols/M4-11cP.png) | M4-11cP | Emergency Route To (plaque) | 30x18 | 30x18 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-37, manual p.280 |
| ![M4-12](symbols/M4-12.png) | M4-12 | End Emergency Route | 24x18 | 24x18 | — | — | — | — | Table 2D-1, manual p.207; picture: Figure 2D-37, manual p.280 |
| ![M4-14P](symbols/M4-14P.png) | M4-14P | Begin (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2D-1, manual p.207; picture: Figure 2D-5, manual p.219 |
|  | M4-17 | Toll Collector | — | — | 48x48 | 48x48 | — | — | Table 2F-1, manual p.381 |
|  | M4-18 | Exact Change | — | — | 48x48 | 48x48 | — | — | Table 2F-1, manual p.381 |
| ![M5-1P](symbols/M5-1P.png) | M5-1P | Advance Turn Arrow Auxiliary Plaques | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M5-2P](symbols/M5-2P.png) | M5-2P | Advance Turn Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M5-3P](symbols/M5-3P.png) | M5-3P | Circular Intersection Advance Turn Arrow | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M5-4P](symbols/M5-4P.png) | M5-4P | Lane Designation Auxiliary Plaques | 24x18 | 24x18 | — | — | — | 36x24 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M5-5P](symbols/M5-5P.png) | M5-5P | Lane Designation (plaque) | 24x18 | 24x18 | — | — | — | 36x24 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M5-6P](symbols/M5-6P.png) | M5-6P | Lane Designation (plaque) | 24x18 | 24x18 | — | — | — | 36x24 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-1P](symbols/M6-1P.png) | M6-1P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-2P](symbols/M6-2P.png) | M6-2P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-2aP](symbols/M6-2aP.png) | M6-2aP | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-3P](symbols/M6-3P.png) | M6-3P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-4P](symbols/M6-4P.png) | M6-4P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-5P](symbols/M6-5P.png) | M6-5P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-6P](symbols/M6-6P.png) | M6-6P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
| ![M6-7P](symbols/M6-7P.png) | M6-7P | Directional Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2D-1, manual p.207; picture: Figure 2D-6, manual p.222 |
|  | M10-1 | National Scenic Byway | 24x24 | 24x24 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M10-1aP | National Scenic Byway (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M10-2 | Byway Identification | 24x24 | 24x24 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M10-2aP | Byway Identification (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M10-3 | State Scenic Byway System | 24x24 | 24x24 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M10-3a | State Scenic Byway - Simple Graphic and Byway | 24x24 | 24x24 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M10-3bP | Scenic Byway (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M11-1 | National Historic Trail - Identification | 24x24 | 24x24 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M11-1aP | National Historic Trail - Historic Route (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M11-1bP | National Historic Trail - Crossing (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M11-1cP | National Historic Trail - Auto Tour Route (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
|  | M11-1dP | National Historic Trail - Distance (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2D-1, manual p.207 |
| ![OM1-1](symbols/OM1-1.png) | OM1-1 | Object Marker Design and Placement Height | — | — | — | — | — | — | section text; picture: Figure 2C-17, manual p.199 |
| ![OM1-2](symbols/OM1-2.png) | OM1-2 | Object Marker Design and Placement Height | — | — | — | — | — | — | section text; picture: Figure 2C-17, manual p.199 |
| ![OM1-3](symbols/OM1-3.png) | OM1-3 | Object Marker Design and Placement Height | — | — | — | — | — | — | section text; picture: Figure 2C-17, manual p.199 |
| ![OM4-1](symbols/OM4-1.png) | OM4-1 | Object Marker Design and Placement Height | — | — | — | — | — | — | section text; picture: Figure 2C-17, manual p.199 |
| ![OM4-2](symbols/OM4-2.png) | OM4-2 | Object Marker Design and Placement Height | — | — | — | — | — | — | section text; picture: Figure 2C-17, manual p.199 |
| ![OM4-3](symbols/OM4-3.png) | OM4-3 | Object Marker Design and Placement Height | — | — | — | — | — | — | section text; picture: Figure 2C-17, manual p.199 |
|  | OM3-C | Object Marker Type 3 | 12x36 | 12x36 | — | — | 6x18 | — | Table 9A-1, manual p.1050 |
|  | OM3-L | Object Marker Type 3 | 12x36 | 12x36 | — | — | 6x18 | — | Table 9A-1, manual p.1050 |
|  | OM3-R | Object Marker Type 3 | 12x36 | 12x36 | — | — | 6x18 | — | Table 9A-1, manual p.1050 |
| ![R1-2aP](symbols/R1-2aP.png) | R1-2aP | To Oncoming Traffic (plaque) | 24x18 | 24x18 | 36x30 | 48x36 | 24x18 | — | Table 2B-1, manual p.68; picture: Figure 6G-1, manual p.794 |
| ![R1-2bP](symbols/R1-2bP.png) | R1-2bP | To Traffic in Circle (plaque) | 24x15 | 24x15 | — | — | 24x15 | 36x24 | Table 2B-1, manual p.68; picture: Figure 2B-1, manual p.74 |
| ![R1-2cP](symbols/R1-2cP.png) | R1-2cP | To All Lanes (plaque) | 24x15 | 24x15 | — | — | 24x15 | 36x24 | Table 2B-1, manual p.68; picture: Figure 2B-1, manual p.74 |
| ![R1-5](symbols/R1-5.png) | R1-5 | Yield Here to Pedestrians | — | 36x36 | — | — | — | 36x36 | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
|  | R1-5a | Yield Here toSchool Crossings | 36x36 | 36x36 | — | — | — | — | Table 7B-1, manual p.971 |
| ![R1-5b](symbols/R1-5b.png) | R1-5b | Stop Here for Pedestrians | — | 36x36 | — | — | — | 36x36 | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-5c](symbols/R1-5c.png) | R1-5c | Stop Here for School Crossing | 36x36 | 36x36 | — | — | — | — | Table 7B-1, manual p.971; picture: Figure 7B-1, manual p.974 |
| ![R1-5d](symbols/R1-5d.png) | R1-5d | Yield Here to Trail Crossings | — | 36x42 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-5e](symbols/R1-5e.png) | R1-5e | StopHere for Trail Crossing | — | 36x42 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-6](symbols/R1-6.png) | R1-6 | In-Street Pedestrian Crossing - | 12x36 | 12x36 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-6a](symbols/R1-6a.png) | R1-6a | In-Street Pedestrian Crossing - | 12x36 | 12x36 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-6b](symbols/R1-6b.png) | R1-6b | School Crossing | — | — | — | — | — | — | section text; picture: Figure 7B-1, manual p.974 |
| ![R1-6c](symbols/R1-6c.png) | R1-6c | In-Street and Overhead Pedestrian and Trail Crossing Signs (R1-6 and R1-9 Series) | — | — | — | — | — | — | section text; picture: Figure 7B-1, manual p.974 |
| ![R1-6d](symbols/R1-6d.png) | R1-6d | In-Street Trail Crossing - | 12x36 | 12x36 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-6e](symbols/R1-6e.png) | R1-6e | In-Street Trail Crossing - | 12x36 | 12x36 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-7](symbols/R1-7.png) | R1-7 | Wait on Stop | 24x30 | 24x30 | 24x30 | 24x30 | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.794 |
| ![R1-7a](symbols/R1-7a.png) | R1-7a | Wait on Stop - Go on Slow | 30x36 | 30x36 | 30x36 | 30x36 | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.794 |
| ![R1-8](symbols/R1-8.png) | R1-8 | Go on Slow | 24x30 | 24x30 | 24x30 | 24x30 | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.794 |
| ![R1-9](symbols/R1-9.png) | R1-9 | Overhead Pedestrian Crossing - | 90x24 | 90x24 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-9a](symbols/R1-9a.png) | R1-9a | Overhead Pedestrian Crossing - | 90x24 | 90x24 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-9b](symbols/R1-9b.png) | R1-9b | Overhead School Crossing | 90x24 | 90x24 | — | — | — | — | Table 7B-1, manual p.971; picture: Figure 7B-1, manual p.974 |
| ![R1-9c](symbols/R1-9c.png) | R1-9c | Overhead School Crossing | 90x24 | 90x24 | — | — | — | — | Table 7B-1, manual p.971; picture: Figure 7B-1, manual p.974 |
| ![R1-9d](symbols/R1-9d.png) | R1-9d | Overhead Trail Crossing | 72x24 | 72x24 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-9e](symbols/R1-9e.png) | R1-9e | Overhead Trail Crossing | 72x24 | 72x24 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-2, manual p.82 |
| ![R1-10P](symbols/R1-10P.png) | R1-10P | Except Right Turn (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2B-1, manual p.68; picture: Figure 2B-1, manual p.74 |
| ![R2-2P](symbols/R2-2P.png) | R2-2P | Truck Speed Limit (plaque) | 24x24 | 24x24 | 36x36 | 48x48 | — | 36x36 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-2aP](symbols/R2-2aP.png) | R2-2aP | Bus Speed Limit (plaque) | 24x24 | 24x24 | 36x36 | 48x48 | — | 36x36 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-2bP](symbols/R2-2bP.png) | R2-2bP | Truck-Bus Speed Limit (plaque) | 24x30 | 24x30 | 36x42 | 48x54 | — | 36x42 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-2cP](symbols/R2-2cP.png) | R2-2cP | Vehicles Over X Tons Speed | 24x30 | 24x30 | 36x42 | 48x54 | — | 36x42 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-3P](symbols/R2-3P.png) | R2-3P | Night Speed Limit (plaque) | 24x24 | 24x24 | 36x36 | 48x48 | — | 36x36 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-4P](symbols/R2-4P.png) | R2-4P | Minimum Speed Limit (plaque) | 24x24 | 24x24 | 36x36 | 48x48 | — | 36x36 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-4a](symbols/R2-4a.png) | R2-4a | Combined Maximum and Minimum | 24x48 | 24x48 | 36x72 | 48x96 | — | 36x72 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-5P](symbols/R2-5P.png) | R2-5P | Unless Otherwise Posted (plaque) | 24x18 | 24x18 | 36x24 | 36x24 | — | 36x24 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-5aP](symbols/R2-5aP.png) | R2-5aP | Citywide (plaque) | 24x6 | 24x6 | — | — | — | 30x9 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-5bP](symbols/R2-5bP.png) | R2-5bP | Neighborhood (plaque) | 24x6 | 24x6 | — | — | — | 30x9 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-5cP](symbols/R2-5cP.png) | R2-5cP | Residential (plaque) | 24x6 | 24x6 | — | — | — | 30x9 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-6P](symbols/R2-6P.png) | R2-6P | Fines Higher (plaque) | 24x18 | 24x18 | 36x24 | 48x36 | — | 36x24 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-6aP](symbols/R2-6aP.png) | R2-6aP | Fines Double (plaque) | 24x18 | 24x18 | 36x24 | 48x36 | — | 36x24 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-6bP](symbols/R2-6bP.png) | R2-6bP | $XX Fine (plaque) | 24x18 | 24x18 | 36x24 | 48x36 | — | 36x24 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-10](symbols/R2-10.png) | R2-10 | Begin Higher Fines Zone | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-11](symbols/R2-11.png) | R2-11 | End Higher Fines Zone | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-12](symbols/R2-12.png) | R2-12 | End Work Zone Speed Limit | 24x36 | 24x36 | 36x54 | 36x54 | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.794 |
| ![R2-13](symbols/R2-13.png) | R2-13 | End Variable Speed Limit | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R2-14](symbols/R2-14.png) | R2-14 | End Truck Speed Limit | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.68; picture: Figure 2B-3, manual p.86 |
| ![R3-1](symbols/R3-1.png) | R3-1 | No Right Turn | 24x24 | 36x36 | 36x36 | — | — | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
|  | R3-1a | No Right Turn - Train (symbol) | 24x30 | 30x36 | — | — | — | — | Table 8B-1, manual p.994 |
| ![R3-1b](symbols/R3-1b.png) | R3-1b | Movement Prohibition - | 24x36 | 24x36 | 36x54 | 36x54 | — | — | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
|  | R3-1c | Movement Prohibition - | 24x42 | 24x42 | 36x60 | 36x60 | — | — | Table 2B-1, manual p.68 |
| ![R3-1d](symbols/R3-1d.png) | R3-1d | Movement Prohibition - | 24x48 | 24x48 | 36x66 | 36x66 | — | — | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
| ![R3-1e](symbols/R3-1e.png) | R3-1e | Movement Prohibition - | 24x36 | 24x36 | 36x54 | 36x54 | — | — | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
| ![R3-1f](symbols/R3-1f.png) | R3-1f | Movement Prohibition - | 24x42 | 24x42 | 36x66 | 36x66 | — | — | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
| ![R3-1g](symbols/R3-1g.png) | R3-1g | Movement Prohibition - | 24x36 | 24x36 | 36x54 | 36x54 | — | — | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
|  | R3-1h | Movement Prohibition - | 24x42 | 24x42 | 36x66 | 36x66 | — | — | Table 2B-1, manual p.69 |
| ![R3-2](symbols/R3-2.png) | R3-2 | No Left Turn | 24x24 | 36x36 | 36x36 | — | — | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
| ![R3-2a](symbols/R3-2a.png) | R3-2a | No Left Turn - Train (symbol) | 24x30 | 30x36 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R3-3](symbols/R3-3.png) | R3-3 | NO TURNS | 24x24 | 36x36 | 36x36 | — | — | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
| ![R3-4](symbols/R3-4.png) | R3-4 | No U-Turn | 24x24 | 36x36 | 36x36 | — | — | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.90 |
| ![R3-5](symbols/R3-5.png) | R3-5 | Mandatory Movement Lane Control Signs | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5a](symbols/R3-5a.png) | R3-5a | Mandatory Movement Lane Control | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5bP](symbols/R3-5bP.png) | R3-5bP | Left Lane (plaque) | 30x12 | 30x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5cP](symbols/R3-5cP.png) | R3-5cP | HOV 2+ (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5dP](symbols/R3-5dP.png) | R3-5dP | Taxi Lane (plaque) | 30x12 | 30x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5fP](symbols/R3-5fP.png) | R3-5fP | Right Lane (plaque) | 30x12 | 30x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5gP](symbols/R3-5gP.png) | R3-5gP | Bus Lane (plaque) | 30x12 | 30x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-5hP](symbols/R3-5hP.png) | R3-5hP | Bike Lane (plaque) | 30x12 | 30x12 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R3-6](symbols/R3-6.png) | R3-6 | Optional Movement Lane Control | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-6a](symbols/R3-6a.png) | R3-6a | Optional Movement U and Left Turn | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-6b](symbols/R3-6b.png) | R3-6b | Optional Movement Left Turns | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-7](symbols/R3-7.png) | R3-7 | Right (Left) Lane Must Turn | 30x30 | 36x36 | 48x48 | — | — | 48x48 | Table 2B-1, manual p.69; picture: Figure 6G-1, manual p.794 |
| ![R3-7aP](symbols/R3-7aP.png) | R3-7aP | Except Buses (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-7bP](symbols/R3-7bP.png) | R3-7bP | Except Bicycles (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-8](symbols/R3-8.png) | R3-8 | Advance Intersection Lane Control | — | — | — | Variesx36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-8a](symbols/R3-8a.png) | R3-8a |  | — | — | — | Variesx36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-8b](symbols/R3-8b.png) | R3-8b |  | — | — | — | Variesx36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
|  | R3-8x | Advance Intersection Lane Control with Bike Lane | Variesx36 | Variesx36 | — | — | — | — | Table 9A-1, manual p.1049 |
| ![R3-8xa](symbols/R3-8xa.png) | R3-8xa |  | — | — | — | Variesx36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-8xb](symbols/R3-8xb.png) | R3-8xb |  | — | — | — | Variesx36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-8xc](symbols/R3-8xc.png) | R3-8xc |  | — | — | — | Variesx36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.90 |
| ![R3-9a](symbols/R3-9a.png) | R3-9a | Two-Way Left Turn Only (overhead) | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9b](symbols/R3-9b.png) | R3-9b | Two-Way Left Turn Only | 24x36 | 24x36 | — | — | — | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9cP](symbols/R3-9cP.png) | R3-9cP | Begin (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9dP](symbols/R3-9dP.png) | R3-9dP | End (plaque) | 24x12 | 24x12 | — | — | — | 36x18 | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9e](symbols/R3-9e.png) | R3-9e | Reversible Lane Control (overhead) | 108x48 | 108x48 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9f](symbols/R3-9f.png) | R3-9f | Reversible Lane Control | 30x42 | 36x54 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9g](symbols/R3-9g.png) | R3-9g | Advance Reversible Lane Control | 108x36 | 108x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9h](symbols/R3-9h.png) | R3-9h | Advance Reversible Lane Control | 108x36 | 108x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-9i](symbols/R3-9i.png) | R3-9i | End Reverse Lane | 108x48 | 108x48 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-6, manual p.95 |
| ![R3-10](symbols/R3-10.png) | R3-10 | Vehicle Occupancy Definition | 30x42 | 30x42 | 36x60 | 78x96 | — | 78x96 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-10a](symbols/R3-10a.png) | R3-10a | ILEV | 30x42 | 30x42 | 36x60 | 78x96 | — | 78x96 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-11](symbols/R3-11.png) | R3-11 | Preferential Lane Operation Signs | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-11a](symbols/R3-11a.png) | R3-11a | Preferential Lane Operation | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-11b](symbols/R3-11b.png) | R3-11b | Preferential Lane Operation | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
|  | R3-11c | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text |
| ![R3-11d](symbols/R3-11d.png) | R3-11d | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-11e](symbols/R3-11e.png) | R3-11e | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-11f](symbols/R3-11f.png) | R3-11f | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-11g](symbols/R3-11g.png) | R3-11g | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-11hP](symbols/R3-11hP.png) | R3-11hP | Motorcycles Allowed (plaque) | 30x15 | 30x15 | 36x18 | 78x36 | — | 78x36 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-12](symbols/R3-12.png) | R3-12 | Preferential Lane Advance Signs | 30x42 | 30x42 | 36x60 | 48x84 | — | 48x84 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-12a](symbols/R3-12a.png) | R3-12a | Preferential Lane Ends Signs | 30x42 | 30x42 | 36x60 | 48x84 | — | 48x84 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-12b](symbols/R3-12b.png) | R3-12b | High-Occupancy Vehicles | 30x42 | 30x42 | 36x60 | 48x84 | — | 48x84 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-12c](symbols/R3-12c.png) | R3-12c | Preferential Lane Ends | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-12d](symbols/R3-12d.png) | R3-12d | A post-mounted Preferential Lane Ends | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-12e](symbols/R3-12e.png) | R3-12e | The Preferential Lane Advance | — | — | — | — | — | — | section text; picture: Figure 2G-1, manual p.410 |
| ![R3-12f](symbols/R3-12f.png) | R3-12f | Preferential Lane Ahead or Ends | 30x36 | 30x36 | 36x48 | 48x60 | — | 48x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-12g](symbols/R3-12g.png) | R3-12g | Preferential Lane Ahead or Ends | 30x36 | 30x36 | 36x48 | 48x60 | — | 48x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-12h](symbols/R3-12h.png) | R3-12h | Preferential Lane Ends | 36x48 | 36x48 | 48x66 | 60x84 | — | 60x84 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.410 |
| ![R3-13](symbols/R3-13.png) | R3-13 | Preferential Lane Vehicle | 66x36 | 66x36 | 84x48 | 144x78 | — | 144x78 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
|  | R3-13a | Preferential Lane Vehicle | 66x36 | 66x36 | 84x48 | 144x78 | — | 144x78 | Table 2G-1, manual p.407 |
| ![R3-14](symbols/R3-14.png) | R3-14 | HOV Lane Operation (overhead) | 72x60 | 72x60 | 96x72 | 144x108 | — | 144x108 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-14a](symbols/R3-14a.png) | R3-14a | HOV Lane Operation (overhead) | 72x60 | 72x60 | 96x72 | 144x108 | — | 144x108 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-14b](symbols/R3-14b.png) | R3-14b | HOV Lane Operation | 72x60 | 72x60 | 96x72 | 120x96 | — | 120x96 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-14c](symbols/R3-14c.png) | R3-14c | Preferential Lane Operation | 90x60 | 90x60 | 108x72 | 156x102 | — | 156x102 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
|  | R3-14d | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text |
|  | R3-14e | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text |
|  | R3-14f | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text |
|  | R3-14g | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | — | — | — | — | — | — | section text |
| ![R3-15](symbols/R3-15.png) | R3-15 | HOV Lane Ahead (overhead) | 66x36 | 66x36 | 84x48 | 102x60 | — | 102x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-15a](symbols/R3-15a.png) | R3-15a | HOV Lane Begins XX Miles | 78x48 | 114x72 | 144x84 | 150x108 | — | 150x108 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-15b](symbols/R3-15b.png) | R3-15b | HOV Lane Ends (overhead) | 66x36 | 66x36 | 84x48 | 102x60 | — | 102x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-15c](symbols/R3-15c.png) | R3-15c | Preferential Lane Ends | 66x36 | 66x36 | 84x48 | 102x60 | — | 102x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-15d](symbols/R3-15d.png) | R3-15d | Preferential Lane Ahead or Ends | 42x36 | 42x36 | 54x48 | 72x60 | — | 72x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-15e](symbols/R3-15e.png) | R3-15e | Preferential Lane Ahead or Ends | 42x36 | 42x36 | 54x48 | 72x60 | — | 72x60 | Table 2G-1, manual p.407; picture: Figure 2G-1, manual p.411 |
| ![R3-17](symbols/R3-17.png) | R3-17 | Bike Lane | 24x18 | 24x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R3-17aP](symbols/R3-17aP.png) | R3-17aP | Ahead, Ends (plaques) | 24x9 | 24x9 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R3-17bP](symbols/R3-17bP.png) | R3-17bP | Ahead, Ends (plaques) | 24x9 | 24x9 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R3-18](symbols/R3-18.png) | R3-18 | No U or Left Turn | 24x24 | 36x36 | 36x36 | — | — | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.91 |
| ![R3-19](symbols/R3-19.png) | R3-19 | Lane For Left Turn Only | 30x24 | 30x24 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.91 |
| ![R3-19a](symbols/R3-19a.png) | R3-19a | Lane for U Turn Only | 30x24 | 30x24 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.91 |
| ![R3-19b](symbols/R3-19b.png) | R3-19b | Lane For U and Left Turns Only | 30x30 | 30x30 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.91 |
|  | R3-20 | Begin Right (Left) Turn Lane | 24x36 | 24x36 | — | — | — | — | Table 2B-1, manual p.69 |
| ![R3-23](symbols/R3-23.png) | R3-23 | Jughandle Signs | 60x36 | 60x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-23a](symbols/R3-23a.png) | R3-23a | U TURN FROM RIGHT LANE | 60x36 | 60x36 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-24](symbols/R3-24.png) | R3-24 |  | — | — | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-24a](symbols/R3-24a.png) | R3-24a | U-Turns and Left Turns Directional | 60x24 | 60x24 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-24b](symbols/R3-24b.png) | R3-24b |  | — | — | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-25](symbols/R3-25.png) | R3-25 |  | — | — | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
|  | R3-25a | U-Turns and Left Turns Directional | 60x24 | 60x24 | — | — | — | — | Table 2B-1, manual p.69 |
| ![R3-25b](symbols/R3-25b.png) | R3-25b |  | — | — | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-26](symbols/R3-26.png) | R3-26 | U-Turns and Left Turns Directional | 60x24 | 60x24 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-26a](symbols/R3-26a.png) | R3-26a |  | — | — | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-8, manual p.98 |
| ![R3-27](symbols/R3-27.png) | R3-27 | No Straight Through | 24x24 | 36x36 | 36x36 | — | — | 48x48 | Table 2B-1, manual p.68; picture: Figure 2B-4, manual p.91 |
| ![R3-28](symbols/R3-28.png) | R3-28 | Toll Rate | — | — | 114x48 | 114x48 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-2, manual p.383 |
| ![R3-29P](symbols/R3-29P.png) | R3-29P | Pay Toll (plaque) | — | — | 24x18 | 24x18 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-2, manual p.383 |
| ![R3-30P](symbols/R3-30P.png) | R3-30P | Take Ticket (plaque) | — | — | 24x18 | 24x18 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-2, manual p.383 |
|  | R3-31 | ETC Account-Only | 24x24 | 24x24 | 36x36 | 36x36 | 24x24 | 36x36 | Table 2F-1, manual p.381 |
|  | R3-32P | No Cash (plaque) | 24x12 | 24x12 | 36x18 | 36x18 | 24x12 | 36x18 | Table 2F-1, manual p.381 |
| ![R3-33](symbols/R3-33.png) | R3-33 | Right (Left) Lane Must Exit | — | — | 78x36 | 78x36 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.91 |
| ![R3-33a](symbols/R3-33a.png) | R3-33a | Right (Left) Lane Must Exit | — | — | 42x60 | 42x60 | — | — | Table 2B-1, manual p.69; picture: Figure 2B-4, manual p.91 |
| ![R3-40](symbols/R3-40.png) | R3-40 | Occupancy Definition | — | — | 54x66 | 54x66 | — | 66x78 | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-42](symbols/R3-42.png) | R3-42 | Priced Managed Lane Ends | — | — | 48x60 | 48x60 | — | 60x78 | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-42a](symbols/R3-42a.png) | R3-42a | Priced Managed Lane Ends | — | — | 48x66 | 48x66 | — | 60x84 | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-42b](symbols/R3-42b.png) | R3-42b | Restriction Ends | — | — | 48x60 | 48x60 | — | 60x78 | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-42c](symbols/R3-42c.png) | R3-42c | Restriction Ends | — | — | 48x66 | 48x66 | — | 60x84 | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-43](symbols/R3-43.png) | R3-43 | Priced Managed Lane Vehicle | — | — | 138x66 | 138x66 | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-44](symbols/R3-44.png) | R3-44 | Priced Managed Lane Operation | — | — | 90x84 | 90x84 | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-44a](symbols/R3-44a.png) | R3-44a | Priced Managed Lane Operation | — | — | 132x84 | 132x84 | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
|  | R3-44b | Priced Managed Lane Operation | — | — | 90x72 | 90x72 | — | — | Table 2G-1, manual p.407 |
| ![R3-45](symbols/R3-45.png) | R3-45 | Priced Managed Lane Ends | — | — | 90x66 | 90x66 | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-45a](symbols/R3-45a.png) | R3-45a | Priced Managed Lane | — | — | 114x66 | 114x66 | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-48](symbols/R3-48.png) | R3-48 | Priced Managed Lane Toll Rate | — | — | Varies | Varies | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
| ![R3-48a](symbols/R3-48a.png) | R3-48a | Priced Managed Lane Toll Rate | — | — | Varies | Varies | — | — | Table 2G-1, manual p.407; picture: Figure 2G-18, manual p.436 |
|  | R3-51 | Part-Time Travel on | — | — | 66x78 | 66x78 | — | — | Table 2G-1, manual p.407 |
|  | R3-51aP | No Trucks (plaque) | — | — | 66x12 | 66x12 | — | — | Table 2G-1, manual p.407 |
|  | R3-51bP | No Trucks or Buses (plaque) | — | — | 66x24 | 66x24 | — | — | Table 2G-1, manual p.407 |
|  | R3-51cP | Emergency Stopping Only | — | — | 54x42 | 54x42 | — | — | Table 2G-1, manual p.407 |
|  | R3-51d | Part-Time Travel on Shoulder Variable Operation | — | — | 66x84 | 66x84 | — | — | Table 2G-1, manual p.408 |
|  | R3-51e | TRAVEL ON SHOULDER ON GREEN ARROW ONLY | — | — | 66x84 | 66x84 | — | — | Table 2G-1, manual p.408 |
|  | R3-52 | Part-Time Travel on Shoulder Ends | — | — | 66x72 | 66x72 | — | — | Table 2G-1, manual p.408 |
|  | R3-52a | TRAVEL ON SHOULDERENDS | — | — | 66x72 | 66x72 | — | — | Table 2G-1, manual p.408 |
|  | R3-52b | Shoulder Must Exit Advance | — | — | 66x72 | 66x72 | — | — | Table 2G-1, manual p.408 |
|  | R3-52c | MILE | — | — | 66x72 | 66x72 | — | — | Table 2G-1, manual p.408 |
|  | R3-56 | Begin Exit Lane | — | — | 48x72 | 48x72 | — | — | Table 2G-1, manual p.408 |
|  | R3-57P | To Traffic on Shoulder (plaque) | — | — | 36x18 | 36x18 | — | — | Table 2G-1, manual p.408 |
| ![R4-1](symbols/R4-1.png) | R4-1 | Do Not Pass | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-2](symbols/R4-2.png) | R4-2 | Pass With Care | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-3](symbols/R4-3.png) | R4-3 | Slower Traffic Keep Right | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-4](symbols/R4-4.png) | R4-4 | Begin Right Turn Lane Yield to Bikes | 36x30 | 36x30 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R4-5](symbols/R4-5.png) | R4-5 | Trucks Use Right Lane | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-7a](symbols/R4-7a.png) | R4-7a | Keep Right | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-7b](symbols/R4-7b.png) | R4-7b | Keep Right | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-7c](symbols/R4-7c.png) | R4-7c | Narrow Keep Right | 18x30 | 18x30 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-8](symbols/R4-8.png) | R4-8 | Keep Left | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-8a](symbols/R4-8a.png) | R4-8a | Keep Left | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-8b](symbols/R4-8b.png) | R4-8b | Keep Left | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-8c](symbols/R4-8c.png) | R4-8c | Narrow Keep Left | 18x30 | 18x30 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-9](symbols/R4-9.png) | R4-9 | Stay in Lane | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-9a](symbols/R4-9a.png) | R4-9a | Stay In Lane To Merge Point | 36x48 | 36x48 | 36x48 | 36x48 | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.794 |
| ![R4-10](symbols/R4-10.png) | R4-10 | Runaway Vehicles Only | 48x48 | 48x48 | — | — | — | — | Table 2B-1, manual p.69; picture: Figure 2B-10, manual p.103 |
| ![R4-12](symbols/R4-12.png) | R4-12 | More Following Vehicles Must | 42x24 | 42x24 | — | — | — | 72x42 | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-13](symbols/R4-13.png) | R4-13 | Slow Vehicles Must Use | 42x24 | 42x24 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-14](symbols/R4-14.png) | R4-14 | Slow Vehicles Must Turn Out | 30x42 | 30x42 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-16](symbols/R4-16.png) | R4-16 | Keep Right Except to Pass | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-17](symbols/R4-17.png) | R4-17 | Do Not Drive on Shoulder | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-18](symbols/R4-18.png) | R4-18 | Do Not Pass on Shoulder | 24x30 | 24x30 | 36x48 | 48x60 | 18x24 | 36x48 | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-19](symbols/R4-19.png) | R4-19 | Bicycle Passing Clearance | 30x30 | 30x30 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R4-20](symbols/R4-20.png) | R4-20 | All Traffic | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
| ![R4-21](symbols/R4-21.png) | R4-21 | Right (Left) Turn Only | 24x30 | 24x30 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-10, manual p.103 |
|  | R5-1b | Bicycle Wrong Way | 12x18 | 12x18 | — | — | 12x18 | — | Table 9A-1, manual p.1049 |
| ![R5-2](symbols/R5-2.png) | R5-2 | No Trucks | 24x24 | 24x24 | 30x30 | 36x36 | — | 36x36 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-2aP](symbols/R5-2aP.png) | R5-2aP | Except Local Deliveries (plaque) | 24x12 | 24x12 | 30x15 | 36x18 | — | 36x18 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-2b](symbols/R5-2b.png) | R5-2b | No Thru Trucks | 24x30 | 24x30 | 30x36 | 36x48 | — | 36x48 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-3](symbols/R5-3.png) | R5-3 | No Motor Vehicles | 24x24 | 24x24 | — | — | 24x24 | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-4](symbols/R5-4.png) | R5-4 | No Commercial Vehicles | 24x30 | 24x30 | 36x48 | 36x48 | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-5](symbols/R5-5.png) | R5-5 | No Vehicles with Lugs | 24x30 | 24x30 | 36x48 | 48x60 | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-6](symbols/R5-6.png) | R5-6 | No Bicycles | 24x24 | 24x24 | 30x30 | 36x36 | 24x24 | 48x48 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-7](symbols/R5-7.png) | R5-7 | No Non-Motorized Traffic | 30x24 | 30x24 | 42x24 | 48x30 | — | 42x24 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-8](symbols/R5-8.png) | R5-8 | No Motor-Driven Cycles | 30x24 | 30x24 | 42x24 | 48x30 | — | 42x24 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-10](symbols/R5-10.png) | R5-10 | No Pedestrians, Bicycles, | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-10a](symbols/R5-10a.png) | R5-10a | No Pedestrians, Bicycles, | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-10b](symbols/R5-10b.png) | R5-10b | No Pedestrians or Bicycles | 30x18 | 30x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-10c](symbols/R5-10c.png) | R5-10c | No Pedestrians | 24x12 | 24x12 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-10dP](symbols/R5-10dP.png) | R5-10dP | On Freeway (plaque) | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R5-11](symbols/R5-11.png) | R5-11 | Authorized Vehicles Only | 30x24 | 30x24 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R5-12](symbols/R5-12.png) | R5-12 | No Thru Traffic | 24x30 | 24x30 | — | — | — | 30x36 | Table 2B-1, manual p.70; picture: Figure 2B-12, manual p.107 |
| ![R6-3](symbols/R6-3.png) | R6-3 | Divided Highway Crossing | 30x24 | 30x24 | 36x30 | — | — | 36x30 | Table 2B-1, manual p.70; picture: Figure 2B-20, manual p.109 |
| ![R6-3a](symbols/R6-3a.png) | R6-3a | Divided Highway Crossing | 30x24 | 30x24 | 36x30 | — | — | 36x30 | Table 2B-1, manual p.70; picture: Figure 2B-20, manual p.109 |
| ![R6-5P](symbols/R6-5P.png) | R6-5P | Roundabout Circulation (plaque) | 30x30 | 30x30 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-20, manual p.109 |
| ![R6-6](symbols/R6-6.png) | R6-6 | Begin One Way | 24x30 | 30x36 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-20, manual p.109 |
| ![R6-7](symbols/R6-7.png) | R6-7 | End One Way | 24x30 | 30x36 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-20, manual p.109 |
| ![R7-1](symbols/R7-1.png) | R7-1 | Parking Prohibition | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-2](symbols/R7-2.png) | R7-2 | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-2a](symbols/R7-2a.png) | R7-2a | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-3](symbols/R7-3.png) | R7-3 | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-4](symbols/R7-4.png) | R7-4 | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-4a](symbols/R7-4a.png) | R7-4a | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-5](symbols/R7-5.png) | R7-5 | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-6](symbols/R7-6.png) | R7-6 | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-8](symbols/R7-8.png) | R7-8 | Accessible Parking | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.125 |
| ![R7-8aP](symbols/R7-8aP.png) | R7-8aP | Van Accessible (plaque) | 12x6 | 12x6 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.125 |
| ![R7-9](symbols/R7-9.png) | R7-9 | No Parking Bike Lane | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R7-9a](symbols/R7-9a.png) | R7-9a | No Parking Bike Lane | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R7-10](symbols/R7-10.png) | R7-10 | Back-In Parking Sign | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-20](symbols/R7-20.png) | R7-20 | Parking Fee Station, | 24x18 | 24x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-21](symbols/R7-21.png) | R7-21 | Metered Parking | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
|  | R7-21aP | Mobile Parking Payment (plaque) | 12x6 | 12x6 | — | — | — | — | Table 2B-1, manual p.70 |
| ![R7-22](symbols/R7-22.png) | R7-22 | Metered Parking | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-107](symbols/R7-107.png) | R7-107 | Parking Restrictions | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-107a](symbols/R7-107a.png) | R7-107a | No Parking Bus Stop | 12x24 | 12x24 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-107b](symbols/R7-107b.png) | R7-107b | No Parking Bus Stop | 12x30 | 12x30 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-108](symbols/R7-108.png) | R7-108 | Permissive Parking | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.70; picture: Figure 2B-25, manual p.124 |
| ![R7-111](symbols/R7-111.png) | R7-111 | No Parking Except Electric Vehicles | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-111a](symbols/R7-111a.png) | R7-111a | No Parking Except Electric Vehicles | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-112](symbols/R7-112.png) | R7-112 | Electric Vehicle Parking (time limit) | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-112a](symbols/R7-112a.png) | R7-112a | Electric Vehicle Parking (time limit | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-112b](symbols/R7-112b.png) | R7-112b | Electric Vehicle Parking (time limit | 12x21 | 12x21 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-113](symbols/R7-113.png) | R7-113 | No Parking Except While Charging | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-113aP](symbols/R7-113aP.png) | R7-113aP | Vehicle Must Be Plugged In (plaque) | 12x6 | 12x6 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-113bP](symbols/R7-113bP.png) | R7-113bP | Vacate Stall When Charging | 12x6 | 12x6 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-114](symbols/R7-114.png) | R7-114 | Vehicle Charging Only (time limit) | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-114a](symbols/R7-114a.png) | R7-114a | Vehicle Charging Only (time limit, | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
| ![R7-114b](symbols/R7-114b.png) | R7-114b | Vehicle Charging Only (time limit | 12x21 | 12x21 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.125 |
|  | R7-200 | No Parking/Restricted Parking | 24x18 | 24x18 | — | — | — | — | Table 2B-1, manual p.71 |
|  | R7-200a | No Parking/Restricted Parking | 12x36 | 12x36 | — | — | — | — | Table 2B-1, manual p.71 |
| ![R7-201P](symbols/R7-201P.png) | R7-201P | Tow Away Zone (plaque) | 12x6 | 12x6 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R7-201aP](symbols/R7-201aP.png) | R7-201aP | Parking, Standing, and Stopping Signs (R7 and R8 Series) | — | — | — | — | — | — | section text; picture: Figure 2B-25, manual p.124 |
| ![R7-202P](symbols/R7-202P.png) | R7-202P | This Side of Sign (plaque) | 12x6 | 12x6 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R7-203](symbols/R7-203.png) | R7-203 | Snow Emergency Route | 18x24 | 18x24 | — | — | — | 24x30 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-1](symbols/R8-1.png) | R8-1 | No Parking on Pavement | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-2](symbols/R8-2.png) | R8-2 | No Parking Except on Shoulder | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-3](symbols/R8-3.png) | R8-3 | No Parking (symbol) | 24x24 | 30x30 | 36x36 | 48x48 | 12x12 | 36x36 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-3a](symbols/R8-3a.png) | R8-3a | No Parking | 24x30 | 24x30 | 36x36 | 48x48 | 18x24 | 36x36 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-3c](symbols/R8-3c.png) | R8-3c | On Pavement | 24x36 | 24x36 | — | — | 18x30 | 36x54 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-3d](symbols/R8-3d.png) | R8-3d | On Bridge | 24x36 | 24x36 | — | — | 18x30 | 36x54 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-3e](symbols/R8-3e.png) | R8-3e | On Tracks | 24x36 | 24x36 | — | — | 18x30 | — | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-3f](symbols/R8-3f.png) | R8-3f | Except on Shoulder | 24x36 | 24x36 | — | — | 18x30 | 36x54 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
|  | R8-4 | Emergency Parking Only | 30x24 | 30x24 | 30x24 | 48x36 | — | 48x36 | Table 2B-1, manual p.71 |
| ![R8-5](symbols/R8-5.png) | R8-5 | No Stopping on Pavement | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
| ![R8-6](symbols/R8-6.png) | R8-6 | No Stopping Except on Shoulder | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.71; picture: Figure 2B-25, manual p.124 |
|  | R8-7 | Emergency Stopping Only | 30x24 | 30x24 | 48x36 | 48x36 | — | 48x36 | Table 2B-1, manual p.71 |
| ![R8-8](symbols/R8-8.png) | R8-8 | Do Not Stop on Tracks | 24x30 | 24x30 | 36x48 | — | — | 36x48 | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R8-9](symbols/R8-9.png) | R8-9 | Tracks Out of Service | 24x24 | 24x24 | 36x36 | — | — | 36x36 | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R8-10](symbols/R8-10.png) | R8-10 | Stop Here When Flashing | 24x36 | 24x36 | — | — | — | 36x48 | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R8-10a](symbols/R8-10a.png) | R8-10a | Stop Here When Flashing | 24x30 | 24x30 | — | — | — | 36x42 | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R9-1](symbols/R9-1.png) | R9-1 | Walk on Left Facing Traffic | 18x24 | 18x24 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-27, manual p.129 |
| ![R9-2](symbols/R9-2.png) | R9-2 | Cross Only at Crosswalks | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-27, manual p.129 |
| ![R9-3](symbols/R9-3.png) | R9-3 | No Pedestrian Crossing (symbol) | 18x18 | 18x18 | 24x24 | 30x30 | — | 30x30 | Table 2B-1, manual p.71; picture: Figure 2B-12, manual p.107 |
| ![R9-3a](symbols/R9-3a.png) | R9-3a | No Pedestrian Crossing | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.71; picture: Figure 2B-27, manual p.129 |
| ![R9-3bP](symbols/R9-3bP.png) | R9-3bP | Use Crosswalk (plaque) | 18x12 | 18x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
|  | R9-3cP | Ride With Traffic (plaque) | 12x12 | 12x12 | — | — | 12x12 | — | Table 9A-1, manual p.1049 |
| ![R9-4](symbols/R9-4.png) | R9-4 | No Hitchhiking (symbol) | 18x18 | 18x18 | — | — | — | 24x24 | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R9-4a](symbols/R9-4a.png) | R9-4a | No Hitchhiking | 18x24 | 18x24 | — | — | 12x18 | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R9-5](symbols/R9-5.png) | R9-5 | Bicycles Use Pedestrian Signal | 12x18 | 12x18 | — | — | 12x18 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-6](symbols/R9-6.png) | R9-6 | Bicycles Yield to Pedestrians | 12x18 | 12x18 | — | — | 12x18 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-7](symbols/R9-7.png) | R9-7 | Shared-Use Path Restriction | — | — | — | — | 12x18 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-8](symbols/R9-8.png) | R9-8 | Pedestrian Crosswalk | 36x18 | 36x18 | — | — | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![R9-9](symbols/R9-9.png) | R9-9 | Sidewalk Closed | 24x12 | 24x12 | — | — | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![R9-10](symbols/R9-10.png) | R9-10 | Sidewalk Closed, Use Other Side | 24x12 | 24x12 | — | — | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![R9-11](symbols/R9-11.png) | R9-11 | Sidewalk Closed Ahead, Cross Here | 24x18 | 24x18 | — | — | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![R9-11a](symbols/R9-11a.png) | R9-11a | Sidewalk Closed, Cross Here | 24x12 | 24x12 | — | — | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![R9-12](symbols/R9-12.png) | R9-12 | Bike Lane Closed | 24x12 | 24x12 | — | — | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![R9-13](symbols/R9-13.png) | R9-13 | No Skaters | 18x18 | 18x18 | 24x24 | 30x30 | — | 30x30 | Table 2B-1, manual p.72; picture: Figure 2B-12, manual p.107 |
| ![R9-14](symbols/R9-14.png) | R9-14 | No Equestrians | 18x18 | 18x18 | 24x24 | 30x30 | — | 30x30 | Table 2B-1, manual p.72; picture: Figure 2B-12, manual p.107 |
| ![R9-15](symbols/R9-15.png) | R9-15 | No Snowmobiles | 18x18 | 18x18 | 24x24 | 30x30 | — | 30x30 | Table 2B-1, manual p.72; picture: Figure 2B-12, manual p.107 |
| ![R9-16](symbols/R9-16.png) | R9-16 | No All-Terrian Vehicles | 18x18 | 18x18 | 24x24 | 30x30 | — | 30x30 | Table 2B-1, manual p.72; picture: Figure 2B-12, manual p.107 |
| ![R9-19P](symbols/R9-19P.png) | R9-19P | Except on Shoulder (plaque) | 18x12 | 18x12 | 24x18 | 30x24 | — | 30x24 | Table 2B-1, manual p.72; picture: Figure 2B-12, manual p.107 |
| ![R9-20](symbols/R9-20.png) | R9-20 | Bicycles Allowed Use of Full Lane | 30x30 | 30x30 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 6G-1, manual p.795 |
| ![R9-21](symbols/R9-21.png) | R9-21 | Bicycles Use Shoulder Only | 24x30 | 24x30 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-22](symbols/R9-22.png) | R9-22 | Bicycles Must Exit | 24x30 | 24x30 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-23](symbols/R9-23.png) | R9-23 | Bicycle All Turns from Bike Lane | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-23a](symbols/R9-23a.png) | R9-23a | Bicycle Left Turn from Bike Lane | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-23b](symbols/R9-23b.png) | R9-23b | Bicycle Turn Must Use Turn Box | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-23c](symbols/R9-23c.png) | R9-23c | Bicycle Left Turn Must Use Turn Box | 12x18 | 12x18 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1052 |
| ![R9-24](symbols/R9-24.png) | R9-24 | Bicycle Jughandle Signs | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-24a](symbols/R9-24a.png) | R9-24a | Bicycle All Turns | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-25](symbols/R9-25.png) | R9-25 | Bicycle U and Left Turns | 24x9 | 24x9 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-25a](symbols/R9-25a.png) | R9-25a | Bicycle U and Left Turns | 24x9 | 24x9 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-25b](symbols/R9-25b.png) | R9-25b | Bicycle U and Left Turns | 24x9 | 24x9 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-26](symbols/R9-26.png) | R9-26 | Bicycle U Turn | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-26a](symbols/R9-26a.png) | R9-26a | Bicycle U Turn | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-26b](symbols/R9-26b.png) | R9-26b | Bicycle U Turn | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-27](symbols/R9-27.png) | R9-27 | Bicycle Left Turn | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-27a](symbols/R9-27a.png) | R9-27a | Bicycle Left Turn | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R9-27b](symbols/R9-27b.png) | R9-27b | Bicycle Left Turn | 24x6 | 24x6 | — | — | — | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-1](symbols/R10-1.png) | R10-1 | Cross Only On Green | 12x18 | 12x18 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-2](symbols/R10-2.png) | R10-2 | SIGNAL | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3](symbols/R10-3.png) | R10-3 | Pedestrian Signs | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3a](symbols/R10-3a.png) | R10-3a | Cross Street Wait for Walk Signal | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3b](symbols/R10-3b.png) | R10-3b | Pedestrian Signs | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3c](symbols/R10-3c.png) | R10-3c | Pedestrian Signs | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3d](symbols/R10-3d.png) | R10-3d | Pedestrian Signs | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3e](symbols/R10-3e.png) | R10-3e | Pedestrian Signs | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3f](symbols/R10-3f.png) | R10-3f | Pedestrian Signs | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3g](symbols/R10-3g.png) | R10-3g | Pedestrian Signs | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3h](symbols/R10-3h.png) | R10-3h | Pedestrian Signs | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.129 |
| ![R10-3i](symbols/R10-3i.png) | R10-3i | Pedestrian Signs | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.130 |
| ![R10-4](symbols/R10-4.png) | R10-4 | Bicycle Actuation Signs | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.130 |
| ![R10-4a](symbols/R10-4a.png) | R10-4a | Cross Street Wait for Green Signal | 9x15 | 9x15 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-27, manual p.130 |
|  | R10-4b | Maintaining Minimum Retrorefectivityl | — | — | — | — | — | — | section text |
| ![R10-5](symbols/R10-5.png) | R10-5 | Left on Green Arrow Only | 30x36 | 30x36 | 30x36 | — | 24x30 | 48x60 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-6](symbols/R10-6.png) | R10-6 | STOPHERE ON RED | 24x36 | 24x36 | — | — | — | 36x48 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-6a](symbols/R10-6a.png) | R10-6a | Stop Here on Red | 24x30 | 24x30 | — | — | — | 36x42 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-7](symbols/R10-7.png) | R10-7 | Do Not Block Intersection | 24x30 | 24x30 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-8](symbols/R10-8.png) | R10-8 | Use Lane with Green Arrow | 30x36 | 30x36 | 36x42 | — | — | 60x72 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-10](symbols/R10-10.png) | R10-10 | Left (Right) Turn Signal | 24x30 | 24x30 | — | — | — | 30x36 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-10a](symbols/R10-10a.png) | R10-10a | U- Turn Signal | 24x30 | 24x30 | — | — | — | 30x36 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-10b](symbols/R10-10b.png) | R10-10b | Left (Right) Lane Signal | 30x36 | 30x36 | — | — | 24x30 | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R10-10c](symbols/R10-10c.png) | R10-10c | Left (Right) Turn Lane Signal | 30x42 | 30x42 | — | — | 24x36 | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R10-11](symbols/R10-11.png) | R10-11 | No Turn on Red | 24x30 | 24x30 | — | — | — | 36x48 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-11a](symbols/R10-11a.png) | R10-11a | No Turn on Circular Red | 24x30 | 24x30 | — | — | — | 36x48 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-11b](symbols/R10-11b.png) | R10-11b | No Turn on Red | 24x24 | 24x24 | — | — | — | 36x36 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
|  | R10-11c | No Turn on Red Except From | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.72 |
| ![R10-11d](symbols/R10-11d.png) | R10-11d | No Turn on Red From This Lane | 30x42 | 30x42 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-12](symbols/R10-12.png) | R10-12 | Left Turn Yield on Green | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-12a](symbols/R10-12a.png) | R10-12a | Left Turn Yield on Flashing | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-12b](symbols/R10-12b.png) | R10-12b | Left Turn Yield to Bicycle | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-13](symbols/R10-13.png) | R10-13 | Emergency Signal | 36x24 | 36x24 | — | — | — | 42x30 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-14](symbols/R10-14.png) | R10-14 | Emergency Signal - Stop on | 36x42 | 36x42 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-14a](symbols/R10-14a.png) | R10-14a | Traffc Signal Signs and Plaques (R10i -5 through R10-30) | — | — | — | — | — | — | section text; picture: Figure 2B-28, manual p.132 |
| ![R10-14b](symbols/R10-14b.png) | R10-14b | Stop Here on Flashing Red | 24x36 | 24x36 | — | — | — | 36x48 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.132 |
| ![R10-15](symbols/R10-15.png) | R10-15 | Turning Vehicles Yield to | 30x30 | 30x30 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.133 |
| ![R10-15a](symbols/R10-15a.png) | R10-15a | Turning Vehicles Stop for | 30x30 | 30x30 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.133 |
| ![R10-16](symbols/R10-16.png) | R10-16 | U-Turn Yield to Right Turn | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.133 |
| ![R10-17a](symbols/R10-17a.png) | R10-17a | Right on Red Arrow After Stop | 30x36 | 30x36 | — | — | — | 36x48 | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.133 |
| ![R10-18](symbols/R10-18.png) | R10-18 | Traffic Laws Photo Enforced | 36x24 | 36x24 | 48x30 | 54x36 | — | 54x36 | Table 2B-1, manual p.72; picture: Figure 2B-32, manual p.140 |
| ![R10-18a](symbols/R10-18a.png) | R10-18a | Traffic Signal Photo Enforced | 30x42 | 30x42 | 30x42 | — | — | 36x54 | Table 2B-1, manual p.72; picture: Figure 2B-32, manual p.140 |
| ![R10-19P](symbols/R10-19P.png) | R10-19P | Photo Enforced (symbol plaque) | 24x12 | 24x12 | 36x18 | 48x24 | — | 48x24 | Table 2B-1, manual p.72; picture: Figure 2B-32, manual p.140 |
| ![R10-19aP](symbols/R10-19aP.png) | R10-19aP | Photo Enforced (plaque) | 24x18 | 24x18 | 36x24 | 48x36 | — | 48x36 | Table 2B-1, manual p.72; picture: Figure 2B-32, manual p.140 |
| ![R10-20aP](symbols/R10-20aP.png) | R10-20aP | MON—FRI (and times) | 24x18 | 24x18 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.133 |
| ![R10-22](symbols/R10-22.png) | R10-22 | Bicycle Detector | 12x18 | 12x18 | — | — | 12x18 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-23](symbols/R10-23.png) | R10-23 | Crosswalk - Stop on Red | 24x30 | 24x30 | — | — | — | — | Table 2B-1, manual p.72; picture: Figure 2B-28, manual p.133 |
| ![R10-23a](symbols/R10-23a.png) | R10-23a | Stop on Red - Yield on Flashing | 24x30 | 24x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-28, manual p.133 |
| ![R10-24](symbols/R10-24.png) | R10-24 | Bike Push Button for Green Light | 9x15 | 9x15 | — | — | 9x15 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-25](symbols/R10-25.png) | R10-25 | Push Button For Warning Lights - | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-27, manual p.130 |
| ![R10-26](symbols/R10-26.png) | R10-26 | Bike Push Button for Green Light (arrow) | 9x15 | 9x15 | — | — | 9x15 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-27](symbols/R10-27.png) | R10-27 | Left Turn Yield on Flashing Red | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-28, manual p.133 |
| ![R10-28](symbols/R10-28.png) | R10-28 | XX Vehicles per Green | 24x30 | 24x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-29, manual p.135 |
| ![R10-29](symbols/R10-29.png) | R10-29 | XX Vehicles per Green Each Lane | 36x24 | 36x24 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-29, manual p.135 |
| ![R10-30](symbols/R10-30.png) | R10-30 | Right Turn on Red Must | 30x36 | 30x36 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-28, manual p.133 |
| ![R10-31P](symbols/R10-31P.png) | R10-31P | At Signal (plaque) | 24x9 | 24x9 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-28, manual p.133 |
| ![R10-32P](symbols/R10-32P.png) | R10-32P | Push Button for 2 Seconds for | 9x12 | 9x12 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-27, manual p.130 |
| ![R10-40](symbols/R10-40.png) | R10-40 | Bicycle Signal | 12x21 | 12x21 | — | — | 12x21 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-40a](symbols/R10-40a.png) | R10-40a | Bicycle Signal | 12x21 | 12x21 | — | — | 12x21 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-41](symbols/R10-41.png) | R10-41 | Bicycle Signal | 12x21 | 12x21 | — | — | 12x21 | — | Table 9A-1, manual p.1049; picture: Figure 9B-1, manual p.1053 |
| ![R10-41a](symbols/R10-41a.png) | R10-41a | Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c) | — | — | — | — | — | — | section text; picture: Figure 9B-1, manual p.1053 |
| ![R10-41b](symbols/R10-41b.png) | R10-41b | Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c) | — | — | — | — | — | — | section text; picture: Figure 9B-1, manual p.1053 |
| ![R10-41c](symbols/R10-41c.png) | R10-41c | Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c) | — | — | — | — | — | — | section text; picture: Figure 9B-1, manual p.1053 |
| ![R11-1](symbols/R11-1.png) | R11-1 | Keep Off Median | 24x30 | 24x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R11-2](symbols/R11-2.png) | R11-2 | ROAD CLOSED Sign | 48x30 | 48x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
|  | R11-2a | STREET CLOSED | 48x30 | 48x30 | — | — | — | — | Table 2B-1, manual p.73 |
|  | R11-2b | BRIDGE OUT | 48x30 | 48x30 | — | — | — | — | Table 2B-1, manual p.73 |
| ![R11-2c](symbols/R11-2c.png) | R11-2c | PATH CLOSED | 48x30 | 48x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 6G-1, manual p.795 |
| ![R11-3](symbols/R11-3.png) | R11-3 | Road Closed - Local Traffic Only | 60x30 | 60x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R11-3a](symbols/R11-3a.png) | R11-3a | LOCALTRAFFIC ONLY | 60x30 | 60x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R11-3b](symbols/R11-3b.png) | R11-3b | BRIDGE OUT | 60x30 | 60x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R11-4](symbols/R11-4.png) | R11-4 | ROAD CLOSED TO THRU TRAFFIC | 60x30 | 60x30 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-1](symbols/R12-1.png) | R12-1 | Weight Limit Signs | 24x30 | 24x30 | 36x48 | — | — | 36x48 | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-2](symbols/R12-2.png) | R12-2 | TONSor AXLE WEIGHT LIMIT XX LBS | 24x30 | 24x30 | 36x48 | — | — | 36x48 | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-4](symbols/R12-4.png) | R12-4 | Weight Limit - Axle, Gross | 36x24 | 36x24 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-5](symbols/R12-5.png) | R12-5 | Weight Limit | 24x36 | 24x36 | 36x48 | 48x60 | — | — | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-6](symbols/R12-6.png) | R12-6 | Weight Limit - Specialized | 30x42 | 36x48 | 36x48 | 48x60 | — | 48x60 | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-7](symbols/R12-7.png) | R12-7 | Weight Limit - Emergency Vehicles | 30x36 | 30x36 | 48x60 | 48x60 | — | 48x60 | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R12-7aP](symbols/R12-7aP.png) | R12-7aP | Weight Limit - Emergency | 30x30 | 30x30 | 48x48 | 48x48 | — | 48x48 | Table 2B-1, manual p.73; picture: Figure 2B-30, manual p.136 |
| ![R13-1](symbols/R13-1.png) | R13-1 | Weigh Station | 72x54 | 72x54 | 96x72 | 132x90 | — | — | Table 2B-1, manual p.73; picture: Figure 2B-31, manual p.139 |
| ![R14-1](symbols/R14-1.png) | R14-1 | Truck Route | 24x18 | 24x18 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-31, manual p.139 |
| ![R14-2](symbols/R14-2.png) | R14-2 | Hazardous Material | 24x24 | 24x24 | 30x30 | 36x36 | — | 42x42 | Table 2B-1, manual p.73; picture: Figure 2B-31, manual p.139 |
| ![R14-3](symbols/R14-3.png) | R14-3 | Hazardous Material | 24x24 | 24x24 | 30x30 | 36x36 | — | 42x42 | Table 2B-1, manual p.73; picture: Figure 2B-31, manual p.139 |
| ![R14-4](symbols/R14-4.png) | R14-4 | National Network | 30x30 | 30x30 | 36x36 | 36x36 | — | 42x42 | Table 2B-1, manual p.73; picture: Figure 2B-31, manual p.139 |
| ![R14-5](symbols/R14-5.png) | R14-5 | National Network | 30x30 | 30x30 | 36x36 | 36x36 | — | 42x42 | Table 2B-1, manual p.73; picture: Figure 2B-31, manual p.139 |
| ![R15-1](symbols/R15-1.png) | R15-1 | Grade Crossing (Crossbuck) | 48x9 | 48x9 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-2P](symbols/R15-2P.png) | R15-2P | Number of Tracks (plaque) | 27x18 | 27x18 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-3P](symbols/R15-3P.png) | R15-3P | Exempt (plaque) | 24x12 | 24x12 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
|  | R15-4 | Light Rail Transit Only Lane Signs | — | — | — | — | — | — | section text |
| ![R15-4a](symbols/R15-4a.png) | R15-4a | Light Rail Only Right Lane | 24x30 | 24x30 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-4b](symbols/R15-4b.png) | R15-4b | Light Rail Only Left Lane | 24x30 | 24x30 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-4c](symbols/R15-4c.png) | R15-4c | Light Rail Only Center Lane | 24x30 | 24x30 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-5](symbols/R15-5.png) | R15-5 | Light Rail Do Not Pass (symbol) | 24x30 | 24x30 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-5a](symbols/R15-5a.png) | R15-5a | Do Not Pass Stopped Train | 24x30 | 24x30 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-6](symbols/R15-6.png) | R15-6 | No Motor Vehicles On Tracks | 24x24 | 24x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-6a](symbols/R15-6a.png) | R15-6a | Do Not Drive On Tracks | 24x30 | 24x30 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-7](symbols/R15-7.png) | R15-7 | Light Rail Divided | 24x24 | 24x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-7a](symbols/R15-7a.png) | R15-7a | Light Rail Divided Highway | 24x24 | 24x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R15-8](symbols/R15-8.png) | R15-8 | Look | 18x9 | 18x9 | — | — | 18x9 | — | Table 8B-1, manual p.994; picture: Figure 8B-1, manual p.996 |
| ![R16-3](symbols/R16-3.png) | R16-3 | Move Over or Reduce Speed | — | 60x48 | 84x60 | 102x72 | — | 84x60 | Table 2B-1, manual p.73; picture: Figure 2B-32, manual p.140 |
| ![R16-4](symbols/R16-4.png) | R16-4 | Minor Crashes Move Vehicles from | — | 60x42 | 84x54 | 96x60 | — | 84x54 | Table 2B-1, manual p.73; picture: Figure 2B-32, manual p.140 |
| ![R16-5](symbols/R16-5.png) | R16-5 | Lights On When Using Wipers | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-6](symbols/R16-6.png) | R16-6 | LIGHTS ON WHEN RAINING | 24x30 | 24x30 | 36x48 | 48x60 | — | 36x48 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-7](symbols/R16-7.png) | R16-7 | Turn On Headlights Next XX Miles | 60x18 | 60x18 | 96x30 | 132x36 | — | 96x30 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-8](symbols/R16-8.png) | R16-8 | Turn On, Check Headlights | 42x18 | 42x18 | 60x30 | 78x36 | — | 60x30 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-9](symbols/R16-9.png) | R16-9 | Turn On, Check Headlights | 42x18 | 42x18 | 60x30 | 78x36 | — | 60x30 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-10](symbols/R16-10.png) | R16-10 | BEGIN DAYTIMEHEADLIGHT SECTION | 60x18 | 60x18 | 96x30 | 120x36 | — | 96x30 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-11](symbols/R16-11.png) | R16-11 | ENDDAYTIME HEADLIGHT SECTION | 60x18 | 60x18 | 96x30 | 120x36 | — | 96x30 | Table 2B-1, manual p.73; picture: Figure 2B-34, manual p.141 |
| ![R16-15](symbols/R16-15.png) | R16-15 | No Hand-Held Phone Use By Driver | — | — | 72x48 | 72x48 | — | — | Table 2B-1, manual p.73; picture: Figure 2B-32, manual p.140 |
| ![R16-15a](symbols/R16-15a.png) | R16-15a | No Hand-Held Phone Use By Driver | 30x42 | 30x42 | — | — | — | — | Table 2B-1, manual p.73; picture: Figure 2B-32, manual p.140 |
| ![R22-2](symbols/R22-2.png) | R22-2 | Turn Off 2-Way Radio and Cell Phone | 42x36 | 42x36 | 42x36 | 42x36 | — | — | Table 6G-1, manual p.796; picture: Figure 6G-1, manual p.795 |
| ![S3-1](symbols/S3-1.png) | S3-1 | School Bus Stop Ahead | 36x36 | 36x36 | — | — | 30x30 | 48x48 | Table 7B-1, manual p.971; picture: Figure 7B-1, manual p.973 |
|  | S3-2 | School Bus Turn Ahead | 36x36 | 36x36 | — | — | 30x30 | 48x48 | Table 7B-1, manual p.971 |
|  | S4-1P | X:XX to X:XX AM | 24x12 | 24x12 | — | — | — | 36x18 | Table 7B-1, manual p.971 |
|  | S4-2P | When Children Are Present | 24x12 | 24x12 | — | — | — | 36x18 | Table 7B-1, manual p.971 |
|  | S4-3P | School | 24x9 | 24x9 | — | — | — | 36x12 | Table 7B-1, manual p.971 |
|  | S4-4P | When Flashing | 24x12 | 24x12 | — | — | — | 36x18 | Table 7B-1, manual p.971 |
|  | S4-5 | Reduced School Speed | 36x36 | 36x36 | — | — | 30x30 | 48x48 | Table 7B-1, manual p.971 |
|  | S4-5a | Reduced School Speed | 36x36 | 36x36 | — | — | 30x30 | 48x48 | Table 7B-1, manual p.971 |
|  | S4-6P | Days of Week | 24x12 | 24x12 | — | — | — | 36x18 | Table 7B-1, manual p.971 |
|  | S4-7P | All Year | 24x12 | 24x12 | — | — | — | 30x18 | Table 7B-1, manual p.971 |
|  | S5-1 | School Speed Limit XX | 24x48 | 24x48 | — | — | — | 36x72 | Table 7B-1, manual p.971 |
|  | S5-2 | End School Zone | 24x30 | 24x30 | — | — | — | 36x48 | Table 7B-1, manual p.971 |
|  | S5-3 | End School Speed Limit | 24x30 | 24x30 | — | — | — | 36x48 | Table 7B-1, manual p.971 |
| ![W1-4b](symbols/W1-4b.png) | W1-4b | Reverse Curve (2 or more lanes) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.799 |
| ![W1-4c](symbols/W1-4c.png) | W1-4c | Reverse Curve (2 or more lanes) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.799 |
| ![W1-5](symbols/W1-5.png) | W1-5 | Winding Road | 30x30 | 36x36 | 36x36 | 36x36 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-6](symbols/W1-6.png) | W1-6 | One-Direction Large Arrow | 48x24 | 48x24 | 60x30 | 60x30 | — | 60x30 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-7](symbols/W1-7.png) | W1-7 | Two-Direction Large Arrow | 48x24 | 48x24 | — | — | — | 60x30 | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W1-10](symbols/W1-10.png) | W1-10 | Combination Horizontal | 36x36 | 36x36 | 36x36 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-10a](symbols/W1-10a.png) | W1-10a | Combination Horizontal | 36x36 | 36x36 | 36x36 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-10b](symbols/W1-10b.png) | W1-10b | Combination Horizontal | 36x36 | 36x36 | 36x36 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-10c](symbols/W1-10c.png) | W1-10c | Combination Horizontal Alignment/Intersection Signs (W1-10 Series) | — | — | — | — | — | — | section text; picture: Figure 2C-1, manual p.153 |
| ![W1-10d](symbols/W1-10d.png) | W1-10d | Combination Horizontal Alignment/Intersection Signs (W1-10 Series) | — | — | — | — | — | — | section text; picture: Figure 2C-1, manual p.153 |
| ![W1-10e](symbols/W1-10e.png) | W1-10e | Combination Horizontal Alignment/Intersection Signs (W1-10 Series) | — | — | — | — | — | — | section text; picture: Figure 2C-1, manual p.153 |
| ![W1-11](symbols/W1-11.png) | W1-11 | Hairpin Curve | 30x30 | 30x30 | 36x36 | 48x48 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-13](symbols/W1-13.png) | W1-13 | Truck Rollover | 36x36 | 36x36 | 36x36 | 48x48 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W1-15](symbols/W1-15.png) | W1-15 | 270-degree Curve | 30x30 | 30x30 | 36x36 | 48x48 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-1, manual p.153 |
| ![W2-3](symbols/W2-3.png) | W2-3 | Intersection Warning | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
|  | W2-3a | Intersection Warning | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148 |
| ![W2-5](symbols/W2-5.png) | W2-5 | Y-Intersection | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 9C-1, manual p.1065 |
|  | W2-7 | Offset SideRoads | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148 |
| ![W2-8](symbols/W2-8.png) | W2-8 | Double Side Roads | 30x30 | 30x30 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
|  | W2-10 | Traffic Entering When Flashing | 36x36 | 36x36 | 48x48 | — | — | — | Table 2C-1, manual p.148 |
|  | W2-11 | Traffic Approaching | 36x36 | 36x36 | 48x48 | — | — | — | Table 2C-1, manual p.148 |
| ![W3-4](symbols/W3-4.png) | W3-4 | Be Prepared to Stop | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
| ![W3-5a](symbols/W3-5a.png) | W3-5a | XX MPH Speed Zone Ahead | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W3-5b](symbols/W3-5b.png) | W3-5b | Variable Speed Zone Ahead | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W3-5c](symbols/W3-5c.png) | W3-5c | XX MPH Truck Speed | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W3-6](symbols/W3-6.png) | W3-6 | Draw Bridge | 36x36 | 36x36 | 48x48 | — | — | 60x60 | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
| ![W3-7](symbols/W3-7.png) | W3-7 | Ramp Meter Ahead | 36x36 | 36x36 | — | — | — | — | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
| ![W3-8](symbols/W3-8.png) | W3-8 | Ramp Metered When Flashing | 36x36 | 36x36 | — | — | — | — | Table 2C-1, manual p.148; picture: Figure 2C-8, manual p.177 |
|  | W3-9 | Traffic Using Shoulder | — | — | 36x48 | 48x60 | — | — | Table 2G-1, manual p.408 |
| ![W4-1](symbols/W4-1.png) | W4-1 | Merge | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W4-3](symbols/W4-3.png) | W4-3 | Added Lane | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W4-4P](symbols/W4-4P.png) | W4-4P | Cross Traffic Does Not | 24x12 | 24x12 | 36x18 | — | — | 48x24 | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W4-4aP](symbols/W4-4aP.png) | W4-4aP | Does Not Stop | 24x12 | 24x12 | 36x18 | — | — | 48x24 | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W4-4bP](symbols/W4-4bP.png) | W4-4bP | Oncoming Traffic Does Not Stop | 24x12 | 24x12 | 36x18 | — | — | 48x24 | Table 2C-1, manual p.148; picture: Figure 2C-9, manual p.179 |
| ![W4-5](symbols/W4-5.png) | W4-5 | Entering Roadway Merge | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W4-5aP](symbols/W4-5aP.png) | W4-5aP | No Merge Area (plaque) | 18x24 | 18x24 | 24x30 | 24x30 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W4-6](symbols/W4-6.png) | W4-6 | Entering Roadway Added Lane | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W4-7](symbols/W4-7.png) | W4-7 | Heavy Merge from Right (Left) | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W4-8](symbols/W4-8.png) | W4-8 | Single Lane Transition | 36x36 | 36x36 | 36x36 | 48x48 | — | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
|  | W4-9 | Work Affecting Pedestrian and Bicycle Facilities | — | — | — | — | — | — | section text |
| ![W5-1](symbols/W5-1.png) | W5-1 | Road Narrows | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W5-2](symbols/W5-2.png) | W5-2 | Narrow Bridge | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W5-2a](symbols/W5-2a.png) | W5-2a | Narrow Underpass | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W5-3](symbols/W5-3.png) | W5-3 | One Lane Bridge | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W5-3a](symbols/W5-3a.png) | W5-3a | One Lane Underpass | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W5-4](symbols/W5-4.png) | W5-4 | Ramp Narrows | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.799 |
| ![W5-4a](symbols/W5-4a.png) | W5-4a | Path Narrows | — | — | — | — | 18x18 | — | Table 9A-1, manual p.1050; picture: Figure 9C-1, manual p.1065 |
| ![W6-1](symbols/W6-1.png) | W6-1 | Divided Highway | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W6-2](symbols/W6-2.png) | W6-2 | Divided Highway Ends | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-6, manual p.169 |
| ![W6-3](symbols/W6-3.png) | W6-3 | Two-Way Traffic | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W6-4](symbols/W6-4.png) | W6-4 | Narrow Two-Way Traffic | 12x18 | 12x18 | 12x18 | 12x18 | — | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.799 |
| ![W6-5](symbols/W6-5.png) | W6-5 | Two-Way Traffic (3-Lane) | 36x36 | 36x36 | 48x48 | — | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W6-5a](symbols/W6-5a.png) | W6-5a | Two-Way Traffic (3-Lane) | 36x36 | 36x36 | 48x48 | — | — | — | Table 2C-1, manual p.148; picture: Figure 2C-11, manual p.182 |
| ![W7-1](symbols/W7-1.png) | W7-1 | Hill | 30x30 | 36x36 | 36x36 | 36x36 | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-5, manual p.167 |
| ![W7-1a](symbols/W7-1a.png) | W7-1a | Hill with Grade | 30x30 | 36x36 | 36x36 | 36x36 | 24x24 | 48x48 | Table 2C-1, manual p.148; picture: Figure 2C-5, manual p.167 |
| ![W7-2P](symbols/W7-2P.png) | W7-2P | Use Low Gear (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-2bP](symbols/W7-2bP.png) | W7-2bP | Trucks Use Lower Gear (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-3P](symbols/W7-3P.png) | W7-3P | XX% Grade (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-3aP](symbols/W7-3aP.png) | W7-3aP | Next XX Miles (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-3bP](symbols/W7-3bP.png) | W7-3bP | XX% Grade, XX Miles (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-4](symbols/W7-4.png) | W7-4 | Runaway Truck Ramp XX Miles | 84x48 | 84x48 | 120x72 | 120x72 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-4b](symbols/W7-4b.png) | W7-4b | Runaway Truck Ramp | 84x54 | 84x54 | 120x78 | 120x78 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-4c](symbols/W7-4c.png) | W7-4c | Truck Escape Ramp | 78x60 | 78x60 | 78x60 | 78x60 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-4dP](symbols/W7-4dP.png) | W7-4dP | Sand, Gravel, Paved (plaques) | 24x12 | 24x12 | 24x12 | 24x12 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-4eP](symbols/W7-4eP.png) | W7-4eP | Sand, Gravel, Paved (plaques) | 24x12 | 24x12 | 24x12 | 24x12 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-4fP](symbols/W7-4fP.png) | W7-4fP | Sand, Gravel, Paved (plaques) | 24x12 | 24x12 | 24x12 | 24x12 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W7-5](symbols/W7-5.png) | W7-5 | Hill | 30x30 | 30x30 | — | — | 18x18 | — | Table 9A-1, manual p.1050; picture: Figure 9C-1, manual p.1065 |
| ![W7-6](symbols/W7-6.png) | W7-6 | Hill Blocks View | 30x30 | 36x36 | 36x36 | — | — | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-5, manual p.167 |
| ![W8-1](symbols/W8-1.png) | W8-1 | Bump or Dip | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-2](symbols/W8-2.png) | W8-2 | Bump or Dip | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-3](symbols/W8-3.png) | W8-3 | Pavement Ends | 36x36 | 36x36 | 48x48 | — | 30x30 | — | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-4](symbols/W8-4.png) | W8-4 | Soft Shoulder | 36x36 | 36x36 | 48x48 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-5](symbols/W8-5.png) | W8-5 | Slippery When Wet | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-5P](symbols/W8-5P.png) | W8-5P | Road Condition (plaques) | 24x18 | 24x18 | 30x24 | 36x30 | — | 36x30 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-5aP](symbols/W8-5aP.png) | W8-5aP | Ice (plaque) | 24x12 | 24x12 | 30x18 | 30x18 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-5bP](symbols/W8-5bP.png) | W8-5bP | Road Condition (plaques) | 24x18 | 24x18 | 30x24 | 36x30 | — | 36x30 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-5cP](symbols/W8-5cP.png) | W8-5cP | Road Condition (plaques) | 24x18 | 24x18 | 30x24 | 36x30 | — | 36x30 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-6](symbols/W8-6.png) | W8-6 | Truck Crossing | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-14, manual p.191 |
| ![W8-7](symbols/W8-7.png) | W8-7 | Loose Gravel | 36x36 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-8](symbols/W8-8.png) | W8-8 | Rough Road | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-9](symbols/W8-9.png) | W8-9 | Low Shoulder | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
|  | W8-10 | Bicycle Surface Condition | 30x30 | 30x30 | — | — | 18x18 | — | Table 9A-1, manual p.1050 |
|  | W8-10P | Slippery When Wet (plaque) | 12x9 | 12x9 | — | — | 12x9 | — | Table 9A-1, manual p.1050 |
| ![W8-11](symbols/W8-11.png) | W8-11 | Uneven Lanes | 36x36 | 36x36 | 36x36 | 48x48 | — | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-12](symbols/W8-12.png) | W8-12 | No Center Line | 36x36 | 36x36 | 36x36 | 48x48 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-13](symbols/W8-13.png) | W8-13 | Bridge Ices Before Road | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-14](symbols/W8-14.png) | W8-14 | Fallen Rocks | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
|  | W8-15 | Grooved Pavement | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149 |
| ![W8-15aP](symbols/W8-15aP.png) | W8-15aP | Motorcycle (plaque) | 24x18 | 24x18 | 30x24 | 36x30 | — | 36x30 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-16](symbols/W8-16.png) | W8-16 | Metal Bridge Deck | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 6H-1, manual p.800 |
|  | W8-17 | Shoulder Drop-Off | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149 |
| ![W8-17P](symbols/W8-17P.png) | W8-17P | Shoulder Drop-Off (plaque) | 24x18 | 24x18 | 30x24 | 36x30 | — | 36x30 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-18](symbols/W8-18.png) | W8-18 | Road May Flood | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-19](symbols/W8-19.png) | W8-19 | Depth Gauge | 12x72 | 12x72 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-21](symbols/W8-21.png) | W8-21 | Gusty Winds Area | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-22](symbols/W8-22.png) | W8-22 | Fog Area | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-23](symbols/W8-23.png) | W8-23 | No Shoulder | 36x36 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-24](symbols/W8-24.png) | W8-24 | Steel Plate Ahead | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.800 |
| ![W8-25](symbols/W8-25.png) | W8-25 | Shoulder Ends | 30x30 | 36x36 | 36x36 | 48x48 | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-7, manual p.174 |
| ![W8-26](symbols/W8-26.png) | W8-26 | Road Ends | 30x30 | 36x36 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-11, manual p.182 |
| ![W8-26a](symbols/W8-26a.png) | W8-26a | Street Ends | 30x30 | 36x36 | — | — | — | — | Table 2C-1, manual p.149; picture: Figure 2C-11, manual p.182 |
| ![W9-1](symbols/W9-1.png) | W9-1 | Right (Left) Lane Ends | 36x36 | 36x36 | 36x36 | 48x48 | 30x30 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-11, manual p.182 |
|  | W9-2 | Lane Ends | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.803 |
| ![W9-2a](symbols/W9-2a.png) | W9-2a | Merge Here Take Turns | 36x48 | 36x48 | 36x48 | 36x48 | — | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.800 |
| ![W9-3](symbols/W9-3.png) | W9-3 | Interior Lane Shift Ahead | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.803; picture: Figure 6H-1, manual p.800 |
| ![W9-4](symbols/W9-4.png) | W9-4 | Lanes Merge | 36x36 | 36x36 | 36x36 | 48x48 | 30x30 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-11, manual p.182 |
| ![W9-5](symbols/W9-5.png) | W9-5 | Bicycle Lane Ends | 30x30 | 30x30 | — | — | — | — | Table 9A-1, manual p.1050; picture: Figure 9C-1, manual p.1065 |
| ![W9-5a](symbols/W9-5a.png) | W9-5a | Bicycles Merging | 30x30 | 30x30 | — | — | 18x18 | — | Table 9A-1, manual p.1050; picture: Figure 6H-1, manual p.800 |
| ![W9-6](symbols/W9-6.png) | W9-6 | Pay Toll XX Miles | 96x66 | 96x66 | 96x66 | 96x66 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6a](symbols/W9-6a.png) | W9-6a | Stop Ahead Pay Toll | 114x66 | 114x66 | 114x66 | 114x66 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6bP](symbols/W9-6bP.png) | W9-6bP | Pay Toll and Take Ticket Advance Warning Plaques | — | — | — | — | — | — | section text; picture: Figure 2F-4, manual p.386 |
| ![W9-6cP](symbols/W9-6cP.png) | W9-6cP | Stop AheadPay Toll | 264x30 | 264x30 | 264x30 | 264x30 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6dP](symbols/W9-6dP.png) | W9-6dP | Stop Ahead Pay | 114x48 | 114x48 | 114x48 | 114x48 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6e](symbols/W9-6e.png) | W9-6e | Take Ticket XX Miles | 114x48 | 114x48 | 114x48 | 114x48 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6f](symbols/W9-6f.png) | W9-6f | Stop Ahead Take Ticket | 114x48 | 114x48 | 114x48 | 114x48 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6gP](symbols/W9-6gP.png) | W9-6gP | Take Ticket XX | 216x30 | 216x30 | 216x30 | 216x30 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-6hP](symbols/W9-6hP.png) | W9-6hP | Stop Ahead Take | 282x30 | 282x30 | 282x30 | 282x30 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W9-7](symbols/W9-7.png) | W9-7 | Right (Left) Lane for Exit Only | 132x72 | 132x72 | 132x72 | 132x72 | — | — | Table 2C-1, manual p.149; picture: Figure 2C-11, manual p.182 |
| ![W10-1](symbols/W10-1.png) | W10-1 | Grade Crossing Advance Warning | 36Dia. | 36Dia. | 48Dia. | — | — | 48Dia. | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-1aP](symbols/W10-1aP.png) | W10-1aP | Exempt (plaque) | 24x12 | 24x12 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-2](symbols/W10-2.png) | W10-2 | Grade Crossing and Intersection Advance Warning | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-3](symbols/W10-3.png) | W10-3 | Grade Crossing and Intersection | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-4](symbols/W10-4.png) | W10-4 | Grade Crossing and Intersection | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
|  | W10-5 | Low Ground Clearance (symbol) | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994 |
|  | W10-5P | Low Ground Clearance (plaque) | 30x24 | 30x24 | — | — | — | — | Table 8B-1, manual p.994 |
|  | W10-7 | Light Rail Activated | 24x24 | 24x24 | — | — | — | — | Table 8B-1, manual p.994 |
| ![W10-8](symbols/W10-8.png) | W10-8 | Trains May Exceed 80 MPH | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-9](symbols/W10-9.png) | W10-9 | No Train Horn | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-9P](symbols/W10-9P.png) | W10-9P | No Train Horn (plaque) | 30x24 | 30x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-11](symbols/W10-11.png) | W10-11 | Storage Space (symbol) | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-11a](symbols/W10-11a.png) | W10-11a | Storage Space XX Feet | 30x36 | 30x36 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-11b](symbols/W10-11b.png) | W10-11b | Storage Space XX Feet between | 30x36 | 30x36 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-12](symbols/W10-12.png) | W10-12 | Skewed Crossing (symbol) | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-13P](symbols/W10-13P.png) | W10-13P | No Gates or Lights (plaque) | 30x24 | 30x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-14P](symbols/W10-14P.png) | W10-14P | Next Crossing (plaque) | 30x24 | 30x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-14aP](symbols/W10-14aP.png) | W10-14aP | Use Next Crossing (plaque) | 30x24 | 30x24 | — | — | — | — | Table 8B-1, manual p.994; picture: Figure 8B-4, manual p.1002 |
| ![W10-15P](symbols/W10-15P.png) | W10-15P | Rough Crossing (plaque) | 30x24 | 30x24 | — | — | — | 36x30 | Table 8B-1, manual p.995; picture: Figure 8B-4, manual p.1002 |
| ![W10-16](symbols/W10-16.png) | W10-16 | Another Train Coming | 30x30 | 30x30 | — | — | — | — | Table 8B-1, manual p.995; picture: Figure 8B-4, manual p.1002 |
| ![W10-21](symbols/W10-21.png) | W10-21 | Busway Crossing | 36x36 | 36x36 | 48x48 | — | — | 48x48 | Table 8B-1, manual p.995; picture: Figure 8B-4, manual p.1002 |
| ![W10-21aP](symbols/W10-21aP.png) | W10-21aP | Signal Ahead (plaque) | 30x24 | 30x24 | — | — | — | — | Table 8B-1, manual p.995; picture: Figure 8B-4, manual p.1002 |
|  | W11-1 | Bicycle | 30x30 | 30x30 | 36x36 | — | — | 48x48 | Table 2C-1, manual p.149 |
| ![W11-3](symbols/W11-3.png) | W11-3 | Deer | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-4](symbols/W11-4.png) | W11-4 | Cattle | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-5](symbols/W11-5.png) | W11-5 | Farm Vehicle | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-14, manual p.191 |
| ![W11-6](symbols/W11-6.png) | W11-6 | Snowmobile | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-7](symbols/W11-7.png) | W11-7 | Equestrian | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-8](symbols/W11-8.png) | W11-8 | Emergency Vehicle | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150; picture: Figure 2C-14, manual p.191 |
|  | W11-9 | Handicapped | 30x30 | 36x36 | 36x36 | — | — | 48x48 | Table 2C-1, manual p.150 |
| ![W11-10](symbols/W11-10.png) | W11-10 | Truck | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150; picture: Figure 2C-14, manual p.191 |
| ![W11-11](symbols/W11-11.png) | W11-11 | Golf Cart | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150; picture: Figure 2C-14, manual p.191 |
| ![W11-12P](symbols/W11-12P.png) | W11-12P | Emergency Signal Ahead (plaque) | 36x30 | 36x30 | 36x30 | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-14, manual p.191 |
| ![W11-14](symbols/W11-14.png) | W11-14 | Horse-Drawn Vehicle | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150; picture: Figure 2C-14, manual p.191 |
|  | W11-15 | Trail Crossing | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150 |
| ![W11-15P](symbols/W11-15P.png) | W11-15P | Trail Crossing (plaque) | 24x18 | 24x18 | 30x24 | — | — | 36x30 | Table 2C-1, manual p.150; picture: Figure 9C-1, manual p.1066 |
|  | W11-15a | Trail Crossing | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150 |
| ![W11-16](symbols/W11-16.png) | W11-16 | Bear | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-17](symbols/W11-17.png) | W11-17 | Sheep | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-18](symbols/W11-18.png) | W11-18 | Bighorn Sheep | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-19](symbols/W11-19.png) | W11-19 | Donkey | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-20](symbols/W11-20.png) | W11-20 | Elk | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-21](symbols/W11-21.png) | W11-21 | Moose | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W11-22](symbols/W11-22.png) | W11-22 | Wild Horse | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.149; picture: Figure 2C-15, manual p.193 |
| ![W12-1](symbols/W12-1.png) | W12-1 | Double Arrow | 30x30 | 36x36 | 36x36 | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W12-2](symbols/W12-2.png) | W12-2 | Low Clearance Advance | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W12-2a](symbols/W12-2a.png) | W12-2a | Low Clearance Overhead | 84x24 | 84x24 | 84x24 | 84x24 | — | — | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W12-2b](symbols/W12-2b.png) | W12-2b | Low Clearance - Lane Overhead | 102x24 | 102x24 | 102x24 | 102x24 | — | — | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W13-1aP](symbols/W13-1aP.png) | W13-1aP |  | 48x15 | 48x15 | 60x18 | 60x18 | — | — | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-2](symbols/W13-2.png) | W13-2 | Advisory Exit Speed | 24x30 | 24x30 | 36x48 | 36x48 | — | 48x60 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-3](symbols/W13-3.png) | W13-3 | Advisory Exit or Ramp Speed | 24x30 | 24x30 | 36x48 | 36x48 | — | 48x60 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-4P](symbols/W13-4P.png) | W13-4P | On Ramp (plaque) | 36x36 | 36x36 | 36x36 | 36x36 | — | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W13-6](symbols/W13-6.png) | W13-6 | Advisory Exit Speed | 24x42 | 24x42 | 36x66 | 36x66 | — | 48x84 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-7](symbols/W13-7.png) | W13-7 | Advisory Ramp Speed | 24x42 | 24x42 | 36x66 | 36x66 | — | 48x84 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-8](symbols/W13-8.png) | W13-8 | Alignment/Advisory Exit or | 24x42 | 24x42 | 36x66 | 36x66 | — | 48x84 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-9](symbols/W13-9.png) | W13-9 | Alignment/Advisory Exit or | 24x42 | 24x42 | 36x66 | 36x66 | — | 48x84 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-10](symbols/W13-10.png) | W13-10 | Alignment/Advisory Exit or | 24x36 | 24x36 | 36x54 | 36x54 | — | 48x72 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-11](symbols/W13-11.png) | W13-11 | Alignment/Advisory Exit or | 24x36 | 24x36 | 36x54 | 36x54 | — | 48x72 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-12](symbols/W13-12.png) | W13-12 | Alignment/Advisory Exit or | 24x42 | 24x42 | 36x66 | 36x66 | — | 48x84 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
| ![W13-13](symbols/W13-13.png) | W13-13 | Alignment/Advisory Exit or | 24x42 | 24x42 | 36x66 | 36x66 | — | 48x84 | Table 2C-1, manual p.150; picture: Figure 2C-1, manual p.153 |
|  | W13-20 | Vehicle Speed Feedback Sign | 24x30 | 30x36 | 36x48 | 48x60 | — | — | Table 2C-1, manual p.150 |
|  | W13-20aP | Vehicle Speed Feedback (plaque) | 24x18 | 30x24 | 36x30 | 48x36 | — | — | Table 2C-1, manual p.150 |
|  | W14-1 | ROAD ENDS Signs | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150 |
| ![W14-1a](symbols/W14-1a.png) | W14-1a | Dead End, No Outlet (with arrow) | 36x9 | 36x9 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W14-2](symbols/W14-2.png) | W14-2 | Dead End, No Outlet | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W14-2a](symbols/W14-2a.png) | W14-2a | Dead End, No Outlet (with arrow) | 36x9 | 36x9 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-6, manual p.169 |
| ![W14-3](symbols/W14-3.png) | W14-3 | No Passing Zone | 48x48x36 | 48x48x36 | 64x64x48 | 64x64x48 | 40x40x30 | 64x64x48 | Table 2C-1, manual p.150; picture: Figure 2C-11, manual p.182 |
|  | W15-1 | Playground | 30x30 | 36x36 | 36x36 | — | 24x24 | 48x48 | Table 2C-1, manual p.150 |
| ![W16-1P](symbols/W16-1P.png) | W16-1P | In Road (plaque) | 18x12 | 18x12 | 24x18 | — | — | 24x18 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-1aP](symbols/W16-1aP.png) | W16-1aP | In Street (plaque) | 18x12 | 18x12 | 24x18 | — | — | 24x18 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-2P](symbols/W16-2P.png) | W16-2P | XX Feet (2-line plaque) | 24x18 | 24x18 | 30x24 | 30x24 | — | 30x24 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-2aP](symbols/W16-2aP.png) | W16-2aP | XX Ft (1-line plaque) | 24x12 | 24x12 | — | — | — | 30x18 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-3P](symbols/W16-3P.png) | W16-3P | XX Miles (2-line plaque) | 30x24 | 30x24 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-3aP](symbols/W16-3aP.png) | W16-3aP | XX Miles (1-line plaque) | 30x12 | 30x12 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-4P](symbols/W16-4P.png) | W16-4P | Next XX Feet (plaque) | 30x24 | 30x24 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-5P](symbols/W16-5P.png) | W16-5P | Supplemental Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-6P](symbols/W16-6P.png) | W16-6P | Supplemental Arrow (plaque) | 21x15 | 21x15 | — | — | — | 30x21 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-7aP](symbols/W16-7aP.png) | W16-7aP | Dual Downward Diagonal | 21x15 | 21x15 | — | — | — | 30x21 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-8P](symbols/W16-8P.png) | W16-8P | Advance Street Name | Variesx8 | Variesx8 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-8aP](symbols/W16-8aP.png) | W16-8aP | Advance Street Name | Variesx15 | Variesx15 | — | — | — | — | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-10P](symbols/W16-10P.png) | W16-10P | Photo Enforced (symbol plaque) | 24x12 | 24x12 | 36x18 | — | — | 48x24 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
| ![W16-10aP](symbols/W16-10aP.png) | W16-10aP | Photo Enforced (plaque) | 24x18 | 24x18 | 36x30 | — | — | 48x36 | Table 2C-1, manual p.150; picture: Figure 2C-16, manual p.195 |
|  | W16-11P | High-Occupancy Vehicles (plaque) | 24x12 | 24x12 | 30x18 | 30x18 | — | 30x18 | Table 2G-1, manual p.408 |
| ![W16-12P](symbols/W16-12P.png) | W16-12P | Traffic Circle (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-9, manual p.179 |
| ![W16-12aP](symbols/W16-12aP.png) | W16-12aP | Roundabout (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-9, manual p.179 |
| ![W16-13P](symbols/W16-13P.png) | W16-13P | When Flashing (plaque) | 24x18 | 24x18 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-16, manual p.195 |
| ![W16-15P](symbols/W16-15P.png) | W16-15P | New (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-16, manual p.195 |
| ![W16-16P](symbols/W16-16P.png) | W16-16P | Ticket (plaque) | — | — | — | — | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
| ![W16-16aP](symbols/W16-16aP.png) | W16-16aP | Last Exit Before Toll | — | — | 144x54 | 144x54 | — | — | Table 2F-1, manual p.381; picture: Figure 2F-4, manual p.386 |
|  | W16-17P | Toll (plaque) | 24x12 | 24x12 | 36x18 | 36x18 | 24x12 | 36x18 | Table 2F-1, manual p.381 |
| ![W16-18P](symbols/W16-18P.png) | W16-18P | Notice (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-16, manual p.195 |
|  | W16-19P | Last In Corridor (plaque) | 24x18 | 24x18 | 24x18 | 24x18 | — | — | Table 2H-1, manual p.461 |
| ![W16-20P](symbols/W16-20P.png) | W16-20P | Except Bicycles (plaque) | 24x12 | 24x12 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-16, manual p.195 |
| ![W16-21P](symbols/W16-21P.png) | W16-21P | 2-Way Bicycle Cross Traffic (plaque) | 24x12 | 24x12 | — | — | — | — | Table 9A-1, manual p.1050; picture: Figure 9C-1, manual p.1066 |
| ![W17-1](symbols/W17-1.png) | W17-1 | Speed Hump | 30x30 | 36x36 | — | — | 24x24 | 48x48 | Table 2C-1, manual p.151; picture: Figure 2C-7, manual p.174 |
| ![W18-1](symbols/W18-1.png) | W18-1 | No Traffic Signs | 30x30 | 36x36 | — | — | 24x24 | 36x36 | Table 2C-1, manual p.151; picture: Figure 2C-6, manual p.169 |
| ![W19-1](symbols/W19-1.png) | W19-1 | Freeway Ends XX Miles | — | — | — | 144x48 | — | — | Table 2C-1, manual p.151; picture: Figure 2C-6, manual p.169 |
| ![W19-2](symbols/W19-2.png) | W19-2 | Expressway Ends XX Miles | — | — | 144x48 | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-6, manual p.169 |
| ![W19-3](symbols/W19-3.png) | W19-3 | Freeway Ends | — | — | — | 48x48 | — | — | Table 2C-1, manual p.151; picture: Figure 2C-6, manual p.169 |
| ![W19-4](symbols/W19-4.png) | W19-4 | Expressway Ends | — | — | 48x48 | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-6, manual p.169 |
| ![W19-5](symbols/W19-5.png) | W19-5 | All Traffic Must Exit | — | — | 90x48 | 90x48 | — | — | Table 2C-1, manual p.151; picture: Figure 2C-6, manual p.169 |
|  | W19-7aP | Freeway or Expressway Ends Signs (W19 Series) | — | — | — | — | — | — | section text |
|  | W20-1 | Road Work (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
| ![W20-1b](symbols/W20-1b.png) | W20-1b | Path Work (with distance) | 36x36 | 36x36 | — | — | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W20-2](symbols/W20-2.png) | W20-2 | Detour (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W20-2a](symbols/W20-2a.png) | W20-2a | Bike Detour (with distance) | 36x36 | 36x36 | — | — | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
|  | W20-2b | Bike Diversion (with distance) | 36x36 | 36x36 | — | — | 30x30 | — | Table 6H-1, manual p.804 |
|  | W20-3 | Road Closed (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
| ![W20-3a](symbols/W20-3a.png) | W20-3a | Path Closed (with distance) | 36x36 | 36x36 | — | — | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W20-4](symbols/W20-4.png) | W20-4 | One Lane Road (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W20-5](symbols/W20-5.png) | W20-5 | Closed Signs | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W20-5a](symbols/W20-5a.png) | W20-5a | Lane(s) Closed (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W20-5b](symbols/W20-5b.png) | W20-5b | Bike Lane Closed (with distance) | 36x36 | 36x36 | — | — | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
|  | W20-7 | Flagger (symbol) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
|  | W20-7a | Flagger | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
|  | W20-8 | Slow (on Stop/Slow Paddle) | 18x18 | 18x18 | — | — | — | — | Table 6H-1, manual p.804 |
| ![W21-1](symbols/W21-1.png) | W21-1 | Workers | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
|  | W21-1a | Workers | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
|  | W21-2 | Fresh Oil | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
| ![W21-3](symbols/W21-3.png) | W21-3 | Road Machinery Ahead | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-4](symbols/W21-4.png) | W21-4 | Slow Moving Vehicle | 36x18 | 36x18 | — | — | — | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-5](symbols/W21-5.png) | W21-5 | Shoulder Work | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-5a](symbols/W21-5a.png) | W21-5a | Shoulder Closed | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-5b](symbols/W21-5b.png) | W21-5b | Shoulder Closed (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-6](symbols/W21-6.png) | W21-6 | Survey Crew | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-7](symbols/W21-7.png) | W21-7 | Utility Work (with distance) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W21-8](symbols/W21-8.png) | W21-8 | Mowing Ahead | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W22-1](symbols/W22-1.png) | W22-1 | Blasting Zone Ahead | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.801 |
| ![W22-3](symbols/W22-3.png) | W22-3 | End Blasting Zone | 42x36 | 42x36 | 42x36 | 42x36 | 36x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
| ![W23-1](symbols/W23-1.png) | W23-1 | Slow Traffic Ahead | 48x24 | 48x24 | 48x24 | 48x24 | — | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
| ![W23-2](symbols/W23-2.png) | W23-2 | New Traffic Pattern Ahead | 36x36 | 36x36 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-8, manual p.177 |
| ![W23-2a](symbols/W23-2a.png) | W23-2a | New Signal Operation Ahead | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.151; picture: Figure 2C-8, manual p.177 |
|  | W24-1 | Double Reverse Curve (1 lane) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804 |
| ![W24-1a](symbols/W24-1a.png) | W24-1a | Double Reverse Curve (2 lanes) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
| ![W24-1b](symbols/W24-1b.png) | W24-1b | Double Reverse Curve (3 lanes) | 36x36 | 36x36 | 48x48 | 48x48 | 30x30 | — | Table 6H-1, manual p.804; picture: Figure 6H-1, manual p.802 |
|  | W24-1cP | All Lanes (plaque) | 24x18 | 24x18 | 30x24 | 30x24 | — | — | Table 6H-1, manual p.804 |
| ![W25-1](symbols/W25-1.png) | W25-1 | Oncoming Traffic Has (May Have) | 24x30 | 24x30 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-9, manual p.179 |
| ![W25-2](symbols/W25-2.png) | W25-2 | Oncoming Traffic Has (May Have) | 24x30 | 24x30 | — | — | — | — | Table 2C-1, manual p.151; picture: Figure 2C-9, manual p.179 |
| ![W26-1](symbols/W26-1.png) | W26-1 | Watch for Stopped Traffic | 36x36 | 36x36 | 48x48 | 48x48 | — | — | Table 2C-1, manual p.151; picture: Figure 2C-8, manual p.177 |

## 4. Pavement markings

| Code | Name | Colour | Pattern | Width (in) | Unit | MUTCD |
|---|---|---|---|---|---|---|
| CL-DY | Center line double solid yellow | yellow | double_solid | 4 | m | 3B.02 |
| CL-BY | Center line broken yellow | yellow | broken_10_30 | 4 | m | 3B.02 |
| LL-BW | Lane line broken white | white | broken_10_30 | 4 | m | 3B.06 |
| EL-SW | Edge line solid white | white | solid | 4 | m | 3B.10 |
| EL-SY | Left edge line solid yellow | yellow | solid | 4 | m | 3B.10 |
| SL | Stop line | white | solid | 24 | m | 3B.19-05 (12 to 24 in) |
| YL | Yield line (shark teeth) | white | triangles | 12 | m | 3B.19-12 (base 12 to 24 in) |
| CW | Crosswalk | white | high_visibility | 12 | m2 | 3C.02 |
| LDRP | Lane drop dotted line (wide) | white | dotted_3_9 | 8 | m | 3B.07-07 and 3B.07-11 |
| NO-PASSING-STUDY | No-passing zone survey (study item) | yellow | study | 4 | m | 3B.02 / Table 3B-1 |
| RXR | Grade crossing X and RR symbol with transverse lines | white | symbol | 24 | ea | 8C.02 |

> normal line 4-6 in, wide line >= 2x normal, broken 10 ft / 30 ft (3A.06, manual p.538); stop line 12-24 in and yield-line triangles 12-24 in base (3B.19, p.573); lane-drop marking wide dotted white 3 ft / 9 ft (3B.07-07/11, p.553).

## 5. Tables used by the engine

### Table 2C-3 Advance placement of warning signs (feet; speeds mph)

| speed_mph | cond_a | b0 | b10 | b20 | b30 | b40 | b50 | b60 | b70 | b80 |
|---|---|---|---|---|---|---|---|---|---|---|
| 20 | 225 | 115 | — | — | — | — | — | — | — | — |
| 25 | 325 | 155 | — | — | — | — | — | — | — | — |
| 30 | 460 | 200 | — | — | — | — | — | — | — | — |
| 35 | 565 | 250 | — | — | — | — | — | — | — | — |
| 40 | 670 | 305 | 100 | 100 | — | — | — | — | — | — |
| 45 | 775 | 360 | 125 | 100 | 100 | — | — | — | — | — |
| 50 | 885 | 425 | 200 | 175 | 125 | 100 | — | — | — | — |
| 55 | 990 | 495 | 275 | 225 | 200 | 125 | — | — | — | — |
| 60 | 1100 | 570 | 350 | 325 | 275 | 200 | 100 | — | — | — |
| 65 | 1200 | 645 | 450 | 400 | 350 | 275 | 200 | 100 | — | — |
| 70 | 1250 | 730 | 525 | 500 | 450 | 375 | 275 | 150 | — | — |
| 75 | 1350 | 820 | 625 | 600 | 550 | 475 | 375 | 250 | 100 | — |
| 80 | 1475 | 910 | 725 | 700 | 625 | 550 | 450 | 350 | 200 | — |
| 85 | 1600 | 1010 | 825 | 800 | 750 | 675 | 575 | 450 | 300 | 150 |

> MUTCD 11th Ed. Table 2C-3 Guidelines for Advance Placement of Warning Signs (feet). Column cond_a = Condition A (speed reduction and lane changing in heavy traffic).
> Columns b0..b80 = Condition B by advisory speed (mph); b0 = potential stop. Blank = N/A (placement per site conditions, 0-100 ft, min 100 ft between signs).
> Source: FHWA MUTCD 11th Edition (Dec 2023), Chapter 2C, Table 2C-3. Verified row by row from the MUTCD 11th Ed. PDF (manual p.152) on 30 Sep 2026.

### Table 2C-4 Chart B Devices by speed differential

| diff_min_mph | devices |
|---|---|
| 5 | markings_or_sign |
| 10 | sign |
| 15 | sign+delineators |
| 20 | sign+chevrons |

> MUTCD 11th Ed. Table 2C-4 Chart B: devices by speed differential (posted/85th minus advisory, mph). Chart A (roadway type, AADT) decides whether devices are required.
> Verified from the MUTCD 11th Ed. PDF (Table 2C-4 Charts A and B, manual p.155) on 30 Sep 2026.

### Table 2C-5 Chevron spacing

| advisory_max_mph | advisory_max_kmh | radius_max_ft | spacing_ft |
|---|---|---|---|
| 15 | 20 | 200 | 40 |
| 30 | 50 | 400 | 80 |
| 45 | 70 | 700 | 120 |
| 60 | 100 | 1250 | 160 |
| 999 | 999 | 99999 | 200 |

> MUTCD 11th Ed. Table 2C-5 Typical Spacing of Chevron Alignment Signs on Horizontal Curves (2C.08-05). Verified from the MUTCD 11th Ed. PDF, manual p.158, 30 Sep 2026. (T&I's earlier screenshot labelled it 2C-6: that is the 2009 edition numbering.)
> Note in the table: the radius-advisory speed relationship shown should NOT be used to determine the advisory speed.
> advisory_max_kmh: AASHTO-style metric bands (15 mph ~ 20 km/h, 30 mph ~ 50 km/h, 45 mph ~ 70 km/h, 60 mph ~ 100 km/h). Advisory speeds are multiples of 10 km/h.

### Mounting height and lateral offset (2A.15 / 2A.16)

| context | min_height_ft | height_clause | height_provision | lateral_offset_ft | offset_reference | offset_clause | offset_provision |
|---|---|---|---|---|---|---|---|
| rural | 5 | 2A.15-04 | Standard | 12 | edge_of_traveled_way | 2A.16-03 | Guidance |
| urban | 7 | 2A.15-05 | Standard | 2 | face_of_curb | T&I default 2 ft; code minimum 1 ft (2A.16-10) | Option |
| freeway | 7 | 2A.15-11 | Standard | 12 | edge_of_traveled_way | 2A.16-03 | Guidance |

> MUTCD 11th Ed. Section 2A.15 (height) and 2A.16 (lateral offset). Units feet. Verified from the MUTCD 11th Ed. PDF (2A.15-04/05/11, 2A.16-03/10, manual pp.58-59) on 30 Sep 2026.

### Table 3B-1 Minimum passing sight distance

| speed_mph | psd_ft |
|---|---|
| 25 | 450 |
| 30 | 500 |
| 35 | 550 |
| 40 | 600 |
| 45 | 700 |
| 50 | 800 |
| 55 | 900 |
| 60 | 1000 |
| 65 | 1100 |
| 70 | 1200 |

> MUTCD 11th Ed. Table 3B-1 Minimum Passing Sight Distances for No-Passing Zone Markings (3B.02-04). Verified from the MUTCD 11th Ed. PDF (manual p.543) on 6 Oct 2026.

Table 2C-4 Chart A (need for curve devices) is applied in code: freeways/expressways Required; arterial or collector under 1,000 AADT Optional, 1,000-2,999 Recommended, 3,000-3,999 Required without markings / Recommended with markings, 4,000+ Required; all other roads Optional. Table 2C-6 (Advisory Speed plaque) is applied through the W13-1P plaque rule.

## 6. Verification status

Values were extracted from the public FHWA 11th Edition chapter PDFs through a summarising web reader, not a clean text copy. Every table carries "VERIFY before sign-off". A T&I engineer must check each table and clause against the printed manual before this rulebook governs a design. 30 Sep 2026: 2B.49, 2C.55, 3B.02, 3B.10, Table 2C-6 (plaque) and chevron spacing confirmed from T&I's copy (see docs/RULEBOOK_REVIEW.md). 30 Sep 2026: whole sign catalog (Tables 2B-1, 2C-1, 7B-1), Tables 2C-3, 2C-4, 2C-5, 2C-6 and mounting (2A.15/2A.16) verified against T&I's MUTCD 11th Edition PDF; sign pictures cropped from its figures (symbols/). 12 Oct 2026: automatic placement extended to 74 signs. Hazard points (hazards.yaml, 34 types: grade crossing, narrow or one-lane structure, low clearance, speed hump, bump/dip, pavement ends, downgrade, school bus stop, vehicle/animal crossings, surface and shoulder conditions, no-passing zone start, dead end / no outlet) and network-derived signs (divided section begins/ends, one-way to two-way, merge, added lane, W1-6 on turns). Clause text comes from the PDF text layer of T&I's copy; engine assumptions: Table 2C-3 Condition B 0 mph column when no advisory speed is given; Crossbuck 4.6 m (15 ft) + half gauge before the track; 40 mph = 60 km/h for RXR markings (8C.02-02).
