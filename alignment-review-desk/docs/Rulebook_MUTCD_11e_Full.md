# Rule book: every sign in the MUTCD 11th Edition

T&I Transportation Systems, road signing skill. Generated 12 Oct 2026. 1065 signs and plaques, 837 with a picture from the manual. Results are DRAFT until a T&I engineer signs the rulebook off.

## How to read it

- Signs are grouped under the MUTCD section that governs them; each group shows its signs, then the section's rules once.
- Rule tags: **[M]** Mandatory (Standard, "shall"), **[R]** Recommended (Guidance, "should"), [O] Optional (Option, "may"), [S] Support (information).
- A paragraph marked ◆ names the sign(s) shown after it; unmarked paragraphs apply to the whole group.
- *Default class* is the class the engine gives a sign placed by the designer: the strongest paragraph that says the sign shall / should / may be used (its reference is shown). The real need always depends on the condition in that paragraph.
- Sizes are inches (width x height; diamond and square signs are side x side) from the MUTCD size tables. Other contexts (work zones, grade crossings, bicycle facilities) are listed under *Also sized in*.
- Automatic placement: signs the engine places from the network carry *Auto*; all others are placed by the designer as a point with `type: sign` and `code`, and the engine sizes, classes, mounts and schedules them.

## Contents

- **2A General**
  - [2A.11 Enhanced Conspicuity for Standard Signs](#sec-2A-11) (1)
  - [2A.22 Maintaining Minimum Retrorefectivityl](#sec-2A-22) (1)
- **2B Regulatory Signs**
  - [2B.04 STOP Sign (R1-1) and ALL-WAY Plaque (R1-3P)](#sec-2B-04) (3)
  - [2B.05 YIELD Sign (R1-2)](#sec-2B-05) (1)
  - [2B.18 STOP Sign or YIELD Sign Placement](#sec-2B-18) (3)
  - [2B.19 Yield Here To Pedestrians Signs and Stop Here For Pedestrians Signs (R1-5 Series)](#sec-2B-19) (4)
  - [2B.20 In-Street and Overhead Pedestrian and Trail Crossing Signs (R1-6 and R1-9 Series)](#sec-2B-20) (10)
  - [2B.21 Speed Limit Sign (R2-1)](#sec-2B-21) (7)
  - [2B.22 Vehicle Speed Limit Plaques (R2-2P Series)](#sec-2B-22) (4)
  - [2B.23 Night Speed Limit Plaque (R2-3P)](#sec-2B-23) (1)
  - [2B.24 Minimum Speed Limit Plaque (R2-4P) and Combined Maximum and Minimum Speed Limits Sign (R2-4a)](#sec-2B-24) (2)
  - [2B.25 Higher Fines Signs and Plaque (R2-6P, R2-10, and R2-11)](#sec-2B-25) (5)
  - [2B.26 Movement Prohibition Signs (R3-1 through R3-4, R3-18, and R3-27)](#sec-2B-26) (13)
  - [2B.28 Mandatory Movement Lane Control Signs (R3-5, R3-5a, R3-7, R3-19 Series, and R3-20) and Plaques](#sec-2B-28) (20)
  - [2B.29 Optional Movement Lane Control Signs (R3-6 Series)](#sec-2B-29) (3)
  - [2B.31 RIGHT (LEFT) LANE MUST EXIT Signs (R3-33, R3-33a)](#sec-2B-31) (2)
  - [2B.32 Two-Way Left-Turn-Only Signs (R3-9a and R3-9b) and Plaques](#sec-2B-32) (2)
  - [2B.33 BEGIN and END Plaques (R3-9cP and R3-9dP)](#sec-2B-33) (2)
  - [2B.34 Reversible Lane Control Signs (R3-9e through R3-9i)](#sec-2B-34) (5)
  - [2B.35 Jughandle Signs (R3-23, R3-24, R3-25, and R3-26 Series)](#sec-2B-35) (10)
  - [2B.36 DO NOT PASS Sign (R4-1)](#sec-2B-36) (1)
  - [2B.37 PASS WITH CARE Sign (R4-2)](#sec-2B-37) (1)
  - [2B.38 KEEP RIGHT EXCEPT TO PASS Sign (R4-16), SLOWER TRAFFIC KEEP RIGHT Sign (R4-3), and TRUCKS USE RIGHT LANE Sign (R4-5)](#sec-2B-38) (3)
  - [2B.39 Keep Right and Keep Left Signs (R4-7 Series and R4-8 Series)](#sec-2B-39) (8)
  - [2B.40 STAY IN LANE Sign (R4-9)](#sec-2B-40) (1)
  - [2B.41 RUNAWAY VEHICLES ONLY Sign (R4-10)](#sec-2B-41) (1)
  - [2B.42 Slow Vehicle Turn-Out Signs (R4-12, R4-13, and R4-14)](#sec-2B-42) (3)
  - [2B.43 DO NOT DRIVE ON SHOULDER Sign (R4-17) and DO NOT PASS ON SHOULDER Sign (R4-18)](#sec-2B-43) (2)
  - [2B.44 ALL TRAFFIC Sign (R4-20) and RIGHT (LEFT) TURN ONLY Sign (R4-21)](#sec-2B-44) (2)
  - [2B.45 Selective Exclusion Signs and Plaques](#sec-2B-45) (20)
  - [2B.46 DO NOT ENTER Sign (R5-1)](#sec-2B-46) (1)
  - [2B.47 WRONG WAY Sign (R5-1a)](#sec-2B-47) (1)
  - [2B.49 ONE WAY Signs (R6-1 and R6-2)](#sec-2B-49) (4)
  - [2B.50 Divided Highway Crossing Signs (R6-3 and R6-3a)](#sec-2B-50) (2)
  - [2B.51 Roundabout Circulation Plaque (R6-5P)](#sec-2B-51) (1)
  - [2B.52 Parking, Standing, and Stopping Signs (R7 and R8 Series)](#sec-2B-52) (34)
  - [2B.53 Design of Parking, Standing, and Stopping Signs](#sec-2B-53) (12)
  - [2B.55 Emergency Restriction Signs (R8-4 and R8-7)](#sec-2B-55) (2)
  - [2B.56 WALK ON LEFT FACING TRAFFIC and No Hitchhiking Signs (R9-1, R9-4, and R9-4a)](#sec-2B-56) (3)
  - [2B.57 Pedestrian Crossing Signs (R9-2 and R9-3)](#sec-2B-57) (4)
  - [2B.58 Traffc Signal Pedestrian and Bicyclist Actuation Signs (R10i -1 through R10-4 and R10-24 through R10-26)](#sec-2B-58) (16)
  - [2B.59 Traffc Signal Signs and Plaques (R10i -5 through R10-30)](#sec-2B-59) (21)
  - [2B.60 No Turn on Red Signs (R10-11 Series, R10-17a, and R10-30)](#sec-2B-60) (8)
  - [2B.61 Ramp Metering Signs (R10-28 and R10-29)](#sec-2B-61) (2)
  - [2B.62 KEEP OFF MEDIAN Sign (R11-1)](#sec-2B-62) (1)
  - [2B.63 ROAD CLOSED Sign (R11-2) and LOCAL TRAFFIC ONLY Signs (R11-3 Series, R11-4)](#sec-2B-63) (8)
  - [2B.64 Weight Limit Signs (R12-1 through R12-7)](#sec-2B-64) (7)
  - [2B.65 Weigh Station Sign (R13-1)](#sec-2B-65) (1)
  - [2B.66 TRUCK ROUTE Sign (R14-1)](#sec-2B-66) (1)
  - [2B.67 Hazardous Material Signs (R14-2 and R14-3)](#sec-2B-67) (2)
  - [2B.68 National Network Signs (R14-4 and R14-5)](#sec-2B-68) (2)
  - [2B.69 Photo Enforced Signs and Plaques (R10-18, R10-18a, R10-19P, R10-19aP)](#sec-2B-69) (4)
  - [2B.70 Move Vehicles from Travel Lanes Sign (R16-4)](#sec-2B-70) (1)
  - [2B.71 Move Over or Reduce Speed Sign (R16-3)](#sec-2B-71) (1)
  - [2B.72 No Hand-Held Phone Use by Driver Signs (R16-15 and R16-15a)](#sec-2B-72) (2)
  - [2B.73 Headlight Use Signs (R16-5 through R16-11)](#sec-2B-73) (7)
- **2C Warning Signs and Object Markers**
  - [2C.07 Horizontal Alignment Signs (W1-1 through W1-5, W1-11, and W1-15)](#sec-2C-07) (7)
  - [2C.08 Chevron Alignment Sign (W1-8)](#sec-2C-08) (1)
  - [2C.09 Combination Horizontal Alignment/Intersection Signs (W1-10 Series)](#sec-2C-09) (6)
  - [2C.10 One-Direction Large Arrow Sign (W1-6)](#sec-2C-10) (1)
  - [2C.11 Truck Rollover Sign (W1-13)](#sec-2C-11) (1)
  - [2C.12 Advisory Exit and Ramp Speed Signs (W13-2 and W13-3) and Combination Horizontal Alignment/Advisory Exit and Ramp Speed Signs (W13-6 through W13-13)](#sec-2C-12) (10)
  - [2C.13 Vehicle Speed Feedback Sign and Plaque (W13-20 and W13-20aP)](#sec-2C-13) (2)
  - [2C.14 Hill Signs (W7-1 and W7-1a)](#sec-2C-14) (2)
  - [2C.15 Truck Escape Ramp Signs (W7-4 Series)](#sec-2C-15) (6)
  - [2C.16 HILL BLOCKS VIEW Sign (W7-6)](#sec-2C-16) (1)
  - [2C.17 ROAD NARROWS Sign (W5-1)](#sec-2C-17) (1)
  - [2C.18 NARROW BRIDGE and NARROW UNDERPASS Signs (W5-2 and W5-2a)](#sec-2C-18) (2)
  - [2C.19 ONE LANE BRIDGE and ONE LANE UNDERPASS Signs (W5-3 and W5-3a)](#sec-2C-19) (2)
  - [2C.20 Divided Highway Sign (W6-1)](#sec-2C-20) (1)
  - [2C.21 Divided Highway Ends Sign (W6-2)](#sec-2C-21) (1)
  - [2C.22 Freeway or Expressway Ends Signs (W19 Series)](#sec-2C-22) (6)
  - [2C.23 Double Arrow Sign (W12-1)](#sec-2C-23) (1)
  - [2C.24 DEAD END, NO OUTLET, and ROAD ENDS Signs (W14-1, W14-1a, W14-2, W14-2a, W8-26, and W8-26a)](#sec-2C-24) (6)
  - [2C.25 Low Clearance Signs (W12-2, W12-2a, and W12-2b)](#sec-2C-25) (3)
  - [2C.26 BUMP and DIP Signs (W8-1 and W8-2)](#sec-2C-26) (2)
  - [2C.27 SPEED HUMP Sign (W17-1)](#sec-2C-27) (1)
  - [2C.28 PAVEMENT ENDS Sign (W8-3)](#sec-2C-28) (1)
  - [2C.29 Shoulder Signs (W8-4, W8-9, W8-17, W8-23, and W8-25)](#sec-2C-29) (6)
  - [2C.30 Surface Condition Signs (W8-5, W8-7, W8-8, W8-11, W8-13, and W8-14)](#sec-2C-30) (10)
  - [2C.31 Warning Signs and Plaque for Motorcyclists (W8-15, W8-15aP, and W8-16)](#sec-2C-31) (3)
  - [2C.32 NO CENTER LINE Sign (W8-12)](#sec-2C-32) (1)
  - [2C.33 NO TRAFFIC SIGNS Sign (W18-1)](#sec-2C-33) (1)
  - [2C.34 Weather Condition Signs (W8-18, W8-19, W8-21, and W8-22)](#sec-2C-34) (4)
  - [2C.35 Advance Traffc Control Signs (W3i -1, W3-2, W3-3, and W3-4)](#sec-2C-35) (4)
  - [2C.36 DRAW BRIDGE Sign (W3-6)](#sec-2C-36) (1)
  - [2C.37 Advance Ramp Control Signal Signs (W3-7 and W3-8)](#sec-2C-37) (2)
  - [2C.38 NEW TRAFFIC PATTERN and NEW SIGNAL OPERATION AHEAD Signs (W23-2 and W23-2a)](#sec-2C-38) (2)
  - [2C.39 WATCH FOR STOPPED TRAFFIC Sign (W26-1)](#sec-2C-39) (1)
  - [2C.40 Reduced Speed Limit Ahead and Speed Zone Signs (W3-5, W3-5a, W3-5b, and W3-5c)](#sec-2C-40) (4)
  - [2C.41 Intersection Warning Signs (W2-1 through W2-8)](#sec-2C-41) (11)
  - [2C.42 Actuated Advance Intersection Signs (W2-10 and W2-11)](#sec-2C-42) (2)
  - [2C.43 Two-Direction Large Arrow Sign (W1-7)](#sec-2C-43) (1)
  - [2C.44 Traffic Signal Oncoming Extended Green Signs (W25-1 and W25-2)](#sec-2C-44) (2)
  - [2C.45 Merge Signs and Plaque (W4-1, W4-5, and W4-5aP)](#sec-2C-45) (3)
  - [2C.46 Added Lane Signs (W4-3 and W4-6)](#sec-2C-46) (2)
  - [2C.47 Lane Ends Signs (W4-2 and W9-1)](#sec-2C-47) (2)
  - [2C.48 Lanes Merge Signs (W9-4 and W4-8)](#sec-2C-48) (2)
  - [2C.49 HEAVY MERGE FROM LEFT (RIGHT) Sign (W4-7)](#sec-2C-49) (1)
  - [2C.50 RIGHT (LEFT) LANE FOR EXIT ONLY Sign (W9-7)](#sec-2C-50) (1)
  - [2C.51 Two-Way Traffc Sign (W6i -3)](#sec-2C-51) (1)
  - [2C.52 Two-Way Traffc on a Threei -Lane Roadway Signs (W6-5 and W6-5a)](#sec-2C-52) (2)
  - [2C.53 NO PASSING ZONE Sign (W14-3)](#sec-2C-53) (1)
  - [2C.54 Vehicular Traffc Warning Signs (W8i -6, W11-1, W11-5, W11-8, W11-10, W11-11, W11- 12P, W11-14, W11-15, and W11-15a)](#sec-2C-54) (11)
  - [2C.55 Non-Vehicular Warning Signs (W11-2, W11-3, W11-4, W11-6, W11-7, W11-9, and W11-16 through W11-22)](#sec-2C-55) (15)
  - [2C.56 Playground Sign (W15-1)](#sec-2C-56) (1)
  - [2C.59 Advisory Speed Plaque (W13-1P) and Confirmation Advisory Speed Plaque (W13-1aP)](#sec-2C-59) (2)
  - [2C.60 NEW Plaque (W16-15P)](#sec-2C-60) (1)
  - [2C.61 Distance Plaques (W16-2 Series, W16-3 Series, W16-4P, and W7-3aP)](#sec-2C-61) (6)
  - [2C.62 Supplemental Arrow Plaques (W16-5P and W16-6P)](#sec-2C-62) (2)
  - [2C.63 Diagonal Downward-Pointing Arrow Plaques (W16-7P and W16-7aP)](#sec-2C-63) (2)
  - [2C.64 Hill-Related Plaques (W7-2 Series and W7-3 Series)](#sec-2C-64) (4)
  - [2C.65 Advance Street Name Plaques (W16-8P and W16-8aP)](#sec-2C-65) (2)
  - [2C.66 Traffc Does Not Stop Plaques (W4i -4P Series)](#sec-2C-66) (3)
  - [2C.67 IN ROAD and IN STREET Plaques (W16-1P and W16-1aP)](#sec-2C-67) (2)
  - [2C.68 EXCEPT BICYCLES Plaque (W16-20P)](#sec-2C-68) (1)
  - [2C.69 Photo Enforced Plaques (W16-10P and W16-10aP)](#sec-2C-69) (2)
  - [2C.70 Object Marker Design and Placement Height](#sec-2C-70) (6)
- **2D Guide Signs, Conventional Roads**
  - [2D.11 Design of Route Signs](#sec-2D-11) (8)
  - [2D.13 Junction Auxiliary Plaque (M2-1P)](#sec-2D-13) (1)
  - [2D.14 Combination Junction Sign (M2-2)](#sec-2D-14) (1)
  - [2D.15 Cardinal Direction Auxiliary Plaques (M3-1P through M3-4P)](#sec-2D-15) (4)
  - [2D.17 ALTERNATE Auxiliary Plaques (M4-1P and M4-1aP)](#sec-2D-17) (2)
  - [2D.18 BY-PASS Auxiliary Plaque (M4-2P)](#sec-2D-18) (1)
  - [2D.19 BUSINESS Auxiliary Plaque (M4-3P)](#sec-2D-19) (1)
  - [2D.20 TRUCK Auxiliary Plaque (M4-4P)](#sec-2D-20) (1)
  - [2D.21 TO Auxiliary Plaque (M4-5P)](#sec-2D-21) (1)
  - [2D.22 END Auxiliary Plaque (M4-6P)](#sec-2D-22) (1)
  - [2D.23 BEGIN Auxiliary Plaque (M4-14P)](#sec-2D-23) (1)
  - [2D.24 TEMPORARY Auxiliary Plaques (M4-7P and M4-7aP)](#sec-2D-24) (2)
  - [2D.26 Advance Turn Arrow Auxiliary Plaques (M5-1P, M5-2P, and M5-3P)](#sec-2D-26) (3)
  - [2D.27 Lane Designation Auxiliary Plaques (M5-4P, M5-5P, and M5-6P)](#sec-2D-27) (3)
  - [2D.28 Directional Arrow Auxiliary Plaques (M6 Series)](#sec-2D-28) (8)
  - [2D.36 Destination Signs (D1 Series)](#sec-2D-36) (6)
  - [2D.38 Combination Lane-Use/Destination Overhead Guide Sign (D15-1)](#sec-2D-38) (1)
  - [2D.39 Destination Signs at Circular Intersections](#sec-2D-39) (6)
  - [2D.43 Distance Signs (D2 Series)](#sec-2D-43) (3)
  - [2D.45 Street Name Signs (D3-1 and D3-1a)](#sec-2D-45) (2)
  - [2D.46 Advance Street Name Signs (D3-2 Series)](#sec-2D-46) (1)
  - [2D.47 Parking Area Guide Sign (D4-1)](#sec-2D-47) (1)
  - [2D.48 PARK - RIDE Sign (D4-2)](#sec-2D-48) (1)
  - [2D.50 Freeway Entrance Signs (D13-3 and D13-3a)](#sec-2D-50) (2)
  - [2D.51 WEIGH STATION Signing (D8 Series)](#sec-2D-51) (4)
  - [2D.52 Crossover Signs (D13-1 and D13-2)](#sec-2D-52) (2)
  - [2D.53 Truck and Passing Lane Signs (D17-1 through D17-4)](#sec-2D-53) (4)
  - [2D.54 Emergency and Slow Vehicle Turn-Out Signs (D17-5 through D17-7)](#sec-2D-54) (3)
  - [2D.57 National Scenic Byways Sign and Plaque (M10-1 and M10-1aP)](#sec-2D-57) (2)
  - [2D.58 State-Designated Scenic Byway, Historic Trail, and Auto Tour Route Signs](#sec-2D-58) (10)
  - [2D.59 Emergency Routing Signs and Plaques (M4-11 and M4-12 Series)](#sec-2D-59) (5)
- **2E Guide Signs, Freeways and Expressways**
  - [2E.23 Interchange Advance Guide Signs (E1-1 through E1-3)](#sec-2E-23) (16)
  - [2E.24 Interchange Sequence Signs (E9-1 and E9-2)](#sec-2E-24) (3)
  - [2E.25 Exit Direction Signs (E4 Series)](#sec-2E-25) (4)
  - [2E.26 Exit Gore Signs and Plaque (E5-1 Series)](#sec-2E-26) (4)
  - [2E.27 Pull-Through Signs (E6-1 Series and E6-2 Series)](#sec-2E-27) (4)
  - [2E.28 Signing for Interchange Lane Drops without an Optional Exit Lane Standard:](#sec-2E-28) (7)
  - [2E.46 Next Exit Plaques (E2-1P and E2-1aP)](#sec-2E-46) (2)
  - [2E.48 Post-Interchange Distance Signs (E7-1 through E7-3)](#sec-2E-48) (3)
  - [2E.49 Post-Interchange Travel Time Sign (E7-4)](#sec-2E-49) (1)
  - [2E.50 Distance and Travel Time Sign (E7-5) and Comparative Travel Time Sign (E7-6)](#sec-2E-50) (2)
  - [2E.51 Supplemental Guide Signs (E3 Series)](#sec-2E-51) (2)
  - [2E.52 Community Interchanges Identifcation Signs (E9i -4 and E9-5)](#sec-2E-52) (2)
  - [2E.53 Next Exits Signs (E9-3 and E9-3a)](#sec-2E-53) (2)
  - [2E.56 Eisenhower Interstate System Signs (M1-10 and M1-10a)](#sec-2E-56) (2)
- **2F Toll Road Signs**
  - [2F.04 Regulatory Signs for Toll Plazas](#sec-2F-04) (3)
  - [2F.05 Electronic Toll Collection (ETC) Account-Only Regulatory Sign and Plaque (R3-31 and R3-32P)](#sec-2F-05) (2)
  - [2F.06 Pay Toll and Take Ticket Advance Warning Signs (W9-6 and W9-6e)](#sec-2F-06) (2)
  - [2F.07 Pay Toll and Take Ticket Advance Warning Plaques (W9-6bP, W9-6dP, and W9-6gP)](#sec-2F-07) (2)
  - [2F.08 Stop Ahead Pay Toll and Take Ticket Warning Signs (W9-6a and W9-6f)](#sec-2F-08) (2)
  - [2F.09 Stop Ahead Pay Toll and Take Ticket Warning Plaques (W9- 6cP and W9-6hP)](#sec-2F-09) (3)
  - [2F.10 LAST EXIT BEFORE TOLL Warning Plaques (W16-16P and W16-16aP)](#sec-2F-10) (2)
  - [2F.11 TOLL Warning Plaque (W16-17P)](#sec-2F-11) (1)
  - [2F.12 Toll Facility and Toll Plaza Guide Signs – General](#sec-2F-12) (2)
- **2G Preferential and Managed Lane Signs**
  - [2G.04 Vehicle Occupancy Definition Signs (R3-10 Series and R3-13 Series)](#sec-2G-04) (4)
  - [2G.05 Preferential Lane Operation Signs (R3-11 Series and R3-14 Series)](#sec-2G-05) (17)
  - [2G.06 Preferential Lane Advance Signs (R3-12, R3-12e, R3-12f, R3-15, R3-15a, and R3-15d)](#sec-2G-06) (6)
  - [2G.07 Preferential Lane Ends Signs (R3-12a, R3-12b, R3-12c, R3-12d, R3-12g, R3-12h,](#sec-2G-07) (9)
  - [2G.09 High-Occupancy Vehicle (HOV) Plaque (W16-11P)](#sec-2G-09) (1)
  - [2G.10 Preferential Lane Guide Signs – General](#sec-2G-10) (5)
  - [2G.13 Signing for Egress from Preferential Lanes to General-Purpose Lanes](#sec-2G-13) (2)
  - [2G.15 Signing for Direct Exits from Preferential Lanes to Another Highway](#sec-2G-15) (1)
  - [2G.18 Regulatory Signs for Priced Managed Lanes Standard:](#sec-2G-18) (13)
  - [2G.21 Regulatory Signs and Plaques for Part-Time Travel on a Shoulder](#sec-2G-21) (11)
  - [2G.22 Warning Signs for Part-Time Travel on a Shoulder](#sec-2G-22) (1)
  - [2G.24 Lane-Use Control Signals for Part-Time Travel on a Shoulder](#sec-2G-24) (1)
- **2H General Information Signs**
  - [2H.01 Scope](#sec-2H-01) (9)
  - [2H.04 Traffc Signal Speed Sign (I1i -1)](#sec-2H-04) (1)
  - [2H.05 Jurisdictional Boundary Signs (I2-1)](#sec-2H-05) (1)
  - [2H.06 Geographical Feature Signs (I2-2)](#sec-2H-06) (1)
  - [2H.08 Future Interstate Corridor Signs (I2-4 and I2-4a)](#sec-2H-08) (2)
  - [2H.09 Project Information Sign (I2-5)](#sec-2H-09) (1)
  - [2H.10 Grade-Separated Roadway Identifcation Signs (I2i -3 and I2-3a)](#sec-2H-10) (2)
  - [2H.11 Reference Location Signs (D10-1 through D10-3) and Intermediate Reference Location Signs (D10-1a through D10-3a)](#sec-2H-11) (6)
  - [2H.12 Enhanced Reference Location Signs (D10-4) and Intermediate Enhanced Reference](#sec-2H-12) (2)
  - [2H.13 Acknowledgment Signs and Plaques (I20 Series)](#sec-2H-13) (6)
  - [2H.14 Alternative Fuels Corridor Sign (D9-19)](#sec-2H-14) (5)
- **2I General Service Signs**
  - [2I.02 General Service Signs for Conventional Roads](#sec-2I-02) (31)
  - [2I.03 General Service Signs for Freeways and Expressways](#sec-2I-03) (9)
  - [2I.04 Interstate Oasis Signing (D5-12 Series)](#sec-2I-04) (3)
  - [2I.05 Rest Area and Other Roadside Area Signs (D5-1 through D5-11 Series)](#sec-2I-05) (15)
  - [2I.06 Brake Check Area Signs (D5-13 and D5-14)](#sec-2I-06) (2)
  - [2I.07 Chain-Up Area Signs (D5-15 and D5-16)](#sec-2I-07) (2)
  - [2I.08 Tourist Information and Welcome Center Signs (D5-7 Series and D5-8)](#sec-2I-08) (3)
  - [2I.09 Radio Information Signing (D12-1 Series)](#sec-2I-09) (3)
  - [2I.10 Channel 9 Monitored Sign (D12-3)](#sec-2I-10) (1)
  - [2I.11 EMERGENCY CALL 911 Sign (D12-4)](#sec-2I-11) (1)
  - [2I.12 TRAVEL INFO CALL 511 Signs (D12-5 and D12-5a)](#sec-2I-12) (2)
  - [2I.13 Roadside Assistance Sign (D12-6)](#sec-2I-13) (1)
  - [2I.14 Carpool and Ridesharing Signing (D12-2)](#sec-2I-14) (1)
  - [2I.15 Signing for Truck Parking Availability (D9-16b through D9-16e)](#sec-2I-15) (4)
- **2N Emergency Management Signing**
  - [2N.03 Evacuation Route Signs (EM1 Series)](#sec-2N-03) (4)
  - [2N.04 AREA CLOSED Sign (EM2-1)](#sec-2N-04) (1)
  - [2N.05 TRAFFIC CONTROL POINT Sign (EM2-2)](#sec-2N-05) (1)
  - [2N.06 MAINTAIN TOP SAFE SPEED Sign (EM2-3)](#sec-2N-06) (1)
  - [2N.07 Permit Required Sign (EM2-4)](#sec-2N-07) (1)
  - [2N.08 Emergency Aid Center Signs (EM3-1 Series)](#sec-2N-08) (4)
  - [2N.09 Shelter Directional Signs (EM4-1 Series)](#sec-2N-09) (4)
- **6D **
  - [6D.02 STOP/SLOW Paddle for Hand-Signaling](#sec-6D-02) (1)
- **6G TTC Regulatory Signs**
  - [6G.03 Regulatory Sign Applications](#sec-6G-03) (1)
  - [6G.07 STAY IN LANE Signs (R4-9 and R4-9a)](#sec-6G-07) (1)
  - [6G.08 Work Zone and Higher Fines Signs and Plaques](#sec-6G-08) (2)
  - [6G.09 PEDESTRIAN CROSSWALK Sign (R9-8)](#sec-6G-09) (1)
  - [6G.10 SIDEWALK CLOSED Signs (R9-9, R9-10, R9-11, and R9-11a)](#sec-6G-10) (4)
  - [6G.11 TURN OFF 2-WAY RADIO AND CELL PHONE Sign (R22-2)](#sec-6G-11) (1)
- **6H TTC Warning Signs**
  - [6H.01 Warning Sign Function, Design, and Application](#sec-6H-01) (1)
  - [6H.03 ROAD (STREET) WORK Sign (W20-1)](#sec-6H-03) (1)
  - [6H.04 DETOUR Sign (W20-2)](#sec-6H-04) (1)
  - [6H.05 ROAD (STREET) CLOSED Sign (W20-3)](#sec-6H-05) (1)
  - [6H.06 ONE LANE ROAD Sign (W20-4)](#sec-6H-06) (1)
  - [6H.07 Lane(s) Closed Signs (W20-5, W20-5a, and W9-3)](#sec-6H-07) (3)
  - [6H.09 ON RAMP Plaque (W13-4P)](#sec-6H-09) (1)
  - [6H.10 RAMP NARROWS Sign (W5-4)](#sec-6H-10) (1)
  - [6H.11 SLOW TRAFFIC AHEAD Sign (W23-1)](#sec-6H-11) (1)
  - [6H.12 EXIT OPEN and EXIT CLOSED Signs (E5-2 and E5-2a)](#sec-6H-12) (2)
  - [6H.13 EXIT ONLY Sign (E5-3)](#sec-6H-13) (1)
  - [6H.15 Flagger Signs (W20-7 and W20-7a)](#sec-6H-15) (2)
  - [6H.17 Narrow Two-Way Traffic Sign (W6-4)](#sec-6H-17) (1)
  - [6H.18 Workers Signs (W21-1 and W21-1a)](#sec-6H-18) (2)
  - [6H.19 FRESH OIL (TAR) Sign (W21-2)](#sec-6H-19) (1)
  - [6H.20 ROAD MACHINERY AHEAD Sign (W21-3)](#sec-6H-20) (1)
  - [6H.22 Shoulder Work Signs (W21-5, W21-5a, and W21-5b)](#sec-6H-22) (3)
  - [6H.23 SURVEY CREW Sign (W21-6)](#sec-6H-23) (1)
  - [6H.24 UTILITY WORK Sign (W21-7)](#sec-6H-24) (1)
  - [6H.25 Signs for Blasting Areas](#sec-6H-25) (2)
  - [6H.28 STEEL PLATE AHEAD Sign (W8-24)](#sec-6H-28) (1)
  - [6H.30 Reverse Curve Signs (W1-4 Series)](#sec-6H-30) (2)
  - [6H.31 Double Reverse Curve Signs (W24-1 Series)](#sec-6H-31) (4)
  - [6H.35 ROAD WORK NEXT XX MILES Sign (G20-1)](#sec-6H-35) (1)
  - [6H.36 END ROAD WORK Sign (G20-2)](#sec-6H-36) (1)
  - [6H.37 PILOT CAR FOLLOW ME Sign (G20-4)](#sec-6H-37) (1)
- **6I TTC Guide Signs**
  - [6I.02 Detour Signs and Plaques (M4-8P, M4-8a, M4-8bP, M4-9, M4-9a, M4-9b, M4-9c, and M4-10)](#sec-6I-02) (7)
- **6L **
  - [6L.03 STOP/SLOW Automated Flagger Assistance Devices](#sec-6L-03) (2)
- **6N **
  - [6N.04 Work Affecting Pedestrian and Bicycle Facilities](#sec-6N-04) (1)
  - [6N.05 Work Outside of the Shoulder](#sec-6N-05) (2)
  - [6N.19 Late Merge](#sec-6N-19) (1)
- **6P **
  - [6P.01 Typical Applications](#sec-6P-01) (6)
- **7B School Signs**
  - [7B.02 School Area Signs and Plaques](#sec-7B-02) (4)
  - [7B.03 School Crossing Signs](#sec-7B-03) (4)
  - [7B.04 School Bus Stop Signs](#sec-7B-04) (2)
  - [7B.05 School Speed Limit Signs and Plaques](#sec-7B-05) (6)
  - [7B.06 Higher Fines Zone Signs and Plaques in School Areas](#sec-7B-06) (2)
- **8B Grade Crossing Signs and Markings**
  - [8B.03 Grade Crossing (Crossbuck) Sign (R15-1) and Number of Tracks Plaque (R15-2P) at Active and Passive Grade Crossings](#sec-8B-03) (2)
  - [8B.06 Grade Crossing Advance Warning Signs (W10-1 through W10-4)](#sec-8B-06) (6)
  - [8B.07 DO NOT STOP ON TRACKS Sign (R8-8)](#sec-8B-07) (1)
  - [8B.08 TRACKS OUT OF SERVICE Sign (R8-9)](#sec-8B-08) (1)
  - [8B.09 STOP HERE WHEN FLASHING Signs (R8-10 and R8-10a)](#sec-8B-09) (2)
  - [8B.11 EXEMPT Grade Crossing Plaques (R15-3P and W10-1aP)](#sec-8B-11) (2)
  - [8B.12 Light Rail Transit Only Lane Signs (R15-4 Series)](#sec-8B-12) (4)
  - [8B.13 Do Not Pass Light Rail Transit Signs (R15-5 and R15-5a)](#sec-8B-13) (2)
  - [8B.14 No Motor Vehicles on Tracks Signs (R15-6 and R15-6a)](#sec-8B-14) (2)
  - [8B.15 Divided Highway with Light Rail Transit Crossing Signs (R15-7 Series)](#sec-8B-15) (2)
  - [8B.16 Low Ground Clearance Grade Crossing Sign (W10-5)](#sec-8B-16) (2)
  - [8B.17 Light Rail Transit Approaching-Activated Blank-Out Warning Sign (W10-7)](#sec-8B-17) (1)
  - [8B.18 Another Train Coming Sign (W10-16)](#sec-8B-18) (1)
  - [8B.19 TRAINS MAY EXCEED 80 MPH Sign (W10-8)](#sec-8B-19) (1)
  - [8B.20 NO TRAIN HORN Sign or Plaque (W10-9 and W10-9P)](#sec-8B-20) (2)
  - [8B.21 Storage Space Signs (W10-11, W10-11a, and W10-11b)](#sec-8B-21) (3)
  - [8B.22 Skewed Crossing Sign (W10-12)](#sec-8B-22) (1)
  - [8B.23 NO GATES OR LIGHTS Plaque (W10-13P)](#sec-8B-23) (1)
  - [8B.24 Next Crossing Plaques (W10-14P and W10-14aP)](#sec-8B-24) (2)
  - [8B.25 ROUGH CROSSING Plaque (W10-15P)](#sec-8B-25) (1)
  - [8B.27 Emergency Notifcation System Sign (I13i -1)](#sec-8B-27) (1)
- **8D **
  - [8D.10 Movements Prohibited During Preemption](#sec-8D-10) (2)
  - [8D.11 Pre-Signals at or Near Grade Crossings](#sec-8D-11) (2)
- **8E **
  - [8E.03 Pathway and Sidewalk Grade Crossing Signs and Markings](#sec-8E-03) (1)
  - [8E.06 Channelizing Devices Used with Sidewalk and Pathway Traffc Control Devicesi](#sec-8E-06) (1)
- **9B Bicycle Regulatory Signs**
  - [9B.03 Advance Intersection Lane Control Signs (R3-8 Series) for Bicycle Lanes](#sec-9B-03) (1)
  - [9B.04 Bicycle Lane Signs and Plaques (R3-17, R3-5hP, R3-17aP, and R3-17bP)](#sec-9B-04) (4)
  - [9B.05 BEGIN RIGHT TURN LANE YIELD TO BIKES Sign (R4-4)](#sec-9B-05) (1)
  - [9B.06 Bicycle Wrong Way Sign and RIDE WITH TRAFFIC Plaque (R5-1b and R9-3cP)](#sec-9B-06) (2)
  - [9B.09 No Parking Bike Lane Signs (R7-9 and R7-9a)](#sec-9B-09) (2)
  - [9B.11 Bicycles Use Ped Signal Sign (R9-5)](#sec-9B-11) (1)
  - [9B.12 Bicycles Yield to Peds Sign (R9-6)](#sec-9B-12) (1)
  - [9B.13 Shared-Use Path Restriction Sign (R9-7)](#sec-9B-13) (1)
  - [9B.14 Bicycles Allowed Use of Full Lane Sign (R9-20)](#sec-9B-14) (1)
  - [9B.15 Bicycle Passing Clearance Sign (R4-19)](#sec-9B-15) (1)
  - [9B.16 Bicycles Use Shoulder Only Sign (R9-21)](#sec-9B-16) (1)
  - [9B.17 Signing for Bicycles on Freeways and Expressways](#sec-9B-17) (2)
  - [9B.18 Two-Stage Bicycle Turn Box Regulatory Signing (R9-23 Series)](#sec-9B-18) (4)
  - [9B.19 Bicycle Jughandle Signs (R9-24, R9-25, R9-26, and R9-27 Series)](#sec-9B-19) (11)
  - [9B.20 Bicycle Actuation Signs (R10-4, R10-22, R10-24, R10-25, and R10-26)](#sec-9B-20) (3)
  - [9B.22 Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c)](#sec-9B-22) (6)
- **9C Bicycle Warning Signs**
  - [9C.03 Bicycle Surface Condition Warning Sign (W8-10)](#sec-9C-03) (2)
  - [9C.06 Two-Way Bicycle Cross Traffc Warning Plaque (W16i -21P)](#sec-9C-06) (1)
  - [9C.07 Bicycle Lane Ends Warning Sign (W9-5) and Bicycles Merging Sign (W9-5a)](#sec-9C-07) (2)
  - [9C.08 Other Bicycle Warning Signs](#sec-9C-08) (2)
  - [9C.09 Object Markers](#sec-9C-09) (3)
- **9D Bicycle Guide Signs**
  - [9D.01 Bicycle Destination Signs (D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, D1-3c, D2-1a, D2-2a, and D2-3a)](#sec-9D-01) (9)
  - [9D.02 Bike Route Guide Signs (D11-1 and D11-1c)](#sec-9D-02) (2)
  - [9D.03 BIKE ROUTE Plaque (D11-1bP)](#sec-9D-03) (1)
  - [9D.05 Numbered Bicycle Route Signs (M1-8 and M1-8a)](#sec-9D-05) (2)
  - [9D.06 Non-Numbered Bicycle Route Signs (M1-8b and M1-8c)](#sec-9D-06) (2)
  - [9D.07 U.S. Bicycle Route Sign (M1-9)](#sec-9D-07) (1)
  - [9D.08 Bicycle Route Sign and Auxiliary Plaques](#sec-9D-08) (1)
  - [9D.09 Bicycle Parking Area, Sharing Station, and Lockers Guide Signs (D4-3, D4-4, and D4-4a)](#sec-9D-09) (3)
  - [9D.11 Mode-Specifc Directional Guide Signs for Sharedi -Use Paths (D11-11, D11-12, D11-13, and D11-14)](#sec-9D-11) (4)
  - [9D.12 Destination Guide Signs for Shared-Use Paths (D11-10a, D11-10b, D11-10c, D11-10d,](#sec-9D-12) (6)
  - [9D.13 Two-Stage Bicycle Turn Box Guide Signs (D11-20 Series)](#sec-9D-13) (2)

## Part 2 Signs

### Chapter 2A General

<a id="sec-2A-11"></a>
#### Section 2A.11 Enhanced Conspicuity for Standard Signs

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-18P](symbols/W16-18P.png) | **W16-18P** | Notice (plaque) | Optional (2A.11-01) | 24 x 12 | 24 x 12 | — | — | — | — | 2C-1 p.151 | — |

- [O] 2A.11-01 (p.47): Based upon engineering judgment, where the improvement of the conspicuity of a standard regulatory, warning, or guide sign is desired, any of the following methods may be used, as appropriate, to enhance the sign’s conspicuity (see Figure 2A-1): A. Increasing the size of a standard regulatory, warning, or guide sign. B. Dual signing of a standard regulatory, warning, or guide sign by adding a second identical sign on the left-hand side of the roadway at the same location. left-hand side of the roadway at the same location. C. Adding a solid yellow or fluorescent yellow rectangular header panel above a standard regulatory sign, with the width of the panel corresponding to the width of the standard regulatory sign. A legend of “NOTICE,” “STATE LAW,” or other appropriate text may be added in black letters within the header panel for a period of time determined by engineering judgment. D. Adding a NEW plaque (see Section 2C.60) above a new standard regulatory or warning sign, for a period of time in accordance with Paragraph 3 of this Section, to call attention to the new sign.
- **[R]** 2A.11-03 (p.49): If a NEW plaque is used, it should remain in place for a period of time determined by engineering judgment, but not more than 12 months.
- **[M]** 2A.11-04 (p.49): Strobe lights shall not be used to enhance the conspicuity of highway signs.
- **[M]** 2A.11-05 (p.49): If a strip of retroreflective material is used on the sign support, it shall be at least 2 inches in width, it shall be placed for the full length of the support from the sign to within 2 feet above the near edge of the roadway, and its color shall match the background color of the sign, except that the color of the strip for the YIELD and DO NOT ENTER signs shall be red. The retroreflective strip shall not display any legend or other information.
- **[M]** 2A.11-06 (p.49): For a post-mounted sign installation, placing a duplicate sign in the same assembly facing the same direction of traffic shall not be permitted as a method of enhancing conspicuity.

<a id="sec-2A-22"></a>
#### Section 2A.22 Maintaining Minimum Retrorefectivityl

| Sign | Code | Name | Default class | Size table | Also sized in |
|---|---|---|---|---|---|
|  | **R10-4b** | Maintaining Minimum Retrorefectivityl | Optional | text | — |

- [O] 2A.22-05 (p.62): Highway agencies may exclude the following signs from the retroreflectivity maintenance guidelines described in this Section: A. Parking, Standing, and Stopping (R7 and R8 series) signs; B. Walking/Hitchhiking/Crossing (R9 series, R10-1 through R10-4b) signs; C. Acknowledgment signs; and D. Bikeway signs that are intended for exclusive use by bicyclists or pedestrians.

*Also governed by Section 2B.58:*

- [S] 2B.58-02 (p.128): Traffic signal signs applicable to pedestrians include: A. CROSS ONLY ON GREEN (symbolic circular green) (R10-1), B. CROSS ONLY ON (symbolic walk indication) SIGNAL (R10-2), C. Push Button for Walk Signal (R10-3 series), and D. Push Button for Green Signal (R10-4 series).

### Chapter 2B Regulatory Signs

<a id="sec-2B-04"></a>
#### Section 2B.04 STOP Sign (R1-1) and ALL-WAY Plaque (R1-3P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R1-1](symbols/R1-1.png) | **R1-1** | Stop | Mandatory (2B.04-01) · *Auto* | 30 x 30 | 36 x 36 | 36 x 36 | — | 30 x 30* | 48 x 48 | 2B-1 p.68 | 8B-1, 9A-1, 6G-1 |
| ![R1-3P](symbols/R1-3P.png) | **R1-3P** | All Way (plaque) | Mandatory (2B.04-01) · *Auto* | 18 x 6 | 18 x 6 | — | — | — | 30 x 12 | 2B-1 p.68 | — |
| ![R1-10P](symbols/R1-10P.png) | **R1-10P** | Except Right Turn (plaque) | Optional | 24 x 18 | 24 x 18 | — | — | — | — | 2B-1 p.68 | — |

- **[M]** 2B.04-01 (p.74) ◆ R1-1: When it is determined that a full stop is always required on an approach to an intersection, a STOP (R1-1) sign (see Figure 2B-1) shall be used.
- **[M]** 2B.04-02 (p.74): Secondary legends shall not be used on STOP sign faces.
- **[M]** 2B.04-03 (p.74): The STOP sign shall not be displayed using a changeable message sign.
- **[M]** 2B.04-04 (p.74) ◆ R1-3P: At intersections where all approaches are controlled by STOP signs (see Section 2B.12), an ALL-WAY (R1-3P) supplemental plaque (see Figure 2B-1) shall be mounted below each STOP sign. The ALL-WAY plaque shall have a white legend and border on a red background.
- **[M]** 2B.04-05 (p.74): Supplemental plaques with legends such as 2-WAY, 3-WAY, 4-WAY, or other numbers of ways shall not be used with STOP signs.
- **[R]** 2B.04-07 (p.74): The TRAFFIC FROM LEFT (RIGHT) DOES NOT STOP (W4-4aP) plaque or ONCOMING TRAFFIC DOES NOT STOP (W4-4bP) plaque should be used at intersections where STOP signs control all but one approach to the intersection, unless the only non-stopped approach is from a one-way street.
- [O] 2B.04-08 (p.74) ◆ R1-10P: The EXCEPT RIGHT TURN (R1-10P) plaque (see Figure 2B-1) may be mounted below the STOP sign if an engineering study determines that a special combination of geometry and traffic volumes is present that makes it possible for right-turning traffic on the approach to be allowed to enter the intersection without stopping.

*Also governed by Section 6D.02:*

- **[R]** 6D.02-01 (p.783): The STOP/SLOW paddle (see Figure 6D-1 and Table 6G-1) should be the primary and preferred handsignaling device because the STOP/SLOW paddle gives road users more positive guidance than red flags.
- **[M]** 6D.02-03 (p.783): A STOP/STOP or a SLOW/SLOW paddle may be used in certain situations (see Section 6D.05), provided the device meets the size and shape requirements for the STOP/SLOW paddle.
- **[R]** 6D.02-04 (p.783): The STOP/SLOW paddle should be fabricated from light semi-rigid material.
- [O] 6D.02-06 (p.783): The STOP/SLOW paddle may be modified to improve conspicuity by incorporating either white or red flashing lights on the STOP face, and either white or yellow flashing lights on the SLOW face. The flashing lights may be arranged in any of the following patterns: A. Two white or red lights, one centered vertically above and one centered vertically below the STOP legend; and/or two white or yellow lights, one centered vertically above and one centered vertically below the SLOW legend; B. Two white or red lights, one centered horizontally on each side of the STOP legend; and/or two white or yellow lights, one centered horizontally on each side of the SLOW legend; C. One white or red light centered below the STOP legend; and/or one white or yellow light centered below the SLOW legend; D. A series of eight or more small white or red lights no larger than ¼ inch in diameter along the outer edge of the paddle, arranged in an octagonal pattern at the eight corners of the border of the STOP face; and/ or a series of eight or more small white or yellow lights no larger than ¼ inch in diameter along the outer edge of the paddle, arranged in a diamond pattern along the border of the SLOW face; or E. A series of white lights forming the shapes of the letters in the legend.
- **[M]** 6D.02-07 (p.783): If flashing lights are used on the STOP face of the paddle, their colors shall be all white or all red. If flashing lights are used on the SLOW face of the paddle, their colors shall be all white or all yellow.
- **[M]** 6D.02-08 (p.783): If more than eight flashing lights are used, the lights shall be arranged such that they clearly convey the octagonal shape of the STOP face of the paddle and/or the diamond shape of the SLOW face of the paddle.
- **[M]** 6D.02-09 (p.783): If flashing lights are used on the STOP/SLOW paddle, the flash rate shall be at least 50, but not more than 60, flashes per minute.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 8B.04:*

- **[M]** 8B.04-01 (p.995) ◆ R1-1: A Crossbuck Assembly shall consist of a Crossbuck (R15-1) sign, and a Number of Tracks (R15-2P) plaque if two or more tracks are present, that complies with the provisions of Section 8B.03, and either a YIELD (R1-2) or STOP (R1-1) sign installed on the same support, except as provided in Paragraph 10 of this Section. YIELD or STOP signs used at passive grade crossings shall be installed in compliance with the provisions of Section 2B.18, and Figures 8B-2 and 8B-3.

*Also governed by Section 8B.05:*

- **[R]** 8B.05-01 (p.1001): The use of only STOP or YIELD signs for road users at highway-LRT grade crossings should be limited to those crossings where the need and feasibility is determined by the Diagnostic Team. Such crossings should have all of the following characteristics: A. The crossing roadways are secondary in character (such as a minor street with one lane in each direction, an alley, or a driveway) with low traffic volumes and low speed limits. The specific thresholds of traffic volumes and speed limits should be determined by the local agencies. B. The line of sight for an approaching LRT operator is adequate from a sufficient distance such that the operator can sound an audible signal and bring the LRT equipment to a stop before arriving at the crossing. C. The road user has sufficient sight distance at the stop line to permit the vehicle to cross the tracks before the arrival of the LRT equipment. D. If at an intersection of two roadways, the intersection does not meet the warrants for a traffic control signal as provided in Chapter 4C. E. The LRT tracks are located such that motor vehicles are not likely to stop on the tracks while waiting to enter a crossroad or highway.
- **[M]** 8B.05-02 (p.1001) ◆ R1-1: For all highway-LRT grade crossings where only STOP (R1-1) or YIELD (R1-2) signs are installed, the placement shall comply with the requirements of Section 2B.18. Stop Ahead (W3-1) or Yield Ahead (W3-2) Advance Warning signs shall also be installed if the criteria for their installation given in Section 2C.35 is met.

*Also governed by Section 9B.01:*

- **[M]** 9B.01-01 (p.1052) ◆ R1-1: STOP (R1-1) signs (see Figure 9B-1) shall be installed on bicycle facilities at points where bicyclists are required to stop.
- **[M]** 9B.01-02 (p.1052): YIELD (R1-2) signs (see Figure 9B-1) shall be installed on bicycle facilities at points where bicyclists have an adequate view of conflicting traffic as they approach the sign, and where bicyclists are required to yield the right-of-way to that conflicting traffic.
- **[M]** 9B.01-03 (p.1052): A STOP sign or a YIELD sign shall not be installed in conjunction with a bicycle signal face (see Chapter 4H).
- [O] 9B.01-04 (p.1053): Larger signs may be used on shared-use paths and separated bikeways for added emphasis.
- **[R]** 9B.01-05 (p.1053): Where conditions require shared-use path users or bicyclists on separated bikeways, but not roadway users, to stop or yield, the STOP or YIELD sign should be placed or shielded so that it is not readily visible to roadway users.
- **[R]** 9B.01-06 (p.1054): When the placement of STOP or YIELD signs is being considered, the priority at a shared-use path/roadway intersection should be assigned with consideration of the following: A. Relative speeds of shared-use path and roadway users, B. Relative volumes of shared-use path and roadway traffic, and C. Relative importance of shared-use path and roadway.
- **[R]** 9B.01-07 (p.1054): Speed should not be the sole factor used to determine priority, as it is sometimes appropriate to give priority to a high-volume shared-use path that crosses a low-volume street, or to a regional shared-use path that crosses a minor collector street.
- **[R]** 9B.01-08 (p.1054): When priority is assigned (see Sections 2B.06 and 2B.08), the least-restrictive control that is appropriate should be placed on the lower-priority approaches. STOP signs should not be used where YIELD signs would provide adequate control.

<a id="sec-2B-05"></a>
#### Section 2B.05 YIELD Sign (R1-2)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R1-2](symbols/R1-2.png) | **R1-2** | Yield | Mandatory (8B.04-01) · *Auto* | 36 x 36 x 36 | 48 x 48 x 48 | 48 x 48 x 48 | 60 x 60 x 60 | 30 x 30 x 30* | — | 2B-1 p.68 | 8B-1, 9A-1, 6G-1 |

- **[M]** 2B.05-02 (p.74): The YIELD (R1-2) sign (see Figure 2B-1) shall not be displayed using a changeable message sign.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 8B.04:*

- **[M]** 8B.04-01 (p.995): A Crossbuck Assembly shall consist of a Crossbuck (R15-1) sign, and a Number of Tracks (R15-2P) plaque if two or more tracks are present, that complies with the provisions of Section 8B.03, and either a YIELD (R1-2) or STOP (R1-1) sign installed on the same support, except as provided in Paragraph 10 of this Section. YIELD or STOP signs used at passive grade crossings shall be installed in compliance with the provisions of Section 2B.18, and Figures 8B-2 and 8B-3.

*Also governed by Section 8B.05:*

- **[R]** 8B.05-01 (p.1001): The use of only STOP or YIELD signs for road users at highway-LRT grade crossings should be limited to those crossings where the need and feasibility is determined by the Diagnostic Team. Such crossings should have all of the following characteristics: A. The crossing roadways are secondary in character (such as a minor street with one lane in each direction, an alley, or a driveway) with low traffic volumes and low speed limits. The specific thresholds of traffic volumes and speed limits should be determined by the local agencies. B. The line of sight for an approaching LRT operator is adequate from a sufficient distance such that the operator can sound an audible signal and bring the LRT equipment to a stop before arriving at the crossing. C. The road user has sufficient sight distance at the stop line to permit the vehicle to cross the tracks before the arrival of the LRT equipment. D. If at an intersection of two roadways, the intersection does not meet the warrants for a traffic control signal as provided in Chapter 4C. E. The LRT tracks are located such that motor vehicles are not likely to stop on the tracks while waiting to enter a crossroad or highway.
- **[M]** 8B.05-02 (p.1001): For all highway-LRT grade crossings where only STOP (R1-1) or YIELD (R1-2) signs are installed, the placement shall comply with the requirements of Section 2B.18. Stop Ahead (W3-1) or Yield Ahead (W3-2) Advance Warning signs shall also be installed if the criteria for their installation given in Section 2C.35 is met.

*Also governed by Section 9B.01:*

- **[M]** 9B.01-01 (p.1052): STOP (R1-1) signs (see Figure 9B-1) shall be installed on bicycle facilities at points where bicyclists are required to stop.
- **[M]** 9B.01-02 (p.1052): YIELD (R1-2) signs (see Figure 9B-1) shall be installed on bicycle facilities at points where bicyclists have an adequate view of conflicting traffic as they approach the sign, and where bicyclists are required to yield the right-of-way to that conflicting traffic.
- **[M]** 9B.01-03 (p.1052): A STOP sign or a YIELD sign shall not be installed in conjunction with a bicycle signal face (see Chapter 4H).
- [O] 9B.01-04 (p.1053): Larger signs may be used on shared-use paths and separated bikeways for added emphasis.
- **[R]** 9B.01-05 (p.1053): Where conditions require shared-use path users or bicyclists on separated bikeways, but not roadway users, to stop or yield, the STOP or YIELD sign should be placed or shielded so that it is not readily visible to roadway users.
- **[R]** 9B.01-06 (p.1054): When the placement of STOP or YIELD signs is being considered, the priority at a shared-use path/roadway intersection should be assigned with consideration of the following: A. Relative speeds of shared-use path and roadway users, B. Relative volumes of shared-use path and roadway traffic, and C. Relative importance of shared-use path and roadway.
- **[R]** 9B.01-07 (p.1054): Speed should not be the sole factor used to determine priority, as it is sometimes appropriate to give priority to a high-volume shared-use path that crosses a low-volume street, or to a regional shared-use path that crosses a minor collector street.
- **[R]** 9B.01-08 (p.1054): When priority is assigned (see Sections 2B.06 and 2B.08), the least-restrictive control that is appropriate should be placed on the lower-priority approaches. STOP signs should not be used where YIELD signs would provide adequate control.

<a id="sec-2B-18"></a>
#### Section 2B.18 STOP Sign or YIELD Sign Placement

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R1-2aP](symbols/R1-2aP.png) | **R1-2aP** | To Oncoming Traffic (plaque) | Optional | 24 x 18 | 24 x 18 | 36 x 30 | 48 x 36 | 24 x 18 | — | 2B-1 p.68 | 6G-1 |
| ![R1-2bP](symbols/R1-2bP.png) | **R1-2bP** | To Traffic in Circle (plaque) | Optional | 24 x 15 | 24 x 15 | — | — | 24 x 15 | 36 x 24 | 2B-1 p.68 | — |
| ![R1-2cP](symbols/R1-2cP.png) | **R1-2cP** | To All Lanes (plaque) | Optional | 24 x 15 | 24 x 15 | — | — | 24 x 15 | 36 x 24 | 2B-1 p.68 | — |

- [O] 2B.18-07 (p.80) ◆ R1-2aP: Where drivers proceeding straight ahead must yield to traffic approaching from the opposite direction, such as at a one-lane bridge, a TO ONCOMING TRAFFIC (R1-2aP) plaque (see Figure 2B-1) may be mounted below the YIELD sign.
- [O] 2B.18-08 (p.80) ◆ R1-2bP, R1-2cP: Where drivers must yield to traffic in a multi-lane roundabout, a TO TRAFFIC IN CIRCLE (R1-2bP) or TO ALL LANES (R1-2cP) plaque (see Figure 2B-1) may be mounted below the YIELD sign.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

<a id="sec-2B-19"></a>
#### Section 2B.19 Yield Here To Pedestrians Signs and Stop Here For Pedestrians Signs (R1-5 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R1-5](symbols/R1-5.png) | **R1-5** | Yield Here to Pedestrians | Mandatory (2B.19-02) | — | 36 x 36 | — | — | — | 36 x 36 | 2B-1 p.68 | — |
| ![R1-5b](symbols/R1-5b.png) | **R1-5b** | Stop Here for Pedestrians | Mandatory (2B.19-02) | — | 36 x 36 | — | — | — | 36 x 36 | 2B-1 p.68 | — |
| ![R1-5d](symbols/R1-5d.png) | **R1-5d** | Yield Here to Trail Crossings | Mandatory (2B.19-02) | — | 36 x 42 | — | — | — | — | 2B-1 p.68 | — |
| ![R1-5e](symbols/R1-5e.png) | **R1-5e** | Stop
Here for Trail Crossing | Mandatory (2B.19-02) | — | 36 x 42 | — | — | — | — | 2B-1 p.68 | — |

- [S] 2B.19-01 (p.81): The R1-5 series signs are intended to mitigate the scenario that can place pedestrians at risk by blocking other drivers’ view of pedestrians and by blocking the pedestrians’ view of the vehicles approaching in the adjacent lanes.
- **[M]** 2B.19-02 (p.81): Yield Here to (Stop Here for) Pedestrians (R1-5, R1-5a, R1-5b, R1-5c, R1-5d, and R1-5e) signs (see Figure 2B-2) shall be used if yield (stop) lines are used in advance of a marked crosswalk only where it crosses an uncontrolled multi-lane approach. The Stop Here for Pedestrians signs shall only be used where the law specifically requires that a driver must stop for a pedestrian in a crosswalk. The legend STATE LAW shall not be displayed on the R1-5 series signs.
- **[R]** 2B.19-03 (p.81): If yield (stop) lines and Yield Here to (Stop Here for) Pedestrians signs are used in advance of a crosswalk that crosses an uncontrolled multi-lane approach, the signs should be placed 20 to 50 feet in advance of the nearest edge of the crosswalk (see Section 3B.19 and Figure 3B-16).
- **[M]** 2B.19-04 (p.81) ◆ R1-5, R1-5b: When used with a School Crossing assembly within school zones (see Part 7), the R1-5a and R1-5c signs shall be used in place of the R1-5 and R1-5b signs in accordance with Paragraph 2 of this Section.
- **[M]** 2B.19-05 (p.81): When used with a Trail Crossing assembly (see Section 2C.54), the R1-5d and R1-5e signs shall be used in place of the R1-5 and R1-5b signs in accordance with Paragraph 2 of this Section.
- **[R]** 2B.19-06 (p.81): When Yield Here to (Stop Here for) Pedestrians signs are provided in advance of a crosswalk across an multi-lane approach, parking should be prohibited in the area between the yield (stop) line and the crosswalk.
- **[R]** 2B.19-07 (p.81): Yield (stop) lines and Yield Here to (Stop Here for) Pedestrians signs should not be used in advance of crosswalks that cross an approach to or departure from a roundabout.
- [O] 2B.19-08 (p.81): Yield Here to (Stop Here for) Pedestrians signs may be used in accordance with Paragraphs 2 through 4 of this Section even if yield (stop) lines are not used.
- [O] 2B.19-09 (p.81): A Pedestrian Crossing (W11-2) warning sign may be placed overhead or may be post-mounted with a diagonal downward-pointing arrow (W16-7P) plaque at the crosswalk location where Yield Here to (Stop Here for) Pedestrians signs have been installed in advance of the crosswalk.
- **[M]** 2B.19-10 (p.81): If a W11-2 sign is post-mounted at the crosswalk location where a Yield Here to (Stop Here for) Pedestrians sign is used on the approach, the Yield Here to (Stop Here for) Pedestrians sign shall not be placed on the same post as the W11-2 sign.
- [O] 2B.19-11 (p.81): An advance Pedestrian Crossing (W11-2) warning sign with an AHEAD or a distance supplemental plaque may be used in conjunction with a Yield Here to (Stop Here for) Pedestrians sign on the approach to the same crosswalk.
- [O] 2B.19-12 (p.81): In-Street Pedestrian Crossing signs and Yield Here to (Stop Here for) Pedestrians signs may be used together at the same crosswalk.

<a id="sec-2B-20"></a>
#### Section 2B.20 In-Street and Overhead Pedestrian and Trail Crossing Signs (R1-6 and R1-9 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R1-6](symbols/R1-6.png) | **R1-6** | In-Street Pedestrian Crossing - | Optional (2B.20-01) | 12 x 36 | 12 x 36 | — | — | — | — | 2B-1 p.68 | 7B-1 |
| ![R1-6a](symbols/R1-6a.png) | **R1-6a** | In-Street Pedestrian Crossing - | Optional (2B.20-01) | 12 x 36 | 12 x 36 | — | — | — | — | 2B-1 p.68 | 7B-1 |
| ![R1-6b](symbols/R1-6b.png) | **R1-6b** | School Crossing | Optional (2B.20-01) | — | — | — | — | — | — | text | — |
| ![R1-6c](symbols/R1-6c.png) | **R1-6c** | In-Street and Overhead Pedestrian and Trail Crossing Signs (R1-6 and R1-9 Series) | Optional (2B.20-01) | — | — | — | — | — | — | text | — |
| ![R1-6d](symbols/R1-6d.png) | **R1-6d** | In-Street Trail Crossing - | Optional (2B.20-01) | 12 x 36 | 12 x 36 | — | — | — | — | 2B-1 p.68 | — |
| ![R1-6e](symbols/R1-6e.png) | **R1-6e** | In-Street Trail Crossing - | Optional (2B.20-01) | 12 x 36 | 12 x 36 | — | — | — | — | 2B-1 p.68 | — |
| ![R1-9](symbols/R1-9.png) | **R1-9** | Overhead Pedestrian Crossing - | Optional (2B.20-01) | 90 x 24 | 90 x 24 | — | — | — | — | 2B-1 p.68 | — |
| ![R1-9a](symbols/R1-9a.png) | **R1-9a** | Overhead Pedestrian Crossing - | Optional (2B.20-01) | 90 x 24 | 90 x 24 | — | — | — | — | 2B-1 p.68 | — |
| ![R1-9d](symbols/R1-9d.png) | **R1-9d** | Overhead Trail Crossing | Optional (2B.20-01) | 72 x 24 | 72 x 24 | — | — | — | — | 2B-1 p.68 | — |
| ![R1-9e](symbols/R1-9e.png) | **R1-9e** | Overhead Trail Crossing | Optional (2B.20-01) | 72 x 24 | 72 x 24 | — | — | — | — | 2B-1 p.68 | — |

- [O] 2B.20-01 (p.81): The In-Street Pedestrian Crossing (R1-6 or R1-6a) sign (see Figure 2B-2), In-Street Trail Crossing (R1-6d or R1-6e) sign (see Figure 2B-2), the Overhead Pedestrian Crossing (R1-9 or R1-9a) sign (see Figure 2B-2), or the Overhead Trail Crossing (R1-9d or R1-9e) sign (see Figure 2B-2) may be used to remind road users of laws regarding right-of-way at an unsignalized crosswalk. The legend STATE LAW may be displayed at the top of the R1-6 series and R1-9 series signs if applicable. On the R1-6 series signs, the legends STOP or YIELD may be used instead of the appropriate STOP sign or YIELD sign symbol.
- [O] 2B.20-02 (p.81): Highway agencies may develop and apply criteria for determining the applicability of In-Street Pedestrian Crossing signs.
- **[M]** 2B.20-03 (p.83): The STOP FOR legend shall only be used in States where the State law specifically requires that a driver must stop for a pedestrian or a bicyclist in a crosswalk.
- **[M]** 2B.20-04 (p.83): If used, In-Street Pedestrian or Trail Crossing signs shall only be placed in the roadway at the crosswalk location on the center line, on a median island, on a lane line, or on an edge line.
- **[M]** 2B.20-05 (p.83): The In-Street Pedestrian or Trail Crossing sign shall not be post-mounted on the left-hand or righthand side of the roadway.
- **[M]** 2B.20-07 (p.83): If used, the Overhead Pedestrian or Trail Crossing sign shall be placed over the roadway at the crosswalk location.
- **[M]** 2B.20-08 (p.83): When used at an uncontrolled crossing, the In-Street or Overhead Pedestrian Crossing sign shall be used only as a supplement to a Pedestrian Crossing (W11-2) warning sign with a diagonal downwardpointing arrow (W16-7P) plaque at the crosswalk location.
- **[M]** 2B.20-09 (p.83): When used at an uncontrolled crossing, the In-Street or Overhead Trail Crossing sign shall be used only as a supplement to a Trail Crossing (W11-15) warning sign with a diagonal downward-pointing arrow (W16-7P) plaque at the crosswalk location.
- **[M]** 2B.20-10 (p.83): An In-Street or Overhead Pedestrian or Trail Crossing sign shall not be placed in advance of the crosswalk to educate road users about the State law prior to reaching the crosswalk, nor shall it be installed as an educational display that is not near any crosswalk.
- **[R]** 2B.20-11 (p.83): If an island (see Chapter 3J) is available, the In-Street Pedestrian or Trail Crossing sign, if used, should be placed on the island.
- [O] 2B.20-12 (p.83): In-Street Pedestrian or Trail Crossing signs may be mounted back-to-back in the median or on the center line of an undivided roadway.
- **[M]** 2B.20-13 (p.83): The In-Street Pedestrian or Trail Crossing sign and the Overhead Pedestrian Crossing or Trail sign shall not be used at crosswalks on approaches controlled by a traffic control signal, pedestrian hybrid beacon, or an emergency-vehicle hybrid beacon.
- **[M]** 2B.20-14 (p.83): Except where the In-Street Crossing sign is placed on a physical island, the sign support shall be designed to bend over and then bounce back to its normal vertical position when struck by a vehicle.
- [O] 2B.20-15 (p.83): The In-Street and Overhead Pedestrian and Trail Crossing sign may be used at intersections or midblock pedestrian crossings with flashing beacons.
- **[M]** 2B.20-17 (p.83): The top of an In-Street Pedestrian or Trail Crossing sign shall be a maximum of 4 feet above the pavement surface. The top of an In-Street Pedestrian or Trail Crossing sign placed in an island shall be a maximum of 4 feet above the island surface.
- [O] 2B.20-18 (p.83): The In-Street Pedestrian Crossing or Trail Crossing signs may be used seasonally to prevent damage in winter because of plowing operations, and may be removed at night if the pedestrian activity at night is minimal.
- [O] 2B.20-19 (p.83): Both sign mounting types, In-Street Crossing (R1-6 series) signs and Overhead Crossing (R1-9 series) signs, may be used together at the same crosswalk.

*Also governed by Section 3I.02:*

- **[R]** 3I.02-05 (p.632) ◆ R1-6b, R1-6c: When tubular markers are used to supplement a R1-6 series sign (see Section 2B.20) that is either on the center line, lane line, or median island, they should not be used on the same pavement marking line where the R1-6 series sign is installed.

*Also governed by Section 7B.03:*

- [O] 7B.03-05 (p.976) ◆ R1-6, R1-6a: A 12‑inch reduced size in‑street School (S1‑1) sign (see Figure 7B‑1), installed in compliance with the mounting height and special mounting support requirements for an In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) sign (see Section 2B.20), may be used in advance of a school crossing to supplement the post‑mounted school warning signs. A 12 x 6‑inch reduced size AHEAD (W16‑9P) plaque (see Figure 7B‑1) may be mounted below the reduced size in‑street School (S1‑1) sign.
- [O] 7B.03-12 (p.976) ◆ R1-6, R1-6a: The In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) sign (see Section 2B.20 and Figure 7B‑1) or the In‑Street School Crossing (R1‑6b or R1‑6c) sign (see Figure 7B‑1) may be used at school crossings on approaches that are not controlled by a traffic control signal, a pedestrian hybrid beacon, or emergency‑vehicle hybrid beacon. If used at a school crossing, a 12 x 4‑inch SCHOOL (S4‑3P) plaque (see Figure 7B‑1) may be mounted above the sign. The STATE LAW legend on the R1‑6 series signs may be omitted.
- [O] 7B.03-13 (p.976) ◆ R1-6, R1-6a: The In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) sign or In‑Street School Crossing (R1‑6b or R1‑6c) sign may be used at intersections or midblock crossings with flashing beacons.
- [O] 7B.03-16 (p.978) ◆ R1-6, R1-6a: A 12‑inch reduced size in‑street School (S1‑1) sign (see Figure 7B‑1) may be used instead of the In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) or the In‑Street School Crossing (R1‑6b or R1‑6c) sign at a school crossing on approaches that are not controlled by a traffic control signal, pedestrian hybrid beacon, or an emergency‑vehicle hybrid beacon. A 12 x 6‑inch reduced size diagonal downward‑pointing arrow (W16‑7P) plaque (see Figure 7B‑1) may be mounted below the reduced size in‑street School (S1‑1) sign.
- **[M]** 7B.03-17 (p.978) ◆ R1-6, R1-6a: If an In‑Street Pedestrian Crossing sign, an In‑Street School Crossing sign, or a reduced size in‑street School (S1‑1) sign is placed in the roadway, the sign support shall comply with the mounting height and special mounting support requirements for an In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) sign (see Section 2B.20).

<a id="sec-2B-21"></a>
#### Section 2B.21 Speed Limit Sign (R2-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R2-1](symbols/R2-1.png) | **R2-1** | Speed Limit | Recommended (2B.21-08) · *Auto* | 24 x 30 | 30 x 36 | 36 x 48 | 48 x 60 | 18 x 24 | 30 x 36 | 2B-1 p.68 | 7B-1, 6G-1 |
| ![R2-5P](symbols/R2-5P.png) | **R2-5P** | Unless Otherwise Posted (plaque) | Optional | 24 x 18 | 24 x 18 | 36 x 24 | 36 x 24 | — | 36 x 24 | 2B-1 p.68 | — |
| ![R2-5aP](symbols/R2-5aP.png) | **R2-5aP** | Citywide (plaque) | Optional | 24 x 6 | 24 x 6 | — | — | — | 30 x 9 | 2B-1 p.68 | — |
| ![R2-5bP](symbols/R2-5bP.png) | **R2-5bP** | Neighborhood (plaque) | Optional | 24 x 6 | 24 x 6 | — | — | — | 30 x 9 | 2B-1 p.68 | — |
| ![R2-5cP](symbols/R2-5cP.png) | **R2-5cP** | Residential (plaque) | Optional | 24 x 6 | 24 x 6 | — | — | — | 30 x 9 | 2B-1 p.68 | — |
| ![R2-13](symbols/R2-13.png) | **R2-13** | End Variable Speed Limit | Optional (2B.21-21) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.68 | — |
| ![R2-14](symbols/R2-14.png) | **R2-14** | End Truck Speed Limit | Mandatory (2B.21-22) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.68 | — |

- **[M]** 2B.21-06 (p.84): Speed zones (other than statutory speed limits) shall only be established on the basis of an engineering study that has been performed in accordance with traffic engineering practices. The engineering study shall consider the roadway context.
- **[R]** 2B.21-07 (p.84): Among the factors that should be considered when conducting an engineering study for establishing or reevaluating speed limits within speed zones are the following: A. Roadway environment (such as roadside development, number and frequency of driveways and access points, and land use), functional classification, public transit volume and location or frequency of stops, parking practices, and pedestrian and bicycle facilities and activity; B. Roadway characteristics (such as lane widths, shoulder condition, grade, alignment, median type, and sight distance); C. Geographic context (such as an urban district, rural town center, non-urbanized rural area, or suburban area), and multi-modal trip generation; D. Reported crash experience for at least a 12-month period; E. Speed distribution of free-flowing vehicles including the pace, median (50th-percentile), and 85thprecentile speeds; and F. A review of past speed studies to identify any trends in operating speeds.
- **[R]** 2B.21-08 (p.84): When the 85th-percentile speed is appreciably greater than the posted speed limit, and the roadway context does not support setting a higher speed limit, the engineering study should consider whether changes to geometric features, enforcement, and/or other speed-reduction countermeasures might improve compliance with the posted speed limit. A similar approach should be used if the results of past speed studies indicate that the 85th-percentile speed has consistently increased.
- **[R]** 2B.21-09 (p.84): On urban and suburban arterials, and on rural arterials that serve as main streets through developed areas of communities, the 85th-percentile speed should not be used to set speed limits without consideration of all factors described in Paragraph 7 of this Section.
- **[R]** 2B.21-10 (p.85): On a freeway, expressway, or rural highway (outside urbanized locations or conditions), the speed limit that is posted within a speed zone should be within 5 mph of the 85th-percentile speed of free-flowing motor-vehicle traffic under the following conditions: A. All factors described in Paragraph 7 of this Section have been considered and determined to be nonmitigating, and B. The measures described in Paragraph 8 of this Section have been considered to the extent practicable.
- **[R]** 2B.21-11 (p.85): State and local agencies should conduct engineering studies to reevaluate non-statutory speed limits on segments of their roadways that have undergone significant changes since the last review (such as changes to roadway context, the addition or elimination of parking or driveways, changes in the number of travel lanes, changes in the configuration of bicycle lanes, changes to road geometrics, changes in traffic control signal coordination, or significant changes in traffic volumes).
- **[R]** 2B.21-12 (p.85): Speed studies for signalized intersection approaches should be taken outside the influence area of the traffic control signal, which is generally considered to be approximately 1/2 mile, to avoid obtaining skewed results for the speed distribution. If the signal spacing is less than 1 mile, the speed study should be at approximately the middle of the segment.
- **[M]** 2B.21-13 (p.85) ◆ R2-1: The Speed Limit (R2-1) sign (see Figure 2B-3) shall display the limit established by law, ordinance, regulation, or as adopted by the authorized agency based on an engineering study. The speed limits displayed shall be in multiples of 5 mph.
- **[M]** 2B.21-14 (p.85) ◆ R2-1: Speed Limit (R2-1) signs, indicating speed limits for which posting is required by law, shall be located at the points of change from one speed limit to another.
- **[M]** 2B.21-15 (p.85): At the downstream end of the section to which a particular speed limit applies, a Speed Limit sign showing the next speed limit shall be installed.
- **[M]** 2B.21-16 (p.85): Speed Limit signs indicating the statutory speed limits shall be installed at entrances to the State and, where appropriate, at jurisdictional boundaries in urban areas.
- **[R]** 2B.21-17 (p.85): Additional Speed Limit signs should be installed beyond interchanges and major intersections and at other locations where it is necessary to remind road users of the speed limit that is applicable.
- [O] 2B.21-19 (p.85) ◆ R2-5P, R2-5aP, R2-5bP, R2-5cP: If a jurisdiction has a policy of installing Speed Limit signs in accordance with statutory requirements only on the streets that enter a city, neighborhood, or residential area to indicate the speed limit that is applicable to the entire city, neighborhood, or residential area unless otherwise posted, a CITYWIDE (R2-5aP), NEIGHBORHOOD (R2-5bP), or RESIDENTIAL (R2-5cP) plaque may be mounted above the Speed Limit sign and an UNLESS OTHERWISE POSTED (R2-5P) plaque may be mounted below the Speed Limit sign (see Figure 2B-3).
- [O] 2B.21-21 (p.85) ◆ R2-13: If a W3-5b sign is posted to provide notice of a variable speed zone, an END VARIABLE SPEED LIMIT (R2-13) sign (see Figure 2B-3) may be installed at the downstream end of the zone to provide notice to road users of the termination of the speed zone.
- **[M]** 2B.21-22 (p.85) ◆ R2-14: If a W3-5c sign is posted to provide notice of a truck speed zone, an END TRUCK SPEED LIMIT (R2-14) sign (see Figure 2B-3) shall be installed at the downstream end of the zone to provide notice to road users of the termination of the speed zone.
- **[R]** 2B.21-23 (p.85): An advisory speed plaque (see Section 2C.59) mounted below a warning sign should be used to warn road users of an advisory speed for a roadway condition. A Speed Limit sign should not be used for this purpose.
- **[R]** 2B.21-24 (p.85): Advance traffic control warning signs (see Section 2C.35), intersection warning signs (see Section 2C.41), and/or other traffic control devices are appropriate warning prior to a signalized intersection. A Speed Limit sign should not be used for this purpose.
- [O] 2B.21-25 (p.86): Two types of Speed Limit signs may be used: one to designate passenger car speeds, including any nighttime information or maximum or minimum speed limit that might apply; and the other to show any special speed limits for trucks and other vehicles.
- **[R]** 2B.21-26 (p.86): No more than three speed limits should be displayed on any one Speed Limit sign or assembly.
- [O] 2B.21-27 (p.86): A variable speed limit sign that changes the speed limit for traffic and ambient conditions may be installed provided that the appropriate speed limit is displayed at the proper times and locations in accordance with Paragraphs 9 and 10 of this Section.
- **[M]** 2B.21-28 (p.86): The variable speed limit sign legend “SPEED LIMIT” shall be a black legend on a white retroreflective background. The variable speed limit legend shall be displayed in white LEDs on an opaque black background.

*Also governed by Section 6G.08:*

- [O] 6G.08-01 (p.795): A WORK ZONE (G20-5aP) plaque (see Figure 6G-1) may be mounted above a Speed Limit sign to emphasize that a reduced speed limit is in effect within a TTC zone. An END WORK ZONE SPEED LIMIT (R2-12) sign (see Figure 6G-1) may be installed at the downstream end of the reduced speed limit zone.
- **[R]** 6G.08-02 (p.795): A BEGIN HIGHER FINES ZONE (R2-10) sign (see Figure 6G-1) should be installed at or near the beginning of a TTC zone where increased fines are imposed for traffic violations, and an END HIGHER FINES ZONE (R2-11) sign (see Figure 6G-1) should be installed at or near the downstream end of the TTC zone.
- [O] 6G.08-03 (p.797): Alternate legends such as BEGIN (or END) DOUBLE FINES ZONE may also be used for the R2-10 and R2-11 signs.
- [O] 6G.08-04 (p.797): A FINES HIGHER, FINES DOUBLE, or $XX FINE plaque (see Section 2B.25 and Figure 6G-1) may be mounted below the Speed Limit sign if increased fines are imposed for traffic violations within the TTC zone.
- [O] 6G.08-05 (p.797): Individual signs and plaques for work zone speed limits and higher fines may be combined into a single sign or may be displayed as an assembly of signs and plaques.

*Also governed by Section 7B.05:*

- **[M]** 7B.05-07 (p.980) ◆ R2-1: The static School Speed Limit assembly shall consist of a top plaque (S4‑3P) with the legend SCHOOL, a Speed Limit (R2‑1) sign, and a bottom plaque (S4‑1P, S4‑2P, S4‑4P, or S4‑6P) indicating the specific periods of the day and/or days of the week that the special school speed limit is in effect (see Figure 7B‑1).
- **[M]** 7B.05-08 (p.980) ◆ R2-1: When a School Speed Limit When Flashing (S5‑1) sign or a Speed Limit (R2‑1) sign with a supplemental WHEN FLASHING (S4‑4P) plaque is used, a Speed Limit Sign Beacon (see Section 4S.04) shall be used to identify the periods that the school speed limit is in effect.

<a id="sec-2B-22"></a>
#### Section 2B.22 Vehicle Speed Limit Plaques (R2-2P Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R2-2P](symbols/R2-2P.png) | **R2-2P** | Truck Speed Limit (plaque) | Optional | 24 x 24 | 24 x 24 | 36 x 36 | 48 x 48 | — | 36 x 36 | 2B-1 p.68 | — |
| ![R2-2aP](symbols/R2-2aP.png) | **R2-2aP** | Bus Speed Limit (plaque) | Optional | 24 x 24 | 24 x 24 | 36 x 36 | 48 x 48 | — | 36 x 36 | 2B-1 p.68 | — |
| ![R2-2bP](symbols/R2-2bP.png) | **R2-2bP** | Truck-Bus Speed Limit (plaque) | Optional | 24 x 30 | 24 x 30 | 36 x 42 | 48 x 54 | — | 36 x 42 | 2B-1 p.68 | — |
| ![R2-2cP](symbols/R2-2cP.png) | **R2-2cP** | Vehicles Over X Tons Speed | Optional | 24 x 30 | 24 x 30 | 36 x 42 | 48 x 54 | — | 36 x 42 | 2B-1 p.68 | — |

- **[M]** 2B.22-01 (p.87): Where a special speed limit applies to certain classes of vehicles, the Truck Speed Limit (R2-2P) plaque, Bus Speed Limit (R2-2aP) plaque, Truck-Bus Speed Limit (R2-2bP) plaque, or Vehicles over X Tons Speed Limit (R2-2cP) plaque (see Figure 2B-3) shall be displayed below the Speed Limit (R2-1) sign, except as provided in Paragraph 2 of this Section.
- [O] 2B.22-02 (p.87): The legend of a Vehicle Speed Limit (R2-2P series) plaque may be combined in a single sign and displayed below the SPEED LIMIT XX legend, similar to the Combined Maximum and Minimum Speed Limits (R2-4a) sign (see Section 2B.24).
- [O] 2B.22-03 (p.87): A different vehicle class legend may be substituted on the R2-2P series plaque for other classes of vehicles not included in Paragraph 1 of this Section.

<a id="sec-2B-23"></a>
#### Section 2B.23 Night Speed Limit Plaque (R2-3P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R2-3P](symbols/R2-3P.png) | **R2-3P** | Night Speed Limit (plaque) | Optional | 24 x 24 | 24 x 24 | 36 x 36 | 48 x 48 | — | 36 x 36 | 2B-1 p.68 | — |

- **[M]** 2B.23-01 (p.87): Where different speed limits are prescribed for day and night, both limits shall be posted.
- **[R]** 2B.23-02 (p.87): A Night Speed Limit (R2-3P) plaque (see Figure 2B-3) should be reversed using a white retroreflective legend and border on a black background.
- [O] 2B.23-03 (p.87): A Night Speed Limit plaque may be combined with or installed below the standard Speed Limit (R2-1) sign.

<a id="sec-2B-24"></a>
#### Section 2B.24 Minimum Speed Limit Plaque (R2-4P) and Combined Maximum and Minimum Speed Limits Sign (R2-4a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R2-4P](symbols/R2-4P.png) | **R2-4P** | Minimum Speed Limit (plaque) | Optional (2B.24-02) | 24 x 24 | 24 x 24 | 36 x 36 | 48 x 48 | — | 36 x 36 | 2B-1 p.68 | — |
| ![R2-4a](symbols/R2-4a.png) | **R2-4a** | Combined Maximum and Minimum | Optional (2B.24-02) | 24 x 48 | 24 x 48 | 36 x 72 | 48 x 96 | — | 36 x 72 | 2B-1 p.68 | — |

- **[M]** 2B.24-01 (p.87) ◆ R2-4P: A Minimum Speed Limit (R2-4P) plaque (see Figure 2B-3) shall be displayed only in combination with a Speed Limit sign. Where used, the R2-4P plaque shall be mounted below a Speed Limit (R2-1) sign.
- [O] 2B.24-02 (p.87): Where engineering judgment determines that slow speeds on a highway might impede the normal and reasonable movement of traffic, the Minimum Speed Limit (R2-4P) plaque may be installed below a Speed Limit (R2-1) sign to indicate the minimum legal speed. In lieu of a sign assembly with the R2-1 sign and R2-4P plaque, the Combined Maximum and Minimum Speed Limits (R2-4a) sign may be used.

<a id="sec-2B-25"></a>
#### Section 2B.25 Higher Fines Signs and Plaque (R2-6P, R2-10, and R2-11)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R2-6P](symbols/R2-6P.png) | **R2-6P** | Fines Higher (plaque) | Mandatory (2B.25-01) | 24 x 18 | 24 x 18 | 36 x 24 | 48 x 36 | — | 36 x 24 | 2B-1 p.68 | 7B-1, 6G-1 |
| ![R2-6aP](symbols/R2-6aP.png) | **R2-6aP** | Fines Double (plaque) | Mandatory (7B.06-02) | 24 x 18 | 24 x 18 | 36 x 24 | 48 x 36 | — | 36 x 24 | 2B-1 p.68 | 7B-1, 6G-1 |
| ![R2-6bP](symbols/R2-6bP.png) | **R2-6bP** | $XX Fine (plaque) | Mandatory (7B.06-02) | 24 x 18 | 24 x 18 | 36 x 24 | 48 x 36 | — | 36 x 24 | 2B-1 p.68 | 7B-1, 6G-1 |
| ![R2-10](symbols/R2-10.png) | **R2-10** | Begin Higher Fines Zone | Mandatory (2B.25-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.68 | 7B-1, 6G-1 |
| ![R2-11](symbols/R2-11.png) | **R2-11** | End Higher Fines Zone | Mandatory (2B.25-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.68 | 7B-1, 6G-1 |

- **[M]** 2B.25-01 (p.87) ◆ R2-6P, R2-10: Except as provided in Paragraph 3 of this Section, if increased fines are imposed for traffic violations within a designated zone of a roadway, a BEGIN HIGHER FINES ZONE (R2-10) sign (see Figure 2B-3) or a FINES HIGHER (R2-6P) plaque (see Figure 2B-3) shall be used to provide notice to road users.
- **[M]** 2B.25-02 (p.87) ◆ R2-6P, R2-10, R2-11: If an R2-10 sign or an R2-6P plaque is posted to provide notice of increased fines for traffic violations, an END HIGHER FINES ZONE (R2-11) sign (see Figure 2B-3) shall be installed at the downstream end of the zone to provide notice to road users of the termination of the increased fines zone.
- [O] 2B.25-03 (p.87) ◆ R2-6P, R2-10: The BEGIN HIGHER FINES ZONE (R2-10) sign or FINES HIGHER (R2-6P) plaque may be omitted where the higher fines zone is established by statute.
- **[R]** 2B.25-04 (p.87): The BEGIN HIGHER FINES ZONE sign or FINES HIGHER plaque should be located at the beginning of the temporary traffic control zone, school zone, or other applicable designated zone and just beyond any interchanges, major intersections, or other major traffic generators.
- **[R]** 2B.25-05 (p.88): Agencies should limit the use of the Higher Fines signs and plaque to locations where work is actually underway, or to locations where the roadway, shoulder, or other conditions, including the presence of a school zone and/or a reduced school speed limit zone, require a speed reduction or extra caution on the part of the road user.
- **[M]** 2B.25-06 (p.88): The Higher Fines signs and plaque shall have a black legend and border on a white rectangular background. All supplemental plaques mounted below the Higher Fines signs and plaque shall have a black legend and border on a white rectangular background.
- **[M]** 2B.25-07 (p.88): The FINES HIGHER plaque shall be mounted below an applicable regulatory or warning sign in a temporary traffic control zone (see Section 6G.08), a school zone (see Section 7B.06), or other applicable designated zone.
- [O] 2B.25-08 (p.88) ◆ R2-10, R2-11: Alternate legends such as BEGIN (or END) DOUBLE FINES ZONE may also be used for the R2-10 and R2-11 signs.
- [O] 2B.25-09 (p.88) ◆ R2-6P, R2-6aP, R2-6bP: The legend FINES HIGHER on the R2-6P plaque may be replaced by FINES DOUBLE (R2-6aP), $XX FINE (R2-6bP), or another legend appropriate to the specific regulation (see Figure 2B-3).
- [O] 2B.25-10 (p.88) ◆ R2-6P, R2-10: The following may be mounted below an R2-10 sign or R2-6P plaque: A. A supplemental plaque specifying the times that the higher fines are in effect (similar to the S4-1P plaque shown in Figure 7B-1), B. A supplemental plaque WHEN CHILDREN (WORKERS) ARE PRESENT, or C. A supplemental plaque WHEN FLASHING (similar to the S4-4P plaque shown in Figure 7B-1) if used in conjunction with a Speed Limit Sign Beacon (see Section 4S.04).

*Also governed by Section 6G.08:*

- [O] 6G.08-01 (p.795): A WORK ZONE (G20-5aP) plaque (see Figure 6G-1) may be mounted above a Speed Limit sign to emphasize that a reduced speed limit is in effect within a TTC zone. An END WORK ZONE SPEED LIMIT (R2-12) sign (see Figure 6G-1) may be installed at the downstream end of the reduced speed limit zone.
- **[R]** 6G.08-02 (p.795) ◆ R2-10, R2-11: A BEGIN HIGHER FINES ZONE (R2-10) sign (see Figure 6G-1) should be installed at or near the beginning of a TTC zone where increased fines are imposed for traffic violations, and an END HIGHER FINES ZONE (R2-11) sign (see Figure 6G-1) should be installed at or near the downstream end of the TTC zone.
- [O] 6G.08-03 (p.797) ◆ R2-10, R2-11: Alternate legends such as BEGIN (or END) DOUBLE FINES ZONE may also be used for the R2-10 and R2-11 signs.
- [O] 6G.08-04 (p.797): A FINES HIGHER, FINES DOUBLE, or $XX FINE plaque (see Section 2B.25 and Figure 6G-1) may be mounted below the Speed Limit sign if increased fines are imposed for traffic violations within the TTC zone.
- [O] 6G.08-05 (p.797): Individual signs and plaques for work zone speed limits and higher fines may be combined into a single sign or may be displayed as an assembly of signs and plaques.

*Also governed by Section 7B.06:*

- **[M]** 7B.06-02 (p.980): Where increased fines are imposed for traffic violations within a designated school zone: A. A BEGIN HIGHER FINES ZONE (R2‑10) sign (see Figure 7B‑1) or a FINES HIGHER (R2‑6P), FINES DOUBLE (R2‑6aP), or $XX FINE (R2‑6bP) plaque (see Figure 7B‑1) shall be installed as a supplement to the School Zone (S1‑1) sign to identify the beginning point of the higher fines zone (see Figures 7B‑4 and 7B‑5); and B. An END HIGHER FINES ZONE (R2‑11) sign (see Figure 7B‑1) or an END SCHOOL ZONE (S5‑2) sign (see Figure 7B‑1) shall be installed at the downstream end of the zone to notify road users of the termination of the increased fines zone (see Figure 7B‑5).
- **[M]** 7B.06-03 (p.980) ◆ R2-6P, R2-6aP, R2-6bP: If exceeding the speed limit is the only traffic violation that is subject to higher fines, a FINES HIGHER (R2‑6P), FINES DOUBLE (R2‑6aP), or $XX FINE (R2‑6bP) plaque shall be posted with the School Speed Limit (S5‑1) sign and shall not be posted beneath the School Zone (S1‑1) sign (see Section 7B.05).
- **[M]** 7B.06-04 (p.980) ◆ R2-10: If the portion of the roadway that is subject to higher fines does not begin at the location of the School Zone (S1‑1) sign, a BEGIN HIGHER FINES ZONE (R2‑10) sign shall be placed at the point where the higher fines begin (see Sheet 2 of Figure 7B‑5).
- [O] 7B.06-05 (p.980) ◆ R2-6P, R2-6aP, R2-6bP, R2-10: If a BEGIN HIGHER FINES ZONE (R2‑10) sign is used downstream of the School Zone (S1‑1) sign, a FINES HIGHER (R2‑6P), FINES DOUBLE (R2‑6aP), or $XX FINE (R2‑6bP) plaque may also be placed beneath the School Zone (S1‑1) sign.
- **[R]** 7B.06-07 (p.983) ◆ R2-6P, R2-6aP, R2-6bP: If other traffic violations in addition to exceeding the speed limit are subject to higher fines, then the duplicate FINES HIGHER (R2‑6P), FINES DOUBLE (R2‑6aP), or $XX FINE (R2‑6bP) plaque should be omitted from the School Speed Limit When Flashing (S5‑1) sign (see Section 7B.05).
- [O] 7B.06-08 (p.983) ◆ R2-11: If a higher fines zone ends at the same point as a reduced school speed limit zone, an END SCHOOL ZONE (S5‑2) sign may be used instead of a combination of an END HIGHER FINES ZONE (R2‑11) sign and an END SCHOOL SPEED LIMIT (S5‑3) sign (see Figure 7B‑5).
- [O] 7B.06-09 (p.983) ◆ R2-6P, R2-6aP, R2-6bP, R2-10: Where the higher fines zone is established by statute, the BEGIN HIGHER FINES ZONE (R2‑10) sign, FINES HIGHER (R2‑6P), FINES DOUBLE (R2‑6aP), and $XX FINE (R2‑6bP) plaques may be omitted.

<a id="sec-2B-26"></a>
#### Section 2B.26 Movement Prohibition Signs (R3-1 through R3-4, R3-18, and R3-27)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-1](symbols/R3-1.png) | **R3-1** | No Right Turn | Mandatory (2B.26-01) | 24 x 24 | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2B-1 p.68 | 6G-1 |
| ![R3-1b](symbols/R3-1b.png) | **R3-1b** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 36 | 24 x 36 | 36 x 54 | 36 x 54 | — | — | 2B-1 p.68 | — |
|  | **R3-1c** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 42 | 24 x 42 | 36 x 60 | 36 x 60 | — | — | 2B-1 p.68 | — |
| ![R3-1d](symbols/R3-1d.png) | **R3-1d** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 48 | 24 x 48 | 36 x 66 | 36 x 66 | — | — | 2B-1 p.68 | — |
| ![R3-1e](symbols/R3-1e.png) | **R3-1e** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 36 | 24 x 36 | 36 x 54 | 36 x 54 | — | — | 2B-1 p.68 | — |
| ![R3-1f](symbols/R3-1f.png) | **R3-1f** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | — | 2B-1 p.68 | — |
| ![R3-1g](symbols/R3-1g.png) | **R3-1g** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 36 | 24 x 36 | 36 x 54 | 36 x 54 | — | — | 2B-1 p.68 | — |
|  | **R3-1h** | Movement Prohibition - | Mandatory (2B.26-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | — | 2B-1 p.69 | — |
| ![R3-2](symbols/R3-2.png) | **R3-2** | No Left Turn | Mandatory (2B.26-01) | 24 x 24 | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2B-1 p.68 | 6G-1 |
| ![R3-3](symbols/R3-3.png) | **R3-3** | NO TURNS | Mandatory (2B.26-01) | 24 x 24 | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2B-1 p.68 | 6G-1 |
| ![R3-4](symbols/R3-4.png) | **R3-4** | No U-Turn | Mandatory (2B.26-01) | 24 x 24 | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2B-1 p.68 | 6G-1 |
| ![R3-18](symbols/R3-18.png) | **R3-18** | No U or Left Turn | Mandatory (2B.26-01) | 24 x 24 | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2B-1 p.68 | 6G-1 |
| ![R3-27](symbols/R3-27.png) | **R3-27** | No Straight Through | Mandatory (2B.26-01) | 24 x 24 | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2B-1 p.68 | 6G-1 |

- **[M]** 2B.26-01 (p.89): Movement Prohibition signs (see Figure 2B-4) shall be installed where specific movements are prohibited at an intersection approach except as provided in Paragraphs 13 and 17 of this Section.
- **[R]** 2B.26-02 (p.89): Movement Prohibition signs should only be used to prohibit a turn or through movement from an entire approach and should not be used to designate movements that are required or permitted from a specific lane or lanes on a multi-lane approach.
- **[R]** 2B.26-03 (p.89): Movement Prohibition signs should be placed where they will be most easily seen by road users who might be intending to make the movement.
- **[R]** 2B.26-04 (p.89) ◆ R3-1: If a No Right Turn (R3-1) sign (see Figure 2B-4) is used, at least one should be placed either over the roadway or at a right-hand corner of the intersection.
- **[R]** 2B.26-05 (p.89) ◆ R3-2: If a No Left Turn (R3-2) sign (see Figure 2B-4) is used, at least one should be placed over the roadway, at the far left corner of the intersection, on a median, or in conjunction with the STOP sign or YIELD sign located on the near right corner.
- **[R]** 2B.26-06 (p.89) ◆ R3-3: Except as provided in Item C in Paragraph 11 of this Section for signalized locations, if a NO TURNS (R3-3) sign (see Figure 2B-4) is used, two signs should be used, one at a location specified for a No Right Turn sign and one at a location specified for a No Left Turn sign.
- **[R]** 2B.26-07 (p.89) ◆ R3-4, R3-18: If a No U-Turn (R3-4) sign (see Figure 2B-4) or a combination No U or Left Turn (R3-18) sign (see Figure 2B-4) is used, at least one should be used at a location specified for a No Left Turn sign.
- **[R]** 2B.26-08 (p.89) ◆ R3-2, R3-4, R3-18: If both left turns and U-turns are prohibited, the combination No U or Left Turn (R3-18) sign should be used instead of separate R3-2 and R3-4 signs.
- **[R]** 2B.26-10 (p.89) ◆ R3-27: If a No Straight Through (R3-27) sign (see Figure 2B-4) is used, at least one should be placed either over the roadway or at a location where it can be seen by road users who might be intending to travel straight through the intersection. If turn prohibition signs are installed in conjunction with traffic control signals:
- **[R]** 2B.26-11 (p.89): If turn prohibition signs are installed in conjunction with traffic control signals: A. The No Right Turn sign should be installed adjacent to a signal face viewed by road users in the right-hand lane. B. The No Left Turn (or No U-Turn or combination No U or Left Turn) sign should be installed adjacent to a signal face viewed by road users in the left-hand lane. C. A NO TURNS sign should be placed adjacent to a signal face viewed by all road users on that approach, or two signs should be used.
- [O] 2B.26-12 (p.89): If turn prohibition signs are installed in conjunction with traffic control signals, an additional turn prohibition sign may be post-mounted to supplement the sign mounted overhead.
- [O] 2B.26-13 (p.89): Where ONE WAY signs are used (see Section 2B.49), No Left Turn and No Right Turn signs may be omitted.
- [O] 2B.26-14 (p.89) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: Where the movement restriction applies to certain vehicle classes, signs incorporating a supplementary legend, modified as appropriate, may be used to indicate the specific vehicle class restriction (R3-1b through R3-1d) or exception (R3-1e and R3-1f) (see Figure 2B-4). When the movement restriction applies during certain time periods only, the following Movement Prohibition signing alternatives may be used and are listed in order of preference: A. A blank-out or changeable message sign (see Chapter 2L) that displays the prohibited movement only during the time that the movement prohibition is applicable, especially at signalized intersections. B. Permanently-mounted signs incorporating a supplementary legend showing the hours and days during which the prohibition is applicable (R3-1g and R3-1h) (see Figure 2B-4). C. Portable signs, installed by proper authority, located off the roadway at each corner of the intersection. The portable signs are only to be used during the time that the movement prohibition is applicable.
- **[M]** 2B.26-15 (p.91): The blank-out part-time electronic-display Movement Prohibition sign shall consist of a red circle and diagonal with a white prohibited movement on an opaque black background.
- [O] 2B.26-16 (p.91): Movement Prohibition signs may be omitted at a ramp entrance to an expressway or a channelized intersection where the design is such as to indicate clearly the one-way traffic movement on the ramp or turning lane.
- **[M]** 2B.26-17 (p.91) ◆ R3-2, R3-4, R3-18: The No Left Turn (R3-2) sign, the No U-Turn (R3-4) sign, and the combination No U or Left Turn (R3-18) sign shall not be used at approaches to roundabouts to prohibit drivers from turning left onto the circulatory roadway of a roundabout.
- [S] 2B.26-18 (p.91) ◆ R3-2, R3-4, R3-18: At roundabouts, the use of R3-2, R3-4, or R3-18 signs to prohibit left turns onto the circulatory roadway might confuse drivers about the possible legal turning movements around the roundabout. Roundabout Circulation (R6-5P) plaques (see Section 2B.51) and/or ONE WAY (R6-1 or R6-2) signs are appropriate to indicate the travel direction within a roundabout.

*Also governed by Section 2B.28:*

- **[M]** 2B.28-01 (p.92): Mandatory Movement Lane Control (R3-5, R3-5a, and R3-7) signs (see Figure 2B-4), if used, shall indicate only the single vehicle movement that is required from the lane.
- **[M]** 2B.28-02 (p.92): The Mandatory Movement Lane Control (R3-5 and R3-5a) symbol signs shall include the legend ONLY and shall be mounted overhead over the specific lanes to which they apply (see Section 2B.27). The R3-7 sign shall be for post-mounting only. The R3-7 sign shall not be mounted at the far side of the intersection.
- **[M]** 2B.28-03 (p.92): When the mandatory movement applies to lanes exclusively designated for HOV traffic, the HOV 2+ (R3-5cP) supplemental plaque shall be used. When the mandatory movement applies to lanes that are not HOV facilities, but are lanes exclusively designated for buses and/or taxis, the TAXI LANE (R3-5dP) and/ or BUS LANE (R3-5gP) supplemental plaques shall be used.
- **[M]** 2B.28-04 (p.93): If used, the Mandatory Movement Lane Control (R3-7) sign shall be located in advance of the intersection, such as near the upstream end of the mandatory movement lane, and/or at the near side of the intersection where the regulation applies.
- **[R]** 2B.28-05 (p.93): The use of the Mandatory Movement Lane Control (R3-7) word message sign should be limited to only locations that are adjacent to the full-width portion of a mandatory turn lane. The R3-7 sign should not be installed adjacent to a through lane in advance of a turn bay taper or adjacent to a turn bay taper.
- **[R]** 2B.28-06 (p.93): Mandatory Movement Lane Control signs should be accompanied by lane-use arrow markings, especially where traffic volumes are high, where there is a high percentage of commercial vehicles, or where other distractions exist.
- **[R]** 2B.28-07 (p.93): Where the restriction does not apply to buses or bicycles an EXCEPT BUSES (R3-7aP) or EXCEPT BICYCLES (R3-7bP) plaque should be used.
- [O] 2B.28-08 (p.93): The Through Only (R3-5a) sign may be used to require a road user in a particular lane to proceed straight through an intersection.
- [O] 2B.28-09 (p.93) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: The diamond symbol may be used instead of the word message HOV on the R3-5cP supplemental plaque. 10 Where a mandatory left or U-turn lane is added at a median location, a LANE FOR LEFT TURN ONLY (R3-19) or LANE FOR U TURN ONLY (R3-19a) sign may be post-mounted on the median at the beginning of the taper. Where a U turn and a left turn are both allowed, a LANE FOR U AND LEFT TURNS ONLY (R3-19b) sign may be used. Where a R3-19 series sign is used, Mandatory Movement Lane Control signs along the turn lane in the median may be omitted.
- [O] 2B.28-11 (p.93) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: The R3-19 series signs may be used where the added median turn lane is separated from the through lanes by a channelizing or divisional island.
- [O] 2B.28-12 (p.93): On an approach to a mandatory turn lane where traffic regularly enters the shoulder to access the turn lane inappropriately, creating safety or operational issues, a DO NOT DRIVE ON SHOULDER (R4-17) sign (see Section 2B.43) may be used to supplement the standard Mandatory Movement Lane Control (R3-5 and/or R3-7 series) signs.

*Also governed by Section 2B.35:*

- **[M]** 2B.35-03 (p.98): On multi-lane roadways, since road users generally anticipate that they need to be in the left-hand lane when approaching a location where they desire to turn left or make a U-turn, an ALL TURNS FROM RIGHT LANE (R3-23) or a U TURN FROM RIGHT LANE (R3-23a) sign (see Figure 2B-8) shall be installed in advance of the location to inform drivers that left turns and/or U-turns will be made from the right-hand lane.
- [O] 2B.35-04 (p.98): Where a median of sufficient width is available, supplemental regulatory or guide signs may also be placed on the left-hand side of the roadway.
- **[M]** 2B.35-05 (p.98) ◆ R3-2: The R3-24 series sign with an upward diagonal arrow pointing to the right if the jughandle entrance is designed as an exit ramp (see Drawings A and B in Figure 2B-9), or the R3-25 series sign with a horizontal arrow pointing to the right if the jughandle entrance is designed as an intersection, shall be installed on the right-hand side of the roadway at the entrance to the jughandle. The legend on the sign shall be ALL TURNS, U TURN, or U AND LEFT TURNS, as appropriate.
- **[M]** 2B.35-06 (p.98) ◆ R3-2: If the jughandle is designed such that the jughandle entrance is downstream of the location where the turn would normally have been made (see Drawing C in Figure 2B-9), the R3-26 series sign with an arrow pointing straight upward shall be installed on the right-hand side of the roadway at the intersection to inform road users that they need to proceed straight through the intersection in order to make a left turn or U-turn. The legend on the sign shall be U TURN or U AND LEFT TURNS, as appropriate.
- [S] 2B.35-07 (p.98) ◆ R3-2: The R3-24, R3-25, and R3-26 series of signs are designed to be mounted below conventional guide signs.

*Also governed by Section 2G.04:*

- **[M]** 2G.04-01 (p.412): The R3-10, R3-13, and R3-13a Vehicle Occupancy Definition signs (see Figure 2G-1) shall be used where agencies determine that it is appropriate to provide a sign that defines the minimum occupancy of vehicles that are allowed to use an HOV lane.
- **[R]** 2G.04-02 (p.412): The Inherently Low Emission Vehicle (ILEV) (R3-10a) sign (see Figure 2G-1) should be used when it is permissible for a properly labeled and certified ILEV, regardless of the number of occupants, to use an HOV lane. When used, the ILEV signs should be post-mounted in advance of and at intervals along the HOV lane based upon engineering judgment and the placement of other Preferential Lane regulatory signs. The R3-10a sign is only applicable to HOV lanes and should not to be used with other preferential lane applications.
- **[M]** 2G.04-05 (p.412): For barrier-separated, buffer-separated, or contiguous preferential lanes where access between the preferential and general-purpose lanes is restricted to designated locations on freeways and expressways, an overhead Vehicle Occupancy Definition (R3-13 or R3-13a) sign shall be installed at least ½ mile in advance of the beginning of or initial entry point to an HOV lane. These signs shall only be displayed in advance of the beginning of or initial or intermediate entry point to HOV lanes.
- **[M]** 2G.04-06 (p.412): For buffer-separated or contiguous HOV lanes where access is restricted to designated locations on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign shall be located at intervals not greater than ½ mile along the length of designated gaps where vehicles are allowed to legally access the HOV lane, and within designated enforcement areas as defined by the operating agency.
- [O] 2G.04-07 (p.412): For buffer-separated or contiguous HOV lanes where access is restricted to designated locations on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign may be located at intervals of approximately ½ mile along the length of the HOV lane.
- [O] 2G.04-08 (p.415): For barrier-separated HOV lanes on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign may be located at intervals of approximately ½ mile along the length of the HOV lane, at intermediate entry points, and at designated enforcement areas as defined by the operating agency.
- **[M]** 2G.04-09 (p.415): For buffer-separated or contiguous HOV lanes where continuous access with the adjacent generalpurpose lanes is provided on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R310) sign, and ILEV (R3-10a) signs, if appropriate, shall be located at intervals not greater than ½ mile along the length of the HOV lane.
- **[R]** 2G.04-10 (p.415): On freeways and expressways, the signs within each Preferential Lane regulatory sign sequence should be separated by a minimum distance of 800 feet and a maximum distance of 1,000 feet.
- **[R]** 2G.04-11 (p.415): On conventional roads, the distance between Preferential Lane regulatory signs within each sequence should be determined by engineering judgment based on speed, block length, distances from adjacent intersections, and other site-specific considerations.
- **[M]** 2G.04-12 (p.415): For all types of direct access ramps that provide access to or lead to HOV lanes, a post-mounted Vehicle Occupancy Definition (R3-10) sign, and an ILEV (R3-10a) sign, if appropriate, shall be used at the beginning or initial entry point for the direct access ramp.

*Also governed by Section 2G.05:*

- [S] 2G.05-01 (p.415) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: The standardized sizes of post-mounted Preferential Lane Operation (R3-11 series) signs are consistent to accommodate any future addition or removal of a single line of legend for each sign. Each size accommodates two lines of legend for the times of day and days of week that the regulation is in effect. Consistent sign sizes are beneficial for agencies when ordering sign materials, as well as when making legend changes to existing signs if changes occur to operating times or occupancy restrictions in the future.
- **[R]** 2G.05-02 (p.415) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: Where the regulation is in effect during more than one time period of the day, such as during the morning and afternoon peak periods, the height of the R3-11 and R3-14 series signs should be suitably increased to accommodate the additional line(s) of legend.
- **[M]** 2G.05-03 (p.415) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: When used, the post-mounted Preferential Lane Operation (R3-11 series) signs shall be located adjacent to the preferential lane, and the overhead Preferential Lane Operation (R3-14 series) signs shall be mounted directly over the lane.
- **[M]** 2G.05-04 (p.415) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: The legend format of the post-mounted Preferential Lane Operation (R3-11 series) signs shall have the following sequence: A. Top Lines: Lanes applicable, such as “RIGHT LANE” or “2 RIGHT LANES” B. Middle Lines: Eligible uses, such as “HOV 2+ ONLY” (or 3+ or 4+, if appropriate) or “BUSES ONLY” or other applicable uses or eligible turning movements C. Bottom Lines: Applicable times and days, such as “7 AM – 9 AM” or “6:30 AM – 9:30 AM, MON-FRI”
- **[M]** 2G.05-05 (p.415) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: The legend format of the overhead Preferential Lane Operation (R3-14 series) signs shall have the following sequence: A. Top Lines: Eligible uses, such as “HOV 2+ ONLY” (or 3+ or 4+, if appropriate) or “BUSES ONLY” or other applicable uses or eligible turning movements B. Bottom Lines: Applicable times and days, with the time and day placed above the down arrow, such as “7 AM – 9 AM” or “6:30 AM – 9:30 AM, MON-FRI.” When the operating periods exceed the available line width, the hours and days of the week shall be stacked as shown for the R3-14a sign in Figure 2G-1.
- **[M]** 2G.05-06 (p.415): For preferential lane restrictions that are in effect on a full-time (24 hours per day, seven days per week) basis, the Preferential Lane Operation (R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, and R3-14g) signs that include a period of operation legend shall be modified to display no legend relative to the period of operation except as provided in Paragraph 7 of this Section.
- [O] 2G.05-07 (p.416): In lieu of removing the period of operation text from the Preferential Lane Operation signs for full-time operation, the legend 24 HOURS may be substituted for the times and days of the week on the Preferential Lane Operation (R3-11, R3-11a, R3-11d, R3-11f, R3-14, R3-14d, and R3-14f) signs for preferential lane restrictions that are in effect on a full-time basis.
- **[M]** 2G.05-09 (p.416): The full-time Preferential Lane Operation (R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, and R3-14g) signs that do not display a period of operation legend, as described in Paragraph 6 of this Section, shall not be used where the preferential lane restriction is in effect only on a part-time basis.
- [O] 2G.05-10 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: Where additional movements are allowed from a preferential lane on an approach to an intersection by vehicles not meeting the preferential lane regulation, the format and words used in the legend in the middle lines on the post-mounted Preferential Lane Operation (R3-11 series) signs and on the top line of the overhead Preferential Lane Operation (R3-14 series) signs may be modified to accommodate the allowable movements (such as “HOV 2+ AND RIGHT TURNS ONLY”).
- [O] 2G.05-11 (p.416): The MOTORCYCLES ALLOWED (R3-11hP) plaque (see Figure 2G-1) may be used where motorcycles, regardless of the number of occupants, are allowed to use an HOV lane.
- **[M]** 2G.05-12 (p.416): If used, the MOTORCYCLES ALLOWED plaque shall be mounted below a post-mounted Preferential Lane Operation (R3-11, R3-11a, or R3-11b) sign.
- **[M]** 2G.05-13 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: For all barrier-separated or buffer-separated or contiguous preferential lanes where access is restricted to designated locations, an overhead Preferential Lane Operation (R3-14 series) sign shall be used at the beginning or initial entry point on freeways, expressways, and at locations on conventional roadways where the preferential lane is not the outermost (far right or far left) lane of the roadway, and at any intermediate entry points or gaps in the barrier or buffer where vehicles are allowed to legally enter the access-restricted preferential lanes. For all barrier-separated and buffer-separated preferential lanes, post-mounted Preferential Lane Operation (R3-11 series) signs shall be used only as a supplement to the overhead signs on freeways, expressways, and at locations on conventional roadways where the preferential lane is not the outermost lane of the roadway at the beginning or initial entry point, or at any intermediate entry points or gaps in the barrier or buffer.
- **[M]** 2G.05-14 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: For buffer-separated or contiguous preferential lanes where continuous access with the adjacent general-purpose lanes is provided, including those where a preferential lane is added to the roadway (see Figure 2G-2 for HOV lanes) and those where a general-purpose lane transitions into a preferential lane (see Figure 2G-3 for HOV lanes), an overhead Preferential Lane Operation (R3-14 series) sign shall be used at the beginning or initial entry point of the preferential lane on freeways and expressways.
- [O] 2G.05-15 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: On conventional roads where preferential lane operations exist, R3-11 series post-mounted signs may be used in lieu of or in addition to overhead R3-14 series signs, except where overhead signs are required as provided in Paragraph 14 of this Section.
- [O] 2G.05-16 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: Additional overhead (R3-14 series) or post-mounted (R3-11 series) Preferential Lane Operation signs may be provided along the length of any type of preferential lane.
- **[M]** 2G.05-17 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: For all types of direct access ramps that provide access to or lead to preferential lanes, a post-mounted Preferential Lane Operation (R3-11 series) sign shall be used at the beginning or initial entry point of the direct access ramp.
- [O] 2G.05-18 (p.416) ◆ R3-1, R3-1b, R3-1c, R3-1d, R3-1e, R3-1f, R3-1g, R3-1h: For direct access ramps to preferential lanes, an overhead Preferential Lane Operation (R3-14 series) sign may be used at the beginning or initial entry point to supplement the required post-mounted signs.
- [O] 2G.05-19 (p.416): Lane-use control signals (see Chapter 4T) may be used at access points to preferential lanes to indicate that a ramp or access roadway leading to the preferential lane or facility, or one or more specific lanes of the facility, are open or closed (see Figure 2G-1).

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

<a id="sec-2B-28"></a>
#### Section 2B.28 Mandatory Movement Lane Control Signs (R3-5, R3-5a, R3-7, R3-19 Series, and R3-20) and Plaques

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-5](symbols/R3-5.png) | **R3-5** | Mandatory Movement Lane Control Signs | Mandatory (2B.28-03) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.69 | 6G-1 |
| ![R3-5a](symbols/R3-5a.png) | **R3-5a** | Mandatory Movement Lane Control | Mandatory (2B.28-03) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-5bP](symbols/R3-5bP.png) | **R3-5bP** | Left Lane (plaque) | Mandatory (2B.28-03) | 30 x 12 | 30 x 12 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-5cP](symbols/R3-5cP.png) | **R3-5cP** | HOV 2+ (plaque) | Mandatory (2B.28-03) | 24 x 12 | 24 x 12 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-5dP](symbols/R3-5dP.png) | **R3-5dP** | Taxi Lane (plaque) | Mandatory (2B.28-03) | 30 x 12 | 30 x 12 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-5fP](symbols/R3-5fP.png) | **R3-5fP** | Right Lane (plaque) | Mandatory (2B.28-03) | 30 x 12 | 30 x 12 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-5gP](symbols/R3-5gP.png) | **R3-5gP** | Bus Lane (plaque) | Mandatory (2B.28-03) | 30 x 12 | 30 x 12 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-7](symbols/R3-7.png) | **R3-7** | Right (Left) Lane Must Turn | Mandatory (2B.28-03) | 30 x 30 | 36 x 36 | 48 x 48 | — | — | 48 x 48 | 2B-1 p.69 | 6G-1 |
| ![R3-7aP](symbols/R3-7aP.png) | **R3-7aP** | Except Buses (plaque) | Recommended (2B.28-07) | 24 x 12 | 24 x 12 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-7bP](symbols/R3-7bP.png) | **R3-7bP** | Except Bicycles (plaque) | Recommended (2B.28-07) | 24 x 12 | 24 x 12 | — | — | — | — | 2B-1 p.69 | 9A-1 |
| ![R3-8](symbols/R3-8.png) | **R3-8** | Advance Intersection Lane Control | Mandatory (2B.28-03) | — | — | — | Varies x 36 | — | — | 2B-1 p.69 | 6G-1 |
| ![R3-8a](symbols/R3-8a.png) | **R3-8a** |  | Mandatory (2B.28-03) | — | — | — | Varies x 36 | — | — | 2B-1 p.69 | — |
| ![R3-8b](symbols/R3-8b.png) | **R3-8b** |  | Mandatory (2B.28-03) | — | — | — | Varies x 36 | — | — | 2B-1 p.69 | — |
| ![R3-8xa](symbols/R3-8xa.png) | **R3-8xa** |  | Mandatory (2B.28-03) | — | — | — | Varies x 36 | — | — | 2B-1 p.69 | — |
| ![R3-8xb](symbols/R3-8xb.png) | **R3-8xb** |  | Mandatory (2B.28-03) | — | — | — | Varies x 36 | — | — | 2B-1 p.69 | — |
| ![R3-8xc](symbols/R3-8xc.png) | **R3-8xc** |  | Mandatory (2B.28-03) | — | — | — | Varies x 36 | — | — | 2B-1 p.69 | — |
| ![R3-19](symbols/R3-19.png) | **R3-19** | Lane For Left Turn Only | Mandatory (2B.28-03) | 30 x 24 | 30 x 24 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-19a](symbols/R3-19a.png) | **R3-19a** | Lane for U Turn Only | Mandatory (2B.28-03) | 30 x 24 | 30 x 24 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-19b](symbols/R3-19b.png) | **R3-19b** | Lane For U and Left Turns Only | Mandatory (2B.28-03) | 30 x 30 | 30 x 30 | — | — | — | — | 2B-1 p.69 | — |
|  | **R3-20** | Begin Right (Left) Turn Lane | Mandatory (2B.28-03) | 24 x 36 | 24 x 36 | — | — | — | — | 2B-1 p.69 | — |

*Also governed by Section 2B.27:*

- **[M]** 2B.27-01 (p.91): Intersection Lane Control signs (see Figure 2B-4), if used, shall require road users in certain lanes to turn, shall permit turns from a lane where such turns would otherwise not be permitted, shall require a road user to stay in the same lane and proceed straight through an intersection, or shall indicate permitted movements from a lane.
- [S] 2B.27-02 (p.91) ◆ R3-5, R3-5a, R3-5bP, R3-5cP, R3-5dP, R3-5fP, R3-5gP, R3-7, R3-7aP, R3-7bP, R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: Intersection Lane Control signs have three applications: A. Mandatory Movement Lane Control (R3-5 series and R3-7 series) signs, B. Optional Movement Lane Control (R3-6 series) signs, and C. Advance Intersection Lane Control (R3-8 series) signs.
- **[R]** 2B.27-03 (p.92): When Intersection Lane Control signs are mounted overhead, each sign used should be placed over the lane or a projection of the lane to which it applies.
- **[R]** 2B.27-04 (p.92): On signalized approaches where through lanes that become mandatory turn lanes, multiple-lane turns that include shared lanes for through and turning movements, or other lane-use regulations are present that would be unexpected by unfamiliar road users, overhead Intersection Lane Control signs should be installed at the signalized location over the appropriate lanes or projections thereof and in advance of the intersection over the appropriate lanes.
- **[R]** 2B.27-05 (p.92) ◆ R3-7, R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: Where overhead mounting on the approach is impracticable for the Advance and/or Intersection lane Control signs, one of the following alternatives should be employed: A. At locations where through lanes become mandatory turn lanes, a Mandatory Movement Lane Control (R3-7) sign should be post-mounted on the left-hand side of the roadway where a through lane is becoming a mandatory left-turn lane on a one-way street or where a median of sufficient width for the signs is available, or on the right-hand side of the roadway where a through lane is becoming a mandatory right-turn lane. B. At locations where a through lane is becoming a mandatory left-turn lane on a two-way street where a median of sufficient width for the signs is not available, and at locations where multiple-lane turns that include shared lanes for through and turning movements are present, an Advance Intersection Lane Control (R3-8 series) sign should be post-mounted in a prominent location in advance of the intersection, and consideration should be given to the use of an oversized version in accordance with Table 2B-1.
- **[R]** 2B.27-06 (p.92): Use of an overhead sign for one approach lane should not require installation of overhead signs for the other lanes of that approach.
- [O] 2B.27-07 (p.92): Intersection Lane Control signs may be omitted where: A. A turn bay has been provided by physical construction or pavement markings, and B. Only the road users using such turn bays are permitted to make a turn in that direction.
- [O] 2B.27-08 (p.92) ◆ R3-5, R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: At roundabouts, Intersection Lane Control (R3-5, R3-6, and R3-8 series) signs may display any of the arrow symbol options shown in Figure 2B-5.

- **[M]** 2B.28-01 (p.92) ◆ R3-5, R3-5a, R3-7: Mandatory Movement Lane Control (R3-5, R3-5a, and R3-7) signs (see Figure 2B-4), if used, shall indicate only the single vehicle movement that is required from the lane.
- **[M]** 2B.28-02 (p.92) ◆ R3-5, R3-5a, R3-7: The Mandatory Movement Lane Control (R3-5 and R3-5a) symbol signs shall include the legend ONLY and shall be mounted overhead over the specific lanes to which they apply (see Section 2B.27). The R3-7 sign shall be for post-mounting only. The R3-7 sign shall not be mounted at the far side of the intersection.
- **[M]** 2B.28-03 (p.92) ◆ R3-5cP, R3-5dP, R3-5gP: When the mandatory movement applies to lanes exclusively designated for HOV traffic, the HOV 2+ (R3-5cP) supplemental plaque shall be used. When the mandatory movement applies to lanes that are not HOV facilities, but are lanes exclusively designated for buses and/or taxis, the TAXI LANE (R3-5dP) and/ or BUS LANE (R3-5gP) supplemental plaques shall be used.
- **[M]** 2B.28-04 (p.93) ◆ R3-7: If used, the Mandatory Movement Lane Control (R3-7) sign shall be located in advance of the intersection, such as near the upstream end of the mandatory movement lane, and/or at the near side of the intersection where the regulation applies.
- **[R]** 2B.28-05 (p.93) ◆ R3-7: The use of the Mandatory Movement Lane Control (R3-7) word message sign should be limited to only locations that are adjacent to the full-width portion of a mandatory turn lane. The R3-7 sign should not be installed adjacent to a through lane in advance of a turn bay taper or adjacent to a turn bay taper.
- **[R]** 2B.28-06 (p.93): Mandatory Movement Lane Control signs should be accompanied by lane-use arrow markings, especially where traffic volumes are high, where there is a high percentage of commercial vehicles, or where other distractions exist.
- **[R]** 2B.28-07 (p.93) ◆ R3-7aP, R3-7bP: Where the restriction does not apply to buses or bicycles an EXCEPT BUSES (R3-7aP) or EXCEPT BICYCLES (R3-7bP) plaque should be used.
- [O] 2B.28-08 (p.93) ◆ R3-5a: The Through Only (R3-5a) sign may be used to require a road user in a particular lane to proceed straight through an intersection.
- [O] 2B.28-09 (p.93) ◆ R3-5cP, R3-19, R3-19a, R3-19b: The diamond symbol may be used instead of the word message HOV on the R3-5cP supplemental plaque. 10 Where a mandatory left or U-turn lane is added at a median location, a LANE FOR LEFT TURN ONLY (R3-19) or LANE FOR U TURN ONLY (R3-19a) sign may be post-mounted on the median at the beginning of the taper. Where a U turn and a left turn are both allowed, a LANE FOR U AND LEFT TURNS ONLY (R3-19b) sign may be used. Where a R3-19 series sign is used, Mandatory Movement Lane Control signs along the turn lane in the median may be omitted.
- [O] 2B.28-11 (p.93) ◆ R3-19, R3-19a, R3-19b: The R3-19 series signs may be used where the added median turn lane is separated from the through lanes by a channelizing or divisional island.
- [O] 2B.28-12 (p.93) ◆ R3-5, R3-7, R3-7aP, R3-7bP: On an approach to a mandatory turn lane where traffic regularly enters the shoulder to access the turn lane inappropriately, creating safety or operational issues, a DO NOT DRIVE ON SHOULDER (R4-17) sign (see Section 2B.43) may be used to supplement the standard Mandatory Movement Lane Control (R3-5 and/or R3-7 series) signs.

*Also governed by Section 2B.30:*

- [O] 2B.30-01 (p.93) ◆ R3-8, R3-8a, R3-8b: Advance Intersection Lane Control (R3-8, R3-8a, and R3-8b) signs (see Figure 2B-4) may be used to indicate the configuration of all lanes ahead.
- [O] 2B.30-02 (p.93) ◆ R3-8: The word messages ONLY, THRU, HOV 2+, TAXI, BUS, or BIKE, or the bicycle symbol, may be used within the border in combination with the arrow symbols of the R3-8 sign series. The R3-5cP, R3-5dP, and R3-5gP supplemental plaques may be installed at the top outside border of the R3-8 sign over the applicable lane designation on the sign. The diamond symbol may be used instead of the word message HOV. The minimum allowable vehicle occupancy requirement may vary based on the level established for a particular facility.
- [O] 2B.30-03 (p.94) ◆ R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: Where a bicycle lane is between two general-purpose lanes the R3-8 series signs may be modified to show the bicycle lane with a white legend on a black background in accordance with designs of the R3-8x series signs (see Figure 2B-4).
- **[R]** 2B.30-04 (p.94): When used, an Advance Intersection Lane Control sign should be placed at an adequate distance in advance of the intersection, either along the lane tapers or at the beginning of the turn lane so that road users can select the appropriate lane (see Figure 2A-4).
- [O] 2B.30-05 (p.94): An Advance Intersection Lane Control sign may be repeated closer to the intersection along the approach for additional emphasis.
- **[M]** 2B.30-06 (p.94) ◆ R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: An Advance Intersection Lane Control (R3-8 series) sign shall not be mounted at the far side of an intersection to which it applies.
- **[M]** 2B.30-07 (p.94) ◆ R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: Where three or more approach lanes are available to traffic, Advance Intersection Lane Control (R3-8 series) signs, if used, shall be post-mounted in advance of the intersection and shall not be mounted overhead.
- **[M]** 2B.30-08 (p.94) ◆ R3-8: When only the two outermost lanes of the roadway are shown on a R3-8 sign, the R3-5bP or R3-5fP plaque shall be mounted above the R3-8 sign.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 9B.02:*

- **[R]** 9B.02-02 (p.1054) ◆ R3-7bP: Where an engineering study or engineering judgment demonstrates that it is appropriate to exempt bicyclists from the provisions of a regulatory sign, the EXCEPT BICYCLES (R3-7bP) regulatory plaque (see Figure 9B-1) should be used.
- **[M]** 9B.02-05 (p.1055): The EXCEPT BICYCLES regulatory plaque shall not be used to exempt bicyclists from the legal requirement of a STOP or YIELD sign, Yield Here to Pedestrians Signs, Stop Here for Pedestrians Signs, or a traffic signal indication.
- **[M]** 9B.02-06 (p.1055): Where a regulatory sign, such as the No Left Turn (R3-2) sign (see Section 2B.26), is installed on the same post or mounting as a STOP sign or YIELD sign, the EXCEPT BICYCLES regulatory plaque shall not be installed in conjunction with the regulatory sign on that post or mounting that includes the STOP sign or YIELD sign.
- **[M]** 9B.02-07 (p.1055): The EXCEPT BICYCLES regulatory plaque shall be placed below the regulatory sign that it supplements.

*Also governed by Section 9B.03:*

- [O] 9B.03-01 (p.1055) ◆ R3-8, R3-8a, R3-8b, R3-8xa, R3-8xb, R3-8xc: Advance Intersection Lane Control (R3-8 series) signs (see Section 2B.30) may display the arrangement of a conventional or buffer-separated bicycle lane in relation to other lanes in the same direction that are present on a roadway approach to an intersection.
- **[R]** 9B.03-03 (p.1055): On an approach to an intersection with complex geometry that can include multiple through lanes and multiple turn lanes and also includes a bicycle lane, consideration should be given to displaying all allowable movements on separate signs, such as using Mandatory Movement Lane Control (R3-5) signs (see Section 2B.28) for the through lanes and Mandatory Movement Lane Control (R3-7) signs (see Section 2B.28) for the turn lanes, and guide signs for bicycle routes (see Section 9D.02 through 9D.07) and Bicycle Route Sign auxiliary plaques (see Section 9D.08) for the bicycle movement.
- **[M]** 9B.03-04 (p.1055): The portion of the sign face for the bicycle lane shall be limited to the relationship of the bicycle lane to the other lanes on the roadway approach to the intersection. The portion of the sign face for the bicycle lane shall not be modified to display specific, supplementary information about the bicycle lane such as bicycle lane extensions, contiguous buffer spaces, or other ancillary bicycle operations such as two-stage turn boxes or bicycle boxes.
- **[M]** 9B.03-05 (p.1055): Counter-flow bicycle lanes shall not be displayed on Advance Intersection Lane Control signs.
- **[M]** 9B.03-06 (p.1055): The shared-lane marking symbol shall not be displayed on Advance Intersection Lane Control signs.
- **[M]** 9B.03-07 (p.1055): Shared-use paths shall not be displayed on Advance Intersection Lane Control signs.
- **[M]** 9B.03-08 (p.1055): Advance Intersection Lane Control signs that display the bicycle lane shall use a contrasting white legend on a black background for the bicycle lane (see Figure 2B-4). The portion of the display for the bicycle lane shall not use the color green on the sign face in an attempt to be consistent with the greencolored pavement that might be present on the intersection approach.

<a id="sec-2B-29"></a>
#### Section 2B.29 Optional Movement Lane Control Signs (R3-6 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-6](symbols/R3-6.png) | **R3-6** | Optional Movement Lane Control | Mandatory (2B.29-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.69 | 6G-1 |
| ![R3-6a](symbols/R3-6a.png) | **R3-6a** | Optional Movement U and Left Turn | Mandatory (2B.29-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-6b](symbols/R3-6b.png) | **R3-6b** | Optional Movement Left Turns | Mandatory (2B.29-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.69 | — |

*Also governed by Section 2B.27:*

- **[M]** 2B.27-01 (p.91): Intersection Lane Control signs (see Figure 2B-4), if used, shall require road users in certain lanes to turn, shall permit turns from a lane where such turns would otherwise not be permitted, shall require a road user to stay in the same lane and proceed straight through an intersection, or shall indicate permitted movements from a lane.
- [S] 2B.27-02 (p.91): Intersection Lane Control signs have three applications: A. Mandatory Movement Lane Control (R3-5 series and R3-7 series) signs, B. Optional Movement Lane Control (R3-6 series) signs, and C. Advance Intersection Lane Control (R3-8 series) signs.
- **[R]** 2B.27-03 (p.92): When Intersection Lane Control signs are mounted overhead, each sign used should be placed over the lane or a projection of the lane to which it applies.
- **[R]** 2B.27-04 (p.92): On signalized approaches where through lanes that become mandatory turn lanes, multiple-lane turns that include shared lanes for through and turning movements, or other lane-use regulations are present that would be unexpected by unfamiliar road users, overhead Intersection Lane Control signs should be installed at the signalized location over the appropriate lanes or projections thereof and in advance of the intersection over the appropriate lanes.
- **[R]** 2B.27-05 (p.92): Where overhead mounting on the approach is impracticable for the Advance and/or Intersection lane Control signs, one of the following alternatives should be employed: A. At locations where through lanes become mandatory turn lanes, a Mandatory Movement Lane Control (R3-7) sign should be post-mounted on the left-hand side of the roadway where a through lane is becoming a mandatory left-turn lane on a one-way street or where a median of sufficient width for the signs is available, or on the right-hand side of the roadway where a through lane is becoming a mandatory right-turn lane. B. At locations where a through lane is becoming a mandatory left-turn lane on a two-way street where a median of sufficient width for the signs is not available, and at locations where multiple-lane turns that include shared lanes for through and turning movements are present, an Advance Intersection Lane Control (R3-8 series) sign should be post-mounted in a prominent location in advance of the intersection, and consideration should be given to the use of an oversized version in accordance with Table 2B-1.
- **[R]** 2B.27-06 (p.92): Use of an overhead sign for one approach lane should not require installation of overhead signs for the other lanes of that approach.
- [O] 2B.27-07 (p.92): Intersection Lane Control signs may be omitted where: A. A turn bay has been provided by physical construction or pavement markings, and B. Only the road users using such turn bays are permitted to make a turn in that direction.
- [O] 2B.27-08 (p.92) ◆ R3-6: At roundabouts, Intersection Lane Control (R3-5, R3-6, and R3-8 series) signs may display any of the arrow symbol options shown in Figure 2B-5.

- **[M]** 2B.29-01 (p.93): Optional Movement Lane Control (R3-6, R3-6a and R3-6b) signs (see Figure 2B-4), if used, shall be used for two or more movements from a specific lane or to emphasize permitted movements. The Optional Movement Lane Control sign shall be mounted overhead over the specific lane to which it applies.
- **[M]** 2B.29-02 (p.93): If used, the Optional Movement Lane Control signs shall indicate all permissible movements from specific lanes.
- **[M]** 2B.29-03 (p.93): Because more than one movement is permitted from the lane, the word message ONLY shall not be used on an Optional Movement Lane Control sign.
- **[M]** 2B.29-04 (p.93): Optional Movement Lane Control signs shall be used for two or more movements from a specific lane where a movement, not allowed by State statute or local ordinance, is permitted.
- **[M]** 2B.29-05 (p.93): The Optional Movement Lane Control signs shall not be used alone to effect a turn prohibition.
- **[R]** 2B.29-06 (p.93): If used, the Optional Movement Lane Control sign should be located overhead in advance of the intersection, such as near the upstream end of an adjacent mandatory movement lane, and/or overhead at the intersection where the regulation applies.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

<a id="sec-2B-31"></a>
#### Section 2B.31 RIGHT (LEFT) LANE MUST EXIT Signs (R3-33, R3-33a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-33](symbols/R3-33.png) | **R3-33** | Right (Left) Lane Must Exit | Optional (2B.31-01) | — | — | 78 x 36 | 78 x 36 | — | — | 2B-1 p.69 | — |
| ![R3-33a](symbols/R3-33a.png) | **R3-33a** | Right (Left) Lane Must Exit | Optional (2B.31-01) | — | — | 42 x 60 | 42 x 60 | — | — | 2B-1 p.69 | — |

- [O] 2B.31-01 (p.94) ◆ R3-33: A RIGHT (LEFT) LANE MUST EXIT (R3-33) sign (see Figure 2B-4) may be used to supplement an overhead EXIT ONLY guide sign to inform road users that traffic in the right-hand (left-hand) lane of a roadway that is approaching a grade-separated interchange is required to depart the roadway on the exit ramp at the next interchange.
- [O] 2B.31-02 (p.94): The R3-33a sign (see Figure 2B-4) may be used in place of the R3-33 sign where the roadside width is limited and will not accommodate the R3-33 sign.

<a id="sec-2B-32"></a>
#### Section 2B.32 Two-Way Left-Turn-Only Signs (R3-9a and R3-9b) and Plaques

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-9a](symbols/R3-9a.png) | **R3-9a** | Two-Way Left Turn Only (overhead) | Recommended (2B.32-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-9b](symbols/R3-9b.png) | **R3-9b** | Two-Way Left Turn Only | Recommended (2B.32-01) | 24 x 36 | 24 x 36 | — | — | — | 36 x 48 | 2B-1 p.69 | — |

- **[R]** 2B.32-01 (p.94): A Two-Way Left-Turn-Only (R3-9a or R3-9b) sign (see Figure 2B-6) should be used in conjunction with the required pavement markings where a non-reversible lane is reserved for the exclusive use of left-turning vehicles in either direction and is not used for passing, overtaking, or through travel.
- [O] 2B.32-02 (p.94): The post-mounted R3-9b sign may be used as an alternate to or a supplement to the overhead R3-9a sign. The legend BEGIN or END may be used within the border of the main sign itself, or on an R3-9cP or R3-9dP plaque (see Figure 2B-6) mounted immediately above it.

*Also governed by Section 2B.34:*

- [O] 2B.34-01 (p.94): A reversible lane may be used for through traffic (with left turns either permitted or prohibited) in alternating directions during different periods of the day, and the lane may be used for exclusive left turns in one or both directions during other periods of the day as well. Reversible Lane Control (R3-9e through R3-9i) signs (see Figure 2B-6) may be either static type or changeable message type. These signs may be either post-mounted or overhead. Lane-use control signals (see Chapter 4T) may also be used for reversible lanes.
- **[M]** 2B.34-02 (p.95): Where it is determined by an engineering study that lane-use control signals or physical barriers are not necessary, the lane shall be controlled by overhead Reversible Lane Control signs (see Figure 2B-7).
- **[M]** 2B.34-03 (p.95): Post-mounted Reversible Lane Control signs shall be used only as a supplement to overhead signs or signals. Post-mounted signs shall be identical in design to the overhead signs and an additional legend such as CENTER LANE shall be added to the top of the sign (R3-9f) to indicate which lane is controlled.
- [O] 2B.34-04 (p.95): Reversing traffic flow may be controlled with pavement markings and Reversible Lane Control signs (without the use of lane-use control signals), when all of the following conditions are met: A. Only one lane is being reversed, B. An engineering study indicates that the use of Reversible Lane Control signs alone would result in an acceptable level of safety and efficiency, and C. There are no unusual or complex operations in the reversible lane pattern.
- **[M]** 2B.34-05 (p.95): Reversible Lane Control signs shall contain the legend or symbols designating the allowable uses of the lane and the time periods such uses are allowed. Where symbols and legends are used, their meanings shall be as shown in Table 2B-2.
- **[M]** 2B.34-06 (p.95): Reversible Lane Control signs shall consist of a white background with a black legend and border, except for the R3-9e sign, where the color red is used for the X symbol.
- **[M]** 2B.34-07 (p.95): Symbol signs, such as the R3-9e sign, shall consist of the appropriate symbol in the upper portion of the sign with the appropriate times of the day and days of the week below it. All times of the day and days of the week shall be accounted for on the sign to eliminate confusion to the road user. Table 2B-2. Meanings of Symbols and Legends on Reversible Lane Control Signs
- **[M]** 2B.34-08 (p.97): In situations where more than one message is conveyed to the road user, such as on the R3-9e sign, the sign legend shall be arranged as follows: A. The prohibition or restriction message is the primary legend and shall be on the top for word message signs and to the far left for symbol signs, B. The permissive use message shall be displayed as the second legend, and C. The OTHER TIMES message shall be displayed at the bottom for word message signs and to the far right for symbol signs.
- [O] 2B.34-09 (p.97): The symbol signs may also include a downward-pointing arrow with the legend THIS LANE. The term OTHER TIMES may be used for either the symbol or word message sign.
- **[M]** 2B.34-10 (p.97): A Reversible Lane Control sign shall be mounted over the approximate center of the lane that is being reversed.
- **[M]** 2B.34-11 (p.97): If the vertical or horizontal alignment is curved to the degree that a driver would be unable to see at least one sign, and preferably two signs, then additional overhead signs shall be installed. The placement of the signs shall be such that the driver will have a definite indication of the lanes specifically reserved for use at any given time. Special consideration shall be given to major generators introducing traffic between the normal sign placement.
- **[M]** 2B.34-12 (p.97): Transitions at the entry to and exit from a section of roadway with reversible lanes shall include advance signs to notify or warn drivers of the boundaries of the reversible lane controls. The R3-9g or R3-9h signs (see Figure 2B-6) shall be used for this purpose.
- [O] 2B.34-13 (p.97): More than one End Reverse Lane (R3-9i) sign (see Figure 2B-6) may be used at the termination of the reversible lane to emphasize the importance of the message.
- [O] 2B.34-14 (p.97): Where longitudinal barriers separate opposing directions of traffic, the R3-9g or R3-9h signs may be omitted.
- **[M]** 2B.34-15 (p.97): Flashing beacons, if used to supplement the overhead Reversible Lane Control signs, shall comply with the applicable requirements for flashing beacons in Chapter 4S.
- **[M]** 2B.34-16 (p.97): When used in conjunction with Reversible Lane Control signs, the Turn Prohibition (R3-1 through R3-4 and R3-18) signs shall be mounted overhead and separate from the Reversible Lane Control signs. The Turn Prohibition signs shall be designed and installed in accordance with Section 2B.26.
- **[R]** 2B.34-17 (p.97): For additional emphasis, a supplemental plaque stating the distance of the prohibition, such as NEXT 1 MILE, should be added to the Turn Prohibition signs that are used in conjunction with Reversible Lane Control signs.
- **[R]** 2B.34-18 (p.97): If used, overhead signs should be located at intervals not greater than ¼ mile. The bottom of the overhead Reversible Lane Control signs should not be more than 19 feet above the pavement grade.
- **[R]** 2B.34-19 (p.97): Where more than one sign is used at the termination of a reversible lane, they should be at least 250 feet apart. Longer distances between signs are appropriate for streets with speeds over 35 mph, but the separation should not exceed 1,000 feet.
- **[R]** 2B.34-20 (p.97): Because left-turning vehicles have a significant impact on the safety and efficiency of a reversible lane operation, if a mandatory left-turn lane or two-way left-turn lane cannot be incorporated into the lane-use pattern for a particular peak or off-peak period, consideration should be given to prohibiting left turns and U-turns during that time period.
- **[R]** 2B.34-21 (p.97): Reversible Lane Control signs and parking signs should be consistent in message during the same operational periods.

<a id="sec-2B-33"></a>
#### Section 2B.33 BEGIN and END Plaques (R3-9cP and R3-9dP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-9cP](symbols/R3-9cP.png) | **R3-9cP** | Begin (plaque) | Optional (2B.33-01) | 24 x 12 | 24 x 12 | — | — | — | 36 x 18 | 2B-1 p.69 | — |
| ![R3-9dP](symbols/R3-9dP.png) | **R3-9dP** | End (plaque) | Optional (2B.33-01) | 24 x 12 | 24 x 12 | — | — | — | 36 x 18 | 2B-1 p.69 | — |

- [O] 2B.33-01 (p.94): The BEGIN (R3-9cP) or END (R3-9dP) plaque (see Figure 2B-6), mounted directly above a regulatory sign, may be used to inform road users of the location where a regulatory condition begins or ends.

*Also governed by Section 2B.34:*

- [O] 2B.34-01 (p.94): A reversible lane may be used for through traffic (with left turns either permitted or prohibited) in alternating directions during different periods of the day, and the lane may be used for exclusive left turns in one or both directions during other periods of the day as well. Reversible Lane Control (R3-9e through R3-9i) signs (see Figure 2B-6) may be either static type or changeable message type. These signs may be either post-mounted or overhead. Lane-use control signals (see Chapter 4T) may also be used for reversible lanes.
- **[M]** 2B.34-02 (p.95): Where it is determined by an engineering study that lane-use control signals or physical barriers are not necessary, the lane shall be controlled by overhead Reversible Lane Control signs (see Figure 2B-7).
- **[M]** 2B.34-03 (p.95): Post-mounted Reversible Lane Control signs shall be used only as a supplement to overhead signs or signals. Post-mounted signs shall be identical in design to the overhead signs and an additional legend such as CENTER LANE shall be added to the top of the sign (R3-9f) to indicate which lane is controlled.
- [O] 2B.34-04 (p.95): Reversing traffic flow may be controlled with pavement markings and Reversible Lane Control signs (without the use of lane-use control signals), when all of the following conditions are met: A. Only one lane is being reversed, B. An engineering study indicates that the use of Reversible Lane Control signs alone would result in an acceptable level of safety and efficiency, and C. There are no unusual or complex operations in the reversible lane pattern.
- **[M]** 2B.34-05 (p.95): Reversible Lane Control signs shall contain the legend or symbols designating the allowable uses of the lane and the time periods such uses are allowed. Where symbols and legends are used, their meanings shall be as shown in Table 2B-2.
- **[M]** 2B.34-06 (p.95): Reversible Lane Control signs shall consist of a white background with a black legend and border, except for the R3-9e sign, where the color red is used for the X symbol.
- **[M]** 2B.34-07 (p.95): Symbol signs, such as the R3-9e sign, shall consist of the appropriate symbol in the upper portion of the sign with the appropriate times of the day and days of the week below it. All times of the day and days of the week shall be accounted for on the sign to eliminate confusion to the road user. Table 2B-2. Meanings of Symbols and Legends on Reversible Lane Control Signs
- **[M]** 2B.34-08 (p.97): In situations where more than one message is conveyed to the road user, such as on the R3-9e sign, the sign legend shall be arranged as follows: A. The prohibition or restriction message is the primary legend and shall be on the top for word message signs and to the far left for symbol signs, B. The permissive use message shall be displayed as the second legend, and C. The OTHER TIMES message shall be displayed at the bottom for word message signs and to the far right for symbol signs.
- [O] 2B.34-09 (p.97): The symbol signs may also include a downward-pointing arrow with the legend THIS LANE. The term OTHER TIMES may be used for either the symbol or word message sign.
- **[M]** 2B.34-10 (p.97): A Reversible Lane Control sign shall be mounted over the approximate center of the lane that is being reversed.
- **[M]** 2B.34-11 (p.97): If the vertical or horizontal alignment is curved to the degree that a driver would be unable to see at least one sign, and preferably two signs, then additional overhead signs shall be installed. The placement of the signs shall be such that the driver will have a definite indication of the lanes specifically reserved for use at any given time. Special consideration shall be given to major generators introducing traffic between the normal sign placement.
- **[M]** 2B.34-12 (p.97): Transitions at the entry to and exit from a section of roadway with reversible lanes shall include advance signs to notify or warn drivers of the boundaries of the reversible lane controls. The R3-9g or R3-9h signs (see Figure 2B-6) shall be used for this purpose.
- [O] 2B.34-13 (p.97): More than one End Reverse Lane (R3-9i) sign (see Figure 2B-6) may be used at the termination of the reversible lane to emphasize the importance of the message.
- [O] 2B.34-14 (p.97): Where longitudinal barriers separate opposing directions of traffic, the R3-9g or R3-9h signs may be omitted.
- **[M]** 2B.34-15 (p.97): Flashing beacons, if used to supplement the overhead Reversible Lane Control signs, shall comply with the applicable requirements for flashing beacons in Chapter 4S.
- **[M]** 2B.34-16 (p.97): When used in conjunction with Reversible Lane Control signs, the Turn Prohibition (R3-1 through R3-4 and R3-18) signs shall be mounted overhead and separate from the Reversible Lane Control signs. The Turn Prohibition signs shall be designed and installed in accordance with Section 2B.26.
- **[R]** 2B.34-17 (p.97): For additional emphasis, a supplemental plaque stating the distance of the prohibition, such as NEXT 1 MILE, should be added to the Turn Prohibition signs that are used in conjunction with Reversible Lane Control signs.
- **[R]** 2B.34-18 (p.97): If used, overhead signs should be located at intervals not greater than ¼ mile. The bottom of the overhead Reversible Lane Control signs should not be more than 19 feet above the pavement grade.
- **[R]** 2B.34-19 (p.97): Where more than one sign is used at the termination of a reversible lane, they should be at least 250 feet apart. Longer distances between signs are appropriate for streets with speeds over 35 mph, but the separation should not exceed 1,000 feet.
- **[R]** 2B.34-20 (p.97): Because left-turning vehicles have a significant impact on the safety and efficiency of a reversible lane operation, if a mandatory left-turn lane or two-way left-turn lane cannot be incorporated into the lane-use pattern for a particular peak or off-peak period, consideration should be given to prohibiting left turns and U-turns during that time period.
- **[R]** 2B.34-21 (p.97): Reversible Lane Control signs and parking signs should be consistent in message during the same operational periods.

<a id="sec-2B-34"></a>
#### Section 2B.34 Reversible Lane Control Signs (R3-9e through R3-9i)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-9e](symbols/R3-9e.png) | **R3-9e** | Reversible Lane Control (overhead) | Optional (2B.34-01) | 108 x 48 | 108 x 48 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-9f](symbols/R3-9f.png) | **R3-9f** | Reversible Lane Control | Optional (2B.34-01) | 30 x 42 | 36 x 54 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-9g](symbols/R3-9g.png) | **R3-9g** | Advance Reversible Lane Control | Optional (2B.34-01) | 108 x 36 | 108 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-9h](symbols/R3-9h.png) | **R3-9h** | Advance Reversible Lane Control | Optional (2B.34-01) | 108 x 36 | 108 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-9i](symbols/R3-9i.png) | **R3-9i** | End Reverse Lane | Optional (2B.34-01) | 108 x 48 | 108 x 48 | — | — | — | — | 2B-1 p.69 | — |

- [O] 2B.34-01 (p.94): A reversible lane may be used for through traffic (with left turns either permitted or prohibited) in alternating directions during different periods of the day, and the lane may be used for exclusive left turns in one or both directions during other periods of the day as well. Reversible Lane Control (R3-9e through R3-9i) signs (see Figure 2B-6) may be either static type or changeable message type. These signs may be either post-mounted or overhead. Lane-use control signals (see Chapter 4T) may also be used for reversible lanes.
- **[M]** 2B.34-02 (p.95): Where it is determined by an engineering study that lane-use control signals or physical barriers are not necessary, the lane shall be controlled by overhead Reversible Lane Control signs (see Figure 2B-7).
- **[M]** 2B.34-03 (p.95) ◆ R3-9f: Post-mounted Reversible Lane Control signs shall be used only as a supplement to overhead signs or signals. Post-mounted signs shall be identical in design to the overhead signs and an additional legend such as CENTER LANE shall be added to the top of the sign (R3-9f) to indicate which lane is controlled.
- [O] 2B.34-04 (p.95): Reversing traffic flow may be controlled with pavement markings and Reversible Lane Control signs (without the use of lane-use control signals), when all of the following conditions are met: A. Only one lane is being reversed, B. An engineering study indicates that the use of Reversible Lane Control signs alone would result in an acceptable level of safety and efficiency, and C. There are no unusual or complex operations in the reversible lane pattern.
- **[M]** 2B.34-05 (p.95): Reversible Lane Control signs shall contain the legend or symbols designating the allowable uses of the lane and the time periods such uses are allowed. Where symbols and legends are used, their meanings shall be as shown in Table 2B-2.
- **[M]** 2B.34-06 (p.95) ◆ R3-9e: Reversible Lane Control signs shall consist of a white background with a black legend and border, except for the R3-9e sign, where the color red is used for the X symbol.
- **[M]** 2B.34-07 (p.95) ◆ R3-9e: Symbol signs, such as the R3-9e sign, shall consist of the appropriate symbol in the upper portion of the sign with the appropriate times of the day and days of the week below it. All times of the day and days of the week shall be accounted for on the sign to eliminate confusion to the road user. Table 2B-2. Meanings of Symbols and Legends on Reversible Lane Control Signs
- **[M]** 2B.34-08 (p.97) ◆ R3-9e: In situations where more than one message is conveyed to the road user, such as on the R3-9e sign, the sign legend shall be arranged as follows: A. The prohibition or restriction message is the primary legend and shall be on the top for word message signs and to the far left for symbol signs, B. The permissive use message shall be displayed as the second legend, and C. The OTHER TIMES message shall be displayed at the bottom for word message signs and to the far right for symbol signs.
- [O] 2B.34-09 (p.97): The symbol signs may also include a downward-pointing arrow with the legend THIS LANE. The term OTHER TIMES may be used for either the symbol or word message sign.
- **[M]** 2B.34-10 (p.97): A Reversible Lane Control sign shall be mounted over the approximate center of the lane that is being reversed.
- **[M]** 2B.34-11 (p.97): If the vertical or horizontal alignment is curved to the degree that a driver would be unable to see at least one sign, and preferably two signs, then additional overhead signs shall be installed. The placement of the signs shall be such that the driver will have a definite indication of the lanes specifically reserved for use at any given time. Special consideration shall be given to major generators introducing traffic between the normal sign placement.
- **[M]** 2B.34-12 (p.97) ◆ R3-9g, R3-9h: Transitions at the entry to and exit from a section of roadway with reversible lanes shall include advance signs to notify or warn drivers of the boundaries of the reversible lane controls. The R3-9g or R3-9h signs (see Figure 2B-6) shall be used for this purpose.
- [O] 2B.34-13 (p.97) ◆ R3-9i: More than one End Reverse Lane (R3-9i) sign (see Figure 2B-6) may be used at the termination of the reversible lane to emphasize the importance of the message.
- [O] 2B.34-14 (p.97) ◆ R3-9g, R3-9h: Where longitudinal barriers separate opposing directions of traffic, the R3-9g or R3-9h signs may be omitted.
- **[M]** 2B.34-15 (p.97): Flashing beacons, if used to supplement the overhead Reversible Lane Control signs, shall comply with the applicable requirements for flashing beacons in Chapter 4S.
- **[M]** 2B.34-16 (p.97): When used in conjunction with Reversible Lane Control signs, the Turn Prohibition (R3-1 through R3-4 and R3-18) signs shall be mounted overhead and separate from the Reversible Lane Control signs. The Turn Prohibition signs shall be designed and installed in accordance with Section 2B.26.
- **[R]** 2B.34-17 (p.97): For additional emphasis, a supplemental plaque stating the distance of the prohibition, such as NEXT 1 MILE, should be added to the Turn Prohibition signs that are used in conjunction with Reversible Lane Control signs.
- **[R]** 2B.34-18 (p.97): If used, overhead signs should be located at intervals not greater than ¼ mile. The bottom of the overhead Reversible Lane Control signs should not be more than 19 feet above the pavement grade.
- **[R]** 2B.34-19 (p.97): Where more than one sign is used at the termination of a reversible lane, they should be at least 250 feet apart. Longer distances between signs are appropriate for streets with speeds over 35 mph, but the separation should not exceed 1,000 feet.
- **[R]** 2B.34-20 (p.97): Because left-turning vehicles have a significant impact on the safety and efficiency of a reversible lane operation, if a mandatory left-turn lane or two-way left-turn lane cannot be incorporated into the lane-use pattern for a particular peak or off-peak period, consideration should be given to prohibiting left turns and U-turns during that time period.
- **[R]** 2B.34-21 (p.97): Reversible Lane Control signs and parking signs should be consistent in message during the same operational periods.

<a id="sec-2B-35"></a>
#### Section 2B.35 Jughandle Signs (R3-23, R3-24, R3-25, and R3-26 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-23](symbols/R3-23.png) | **R3-23** | Jughandle Signs | Mandatory (2B.35-03) | 60 x 36 | 60 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-23a](symbols/R3-23a.png) | **R3-23a** | U TURN FROM RIGHT LANE | Mandatory (2B.35-03) | 60 x 36 | 60 x 36 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-24](symbols/R3-24.png) | **R3-24** |  | Mandatory (2B.35-03) | — | — | — | — | — | — | 2B-1 p.69 | — |
| ![R3-24a](symbols/R3-24a.png) | **R3-24a** | U-Turns and Left Turns Directional | Mandatory (2B.35-05) | 60 x 24 | 60 x 24 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-24b](symbols/R3-24b.png) | **R3-24b** |  | Mandatory (2B.35-05) | — | — | — | — | — | — | 2B-1 p.69 | — |
| ![R3-25](symbols/R3-25.png) | **R3-25** |  | Mandatory (2B.35-03) | — | — | — | — | — | — | 2B-1 p.69 | — |
|  | **R3-25a** | U-Turns and Left Turns Directional | Mandatory (2B.35-05) | 60 x 24 | 60 x 24 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-25b](symbols/R3-25b.png) | **R3-25b** |  | Mandatory (2B.35-05) | — | — | — | — | — | — | 2B-1 p.69 | — |
| ![R3-26](symbols/R3-26.png) | **R3-26** | U-Turns and Left Turns Directional | Mandatory (2B.35-03) | 60 x 24 | 60 x 24 | — | — | — | — | 2B-1 p.69 | — |
| ![R3-26a](symbols/R3-26a.png) | **R3-26a** |  | Mandatory (2B.35-03) | — | — | — | — | — | — | 2B-1 p.69 | — |

- **[M]** 2B.35-03 (p.98) ◆ R3-23, R3-23a: On multi-lane roadways, since road users generally anticipate that they need to be in the left-hand lane when approaching a location where they desire to turn left or make a U-turn, an ALL TURNS FROM RIGHT LANE (R3-23) or a U TURN FROM RIGHT LANE (R3-23a) sign (see Figure 2B-8) shall be installed in advance of the location to inform drivers that left turns and/or U-turns will be made from the right-hand lane.
- [O] 2B.35-04 (p.98): Where a median of sufficient width is available, supplemental regulatory or guide signs may also be placed on the left-hand side of the roadway.
- **[M]** 2B.35-05 (p.98) ◆ R3-24, R3-24a, R3-24b, R3-25, R3-25a, R3-25b: The R3-24 series sign with an upward diagonal arrow pointing to the right if the jughandle entrance is designed as an exit ramp (see Drawings A and B in Figure 2B-9), or the R3-25 series sign with a horizontal arrow pointing to the right if the jughandle entrance is designed as an intersection, shall be installed on the right-hand side of the roadway at the entrance to the jughandle. The legend on the sign shall be ALL TURNS, U TURN, or U AND LEFT TURNS, as appropriate.
- **[M]** 2B.35-06 (p.98) ◆ R3-26, R3-26a: If the jughandle is designed such that the jughandle entrance is downstream of the location where the turn would normally have been made (see Drawing C in Figure 2B-9), the R3-26 series sign with an arrow pointing straight upward shall be installed on the right-hand side of the roadway at the intersection to inform road users that they need to proceed straight through the intersection in order to make a left turn or U-turn. The legend on the sign shall be U TURN or U AND LEFT TURNS, as appropriate.
- [S] 2B.35-07 (p.98) ◆ R3-24, R3-25, R3-26, R3-26a: The R3-24, R3-25, and R3-26 series of signs are designed to be mounted below conventional guide signs.

<a id="sec-2B-36"></a>
#### Section 2B.36 DO NOT PASS Sign (R4-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-1](symbols/R4-1.png) | **R4-1** | Do Not Pass | Optional (2B.36-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | 9A-1, 6G-1 |

- [O] 2B.36-01 (p.102): The Do Not Pass (R4-1) sign (see Figure 2B-10) may be used in addition to pavement markings (see Section 3B.03) to emphasize the restriction on passing. The Do Not Pass sign may be used at the beginning of, and at intervals within, a zone through which sight distance is restricted or where other conditions make overtaking and passing inappropriate.
- [O] 2B.36-02 (p.102): If signing is needed on the left-hand side of the roadway for additional emphasis, NO PASSING ZONE (W14-3) signs may be used (see Section 2C.53).

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 9B.24:*

- [O] 9B.24-01 (p.1064): Other regulatory signs described in Chapters 2B and 8B may be installed on bicycle facilities as appropriate.

<a id="sec-2B-37"></a>
#### Section 2B.37 PASS WITH CARE Sign (R4-2)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-2](symbols/R4-2.png) | **R4-2** | Pass With Care | Recommended (2B.37-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | 9A-1, 6G-1 |

- **[R]** 2B.37-01 (p.102): The PASS WITH CARE (R4-2) sign (see Figure 2B-10) should be installed at the downstream end of a nopassing zone if a Do Not Pass sign has been installed at the upstream end of the zone.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 9B.24:*

- [O] 9B.24-01 (p.1064): Other regulatory signs described in Chapters 2B and 8B may be installed on bicycle facilities as appropriate.

<a id="sec-2B-38"></a>
#### Section 2B.38 KEEP RIGHT EXCEPT TO PASS Sign (R4-16), SLOWER TRAFFIC KEEP RIGHT Sign (R4-3), and TRUCKS USE RIGHT LANE Sign (R4-5)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-3](symbols/R4-3.png) | **R4-3** | Slower Traffic Keep Right | Optional (2B.38-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | 9A-1 |
| ![R4-5](symbols/R4-5.png) | **R4-5** | Trucks Use Right Lane | Optional (2B.38-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.69 | — |
| ![R4-16](symbols/R4-16.png) | **R4-16** | Keep Right Except to Pass | Optional (2B.38-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.70 | 9A-1 |

- [O] 2B.38-01 (p.102) ◆ R4-16: The KEEP RIGHT EXCEPT TO PASS (R4-16) sign (see Figure 2B-10) may be used on roadways where there are two lanes in one direction of travel to direct drivers to stay in the right-hand lane except when they are passing another vehicle.
- **[R]** 2B.38-02 (p.102): If used, the KEEP RIGHT EXCEPT TO PASS sign should be installed at or just beyond the beginning of a two-lane section of roadway and at selected locations along two-lane roadways where additional emphasis is needed.
- [O] 2B.38-03 (p.102) ◆ R4-3, R4-5: The SLOWER TRAFFIC KEEP RIGHT (R4-3) or the TRUCKS USE RIGHT LANE (R4-5) sign (see Figure 2B-10) may be used on multi-lane through roadways to improve capacity or reduce unnecessary lane changing due to the presence of slower vehicles that impede the normal flow of traffic.
- **[R]** 2B.38-04 (p.102): If used, the SLOWER TRAFFIC KEEP RIGHT sign or the TRUCKS USE RIGHT LANE sign should be installed at or just beyond the beginning of a multi-lane roadway section or at the beginning of an extra lane provided for trucks and/or other slow-moving traffic, and at selected locations where there is a tendency on the part of some road users to drive in the left-hand lane(or lanes) below the normal speed of traffic. These signs should not be used on the approach to an interchange or through an interchange area where traffic is entering or exiting, or along deceleration or acceleration lanes.
- [O] 2B.38-05 (p.102): The TRUCKS USE RIGHT LANE sign may be used as a supplement to the SLOWER TRAFFIC KEEP RIGHT sign.
- **[R]** 2B.38-06 (p.102): If an extra lane has been provided for trucks and other slow-moving traffic, a Lane Ends sign (see Section 2C.47) should be installed in advance of the point where the extra lane ends. Appropriate pavement markings should be installed at both the upstream and downstream ends of the extra lane (see Section 3B.12 and Figure 3B-14).

*Also governed by Section 9B.24:*

- [O] 9B.24-01 (p.1064): Other regulatory signs described in Chapters 2B and 8B may be installed on bicycle facilities as appropriate.

<a id="sec-2B-39"></a>
#### Section 2B.39 Keep Right and Keep Left Signs (R4-7 Series and R4-8 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-7](symbols/R4-7.png) | **R4-7** | Keep Right | Optional (2B.39-01) · *Auto* | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | 9A-1, 6G-1 |
| ![R4-7a](symbols/R4-7a.png) | **R4-7a** | Keep Right | Optional (2B.39-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | — |
| ![R4-7b](symbols/R4-7b.png) | **R4-7b** | Keep Right | Optional (2B.39-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | — |
| ![R4-7c](symbols/R4-7c.png) | **R4-7c** | Narrow Keep Right | Optional (2B.39-01) | 18 x 30 | 18 x 30 | — | — | — | — | 2B-1 p.69 | 6G-1 |
| ![R4-8](symbols/R4-8.png) | **R4-8** | Keep Left | Optional (2B.39-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | — |
| ![R4-8a](symbols/R4-8a.png) | **R4-8a** | Keep Left | Optional (2B.39-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | — |
| ![R4-8b](symbols/R4-8b.png) | **R4-8b** | Keep Left | Optional (2B.39-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | — |
| ![R4-8c](symbols/R4-8c.png) | **R4-8c** | Narrow Keep Left | Optional (2B.39-01) | 18 x 30 | 18 x 30 | — | — | — | — | 2B-1 p.69 | — |

- [O] 2B.39-01 (p.102) ◆ R4-7, R4-8: The Keep Right (R4-7) sign (see Figure 2B-10) may be used at locations where it is necessary for traffic to pass only to the right-hand side of a roadway feature or obstruction. The Keep Left (R4-8) sign (see Figure 2B-10) may be used at locations where it is necessary for traffic to pass only to the left-hand side of a roadway feature or obstruction.
- **[R]** 2B.39-02 (p.104): At locations where it is not readily apparent that traffic is required to keep to the right, a Keep Right sign should be used.
- **[M]** 2B.39-03 (p.104): If Keep Right signs are installed at the start of a median or at a median opening, they shall be placed as close as practicable to the approach ends of the medians, and shall be visible to traffic on the divided highway and angled toward the applicable crossroad approach as shown in Figure 2B-20.
- **[R]** 2B.39-04 (p.104): If used, the Keep Right sign should be mounted on the face of or just in front of a pier or other obstruction separating opposite directions of traffic in the center of the highway such that traffic will have to pass to the right-hand side of the sign.
- **[R]** 2B.39-05 (p.104) ◆ R4-7, R4-7a, R4-7b, R4-8, R4-8a, R4-8b: Where the approach end of the island channelizes traffic away from the approach direction, the word legend (R4-7a, R4-7b, R4-8a, or R4-8b) signs (see Figure 2B-10) should be used instead of the symbol (R4-7 or R4-8) signs to emphasize the degree of curvature away from the approach direction (see Figure 2B-11).
- **[R]** 2B.39-06 (p.104) ◆ R4-7b: Where a regulatory sign is used within the central island of a neighborhood traffic circle to direct traffic counter-clockwise around the central island, the Keep Right with diagonal arrow (R4-7b) sign should be used (see Figure 2B-24). The mounting height of the sign should be at least 4 feet, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way.
- **[M]** 2B.39-07 (p.104): The Keep Right (Left) sign shall not be installed on the right-hand (left-hand) side of the roadway in a position where traffic must pass to the left-hand (right-hand) side of the sign.
- [O] 2B.39-08 (p.104): The Keep Right sign may be omitted at intermediate ends of divisional islands and medians.
- [O] 2B.39-09 (p.104) ◆ R4-7, R4-7a, R4-7b, R4-8: Word message KEEP RIGHT (LEFT) with an arrow (R4-7a or R4-7b) signs (see Figure 2B-10) may be used instead of the R4-7 or R4-8 symbol signs.
- [O] 2B.39-10 (p.104) ◆ R4-7c: A narrow Keep Right (R4-7c) sign (see Figure 2B-10) may be installed on the approach end of a median island that is less than 4 feet wide at the point where the sign is to be located.
- **[M]** 2B.39-11 (p.104) ◆ R4-7c: A narrow Keep Right (R4-7c) sign shall not be installed on a median island that has a width of 4 feet or more at the point where the sign is to be located.
- [O] 2B.39-12 (p.104): The Keep Right sign may be installed in the median of a divided highway crossing that functions as a single intersection such that it is visible to traffic on the divided highway and angled as needed toward the applicable crossroad approach as shown in Figure 2B-20.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 9B.24:*

- [O] 9B.24-01 (p.1064): Other regulatory signs described in Chapters 2B and 8B may be installed on bicycle facilities as appropriate.

<a id="sec-2B-40"></a>
#### Section 2B.40 STAY IN LANE Sign (R4-9)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-9](symbols/R4-9.png) | **R4-9** | Stay in Lane | Optional (2B.40-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.69 | 6G-1 |

- [O] 2B.40-01 (p.104): A STAY IN LANE (R4-9) sign (see Figure 2B-10) may be used on multi-lane highways to direct road users to stay in their lane until conditions permit shifting to another lane.
- **[R]** 2B.40-02 (p.104): If a STAY IN LANE sign is used, it should be accompanied by a solid double white lane line(s) to prohibit lane changing.

*Also governed by Section 6G.07:*

- [O] 6G.07-01 (p.795): A STAY IN LANE (R4-9) sign (see Figure 6G-1) may be used where a multi-lane shift has been incorporated as part of the TTC on a highway to direct road users around road work that occupies part of the roadway on a multi-lane highway.
- **[R]** 6G.07-02 (p.795): A STAY IN LANE TO MERGE POINT (R4-9a) sign (see Figure 6G-1) should be used during late merge operations (see Section 6N.19) to direct traffic to use all available lanes until the merge point is reached.

<a id="sec-2B-41"></a>
#### Section 2B.41 RUNAWAY VEHICLES ONLY Sign (R4-10)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-10](symbols/R4-10.png) | **R4-10** | Runaway Vehicles Only | Recommended (2B.41-01) | 48 x 48 | 48 x 48 | — | — | — | — | 2B-1 p.69 | — |

- **[R]** 2B.41-01 (p.104): A RUNAWAY VEHICLES ONLY (R4-10) sign (see Figure 2B-10) should be installed near a truck escape (or runaway truck) ramp entrance to discourage other road users from entering the ramp.

<a id="sec-2B-42"></a>
#### Section 2B.42 Slow Vehicle Turn-Out Signs (R4-12, R4-13, and R4-14)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-12](symbols/R4-12.png) | **R4-12** | More Following Vehicles Must | Optional (2B.42-02) | 42 x 24 | 42 x 24 | — | — | — | 72 x 42 | 2B-1 p.70 | — |
| ![R4-13](symbols/R4-13.png) | **R4-13** | Slow Vehicles Must Use | Optional (2B.42-02) | 42 x 24 | 42 x 24 | — | — | — | — | 2B-1 p.70 | — |
| ![R4-14](symbols/R4-14.png) | **R4-14** | Slow Vehicles Must Turn Out | Optional (2B.42-02) | 30 x 42 | 30 x 42 | — | — | — | — | 2B-1 p.70 | — |

- [O] 2B.42-02 (p.106) ◆ R4-12: A SLOW VEHICLES WITH XX OR MORE FOLLOWING VEHICLES MUST USE TURN-OUT (R4-12) sign (see Figure 2B-10) may be installed in advance of a turn-out area to inform drivers who are driving so slow that they have accumulated a specific number of vehicles behind them that they are required by the traffic laws of that State to use the turn-out to allow the vehicles following them to pass.
- [S] 2B.42-03 (p.106) ◆ R4-12: The specific number of vehicles displayed on the R4-12 sign provides law enforcement personnel with the information they need to enforce this regulation.
- [O] 2B.42-04 (p.106) ◆ R4-12, R4-13: If an R4-12 sign has been installed in advance of a turn-out area, a SLOW VEHICLES MUST USE TURNOUT AHEAD (R4-13) sign (see Figure 2B-10) may also be installed downstream from the R4-12 sign, but upstream from the turn-out area, to remind slow drivers that they are required to use a turn-out that is a short distance ahead.
- **[M]** 2B.42-05 (p.106) ◆ R4-12, R4-14: If an R4-12 sign has been installed in advance of a turn-out area, a SLOW VEHICLES MUST TURN OUT (with arrow) (R4-14) sign (see Figure 2B-10) shall be installed at the entry point of the turn-out area.

<a id="sec-2B-43"></a>
#### Section 2B.43 DO NOT DRIVE ON SHOULDER Sign (R4-17) and DO NOT PASS ON SHOULDER Sign (R4-18)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-17](symbols/R4-17.png) | **R4-17** | Do Not Drive on Shoulder | Optional (2B.43-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.70 | — |
| ![R4-18](symbols/R4-18.png) | **R4-18** | Do Not Pass on Shoulder | Optional (2B.43-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.70 | — |

- [O] 2B.43-01 (p.106) ◆ R4-17: The DO NOT DRIVE ON SHOULDER (R4-17) sign (see Figure 2B-10) may be installed to inform road users that using the shoulder of a roadway as a travel lane is prohibited.
- [O] 2B.43-02 (p.106) ◆ R4-18: The DO NOT PASS ON SHOULDER (R4-18) sign (see Figure 2B-10) may be installed to inform road users that using the shoulder of a roadway to pass other vehicles is prohibited.

<a id="sec-2B-44"></a>
#### Section 2B.44 ALL TRAFFIC Sign (R4-20) and RIGHT (LEFT) TURN ONLY Sign (R4-21)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R4-20](symbols/R4-20.png) | **R4-20** | All Traffic | Optional (2B.44-01) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.70 | — |
| ![R4-21](symbols/R4-21.png) | **R4-21** | Right (Left) Turn Only | Optional (2B.44-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2B-1 p.70 | — |

- [O] 2B.44-01 (p.106) ◆ R4-20: The ALL TRAFFIC (R4-20) sign may be used at an intersection where all traffic on the approach to the intersection must turn in the direction indicated and the Movement Prohibition (see Section 2B.26) and/or ONE WAY (see Section 2B.49) signs do not adequately convey the allowable direction of travel.
- [O] 2B.44-02 (p.106) ◆ R4-21: The RIGHT (LEFT) TURN ONLY (R4-21) sign may be used at or on an approach to an intersection where all traffic on that approach must turn in the direction indicated.
- **[R]** 2B.44-03 (p.106): The RIGHT (LEFT) TURN ONLY sign should not be used for a channelized turn lane separated from the adjacent travel lanes by an island.
- **[M]** 2B.44-04 (p.106): The ALL TRAFFIC sign shall not be used to substitute for the Keep Right (R4-7 series) or Keep Left (R4-8 series) signs.
- **[M]** 2B.44-05 (p.106): The RIGHT (LEFT) TURN ONLY sign shall not be used to substitute for the Mandatory Movement Lane Control signs (see Sections 2B.27 and 2B.28).

<a id="sec-2B-45"></a>
#### Section 2B.45 Selective Exclusion Signs and Plaques

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R5-2](symbols/R5-2.png) | **R5-2** | No Trucks | Optional | 24 x 24 | 24 x 24 | 30 x 30 | 36 x 36 | — | 36 x 36 | 2B-1 p.70 | — |
| ![R5-2aP](symbols/R5-2aP.png) | **R5-2aP** | Except Local Deliveries (plaque) | Optional | 24 x 12 | 24 x 12 | 30 x 15 | 36 x 18 | — | 36 x 18 | 2B-1 p.70 | — |
| ![R5-2b](symbols/R5-2b.png) | **R5-2b** | No Thru Trucks | Optional (2B.45-09) | 24 x 30 | 24 x 30 | 30 x 36 | 36 x 48 | — | 36 x 48 | 2B-1 p.70 | — |
| ![R5-3](symbols/R5-3.png) | **R5-3** | No Motor Vehicles | Optional (9B.07-01) | 24 x 24 | 24 x 24 | — | — | 24 x 24 | — | 2B-1 p.70 | 9A-1 |
| ![R5-4](symbols/R5-4.png) | **R5-4** | No Commercial Vehicles | Optional | 24 x 30 | 24 x 30 | 36 x 48 | 36 x 48 | — | — | 2B-1 p.70 | — |
| ![R5-5](symbols/R5-5.png) | **R5-5** | No Vehicles with Lugs | Optional | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | — | 2B-1 p.70 | — |
| ![R5-6](symbols/R5-6.png) | **R5-6** | No Bicycles | Optional | 24 x 24 | 24 x 24 | 30 x 30 | 36 x 36 | 24 x 24* | 48 x 48 | 2B-1 p.70 | 9A-1 |
| ![R5-7](symbols/R5-7.png) | **R5-7** | No Non-Motorized Traffic | Optional | 30 x 24 | 30 x 24 | 42 x 24 | 48 x 30 | — | 42 x 24 | 2B-1 p.70 | — |
| ![R5-8](symbols/R5-8.png) | **R5-8** | No Motor-Driven Cycles | Optional (2B.45-01) | 30 x 24 | 30 x 24 | 42 x 24 | 48 x 30 | — | 42 x 24 | 2B-1 p.70 | — |
| ![R5-10](symbols/R5-10.png) | **R5-10** | No Pedestrians, Bicycles, | Optional (2B.45-04) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.70 | — |
| ![R5-10a](symbols/R5-10a.png) | **R5-10a** | No Pedestrians, Bicycles, | Optional (2B.45-04) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.70 | — |
| ![R5-10b](symbols/R5-10b.png) | **R5-10b** | No Pedestrians or Bicycles | Optional (2B.45-04) | 30 x 18 | 30 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R5-10c](symbols/R5-10c.png) | **R5-10c** | No Pedestrians | Recommended (2B.45-07) | 24 x 12 | 24 x 12 | — | — | — | — | 2B-1 p.70 | — |
| ![R5-11](symbols/R5-11.png) | **R5-11** | Authorized Vehicles Only | Optional (2B.45-12) | 30 x 24 | 30 x 24 | — | — | — | — | 2B-1 p.70 | — |
| ![R5-12](symbols/R5-12.png) | **R5-12** | No Thru Traffic | Optional (2B.45-09) | 24 x 30 | 24 x 30 | — | — | — | 30 x 36 | 2B-1 p.70 | — |
| ![R9-13](symbols/R9-13.png) | **R9-13** | No Skaters | Optional (2B.45-01) | 18 x 18 | 18 x 18 | 24 x 24 | 30 x 30 | — | 30 x 30 | 2B-1 p.72 | 9A-1 |
| ![R9-14](symbols/R9-14.png) | **R9-14** | No Equestrians | Optional (2B.45-01) | 18 x 18 | 18 x 18 | 24 x 24 | 30 x 30 | — | 30 x 30 | 2B-1 p.72 | 9A-1 |
| ![R9-15](symbols/R9-15.png) | **R9-15** | No Snowmobiles | Optional (2B.45-01) | 18 x 18 | 18 x 18 | 24 x 24 | 30 x 30 | — | 30 x 30 | 2B-1 p.72 | 9A-1 |
| ![R9-16](symbols/R9-16.png) | **R9-16** | No All-Terrian Vehicles | Optional (2B.45-01) | 18 x 18 | 18 x 18 | 24 x 24 | 30 x 30 | — | 30 x 30 | 2B-1 p.72 | 9A-1 |
| ![R9-19P](symbols/R9-19P.png) | **R9-19P** | Except on Shoulder (plaque) | Optional (2B.45-11) | 18 x 12 | 18 x 12 | 24 x 18 | 30 x 24 | — | 30 x 24 | 2B-1 p.72 | — |

- [O] 2B.45-01 (p.107): Selective Exclusion signs (see Figure 2B-12) may be used to provide notice to road users that State or local statutes or ordinances exclude designated types of traffic from using particular roadways or facilities.
- **[M]** 2B.45-02 (p.107): Selective Exclusion signs shall clearly indicate the type of traffic that is excluded.
- [S] 2B.45-03 (p.107) ◆ R5-2, R5-3, R5-4, R5-5, R5-6, R5-7: Typical exclusion messages include: A. No Trucks (R5-2), B. NO MOTOR VEHICLES (R5-3), C. NO COMMERCIAL VEHICLES (R5-4), D. NO VEHICLES WITH LUGS (R5-5), E. No Bicycles (R5-6), F. NO NON-MOTORIZED TRAFFIC (R5-7),
- [O] 2B.45-04 (p.108) ◆ R5-10, R5-10a, R5-10b: Appropriate combinations or groupings of these legends into a single sign, such as NO PEDESTRIANS BICYCLES MOTOR-DRIVEN CYCLES (R5-10 and R5-10a) or NO PEDESTRIANS OR BICYCLES (R5-10b), may be used.
- **[R]** 2B.45-05 (p.108): If an exclusion is governed by vehicle weight, a Weight Limit sign (see Section 2B.64) should be used instead of a Selective Exclusion sign.
- **[R]** 2B.45-06 (p.108) ◆ R5-10b: If used on a ramp to a freeway or expressway where pedestrian and bicyclist travel are prohibited by law or regulation, the NO PEDESTRIANS OR BICYCLES (R5-10b) sign should be installed in a location where it is clearly visible to any pedestrian or bicyclist attempting to enter the limited access facility from a street intersecting the ramp. In locations where a freeway or expressway is accessed from a ramp from a roadway parallel to the freeway or expressway, the sign should be placed in a location that clearly indicates the prohibition applies only to the freeway or expressway or to the ramp.
- **[R]** 2B.45-07 (p.108) ◆ R5-10c: The Selective Exclusion sign should be placed on the right-hand side of the roadway at an appropriate distance from the intersection so as to be clearly visible to all road users turning into the roadway that has the exclusion. The NO PEDESTRIANS (R5-10c) or No Pedestrian Crossing (R9-3) sign (see Section 2B.57) should be installed so as to be clearly visible to pedestrians who are at a location where an alternative route is available.
- [O] 2B.45-08 (p.108) ◆ R5-10c: The NO PEDESTRIANS (R5-10c) or No Pedestrian Crossing (R9-3) sign may also be used at underpasses or elsewhere where pedestrian facilities are not provided.
- [O] 2B.45-09 (p.108) ◆ R5-2b, R5-12: The NO THRU TRAFFIC (R5-12) or NO THRU TRUCKS (R5-2b) signs may be used at locations to prohibit through traffic from using a particular roadway or facility.
- [O] 2B.45-10 (p.108) ◆ R5-2, R5-2aP, R5-2b: The EXCEPT LOCAL DELIVERY (R5-2aP) plaque may be mounted below the R5-2 or R5-2b sign.
- [O] 2B.45-11 (p.108) ◆ R9-19P: The EXCEPT ON SHOULDER (R9-19P) plaque may be used where such modes are allowed on a shoulder but not on the traveled way and placed at intersections with other roads and established paths or trails, where such vehicles or modes are expected to enter the highway.
- [O] 2B.45-12 (p.108) ◆ R5-11: The AUTHORIZED VEHICLES ONLY (R5-11) sign may be used at median openings and other locations to prohibit vehicles from using the median opening or facility unless they have special permission (such as law enforcement vehicles or emergency vehicles) or are performing official business (such as highway agency vehicles).

*Also governed by Section 9B.07:*

- [O] 9B.07-01 (p.1056) ◆ R5-3: The NO MOTOR VEHICLES (R5-3) sign (see Figure 9B-1) may be installed at the entrance to a shared-use path.

*Also governed by Section 9B.08:*

- [S] 9B.08-02 (p.1056) ◆ R5-6, R9-13, R9-14, R9-15, R9-16: Typical exclusion messages include: A. No Bicycles (R5-6); B. No Pedestrians (R9-3); C. No Skaters (R9-13); D. No Equestrians (R9-14); E. No Snowmobiles (R9-15); and F. No All-Terrain Vehicles (R9-16).

<a id="sec-2B-46"></a>
#### Section 2B.46 DO NOT ENTER Sign (R5-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R5-1](symbols/R5-1.png) | **R5-1** | Do Not Enter | Mandatory (2B.46-01) · *Auto* | 30 x 30 | 36 x 36 | 36 x 36 | 48 x 48 | — | 36 x 36 | 2B-1 p.70 | 6G-1 |

- **[M]** 2B.46-01 (p.109): The DO NOT ENTER (R5-1) sign (see Figure 2B-13) shall be used at the following locations: A. Where a two-way roadway becomes a one-way roadway (see Figure 2B-18); B. The intersection of an interchange exit ramp with a crossroad as specified in Section 2B.48 (see Figure 2B-15); C. The intersection of a channelized or turning roadway with a two-way undivided crossroad; and D. Except as provided in Paragraph 4 of this Section, an intersection with a divided highway where the crossing functions as two separate intersections (see Figure 2B-14).
- **[R]** 2B.46-02 (p.109): A DO NOT ENTER sign should be installed at other locations where additional emphasis is needed where wrong-way movements are prominent or where the intersecting angle of roadways is such that the visibility of ONE WAY signs alone does not sufficiently convey the restriction.
- [O] 2B.46-03 (p.109): A DO NOT ENTER sign may be installed at an intersection with a divided highway where the crossing functions as a single intersection as shown in Figure 2B-20.
- [O] 2B.46-04 (p.109): A DO NOT ENTER sign may be omitted on a low-speed urban street that is a divided highway at a crossing that functions as two separate intersections.
- [O] 2B.46-05 (p.109): An EXCEPT BICYCLES (R3-7bP) plaque (see Figure 2B-4) may be used with a DO NOT ENTER sign when counter-flow bicycle traffic is allowed.
- **[R]** 2B.46-06 (p.109): The DO NOT ENTER sign, if used, should be placed directly in view of a road user at the point where a road user could wrongly enter a divided highway, one-way roadway, or ramp. The sign should be mounted facing traffic that might enter the roadway or ramp in the wrong direction.
- **[R]** 2B.46-07 (p.109): At a crossing with a divided highway that functions as a single intersection; the sign, if used, should be placed on the outside edge side of the roadway facing traffic that might enter the roadway in the wrong direction.
- **[R]** 2B.46-08 (p.109): If the DO NOT ENTER sign would be visible to traffic to which it does not apply, the sign should be turned away from, or shielded from, the view of that traffic.
- [O] 2B.46-09 (p.109): A second DO NOT ENTER sign may be used, particularly where traffic approaches from an intersecting roadway (see Figure 2B-14).

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

<a id="sec-2B-47"></a>
#### Section 2B.47 WRONG WAY Sign (R5-1a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R5-1a](symbols/R5-1a.png) | **R5-1a** | Wrong Way | Optional (2B.47-01) | 36 x 24 | 42 x 30 | 36 x 24 | 42 x 30 | 30 x 18 | 42 x 30 | 2B-1 p.70 | 6G-1 |

- [O] 2B.47-01 (p.110): The WRONG WAY (R5-1a) sign (see Figure 2B-13) may be used as a supplement to the DO NOT ENTER sign where a crossroad intersects a one-way roadway in a manner that does not physically discourage or prevent wrong-way entry (see Figures 2B-14 and 2B-20).
- **[R]** 2B.47-02 (p.110): If used, the WRONG WAY sign should be placed at a location along the one-way roadway farther from the crossroad than the DO NOT ENTER sign (see Section 2B.46).
- **[R]** 2B.47-03 (p.110): The WRONG WAY sign should be placed on the same side of the road as the DO NOT ENTER sign. Sect. 2B.46 to 2B.47

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

<a id="sec-2B-49"></a>
#### Section 2B.49 ONE WAY Signs (R6-1 and R6-2)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R6-1](symbols/R6-1.png) | **R6-1** | One Way | Mandatory (2B.49-01) · *Auto* | 36 x 12 | 48 x 18 | 48 x 18 | 48 x 18 | — | 72 x 24 | 2B-1 p.70 | 6G-1 |
| ![R6-2](symbols/R6-2.png) | **R6-2** | One Way | Mandatory (2B.49-01) | 24 x 30 | 30 x 36 | 36 x 48 | 48 x 60 | 18 x 24 | 36 x 48 | 2B-1 p.70 | 6G-1 |
| ![R6-6](symbols/R6-6.png) | **R6-6** | Begin One Way | Optional (2B.49-14) | 24 x 30 | 30 x 36 | — | — | — | — | 2B-1 p.70 | — |
| ![R6-7](symbols/R6-7.png) | **R6-7** | End One Way | Optional (2B.49-14) | 24 x 30 | 30 x 36 | — | — | — | — | 2B-1 p.70 | — |

- **[M]** 2B.49-01 (p.114) ◆ R6-1, R6-2: Except as provided in Paragraph 6 of this Section, the ONE WAY (R6-1 or R6-2) sign (see Figure 2B-13) shall be used to indicate streets or roadways upon which vehicular traffic is allowed to travel in one direction only.
- **[M]** 2B.49-02 (p.114): ONE WAY signs shall be placed parallel to the one-way street at all alleys and roadways that intersect one-way roadways as shown in Figure 2B-18.
- **[M]** 2B.49-03 (p.114): At the crossing of a roadway with a divided highway that functions as two separate intersections, ONE WAY signs shall be placed, visible to each crossroad approach, on the near right and far left corners of each intersection with the directional roadways (see Figure 2B-19).
- **[M]** 2B.49-04 (p.114): At the crossing of a roadway with a divided highway that functions as a single intersection Keep Right (R4-7) signs (see Section 2B.39) and/or ONE WAY signs shall be installed (see Figure 2B-20). If Keep Right signs are installed, they shall be placed as close as practicable to the approach ends of the medians and shall be visible to traffic on the divided highway and angled (as needed) toward the applicable crossroad approach as shown in Figure 2B-20. If ONE WAY signs are installed, they shall be placed on the near right and far left corners of the intersection and shall be visible to each crossroad approach.
- [O] 2B.49-05 (p.114): At the crossing of a roadway with a divided highway, regardless of function as a single or separate intersections, ONE WAY signs may also be placed on the far right corner of the intersection as shown in Figures 2B-19 and 2B-20.
- [O] 2B.49-06 (p.114): ONE WAY signs may be omitted on the one-way roadways of divided highways, where the design of interchanges indicates the direction of traffic on the separate roadways.
- [O] 2B.49-07 (p.114): An EXCEPT BICYCLES (R3-7bP) plaque (see Figure 2B-4) may be used with a ONE WAY sign when counter-flow bicycle traffic is allowed.
- **[M]** 2B.49-09 (p.114): If used at unsignalized intersections with one-way streets, ONE WAY signs shall be placed on the near right and the far left corners of the intersection facing traffic entering or crossing the one-way street (see Figure 2B-18).
- **[M]** 2B.49-10 (p.114): If used at signalized intersections with one-way streets, ONE WAY signs shall be placed near the appropriate signal faces, on the poles holding the traffic signals, on the mast arm or span wire holding the signals, or at the locations specified for unsignalized intersections.
- **[M]** 2B.49-11 (p.114): At unsignalized T-intersections where the roadway at the top of the T-intersection is a one-way roadway, ONE WAY signs shall be placed on the near-right and the far side of the intersection facing traffic on the stem approach (see Figure 2B-18).
- [O] 2B.49-12 (p.114): Where the central island of a roundabout allows for the installation of signs, ONE WAY signs may be used to direct traffic counter-clockwise around the central island (see Figures 2B-22 and 2B-23).
- **[R]** 2B.49-13 (p.114): Where used on the central island of a roundabout, the mounting height of a ONE WAY sign should be at least 4 feet, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way.
- [O] 2B.49-14 (p.114) ◆ R6-6, R6-7: The BEGIN ONE WAY (R6-6) sign (see Figure 2B-13) may be used to notify road users of the beginning point of a one direction of travel restriction on the street or roadway. The END ONE WAY (R6-7) sign (see Figure 2B-13) may be used to notify road users of the ending point of a one direction of travel restriction on the street or roadway. Sect. 2B.48 to 2B.49

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

<a id="sec-2B-50"></a>
#### Section 2B.50 Divided Highway Crossing Signs (R6-3 and R6-3a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R6-3](symbols/R6-3.png) | **R6-3** | Divided Highway Crossing | Mandatory (2B.50-01) | 30 x 24 | 30 x 24 | 36 x 30 | — | — | 36 x 30 | 2B-1 p.70 | — |
| ![R6-3a](symbols/R6-3a.png) | **R6-3a** | Divided Highway Crossing | Mandatory (2B.50-01) | 30 x 24 | 30 x 24 | 36 x 30 | — | — | 36 x 30 | 2B-1 p.70 | — |

- **[M]** 2B.50-01 (p.116): On unsignalized minor-street approaches from which both left turns and right turns are permitted onto a divided highway at a crossing that functions as two separate intersections (see Section 2A.23), except as provided in Paragraph 2 of this Section, a Divided Highway Crossing (R6-3 or R6-3a) sign (see Figure 2B-13) shall be used to advise road users that they are approaching an intersection with a divided highway (see Figure 2B-19).
- [O] 2B.50-02 (p.116): If the divided highway has a traffic volume of less than 400 AADT and a speed limit of 25 mph or less, at a crossing that functions as two separate intersections, the Divided Highway Crossing signs facing the unsignalized minor-street approaches may be omitted.
- [O] 2B.50-03 (p.116): A Divided Highway Crossing sign may be used on signalized minor-street approaches from which both left turns and right turns are permitted onto a divided highway to advise road users that they are approaching an intersection with a divided highway.
- **[M]** 2B.50-04 (p.117): If a Divided Highway Crossing sign is used at a four-leg intersection, the R6-3 sign shall be used. If used at a T-intersection, the R6-3a sign shall be used.
- **[M]** 2B.50-05 (p.117): The Divided Highway Crossing sign shall be located on the near right corner of the intersection, mounted beneath a STOP or YIELD sign or on a separate support.
- [O] 2B.50-06 (p.117): An additional Divided Highway Crossing sign may be installed on the left-hand side of the approach to supplement the Divided Highway Crossing sign on the near right corner of the intersection. December 2023

<a id="sec-2B-51"></a>
#### Section 2B.51 Roundabout Circulation Plaque (R6-5P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R6-5P](symbols/R6-5P.png) | **R6-5P** | Roundabout Circulation (plaque) | Optional (2B.51-05) | 30 x 30 | 30 x 30 | — | — | — | — | 2B-1 p.70 | — |

- **[R]** 2B.51-01 (p.118): Where the central island of a roundabout or neighborhood traffic circle does not provide a reasonable place to install a sign as provided elsewhere in this Chapter, Roundabout Circulation (R6-5P) plaques (see Figure 2B-13) should be placed below the YIELD signs on each approach.
- [O] 2B.51-04 (p.118): At roundabouts where ONE WAY signs have been installed in the central island, Roundabout Circulation plaques may be placed below the YIELD signs on approaches to roundabouts to supplement the central island signs.
- [O] 2B.51-05 (p.118): The Roundabout Circulation plaque may be used at any type of circular intersection.

<a id="sec-2B-52"></a>
#### Section 2B.52 Parking, Standing, and Stopping Signs (R7 and R8 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R7-1](symbols/R7-1.png) | **R7-1** | Parking Prohibition | Recommended (2B.53-18) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-2](symbols/R7-2.png) | **R7-2** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-2a](symbols/R7-2a.png) | **R7-2a** | Parking Restrictions | Optional (2B.53-23) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-3](symbols/R7-3.png) | **R7-3** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-4](symbols/R7-4.png) | **R7-4** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-4a](symbols/R7-4a.png) | **R7-4a** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-5](symbols/R7-5.png) | **R7-5** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-6](symbols/R7-6.png) | **R7-6** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-8](symbols/R7-8.png) | **R7-8** | Accessible Parking | Mandatory (2B.53-16) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-8aP](symbols/R7-8aP.png) | **R7-8aP** | Van Accessible (plaque) | Optional | 12 x 6 | 12 x 6 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-10](symbols/R7-10.png) | **R7-10** | Back-In Parking Sign | Optional (9B.10-01) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | 9A-1 |
| ![R7-21](symbols/R7-21.png) | **R7-21** | Metered Parking | Recommended (2B.53-12) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
|  | **R7-21aP** | Mobile Parking Payment (plaque) | Optional (2B.53-13) | 12 x 6 | 12 x 6 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-22](symbols/R7-22.png) | **R7-22** | Metered Parking | Recommended (2B.53-12) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-107](symbols/R7-107.png) | **R7-107** | Parking Restrictions | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-107a](symbols/R7-107a.png) | **R7-107a** | No Parking Bus Stop | Optional | 12 x 24 | 12 x 24 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-108](symbols/R7-108.png) | **R7-108** | Permissive Parking | Optional (2B.53-21) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-111](symbols/R7-111.png) | **R7-111** | No Parking Except Electric Vehicles | Recommended (2B.53-18) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-112](symbols/R7-112.png) | **R7-112** | Electric Vehicle Parking (time limit) | Recommended (2B.53-18) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-113](symbols/R7-113.png) | **R7-113** | No Parking Except While Charging | Recommended (2B.53-18) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-113aP](symbols/R7-113aP.png) | **R7-113aP** | Vehicle Must Be Plugged In (plaque) | Recommended (2B.53-20) | 12 x 6 | 12 x 6 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-114](symbols/R7-114.png) | **R7-114** | Vehicle Charging Only (time limit) | Recommended (2B.53-19) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-201P](symbols/R7-201P.png) | **R7-201P** | Tow Away Zone (plaque) | Optional | 12 x 6 | 12 x 6 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-201aP](symbols/R7-201aP.png) | **R7-201aP** | Parking, Standing, and Stopping Signs (R7 and R8 Series) | Optional | — | — | — | — | — | — | text | — |
| ![R7-202P](symbols/R7-202P.png) | **R7-202P** | This Side of Sign (plaque) | Recommended (2B.54-05) | 12 x 6 | 12 x 6 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-203](symbols/R7-203.png) | **R7-203** | Snow Emergency Route | Recommended (2B.53-11) | 18 x 24 | 18 x 24 | — | — | — | 24 x 30 | 2B-1 p.71 | — |
| ![R8-1](symbols/R8-1.png) | **R8-1** | No Parking on Pavement | Optional (2B.53-10) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.71 | — |
| ![R8-2](symbols/R8-2.png) | **R8-2** | No Parking Except on Shoulder | Optional (2B.53-10) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.71 | — |
| ![R8-3](symbols/R8-3.png) | **R8-3** | No Parking (symbol) | Optional (2B.53-10) | 24 x 24 | 30 x 30 | 36 x 36 | 48 x 48 | 12 x 12 | 36 x 36 | 2B-1 p.71 | 6G-1 |
| ![R8-3a](symbols/R8-3a.png) | **R8-3a** | No Parking | Optional (2B.53-10) | 24 x 30 | 24 x 30 | 36 x 36 | 48 x 48 | 18 x 24 | 36 x 36 | 2B-1 p.71 | — |
| ![R8-3c](symbols/R8-3c.png) | **R8-3c** | On Pavement | Optional (2B.53-10) | 24 x 36 | 24 x 36 | — | — | 18 x 30 | 36 x 54 | 2B-1 p.71 | — |
| ![R8-3d](symbols/R8-3d.png) | **R8-3d** | On Bridge | Optional (2B.53-10) | 24 x 36 | 24 x 36 | — | — | 18 x 30 | 36 x 54 | 2B-1 p.71 | — |
| ![R8-3e](symbols/R8-3e.png) | **R8-3e** | On Tracks | Optional (2B.53-10) | 24 x 36 | 24 x 36 | — | — | 18 x 30 | — | 2B-1 p.71 | — |
| ![R8-3f](symbols/R8-3f.png) | **R8-3f** | Except on Shoulder | Optional (2B.53-10) | 24 x 36 | 24 x 36 | — | — | 18 x 30 | 36 x 54 | 2B-1 p.71 | — |

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

*Also governed by Section 2B.53:*

- **[M]** 2B.53-01 (p.123): Parking, standing, or stopping signs (see Figure 2B-25) shall be rectangular or square.
- **[M]** 2B.53-02 (p.123): Public agencies shall follow established law (State law, local ordinance, or regulation) as adopted by the authorized agency regarding what messages are allowed on parking signs.
- **[M]** 2B.53-03 (p.123): The legend on parking signs shall state applicable regulations. Parking signs shall comply with the standards of shape, color, and location.
- **[M]** 2B.53-04 (p.123): Prohibitive parking signs (see Drawing A in Figure 2B-25 for some commonly used examples) shall be used where parking is prohibited at all times or at specific times. Except as otherwise provided in this Section, parking signs shall have a red legend and border on a white background and, when the parking prohibition symbol is used, the symbol “P” shall be black.
- **[M]** 2B.53-05 (p.123): Permissive parking signs (see Drawing B in Figure 2B-25) shall be used where only time-limited parking or parking in a particular manner is allowed. Permissive parking signs shall have a green legend and border on a white background.
- **[R]** 2B.53-06 (p.123): Parking information, should be displayed from top to bottom of the sign, as applicable, in the following order: A. The restriction or prohibition; B. The times of the day that it is applicable, if not all hours; C. The days of the week that it is applicable, if not every day; D. Qualifying or supplementary information; E. Exemptions to the restriction of prohibition; and F. Any tow-away message or symbol.
- **[R]** 2B.53-07 (p.123): If the parking regulation applies to a limited area or zone, the limits of the regulation should be shown by arrows or supplemental plaques. If arrows are used and if the sign is at the end of a parking zone, there should be a single-headed arrow pointing in the direction that the regulation is in effect. If the sign is at an intermediate point in a zone, there should be a double-headed arrow pointing both ways. When a single sign is used at the transition point between two parking zones, it should display a right arrow and a left arrow pointing in the direction that the respective regulations apply.
- **[M]** 2B.53-08 (p.125): The times and days for which the parking regulations are in effect shall be posted if they are not in effect at all times of day or all days of the week.
- [O] 2B.53-09 (p.125): As an alternate to the use of arrows to show designated restriction zones, the following word messages may be used: BEGIN, END, HERE TO CORNER, HERE TO ALLEY, and THIS SIDE OF SIGN.
- [O] 2B.53-10 (p.125) ◆ R8-1, R8-2, R8-3, R8-3a, R8-3c, R8-3d, R8-3e, R8-3f: The R8 series signs (see Drawing A in Figure 2B-25) may be used where sufficient notice of a parking prohibition is satisfied by the use of single signs and are not needed to designate the beginning and end of a zone in which parking is prohibited or restricted. In rural and certain other areas the legends NO PARKING ON PAVEMENT (R8-1) or NO STOPPING ON PAVEMENT (R8-5) are generally suitable and may be used where parking or stopping is allowed on an unpaved shoulder or border adjacent to the paved portion of the road. If a roadway has an adjacent paved shoulder on which parking or stopping is allowed, the legend NO PARKING EXCEPT ON SHOULDER (R8-2) or NO STOPPING EXCEPT ON SHOULDER (R8-6) may be used. The R8-3 symbol sign or the word message NO PARKING may be used to prohibit any parking along a roadway. Word legend supplemental plaques may be mounted below the NO PARKING signs or the word legend may be incorporated within signs whose sizes are increased accordingly. The R8-3 series signs may include word legends such as ON PAVEMENT (R8-3c), ON BRIDGE (R8-3d), ON TRACKS (R8-3e), and EXCEPT ON SHOULDERS (R8-3f).
- **[R]** 2B.53-11 (p.125) ◆ R7-203: Where special parking restrictions are imposed during heavy snowfall or a declared snow emergency, a Snow Emergency Route (R7-203) sign (see Drawing A in Figure 2B-25) should be installed. The legend should be modified to display the specific regulations. The upper section of the sign should display the designation as a snow emergency route in a white legend and border on a red background.
- **[R]** 2B.53-12 (p.125) ◆ R7-21, R7-22: If a fee is charged for on-street parking and payments are made at a multi-space parking meter, instead of individual parking meters for each parking space, Metered Parking (R7-21 and R7-22) signs (see Drawing B in Figure 2B-25) should be used to define the area where the multi-space parking meter applies. The Multi-Space Parking Meter (R7-20) sign (see Drawing B in Figure 2B-25) should be used at the meter location to direct road users to the meter.
- [O] 2B.53-13 (p.126) ◆ R7-21aP: Where payments can be made electronically, such as by telephone or mobile application, the Mobile Parking Payment (R7-21aP) plaque (see Drawing B in Figure 2B-25) may be installed below or as part of the legend of a Metered Parking sign.
- **[M]** 2B.53-14 (p.126) ◆ R7-21, R7-22: If the metered parking is subject to a maximum time limit, the appropriate time limit (number of hours or minutes) shall be displayed on the Metered Parking (R7-21 and R7-22) signs and, except as provided in Paragraph 15 of this Section, on the Multi-space Parking Meter (R7-20) signs.
- [O] 2B.53-15 (p.126): Where the maximum time limit varies by the time of the day or by the day of the week, the display of the time limits may be omitted from the R7-20 sign and, instead, be displayed on the multi-space parking meter so that they are visible to pedestrians as they make payments.
- **[M]** 2B.53-16 (p.126) ◆ R7-8: Where parking spaces are reserved for persons with disabilities, the Accessible Parking (R7-8) sign (see Drawing D in Figure 2B-25) shall be used to designate the space and shall display the official International Symbol of Accessibility.
- **[M]** 2B.53-17 (p.126) ◆ R7-8, R7-8aP: Where parking spaces that are reserved for persons with disabilities are designed to accommodate wheelchair vans, a VAN ACCESSIBLE (R7-8aP) plaque (see Drawing D in Figure 2B-25) shall be mounted below the R7-8 sign.
- **[R]** 2B.53-18 (p.126) ◆ R7-1, R7-111, R7-112, R7-113: Where parking spaces are designated for parking of electric vehicles, an Electric Vehicle Parking (R7-111 series, R7-112 series, and R7-113) sign (see Drawing E of Figure 2B-25) should be installed adjacent to the designated spaces. Where there is no time limit, the R7-111 series sign should be used. Where parking is subject to a time limit, the R7-112 series sign should be used.
- **[R]** 2B.53-19 (p.126) ◆ R7-1, R7-113, R7-114: Where parking spaces are only designated for charging of electric vehicles, an R7-113 sign or R7-114 series sign (see Drawing E in Figure 2B-25) should be installed adjacent to the designated spaces.
- **[R]** 2B.53-20 (p.126) ◆ R7-1, R7-113, R7-113aP, R7-114: Where additional restrictions apply while a vehicle occupies the designated space, the R7-113P series plaques should be installed below the R7-113 sign or the R7-114 series signs.
- [O] 2B.53-21 (p.126) ◆ R7-1, R7-108: Where parking is prohibited during certain hours and time-limited parking or parking in a particular manner is allowed during certain other time periods, the red Parking Prohibition and green Permissive Parking signs may be designed as follows (see Drawing C in Figure 2B-25): A. Two 12 x 18-inch parking signs may be used with the red Parking Prohibition (R7-1) sign installed above or to the left of the green Permissive Parking (R7-108) sign; or B. A single sign (R7-200 or R7-200a) may be used.
- [O] 2B.53-22 (p.126): At the transition point between two parking zones, a single sign (R7-200 or R7-200a) or two signs mounted side-by-side may be used.
- [O] 2B.53-23 (p.126) ◆ R7-2a: The words NO PARKING may be used as an alternative to the No Parking symbol (see the R7-2a sign in Drawing A in Figure 2B-25).
- [O] 2B.53-24 (p.126) ◆ R7-1, R7-10, R7-107, R7-107a: Alternate designs for the R7-107 sign may be developed such as the R7-107a sign (see Drawing A in Figure 2B-25). Alternate designs may include, on a single sign, a transit logo, an approved bus symbol, a parking prohibition, the words BUS STOP, and an arrow. The reverse side of the R7-107 series signs may display bus routing information for pedestrians.
- [O] 2B.53-25 (p.126) ◆ R7-201P: A Tow-Away Zone (R7-201P or R7-201aP) plaque (see Drawing A in Figure 2B-25) may be mounted below any parking prohibition sign. The word legend TOW-AWAY ZONE may be incorporated into the parking prohibition sign in lieu of using a separate plaque.
- [O] 2B.53-26 (p.126) ◆ R7-201P: The R7-201P plaque may have a black or red symbol and border on a white background.
- **[R]** 2B.53-27 (p.126): When a legend other than that on the standard parking signs is necessary, letter height, symbol size, and basic sign layout should be consistent with the those shown on the standard parking signs as detailed in the “Standard Highway Signs” publication (see Section 1A.05.)
- **[R]** 2B.53-28 (p.126): In general, the letter height of the principal legend on parking signs sized for urbanized applications should be at least 2 inches.

*Also governed by Section 2B.54:*

- **[R]** 2B.54-02 (p.127): When signs with arrows are used to indicate the extent of the restricted zones, the signs should be set at an angle of not less than 30 degrees or more than 45 degrees with the line of traffic flow in order to be visible to approaching traffic.
- **[R]** 2B.54-03 (p.127): When signs are placed at the head of perpendicular parking stalls, the signs should be parallel to the roadway facing the parking stall.
- **[R]** 2B.54-04 (p.127): Spacing of signs should be based on legibility, conspicuity, and sign orientation.
- **[R]** 2B.54-05 (p.127) ◆ R7-202P: If the zone is long, signs should be used at intermediate points within the zone. 06 If the signs are mounted at an angle of 90 degrees to the curb line, two signs should be mounted back to back at the transition point between two parking zones, each with an appended THIS SIDE OF SIGN (R7-202P) supplemental plaque (see Drawing A in Figure 2B-25).
- **[R]** 2B.54-07 (p.127): If the signs are mounted at an angle of 90 degrees to the curb line, signs without any arrows or appended plaques should be used at intermediate points within a parking zone, facing in the direction of approaching traffic. Otherwise, the standards of placement should be the same as for signs using directional arrows.
- [O] 2B.54-08 (p.127): Blanket parking regulations that apply to an entire jurisdiction may, if legal, be posted in the vicinity of the jurisdictional boundary lines. Blanket parking regulations that apply to a posted zone or district may, if legal, be posted at the entry points to the zone or district.

*Also governed by Section 6G.02:*

- **[M]** 6G.02-01 (p.793): TTC regulatory signs shall comply with the Standards for regulatory signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6G.02-02 (p.793): The sizes for TTC regulatory signs shall be as shown in Table 6G-1.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

*Also governed by Section 9B.10:*

- [O] 9B.10-01 (p.1057) ◆ R7-10: The Back-In Parking (R7-10) sign (see Section 2B.52 and Figure 9B-1) may be used where back-in parking is required by motor vehicles in the presence of a bicycle lane or movement.

<a id="sec-2B-53"></a>
#### Section 2B.53 Design of Parking, Standing, and Stopping Signs

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R7-20](symbols/R7-20.png) | **R7-20** | Parking Fee Station, | Recommended (2B.53-12) | 24 x 18 | 24 x 18 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-107b](symbols/R7-107b.png) | **R7-107b** | No Parking Bus Stop | Optional | 12 x 30 | 12 x 30 | — | — | — | — | 2B-1 p.70 | — |
| ![R7-111a](symbols/R7-111a.png) | **R7-111a** | No Parking Except Electric Vehicles | Recommended (2B.53-18) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-112a](symbols/R7-112a.png) | **R7-112a** | Electric Vehicle Parking (time limit | Recommended (2B.53-18) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-112b](symbols/R7-112b.png) | **R7-112b** | Electric Vehicle Parking (time limit | Recommended (2B.53-18) | 12 x 21 | 12 x 21 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-113bP](symbols/R7-113bP.png) | **R7-113bP** | Vacate Stall When Charging | Recommended (2B.53-20) | 12 x 6 | 12 x 6 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-114a](symbols/R7-114a.png) | **R7-114a** | Vehicle Charging Only (time limit, | Recommended (2B.53-19) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R7-114b](symbols/R7-114b.png) | **R7-114b** | Vehicle Charging Only (time limit | Recommended (2B.53-19) | 12 x 21 | 12 x 21 | — | — | — | — | 2B-1 p.71 | — |
|  | **R7-200** | No Parking/Restricted Parking | Optional (2B.53-21) | 24 x 18 | 24 x 18 | — | — | — | — | 2B-1 p.71 | — |
|  | **R7-200a** | No Parking/Restricted Parking | Optional (2B.53-21) | 12 x 36 | 12 x 36 | — | — | — | — | 2B-1 p.71 | — |
| ![R8-5](symbols/R8-5.png) | **R8-5** | No Stopping on Pavement | Optional (2B.53-10) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.71 | — |
| ![R8-6](symbols/R8-6.png) | **R8-6** | No Stopping Except on Shoulder | Optional (2B.53-10) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.71 | — |

*Also governed by Section 2B.52:*

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

- [O] 2B.53-10 (p.125) ◆ R8-5, R8-6: The R8 series signs (see Drawing A in Figure 2B-25) may be used where sufficient notice of a parking prohibition is satisfied by the use of single signs and are not needed to designate the beginning and end of a zone in which parking is prohibited or restricted. In rural and certain other areas the legends NO PARKING ON PAVEMENT (R8-1) or NO STOPPING ON PAVEMENT (R8-5) are generally suitable and may be used where parking or stopping is allowed on an unpaved shoulder or border adjacent to the paved portion of the road. If a roadway has an adjacent paved shoulder on which parking or stopping is allowed, the legend NO PARKING EXCEPT ON SHOULDER (R8-2) or NO STOPPING EXCEPT ON SHOULDER (R8-6) may be used. The R8-3 symbol sign or the word message NO PARKING may be used to prohibit any parking along a roadway. Word legend supplemental plaques may be mounted below the NO PARKING signs or the word legend may be incorporated within signs whose sizes are increased accordingly. The R8-3 series signs may include word legends such as ON PAVEMENT (R8-3c), ON BRIDGE (R8-3d), ON TRACKS (R8-3e), and EXCEPT ON SHOULDERS (R8-3f).
- **[R]** 2B.53-12 (p.125) ◆ R7-20: If a fee is charged for on-street parking and payments are made at a multi-space parking meter, instead of individual parking meters for each parking space, Metered Parking (R7-21 and R7-22) signs (see Drawing B in Figure 2B-25) should be used to define the area where the multi-space parking meter applies. The Multi-Space Parking Meter (R7-20) sign (see Drawing B in Figure 2B-25) should be used at the meter location to direct road users to the meter.
- **[M]** 2B.53-14 (p.126) ◆ R7-20: If the metered parking is subject to a maximum time limit, the appropriate time limit (number of hours or minutes) shall be displayed on the Metered Parking (R7-21 and R7-22) signs and, except as provided in Paragraph 15 of this Section, on the Multi-space Parking Meter (R7-20) signs.
- [O] 2B.53-15 (p.126) ◆ R7-20: Where the maximum time limit varies by the time of the day or by the day of the week, the display of the time limits may be omitted from the R7-20 sign and, instead, be displayed on the multi-space parking meter so that they are visible to pedestrians as they make payments.
- **[R]** 2B.53-18 (p.126) ◆ R7-111a, R7-112a, R7-112b: Where parking spaces are designated for parking of electric vehicles, an Electric Vehicle Parking (R7-111 series, R7-112 series, and R7-113) sign (see Drawing E of Figure 2B-25) should be installed adjacent to the designated spaces. Where there is no time limit, the R7-111 series sign should be used. Where parking is subject to a time limit, the R7-112 series sign should be used.
- **[R]** 2B.53-19 (p.126) ◆ R7-114a, R7-114b: Where parking spaces are only designated for charging of electric vehicles, an R7-113 sign or R7-114 series sign (see Drawing E in Figure 2B-25) should be installed adjacent to the designated spaces.
- **[R]** 2B.53-20 (p.126) ◆ R7-113bP, R7-114a, R7-114b: Where additional restrictions apply while a vehicle occupies the designated space, the R7-113P series plaques should be installed below the R7-113 sign or the R7-114 series signs.
- [O] 2B.53-21 (p.126) ◆ R7-200, R7-200a: Where parking is prohibited during certain hours and time-limited parking or parking in a particular manner is allowed during certain other time periods, the red Parking Prohibition and green Permissive Parking signs may be designed as follows (see Drawing C in Figure 2B-25): A. Two 12 x 18-inch parking signs may be used with the red Parking Prohibition (R7-1) sign installed above or to the left of the green Permissive Parking (R7-108) sign; or B. A single sign (R7-200 or R7-200a) may be used.
- [O] 2B.53-22 (p.126) ◆ R7-200, R7-200a: At the transition point between two parking zones, a single sign (R7-200 or R7-200a) or two signs mounted side-by-side may be used.
- [O] 2B.53-24 (p.126) ◆ R7-107b: Alternate designs for the R7-107 sign may be developed such as the R7-107a sign (see Drawing A in Figure 2B-25). Alternate designs may include, on a single sign, a transit logo, an approved bus symbol, a parking prohibition, the words BUS STOP, and an arrow. The reverse side of the R7-107 series signs may display bus routing information for pedestrians.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

<a id="sec-2B-55"></a>
#### Section 2B.55 Emergency Restriction Signs (R8-4 and R8-7)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **R8-4** | Emergency Parking Only | Optional (2B.55-02) | 30 x 24 | 30 x 24 | 30 x 24 | 48 x 36 | — | 48 x 36 | 2B-1 p.71 | — |
|  | **R8-7** | Emergency Stopping Only | Optional (2B.55-02) | 30 x 24 | 30 x 24 | 48 x 36 | 48 x 36 | — | 48 x 36 | 2B-1 p.71 | — |

*Also governed by Section 2B.52:*

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

- **[M]** 2B.55-01 (p.127): Emergency Restriction signs (see Figure 2B-26) shall be rectangular and shall have a black legend and border on a white background.
- [O] 2B.55-02 (p.127): The EMERGENCY PARKING ONLY (R8-4) sign or the EMERGENCY STOPPING ONLY (R8-7) sign may be used to discourage or prohibit shoulder parking, particularly where scenic or other attractions create a tendency for road users to desire to stop temporarily.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

<a id="sec-2B-56"></a>
#### Section 2B.56 WALK ON LEFT FACING TRAFFIC and No Hitchhiking Signs (R9-1, R9-4, and R9-4a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R9-1](symbols/R9-1.png) | **R9-1** | Walk on Left Facing Traffic | Optional (2B.56-01) | 18 x 24 | 18 x 24 | — | — | — | — | 2B-1 p.71 | — |
| ![R9-4](symbols/R9-4.png) | **R9-4** | No Hitchhiking (symbol) | Optional (2B.56-01) | 18 x 18 | 18 x 18 | — | — | — | 24 x 24 | 2B-1 p.72 | — |
| ![R9-4a](symbols/R9-4a.png) | **R9-4a** | No Hitchhiking | Optional (2B.56-01) | 18 x 24 | 18 x 24 | — | — | 12 x 18 | — | 2B-1 p.72 | — |

- [O] 2B.56-01 (p.128) ◆ R9-1: The WALK ON LEFT FACING TRAFFIC (R9-1) sign (see Figure 2B-27) may be used on highways where no sidewalks are provided.
- **[R]** 2B.56-02 (p.128): If used, the WALK ON LEFT FACING TRAFFIC sign should be installed on the right-hand side of the road where pedestrians walk on the pavement or shoulder in the absence of pedestrian pathways or sidewalks.
- [O] 2B.56-03 (p.128) ◆ R9-4, R9-4a: The No Hitchhiking (R9-4) sign (see Figure 2B-27) may be used to prohibit standing in or adjacent to the roadway for the purpose of soliciting a ride. The R9-4a word message sign (see Figure 2B-27) may be used as an alternate to the R9-4 symbol sign.

<a id="sec-2B-57"></a>
#### Section 2B.57 Pedestrian Crossing Signs (R9-2 and R9-3)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R9-2](symbols/R9-2.png) | **R9-2** | Cross Only at Crosswalks | Optional (2B.57-01) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R9-3](symbols/R9-3.png) | **R9-3** | No Pedestrian Crossing (symbol) | Optional (2B.57-01) | 18 x 18 | 18 x 18 | 24 x 24 | 30 x 30 | — | 30 x 30 | 2B-1 p.71 | 9A-1 |
| ![R9-3a](symbols/R9-3a.png) | **R9-3a** | No Pedestrian Crossing | Optional (2B.57-05) | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.71 | — |
| ![R9-3bP](symbols/R9-3bP.png) | **R9-3bP** | Use Crosswalk (plaque) | Optional (2B.57-05) | 18 x 12 | 18 x 12 | — | — | — | — | 2B-1 p.72 | — |

- [O] 2B.57-01 (p.128): Pedestrian Crossing signs (see Figure 2B-27) may be used to limit pedestrian crossing to specific locations.
- **[M]** 2B.57-02 (p.128): If used, Pedestrian Crossing signs shall be installed to face pedestrian approaches.
- [O] 2B.57-03 (p.128) ◆ R9-2: Where crosswalks are clearly defined, the CROSS ONLY AT CROSSWALKS (R9-2) sign may be used to prohibit pedestrians from crossing at locations away from crosswalks.
- [O] 2B.57-04 (p.128) ◆ R9-3: The No Pedestrian Crossing (R9-3) sign may be used to prohibit pedestrians from crossing a roadway at an undesirable location or in front of a school or other public building where a crossing is not designated.
- [O] 2B.57-05 (p.128) ◆ R9-3, R9-3a, R9-3bP: The NO PEDESTRIAN CROSSING (R9-3a) word message sign may be used as an alternate to the R9-3 symbol sign. The USE CROSSWALK (R9-3bP) supplemental plaque, along with an arrow, may be installed below either sign to designate the direction of the crossing.

*Also governed by Section 9B.08:*

- [S] 9B.08-02 (p.1056) ◆ R9-3: Typical exclusion messages include: A. No Bicycles (R5-6); B. No Pedestrians (R9-3); C. No Skaters (R9-13); D. No Equestrians (R9-14); E. No Snowmobiles (R9-15); and F. No All-Terrain Vehicles (R9-16).

*Also governed by Section 9B.18:*

- **[M]** 9B.18-03 (p.1059): Where bicycles are required to use a two-stage bicycle turn box (see Figure 9B-5), the Two-Stage Bicycle Turn Box regulatory sign series (see Figure 9B-5) shall be used.
- **[M]** 9B.18-04 (p.1059): Where bicycles are required to use a two-stage bicycle turn box, the Bicycles All Turns from Bike Lane (R9-23) or Bicycle Left Turn from Bike Lane (R9-23a) advance regulatory sign shall be mounted in advance of the intersection, and at least one Bicycle Turn Must Use Turn Box (R9-23b or R9-23c) sign shall be used at the intersection.
- **[M]** 9B.18-05 (p.1059): Where used, the Bicycle Turn Must Use Turn Box (R9-23b) sign shall be mounted at the near side of the intersection.
- **[M]** 9B.18-06 (p.1059): Where used, the Bicycle Turn Must Use Turn Box location (R9-23c) sign shall be mounted at the far side of the intersection.
- [O] 9B.18-07 (p.1059): Where use of a two-stage bicycle turn box is optional, the Two-Stage Bicycle Turn Box guide sign series (see Section 9D.13) may be used to provide directional information.
- [O] 9B.18-08 (p.1059): If used, an appropriately sized Street Name (D3-1) sign (see Section 2D.45) may be installed below the All Turns from Bike Lane sign or Left Turn from Bike Lane sign to identify the crossroad where the turn box will be available.

*Also governed by Section 9B.19:*

- [O] 9B.19-02 (p.1062): The R9-23 sign (see Figure 9B-1) may be used in advance of where bicyclists are required to use the bicycle jughandle turn in order to facilitate all turns.
- [O] 9B.19-03 (p.1062) ◆ R9-2: The R9-24 series sign (see Figure 9B-1) may be used where bicyclists are required to use the bicycle jughandle turn in order to facilitate all turns.
- [O] 9B.19-04 (p.1062) ◆ R9-2: The R9-25 series sign (see Figure 9B-1) may be used where bicyclists are required to use a bicycle jughandle turn to facilitate U-turns and left turns and where right-turning bicyclists are exempted or the right turn is not available or possible (see Figure 9B-6).
- [O] 9B.19-05 (p.1062) ◆ R9-2: The R9-26 series sign (see Figure 9B-1) may be used where bicyclists are required to use a jughandle to facilitate U-turns and where left-turning and right-turning bicyclists are exempted or the left turn or right turn is not available or possible.
- [O] 9B.19-06 (p.1062) ◆ R9-2: The R9-27 series sign (see Figure 9B-1) may be used where bicyclists are required to use a jughandle to facilitate left turns and where U-turning and right-turning bicyclists are exempted or the U-turn or right turn is not available or possible.
- [O] 9B.19-07 (p.1063): A Bicycle Jughandle sign may be used to indicate a jughandle turn initially made by a left turn for a bicycle lane on the left-hand side of a one-way street or for a counter-flow bicycle lane. The legend RIGHT may be substituted for the legend LEFT on Bicycle Jughandle signs to represent bicycle facilities on the left-hand side of the roadway where facilitating a right turn would be applicable.
- **[R]** 9B.19-08 (p.1063): Applications of Bicycle Jughandle signs should be limited to brief independent alignments either through physical separation or islands formed by pavement markings. Bicycle Jughandle signs should not be used for a turning movement facilitated by a two-stage turn box (see Section 9B.18).

<a id="sec-2B-58"></a>
#### Section 2B.58 Traffc Signal Pedestrian and Bicyclist Actuation Signs (R10i -1 through R10-4 and R10-24 through R10-26)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R10-1](symbols/R10-1.png) | **R10-1** | Cross Only On Green | Optional | 12 x 18 | 12 x 18 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-2](symbols/R10-2.png) | **R10-2** | SIGNAL | Optional | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3](symbols/R10-3.png) | **R10-3** | Pedestrian Signs | Optional (2B.58-03) | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3a](symbols/R10-3a.png) | **R10-3a** | Cross Street Wait for Walk Signal | Optional (2B.58-03) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3b](symbols/R10-3b.png) | **R10-3b** | Pedestrian Signs | Optional (2B.58-06) | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3c](symbols/R10-3c.png) | **R10-3c** | Pedestrian Signs | Optional (2B.58-06) | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3d](symbols/R10-3d.png) | **R10-3d** | Pedestrian Signs | Optional (2B.58-06) | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3e](symbols/R10-3e.png) | **R10-3e** | Pedestrian Signs | Optional (2B.58-06) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3f](symbols/R10-3f.png) | **R10-3f** | Pedestrian Signs | Optional (2B.58-06) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3g](symbols/R10-3g.png) | **R10-3g** | Pedestrian Signs | Optional (2B.58-06) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3h](symbols/R10-3h.png) | **R10-3h** | Pedestrian Signs | Optional (2B.58-06) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-3i](symbols/R10-3i.png) | **R10-3i** | Pedestrian Signs | Optional (2B.58-06) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-4](symbols/R10-4.png) | **R10-4** | Bicycle Actuation Signs | Optional (2B.58-03) | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.72 | 9A-1 |
| ![R10-4a](symbols/R10-4a.png) | **R10-4a** | Cross Street Wait for Green Signal | Optional (2B.58-03) | 9 x 15 | 9 x 15 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-25](symbols/R10-25.png) | **R10-25** | Push Button For Warning Lights - | Optional (2B.58-03) | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.73 | 9A-1 |
| ![R10-32P](symbols/R10-32P.png) | **R10-32P** | Push Button for 2 Seconds for | Optional | 9 x 12 | 9 x 12 | — | — | — | — | 2B-1 p.73 | — |

- **[M]** 2B.58-01 (p.128): Where manual actuation of a traffic signal is required for pedestrians or bicyclists to call a signal phase to cross the roadway, traffic signal signs applicable to pedestrian actuation (see Figure 2B-27) or bicyclist actuation (see Figure 9B-1) shall be mounted immediately above or incorporated into the push button detector units (see Section 4I.05).
- [S] 2B.58-02 (p.128) ◆ R10-1, R10-2, R10-3, R10-3a, R10-3b, R10-3c, R10-3d, R10-3e, R10-3f, R10-3g, R10-3h, R10-3i, R10-4, R10-4a: Traffic signal signs applicable to pedestrians include: A. CROSS ONLY ON GREEN (symbolic circular green) (R10-1), B. CROSS ONLY ON (symbolic walk indication) SIGNAL (R10-2), C. Push Button for Walk Signal (R10-3 series), and D. Push Button for Green Signal (R10-4 series).
- [O] 2B.58-03 (p.128) ◆ R10-3, R10-3a, R10-4, R10-4a: The following signs may be used as an alternate for the R10-3 and R10-4 signs: A. Push Button to Cross Street Wait for Walk Signal (R10-3a); or B. Push Button to Cross Street Wait for Green Signal (R10-4a).
- [O] 2B.58-04 (p.128) ◆ R10-3a, R10-4a: The name of the street to be crossed may be substituted for the word STREET in the legends on the R10-3a and R10-4a signs.
- **[R]** 2B.58-05 (p.128) ◆ R10-3, R10-3a, R10-4, R10-4a: The finger in the push button symbol on the R10-3, R10-3a, R10-4, and R10-4a signs should point in the same direction as the arrow on the sign. Figure 2B-27. Pedestrian Signs and Plaques (Sheet 1 of 2)
- [O] 2B.58-06 (p.130) ◆ R10-3, R10-3a, R10-3b, R10-3c, R10-3d, R10-3e, R10-3f, R10-3g, R10-3h, R10-3i: Where symbolic pedestrian signal indications are used, an educational sign (R10-3b) may be used instead of the R10-3 sign to improve pedestrian understanding of pedestrian indications at signalized intersections. Where word-legend pedestrian signal indications are being retained for the remainder of their useful service life, the legends WALK/DONT WALK may be substituted for the symbols on the educational sign R10-3b, thus creating educational sign R10-3c. The R10-3d educational sign may be used to inform pedestrians that the pedestrian clearance time is sufficient only for the pedestrian to cross to the median at locations where pedestrians cross in two stages using a median refuge island. The R10-3e educational sign may be used where countdown pedestrian signals have been provided. In order to assist the pedestrian in understanding which push button to push, the R10-3f through R10-3i educational signs that provide the name of the street to be crossed may be used instead of the R10-3b through R10-3e educational signs.
- [O] 2B.58-07 (p.130): The R10-24 or R10-26 sign (see Section 9B.20) may be used where a push button detector has been installed exclusively to actuate a green phase for bicyclists.
- [O] 2B.58-08 (p.130) ◆ R10-25: The R10-25 sign (see Figure 2B-27) may be used where a push button detector has been installed for pedestrians to activate In-Roadway Warning Lights (see Chapter 4U) or flashing beacons that have been added to the pedestrian warning signs.
- [S] 2B.58-09 (p.130) ◆ R10-32P: Section 4I.05 contains information regarding the application of the R10-32P plaque.

*Also governed by Section 2B.60:*

- **[M]** 2B.60-01 (p.134): Where a right turn on a circular red signal indication (or a left turn on a circular red signal indication from a one-way street to a one-way street) is to be prohibited, a NO TURN ON RED (R10-11, R10-11b) word message sign (see Figure 2B-28) shall be used. A NO TURN ON RED (symbolic circular red) (R10-11a) sign (see Figure 2B-28) shall be used when the approach is controlled by both circular red and red arrow indications.
- **[R]** 2B.60-02 (p.134): If used, the No Turn on Red sign should be installed near the appropriate signal head.
- **[R]** 2B.60-03 (p.134): A No Turn on Red sign should be considered when an engineering study finds that one or more of the following conditions exists: A. Inadequate sight distance to vehicles approaching from the left (or right, if applicable); B. Geometrics or operational characteristics of the intersection that might result in unexpected conflicts; C. An exclusive pedestrian or bicycle phase; D. An unacceptable number of conflicting pedestrian movements with right-turn-on-red maneuvers, especially involving children, older pedestrians, or persons with disabilities; E. More than three right-turn-on-red crashes reported in a 12-month period for the particular approach; or F. The skew angle of the intersecting roadways creates difficulty for drivers to see traffic approaching from their left (or right, if applicable).
- **[M]** 2B.60-04 (p.134): If an R10-11, R10-11a, R10-11b, or R10-17a sign with conventional road size as shown in Table 2B-1 is used on an approach on the far side of the intersection and the distance between the stop line and the sign is greater than 120 feet, then a duplicate sign shall be located on the near side of the intersection to supplement the sign on the far side of the intersection.
- [O] 2B.60-05 (p.134): When a no-turn-on-red restriction applies during certain time periods only, the following alternatives may be used: A. Movement Prohibition (R3-1, R3-2, R3-4, R3-18, and R3-27) signs or NO TURN ON RED signs displayed by using a blank-out sign for the time period or one or more portion(s) of a particular cycle of the traffic control signal during which the prohibition is applicable; or B. Static signs incorporating a supplemental legend or with a supplemental R10-20aP plaque (see Figure 2B28) showing the hours and days during which the prohibition is applicable.
- [O] 2B.60-06 (p.134): White LEDs may be used in the border and activated during periods of turn prohibition to enhance the sign conspicuity.
- [O] 2B.60-07 (p.134): On signalized approaches with more than one right-turn lane, a NO TURN ON RED EXCEPT FROM RIGHT LANE (R10-11c) sign (see Figure 2B-28) may be post-mounted at the intersection or a NO TURN ON RED FROM THIS LANE (with down arrow) (R10-11d) sign (see Figure 2B-28) may be mounted over the approximate center of the lane from which turns on red are prohibited.
- **[R]** 2B.60-08 (p.134): Where turns on red are permitted and the signal indication is a steady RED ARROW, the RIGHT (LEFT) ON RED ARROW AFTER STOP (R10-17a) sign (see Figure 2B-28) should be installed adjacent to the RED ARROW signal indication.
- [O] 2B.60-09 (p.134): A RIGHT TURN ON RED MUST YIELD TO U-TURN (R10-30) sign (see Figure 2B-28) may be installed to remind road users that they must yield to conflicting U-turn traffic on the street or highway onto which they are turning right on a red signal after stopping.

*Also governed by Section 9B.20:*

- [O] 9B.20-01 (p.1063) ◆ R10-4: Where bicycles are not controlled by pedestrian signal indications, the R10-4, R10-24, or R10-26 sign (see Section 2B.58) may be used.
- **[R]** 9B.20-02 (p.1063) ◆ R10-4: If used, the R10-4, R10-24, or R10-26 signs (see Figure 9B-1) should be installed in the vicinity of where bicycles will be crossing the street.
- [O] 9B.20-03 (p.1063) ◆ R10-25: If bicycles are crossing a roadway where In-Roadway Warning Lights (see Section 4U.02) or other warning lights or beacons have been provided, the R10-25 sign may be used.
- [O] 9B.20-04 (p.1063): The Bicycle Detector (R10-22) sign (see Figure 9B-1) may be installed at signalized intersections where pavement markings are used to indicate the location where a bicycle is to be positioned to actuate the signal (see Section 9E.15).
- **[R]** 9B.20-05 (p.1063): If the Bicycle Detector sign is installed, it should be placed at the roadside adjacent to the marking to emphasize the location of the marking.

<a id="sec-2B-59"></a>
#### Section 2B.59 Traffc Signal Signs and Plaques (R10i -5 through R10-30)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R10-5](symbols/R10-5.png) | **R10-5** | Left on Green Arrow Only | Optional (2B.59-01) | 30 x 36 | 30 x 36 | 30 x 36 | — | 24 x 30 | 48 x 60 | 2B-1 p.72 | — |
| ![R10-6](symbols/R10-6.png) | **R10-6** | STOP
HERE ON RED | Optional (2B.59-01) | 24 x 36 | 24 x 36 | — | — | — | 36 x 48 | 2B-1 p.72 | 8B-1, 6G-1 |
| ![R10-6a](symbols/R10-6a.png) | **R10-6a** | Stop Here on Red | Optional (2B.59-01) | 24 x 30 | 24 x 30 | — | — | — | 36 x 42 | 2B-1 p.72 | 8B-1 |
| ![R10-7](symbols/R10-7.png) | **R10-7** | Do Not Block Intersection | Optional (2B.59-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-8](symbols/R10-8.png) | **R10-8** | Use Lane with Green Arrow | Optional (2B.59-01) | 30 x 36 | 30 x 36 | 36 x 42 | — | — | 60 x 72 | 2B-1 p.72 | — |
| ![R10-10](symbols/R10-10.png) | **R10-10** | Left (Right) Turn Signal | Optional (2B.59-01) | 24 x 30 | 24 x 30 | — | — | — | 30 x 36 | 2B-1 p.72 | — |
| ![R10-10a](symbols/R10-10a.png) | **R10-10a** | U- Turn Signal | Optional (2B.59-01) | 24 x 30 | 24 x 30 | — | — | — | 30 x 36 | 2B-1 p.72 | — |
| ![R10-12](symbols/R10-12.png) | **R10-12** | Left Turn Yield on Green | Optional (2B.59-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-12a](symbols/R10-12a.png) | **R10-12a** | Left Turn Yield on Flashing | Optional (2B.59-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-12b](symbols/R10-12b.png) | **R10-12b** | Left Turn Yield to Bicycle | Optional (2B.59-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.72 | 9A-1 |
| ![R10-13](symbols/R10-13.png) | **R10-13** | Emergency Signal | Optional (2B.59-01) | 36 x 24 | 36 x 24 | — | — | — | 42 x 30 | 2B-1 p.72 | — |
| ![R10-14](symbols/R10-14.png) | **R10-14** | Emergency Signal - Stop on | Optional (2B.59-01) | 36 x 42 | 36 x 42 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-14a](symbols/R10-14a.png) | **R10-14a** | Traffc Signal Signs and Plaques (R10i -5 through R10-30) | Optional (2B.59-01) | — | — | — | — | — | — | text | — |
| ![R10-14b](symbols/R10-14b.png) | **R10-14b** | Stop Here on Flashing Red | Optional (2B.59-01) | 24 x 36 | 24 x 36 | — | — | — | 36 x 48 | 2B-1 p.72 | — |
| ![R10-15](symbols/R10-15.png) | **R10-15** | Turning Vehicles Yield to | Optional (2B.59-01) | 30 x 30 | 30 x 30 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-15a](symbols/R10-15a.png) | **R10-15a** | Turning Vehicles Stop for | Optional (2B.59-01) | 30 x 30 | 30 x 30 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-16](symbols/R10-16.png) | **R10-16** | U-Turn Yield to Right Turn | Optional (2B.59-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-23](symbols/R10-23.png) | **R10-23** | Crosswalk - Stop on Red | Optional (2B.59-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-23a](symbols/R10-23a.png) | **R10-23a** | Stop on Red - Yield on Flashing | Optional (2B.59-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2B-1 p.73 | — |
| ![R10-27](symbols/R10-27.png) | **R10-27** | Left Turn Yield on Flashing Red | Optional (2B.59-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.73 | — |
| ![R10-31P](symbols/R10-31P.png) | **R10-31P** | At Signal (plaque) | Optional (2B.59-07) | 24 x 9 | 24 x 9 | — | — | — | — | 2B-1 p.73 | — |

- [O] 2B.59-01 (p.131) ◆ R10-5, R10-6, R10-6a, R10-7, R10-8, R10-10, R10-10a, R10-12, R10-12a, R10-12b, R10-13, R10-14, R10-14a, R10-14b, R10-15, R10-15a, R10-16, R10-23, R10-23a, R10-27: To supplement traffic signal control, traffic signal (R10-5 through R10-30) signs (see Figure 2B-28) may be used to regulate road users.
- [O] 2B.59-02 (p.131) ◆ R10-5, R10-6, R10-6a, R10-7, R10-8, R10-10, R10-10a, R10-12, R10-12a, R10-16, R10-27: Traffic signal signs may be installed at certain locations to clarify signal control. Among the legends that may be used for this purpose are: A. LEFT (RIGHT) ON GREEN ARROW ONLY (R10-5), B. STOP HERE ON RED (R10-6 or R10-6a) for observance of stop lines, C. DO NOT BLOCK INTERSECTION (R10-7) for avoidance of traffic obstructions, D. USE LANE(S) WITH GREEN ARROW (R10-8) for obedience to lane-use control signals (see Chapter 4T), E. LEFT (RIGHT) TURN SIGNAL (R10-10), F. U TURN SIGNAL (R10-10a) for exclusive control of a U-turn movement, G. U TURN YIELD TO RIGHT TURN (R10-16), H. LEFT (RIGHT) TURN YIELD ON GREEN (symbolic circular green) (R10-12), I. LEFT (RIGHT) TURN YIELD ON FLASHING YELLOW ARROW (R10-12a), and J. LEFT (RIGHT) TURN YIELD ON FLASHING RED ARROW AFTER STOP (R10-27).
- **[R]** 2B.59-05 (p.131) ◆ R10-16: A U TURN YIELD TO RIGHT TURN (R10-16) sign should be installed near the left-turn signal face if U-turns are allowed on a protected left-turn movement on an approach from which a right-turn GREEN ARROW signal indication is simultaneously being displayed to drivers making a right turn from the conflicting approach to their left.
- [O] 2B.59-06 (p.131) ◆ R10-10a: If used, a U TURN SIGNAL (R10-10a) sign may be installed adjacent to the signal face that exclusively controls a U-turn movement.
- [O] 2B.59-07 (p.131) ◆ R10-12, R10-31P: If needed for additional emphasis, an additional LEFT TURN YIELD ON GREEN (symbolic circular green) (R10-12) sign with an AT SIGNAL (R10-31P) supplemental plaque (see Figure 2B-28) may be installed in advance of the intersection.
- **[M]** 2B.59-09 (p.131) ◆ R10-23, R10-23a: The CROSSWALK—STOP ON RED (symbolic circular red) (R10-23) and STOP ON STEADY REDYIELD ON FLASHING RED AFTER STOP (R10-23a) signs (see Figure 2B-28) shall only be used in conjunction with pedestrian hybrid beacons (see Section 4J.02).
- **[M]** 2B.59-10 (p.131) ◆ R10-13: The EMERGENCY SIGNAL (R10-13) sign (see Figure 2B-28) shall be used in conjunction with emergency-vehicle traffic control signals (see Section 4M.02).
- **[M]** 2B.59-11 (p.131) ◆ R10-14, R10-14a: The EMERGENCY SIGNAL—STOP ON FLASHING RED (R10-14 or R10-14a) sign (see Figure 2B-28) shall be used in conjunction with emergency-vehicle hybrid beacons (see Section 4N.02).
- [O] 2B.59-12 (p.131) ◆ R10-14b: If needed for extra emphasis, a STOP HERE ON FLASHING RED (R10-14b) sign may be installed with an emergency-vehicle hybrid beacon.
- **[M]** 2B.59-13 (p.131) ◆ R10-12b: The Left Turn Yield to Bicycles (R10-12b) sign shall be limited to applications where the conflicting bicyclist movement would be unexpected in direction, location, or similar condition that would tend to violate the expectation of a turning motorist.
- [O] 2B.59-16 (p.133) ◆ R10-15, R10-15a: Where conditions might warrant additional emphasis to drivers turning at a signalized intersection where potential pedestrian conflicts might not be readily apparent, a Turning Vehicles Yield to (Stop for) Pedestrians (R10-15, R10-15a) sign (see Figure 2B-28) may be used.
- **[M]** 2B.59-17 (p.133) ◆ R10-15a: The Turning Vehicles Stop for Pedestrians (R10-15a) sign shall only be used in jurisdictions where laws, ordinances or resolutions specifically require that a driver must stop for a pedestrian.
- **[R]** 2B.59-18 (p.133) ◆ R10-15, R10-15a: The R10-15 series signs, where used, should be placed as follows: A. On the near right corner of the signalized intersection for right-turning vehicles. B. On the far left corner of the signalized intersection for the left-turning vehicles onto a two-way street. C. On the near left corner of the signalized intersection for left-turning vehicles from a one-way street onto a one-way street.

*Also governed by Section 4N.02:*

- **[M]** 4N.02-07 (p.742) ◆ R10-14a: Stop lines and EMERGENCY SIGNAL—STOP ON FLASHING RED (R10-14 or R10-14a) signs (see Section 2B.59) shall be used with emergency-vehicle hybrid beacons for each approach of the major street.

*Also governed by Section 6L.04:*

- **[M]** 6L.04-05 (p.830) ◆ R10-6: A Stop Here On Red (R10-6 or R10-6a) sign (see Section 2B.59) shall be installed on the right-hand side of the approach at the point at which drivers are expected to stop when the steady CIRCULAR RED lens is illuminated (see Figure 6L-2).

*Also governed by Section 8B.10:*

- [S] 8B.10-01 (p.1003) ◆ R10-6, R10-6a: The STOP HERE ON RED (R10-6 or R10-6a) sign (see Figure 8B-1) defines and facilitates observance of stop lines at traffic control signals.
- [O] 8B.10-02 (p.1003): STOP HERE ON RED signs may be used at locations where motor vehicles frequently violate the stop line or where it is not obvious to road users where to stop.
- **[R]** 8B.10-03 (p.1003): If possible, stop lines should be placed at a point where the motor vehicle driver has adequate sight distance along the track.

*Also governed by Section 9B.21:*

- [O] 9B.21-01 (p.1063) ◆ R10-12b: The Left Turn Yield to Bicycles (R10-12b) sign (see Figure 9B-1) may be used to emphasize the requirement for motorists to yield to bicyclists in situations where the motorist is turning across a bicycle movement that may be unexpected in direction, location, or some other quality that would be inconsistent with the typical bicycle lane.

<a id="sec-2B-60"></a>
#### Section 2B.60 No Turn on Red Signs (R10-11 Series, R10-17a, and R10-30)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R10-11](symbols/R10-11.png) | **R10-11** | No Turn on Red | Mandatory (2B.60-01) | 24 x 30 | 24 x 30 | — | — | — | 36 x 48 | 2B-1 p.72 | — |
| ![R10-11a](symbols/R10-11a.png) | **R10-11a** | No Turn on Circular Red | Mandatory (2B.60-01) | 24 x 30 | 24 x 30 | — | — | — | 36 x 48 | 2B-1 p.72 | — |
| ![R10-11b](symbols/R10-11b.png) | **R10-11b** | No Turn on Red | Mandatory (2B.60-01) | 24 x 24 | 24 x 24 | — | — | — | 36 x 36 | 2B-1 p.72 | — |
|  | **R10-11c** | No Turn on Red Except From | Mandatory (2B.60-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-11d](symbols/R10-11d.png) | **R10-11d** | No Turn on Red From This Lane | Mandatory (2B.60-01) | 30 x 42 | 30 x 42 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-17a](symbols/R10-17a.png) | **R10-17a** | Right on Red Arrow After Stop | Mandatory (2B.60-01) | 30 x 36 | 30 x 36 | — | — | — | 36 x 48 | 2B-1 p.72 | — |
| ![R10-20aP](symbols/R10-20aP.png) | **R10-20aP** | MON—FRI (and times) | Optional (2B.60-05) | 24 x 18 | 24 x 18 | — | — | — | — | 2B-1 p.72 | — |
| ![R10-30](symbols/R10-30.png) | **R10-30** | Right Turn on Red Must | Mandatory (2B.60-01) | 30 x 36 | 30 x 36 | — | — | — | — | 2B-1 p.73 | — |

*Also governed by Section 2B.59:*

- [O] 2B.59-01 (p.131) ◆ R10-30: To supplement traffic signal control, traffic signal (R10-5 through R10-30) signs (see Figure 2B-28) may be used to regulate road users.
- [O] 2B.59-02 (p.131): Traffic signal signs may be installed at certain locations to clarify signal control. Among the legends that may be used for this purpose are: A. LEFT (RIGHT) ON GREEN ARROW ONLY (R10-5), B. STOP HERE ON RED (R10-6 or R10-6a) for observance of stop lines, C. DO NOT BLOCK INTERSECTION (R10-7) for avoidance of traffic obstructions, D. USE LANE(S) WITH GREEN ARROW (R10-8) for obedience to lane-use control signals (see Chapter 4T), E. LEFT (RIGHT) TURN SIGNAL (R10-10), F. U TURN SIGNAL (R10-10a) for exclusive control of a U-turn movement, G. U TURN YIELD TO RIGHT TURN (R10-16), H. LEFT (RIGHT) TURN YIELD ON GREEN (symbolic circular green) (R10-12), I. LEFT (RIGHT) TURN YIELD ON FLASHING YELLOW ARROW (R10-12a), and J. LEFT (RIGHT) TURN YIELD ON FLASHING RED ARROW AFTER STOP (R10-27).
- **[R]** 2B.59-03 (p.131): If used, the LEFT ON GREEN ARROW ONLY sign, the LEFT TURN SIGNAL sign, the LEFT TURN YIELD ON GREEN (symbolic circular green)) sign, the LEFT TURN YIELD ON FLASHING YELLOW ARROW sign, or the LEFT TURN YIELD ON FLASHING RED ARROW AFTER STOP) sign should be located adjacent to the left-turn signal face.
- **[R]** 2B.59-04 (p.131): If used, the RIGHT ON GREEN ARROW ONLY sign, the RIGHT TURN SIGNAL sign, the RIGHT TURN YIELD ON FLASHING YELLOW ARROW sign, or the RIGHT TURN YIELD ON FLASHING RED ARROW AFTER STOP sign should be located adjacent to the right-turn signal face.
- **[R]** 2B.59-05 (p.131): A U TURN YIELD TO RIGHT TURN (R10-16) sign should be installed near the left-turn signal face if U-turns are allowed on a protected left-turn movement on an approach from which a right-turn GREEN ARROW signal indication is simultaneously being displayed to drivers making a right turn from the conflicting approach to their left.
- [O] 2B.59-06 (p.131): If used, a U TURN SIGNAL (R10-10a) sign may be installed adjacent to the signal face that exclusively controls a U-turn movement.
- [O] 2B.59-07 (p.131): If needed for additional emphasis, an additional LEFT TURN YIELD ON GREEN (symbolic circular green) (R10-12) sign with an AT SIGNAL (R10-31P) supplemental plaque (see Figure 2B-28) may be installed in advance of the intersection.
- [O] 2B.59-08 (p.131): In situations where traffic control signals are coordinated for progressive timing, the Traffic Signal Speed (I1-1) sign may be used (see Section 2H.04).
- **[M]** 2B.59-09 (p.131): The CROSSWALK—STOP ON RED (symbolic circular red) (R10-23) and STOP ON STEADY REDYIELD ON FLASHING RED AFTER STOP (R10-23a) signs (see Figure 2B-28) shall only be used in conjunction with pedestrian hybrid beacons (see Section 4J.02).
- **[M]** 2B.59-10 (p.131): The EMERGENCY SIGNAL (R10-13) sign (see Figure 2B-28) shall be used in conjunction with emergency-vehicle traffic control signals (see Section 4M.02).
- **[M]** 2B.59-11 (p.131): The EMERGENCY SIGNAL—STOP ON FLASHING RED (R10-14 or R10-14a) sign (see Figure 2B-28) shall be used in conjunction with emergency-vehicle hybrid beacons (see Section 4N.02).
- [O] 2B.59-12 (p.131): If needed for extra emphasis, a STOP HERE ON FLASHING RED (R10-14b) sign may be installed with an emergency-vehicle hybrid beacon.
- **[M]** 2B.59-13 (p.131): The Left Turn Yield to Bicycles (R10-12b) sign shall be limited to applications where the conflicting bicyclist movement would be unexpected in direction, location, or similar condition that would tend to violate the expectation of a turning motorist.
- **[R]** 2B.59-14 (p.133): The Left Turn Yield to Bicycles sign should be located adjacent to the left-turn signal face.
- [O] 2B.59-16 (p.133): Where conditions might warrant additional emphasis to drivers turning at a signalized intersection where potential pedestrian conflicts might not be readily apparent, a Turning Vehicles Yield to (Stop for) Pedestrians (R10-15, R10-15a) sign (see Figure 2B-28) may be used.
- **[M]** 2B.59-17 (p.133): The Turning Vehicles Stop for Pedestrians (R10-15a) sign shall only be used in jurisdictions where laws, ordinances or resolutions specifically require that a driver must stop for a pedestrian.
- **[R]** 2B.59-18 (p.133): The R10-15 series signs, where used, should be placed as follows: A. On the near right corner of the signalized intersection for right-turning vehicles. B. On the far left corner of the signalized intersection for the left-turning vehicles onto a two-way street. C. On the near left corner of the signalized intersection for left-turning vehicles from a one-way street onto a one-way street.

- **[M]** 2B.60-01 (p.134) ◆ R10-11, R10-11a, R10-11b: Where a right turn on a circular red signal indication (or a left turn on a circular red signal indication from a one-way street to a one-way street) is to be prohibited, a NO TURN ON RED (R10-11, R10-11b) word message sign (see Figure 2B-28) shall be used. A NO TURN ON RED (symbolic circular red) (R10-11a) sign (see Figure 2B-28) shall be used when the approach is controlled by both circular red and red arrow indications.
- **[R]** 2B.60-02 (p.134): If used, the No Turn on Red sign should be installed near the appropriate signal head.
- **[R]** 2B.60-03 (p.134): A No Turn on Red sign should be considered when an engineering study finds that one or more of the following conditions exists: A. Inadequate sight distance to vehicles approaching from the left (or right, if applicable); B. Geometrics or operational characteristics of the intersection that might result in unexpected conflicts; C. An exclusive pedestrian or bicycle phase; D. An unacceptable number of conflicting pedestrian movements with right-turn-on-red maneuvers, especially involving children, older pedestrians, or persons with disabilities; E. More than three right-turn-on-red crashes reported in a 12-month period for the particular approach; or F. The skew angle of the intersecting roadways creates difficulty for drivers to see traffic approaching from their left (or right, if applicable).
- **[M]** 2B.60-04 (p.134) ◆ R10-11, R10-11a, R10-11b, R10-17a: If an R10-11, R10-11a, R10-11b, or R10-17a sign with conventional road size as shown in Table 2B-1 is used on an approach on the far side of the intersection and the distance between the stop line and the sign is greater than 120 feet, then a duplicate sign shall be located on the near side of the intersection to supplement the sign on the far side of the intersection.
- [O] 2B.60-05 (p.134) ◆ R10-20aP: When a no-turn-on-red restriction applies during certain time periods only, the following alternatives may be used: A. Movement Prohibition (R3-1, R3-2, R3-4, R3-18, and R3-27) signs or NO TURN ON RED signs displayed by using a blank-out sign for the time period or one or more portion(s) of a particular cycle of the traffic control signal during which the prohibition is applicable; or B. Static signs incorporating a supplemental legend or with a supplemental R10-20aP plaque (see Figure 2B28) showing the hours and days during which the prohibition is applicable.
- [O] 2B.60-06 (p.134): White LEDs may be used in the border and activated during periods of turn prohibition to enhance the sign conspicuity.
- [O] 2B.60-07 (p.134) ◆ R10-11c, R10-11d: On signalized approaches with more than one right-turn lane, a NO TURN ON RED EXCEPT FROM RIGHT LANE (R10-11c) sign (see Figure 2B-28) may be post-mounted at the intersection or a NO TURN ON RED FROM THIS LANE (with down arrow) (R10-11d) sign (see Figure 2B-28) may be mounted over the approximate center of the lane from which turns on red are prohibited.
- **[R]** 2B.60-08 (p.134) ◆ R10-17a: Where turns on red are permitted and the signal indication is a steady RED ARROW, the RIGHT (LEFT) ON RED ARROW AFTER STOP (R10-17a) sign (see Figure 2B-28) should be installed adjacent to the RED ARROW signal indication.
- [O] 2B.60-09 (p.134) ◆ R10-30: A RIGHT TURN ON RED MUST YIELD TO U-TURN (R10-30) sign (see Figure 2B-28) may be installed to remind road users that they must yield to conflicting U-turn traffic on the street or highway onto which they are turning right on a red signal after stopping.

<a id="sec-2B-61"></a>
#### Section 2B.61 Ramp Metering Signs (R10-28 and R10-29)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R10-28](symbols/R10-28.png) | **R10-28** | XX Vehicles per Green | Optional (2B.61-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2B-1 p.73 | — |
| ![R10-29](symbols/R10-29.png) | **R10-29** | XX Vehicles per Green Each Lane | Optional (2B.61-01) | 36 x 24 | 36 x 24 | — | — | — | — | 2B-1 p.73 | — |

- [O] 2B.61-01 (p.135): When ramp control signals (see Chapter 4P) are used to meter traffic on a freeway or expressway entrance ramp, regulatory signs with legends appropriate to the control may be installed adjacent to the ramp control signal faces.
- [O] 2B.61-02 (p.135): For entrance ramps with only one controlled lane, an XX VEHICLE(S) PER GREEN (R10-28) sign (see Figure 2B-29) may be used to inform road users of the number of vehicles that are permitted to proceed during each short display of the green signal indication. For entrance ramps with more than one controlled lane, an XX VEHICLE(S) PER GREEN EACH LANE (R10-29) (see Figure 2B-29) sign may be used to inform road users of the number of vehicles that are permitted to proceed from each lane during each short display of the green signal indication.

<a id="sec-2B-62"></a>
#### Section 2B.62 KEEP OFF MEDIAN Sign (R11-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R11-1](symbols/R11-1.png) | **R11-1** | Keep Off Median | Optional (2B.62-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2B-1 p.73 | — |

- [O] 2B.62-01 (p.136): The KEEP OFF MEDIAN (R11-1) sign (see Figure 2B-30) may be used to prohibit driving into or parking on the median.
- **[R]** 2B.62-02 (p.136): The KEEP OFF MEDIAN sign should be installed on the left-hand side of the roadway within the median at random intervals as needed wherever there is a tendency for encroachment.

<a id="sec-2B-63"></a>
#### Section 2B.63 ROAD CLOSED Sign (R11-2) and LOCAL TRAFFIC ONLY Signs (R11-3 Series, R11-4)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R11-2](symbols/R11-2.png) | **R11-2** | ROAD CLOSED Sign | Recommended (2B.63-01) | 48 x 30 | 48 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
|  | **R11-2a** | STREET CLOSED | Recommended (2B.63-01) | 48 x 30 | 48 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
|  | **R11-2b** | BRIDGE OUT | Recommended (2B.63-01) | 48 x 30 | 48 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
| ![R11-2c](symbols/R11-2c.png) | **R11-2c** | PATH CLOSED | Recommended (2B.63-01) | 48 x 30 | 48 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
| ![R11-3](symbols/R11-3.png) | **R11-3** | Road Closed - Local Traffic Only | Recommended (2B.63-01) | 60 x 30 | 60 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
| ![R11-3a](symbols/R11-3a.png) | **R11-3a** | LOCAL
TRAFFIC ONLY | Recommended (2B.63-01) | 60 x 30 | 60 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
| ![R11-3b](symbols/R11-3b.png) | **R11-3b** | BRIDGE OUT | Recommended (2B.63-01) | 60 x 30 | 60 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |
| ![R11-4](symbols/R11-4.png) | **R11-4** | ROAD CLOSED TO THRU TRAFFIC | Recommended (2B.63-01) | 60 x 30 | 60 x 30 | — | — | — | — | 2B-1 p.73 | 6G-1 |

- **[R]** 2B.63-01 (p.137) ◆ R11-2: The ROAD CLOSED (R11-2) sign should be installed where roads have been closed to all traffic (except authorized vehicles).
- **[R]** 2B.63-02 (p.137) ◆ R11-3, R11-4: ROAD CLOSED—LOCAL TRAFFIC ONLY (R11-3) or ROAD CLOSED TO THRU TRAFFIC (R11-4) signs should be used where through traffic is not permitted, or for a closure some distance beyond the sign, but where the highway is open for local traffic up to the point of closure.
- **[M]** 2B.63-03 (p.137) ◆ R11-2, R11-3, R11-3a, R11-3b, R11-4: The Road Closed (R11-2, R11-3 series, and R11-4) signs (see Figure 2B-30) shall be designed as horizontal rectangles. These signs shall be preceded by the applicable Advance Road Closed warning sign with the secondary legend AHEAD and, if applicable, an Advance Detour warning sign (see Section 6H.04).
- [O] 2B.63-04 (p.137): An intersecting street name or a well-known destination may be substituted for the XX MILES AHEAD legend in urban areas.
- [O] 2B.63-05 (p.137): The word message BRIDGE OUT may be substituted for the ROAD CLOSED legend where applicable. 06 Where conditions allow for bicycle travel on the road beyond the point of closure to motor vehicles, an EXCEPT BICYCLES (R3-7bP) plaque (see Figure 2B-4) may be used with the ROAD CLOSED sign.

*Also governed by Section 6G.04:*

- **[R]** 6G.04-01 (p.793) ◆ R11-2: The ROAD CLOSED (R11-2) sign (see Figure 6G-1) should be used when the roadway is closed to all road users except contractors’ equipment or officially authorized vehicles. The R11-2 sign should be accompanied by appropriate warning and detour signing.
- [O] 6G.04-02 (p.793) ◆ R11-2a, R11-2b, R11-2c: STREET CLOSED (R11-2a), BRIDGE OUT (R11-2b), or PATH CLOSED (R11-2c) signs may be substituted for Road Closed signs where applicable.
- **[R]** 6G.04-03 (p.793): Road Closed signs should be installed at or near the center of the roadway on or above a Type 3 Barricade that closes the roadway (see Section 6K.07).
- **[M]** 6G.04-04 (p.793): Road Closed signs shall not be used where road user flow is maintained through the TTC zone with a reduced number of lanes on the existing roadway or where the actual closure is some distance beyond the sign.

*Also governed by Section 6G.05:*

- **[R]** 6G.05-01 (p.793): The Local Traffic Only signs (see Figure 6G-1) should be used where road user flow detours to avoid a closure some distance beyond the sign, but where local road users can use the roadway to the point of closure. These signs should be accompanied by appropriate warning and detour signing.
- **[R]** 6G.05-02 (p.793) ◆ R11-3: In rural applications, the Local Traffic Only sign should have the legend ROAD CLOSED XX MILES AHEAD, LOCAL TRAFFIC ONLY (R11-3).
- [O] 6G.05-03 (p.793) ◆ R11-4: In urban areas, a ROAD (STREET) CLOSED TO THRU TRAFFIC (R11-4) sign or the legend ROAD CLOSED, LOCAL TRAFFIC ONLY may be used.
- [O] 6G.05-04 (p.793) ◆ R11-3: In urban areas, a word message that includes the name of an intersecting street name or well-known destination may be substituted for the words XX MILES AHEAD on the R11-3 sign where applicable.
- [O] 6G.05-05 (p.793) ◆ R11-3, R11-3a, R11-3b: A STREET CLOSED (R11-3a) or BRIDGE OUT (R11-3b) sign may be substituted for an R11-3 sign, where applicable.
- [O] 6G.05-06 (p.793) ◆ R11-4: The words BRIDGE OUT, BRIDGE CLOSED, or STREET CLOSED may be substituted for the words ROAD CLOSED on the R11-4 sign where applicable.

<a id="sec-2B-64"></a>
#### Section 2B.64 Weight Limit Signs (R12-1 through R12-7)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R12-1](symbols/R12-1.png) | **R12-1** | Weight Limit Signs | Mandatory (2B.64-01) | 24 x 30 | 24 x 30 | 36 x 48 | — | — | 36 x 48 | 2B-1 p.73 | 6G-1 |
| ![R12-2](symbols/R12-2.png) | **R12-2** | TONS
or AXLE WEIGHT LIMIT XX LBS | Mandatory (2B.64-01) | 24 x 30 | 24 x 30 | 36 x 48 | — | — | 36 x 48 | 2B-1 p.73 | 6G-1 |
| ![R12-4](symbols/R12-4.png) | **R12-4** | Weight Limit - Axle, Gross | Mandatory (2B.64-01) | 36 x 24 | 36 x 24 | — | — | — | — | 2B-1 p.73 | — |
| ![R12-5](symbols/R12-5.png) | **R12-5** | Weight Limit | Mandatory (2B.64-01) | 24 x 36 | 24 x 36 | 36 x 48 | 48 x 60 | — | — | 2B-1 p.73 | 6G-1 |
| ![R12-6](symbols/R12-6.png) | **R12-6** | Weight Limit - Specialized | Mandatory (2B.64-01) | 30 x 42 | 36 x 48 | 36 x 48 | 48 x 60 | — | 48 x 60 | 2B-1 p.73 | — |
| ![R12-7](symbols/R12-7.png) | **R12-7** | Weight Limit - Emergency Vehicles | Mandatory (2B.64-01) | 30 x 36 | 30 x 36 | 48 x 60 | 48 x 60 | — | 48 x 60 | 2B-1 p.73 | — |
| ![R12-7aP](symbols/R12-7aP.png) | **R12-7aP** | Weight Limit - Emergency | Mandatory (2B.64-01) | 30 x 30 | 30 x 30 | 48 x 48 | 48 x 48 | — | 48 x 48 | 2B-1 p.73 | — |

- **[M]** 2B.64-01 (p.137): Weight limit signs (see Figure 2B-30) shall be used to indicate a section of highway or structure that has a vehicle weight restriction.
- **[R]** 2B.64-02 (p.137): The units shown on any weight limit sign should be consistent within a State or region with respect to pounds or tons.
- [O] 2B.64-03 (p.137) ◆ R12-2: Where the restriction applies to axle weight rather than gross load, the legend AXLE WEIGHT LIMIT XX TONS or AXLE WEIGHT LIMIT XX LBS (R12-2) may be used.
- [O] 2B.64-04 (p.137) ◆ R12-4: In areas where multiple regulations are applicable, such as limiting both axle weight and gross vehicle weight, a WEIGHT LIMIT XX TONS PER AXLE, XX TONS GROSS (R12-4) sign combining the necessary messages on a single sign may be used.
- [O] 2B.64-05 (p.137) ◆ R12-5: Posting of specific load limits may be accomplished by use of the Weight Limit (R12-5) symbol sign. A sign containing the legend WEIGHT LIMIT on the top two lines, and showing up to three different truck symbols and their respective weight limits for which restrictions apply may be used, with the weight limits displayed to the right of each symbol as XX T. A bottom line of legend stating GROSS WT may be included if needed for enforcement purposes.
- [O] 2B.64-07 (p.137) ◆ R12-6: The Weight Limit (R12-6) sign may be used to indicate vehicle weight restrictions for specialized hauling vehicles.
- **[M]** 2B.64-08 (p.137) ◆ R12-5, R12-6: The symbols shown on the R12-5 and R12-6 Weight Limit sign shall apply to all trucks of that configuration (single-unit, single-trailer or multi-trailer) regardless of the shape of the vehicle. Symbolic representations of other vehicle shapes or modifications of standard symbols shall not be used.
- [O] 2B.64-09 (p.137): The facility type (such as “BRIDGE”) may be added to the legend of the sign to clarify the specific applicability of the weight limit.
- **[M]** 2B.64-10 (p.138) ◆ R12-5: If the R12-5 sign depicts only one single-unit vehicle symbol, the weight limit associated with that singleunit vehicle symbol shall apply to all single-unit vehicles, regardless of number of axles.
- **[M]** 2B.64-11 (p.138): The weight limit associated with the single-trailer vehicle symbol shall apply to all single-trailer vehicles, regardless of number of axles or vehicle shape.
- **[M]** 2B.64-12 (p.138): The weight limit associated with the multi-trailer vehicle symbol shall apply to all multi-trailer vehicles with two or more trailers, regardless of number of axles or vehicle shape.
- **[M]** 2B.64-13 (p.138): A weight limit sign (see Figure 2B-30) shall be located at the applicable section of highway or structure.
- **[M]** 2B.64-14 (p.138): An additional weight limit sign, with an advisory distance or directional legend, shall be located in advance of the applicable section of highway or structure so that prohibited vehicles can detour or turn around prior to the limit zone.
- [O] 2B.64-16 (p.138) ◆ R12-7: The Emergency Vehicle Weight Limit (R12-7) sign carrying the legend EMERGENCY VEHICLE WEIGHT LIMIT SINGLE AXLE XX TONS, TANDEM XX TONS, and GROSS XX TONS may be used to indicate vehicle weight restrictions for emergency vehicles.
- **[M]** 2B.64-17 (p.138) ◆ R12-7aP: When the emergency-vehicle weight limit is displayed in the same assembly as the primary weight limit sign, the Emergency Vehicle Weight Limit (R12-7aP) plaque shall be mounted below.

*Also governed by Section 6G.06:*

- **[M]** 6G.06-01 (p.795): A Weight Limit sign (see Figure 6G-1), which shows the gross weight or axle weight that is permitted on the roadway or bridge, shall be consistent with State or local regulations and shall not be installed without the approval of the authority having jurisdiction over the highway.
- **[M]** 6G.06-02 (p.795): When weight restrictions are imposed because of the activity in a TTC zone, a marked detour shall be provided for vehicles weighing more than the posted limit.

<a id="sec-2B-65"></a>
#### Section 2B.65 Weigh Station Sign (R13-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R13-1](symbols/R13-1.png) | **R13-1** | Weigh Station | Recommended (2B.65-01) | 72 x 54 | 72 x 54 | 96 x 72 | 132 x 90 | — | — | 2B-1 p.73 | — |

- **[R]** 2B.65-01 (p.138): An R13-1 sign with the legend TRUCKS OVER XX TONS MUST ENTER WEIGH STATION NEXT RIGHT (see Figure 2B-31) should be used to direct appropriate traffic into an inspection station.
- **[R]** 2B.65-02 (p.138): The R13-1 sign should be supplemented by the D8 series of guide signs (see Section 2D.51).

<a id="sec-2B-66"></a>
#### Section 2B.66 TRUCK ROUTE Sign (R14-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R14-1](symbols/R14-1.png) | **R14-1** | Truck Route | Recommended (2B.66-01) | 24 x 18 | 24 x 18 | — | — | — | — | 2B-1 p.73 | — |

- **[R]** 2B.66-01 (p.138): The TRUCK ROUTE (R14-1) sign (see Figure 2B-31) should be used to mark a route that has been designated to allow truck traffic.

<a id="sec-2B-67"></a>
#### Section 2B.67 Hazardous Material Signs (R14-2 and R14-3)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R14-2](symbols/R14-2.png) | **R14-2** | Hazardous Material | Optional (2B.67-01) | 24 x 24 | 24 x 24 | 30 x 30 | 36 x 36 | — | 42 x 42 | 2B-1 p.73 | — |
| ![R14-3](symbols/R14-3.png) | **R14-3** | Hazardous Material | Optional (2B.67-01) | 24 x 24 | 24 x 24 | 30 x 30 | 36 x 36 | — | 42 x 42 | 2B-1 p.73 | — |

- [O] 2B.67-01 (p.138) ◆ R14-2: The Hazardous Material Route (R14-2) sign (see Figure 2B-31) may be used to identify routes that have been designated by proper authority for vehicles transporting hazardous material.
- [O] 2B.67-02 (p.138) ◆ R14-3: On routes where the transporting of hazardous material is prohibited, the Hazardous Material Prohibition (R14-3) sign (see Figure 2B-31) may be used.
- **[R]** 2B.67-03 (p.138): If used, the Hazardous Material Prohibition sign should be installed on a street or roadway at a point where vehicles transporting hazardous material have the opportunity to take an alternate route.

<a id="sec-2B-68"></a>
#### Section 2B.68 National Network Signs (R14-4 and R14-5)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R14-4](symbols/R14-4.png) | **R14-4** | National Network | Mandatory (2B.68-02) | 30 x 30 | 30 x 30 | 36 x 36 | 36 x 36 | — | 42 x 42 | 2B-1 p.73 | — |
| ![R14-5](symbols/R14-5.png) | **R14-5** | National Network | Mandatory (2B.68-02) | 30 x 30 | 30 x 30 | 36 x 36 | 36 x 36 | — | 42 x 42 | 2B-1 p.73 | — |

- **[M]** 2B.68-02 (p.139) ◆ R14-4: When a National Network route is signed, the National Network (R14-4) sign (see Figure 2B-31) shall be used.
- [O] 2B.68-03 (p.139) ◆ R14-5: The National Network Prohibition (R14-5) sign (see Figure 2B-31) may be used to identify routes, portions of routes, and ramps where trucks are prohibited. The R14-5 sign may also be used to mark the ends of designated routes.

<a id="sec-2B-69"></a>
#### Section 2B.69 Photo Enforced Signs and Plaques (R10-18, R10-18a, R10-19P, R10-19aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R10-18](symbols/R10-18.png) | **R10-18** | Traffic Laws Photo Enforced | Optional (2B.69-01) | 36 x 24 | 36 x 24 | 48 x 30 | 54 x 36 | — | 54 x 36 | 2B-1 p.72 | — |
| ![R10-18a](symbols/R10-18a.png) | **R10-18a** | Traffic Signal Photo Enforced | Optional (2B.69-01) | 30 x 42 | 30 x 42 | 30 x 42 | — | — | 36 x 54 | 2B-1 p.72 | — |
| ![R10-19P](symbols/R10-19P.png) | **R10-19P** | Photo Enforced (symbol plaque) | Optional (2B.69-01) | 24 x 12 | 24 x 12 | 36 x 18 | 48 x 24 | — | 48 x 24 | 2B-1 p.72 | — |
| ![R10-19aP](symbols/R10-19aP.png) | **R10-19aP** | Photo Enforced (plaque) | Optional (2B.69-01) | 24 x 18 | 24 x 18 | 36 x 24 | 48 x 36 | — | 48 x 36 | 2B-1 p.72 | — |

- [O] 2B.69-01 (p.140) ◆ R10-18: A Traffic Laws Photo Enforced (R10-18) sign (see Figure 2B-32) may be installed at a jurisdictional boundary to advise road users that some of the traffic regulations within that jurisdiction are being enforced by photographic equipment.
- [O] 2B.69-02 (p.140) ◆ R10-18a: A Traffic Signal Photo Enforced (R10-18a) sign (see Figure 2B-32) may be installed in advance of or at a traffic signal to advise road users that compliance with the signal is enforced by photographic equipment. A Signal Ahead (W3-3) sign and a Traffic Signal Photo Enforced (R10-18a) sign may be used on the same approach provided that they are on separate supports.
- [O] 2B.69-03 (p.140) ◆ R10-19P, R10-19aP: A Photo Enforced (R10-19P) plaque or a PHOTO ENFORCED (R10-19aP) word message plaque (see Figure 2B-32) may be mounted below a regulatory sign to advise road users that the regulation is being enforced by photographic equipment.
- **[M]** 2B.69-04 (p.140) ◆ R10-18a: The Traffic Signal Photo Enforced (R10-18a) sign shall not be installed on approaches to signalized locations where red-light cameras are not present on any of the approaches to the signalized location.
- **[M]** 2B.69-05 (p.140) ◆ R10-18a: A Traffic Signal Photo Enforced (R10-18a) sign shall not be installed on the same support in combination with a Signal Ahead (W3-3) sign.
- **[M]** 2B.69-06 (p.140) ◆ R10-19P, R10-19aP: If used below a regulatory sign, the Photo Enforced (R10-19P or R10-19aP) plaque shall be a rectangle with a black legend and border on a white background.

<a id="sec-2B-70"></a>
#### Section 2B.70 Move Vehicles from Travel Lanes Sign (R16-4)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R16-4](symbols/R16-4.png) | **R16-4** | Minor Crashes Move Vehicles from | Optional (2B.70-01) | — | 60 x 42 | 84 x 54 | 96 x 60 | — | 84 x 54 | 2B-1 p.73 | — |

- [O] 2B.70-01 (p.140): A STATE LAW MINOR CRASHES MOVE VEHICLES FROM TRAVEL LANES (R16-4) sign (see Figure 2B-33) may be installed in accordance with the provisions of Section 2A.01 to require motorists to move their vehicle out of the travel lanes if they have been involved in a crash.
- [O] 2B.70-02 (p.140): If the specific requirements of a State law vary, the word legend of the R16-4 sign may be modified to reflect the appropriate law.

<a id="sec-2B-71"></a>
#### Section 2B.71 Move Over or Reduce Speed Sign (R16-3)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R16-3](symbols/R16-3.png) | **R16-3** | Move Over or Reduce Speed | Optional (2B.71-01) | — | 60 x 48 | 84 x 60 | 102 x 72 | — | 84 x 60 | 2B-1 p.73 | — |

- [O] 2B.71-01 (p.141): A STATE LAW MOVE OVER OR REDUCE SPEED FOR VEHICLES STOPPED ON SHOULDER (R16-3) sign (see Figure 2B-33) may be installed in accordance with the provisions of Section 2A.01 to require motorists to change lanes and/or reduce speed when passing stopped emergency vehicles on the shoulder.
- [O] 2B.71-02 (p.141): If the specific requirements of a State law vary, the word legend of the R16-3 sign may be modified to reflect the appropriate law.

<a id="sec-2B-72"></a>
#### Section 2B.72 No Hand-Held Phone Use by Driver Signs (R16-15 and R16-15a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R16-15](symbols/R16-15.png) | **R16-15** | No Hand-Held Phone Use By Driver | Optional (2B.72-01) | — | — | 72 x 48 | 72 x 48 | — | — | 2B-1 p.73 | — |
| ![R16-15a](symbols/R16-15a.png) | **R16-15a** | No Hand-Held Phone Use By Driver | Optional (2B.72-01) | 30 x 42 | 30 x 42 | — | — | — | — | 2B-1 p.73 | — |

- [O] 2B.72-01 (p.141): A STATE LAW NO HAND-HELD PHONE USE BY DRIVER (R16-15 or R16-15a) sign (see Figure 2B-33) may be installed in accordance with the provisions of Section 2A.01 to notify drivers that they are prohibited from using hand-held telephones while driving.
- [O] 2B.72-02 (p.141): If the specific requirements of a State law vary, the word legend of the R16-15 series signs may be modified to reflect the appropriate law.

<a id="sec-2B-73"></a>
#### Section 2B.73 Headlight Use Signs (R16-5 through R16-11)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R16-5](symbols/R16-5.png) | **R16-5** | Lights On When Using Wipers | Optional (2B.73-03) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.73 | — |
| ![R16-6](symbols/R16-6.png) | **R16-6** | LIGHTS ON WHEN RAINING | Optional (2B.73-03) | 24 x 30 | 24 x 30 | 36 x 48 | 48 x 60 | — | 36 x 48 | 2B-1 p.73 | — |
| ![R16-7](symbols/R16-7.png) | **R16-7** | Turn On Headlights Next XX Miles | Optional (2B.73-03) | 60 x 18 | 60 x 18 | 96 x 30 | 132 x 36 | — | 96 x 30 | 2B-1 p.73 | — |
| ![R16-8](symbols/R16-8.png) | **R16-8** | Turn On, Check Headlights | Optional (2B.73-03) | 42 x 18 | 42 x 18 | 60 x 30 | 78 x 36 | — | 60 x30 | 2B-1 p.73 | — |
| ![R16-9](symbols/R16-9.png) | **R16-9** | Turn On, Check Headlights | Optional (2B.73-03) | 42 x 18 | 42 x 18 | 60 x 30 | 78 x 36 | — | 60 x30 | 2B-1 p.73 | — |
| ![R16-10](symbols/R16-10.png) | **R16-10** | BEGIN DAYTIME
HEADLIGHT SECTION | Optional (2B.73-03) | 60 x 18 | 60 x 18 | 96 x 30 | 120 x 36 | — | 96 x 30 | 2B-1 p.73 | — |
| ![R16-11](symbols/R16-11.png) | **R16-11** | END
DAYTIME HEADLIGHT SECTION | Optional (2B.73-03) | 60 x 18 | 60 x 18 | 96 x 30 | 120 x 36 | — | 96 x 30 | 2B-1 p.73 | — |

- [O] 2B.73-03 (p.141) ◆ R16-5, R16-6: A LIGHTS ON WHEN USING WIPERS (R16-5) sign or a LIGHTS ON WHEN RAINING (R16-6) sign may be installed in accordance with the provisions of Section 2A.01 to inform road users of State laws regarding headlight use. Although these signs are typically installed facing traffic entering the State just inside the State border, they also may be installed at other locations within the State.
- **[R]** 2B.73-04 (p.141) ◆ R16-7, R16-10, R16-11: If a particular section of roadway has been designated as a safety improvement zone within which headlight use is required, a TURN ON HEADLIGHTS NEXT XX MILES (R16-7) sign or a BEGIN DAYTIME HEADLIGHT SECTION (R16-10) sign should be installed at the upstream end of the section, and an END DAYTIME HEADLIGHT SECTION (R16-11) sign should be installed at the downstream end of the section.
- [O] 2B.73-05 (p.141) ◆ R16-8, R16-9: A TURN ON HEADLIGHTS (R16-8) sign may be installed to require road users to turn on their headlights in special situations such as when driving through a tunnel. A CHECK HEADLIGHTS (R16-9) sign may be installed downstream from the special situation to inform drivers that using their headlights is no longer required.

### Chapter 2C Warning Signs and Object Markers

<a id="sec-2C-07"></a>
#### Section 2C.07 Horizontal Alignment Signs (W1-1 through W1-5, W1-11, and W1-15)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W1-1](symbols/W1-1.png) | **W1-1** | Turn | Recommended (2C.07-02) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | — | 48 x 48 | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W1-2](symbols/W1-2.png) | **W1-2** | Curve | Recommended (2C.07-02) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | — | 48 x 48 | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W1-3](symbols/W1-3.png) | **W1-3** | Reverse Turn | Recommended (2C.07-02) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | — | 48 x 48 | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W1-4](symbols/W1-4.png) | **W1-4** | Reverse Curve | Recommended (2C.07-02) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | — | 48 x 48 | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W1-5](symbols/W1-5.png) | **W1-5** | Winding Road | Recommended (2C.07-02) | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | — | 48 x 48 | 2C-1 p.148 | 9A-1 |
| ![W1-11](symbols/W1-11.png) | **W1-11** | Hairpin Curve | Recommended (2C.07-02) | 30 x 30 | 30 x 30 | 36 x 36 | 48 x 48 | — | 48 x 48 | 2C-1 p.148 | — |
| ![W1-15](symbols/W1-15.png) | **W1-15** | 270-degree Curve | Recommended (2C.07-02) | 30 x 30 | 30 x 30 | 36 x 36 | 48 x 48 | — | 48 x 48 | 2C-1 p.148 | — |

- **[M]** 2C.07-01 (p.155) ◆ W1-2: If Table 2C-4 indicates that a horizontal alignment sign (see Figure 2C-1) is required, recommended, or allowed, the sign installed in advance of the curve shall be a Curve (W1-2) sign unless a different sign is recommended or allowed by the provisions of this Section.
- **[R]** 2C.07-02 (p.155) ◆ W1-1, W1-2: A Turn (W1-1) sign should be used instead of a Curve (W1-2) sign in advance of a horizontal curve that has an advisory speed of 30 mph or less.
- **[R]** 2C.07-03 (p.155) ◆ W1-1, W1-2, W1-3, W1-4: Where there are two changes in roadway alignment in opposite directions that are separated by a tangent distance of less than 600 feet, the Reverse Turn (W1-3) sign should be used instead of multiple Turn (W1-1) signs or the Reverse Curve (W1-4) sign should be used instead of multiple Curve (W1-2) signs.
- [O] 2C.07-05 (p.155) ◆ W1-1, W1-2, W1-5: A Winding Road (W1-5) sign may be used instead of multiple Turn (W1-1) or Curve (W1-2) signs where there are three or more changes in roadway alignment each separated by a tangent distance of less than 600 feet.
- [O] 2C.07-06 (p.155): A NEXT XX MILES (W7-3aP) supplemental distance plaque (see Section 2C.61) may be installed below the Winding Road sign where continuous roadway curves exist for a specific distance.
- [O] 2C.07-07 (p.158) ◆ W1-11: If the curve has a change in horizontal alignment of 135 degrees or more, the Hairpin Curve (W1-11) sign may be used instead of a Turn or Curve sign.
- [O] 2C.07-08 (p.158) ◆ W1-15: If the curve has a change of direction of approximately 270 degrees, such as on a cloverleaf interchange ramp, the 270-degree Loop (W1-15) sign may be used instead of a Turn or Curve sign.
- **[R]** 2C.07-09 (p.158): When the Hairpin Curve sign or the 270-degree Loop sign is installed, either a One-Direction Large Arrow (W1-6) sign or Chevron Alignment (W1-8) signs should be installed on the outside of the turn or curve.

*Also governed by Section 2C.09:*

- [O] 2C.09-01 (p.158) ◆ W1-1: The Turn (W1-1) sign, the Curve (W1-2) sign, and the Reverse Curve (W1-4) sign may be combined with the Cross Road (W2-1) sign or the Side Road (W2-2 or W2-3) sign to create a combination Horizontal Alignment/ Intersection (W1-10 series) sign (see Figure 2C-1) that depicts the condition where an intersection occurs within or immediately adjacent to a turn or curve.
- **[R]** 2C.09-03 (p.159): Elements of the combination Horizontal Alignment/Intersection sign related to horizontal alignment should comply with the provisions of Section 2C.07, and elements related to intersection configuration should comply with the provisions of Section 2C.41. The symbol design should approximate the configuration of the intersecting roadway(s). No more than one Cross Road or two Side Road symbols should be displayed on any one combination Horizontal Alignment/Intersection sign.
- **[M]** 2C.09-04 (p.159): The use of the combination Horizontal Alignment/Intersection sign shall be in accordance with the provisions of Section 2C.07 for the appropriate Turn or Curve sign .

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065) ◆ W1-1, W1-2, W1-3, W1-4, W1-5: To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065) ◆ W1-1, W1-2, W1-3, W1-4, W1-5: The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-2C-08"></a>
#### Section 2C.08 Chevron Alignment Sign (W1-8)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W1-8](symbols/W1-8.png) | **W1-8** | Chevron Alignment | Optional (2C.08-02) · *Auto* | 18 x 24 | 18 x 24 | 30 x 36 | 36 x 48 | — | 24 x 30 | 2C-1 p.148 | 6H-1 |

- **[M]** 2C.08-01 (p.158): The use of the Chevron Alignment (W1-8) sign (see Figures 2C-1 and 2C-2) to provide additional emphasis and guidance for a change in horizontal alignment shall be in accordance with the information shown in Table 2C-4.
- [O] 2C.08-02 (p.158): Chevron Alignment signs may be used instead of or in addition to standard delineators.
- **[M]** 2C.08-03 (p.158): The Chevron Alignment sign shall be a vertical rectangle. No border shall be used on the Chevron Alignment sign.
- **[M]** 2C.08-04 (p.158): If used, Chevron Alignment signs shall be installed on the outside of a turn or curve, in line with and at approximately a right angle to approaching traffic. Chevron Alignment signs shall be installed at a minimum height of 4 feet, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way.
- **[R]** 2C.08-05 (p.158): The approximate spacing of Chevron Alignment signs on the turn or curve measured from the point of curvature (PC) should be as shown in Table 2C-5.
- **[R]** 2C.08-06 (p.158): The Chevron Alignment signs should be visible for a sufficient distance to provide the road user with adequate time to react to the change in alignment.
- [O] 2C.08-07 (p.158): LEDs may be used to enhance the conspicuity of Chevron Alignment signs (see Section 2A.12).
- **[M]** 2C.08-08 (p.158): The LEDs used in the Chevron Alignment sign shall consist of yellow LEDs outlining the chevron symbol.
- **[M]** 2C.08-09 (p.158): Chevron Alignment signs shall not be placed on the far side of a T-intersection facing traffic on the stem approach to warn drivers that a through movement is not physically possible, as this is the function of a Two-Direction (or One-Direction) Large Arrow sign.
- **[M]** 2C.08-10 (p.158): Chevron Alignment signs shall not be used to mark obstructions within or adjacent to the roadway, including the beginning of guardrails or barriers, as this is the function of an object marker (see Section 2C.70).
- **[M]** 2C.08-11 (p.158): Chevron Alignment signs directing traffic to the right shall not be used in the central island of a roundabout or a neighborhood traffic circle.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065): To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065): The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-2C-09"></a>
#### Section 2C.09 Combination Horizontal Alignment/Intersection Signs (W1-10 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W1-10](symbols/W1-10.png) | **W1-10** | Combination Horizontal | Optional | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | — | 2C-1 p.148 | — |
| ![W1-10a](symbols/W1-10a.png) | **W1-10a** | Combination Horizontal | Optional | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | — | 2C-1 p.148 | — |
| ![W1-10b](symbols/W1-10b.png) | **W1-10b** | Combination Horizontal | Optional | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | — | 2C-1 p.148 | — |
| ![W1-10c](symbols/W1-10c.png) | **W1-10c** | Combination Horizontal Alignment/Intersection Signs (W1-10 Series) | Optional | — | — | — | — | — | — | text | — |
| ![W1-10d](symbols/W1-10d.png) | **W1-10d** | Combination Horizontal Alignment/Intersection Signs (W1-10 Series) | Optional | — | — | — | — | — | — | text | — |
| ![W1-10e](symbols/W1-10e.png) | **W1-10e** | Combination Horizontal Alignment/Intersection Signs (W1-10 Series) | Optional | — | — | — | — | — | — | text | — |

- [O] 2C.09-01 (p.158): The Turn (W1-1) sign, the Curve (W1-2) sign, and the Reverse Curve (W1-4) sign may be combined with the Cross Road (W2-1) sign or the Side Road (W2-2 or W2-3) sign to create a combination Horizontal Alignment/ Intersection (W1-10 series) sign (see Figure 2C-1) that depicts the condition where an intersection occurs within or immediately adjacent to a turn or curve.
- **[R]** 2C.09-03 (p.159): Elements of the combination Horizontal Alignment/Intersection sign related to horizontal alignment should comply with the provisions of Section 2C.07, and elements related to intersection configuration should comply with the provisions of Section 2C.41. The symbol design should approximate the configuration of the intersecting roadway(s). No more than one Cross Road or two Side Road symbols should be displayed on any one combination Horizontal Alignment/Intersection sign.
- **[M]** 2C.09-04 (p.159): The use of the combination Horizontal Alignment/Intersection sign shall be in accordance with the provisions of Section 2C.07 for the appropriate Turn or Curve sign .

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065): To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065): The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-2C-10"></a>
#### Section 2C.10 One-Direction Large Arrow Sign (W1-6)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W1-6](symbols/W1-6.png) | **W1-6** | One-Direction Large Arrow | Optional (2C.10-01) · *Auto* | 48 x 24 | 48 x 24 | 60 x 30 | 60 x 30 | — | 60 x 30 | 2C-1 p.148 | 9A-1, 6H-1 |

- [O] 2C.10-01 (p.159): A One-Direction Large Arrow (W1-6) sign (see Figure 2C-1) may be used either as a supplement or alternative to Chevron Alignment signs or delineators in order to delineate a change in horizontal alignment (see Figure 2C-2).
- [O] 2C.10-02 (p.159): A One-Direction Large Arrow (W1-6) sign may be used to supplement a Turn (W1-1) or Reverse Turn (W1-3) sign (see Figure 2C-2) to emphasize the abrupt curvature.
- **[M]** 2C.10-03 (p.159): The One-Direction Large Arrow sign shall be a horizontal rectangle with an arrow pointing to the left or right.
- **[M]** 2C.10-04 (p.159): If used, the One-Direction Large Arrow sign shall be installed on the outside of a turn or curve in line with and at approximately a right angle to approaching traffic.
- **[M]** 2C.10-05 (p.159): The One-Direction Large Arrow sign shall not be used where there is no alignment change in the direction of travel, such as at the beginnings and ends of medians or at center piers.
- **[M]** 2C.10-06 (p.159): The One-Direction Large Arrow sign directing traffic to the right shall not be used in the central island of a roundabout or a neighborhood traffic circle.
- **[R]** 2C.10-07 (p.159): The One-Direction Large Arrow sign should be visible for a sufficient distance to provide the road user with adequate time to react to the change in alignment.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065): To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065): The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-2C-11"></a>
#### Section 2C.11 Truck Rollover Sign (W1-13)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W1-13](symbols/W1-13.png) | **W1-13** | Truck Rollover | Optional (2C.11-01) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 2C-1 p.148 | — |

- [O] 2C.11-01 (p.159): A Truck Rollover (W1-13) sign (see Figure 2C-1) may be used as a supplement to a horizontal alignment warning sign to warn drivers of vehicles with a high center of gravity, such as trucks, tankers, and recreational vehicles, of a curve or turn where there are: A. Past incidents of truck rollovers at the specific location, B. High volumes of trucks, or C. A speed differential (see Section 2C.06) that might pose a greater risk for vehicles with high centers of gravity.
- **[R]** 2C.11-02 (p.159): Where engineering judgment determines the need for the installation of a Truck Rollover (W1-13) sign, it should be located downstream of the horizontal alignment warning sign in advance of the curve.
- **[M]** 2C.11-03 (p.159): If a Truck Rollover (W1-13) sign is used, it shall be accompanied by an Advisory Speed (W13-1P) plaque indicating the recommended speed for vehicles with a higher center of gravity.
- [O] 2C.11-04 (p.159): The Truck Rollover sign may include conspicuity enhancements, or may be a blank-out sign, activated by the detection of an approaching vehicle with a high center of gravity that is traveling in excess of the recommended speed for the condition.

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065): To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065): The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-2C-12"></a>
#### Section 2C.12 Advisory Exit and Ramp Speed Signs (W13-2 and W13-3) and Combination Horizontal Alignment/Advisory Exit and Ramp Speed Signs (W13-6 through W13-13)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W13-2](symbols/W13-2.png) | **W13-2** | Advisory Exit Speed | Mandatory (2C.12-01) | 24 x 30 | 24 x 30 | 36 x 48 | 36 x 48 | — | 48 x 60 | 2C-1 p.150 | — |
| ![W13-3](symbols/W13-3.png) | **W13-3** | Advisory Exit or Ramp Speed | Mandatory (2C.12-01) | 24 x 30 | 24 x 30 | 36 x 48 | 36 x 48 | — | 48 x 60 | 2C-1 p.150 | — |
| ![W13-6](symbols/W13-6.png) | **W13-6** | Advisory Exit Speed | Mandatory (2C.12-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | 48 x 84 | 2C-1 p.150 | — |
| ![W13-7](symbols/W13-7.png) | **W13-7** | Advisory Ramp Speed | Mandatory (2C.12-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | 48 x 84 | 2C-1 p.150 | — |
| ![W13-8](symbols/W13-8.png) | **W13-8** | Alignment/Advisory Exit or | Mandatory (2C.12-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | 48 x 84 | 2C-1 p.150 | — |
| ![W13-9](symbols/W13-9.png) | **W13-9** | Alignment/Advisory Exit or | Mandatory (2C.12-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | 48 x 84 | 2C-1 p.150 | — |
| ![W13-10](symbols/W13-10.png) | **W13-10** | Alignment/Advisory Exit or | Mandatory (2C.12-01) | 24 x 36 | 24 x 36 | 36 x 54 | 36 x 54 | — | 48 x 72 | 2C-1 p.150 | — |
| ![W13-11](symbols/W13-11.png) | **W13-11** | Alignment/Advisory Exit or | Mandatory (2C.12-01) | 24 x 36 | 24 x 36 | 36 x 54 | 36 x 54 | — | 48 x 72 | 2C-1 p.150 | — |
| ![W13-12](symbols/W13-12.png) | **W13-12** | Alignment/Advisory Exit or | Mandatory (2C.12-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | 48 x 84 | 2C-1 p.150 | — |
| ![W13-13](symbols/W13-13.png) | **W13-13** | Alignment/Advisory Exit or | Mandatory (2C.12-01) | 24 x 42 | 24 x 42 | 36 x 66 | 36 x 66 | — | 48 x 84 | 2C-1 p.150 | — |

- **[M]** 2C.12-01 (p.160) ◆ W13-2: Where an advisory speed is posted in advance of a freeway or expressway exit, the Advisory Exit Speed (W13-2) sign (see Figure 2C-1) shall be used.
- **[M]** 2C.12-02 (p.160) ◆ W13-3: Where an advisory speed is posted in advance of a conventional road ramp or to another roadway or roadside facility, the Advisory Ramp Speed (W13-3) sign (see Figure 2C-1) shall be used.
- **[M]** 2C.12-03 (p.160): An Advisory Exit Speed or Advisory Ramp Speed sign shall be used when the difference between the mainline roadway speed limit and the exit or ramp advisory speed in the vicinity of the departure is 20 mph or greater.
- **[R]** 2C.12-04 (p.160): An Advisory Exit Speed or Advisory Ramp Speed sign should be used when the difference between the mainline roadway speed limit and the exit or ramp advisory speed in the vicinity of the departure is 15 mph.
- [O] 2C.12-05 (p.160): An Advisory Exit Speed or Advisory Ramp Speed sign may be used based on engineering judgment when the difference between the mainline roadway speed limit and the exit or ramp advisory speed in the vicinity of the departure is 10 mph or less.
- [O] 2C.12-06 (p.160) ◆ W13-2, W13-3, W13-6, W13-7, W13-8, W13-9, W13-10, W13-11: The Combination Horizontal Alignment/Advisory Exit Speed (W13-6, W13-8, and W13-10) signs (see Figure 2C-1) may be used in lieu of the Advisory Exit Speed (W13-2) sign, and the combination Horizontal Alignment/ Advisory Ramp Speed (W13-7, W13-9, and W13-11) signs (see Figure 2C-1) may be used in lieu of the Advisory Ramp Speed (W13-3) sign.
- [O] 2C.12-07 (p.160) ◆ W13-2, W13-3, W13-12, W13-13: The Combination Truck Rollover/Advisory Exit Speed and Truck Rollover/Advisory Ramp Speed (W13-12 and W13-13) signs (see Figure 2C-1) may be used in lieu of the W13-2 and W13-3 signs, respectively, if the tip over condition is in the vicinity of the gore.
- **[M]** 2C.12-08 (p.160): Roadway geometrics represented on the Combination Horizontal Alignment/Advisory Exit and Combination Horizontal Alignment/Advisory Ramp Speed signs (see Figure 2C-1) shall be limited to the standard signs shown in this Manual.
- **[R]** 2C.12-09 (p.160): If used, the Advisory Exit Speed sign or the Combination Horizontal Alignment/Advisory Exit Speed sign should be installed along the deceleration lane. The Advisory Exit Speed or the Combination Horizontal Alignment/Advisory Exit signs should be visible in time for the road user to decelerate and make an exiting maneuver.
- **[R]** 2C.12-10 (p.160): Regulatory Speed Limit signs (see Section 2B.21) should not be located in the vicinity of exit ramps or deceleration lanes, particularly where they will conflict with the advisory speed displayed on the Advisory Exit or Ramp Speed signs.
- [O] 2C.12-13 (p.160): Where there is a need to remind road users of the recommended advisory speed, a horizontal alignment warning sign with an advisory speed plaque displaying the same advisory speed may be installed at a downstream location along the ramp.
- **[R]** 2C.12-14 (p.160): If the ramp curvature changes to the extent that it warrants a lower advisory speed, a horizontal alignment warning sign with the new advisory speed should be displayed in advance of the change in curvature.
- [O] 2C.12-15 (p.160): The One-Direction Large Arrow (W1-6) sign may be installed beyond the exit gore on the outside of the curve to provide additional warning of an immediate change in curvature. When used in conjunction with the exit speed, the One-Direction Large Arrow (W1-6) sign may be supplemented with a Confirmation Advisory Speed (W13-1aP) plaque (see Figure 2C-1) when the plaque is not used with the Exit Gore (E5-1 series) sign.
- **[R]** 2C.12-16 (p.161): The horizontal alignment symbol displayed on the Combination Horizontal Alignment/Advisory Exit and Ramp Speed signs should be consistent with the horizontal geometry of the ramp.

<a id="sec-2C-13"></a>
#### Section 2C.13 Vehicle Speed Feedback Sign and Plaque (W13-20 and W13-20aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **W13-20** | Vehicle Speed Feedback Sign | Optional (2C.13-01) | 24 x 30 | 30 x 36 | 36 x 48 | 48 x 60 | — | — | 2C-1 p.150 | — |
|  | **W13-20aP** | Vehicle Speed Feedback (plaque) | Optional (2C.13-01) | 24 x 18 | 30 x 24 | 36 x 30 | 48 x 36 | — | — | 2C-1 p.150 | — |

- [O] 2C.13-01 (p.166): A Vehicle Speed Feedback (W13-20) sign or (W13-20aP) plaque (see Figure 2C-4) that displays the speed of an approaching vehicle to the vehicle operator may be used to provide warning to drivers of their speed in relation to either a speed limit (R2-1) sign or a horizontal alignment warning sign assembly with a posted advisory speed.
- **[M]** 2C.13-02 (p.166) ◆ W13-20aP: When used to display the speed of an approaching vehicle in relation to the posted speed limit, the Vehicle Speed Feedback (W13-20aP) plaque shall be mounted below a Speed Limit (R2-1) sign (see Section 2B.21).
- **[M]** 2C.13-03 (p.166) ◆ W13-20: When used to supplement a horizontal alignment warning sign advisory speed, the Vehicle Speed Feedback (W13-20) sign shall be an independent installation near the point of curvature of a horizontal curve (see Section 2C.06).
- **[M]** 2C.13-04 (p.166): The legend YOUR SPEED shall be a black legend on a yellow retroreflective background, except as provided in Sections 6H.01 and 7B.01. The changeable legend displaying the speed of the approaching vehicle shall be a yellow luminous legend on a black opaque background. The vehicle speed displayed on the changeable portion of the sign shall be displayed as an integer. The Vehicle Speed Feedback sign and plaque shall not flash, strobe, change color, or use other animated elements integrated into the changeable legend display. When no vehicles are approaching, the changeable display shall not display a legend.
- **[R]** 2C.13-05 (p.166): The changeable portion of the Vehicle Speed Feedback legend should be approximately the same height, width, and stroke of those on the Speed Limit sign it supplements or is mounted below.
- **[R]** 2C.13-06 (p.166) ◆ W13-20aP: When a W13-20aP plaque is used with a Speed Limit sign it should be approximately the same width as the Speed Limit sign it is mounted below.

<a id="sec-2C-14"></a>
#### Section 2C.14 Hill Signs (W7-1 and W7-1a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W7-1](symbols/W7-1.png) | **W7-1** | Hill | Recommended (2C.14-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | 24 x 24* | 48 x 48 | 2C-1 p.148 | 6H-1 |
| ![W7-1a](symbols/W7-1a.png) | **W7-1a** | Hill with Grade | Recommended (2C.14-01) | 30 x 30* | 36 x 36 | 36 x 36 | 36 x 36 | 24 x 24* | 48 x 48 | 2C-1 p.148 | — |

- **[R]** 2C.14-01 (p.167) ◆ W7-1: The Hill (W7-1) sign (see Figure 2C-5) should be used in advance of a downgrade where the length, percent of grade, horizontal curvature, and/or other physical features require special precautions on the part of road users.
- **[R]** 2C.14-02 (p.167) ◆ W7-1a: The Hill sign and supplemental grade (W7-3P) plaque (see Figure 2C-5 and Section 2C.64) used in combination, or the W7-1a sign used alone, should be installed in advance of downgrades for the following conditions: A. 5% grade that is more than 3,000 feet in length, B. 6% grade that is more than 2,000 feet in length, C. 7% grade that is more than 1,000 feet in length, D. 8% grade that is more than 750 feet in length, or E. 9% grade that is more than 500 feet in length.
- **[R]** 2C.14-03 (p.167): These signs should also be installed for steeper grades or where crash experience and field observations indicate a need.
- **[R]** 2C.14-04 (p.167): Supplemental plaques (see Sections 2C.57 and 2C.64) and larger signs should be used for emphasis or where special hill characteristics exist. On longer grades, the use of the Hill sign with a distance (W7-3aP) plaque or the combination distance/grade (W7-3bP) plaque (see Figure 2C-5) at periodic intervals of approximately 1-mile spacing should be considered.
- [O] 2C.14-05 (p.167): A USE LOW GEAR (W7-2P) or TRUCKS USE LOWER GEAR (W7-2bP) supplemental plaque (see Figure 2C-5) may be used to indicate a situation where downshifting as well as braking might be advisable.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-15"></a>
#### Section 2C.15 Truck Escape Ramp Signs (W7-4 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W7-4](symbols/W7-4.png) | **W7-4** | Runaway Truck Ramp XX Miles | Recommended (2C.15-02) | 84 x 48 | 84 x 48 | 120 x 72 | 120 x 72 | — | — | 2C-1 p.149 | — |
| ![W7-4b](symbols/W7-4b.png) | **W7-4b** | Runaway Truck Ramp | Recommended (2C.15-02) | 84 x 54 | 84 x 54 | 120 x 78 | 120 x 78 | — | — | 2C-1 p.149 | — |
| ![W7-4c](symbols/W7-4c.png) | **W7-4c** | Truck Escape Ramp | Recommended (2C.15-02) | 78 x 60 | 78 x 60 | 78 x 60 | 78 x 60 | — | — | 2C-1 p.149 | — |
| ![W7-4dP](symbols/W7-4dP.png) | **W7-4dP** | Sand, Gravel, Paved (plaques) | Recommended (2C.15-02) | 24 x 12 | 24 x 12 | 24 x 12 | 24 x 12 | — | — | 2C-1 p.149 | — |
| ![W7-4eP](symbols/W7-4eP.png) | **W7-4eP** | Sand, Gravel, Paved (plaques) | Recommended (2C.15-02) | 24 x 12 | 24 x 12 | 24 x 12 | 24 x 12 | — | — | 2C-1 p.149 | — |
| ![W7-4fP](symbols/W7-4fP.png) | **W7-4fP** | Sand, Gravel, Paved (plaques) | Recommended (2C.15-02) | 24 x 12 | 24 x 12 | 24 x 12 | 24 x 12 | — | — | 2C-1 p.149 | — |

- **[R]** 2C.15-01 (p.168) ◆ W7-4b, W7-4c: Where applicable, truck escape (or runaway truck) ramp advance warning signs (see Figure 2C-5) should be located approximately 1 mile and approximately ½ mile in advance of the grade, and of the escape ramp. An additional W7-4b or W7-4c sign should be placed at the gore.
- **[R]** 2C.15-02 (p.168): A RUNAWAY VEHICLES ONLY (R4-10) sign (see Section 2B.41) should be installed near the escape ramp entrance to discourage other road users from entering the ramp. No Parking (R8-3) signs should be placed near the ramp entrance.
- **[M]** 2C.15-03 (p.168): When truck escape ramps are installed, at least one of the W7-4 series signs shall be used.
- [O] 2C.15-04 (p.168) ◆ W7-4dP, W7-4eP, W7-4fP: A SAND (W7-4dP), GRAVEL (W7-4eP), or PAVED (W7-4fP) supplemental plaque (see Figure 2C-5) may be used to describe the ramp surface. State and local highway agencies may develop appropriate word message signs for the specific situation.

<a id="sec-2C-16"></a>
#### Section 2C.16 HILL BLOCKS VIEW Sign (W7-6)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W7-6](symbols/W7-6.png) | **W7-6** | Hill Blocks View | Optional (2C.16-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2C-1 p.149 | — |

- [O] 2C.16-01 (p.168): A HILL BLOCKS VIEW (W7-6) sign (see Figure 2C-5) may be used on the approach to a crest vertical curve where the vertical curvature provides inadequate stopping sight distance at the posted speed limit.
- **[R]** 2C.16-02 (p.168): When a vertical curve results in a sight distance obstruction to a specific condition beyond the crest of the vertical curve, the warning sign for the specific condition beyond the vertical crest should be used rather than the HILL BLOCKS VIEW sign.
- **[R]** 2C.16-03 (p.168): When a HILL BLOCKS VIEW sign is used, it should be supplemented by an Advisory Speed (W13-1P) plaque (see Figure 2C-1) indicating the recommended speed for traveling over the hillcrest based on available stopping sight distance.

<a id="sec-2C-17"></a>
#### Section 2C.17 ROAD NARROWS Sign (W5-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W5-1](symbols/W5-1.png) | **W5-1** | Road Narrows | Recommended (2C.17-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | 6H-1 |

- **[R]** 2C.17-01 (p.169): Except as provided in Paragraph 2 of this Section, a ROAD NARROWS (W5-1) sign (see Figure 2C-6) should be used in advance of a transition on two-lane roads where the pavement width is reduced abruptly to a width such that vehicles traveling in opposite directions cannot simultaneously travel through the narrow portion of the roadway without reducing speed. Figure 2C-6. Miscellaneous Warning Signs SSSS6 W5-1 W5-2 W5-2a W5-3 W5-3a ~~PD~~ O tama W6-1 W6-2 W12-1 W12-2 W12-2a W12-2b W14-1 W14-1a W14-2 W14-2a W18-1 { FREEWAY ENDS | hd» [ALL TRAFFIC |
- [O] 2C.17-02 (p.170): The ROAD NARROWS (W5-1) sign may be omitted on low-volume local streets that have speed limits of 30 mph or less.
- [O] 2C.17-03 (p.170): Additional emphasis may be provided by the use of object markers and delineators (see Sections 2C.70 through 2C.73 and Chapter 3G). The Advisory Speed (W13-1P) plaque (see Figure 2C-1 and Section 2C.59) may be used to indicate the recommended speed.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-18"></a>
#### Section 2C.18 NARROW BRIDGE and NARROW UNDERPASS Signs (W5-2 and W5-2a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W5-2](symbols/W5-2.png) | **W5-2** | Narrow Bridge | Recommended (2C.18-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W5-2a](symbols/W5-2a.png) | **W5-2a** | Narrow Underpass | Recommended (2C.18-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | — |

- **[R]** 2C.18-01 (p.170): A NARROW BRIDGE (W5-2) sign (see Figure 2C-6) should be used in advance of any bridge or culvert having a two-way roadway horizontal clearance of 16 to 18 feet, or any bridge or culvert having a roadway horizontal clearance less than the width of the approach travel lanes. Where these conditions exist for an underpass, a NARROW UNDERPASS (W5-2a) sign (see Figure 2C-6) should be used.
- **[R]** 2C.18-02 (p.170): Additional emphasis should be provided by the use of object markers, delineators, and/or pavement markings.
- [O] 2C.18-03 (p.170): A NARROW BRIDGE sign may be used in advance of a bridge or culvert on which the approach shoulders are narrowed or eliminated. Where these conditions exist for an underpass, a NARROW UNDERPASS sign may be used.
- [O] 2C.18-04 (p.170): The NARROW BRIDGE or NARROW UNDERPASS sign may be omitted on low-volume rural roads where there is adequate sight distance to the bridge, culvert, or underpass on both approaches.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-2C-19"></a>
#### Section 2C.19 ONE LANE BRIDGE and ONE LANE UNDERPASS Signs (W5-3 and W5-3a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W5-3](symbols/W5-3.png) | **W5-3** | One Lane Bridge | Recommended (2C.19-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | 6H-1 |
| ![W5-3a](symbols/W5-3a.png) | **W5-3a** | One Lane Underpass | Recommended (2C.19-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | — |

- **[R]** 2C.19-01 (p.170) ◆ W5-3: A ONE LANE BRIDGE (W5-3) sign (see Figure 2C-6) should be used on two-way roadways in advance of any bridge or culvert: A. Having a roadway horizontal clearance of less than 16 feet, or B. Having a roadway horizontal clearance of less than 18 feet when commercial vehicles constitute a high proportion of the traffic, or C. Having a roadway horizontal clearance of 18 feet or less where the sight distance on the approach is less than that shown in Condition A of Table 2C-3.
- **[R]** 2C.19-02 (p.170) ◆ W5-3a: Where these conditions exist for an underpass, a ONE LANE UNDERPASS (W5-3a) sign (see Figure 2C-6) should be used.
- **[R]** 2C.19-03 (p.170): Additional emphasis should be provided by the use of object markers, delineators, and/or pavement markings.
- [O] 2C.19-04 (p.170): The ONE LANE BRIDGE or ONE LANE UNDERPASS sign may be omitted on low-volume rural roads where there is adequate sight distance to the bridge, culvert, or underpass on both approaches.
- [O] 2C.19-05 (p.170): STOP (R1-1) or YIELD (R1-2) signs (see Sections 2B.04 and 2B.05) and related pavement markings (see Sections 3B.21 and 3B.22) may be used when conditions A, B, or C in Paragraph 1 of this Section apply.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-20"></a>
#### Section 2C.20 Divided Highway Sign (W6-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W6-1](symbols/W6-1.png) | **W6-1** | Divided Highway | Recommended (2C.20-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |

- **[R]** 2C.20-01 (p.170): A Divided Highway (W6-1) sign (see Figure 2C-6) should be used on the approaches to a section of highway (not an intersection or junction) where the opposing flows of traffic are separated by a median or other physical barrier.
- **[M]** 2C.20-02 (p.170): The Divided Highway (W6-1) sign shall not be used instead of a Keep Right (R4-7 series) sign on the approach end of a median island.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-21"></a>
#### Section 2C.21 Divided Highway Ends Sign (W6-2)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W6-2](symbols/W6-2.png) | **W6-2** | Divided Highway Ends | Recommended (2C.21-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |

- **[R]** 2C.21-01 (p.170): A Divided Highway Ends (W6-2) sign (see Figure 2C-6) should be used in advance of the end of a section of physically divided highway (not an intersection or junction) as a warning of two-way traffic ahead.
- **[R]** 2C.21-02 (p.170): The Two-Way Traffic (W6-3) sign (see Section 2C.51) should be used to give warning and notice of the transition to a two-lane, two-way section.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-22"></a>
#### Section 2C.22 Freeway or Expressway Ends Signs (W19 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W19-1](symbols/W19-1.png) | **W19-1** | Freeway Ends XX Miles | Optional (2C.22-01) | — | — | — | 144 x 48 | — | — | 2C-1 p.151 | — |
| ![W19-2](symbols/W19-2.png) | **W19-2** | Expressway Ends XX Miles | Optional (2C.22-01) | — | — | 144 x 48 | — | — | — | 2C-1 p.151 | — |
| ![W19-3](symbols/W19-3.png) | **W19-3** | Freeway Ends | Optional (2C.22-01) | — | — | — | 48 x 48 | — | — | 2C-1 p.151 | — |
| ![W19-4](symbols/W19-4.png) | **W19-4** | Expressway Ends | Optional (2C.22-01) | — | — | 48 x 48 | — | — | — | 2C-1 p.151 | — |
| ![W19-5](symbols/W19-5.png) | **W19-5** | All Traffic Must Exit | Optional (2C.22-01) | — | — | 90 x 48 | 90 x 48 | — | — | 2C-1 p.151 | — |
|  | **W19-7aP** | Freeway or Expressway Ends Signs (W19 Series) | Optional (2C.22-01) | — | — | — | — | — | — | text | — |

- [O] 2C.22-01 (p.171) ◆ W19-1, W19-3: A FREEWAY ENDS XX MILES (W19-1) sign or a FREEWAY ENDS (W19-3) sign (see Figure 2C-6) may be used in advance of the end of a freeway.
- [O] 2C.22-02 (p.171) ◆ W19-2, W19-4: An EXPRESSWAY ENDS XX MILES (W19-2) sign or an EXPRESSWAY ENDS (W19-4) sign (see Figure 2C-6) may be used in advance of the end of an expressway.
- [O] 2C.22-03 (p.171) ◆ W19-1, W19-2: The rectangular W19-1 and W19-2 signs may be post-mounted or may be mounted overhead for increased emphasis.
- **[R]** 2C.22-04 (p.171) ◆ W19-5: If the reason that the freeway is ending is that the next portion of the freeway is not yet constructed and as a result all traffic must use an exit ramp to leave the freeway, an ALL TRAFFIC MUST EXIT (W19-5) sign (see Figure 2C-6) should be used in addition to the Freeway Ends signs in advance of the downstream end of the freeway.

<a id="sec-2C-23"></a>
#### Section 2C.23 Double Arrow Sign (W12-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W12-1](symbols/W12-1.png) | **W12-1** | Double Arrow | Optional (2C.23-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | — | — | 2C-1 p.150 | 6H-1 |

- [O] 2C.23-01 (p.171): The Double Arrow (W12-1) sign (see Figure 2C-6) may be used to advise road users that traffic is permitted to pass on either side of an island, obstruction, or gore in the roadway. Traffic separated by this sign may either rejoin or change directions.
- **[R]** 2C.23-02 (p.171): If used on an island, the Double Arrow sign should be mounted near the approach end.
- **[R]** 2C.23-03 (p.171): If used in front of a pier or obstruction, the Double Arrow sign should be mounted on the face of, or just in front of, the pier or obstruction. Where stripe markings are used on the pier or obstruction, they should be discontinued to leave a 3-inch space around the outside of the Double Arrow sign.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-24"></a>
#### Section 2C.24 DEAD END, NO OUTLET, and ROAD ENDS Signs (W14-1, W14-1a, W14-2, W14-2a, W8-26, and W8-26a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-26](symbols/W8-26.png) | **W8-26** | Road Ends | Optional (2C.24-01) | 30 x 30 | 36 x 36 | — | — | — | — | 2C-1 p.149 | — |
| ![W8-26a](symbols/W8-26a.png) | **W8-26a** | Street Ends | Optional (2C.24-01) | 30 x 30 | 36 x 36 | — | — | — | — | 2C-1 p.149 | — |
|  | **W14-1** | ROAD ENDS Signs | Optional (2C.24-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | — |
| ![W14-1a](symbols/W14-1a.png) | **W14-1a** | Dead End, No Outlet (with arrow) | Optional (2C.24-01) | 36 x 9 | 36 x 9 | — | — | — | — | 2C-1 p.150 | — |
| ![W14-2](symbols/W14-2.png) | **W14-2** | Dead End, No Outlet | Optional (2C.24-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | — |
| ![W14-2a](symbols/W14-2a.png) | **W14-2a** | Dead End, No Outlet (with arrow) | Optional (2C.24-01) | 36 x 9 | 36 x 9 | — | — | — | — | 2C-1 p.150 | — |

- [O] 2C.24-01 (p.171) ◆ W14-1, W14-2: The DEAD END (W14-1) sign (see Figure 2C-6) may be used at the entrance to a single road or street that terminates without intersecting another street. The NO OUTLET (W14-2) sign (see Figure 2C-6) may be used at the entrance to a road or road network from which there is no other exit.
- [O] 2C.24-02 (p.171) ◆ W14-1a, W14-2a: DEAD END (W14-1a) or NO OUTLET (W14-2a) signs (see Figure 2C-6) may be used in combination with Street Name (D3-1) signs (see Section 2D.45) to warn turning traffic that the cross street ends in the direction indicated by the arrow.
- [O] 2C.24-03 (p.171) ◆ W14-1a, W14-2a: At locations where the cross street does not have a name, a W14-1a or W14-2a sign may be used alone in place of a street name sign.
- **[R]** 2C.24-04 (p.171) ◆ W14-1, W14-2: When the W14-1 or W14-2 sign is used, the sign should be posted as near as practicable to the entry point or at a sufficient advance distance to permit the road user to avoid the dead end or no outlet condition by turning at the nearest intersecting street.
- **[M]** 2C.24-05 (p.171) ◆ W14-1, W14-1a, W14-2, W14-2a: The DEAD END (W14-1a) or NO OUTLET (W14-2a) sign shall not be used instead of the W14-1 or W14-2 signs where traffic can proceed straight through the intersection into the dead end street or no outlet area.
- [O] 2C.24-06 (p.171) ◆ W8-26, W8-26a: The ROAD ENDS XX FT (W8-26) or STREET ENDS XX FT (W8-26a) sign (see Figure 2C-11) may be used on the approach to the end of a conventional road or street where the terminus is not apparent.
- **[M]** 2C.24-08 (p.171) ◆ W8-26, W8-26a, W14-1, W14-2: The W8-26 and W8-26a signs shall not be used in place of a W14-1 or W14-2 sign at the entrance to such a road or street.

<a id="sec-2C-25"></a>
#### Section 2C.25 Low Clearance Signs (W12-2, W12-2a, and W12-2b)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W12-2](symbols/W12-2.png) | **W12-2** | Low Clearance Advance | Mandatory (2C.25-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.150 | 9A-1, 6H-1 |
| ![W12-2a](symbols/W12-2a.png) | **W12-2a** | Low Clearance Overhead | Mandatory (2C.25-01) | 84 x 24 | 84 x 24 | 84 x 24 | 84 x 24 | — | — | 2C-1 p.150 | — |
| ![W12-2b](symbols/W12-2b.png) | **W12-2b** | Low Clearance - Lane Overhead | Mandatory (2C.25-01) | 102 x 24 | 102 x 24 | 102 x 24 | 102 x 24 | — | — | 2C-1 p.150 | — |

- **[M]** 2C.25-01 (p.172) ◆ W12-2: The Low Clearance Advance (W12-2) sign (see Figure 2C-6) shall be used to warn road users of vertical clearances less than 14 feet 6 inches, or vertical clearances less than 12 inches above the statutory maximum vehicle height, whichever is greater.
- **[R]** 2C.25-02 (p.172): The actual clearance should be displayed on the Low Clearance (W12-2, W12-2a, and W12-2b) sign to the nearest 1 inch not exceeding the actual clearance. However, in areas that experience changes in temperature causing frost action, a reduction, not exceeding 3 inches, should be used for this condition.
- **[R]** 2C.25-03 (p.172): Clearances should be evaluated periodically to determine if additional low clearance signing is necessary, particularly when resurfacing operations have occurred, on routes onto which over-height vehicles are normally directed under the permit process, and structures that are susceptible to catastrophic failure when struck by overheight vehicles.
- **[R]** 2C.25-04 (p.172) ◆ W12-2: The W12-2 sign with a supplemental distance plaque should also be placed at the nearest intersecting road or wide point in the road at which a vehicle can detour or turn around.
- **[R]** 2C.25-05 (p.172) ◆ W12-2: Where there is a need to warn of a low clearance on an intersecting road or off a freeway or expressway exit, a rectangular warning sign with an appropriate word legend should be used rather than a W12-2 sign.
- [O] 2C.25-06 (p.172) ◆ W12-2a, W12-2b: The Low Clearance Overhead (W12-2a or W12-2b) sign (see Figure 2C-6) may be installed on the structure to supplement the advance warning sign.
- [O] 2C.25-07 (p.172): In cases where physical conditions on a structure limit the width such that the W12-2a or W12-2b signs are physically unable to fit, a W12-2 sign may be installed overhead on the structure or post-mounted in front of the structure, in addition to the required W12-2 sign at the advance location.
- **[R]** 2C.25-08 (p.172) ◆ W12-2a: In the case of an arch, or other structure under which the clearance varies greatly, two or more Low Clearance Overhead (W12-2a or 12-2b) signs should be installed on the structure itself to give information as to the clearances over the low clearance portions of the roadway.
- **[M]** 2C.25-09 (p.172) ◆ W12-2b: If used, the Low Clearance Overhead (W12-2b) sign shall be placed over a lane or shoulder to indicate the portion of the structure with low clearance if the posted clearance does not apply to the entire structure.
- **[R]** 2C.25-10 (p.172) ◆ W12-2a, W12-2b: The clearance shown on the Low Clearance Advance sign should match the clearance on the W12-2a or W12-2b sign or, if there are multiple W12-2b signs, should match the lowest clearance.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-2C-26"></a>
#### Section 2C.26 BUMP and DIP Signs (W8-1 and W8-2)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-1](symbols/W8-1.png) | **W8-1** | Bump or Dip | Recommended (2C.26-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 9A-1, 6H-1 |
| ![W8-2](symbols/W8-2.png) | **W8-2** | Bump or Dip | Recommended (2C.26-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 9A-1, 6H-1 |

- **[R]** 2C.26-01 (p.173): BUMP (W8-1) and DIP (W8-2) signs (see Figure 2C-7) should be used in advance of a sharp rise or depression in the profile of the road.
- [O] 2C.26-02 (p.173): These signs may be supplemented with an Advisory Speed plaque (see Figure 2C-1 and Section 2C.59).
- **[R]** 2C.26-03 (p.173): The DIP sign should not be used in advance of a short stretch of depressed alignment that might momentarily hide a vehicle.
- **[R]** 2C.26-04 (p.173): A short stretch of depressed alignment that might momentarily hide a vehicle should be treated as a no-passing zone when center line striping is provided on a two-lane or three-lane road (see Section 3B.03).

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.03:*

- [O] 9C.03-02 (p.1066): Signs warning of other conditions that might be of concern to bicyclists, including BUMP (W8-1), DIP (W8-2), PAVEMENT ENDS (W8-3), and any other word message that describes conditions that are of concern to bicyclists, may also be used (see Figure 9C-1). A supplemental plaque may be used to clarify the specific type of surface condition. 03

<a id="sec-2C-27"></a>
#### Section 2C.27 SPEED HUMP Sign (W17-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W17-1](symbols/W17-1.png) | **W17-1** | Speed Hump | Recommended (2C.27-01) · *Auto* | 30 x 30* | 36 x 36 | — | — | 24 x 24* | 48 x 48 | 2C-1 p.151 | — |

- **[R]** 2C.27-01 (p.173): The SPEED HUMP (W17-1) sign (see Figure 2C-7) should be used in advance of a vertical deflection in the roadway that is designed to limit the speed of traffic.
- **[R]** 2C.27-02 (p.173): If used, the SPEED HUMP sign should be supplemented by an Advisory Speed plaque (see Figure 2C-1 and Section 2C.59).
- [O] 2C.27-03 (p.173): If a series of speed humps exists in close proximity, an Advisory Speed plaque may be eliminated on all but the first SPEED HUMP sign in the series.
- [O] 2C.27-04 (p.173): The legend SPEED BUMP may be used instead of the legend SPEED HUMP on the W17-1 sign.

<a id="sec-2C-28"></a>
#### Section 2C.28 PAVEMENT ENDS Sign (W8-3)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-3](symbols/W8-3.png) | **W8-3** | Pavement Ends | Recommended (2C.28-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | — | 30 x 30* | — | 2C-1 p.149 | 9A-1, 6H-1 |

- **[R]** 2C.28-01 (p.173): A PAVEMENT ENDS (W8-3) sign (see Figure 2C-7) should be used where a paved surface changes to either a gravel treated surface or an earth road surface.
- [O] 2C.28-02 (p.173): An Advisory Speed plaque (see Figure 2C-1 and Section 2C.59) may be used when the change in roadway condition requires a reduced speed.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.03:*

- [O] 9C.03-02 (p.1066): Signs warning of other conditions that might be of concern to bicyclists, including BUMP (W8-1), DIP (W8-2), PAVEMENT ENDS (W8-3), and any other word message that describes conditions that are of concern to bicyclists, may also be used (see Figure 9C-1). A supplemental plaque may be used to clarify the specific type of surface condition. 03

<a id="sec-2C-29"></a>
#### Section 2C.29 Shoulder Signs (W8-4, W8-9, W8-17, W8-23, and W8-25)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-4](symbols/W8-4.png) | **W8-4** | Soft Shoulder | Optional (2C.29-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-9](symbols/W8-9.png) | **W8-9** | Low Shoulder | Optional (2C.29-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
|  | **W8-17** | Shoulder Drop-Off | Optional (2C.29-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-17P](symbols/W8-17P.png) | **W8-17P** | Shoulder Drop-Off (plaque) | Optional · *Auto* | 24 x 18 | 24 x 18 | 30 x 24 | 36 x 30 | — | 36 x 30 | 2C-1 p.149 | 6H-1 |
| ![W8-23](symbols/W8-23.png) | **W8-23** | No Shoulder | Optional (2C.29-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-25](symbols/W8-25.png) | **W8-25** | Shoulder Ends | Optional (2C.29-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |

- [O] 2C.29-01 (p.173) ◆ W8-4, W8-9: The SOFT SHOULDER (W8-4) sign (see Figure 2C-7) may be used to warn of a soft shoulder condition. 02 The LOW SHOULDER (W8-9) sign (see Figure 2C-7) may be used to warn of a shoulder condition where there is an elevation difference of 3 inches or less between the shoulder and the travel lane.
- **[R]** 2C.29-03 (p.173) ◆ W8-17: The Shoulder Drop Off (W8-17) sign (see Figure 2C-7) should be used where an unprotected shoulder dropoff, adjacent to the travel lane, exceeds 3 inches in depth for a significant continuous length along the roadway, based on engineering judgment.
- [O] 2C.29-04 (p.173) ◆ W8-17, W8-17P: A SHOULDER DROP-OFF (W8-17P) supplemental plaque (see Figure 2C-7) may be mounted below the W8-17 sign.
- [O] 2C.29-05 (p.173) ◆ W8-23: The NO SHOULDER (W8-23) sign (see Figure 2C-7) may be used to warn road users that a shoulder does not exist along a portion of the roadway.
- [O] 2C.29-06 (p.175) ◆ W8-25: The SHOULDER ENDS (W8-25) sign (see Figure 2C-7) may be used to warn road users that a shoulder is ending.
- **[R]** 2C.29-07 (p.175): Additional shoulder signs should be placed at appropriate intervals along the road where the condition continually exists.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 6H.26:*

- [O] 6H.26-01 (p.808) ◆ W8-4: The SOFT SHOULDER (W8-4) sign (see Figure 6H-1) may be used to warn of a soft shoulder condition.
- [O] 6H.26-02 (p.808) ◆ W8-9: The LOW SHOULDER (W8-9) sign (see Figure 6H-1) may be used to warn of a shoulder condition where there is an elevation difference of 3 inches or less between the shoulder and the travel lane.
- **[R]** 6H.26-03 (p.808) ◆ W8-17: The Shoulder Drop Off (W8-17) sign (see Figure 6H-1) should be used when an unprotected shoulder drop-off, adjacent to the travel lane, exceeds 3 inches in depth for a continuous length along the roadway, based on engineering judgment.
- [O] 6H.26-04 (p.808) ◆ W8-17, W8-17P: A SHOULDER DROP-OFF (W8-17P) supplemental plaque (see Figure 6H-1) may be mounted below the W8-17 sign.

<a id="sec-2C-30"></a>
#### Section 2C.30 Surface Condition Signs (W8-5, W8-7, W8-8, W8-11, W8-13, and W8-14)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-5](symbols/W8-5.png) | **W8-5** | Slippery When Wet | Optional (2C.30-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-5P](symbols/W8-5P.png) | **W8-5P** | Road Condition (plaques) | Optional (2C.30-01) | 24 x 18 | 24 x 18 | 30 x 24 | 36 x 30 | — | 36 x 30 | 2C-1 p.149 | — |
| ![W8-5aP](symbols/W8-5aP.png) | **W8-5aP** | Ice (plaque) | Optional (2C.30-01) | 24 x 12 | 24 x 12 | 30 x 18 | 30 x 18 | — | — | 2C-1 p.149 | — |
| ![W8-5bP](symbols/W8-5bP.png) | **W8-5bP** | Road Condition (plaques) | Optional (2C.30-01) | 24 x 18 | 24 x 18 | 30 x 24 | 36 x 30 | — | 36 x 30 | 2C-1 p.149 | — |
| ![W8-5cP](symbols/W8-5cP.png) | **W8-5cP** | Road Condition (plaques) | Optional (2C.30-01) | 24 x 18 | 24 x 18 | 30 x 24 | 36 x 30 | — | 36 x 30 | 2C-1 p.149 | — |
| ![W8-7](symbols/W8-7.png) | **W8-7** | Loose Gravel | Optional (2C.30-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-8](symbols/W8-8.png) | **W8-8** | Rough Road | Optional (2C.30-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-11](symbols/W8-11.png) | **W8-11** | Uneven Lanes | Optional (2C.30-01) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-13](symbols/W8-13.png) | **W8-13** | Bridge Ices Before Road | Optional (2C.30-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W8-14](symbols/W8-14.png) | **W8-14** | Fallen Rocks | Optional (2C.30-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |

- [O] 2C.30-01 (p.175) ◆ W8-5: The Slippery When Wet (W8-5) sign (see Figure 2C-7) may be used to warn of unexpected slippery conditions. Supplemental plaques (see Figure 2C-7) with legends such as ICE, WHEN WET, STEEL DECK, or EXCESS OIL may be used with the W8-5 sign to indicate the reason that the slippery conditions might be present.
- [O] 2C.30-02 (p.175) ◆ W8-7: The LOOSE GRAVEL (W8-7) sign (see Figure 2C-7) may be used to warn of loose gravel on the roadway surface.
- [O] 2C.30-03 (p.175) ◆ W8-8: The ROUGH ROAD (W8-8) sign (see Figure 2C-7) may be used to warn of a rough roadway surface.
- [O] 2C.30-04 (p.175) ◆ W8-11: An UNEVEN LANES (W8-11) sign (see Figure 2C-7) may be used to warn of a difference in elevation between travel lanes.
- [O] 2C.30-05 (p.175) ◆ W8-13: The BRIDGE ICES BEFORE ROAD (W8-13) sign (see Figure 2C-7) may be used in advance of bridges to advise bridge users of winter weather conditions. The BRIDGE ICES BEFORE ROAD sign may be removed or covered during seasons of the year when its message is not relevant.
- [O] 2C.30-06 (p.175) ◆ W8-14: The FALLEN ROCKS (W8-14) sign (see Figure 2C-7) may be used in advance of an area that is adjacent to a hillside, mountain, or cliff where rocks frequently fall onto the roadway.
- **[R]** 2C.30-07 (p.175): When used, Surface Condition signs should be placed in advance of the beginning of the affected section (see Table 2C-3), and additional signs should be placed at appropriate intervals along the road where the condition exists.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 6H.27:*

- **[R]** 6H.27-01 (p.808) ◆ W8-11: The UNEVEN LANES (W8-11) sign (see Figure 6H-1) should be used during operations that create a difference in elevation between adjacent lanes that are open to travel.

<a id="sec-2C-31"></a>
#### Section 2C.31 Warning Signs and Plaque for Motorcyclists (W8-15, W8-15aP, and W8-16)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **W8-15** | Grooved Pavement | Optional (2C.31-02) | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-15aP](symbols/W8-15aP.png) | **W8-15aP** | Motorcycle (plaque) | Optional (2C.31-02) | 24 x 18 | 24 x 18 | 30 x 24 | 36 x 30 | — | 36 x 30 | 2C-1 p.149 | 6H-1 |
| ![W8-16](symbols/W8-16.png) | **W8-16** | Metal Bridge Deck | Optional (2C.31-02) | 30 x 30* | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |

- [O] 2C.31-02 (p.175) ◆ W8-15: If a portion of a street or highway features a roadway pavement surface that is grooved or textured instead of smooth, such as a grooved skid resistance treatment for a horizontal curve or a brick pavement surface, a GROOVED PAVEMENT (W8-15) sign (see Figure 2C-7) may be used to provide advance warning of this condition to motorcyclists, bicyclists, and other road users. Alternate legends such as TEXTURED PAVEMENT or BRICK PAVEMENT may also be used on the W8-15 sign.
- [O] 2C.31-03 (p.175) ◆ W8-16: If a bridge or a portion of a bridge includes a metal or grated surface, a METAL BRIDGE DECK (W8-16) sign (see Figure 2C-7) may be used to provide advance warning of this condition to motorcyclists, bicyclists, and other road users.
- [O] 2C.31-04 (p.175): A Motorcycle (W8-15aP) plaque (see Figure 2C-7) may be mounted below or above a W8-15 or W8-16 sign if the warning is intended to be directed primarily to motorcyclists.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 6H.34:*

- [O] 6H.34-01 (p.810) ◆ W8-16: A Motorcycle (W8-15P) plaque (see Figure 6H-1) may be mounted below a LOOSE GRAVEL (W8-7) sign, a GROOVED PAVEMENT (W8-15) sign, a METAL BRIDGE DECK (W8-16) sign, or a STEEL PLATE AHEAD (W8-24) sign if the warning is intended to be directed primarily to motorcyclists.

<a id="sec-2C-32"></a>
#### Section 2C.32 NO CENTER LINE Sign (W8-12)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-12](symbols/W8-12.png) | **W8-12** | No Center Line | Optional (2C.32-01) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | — | 2C-1 p.149 | 6H-1 |

- [O] 2C.32-01 (p.175): The NO CENTER LINE (W8-12) sign (see Figure 2C-7) may be used to warn of a roadway without center line pavement markings.

*Also governed by Section 6H.29:*

- **[R]** 6H.29-01 (p.808): The NO CENTER LINE (W8-12) sign (see Figure 6H-1) should be used when the work obliterates the center line pavement markings. This sign should be placed at the beginning of the TTC zone and repeated at 2-mile intervals in long TTC zones.

<a id="sec-2C-33"></a>
#### Section 2C.33 NO TRAFFIC SIGNS Sign (W18-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W18-1](symbols/W18-1.png) | **W18-1** | No Traffic Signs | Optional (2C.33-01) | 30 x 30* | 36 x 36 | — | — | 24 x 24* | 36 x 36 | 2C-1 p.151 | — |

- [O] 2C.33-01 (p.175): The NO TRAFFIC SIGNS (W18-1) sign (see Figure 2C-6) may be used only on low-volume rural roads to advise road users that no signs are installed along the distance of the road. The sign may be installed at the point where road users would enter the low volume road or where, based on engineering judgment, the road user might need this information.
- [O] 2C.33-02 (p.176): A W7-3aP (see Figure 2C-5), W16-2P (see Figure 2C-16), or W16-9P (see Figure 2C-16) supplemental plaque with the legend NEXT XX MILES, XX FEET, or AHEAD may be installed below the W18-1 sign when appropriate.

<a id="sec-2C-34"></a>
#### Section 2C.34 Weather Condition Signs (W8-18, W8-19, W8-21, and W8-22)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-18](symbols/W8-18.png) | **W8-18** | Road May Flood | Optional (2C.34-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
| ![W8-19](symbols/W8-19.png) | **W8-19** | Depth Gauge | Optional (2C.34-01) | 12 x 72 | 12 x 72 | — | — | — | — | 2C-1 p.149 | — |
| ![W8-21](symbols/W8-21.png) | **W8-21** | Gusty Winds Area | Optional (2C.34-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W8-22](symbols/W8-22.png) | **W8-22** | Fog Area | Optional (2C.34-01) · *Auto* | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |

- [O] 2C.34-01 (p.176) ◆ W8-18, W8-19: The ROAD MAY FLOOD (W8-18) sign (see Figure 2C-7) may be used to warn road users that a section of roadway is subject to frequent flooding. A Depth Gauge (W8-19) sign (see Figure 2C-7) may also be installed within a roadway section that frequently floods.
- **[R]** 2C.34-02 (p.176): If used, the Depth Gauge sign should be in addition to the ROAD MAY FLOOD sign and should be mounted at the appropriate height to indicate the depth of the water at the deepest point on the roadway .
- [O] 2C.34-03 (p.176) ◆ W8-21: The GUSTY WINDS AREA (W8-21) sign (see Figure 2C-7) may be used to warn road users that wind gusts frequently occur along a section of highway that are strong enough to impact the stability of trucks, recreational vehicles, and other vehicles with high centers of gravity. A NEXT XX MILES (W7-3aP) supplemental plaque (see Figure 2C-5) may be mounted below the W8-21 sign to inform road users of the length of roadway that frequently experiences strong wind gusts.
- [O] 2C.34-04 (p.176) ◆ W8-22: The FOG AREA (W8-22) sign (see Figure 2C-7) may be used to warn road users that foggy conditions frequently reduce visibility along a section of highway . A NEXT XX MILES (W7-3aP) supplemental plaque (see Figure 2C-5) may be mounted below the W8-22 sign to inform road users of the length of roadway that frequently experiences foggy conditions.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-35"></a>
#### Section 2C.35 Advance Traffc Control Signs (W3i -1, W3-2, W3-3, and W3-4)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W3-1](symbols/W3-1.png) | **W3-1** | Stop Ahead | Mandatory (2C.35-01) · *Auto* | 30 x 30 | 30 x 30 | 48 x 48 | 48 x 48 | 30 x 30 | — | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W3-2](symbols/W3-2.png) | **W3-2** | Yield Ahead | Mandatory (2C.35-01) · *Auto* | 30 x 30 | 30 x 30 | 48 x 48 | 48 x 48 | 30 x 30 | — | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W3-3](symbols/W3-3.png) | **W3-3** | Stop, Yield, Signal Ahead | Mandatory (2C.35-01) · *Auto* | 30 x 30 | 30 x 30 | 48 x 48 | 48 x 48 | 30 x 30 | — | 2C-1 p.148 | 9A-1, 6H-1 |
| ![W3-4](symbols/W3-4.png) | **W3-4** | Be Prepared to Stop | Mandatory (2C.35-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30 | — | 2C-1 p.148 | 6H-1 |

- **[M]** 2C.35-01 (p.177) ◆ W3-1, W3-2, W3-3: The Stop Ahead (W3-1), Yield Ahead (W3-2), and Signal Ahead (W3-3) Advance Traffic Control signs (see Figure 2C-8) shall be installed on an approach to a primary traffic control device that is not visible for a sufficient distance to permit the road user to respond to the device (see Table 2C-3). The visibility criteria for a traffic control signal shall be based on having a continuous view of at least two signal faces for the distance specified in Table 4D-2.
- **[R]** 2C.35-02 (p.177): Where intermittent obstructions occur, engineering judgment should determine the treatment to be implemented.
- [O] 2C.35-05 (p.177): An Advance Traffic Control sign may be used for additional emphasis of the primary traffic control device, even when the visibility distance to the device is satisfactory.
- [O] 2C.35-07 (p.177) ◆ W3-4: A BE PREPARED TO STOP (W3-4) sign (see Figure 2C-8) may be used to warn of stopped traffic caused by a traffic control signal.
- [O] 2C.35-08 (p.177): A Warning Beacon (see Section 4S.03) or yellow LEDs within the border of the sign may be used with an Advance Traffic Control or BE PREPARED TO STOP sign.
- **[M]** 2C.35-09 (p.177): When a BE PREPARED TO STOP sign is used in advance of a traffic control signal, it shall be used in addition to a Signal Ahead sign and shall be placed downstream from the Signal Ahead sign.
- **[R]** 2C.35-10 (p.177): When a Warning Beacon is interconnected with a traffic control signal or queue detection system, the BE PREPARED TO STOP sign should be supplemented with a WHEN FLASHING (W16-13P) plaque (see Figure 2C-16).

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-2C-36"></a>
#### Section 2C.36 DRAW BRIDGE Sign (W3-6)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W3-6](symbols/W3-6.png) | **W3-6** | Draw Bridge | Mandatory (2C.36-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | — | 60 x 60 | 2C-1 p.148 | — |

- **[M]** 2C.36-01 (p.178): A DRAW BRIDGE (W3-6) sign (see Figure 2C-8) shall be used in advance of movable bridge signals and gates (see Section 4Q.02) to give warning to road users.

<a id="sec-2C-37"></a>
#### Section 2C.37 Advance Ramp Control Signal Signs (W3-7 and W3-8)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W3-7](symbols/W3-7.png) | **W3-7** | Ramp Meter Ahead | Optional (2C.37-01) | 36 x 36 | 36 x 36 | — | — | — | — | 2C-1 p.148 | — |
| ![W3-8](symbols/W3-8.png) | **W3-8** | Ramp Metered When Flashing | Optional (2C.37-01) | 36 x 36 | 36 x 36 | — | — | — | — | 2C-1 p.148 | — |

- [O] 2C.37-01 (p.178) ◆ W3-7: A RAMP METER AHEAD (W3-7) sign (see Figure 2C-8) may be used to warn road users that a freeway entrance ramp is metered and that they will encounter a ramp control signal (see Chapter 4P).
- **[R]** 2C.37-02 (p.178) ◆ W3-8: When the ramp control signals are operated only during certain periods of the day, a RAMP METERED WHEN FLASHING (W3-8) sign (see Figure 2C-8) should be installed in advance of the ramp control signal near the entrance to the ramp, or on the arterial on the approach to the ramp, to alert road users to the presence and operation of ramp meters.
- **[M]** 2C.37-03 (p.178): The RAMP METERED WHEN FLASHING sign shall be supplemented with a Warning Beacon (see Section 4S.03) that flashes when the ramp control signal is in operation.

<a id="sec-2C-38"></a>
#### Section 2C.38 NEW TRAFFIC PATTERN and NEW SIGNAL OPERATION AHEAD Signs (W23-2 and W23-2a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W23-2](symbols/W23-2.png) | **W23-2** | New Traffic Pattern Ahead | Optional (2C.38-01) | 36 x 36 | 36 x 36 | — | — | — | — | 2C-1 p.151 | 6H-1 |
| ![W23-2a](symbols/W23-2a.png) | **W23-2a** | New Signal Operation Ahead | Optional (2C.38-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.151 | — |

- [O] 2C.38-01 (p.178) ◆ W23-2: A NEW TRAFFIC PATTERN AHEAD (W23-2) sign (see Figure 2C-8) may be used on the approach to an intersection or along a section of roadway to provide advance warning of a change in traffic patterns, such as revised lane usage or roadway geometry.
- [O] 2C.38-02 (p.178) ◆ W23-2a: A NEW SIGNAL OPERATION AHEAD (W23-2a) sign (see Figure 2C-8) may be used on the approach to a signalized intersection to provide advance warning of a change in signal phasing.
- **[R]** 2C.38-03 (p.178): The NEW TRAFFIC PATTERN or NEW SIGNAL OPERATION AHEAD sign should be removed when the traffic pattern returns to normal, when the changed pattern is no longer considered to be new, or within 12 months.

*Also governed by Section 6H.14:*

- [O] 6H.14-01 (p.806) ◆ W23-2: A NEW TRAFFIC PATTERN AHEAD (W23-2) sign (see Figure 6H-1) may be used on the approach to an intersection or along a section of roadway to provide advance warning of a change in traffic patterns, such as revised lane usage, roadway geometry, or signal phasing.
- **[R]** 6H.14-02 (p.806) ◆ W23-2: To retain its effectiveness, the W23-2 sign should be displayed for up to 2 weeks, and then it should be covered or removed until it is needed again.

<a id="sec-2C-39"></a>
#### Section 2C.39 WATCH FOR STOPPED TRAFFIC Sign (W26-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W26-1](symbols/W26-1.png) | **W26-1** | Watch for Stopped Traffic | Optional (2C.39-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.151 | — |

- [O] 2C.39-01 (p.178): The WATCH FOR STOPPED TRAFFIC (W26-1) sign (see Figure 2C-8) may be used to warn road users of the possibility of vehicles stopping abruptly in the travel lane due to recurring congested conditions.

<a id="sec-2C-40"></a>
#### Section 2C.40 Reduced Speed Limit Ahead and Speed Zone Signs (W3-5, W3-5a, W3-5b, and W3-5c)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W3-5](symbols/W3-5.png) | **W3-5** | Reduced Speed Limit Ahead | Recommended (2C.40-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |
| ![W3-5a](symbols/W3-5a.png) | **W3-5a** | XX MPH Speed Zone Ahead | Recommended (2C.40-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |
| ![W3-5b](symbols/W3-5b.png) | **W3-5b** | Variable Speed Zone Ahead | Recommended (2C.40-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | — |
| ![W3-5c](symbols/W3-5c.png) | **W3-5c** | XX MPH Truck Speed | Recommended (2C.40-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | — |

- **[R]** 2C.40-01 (p.178) ◆ W3-5, W3-5a, W3-5c: A Reduced Speed Limit Ahead (W3-5 or W3-5a) or Truck Speed Zone Ahead (W3-5c) sign (see Figure 2C-9) should be used to inform road users of a reduced speed zone where the speed limit is being reduced by more than 10 mph, or where engineering judgment indicates the need for advance notice to comply with the posted speed limit ahead.
- **[R]** 2C.40-02 (p.178) ◆ W3-5b: A VARIABLE SPEED ZONE AHEAD (W3-5b) sign (see Figure 2C-9) should be used to inform road users of a zone where the speed limit is varied by time of day or as conditions change.
- **[M]** 2C.40-03 (p.178): If used, Reduced Speed Limit, Variable Speed Zone, or Truck Speed Zone Ahead signs shall be followed by a Speed Limit (R2-1) sign (see Figure 2B-3), with the Trucks (R2-2P) plaque (see Figure 2B-3) if applicable, installed at the beginning of the zone where the speed limit applies.
- **[M]** 2C.40-04 (p.178) ◆ W3-5, W3-5a, W3-5c: The speed limit displayed on the W3-5, W3-5a, and W3-5c signs shall be identical to the speed limit displayed on the subsequent Speed Limit sign.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-41"></a>
#### Section 2C.41 Intersection Warning Signs (W2-1 through W2-8)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W2-1](symbols/W2-1.png) | **W2-1** | Cross Road | Optional (2C.41-01) · *Auto* | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | 9A-1 |
| ![W2-2](symbols/W2-2.png) | **W2-2** | Side Road | Optional (2C.41-01) · *Auto* | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | 9A-1 |
| ![W2-3](symbols/W2-3.png) | **W2-3** | Intersection Warning | Optional (2C.41-01) | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | 9A-1 |
|  | **W2-3a** | Intersection Warning | Optional (2C.41-01) | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | — |
| ![W2-4](symbols/W2-4.png) | **W2-4** | T-Intersection | Optional (2C.41-01) · *Auto* | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | 9A-1 |
| ![W2-5](symbols/W2-5.png) | **W2-5** | Y-Intersection | Optional (2C.41-01) | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | 9A-1 |
| ![W2-6](symbols/W2-6.png) | **W2-6** | Circular Intersection | Optional (2C.41-01) · *Auto* | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | — |
|  | **W2-7** | Offset Side
Roads | Optional (2C.41-01) | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | — |
| ![W2-8](symbols/W2-8.png) | **W2-8** | Double Side Roads | Optional (2C.41-01) | 30 x 30 | 30 x 30 | 36 x 36 | — | 24 x 24 | 48 x 48 | 2C-1 p.148 | — |
| ![W16-12P](symbols/W16-12P.png) | **W16-12P** | Traffic Circle (plaque) | Optional | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.151 | — |
| ![W16-12aP](symbols/W16-12aP.png) | **W16-12aP** | Roundabout (plaque) | Optional | 24 x 12 | 24 x 12 | — | — | — | — | 2C-1 p.151 | — |

- [O] 2C.41-01 (p.179) ◆ W2-1, W2-2, W2-3, W2-3a, W2-4, W2-5: A Cross Road (W2-1), Side Road (W2-2, W2-3, or W2-3a), T-Intersection (W2-4), or Y-Intersection (W2-5) sign (see Figure 2C-10) may be used in advance of an intersection to indicate the presence of an intersection and the possibility of turning or entering traffic.
- [O] 2C.41-02 (p.180) ◆ W2-6: The Circular Intersection (W2-6) sign (see Figure 2C-10) may be installed in advance of a circular intersection (see Figures 2B-21 through 2B-23).
- **[R]** 2C.41-03 (p.180) ◆ W2-6: If an approach to a circular intersection has a statutory or posted speed limit of 40 mph or higher, the Circular Intersection (W2-6) sign should be installed in advance of the circular intersection.
- [O] 2C.41-04 (p.180) ◆ W16-12P, W16-12aP: An educational plaque (see Figure 2C-10) with a legend such as TRAFFIC CIRCLE (W16-12P) or ROUNDABOUT (W16-12aP) may be mounted below a Circular Intersection sign.
- **[R]** 2C.41-06 (p.180): The Intersection Warning sign should illustrate and depict the general configuration of the intersecting roadway, such as a cross road, side road, T-intersection, or Y-intersection.
- **[R]** 2C.41-07 (p.180) ◆ W2-4, W2-6: Intersection Warning signs, other than the Circular Intersection (W2-6) sign, the T-intersection (W2-4) sign, and the Grade Crossing and Intersection Advance Warning (W10-2, W10-3, W10-4, W10-11, and W10-12) signs (see Figure 8B-4) should not be used on approaches controlled by STOP signs, YIELD signs, or signals.
- **[R]** 2C.41-08 (p.180) ◆ W2-7: If an Intersection Warning sign is used where the side roads are not opposite of each other, the Offset Side Roads (W2-7) sign (see Figure 2C-10) should be used instead of the Cross Road sign.
- **[R]** 2C.41-09 (p.180) ◆ W2-8: If an Intersection Warning sign is used where two closely-spaced side roads are on the same side of the highway, the Double Side Roads (W2-8) sign (see Figure 2C-10) should be used instead of the Side Road sign.
- **[R]** 2C.41-10 (p.180) ◆ W2-7, W2-8: No more than two side roads should be depicted on the same side of the highway on a W2-7 or W2-8 sign, and no more than three side roads should be depicted on a W2-7 or W2-8 sign.
- [O] 2C.41-11 (p.180): When at least one side road is shown, the stem of an additional side road representing a significantly lower relative volume may be depicted using a line that is two-thirds the width of the through road based on engineering judgment.

*Also governed by Section 9C.02:*

- [O] 9C.02-01 (p.1066) ◆ W2-1, W2-2, W2-3, W2-3a, W2-4, W2-5: Intersection Warning (W2-1 through W2-5) signs (see Figure 9C-1) may be used on a roadway, street, or shared-use path in advance of an intersection to indicate the presence of an intersection and the possibility of turning or entering traffic.
- **[R]** 9C.02-02 (p.1066): When engineering judgment determines that the visibility of the intersection is limited on the shared-use path approach, Intersection Warning signs should be used.
- **[R]** 9C.02-03 (p.1066): Intersection Warning signs should not be used where the shared-use path approach to the intersection is controlled by a STOP sign, a YIELD sign, or a traffic control signal.

<a id="sec-2C-42"></a>
#### Section 2C.42 Actuated Advance Intersection Signs (W2-10 and W2-11)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **W2-10** | Traffic Entering When Flashing | Optional (2C.42-02) | 36 x 36 | 36 x 36 | 48 x 48 | — | — | — | 2C-1 p.148 | — |
|  | **W2-11** | Traffic Approaching | Optional (2C.42-02) | 36 x 36 | 36 x 36 | 48 x 48 | — | — | — | 2C-1 p.148 | — |

- [O] 2C.42-02 (p.180) ◆ W2-10: The TRAFFIC ENTERING WHEN FLASHING (W2-10) sign (see Figure 2C-10) may be used on the uncontrolled through roadway approach to a side or cross road stop-controlled intersection to warn of entering traffic from the side or cross road.
- [O] 2C.42-03 (p.180) ◆ W2-11: The TRAFFIC APPROACHING WHEN FLASHING (W2-11) sign (see Figure 2C-10) may be used on the side road stop-controlled approach to warn of traffic approaching on the uncontrolled through road.
- **[M]** 2C.42-04 (p.180): When used, the TRAFFIC ENTERING WHEN FLASHING sign and the TRAFFIC APPROACHING WHEN FLASHING sign shall be supplemented with a Warning Beacon (see Section 4S.03) that activates when a vehicle on a conflicting approach is detected.

*Also governed by Section 9C.02:*

- [O] 9C.02-01 (p.1066): Intersection Warning (W2-1 through W2-5) signs (see Figure 9C-1) may be used on a roadway, street, or shared-use path in advance of an intersection to indicate the presence of an intersection and the possibility of turning or entering traffic.
- **[R]** 9C.02-02 (p.1066): When engineering judgment determines that the visibility of the intersection is limited on the shared-use path approach, Intersection Warning signs should be used.
- **[R]** 9C.02-03 (p.1066): Intersection Warning signs should not be used where the shared-use path approach to the intersection is controlled by a STOP sign, a YIELD sign, or a traffic control signal.

<a id="sec-2C-43"></a>
#### Section 2C.43 Two-Direction Large Arrow Sign (W1-7)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W1-7](symbols/W1-7.png) | **W1-7** | Two-Direction Large Arrow | Mandatory (2C.43-01) | 48 x 24 | 48 x 24 | — | — | — | 60 x 30 | 2C-1 p.148 | 9A-1 |

- **[M]** 2C.43-01 (p.180): The Two-Direction Large Arrow (W1-7) sign (see Figure 2C-10) shall be a horizontal rectangle.
- **[M]** 2C.43-02 (p.180): If used, the Two-Direction Large Arrow sign shall be installed on the far side of a T-intersection in line with, and at approximately a right angle to, traffic approaching from the stem of the T-intersection.
- **[M]** 2C.43-03 (p.180): The Two-Direction Large Arrow sign shall not be used where there is no change in the direction of travel such as at the beginnings and ends of medians or at center piers.
- **[R]** 2C.43-04 (p.181): The Two-Direction Large Arrow sign should be visible for a sufficient distance to provide the road user with adequate time to react to the intersection configuration. Section 2C.44 Traffc Signal Oncoming Extended Green Signs (W25i -1 and W25-2)

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065): To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065): The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-2C-44"></a>
#### Section 2C.44 Traffic Signal Oncoming Extended Green Signs (W25-1 and W25-2)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W25-1](symbols/W25-1.png) | **W25-1** | Oncoming Traffic Has (May Have) | Mandatory (2C.44-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2C-1 p.151 | — |
| ![W25-2](symbols/W25-2.png) | **W25-2** | Oncoming Traffic Has (May Have) | Mandatory (2C.44-01) | 24 x 30 | 24 x 30 | — | — | — | — | 2C-1 p.151 | — |

- **[M]** 2C.44-01 (p.181): At locations where either a W25-1 or a W25-2 sign is required based on the provisions in Section 4F.01, the W25-1 or W25-2 sign (see Figure 2C-10) shall be installed near the left-most signal face for the approach.

<a id="sec-2C-45"></a>
#### Section 2C.45 Merge Signs and Plaque (W4-1, W4-5, and W4-5aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W4-1](symbols/W4-1.png) | **W4-1** | Merge | Optional (2C.45-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | 6H-1 |
| ![W4-5](symbols/W4-5.png) | **W4-5** | Entering Roadway Merge | Optional (2C.45-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |
| ![W4-5aP](symbols/W4-5aP.png) | **W4-5aP** | No Merge Area (plaque) | Optional (2C.45-01) | 18 x 24 | 18 x 24 | 24 x 30 | 24 x 30 | — | — | 2C-1 p.148 | 6H-1 |

- [O] 2C.45-01 (p.182) ◆ W4-1: A Merge (W4-1) sign (see Figure 2C-11) may be used to warn road users on the major roadway that merging movements might be encountered in advance of a point where lanes from two separate roadways converge as a single traffic lane and no turning conflict occurs.
- [O] 2C.45-02 (p.182): A Merge sign may also be installed on the side of the entering roadway to warn road users on the entering roadway of the merge condition.
- **[R]** 2C.45-03 (p.182): The Merge sign should be installed on the side of the major roadway where merging traffic will be encountered and in such a position as to not obstruct the road user’s view of entering traffic.
- **[R]** 2C.45-04 (p.183): When a Merge sign is installed on a major roadway, the symbol should be oriented right or left as appropriate to depict the side from which the merge occurs, with the arrow representing the major roadway and the curved stem representing the entering roadway (see Figure 2C-11)
- **[R]** 2C.45-05 (p.183) ◆ W4-5: When a Merge sign is installed on an entering roadway that curves before merging with the major roadway, such as a ramp with a curving horizontal alignment as it approaches the major roadway, the Entering Roadway Merge (W4-5) sign (see Figure 2C-11) should be used to better portray the actual geometric conditions to road users on the entering roadway.
- **[R]** 2C.45-06 (p.183): Where two roadways of approximately equal importance converge and merging movements are required, a Merge sign should be placed on each roadway.
- **[R]** 2C.45-07 (p.183): The Merge sign should not be used where two roadways converge and merging movements are not required.
- **[M]** 2C.45-08 (p.183): The Merge sign shall not be used in place of a Lane Ends (W4-2) sign (see Section 2C.47) where lanes of traffic moving on a single roadway must merge because of a reduction in the actual or usable pavement width.
- [O] 2C.45-09 (p.183) ◆ W4-5, W4-5aP: An Entering Roadway Merge (W4-5) sign with a NO MERGE AREA (W4-5aP) supplemental plaque (see Figure 2C-11) mounted below it may be used to warn road users on an entering roadway that they will encounter an abrupt merging situation without an acceleration lane at the downstream end of the ramp.
- [O] 2C.45-10 (p.183) ◆ W4-1, W4-5aP: A Merge (W4-1) sign with a NO MERGE AREA (W4-5aP) supplemental plaque mounted below it may be used to warn road users on the major roadway that traffic on an entering roadway will encounter an abrupt merging situation without an acceleration lane at the downstream end of the ramp.
- [O] 2C.45-11 (p.183) ◆ W4-5aP: For a yield-controlled channelized right-turn movement onto a roadway without an acceleration lane, a NO MERGE AREA (W4-5aP) supplemental plaque may be mounted below a Yield Ahead (W3-2) sign and/or below a YIELD (R1-2) sign when engineering judgment indicates that road users would expect an acceleration lane to be present.
- [S] 2C.45-12 (p.183) ◆ W4-1: Examples of the use of Merge (W4-1) signs are shown in Drawing A in Figure 2C-12.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-46"></a>
#### Section 2C.46 Added Lane Signs (W4-3 and W4-6)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W4-3](symbols/W4-3.png) | **W4-3** | Added Lane | Recommended (2C.46-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | 6H-1 |
| ![W4-6](symbols/W4-6.png) | **W4-6** | Entering Roadway Added Lane | Recommended (2C.46-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |

- **[R]** 2C.46-01 (p.183) ◆ W4-3: The Added Lane (W4-3) sign (see Figure 2C-11) should be installed in advance of a point where two roadways converge and merging movements are not required. When possible, the Added Lane sign should be placed such that it is visible from both roadways; if this is not possible, an Added Lane sign should be placed on the side of each roadway.
- **[R]** 2C.46-02 (p.183) ◆ W4-3: When an Added Lane (W4-3) sign is installed on a major roadway, the symbol should be oriented right or left as appropriate to depict the side from which the entering roadway converges, with the straight arrow representing the major roadway and the curved arrow representing the entering roadway. The sign should be located on the side of the major roadway from which the entering roadway converges.
- **[R]** 2C.46-03 (p.183) ◆ W4-6: When an Added Lane sign is to be installed on a roadway that curves before converging with another roadway that has a tangent alignment at the point of convergence, the Entering Roadway Added Lane (W4-6) sign (see Figure 2C-11) should be used to better portray the actual geometric conditions to road users on the curving roadway.
- [S] 2C.46-04 (p.183): Examples of the use of Added Lane (W4-3) and Entering Roadway Added Lane (W4-6) signs are shown in Drawing B in Figure 2C-12.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-47"></a>
#### Section 2C.47 Lane Ends Signs (W4-2 and W9-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W4-2](symbols/W4-2.png) | **W4-2** | Lane Ends | Recommended (2C.47-03) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | 30 x 30* | — | 2C-1 p.148 | 6H-1 |
| ![W9-1](symbols/W9-1.png) | **W9-1** | Right (Left) Lane Ends | Recommended (2C.47-03) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 30 x 30* | 48 x 48 | 2C-1 p.149 | 6H-1 |

- [S] 2C.47-01 (p.183): The Lane Ends (W4-2) and RIGHT (LEFT) LANE ENDS (W9-1) signs (see Figure 2C-11) are used to warn of the reduction in the number of traffic lanes in the direction of travel.
- [S] 2C.47-02 (p.183): The sequence of the W4-2 and W9-1 signs is illustrated in Figure 2C-13.
- **[R]** 2C.47-03 (p.183) ◆ W4-2: The Lane Ends (W4-2) sign should be installed at the advance placement distance in accordance with Table 2C-3.
- [O] 2C.47-04 (p.186) ◆ W9-1: A RIGHT (LEFT) LANE ENDS (W9-1) sign may be installed in advance of the Lane Ends sign to provide additional warning that a lane is ending and that a merging maneuver will be required.
- **[R]** 2C.47-05 (p.186) ◆ W9-1: If a W9-1 sign is installed, a Distance (W16-2P series or W16-3P series) plaque (see Figure 2C-16) should be installed below the W9-1 sign.
- **[R]** 2C.47-06 (p.186): On one-way streets or on divided highways where the left-hand lane is ending and the width of the median will permit, the W9-1 and W4-2 signs should be placed facing approaching traffic on the left-hand side or median.
- [O] 2C.47-07 (p.186) ◆ W4-2: Where a lane ends a distance beyond the intersection that is less than the advance placement distance indicated in Table 2C-3, the W4-2 sign may be located at the far side of the intersection (see Sheet 4 of Figure 2C-13).
- **[R]** 2C.47-08 (p.186): When the W4-2 sign is located at the far side of the intersection in accordance with Paragraph 7 of this Section, the W9-1 sign should be placed upstream of the intersection with the appropriate distance plaque.
- **[R]** 2C.47-10 (p.187): Lane Ends signs should not be installed in advance of the downstream end of an acceleration lane.
- **[M]** 2C.47-11 (p.187): The W4-2 and W9-1 signs shall not be used in dropped lane situations. In dropped lane situations on conventional roads at intersections, regulatory signs (see Section 2B.28) shall be used to inform road users that a through lane becomes a mandatory turn lane.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 6H.08:*

- [O] 6H.08-01 (p.805) ◆ W4-2: The Lane Ends (W4-2) sign (see Figure 6H-1) may be used to warn drivers of the reduction in the number of lanes for moving motor vehicle traffic in the direction of travel on a multi-lane roadway.
- **[R]** 6H.08-02 (p.805): The MERGE HERE TAKE TURNS (W9-2a) sign (see Figure 6H-1) should be used to identify the merge point at which vehicles from alternate lanes take turns merging during Late Merge applications (see Section 6N.19).

<a id="sec-2C-48"></a>
#### Section 2C.48 Lanes Merge Signs (W9-4 and W4-8)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W4-8](symbols/W4-8.png) | **W4-8** | Single Lane Transition | Optional (2C.48-03) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 2C-1 p.148 | — |
| ![W9-4](symbols/W9-4.png) | **W9-4** | Lanes Merge | Optional (2C.48-03) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 30 x 30* | 48 x 48 | 2C-1 p.149 | — |

- [S] 2C.48-01 (p.187): The LANES MERGE (W9-4) and Single-Lane Transition (W4-8) signs (see Figure 2C-11) are used to warn of a merge of two lanes to one in the same direction of travel with a merging maneuver required for each lane (see Sheet 5 of Figure 2C-13). This type of merge is for a geometric condition where both approach lanes merge into a single lane, not where one lane merges into the other. Section 6H.08 contains information about the use of the late merge sign.
- **[R]** 2C.48-02 (p.187) ◆ W4-8: The Single-Lane Transition (W4-8) sign should be located at the advance placement distance in accordance with Table 2C-3.
- [O] 2C.48-03 (p.187): The Lanes Merge (W9-4) sign may be used in advance of the W4-8 sign to provide additional warning that both lanes form a single lane and that a merging maneuver is needed for the traffic in each lane.

<a id="sec-2C-49"></a>
#### Section 2C.49 HEAVY MERGE FROM LEFT (RIGHT) Sign (W4-7)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W4-7](symbols/W4-7.png) | **W4-7** | Heavy Merge from Right (Left) | Optional (2C.49-01) | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | 2C-1 p.148 | — |

- [O] 2C.49-01 (p.188): The HEAVY MERGE FROM LEFT (RIGHT) (W4-7) sign (see Figure 2C-11) may be used to supplement a W4-1 sign at multilane approaches to congested areas to inform road users that it is desirable for through traffic to move out of a lane that will be occupied by a high volume of entering traffic. If used, the W4-7 sign may be supplemented with a W16-2P series or W16-3P series plaque (see Section 2C.61).

<a id="sec-2C-50"></a>
#### Section 2C.50 RIGHT (LEFT) LANE FOR EXIT ONLY Sign (W9-7)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W9-7](symbols/W9-7.png) | **W9-7** | Right (Left) Lane for Exit Only | Recommended (2C.50-02) | 132 x 72 | 132 x 72 | 132 x 72 | 132 x 72 | — | — | 2C-1 p.149 | — |

- [O] 2C.50-01 (p.188): depart the roadway at the next exit.
- **[R]** 2C.50-02 (p.188): If used, the W9-7 sign should be installed upstream from the first overhead guide sign that contains an EXIT ONLY sign panel or upstream from the first RIGHT (LEFT) LANE MUST EXIT (R3-33) regulatory sign, if used, whichever is farther upstream from the exit.
- [O] 2C.50-03 (p.188): A legend or plaque displaying the distance may be added to the W9-7 sign where the distance along the dropped lane between the sign and the exit ramp is greater than 1 mile. Sect. 2C.49 to 2C.50

<a id="sec-2C-51"></a>
#### Section 2C.51 Two-Way Traffc Sign (W6i -3)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W6-3](symbols/W6-3.png) | **W6-3** | Two-Way Traffic | Recommended (2C.51-01) · *Auto* | 36 x 36 | 36 x 36 | 48 x 48 | 48 x 48 | — | — | 2C-1 p.148 | 6H-1 |

- **[R]** 2C.51-01 (p.189): A Two-Way Traffic (W6-3) sign (see Figure 2C-11) should be used to warn road users of a transition from a multi-lane divided section of roadway to a two-lane, two-way section of roadway.
- **[R]** 2C.51-02 (p.189): A Two-Way Traffic (W6-3) sign with an AHEAD (W16-9P) plaque (see Figure 2C-16) should be used to warn road users of a transition from a one-way street to a two-lane, two-way section of roadway (see Figure 2B-18).

*Also governed by Section 6H.16:*

- **[R]** 6H.16-01 (p.806): When one roadway of a normally-divided highway is closed, with two-way vehicular traffic maintained on the other roadway, the Two-Way Traffic (W6-3) sign (see Figure 6H-1) should be used at the beginning of the twoway vehicular traffic section and at intervals to remind road users of opposing vehicular traffic. Section 6H.17 Narrow Two-Way Traffc Sign (W6i -4)

<a id="sec-2C-52"></a>
#### Section 2C.52 Two-Way Traffc on a Threei -Lane Roadway Signs (W6-5 and W6-5a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W6-5](symbols/W6-5.png) | **W6-5** | Two-Way Traffic (3-Lane) | Optional (2C.52-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | — | — | 2C-1 p.148 | — |
| ![W6-5a](symbols/W6-5a.png) | **W6-5a** | Two-Way Traffic (3-Lane) | Optional (2C.52-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | — | — | 2C-1 p.148 | — |

- [O] 2C.52-01 (p.190): The Two-Way Traffic on a Three-Lane Roadway (W6-5 and W6-5a) signs (see Figure 2C-11) may be installed along three-lane roadways with two lanes in one direction and one in the opposing direction.

<a id="sec-2C-53"></a>
#### Section 2C.53 NO PASSING ZONE Sign (W14-3)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W14-3](symbols/W14-3.png) | **W14-3** | No Passing Zone | Mandatory (2C.53-01) · *Auto* | 48 x 48 x 36 | 48 x 48 x 36 | 64 x 64 x 48 | 64 x 64 x 48 | 40 x 40 x 30 | 64 x 64 x 48 | 2C-1 p.150 | 6H-1 |

- **[M]** 2C.53-01 (p.190): The NO PASSING ZONE (W14-3) sign (see Figure 2C-11) shall be a pennant-shaped isosceles triangle with its longer axis horizontal and pointing to the right. When used, the NO PASSING ZONE sign shall be installed on the left-hand side of the roadway at the beginning of no-passing zones identified by pavement markings or DO NOT PASS signs or both (see Sections 2B.36 and 3B.03).

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-2C-54"></a>
#### Section 2C.54 Vehicular Traffc Warning Signs (W8i -6, W11-1, W11-5, W11-8, W11-10, W11-11, W11- 12P, W11-14, W11-15, and W11-15a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W8-6](symbols/W8-6.png) | **W8-6** | Truck Crossing | Optional (2C.54-01) | 36 x 36 | 36 x 36 | 36 x 36 | 48 x 48 | 24 x 24* | 48 x 48 | 2C-1 p.149 | 6H-1 |
|  | **W11-1** | Bicycle | Optional (2C.54-01) · *Auto* | 30 x 30 | 30 x 30 | 36 x 36 | — | — | 48 x 48 | 2C-1 p.149 | 9A-1 |
| ![W11-5](symbols/W11-5.png) | **W11-5** | Farm Vehicle | Optional (2C.54-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-8](symbols/W11-8.png) | **W11-8** | Emergency Vehicle | Optional (2C.54-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | — |
| ![W11-10](symbols/W11-10.png) | **W11-10** | Truck | Optional (2C.54-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | 6H-1 |
| ![W11-11](symbols/W11-11.png) | **W11-11** | Golf Cart | Optional (2C.54-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | — |
| ![W11-12P](symbols/W11-12P.png) | **W11-12P** | Emergency Signal Ahead (plaque) | Optional (2C.54-01) · *Auto* | 36 x 30 | 36 x 30 | 36 x 30 | — | — | — | 2C-1 p.150 | — |
| ![W11-14](symbols/W11-14.png) | **W11-14** | Horse-Drawn Vehicle | Optional (2C.54-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | — |
|  | **W11-15** | Trail Crossing | Optional (2C.54-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | 9A-1 |
| ![W11-15P](symbols/W11-15P.png) | **W11-15P** | Trail Crossing (plaque) | Optional (2C.54-05) | 24 x 18 | 24 x 18 | 30 x 24 | — | — | 36 x 30 | 2C-1 p.150 | 9A-1 |
|  | **W11-15a** | Trail Crossing | Optional (2C.54-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | — |

- [O] 2C.54-01 (p.191) ◆ W8-6, W11-1, W11-5, W11-8, W11-10, W11-11, W11-12P, W11-14, W11-15, W11-15a: Vehicular Traffic Warning (W8-6, W11-1, W11-5, W11-8, W11-10, W11-11, W11-12P, W11-14, W11-15, and W11-15a) signs (see Figure 2C-14) may be used to alert road users to locations where unexpected entries into the roadway by trucks, bicycles, farm vehicles, emergency vehicles, golf carts, horse-drawn vehicles, or other vehicles might occur. The TRUCK CROSSING (W8-6) word message sign may be used as an alternate to the Truck (W11-10) symbol sign.
- **[R]** 2C.54-03 (p.191): Vehicular Traffic Warning signs should be used only at locations where the road user’s sight distance is restricted, or the condition, activity, or entering traffic would be unexpected.
- **[R]** 2C.54-04 (p.191): If the condition or activity is seasonal or temporary, the Vehicular Traffic Warning sign should be removed or covered when the condition or activity does not exist.
- [O] 2C.54-05 (p.191) ◆ W11-15, W11-15P, W11-15a: The Trail Crossing (W11-15) sign may be used where both bicyclists and pedestrians might be crossing the roadway, such as at an intersection with a shared-use path. A TRAIL X-ING (W11-15P) supplemental plaque (see Figure 2C-14) may be mounted below the W11-15 sign. The TRAIL CROSSING (W11-15a) sign may be used to warn of shared-use path crossings where pedestrians, bicyclists, and other user groups might be crossing the roadway.
- [O] 2C.54-06 (p.191) ◆ W11-1, W11-15, W11-15a: The W11-1, W11-15, and W11-15a signs and their related supplemental plaques may have a fluorescent yellow- green background with a black legend and border.
- [O] 2C.54-07 (p.191): Supplemental plaques (see Figure 2C-16 and Section 2C.57) with legends such as AHEAD, XX FEET, NEXT XX MILES, IN STREET, or IN ROAD may be mounted below Vehicular Traffic Warning signs to provide advance notice to road users of unexpected entries.
- **[R]** 2C.54-08 (p.191) ◆ W11-15, W11-15a: If used in advance of a trail crossing, a W11-15 or W11-15a sign should be supplemented with an AHEAD or XX FEET plaque to inform road users that they are approaching a point where crossing activity might occur.
- **[M]** 2C.54-09 (p.192) ◆ W11-1, W11-11, W11-15, W11-15a: If a post-mounted W11-1, W11-11, W11-15, or W11-15a sign is placed at the location of the crossing point where golf carts, pedestrians, bicyclists, or other shared-use path users might be crossing the roadway, a diagonal downward-pointing arrow (W16-7P) plaque (see Figure 2C-16 and Section 2C.63) shall be mounted below the sign. If the W11-1, W11-11, W11-15, or W11-15a sign is mounted overhead, the W16-7P supplemental plaque shall not be used.
- **[M]** 2C.54-10 (p.192): A Vehicular Traffic Warning sign assembly shall not be installed on an approach controlled by a STOP or a YIELD sign, except as provided in Paragraphs 11 and 12 of this Section.
- [O] 2C.54-11 (p.192): The Vehicular Traffic Warning sign assembly may be installed on an approach to a circular intersection controlled by a YIELD sign where the crosswalk is at least 20 feet in advance of the yield point at the entrance to the circulatory roadway.
- [O] 2C.54-12 (p.192): At a signalized or stop-controlled intersection the Vehicular Traffic Warning sign assembly may be installed on an approach to a channelized right turn lane controlled by a YIELD sign where the crosswalk is at least 20 feet in advance of the yield point.
- [O] 2C.54-13 (p.192) ◆ W11-1, W11-11, W11-15, W11-15a: The crossing location identified by a W11-1, W11-11, W11-15, or W11-15a sign may be defined with crosswalk markings (see Chapter 3C).
- **[M]** 2C.54-14 (p.192) ◆ W11-8, W11-12P: The Emergency Vehicle (W11-8) sign (see Figure 2C-14) with the EMERGENCY SIGNAL AHEAD (W11-12P) supplemental plaque (see Figure 2C-14) shall be placed in advance of all emergency-vehicle traffic control signals (see Chapter 4M).
- [O] 2C.54-15 (p.192) ◆ W11-8: The Emergency Vehicle (W11-8) sign, or a word message sign indicating the type of emergency vehicle (such as rescue squad), may be used in advance of the emergency-vehicle station when no emergency-vehicle traffic control signal is present.
- [O] 2C.54-16 (p.192): A Warning Beacon (see Section 4S.03) may be used with any Vehicular Traffic Warning sign to indicate specific periods when the condition or activity is present or is likely to be present, or to provide enhanced sign conspicuity.
- [O] 2C.54-17 (p.192): A supplemental WHEN FLASHING (W16-13P) plaque (see Figure 2C-16) may be used with any Vehicular Traffic Warning sign that is supplemented with a Warning Beacon to indicate specific periods when the condition or activity is present or is likely to be present.

*Also governed by Section 6H.21:*

- [O] 6H.21-01 (p.807) ◆ W8-6, W11-10: Motorized Traffic (W8-6 and W11-10) signs may be used to alert road users to locations where unexpected travel on the roadway or entries into or departures from the roadway by construction vehicles might occur. The TRUCK CROSSING (W8-6) word message sign may be used as an alternate to the Truck (W11-10) symbol sign (see Figure 6H-1) where there is an established construction vehicle crossing of the roadway.

*Also governed by Section 9C.04:*

- [S] 9C.04-01 (p.1066) ◆ W11-1: The Bicycle Warning (W11-1) sign (see Figure 9C-1) alerts the road user to unexpected entries into the roadway by bicyclists, and other crossing activities that might cause conflicts. These conflicts might be relatively confined, or might occur randomly over a segment of roadway.
- [O] 9C.04-03 (p.1066) ◆ W11-15, W11-15P: The Trail Crossing (W11-15) sign (see Figure 9C-1) may be used where both bicyclists and pedestrians might be crossing the roadway, such as at an intersection with a shared-use path. A TRAIL X-ING (W11-15P) supplemental plaque may be mounted below the W11-15 sign.
- [O] 9C.04-04 (p.1067) ◆ W11-15: If used in advance of a trail crossing, a W11-15 or W11-15a sign should be supplemented with an AHEAD (W16-9P) or XX FEET (W16-2P or W16-2aP) plaque to inform road users that they are approaching a point where crossing activity might occur.
- **[R]** 9C.04-05 (p.1067): If used in advance of a specific crossing point, the Bicycle Warning or Trail Crossing sign should be placed at a distance in advance of the crossing location that complies with Table 2C-3.
- **[M]** 9C.04-06 (p.1067): Bicycle Warning and Trail Crossing signs, when used at the location of the crossing, shall be supplemented with a diagonal downward-pointing arrow (W16-7P) plaque to show the location of the crossing.
- [O] 9C.04-07 (p.1067): A fluorescent yellow-green background color with a black legend and border may be used for Bicycle Warning and Trail Crossing signs and supplemental plaques.
- **[R]** 9C.04-08 (p.1067): When the fluorescent yellow-green background color is used, a systematic approach featuring one background color within a zone or area should be used. The mixing of standard yellow and fluorescent yellowgreen backgrounds within a zone or area should be avoided.

*Also governed by Section 9C.08:*

- [O] 9C.08-02 (p.1068) ◆ W11-1: In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).

<a id="sec-2C-55"></a>
#### Section 2C.55 Non-Vehicular Warning Signs (W11-2, W11-3, W11-4, W11-6, W11-7, W11-9, and W11-16 through W11-22)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W11-2](symbols/W11-2.png) | **W11-2** | Pedestrian | Optional (2C.55-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2C-1 p.149 | 9A-1 |
| ![W11-3](symbols/W11-3.png) | **W11-3** | Deer | Optional (2C.55-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-4](symbols/W11-4.png) | **W11-4** | Cattle | Optional (2C.55-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-6](symbols/W11-6.png) | **W11-6** | Snowmobile | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-7](symbols/W11-7.png) | **W11-7** | Equestrian | Optional (2C.55-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
|  | **W11-9** | Handicapped | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | — | 48 x 48 | 2C-1 p.150 | — |
| ![W11-16](symbols/W11-16.png) | **W11-16** | Bear | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-17](symbols/W11-17.png) | **W11-17** | Sheep | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-18](symbols/W11-18.png) | **W11-18** | Bighorn Sheep | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-19](symbols/W11-19.png) | **W11-19** | Donkey | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-20](symbols/W11-20.png) | **W11-20** | Elk | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-21](symbols/W11-21.png) | **W11-21** | Moose | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W11-22](symbols/W11-22.png) | **W11-22** | Wild Horse | Optional (2C.55-01) | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.149 | — |
| ![W16-9P](symbols/W16-9P.png) | **W16-9P** | Ahead (plaque) | Optional (2C.55-01) · *Auto* | 24 x 12 | 24 x 12 | 30 x 18 | — | — | 30 x 18 | 2C-1 p.150 | 7B-1, 9A-1 |
| ![W16-13P](symbols/W16-13P.png) | **W16-13P** | When Flashing (plaque) | Optional (2C.55-15) | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.151 | — |

- [O] 2C.55-01 (p.192) ◆ W11-2, W11-3, W11-4, W11-6, W11-7, W11-9, W11-16, W11-17, W11-18, W11-19, W11-20, W11-21, W11-22: Non-Vehicular Warning (W11-2, W11-3, W11-4, W11-6, W11-7, W11-9, and W11-16 through W11-22) signs (see Figure 2C-15) may be used to alert road users in advance of locations where unexpected entries into the roadway might occur or where shared use of the roadway by pedestrians, animals, or equestrians might occur.
- **[R]** 2C.55-03 (p.192) ◆ W11-2, W11-6, W11-7, W11-9: If used in advance of a pedestrian, snowmobile, or equestrian crossing, the W11-2, W11-6, W11-7, and W11-9 signs should be supplemented with plaques (see Figure 2C-16 and Section 2C.61) with the legend AHEAD or XX FEET to inform road users that they are approaching a point where crossing activity might occur.
- **[M]** 2C.55-04 (p.192) ◆ W11-2, W11-6, W11-7, W11-9: If a post-mounted W11-2, W11-6, W11-7, or W11-9 sign is placed at the location of the crossing point where pedestrians, snowmobilers, or equestrians might be crossing the roadway, a diagonal downwardpointing arrow (W16-7P) plaque (see Figure 2C-16 and Section 2C.63) shall be mounted below the sign. If the W11-2, W11-6, W11-7, or W11-9 sign is mounted overhead, the W16-7P plaque shall not be used.
- **[M]** 2C.55-05 (p.192): A Non-Vehicular Warning sign assembly shall not be installed on an approach controlled by a STOP or a YIELD sign, except as provided in Paragraphs 6 and 7 of this Section.
- [O] 2C.55-06 (p.192): The Non-Vehicular Warning sign assembly may be installed on an approach to a circular intersection controlled by a YIELD sign where the crosswalk is at least 20 feet in advance of the yield point at the entrance to a circulatory roadway.
- [O] 2C.55-07 (p.193): At a signalized or stop-controlled intersection the Non-Vehicular Warning sign assembly may be installed on an approach to a channelized right turn lane controlled by a YIELD sign where the crosswalk is at least 20 feet in advance of the yield point.
- [O] 2C.55-08 (p.193) ◆ W11-2: A Pedestrian Crossing (W11-2) sign may be placed overhead or may be post-mounted with a diagonal downward-pointing arrow (W16-7P) plaque at the crosswalk location where Yield Here To (Stop Here For) Pedestrians signs (see Section 2B.19) have been installed in advance of the crosswalk.
- **[M]** 2C.55-09 (p.193) ◆ W11-2: If a W11-2 sign has been post-mounted at the crosswalk location where a Yield Here To (Stop Here For) Pedestrians sign is used on the approach, the Yield Here To (Stop Here For) Pedestrians sign shall not be placed on the same post as the W11-2 sign.
- [O] 2C.55-10 (p.193) ◆ W11-2: An advance Pedestrian Crossing (W11-2) sign with an AHEAD or a distance supplemental plaque may be used in conjunction with a Yield Here To (Stop Here For) Pedestrians sign on the approach to the same crosswalk.
- [O] 2C.55-11 (p.193) ◆ W11-2, W11-6, W11-7, W11-9: The crossing location identified by a W11-2, W11-6, W11-7, or W11-9 sign may be defined with crosswalk markings (see Chapter 3C).
- [O] 2C.55-12 (p.193) ◆ W11-2, W11-9: The W11-2 and W11-9 signs and their related supplemental plaques may have a fluorescent yellow-green background with a black legend and border.
- **[R]** 2C.55-13 (p.193): When a fluorescent yellow-green background is used, a systematic approach featuring one background color within a zone or area should be used. The mixing of standard yellow and fluorescent yellow-green backgrounds within a selected site area should be avoided.
- [O] 2C.55-14 (p.193): A Warning Beacon (see Section 4S.03) may be used with any Non-Vehicular Warning sign to indicate specific periods when the condition or activity is present or is likely to be present, or to provide enhanced sign conspicuity.
- [O] 2C.55-15 (p.193) ◆ W16-13P: A supplemental WHEN FLASHING (W16-13P) plaque (see Figure 2C-16) may be used with any NonVehicular Warning sign that is supplemented with a Warning Beacon to indicate specific periods when the condition or activity is present or is likely to be present.

*Also governed by Section 7B.02:*

- [S] 7B.02-02 (p.972) ◆ W16-9P: The School (S1‑1) sign (see Figure 7B‑1) has the following four applications: A. School Area – the S1‑1 sign can be used to warn road users that they are approaching a school area that might include school buildings or grounds, a school crossing, or school related activity adjacent to the highway. B. School Zone – the S1‑1 sign can be used to identify the location of the beginning of a designated school zone. C. School Advance Crossing – if combined with an AHEAD (W16‑9P) plaque or an XX FEET (W16‑2P or W16‑2aP) plaque to comprise the School Advance Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn road users that they are approaching a crossing where schoolchildren cross the roadway (see Section 7B.03). D. School Crossing – if combined with a diagonal downward‑pointing arrow (W16‑7P) plaque to comprise the School Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn approaching road users of the location of a crossing where schoolchildren cross the roadway (see Section 7B.03).

*Also governed by Section 7B.03:*

- **[M]** 7B.03-01 (p.976) ◆ W16-9P: The School Advance Crossing assembly (see Figure 7B‑1) shall consist of a School (S1‑1) sign supplemented with an AHEAD (W16‑9P) plaque or an XX FEET (W16‑2P or W16‑2aP) plaque.
- [O] 7B.03-05 (p.976) ◆ W16-9P: A 12‑inch reduced size in‑street School (S1‑1) sign (see Figure 7B‑1), installed in compliance with the mounting height and special mounting support requirements for an In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) sign (see Section 2B.20), may be used in advance of a school crossing to supplement the post‑mounted school warning signs. A 12 x 6‑inch reduced size AHEAD (W16‑9P) plaque (see Figure 7B‑1) may be mounted below the reduced size in‑street School (S1‑1) sign.

*Also governed by Section 9C.04:*

- [O] 9C.04-04 (p.1067) ◆ W16-9P: If used in advance of a trail crossing, a W11-15 or W11-15a sign should be supplemented with an AHEAD (W16-9P) or XX FEET (W16-2P or W16-2aP) plaque to inform road users that they are approaching a point where crossing activity might occur.

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-2C-56"></a>
#### Section 2C.56 Playground Sign (W15-1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **W15-1** | Playground | Optional (2C.56-01) · *Auto* | 30 x 30* | 36 x 36 | 36 x 36 | — | 24 x 24* | 48 x 48 | 2C-1 p.150 | 9A-1 |

- [O] 2C.56-01 (p.194): The Playground (W15-1) sign (see Figure 2C-15) may be used to give advance warning of a designated children’s playground that is located adjacent to the road.
- [O] 2C.56-02 (p.194): The Playground sign may have a fluorescent yellow-green background with a black legend and border.
- **[R]** 2C.56-03 (p.194): If the access to the playground area requires a roadway crossing, the application of crosswalk pavement markings (see Chapter 3C) and a Non-Vehicular Warning sign (see Section 2C.55) should be considered.

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-2C-59"></a>
#### Section 2C.59 Advisory Speed Plaque (W13-1P) and Confirmation Advisory Speed Plaque (W13-1aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W13-1P](symbols/W13-1P.png) | **W13-1P** | Advisory Speed (plaque) | Optional (2C.59-01) · *Auto* | 18 x 18 | 18 x 18 | 24 x 24 | 30 x 30 | — | 30 x 30 | 2C-1 p.150 | 6H-1 |
| ![W13-1aP](symbols/W13-1aP.png) | **W13-1aP** |  | Optional (2C.59-01) | 48 x 15 | 48 x 15 | 60 x 18 | 60 x 18 | — | — | 2C-1 p.150 | — |

- [O] 2C.59-01 (p.196) ◆ W13-1P: The Advisory Speed (W13-1P) plaque (see Figure 2C-1) may be used to supplement an advance warning sign to indicate the advisory speed for a condition.
- [O] 2C.59-02 (p.196) ◆ W13-1aP: The Confirmation Advisory Speed (W13-1aP) plaque (see Figure 2C-1) may be used to supplement a One- Direction Large Arrow (W1-6) sign on the outside of a turn or curve in line with and at approximately a right angle to approaching traffic.
- **[M]** 2C.59-03 (p.196): The use of the Advisory Speed and Confirmation Advisory Speed plaques for horizontal curves shall be in accordance with Section 2C.06 and Table 2C-6. The speed differential in Table 2C-6 shall be the difference between the advisory speed for the horizontal curve and the posted speed limit, statutory speed limit, or the 85th percentile speed on the approach to the curve. The Advisory Speed plaque shall also be used where an engineering study indicates a need to advise road users of the advisory speed for other roadway conditions.
- **[M]** 2C.59-04 (p.196): The speed displayed on the Advisory Speed and Confirmation Advisory Speed plaques shall be a multiple of 5 mph.
- **[M]** 2C.59-05 (p.196): Except in emergencies or when the condition is temporary, an Advisory Speed or Confirmation Advisory Speed plaque shall not be installed until the advisory speed has been determined by an engineering study.
- **[M]** 2C.59-06 (p.196): The Advisory Speed plaque shall only be used to supplement an advance warning sign. The Advisory Speed plaque or the Confirmation Advisory Speed plaque shall not be installed as a separate sign installation.
- **[R]** 2C.59-07 (p.196): The Advisory Speed plaque, if used with a sign that is also supplemented with another plaque, such as an Advance Street Name plaque (see Section 2C.65), should be mounted immediately below the primary warning sign with any other plaque mounted below the Advisory Speed plaque.
- **[M]** 2C.59-08 (p.196): The Confirmation Advisory Speed plaque shall only be used to supplement a One-Direction Large Arrow (W1-6) sign (see Section 2C.10) or an Exit Gore (E5-1 series) (see Section 2E.26) sign and shall not be installed as a separate sign installation.
- **[M]** 2C.59-09 (p.196): The advisory speed shall be determined by an engineering study that follows established engineering practices.
- **[R]** 2C.59-10 (p.196): The advisory speed should be determined based on free-flowing traffic conditions.
- **[R]** 2C.59-11 (p.196): Because changes in conditions, such as roadway geometrics, surface characteristics, or sight distance, might affect the advisory speed, each location should be evaluated periodically or when conditions change.
- **[M]** 2C.59-15 (p.196): mph or more Required 1 See Section 2C.59

*Also governed by Section 6H.32:*

- [O] 6H.32-01 (p.809) ◆ W13-1P: In combination with a warning sign, an Advisory Speed (W13-1P) plaque (see Figure 6H-1) may be used to indicate a recommended speed through the TTC zone.
- **[M]** 6H.32-02 (p.809): The Advisory Speed plaque shall not be used in conjunction with any sign other than a warning sign, nor shall it be used alone. When used with orange TTC zone signs, this plaque shall have a black legend and border on an orange background. The plaque shall be at least 24 x 24 inches in size when used with a sign that is 36 x 36 inches or larger. Except in emergencies, an Advisory Speed plaque shall not be mounted until the recommended speed is determined by the highway agency.

<a id="sec-2C-60"></a>
#### Section 2C.60 NEW Plaque (W16-15P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-15P](symbols/W16-15P.png) | **W16-15P** | New (plaque) | Optional | 24 x 12 | 24 x 12 | — | — | — | — | 2C-1 p.151 | — |

- [O] 2C.60-01 (p.197): A NEW (W16-15P) plaque (see Figure 2C-16) may be mounted above a regulatory sign when a new regulation takes effect in order to alert road users to the new traffic regulation. A NEW plaque may also be mounted above an advance warning sign (such as a Signal Ahead sign for a newly-installed traffic control signal) for a warning of a new traffic condition.
- **[R]** 2C.60-02 (p.197): The NEW plaque should be removed no later than 6 months after it was installed.

<a id="sec-2C-61"></a>
#### Section 2C.61 Distance Plaques (W16-2 Series, W16-3 Series, W16-4P, and W7-3aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W7-3aP](symbols/W7-3aP.png) | **W7-3aP** | Next XX Miles (plaque) | Optional (2C.61-01) | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.149 | 6H-1 |
| ![W16-2P](symbols/W16-2P.png) | **W16-2P** | XX Feet (2-line plaque) | Optional (2C.61-01) | 24 x 18 | 24 x 18 | 30 x 24 | 30 x 24 | — | 30 x 24 | 2C-1 p.150 | 7B-1, 9A-1, 6H-1 |
| ![W16-2aP](symbols/W16-2aP.png) | **W16-2aP** | XX Ft (1-line plaque) | Optional (2C.61-01) | 24 x 12 | 24 x 12 | — | — | — | 30 x 18 | 2C-1 p.150 | 7B-1, 9A-1 |
| ![W16-3P](symbols/W16-3P.png) | **W16-3P** | XX Miles (2-line plaque) | Optional (2C.61-01) | 30 x 24 | 30 x 24 | — | — | — | — | 2C-1 p.150 | — |
| ![W16-3aP](symbols/W16-3aP.png) | **W16-3aP** | XX Miles (1-line plaque) | Optional (2C.61-01) | 30 x 12 | 30 x 12 | — | — | — | — | 2C-1 p.150 | — |
| ![W16-4P](symbols/W16-4P.png) | **W16-4P** | Next XX Feet (plaque) | Optional (2C.61-01) | 30 x 24 | 30 x 24 | — | — | — | — | 2C-1 p.150 | — |

- [O] 2C.61-01 (p.197) ◆ W16-2P, W16-2aP, W16-3P, W16-3aP: The Distance Ahead (W16-2 series and W16-3 series) plaques (see Figure 2C-16) may be used to inform the road user of the distance to the condition indicated by the warning sign.
- [O] 2C.61-02 (p.197) ◆ W7-3aP, W16-4P: The Next Distance (W7-3aP and W16-4P) plaques (see Figures 2C-5 and 2C-16) may be used to inform road users of the length of roadway over which the condition indicated by the warning sign exists.

*Also governed by Section 2C.64:*

- **[R]** 2C.64-01 (p.197) ◆ W7-3aP: Hill-Related (W7-2 series and W7-3 series) plaques (see Figure 2C-5) or other appropriate legends and larger signs should be used for emphasis or where special hill characteristics exist.
- **[R]** 2C.64-02 (p.197) ◆ W7-3aP: On longer grades, the use of a distance (W7-3aP or W7-3bP) plaque (see Figure 2C-5) at periodic intervals of approximately 1-mile spacing should be considered.

*Also governed by Section 6H.01:*

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

*Also governed by Section 6H.33:*

- [O] 6H.33-01 (p.809) ◆ W7-3aP: In combination with a warning sign, a Supplementary Distance (W7-3aP) plaque (see Figure 6H-1) with the legend NEXT XX MILES may be used to indicate the length of highway over which a work activity is being conducted, or over which a condition exists in the TTC zone.
- [O] 6H.33-02 (p.810): In long TTC zones, Supplementary Distance plaques with the legend NEXT XX MILES may be placed in combination with warning signs at regular intervals within the zone to indicate the remaining length of highway over which the TTC work activity or condition exists.
- **[M]** 6H.33-03 (p.810): The Supplementary Distance plaque with the legend NEXT XX MILES shall not be used in conjunction with any sign other than a warning sign, nor shall it be used alone. When used with orange TTC zone signs, this plaque shall have a black legend and border on an orange background. The plaque shall be at least 30 x 24 inches in size when used with a sign that is 36 x 36 inches or larger.
- **[R]** 6H.33-04 (p.810): When used in TTC zones, the Supplementary Distance plaque with the legend NEXT XX MILES should be placed below the initial warning sign designating that, within the approaching zone, a temporary work activity or condition exists.

*Also governed by Section 7B.02:*

- [S] 7B.02-02 (p.972) ◆ W16-2P, W16-2aP: The School (S1‑1) sign (see Figure 7B‑1) has the following four applications: A. School Area – the S1‑1 sign can be used to warn road users that they are approaching a school area that might include school buildings or grounds, a school crossing, or school related activity adjacent to the highway. B. School Zone – the S1‑1 sign can be used to identify the location of the beginning of a designated school zone. C. School Advance Crossing – if combined with an AHEAD (W16‑9P) plaque or an XX FEET (W16‑2P or W16‑2aP) plaque to comprise the School Advance Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn road users that they are approaching a crossing where schoolchildren cross the roadway (see Section 7B.03). D. School Crossing – if combined with a diagonal downward‑pointing arrow (W16‑7P) plaque to comprise the School Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn approaching road users of the location of a crossing where schoolchildren cross the roadway (see Section 7B.03).

*Also governed by Section 7B.03:*

- **[M]** 7B.03-01 (p.976) ◆ W16-2P, W16-2aP: The School Advance Crossing assembly (see Figure 7B‑1) shall consist of a School (S1‑1) sign supplemented with an AHEAD (W16‑9P) plaque or an XX FEET (W16‑2P or W16‑2aP) plaque.

*Also governed by Section 9C.04:*

- [O] 9C.04-04 (p.1067) ◆ W16-2P, W16-2aP: If used in advance of a trail crossing, a W11-15 or W11-15a sign should be supplemented with an AHEAD (W16-9P) or XX FEET (W16-2P or W16-2aP) plaque to inform road users that they are approaching a point where crossing activity might occur.

<a id="sec-2C-62"></a>
#### Section 2C.62 Supplemental Arrow Plaques (W16-5P and W16-6P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-5P](symbols/W16-5P.png) | **W16-5P** | Supplemental Arrow (plaque) | Recommended (2C.62-01) | 21 x 15 | 21 x 15 | — | — | — | 30 x 21 | 2C-1 p.150 | 7B-1 |
| ![W16-6P](symbols/W16-6P.png) | **W16-6P** | Supplemental Arrow (plaque) | Recommended (2C.62-01) | 21 x 15 | 21 x 15 | — | — | — | 30 x 21 | 2C-1 p.150 | 7B-1 |

- **[R]** 2C.62-01 (p.197): If the condition indicated by a warning sign is located on an intersecting road and the distance between the intersection and condition is not sufficient to provide adequate advance placement of the warning sign, a Supplemental Arrow (W16-5P or W16-6P) plaque (see Figure 2C-16) should be used below the warning sign.
- **[M]** 2C.62-02 (p.197): Supplemental Arrow plaques shall have the same legend design as the Advance Turn Arrow and Directional Arrow auxiliary signs (see Sections 2D.26 and 2D.28) except that they shall have a black legend and border on a yellow or fluorescent yellow-green background, as appropriate.

*Also governed by Section 7B.02:*

- [O] 7B.02-03 (p.972): If a school area or school zone is located on a cross street in close proximity to the intersection, a School (S1‑1) sign with a supplemental arrow (W16‑5P or W16‑6P) plaque (see Figure 7B‑1) may be installed on each approach of the street or highway to warn road users making a turn onto the cross street that they will encounter a school area soon after making the turn.

*Also governed by Section 7B.03:*

- [O] 7B.03-04 (p.976): If a school crosswalk is located on a cross street in close proximity to an intersection, a School Advance Crossing assembly with a supplemental arrow (W16‑5P or W16‑6P) plaque may be installed on each approach of the street or highway to warn road users making a turn onto the cross street that they will encounter a school crosswalk soon after making the turn (see Figure 7B‑3).

<a id="sec-2C-63"></a>
#### Section 2C.63 Diagonal Downward-Pointing Arrow Plaques (W16-7P and W16-7aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-7P](symbols/W16-7P.png) | **W16-7P** | Diagonal Downward | Optional (2C.63-03) · *Auto* | 21 x 15 | 21 x 15 | — | — | — | 30 x 21 | 2C-1 p.150 | 7B-1, 9A-1 |
| ![W16-7aP](symbols/W16-7aP.png) | **W16-7aP** | Dual Downward Diagonal | Optional (2C.63-03) | 21 x 15 | 21 x 15 | — | — | — | 30 x 21 | 2C-1 p.150 | — |

- [S] 2C.63-01 (p.197): Diagonal downward-pointing arrow (W16-7P and W16-7aP) plaques (see Figure 2C-16) are used with certain Vehicular Traffic Warning signs (see Section 2C.54) and certain Non-Vehicular Warning signs (see Section 2C.55), and School Crossing signs (see Section 7B.03) to indicate the specific location of a crossing point.
- [S] 2C.63-02 (p.197) ◆ W16-7P: The W16-7P plaque contains a single arrow pointing diagonally down to the right or left, toward the roadway, depending on which side of the roadway it is located.
- [O] 2C.63-03 (p.197) ◆ W16-7aP: A W16-7aP plaque may be used with a single crossing sign located on a narrow median separating two roadways with traffic in the same direction where the crossing traverses both roadways.

*Also governed by Section 7B.02:*

- [S] 7B.02-02 (p.972) ◆ W16-7P: The School (S1‑1) sign (see Figure 7B‑1) has the following four applications: A. School Area – the S1‑1 sign can be used to warn road users that they are approaching a school area that might include school buildings or grounds, a school crossing, or school related activity adjacent to the highway. B. School Zone – the S1‑1 sign can be used to identify the location of the beginning of a designated school zone. C. School Advance Crossing – if combined with an AHEAD (W16‑9P) plaque or an XX FEET (W16‑2P or W16‑2aP) plaque to comprise the School Advance Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn road users that they are approaching a crossing where schoolchildren cross the roadway (see Section 7B.03). D. School Crossing – if combined with a diagonal downward‑pointing arrow (W16‑7P) plaque to comprise the School Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn approaching road users of the location of a crossing where schoolchildren cross the roadway (see Section 7B.03).

*Also governed by Section 7B.03:*

- **[M]** 7B.03-06 (p.976) ◆ W16-7P: If used, the School Crossing assembly (see Figure 7B‑1) shall be installed at the school crossing (see Figures 7B‑2 and 7B‑3), or as close to it as possible, and shall consist of a School (S1‑1) sign supplemented with a diagonal downward‑pointing arrow (W16‑7P) plaque (see Section 2C.63) to show the location of the crossing.
- **[M]** 7B.03-15 (p.976) ◆ W16-7P: When used at an uncontrolled crossing, the In‑Street or Overhead Pedestrian Crossing sign shall be used only as a supplement to a School Crossing assembly with a diagonal downward‑pointing arrow (W16‑7P) plaque at the crosswalk location.
- [O] 7B.03-16 (p.978) ◆ W16-7P: A 12‑inch reduced size in‑street School (S1‑1) sign (see Figure 7B‑1) may be used instead of the In‑Street Pedestrian Crossing (R1‑6 or R1‑6a) or the In‑Street School Crossing (R1‑6b or R1‑6c) sign at a school crossing on approaches that are not controlled by a traffic control signal, pedestrian hybrid beacon, or an emergency‑vehicle hybrid beacon. A 12 x 6‑inch reduced size diagonal downward‑pointing arrow (W16‑7P) plaque (see Figure 7B‑1) may be mounted below the reduced size in‑street School (S1‑1) sign.

*Also governed by Section 9C.04:*

- **[M]** 9C.04-06 (p.1067) ◆ W16-7P: Bicycle Warning and Trail Crossing signs, when used at the location of the crossing, shall be supplemented with a diagonal downward-pointing arrow (W16-7P) plaque to show the location of the crossing.

<a id="sec-2C-64"></a>
#### Section 2C.64 Hill-Related Plaques (W7-2 Series and W7-3 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W7-2P](symbols/W7-2P.png) | **W7-2P** | Use Low Gear (plaque) | Recommended (2C.64-01) | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.149 | — |
| ![W7-2bP](symbols/W7-2bP.png) | **W7-2bP** | Trucks Use Lower Gear (plaque) | Recommended (2C.64-01) | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.149 | — |
| ![W7-3P](symbols/W7-3P.png) | **W7-3P** | XX% Grade (plaque) | Recommended (2C.64-01) · *Auto* | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.149 | — |
| ![W7-3bP](symbols/W7-3bP.png) | **W7-3bP** | XX% Grade, XX Miles (plaque) | Recommended (2C.64-01) | 24 x 18 | 24 x 18 | — | — | — | — | 2C-1 p.149 | — |

- **[R]** 2C.64-01 (p.197): Hill-Related (W7-2 series and W7-3 series) plaques (see Figure 2C-5) or other appropriate legends and larger signs should be used for emphasis or where special hill characteristics exist.
- **[R]** 2C.64-02 (p.197) ◆ W7-3bP: On longer grades, the use of a distance (W7-3aP or W7-3bP) plaque (see Figure 2C-5) at periodic intervals of approximately 1-mile spacing should be considered.

<a id="sec-2C-65"></a>
#### Section 2C.65 Advance Street Name Plaques (W16-8P and W16-8aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-8P](symbols/W16-8P.png) | **W16-8P** | Advance Street Name | Optional (2C.65-01) | Varies x 8 | Varies x 8 | — | — | — | — | 2C-1 p.150 | — |
| ![W16-8aP](symbols/W16-8aP.png) | **W16-8aP** | Advance Street Name | Optional (2C.65-01) | Varies x 15 | Varies x 15 | — | — | — | — | 2C-1 p.150 | — |

- [O] 2C.65-01 (p.197): An Advance Street Name (W16-8P or W16-8aP) plaque (see Figure 2C-16) may be used with any Intersection (W1-10 series, W2 series, W10-2, W10-3, or W10-4) or Advance Traffic Control (W3 series) sign to identify the name of the intersecting street.
- **[M]** 2C.65-02 (p.197): The lettering on Advance Street Name plaques shall be composed of a combination of lower-case letters with initial upper-case letters.
- **[M]** 2C.65-03 (p.197): If two street names are used on the Advance Street Name plaque, a directional arrow pointing in the direction of the street shall be placed next to each street name. Arrows pointing to the left shall be placed to the left of the street name, and arrows pointing to the right shall be placed to the right of the street name.
- **[R]** 2C.65-04 (p.198): If two street names are used on the Advance Street Name plaque, the street names and associated arrows should be displayed in the following order: A. For a single intersection, the name of the street to the left should be displayed above the name of the street to the right; or B. For two sequential intersections, such as where the plaque is used with an Offset Side Roads (W2-7) or a Double Side Road (W2-8) sign, the name of the first street encountered should be displayed above the name of the second street encountered, and the arrow associated with the second street encountered should be an advance arrow, such as the arrow shown on the W16-6P arrow plaque (see Figure 2C-16).

<a id="sec-2C-66"></a>
#### Section 2C.66 Traffc Does Not Stop Plaques (W4i -4P Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W4-4P](symbols/W4-4P.png) | **W4-4P** | Cross Traffic Does Not | Optional (2C.66-01) | 24 x 12 | 24 x 12 | 36 x 18 | — | — | 48 x 24 | 2C-1 p.148 | — |
| ![W4-4aP](symbols/W4-4aP.png) | **W4-4aP** | Does Not Stop | Optional (2C.66-02) | 24 x 12 | 24 x 12 | 36 x 18 | — | — | 48 x 24 | 2C-1 p.148 | — |
| ![W4-4bP](symbols/W4-4bP.png) | **W4-4bP** | Oncoming Traffic Does Not Stop | Optional (2C.66-02) | 24 x 12 | 24 x 12 | 36 x 18 | — | — | 48 x 24 | 2C-1 p.148 | — |

- [O] 2C.66-01 (p.198) ◆ W4-4P: The CROSS TRAFFIC DOES NOT STOP (W4-4P) plaque (see Figure 2C-10) may be used in combination with a STOP sign when engineering judgment indicates that conditions are present that are causing or could cause road users to misinterpret the intersection as an all-way stop.
- [O] 2C.66-02 (p.198) ◆ W4-4aP, W4-4bP: The TRAFFIC FROM LEFT (RIGHT) DOES NOT STOP (W4-4aP) or ONCOMING TRAFFIC DOES NOT STOP (W4-4bP) plaque may be used when such messages more accurately describe the traffic controls established at the intersection.
- **[R]** 2C.66-03 (p.198) ◆ W4-4aP, W4-4bP: The W4-4aP and W4-4bP plaques should be used at intersections where STOP signs control all but one approach to the intersection, unless the only non-stopped approach is from a one-way street.
- **[M]** 2C.66-04 (p.198): If a W4-4P series plaque is used, it shall be mounted below the STOP sign.

<a id="sec-2C-67"></a>
#### Section 2C.67 IN ROAD and IN STREET Plaques (W16-1P and W16-1aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-1P](symbols/W16-1P.png) | **W16-1P** | In Road (plaque) | Optional (2C.67-01) | 18 x 12 | 18 x 12 | 24 x 18 | — | — | 24 x 18 | 2C-1 p.150 | 9A-1 |
| ![W16-1aP](symbols/W16-1aP.png) | **W16-1aP** | In Street (plaque) | Optional (2C.67-01) | 18 x 12 | 18 x 12 | 24 x 18 | — | — | 24 x 18 | 2C-1 p.150 | 9A-1 |

- [O] 2C.67-01 (p.198): In situations where there is a need to warn drivers to watch for other slower forms of transportation traveling along the highway, such as bicycles, pedestrians, golf carts, horse-drawn vehicles, or farm machinery, an IN ROAD (W16-1P) plaque or IN STREET (W16-1aP) plaque (see Figure 2C-16) may be used.
- **[M]** 2C.67-02 (p.198): The background color of the W16-1P or W16-1aP plaque shall match the background color of the warning sign with which it is displayed. If a W16-1P or W16-1aP plaque is used, it shall be mounted below either a Vehicular Traffic Warning sign (see Section 2C.54) or a Non-Vehicular Warning sign (see Section 2C.55), and shall not be mounted alone.

*Also governed by Section 9C.08:*

- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).

<a id="sec-2C-68"></a>
#### Section 2C.68 EXCEPT BICYCLES Plaque (W16-20P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-20P](symbols/W16-20P.png) | **W16-20P** | Except Bicycles (plaque) | Optional (9C.05-01) | 24 x 12 | 24 x 12 | — | — | — | — | 2C-1 p.151 | 9A-1 |

- [O] 2C.68-01 (p.198): Where it is desired to notify bicyclists that the conditions depicted by a warning sign are not applicable to bicycles, the EXCEPT BICYCLES (W16-20P) supplemental warning plaque (see Figure 2C-16) may be mounted below the warning sign.
- [S] 2C.68-02 (p.198): Examples of warning signs with which an EXCEPT BICYCLES (W16-20P) plaque can be mounted include DEAD END (W14-1) or NO OUTLET (W14-2) signs.

*Also governed by Section 9C.05:*

- [O] 9C.05-01 (p.1067): Where it might be advantageous to notify bicyclists that the conditions or hazards depicted by a warning sign are not applicable to bicycles, the EXCEPT BICYCLES (W16-20P) warning plaque (see Figure 9C-1) may be used.

<a id="sec-2C-69"></a>
#### Section 2C.69 Photo Enforced Plaques (W16-10P and W16-10aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-10P](symbols/W16-10P.png) | **W16-10P** | Photo Enforced (symbol plaque) | Optional | 24 x 12 | 24 x 12 | 36 x 18 | — | — | 48 x 24 | 2C-1 p.150 | — |
| ![W16-10aP](symbols/W16-10aP.png) | **W16-10aP** | Photo Enforced (plaque) | Optional | 24 x 18 | 24 x 18 | 36 x 30 | — | — | 48 x 36 | 2C-1 p.150 | — |

- [O] 2C.69-01 (p.198): A Photo Enforced (W16-10P) plaque or a PHOTO ENFORCED (W16-10aP) word message plaque (see Figure 2C-16) may be mounted below a warning sign to advise road users that the regulations associated with the condition being warned about (such as a traffic control signal or a toll plaza) are being enforced by photographic equipment.

<a id="sec-2C-70"></a>
#### Section 2C.70 Object Marker Design and Placement Height

| Sign | Code | Name | Default class | Size table | Also sized in |
|---|---|---|---|---|---|
| ![OM1-1](symbols/OM1-1.png) | **OM1-1** | Object Marker Design and Placement Height | Optional | text | — |
| ![OM1-2](symbols/OM1-2.png) | **OM1-2** | Object Marker Design and Placement Height | Optional | text | — |
| ![OM1-3](symbols/OM1-3.png) | **OM1-3** | Object Marker Design and Placement Height | Optional | text | — |
| ![OM4-1](symbols/OM4-1.png) | **OM4-1** | Object Marker Design and Placement Height | Optional | text | — |
| ![OM4-2](symbols/OM4-2.png) | **OM4-2** | Object Marker Design and Placement Height | Optional | text | — |
| ![OM4-3](symbols/OM4-3.png) | **OM4-3** | Object Marker Design and Placement Height | Optional | text | — |

- **[M]** 2C.70-02 (p.199): When used, object markers (see Figure 2C-17) shall not have a border and shall consist of an arrangement of one or more of the following types: Type 1—a diamond-shaped sign, at least 18 inches on a side, consisting of either a yellow (OM1-1) or black (OM1-2) sign with nine yellow retroreflective devices, each with a minimum diameter of 3 inches, mounted symmetrically on the sign, or an all-yellow retroreflective sign (OM1-3). Type 2—either a marker (OM2-1V or OM21H) consisting of three yellow retroreflective devices, each with a minimum diameter of 3 inches, arranged either horizontally or vertically on a white sign measuring at least 6 x 12 inches; or an all-yellow horizontal or vertical retroreflective sign (OM2-2V or OM2-2H), measuring at least 6 x 12 inches. Type 3—a striped marker, 12 x 36 inches, consisting of a vertical rectangle with alternating black and retroreflective yellow stripes sloping downward at an angle of 45 degrees toward the side of the obstruction on which traffic is to pass. The minimum width of the yellow and black stripes shall be 3 inches. Type 4—a diamond-shaped sign, at least 18 inches on a side, consisting of either a red (OM4-1) or black (OM4-2) sign with nine red retroreflective devices, each with a minimum diameter of 3 inches, mounted symmetrically on the sign, or an all-red retroreflective sign (OM4-3).

### Chapter 2D Guide Signs, Conventional Roads

<a id="sec-2D-11"></a>
#### Section 2D.11 Design of Route Signs

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M1-1](symbols/M1-1.png) | **M1-1** | Interstate Route (1 or 2 digits) | Mandatory (2D.11-02) | 30 x 24 | — | 45 x 36 | 2D-1 p.207 | 2E-1 |
| ![M1-1a](symbols/M1-1a.png) | **M1-1a** | Interstate Route (1 or 2 digits) | Mandatory (2D.11-02) | 30 x 24 | — | 45 x 36 | 2D-1 p.207 | — |
| ![M1-2](symbols/M1-2.png) | **M1-2** | Loop | Optional | 30 x 24 | — | 45 x 36 | 2D-1 p.207 | 2E-1 |
| ![M1-3](symbols/M1-3.png) | **M1-3** | Spur | Optional | 30 x 24 | — | 45 x 36 | 2D-1 p.207 | 2E-1 |
| ![M1-4](symbols/M1-4.png) | **M1-4** | U.S. Route (1 or 2 digits) | Recommended (2D.11-13) | 30 x 24 | — | 45 x 36 | 2D-1 p.207 | 2E-1 |
| ![M1-5](symbols/M1-5.png) | **M1-5** | State Route (1 or 2 digits) | Recommended (2D.11-13) | 30 x 24 | — | 45 x 36 | 2D-1 p.207 | 2E-1 |
| ![M1-6](symbols/M1-6.png) | **M1-6** | County Route | Optional | 24 x 24 | — | 36 x 36 | 2D-1 p.207 | 2E-1 |
| ![M1-7](symbols/M1-7.png) | **M1-7** | Forest Route | Optional | 24 x 24 | 18 x 18 | 36 x 36 | 2D-1 p.207 | 2E-1 |

- **[M]** 2D.11-02 (p.216) ◆ M1-1, M1-1a: Interstate Route (M1-1 and M1-1a) signs (see Figure 2D-4) shall be used on all Interstate routes and in connection with Route Sign assemblies on intersecting highways. DecemberMonth 2023
- [O] 2D.11-04 (p.217) ◆ M1-1, M1-1a: When the Interstate Route sign is used in a Route Sign assembly (see Section 2D.29), the M1-1a sign, containing the State name in white upper-case letters on a blue background as detailed in the “Standard Highway Signs” publication (see Section 1A.05), may be used in place of the M1-1 sign.
- **[M]** 2D.11-05 (p.217) ◆ M1-1a: Use of the M1-1a sign shall be limited to Route Sign assemblies.
- **[M]** 2D.11-06 (p.217) ◆ M1-2, M1-3: Off-Interstate Business Route (M1-2 and M1-3) signs (see Figure 2D-4) shall consist of a cutout shield displaying the number of the connecting Interstate route and the words BUSINESS and either LOOP (when the route rejoins the same Interstate route) or SPUR (when the route leaves the corresponding Interstate route and does not rejoin) in upper-case letters. The legend and border shall be white on a green background, and the shield shall be the same shape and dimensions as the Interstate Route sign. In no instance shall the word INTERSTATE appear on the Off-Interstate Business Route sign.
- **[R]** 2D.11-13 (p.218) ◆ M1-4, M1-5: Where U.S. or State Route signs are used as components of guide signs, only the distinctive shape of the shield itself and the route numerals within should be used. The rectangular background upon which the distinctive shape of the shield is mounted, such as the black area around the outside of the shields on the M1-4 and standard M1-5 signs, should not be included on the guide sign. Where U.S. or State Route signs are used as components of other signs of non-contrasting background colors, the rectangular background should be used so that recognition of the distinctive shape of the shield can be maintained.
- **[M]** 2D.11-14 (p.218) ◆ M1-6: If county road authorities elect to establish and identify a special system of important county roads, a statewide policy for such signing shall be established that includes a uniform numbering system to uniquely identify each route. The County Route (M1-6) sign (see Figure 2D-4) shall consist of a pentagon shape with a yellow county name and route number and border on a blue background. County Route signs shall be a minimum size of 24 x 24 inches.
- **[M]** 2D.11-17 (p.218) ◆ M1-7: The design of the National Forest Route (M1-7) sign (see Figure 2D-4) shall be as detailed in the “Standard Highway Signs” publication (see Section 1A.05). Route signs for other park and forest roads shall be designed with an appropriate level of distinctiveness and adequate legibility, but in general compliance with the design principles for route signs and of a size compatible with other route signs used in common assemblies.

*Also governed by Section 2E.55:*

- **[R]** 2E.55-01 (p.370): Route signs (see Figure 2E-60) should be incorporated as cut-out shields or other distinctive shapes on large directional guide signs. Where the Interstate shield is displayed in an assembly or on the face of a guide sign with U.S. or State Route signs, the Interstate numeral should be at least equal in size to the numerals on the other Route signs. The use of independent Route signs should be limited primarily to route confirmation assemblies. DecemberMonth 2023 Month 2023December 2023 Sect. 2E.55
- **[R]** 2E.55-02 (p.373): Route signs and auxiliary plaques showing junctions and turns should be used for guidance on approach roads, for route confirmation just beyond entrances and exits, and for reassurance along the freeway or expressway. When used along the freeway or expressway, the Route signs should be enlarged to a 36 x 36inch minimum size for route numbers with one or two digits and to a 45 x 36-inch minimum size for route numbers with three digits as shown in the “Standard Highway Signs” publication (see Section 1A.05). When independently-mounted Route signs are used in place of Pull-Through signs (see Section 2E.27), they should be located just beyond the exit.
- [O] 2E.55-03 (p.373): The standard Trailblazer Assembly (see Section 2D.34) may be used on roads leading to the freeway or expressway. Component messages of the Trailblazer Assembly may be incorporated into a single sign in accordance with the provisions of Section 2D.12. Independently-mounted Route signs may be used instead of Pull-Through signs as confirmation information.
- [O] 2E.55-05 (p.373): The commonly-used name or trailblazer route sign for a toll highway (see Chapter 2F) may be displayed on non-toll sections of the Interstate Highway System at: A. The last exit before entering a toll section of the Interstate Highway System; B. The interchange or connection with a toll highway, whether or not the toll highway is a part of the Interstate Highway System; and C. Other locations within a reasonable approach distance of toll highways when the name or trailblazer symbol for the toll highway would provide better guidance to road users unfamiliar with the area than would place names and route numbers.
- [O] 2E.55-06 (p.373): The toll highway name or route sign may be included as a part of the guide sign installations on intersecting highways and approach roads to indicate the interchange with a toll section of an Interstate route. Where needed for the proper direction of traffic, a trailblazer for a toll highway that is part of the Interstate Highway System may be displayed with the Interstate Trailblazer Assembly.

<a id="sec-2D-13"></a>
#### Section 2D.13 Junction Auxiliary Plaque (M2-1P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M2-1P](symbols/M2-1P.png) | **M2-1P** | Junction (plaque) | Mandatory (9D.08-10) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |

- **[M]** 2D.13-01 (p.219): The Junction (M2-1P) auxiliary plaque (see Figure 2D-5) shall display the abbreviated legend JCT and shall be mounted at the top of an assembly (see Section 2D.30) directly above the route sign, the sign for an alternative route (see Section 2D.17) that is part of the route designation, or the Cardinal Direction auxiliary plaque where access is available only to one direction of the intersected route. The minimum size of the Junction auxiliary plaque shall be 21 x 15 inches for compatibility with auxiliary plaques displaying arrow symbols.

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-14"></a>
#### Section 2D.14 Combination Junction Sign (M2-2)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M2-2](symbols/M2-2.png) | **M2-2** | Combination Junction (2 route signs) | Optional (2D.14-01) | 60 x 48* | — | — | 2D-1 p.207 | 2E-1 |

- [O] 2D.14-01 (p.219): As an alternative to the standard Junction assembly where more than one route is to be intersected or joined, a rectangular guide sign may be used displaying the word JUNCTION above the route numbers.
- **[M]** 2D.14-02 (p.219): The Combination Junction (M2-2) sign (see Figure 2D-5) shall have a green background with white border and lettering for the word JUNCTION.
- **[R]** 2D.14-03 (p.219): The Combination Junction sign should comply with the specific provisions of Section 2D.11 regarding the incorporation of the route signs as components of guide signs.
- **[R]** 2D.14-04 (p.219): Although the size of the Combination Junction sign will depend on the number of routes involved, the numerals should be large enough for clear legibility and should be of a size comparable with those in the individual route signs.

<a id="sec-2D-15"></a>
#### Section 2D.15 Cardinal Direction Auxiliary Plaques (M3-1P through M3-4P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M3-1P](symbols/M3-1P.png) | **M3-1P** | Cardinal Direction (plaque) | Recommended (2D.15-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M3-2P](symbols/M3-2P.png) | **M3-2P** | Cardinal Direction (plaque) | Recommended (2D.15-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M3-3P](symbols/M3-3P.png) | **M3-3P** | Cardinal Direction (plaque) | Recommended (2D.15-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M3-4P](symbols/M3-4P.png) | **M3-4P** | Cardinal Direction (plaque) | Recommended (2D.15-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

- **[R]** 2D.15-01 (p.219): Cardinal Direction auxiliary plaques (see Figure 2D-5) displaying the legend NORTH, EAST, SOUTH, or WEST should be used to indicate the general direction of the entire route.
- **[M]** 2D.15-02 (p.219): To improve the readability and recognition of the cardinal directions, the first letter of the cardinal direction words shall be ten percent larger, rounded up to the nearest whole number size.
- **[M]** 2D.15-03 (p.219): If used, the Cardinal Direction auxiliary plaque shall be mounted directly above a route sign or, if used, an auxiliary plaque for an alternative route.

*Also governed by Section 2N.08:*

- **[M]** 2N.08-01 (p.534): In the event of emergency, State and local authorities shall establish various centers for civilian relief, communication, medical service, and similar purposes. To guide the public to such centers a series of directional signs shall be used.
- **[M]** 2N.08-02 (p.534) ◆ M3-1P: Emergency Aid Center (EM3-1 series) signs (see Figure 2N-1) shall display the designation of the center and an arrow indicating the direction to the center. They shall be installed as needed, at intersections and elsewhere, on the right-hand side of the roadway, in urban areas at a minimum height, measured vertically from the bottom of the sign to the top of the curb, or in the absence of curb, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way, of 7 feet, and not less than 1 foot back from the face of the curb, and in rural areas at a minimum height, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way, of 5 feet, and at a horizontal distance of not less than 6 feet or more than 10 feet from the roadway edge.
- **[M]** 2N.08-03 (p.534): Emergency Aid Center signs shall display one of the following legends, as appropriate, or others designating similar emergency facilities: A. MEDICAL CENTER (EM3-1), B. WELFARE CENTER (EM3-1a), C. REGISTRATION CENTER (EM3-1b), or D. DECONTAMINATION CENTER (EM3-1c).
- **[M]** 2N.08-04 (p.534): The Emergency Aid Center sign shall be a horizontally-oriented rectangle. Except as provided in Paragraph 5 of this Section, the Emergency Aid Center signs shall have a black legend and border on a white background.
- [O] 2N.08-05 (p.534): When Emergency Aid Center signs are used in an incident situation, such as during the aftermath of a nuclear or biological attack, the background color may be fluorescent pink (see Chapter 6O).

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-17"></a>
#### Section 2D.17 ALTERNATE Auxiliary Plaques (M4-1P and M4-1aP)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-1P](symbols/M4-1P.png) | **M4-1P** | Alternate (plaque) | Optional (2D.17-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M4-1aP](symbols/M4-1aP.png) | **M4-1aP** | Alternate (plaque) | Optional (2D.17-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

*Also governed by Section 2D.16:*

- [O] 2D.16-01 (p.220): Alternative Route auxiliary plaques (see Figure 2D-5) displaying legends such as ALTERNATE, BY-PASS, BUSINESS, or TRUCK, may be used to indicate an alternate route of the same number between two points on that route.
- **[M]** 2D.16-02 (p.220): If used, the Alternative Route auxiliary plaques shall be mounted directly above a route sign.

- [O] 2D.17-01 (p.220): The ALTERNATE (M4-1P) or the ALT (M4-1aP) auxiliary plaque (see Figure 2D-5) may be used to indicate an officially designated alternate routing of a numbered route between two points on that route.
- **[M]** 2D.17-02 (p.220): If used, the ALTERNATE or ALT auxiliary plaque shall be mounted directly above a route sign.
- **[M]** 2D.17-03 (p.220): The M4-1P series plaques shall not be used to sign an alternative routing that is not officially designated and incorporated into the numbered highway system, such as alternative routings for incident management or emergency detours.
- **[R]** 2D.17-04 (p.220): The shorter (time or distance) or better-constructed route should retain the regular route number, and the longer or worse-constructed route should be designated as the alternate route.

*Also governed by Section 2D.59:*

- [O] 2D.59-02 (p.279): EMERGENCY ROUTE (M4-11 and M4-11a) signs and EMERGENCY ROUTE TO (M4-11bP and M4-11cP) plaques mounted on a directional assembly may be permanently installed on conventional roadways to provide trailblazing along a designated diversionary route to bypass a traffic incident.
- **[M]** 2D.59-04 (p.279): Emergency Routing signs and plaques shall only be installed at departure points and along diversion routes for directing road users around highway segments in areas that are more susceptible to traffic incidents (see Figure 2D-38). EMERGENCY ROUTE and EMERGENCY ROUTE TO signs shall be placed at each turning decision point along the designated route until it rejoins the original route or until other directional signs leading back to the original route are provided.
- **[M]** 2D.59-05 (p.279): Emergency Routing signs shall have a white legend and border on a green background.
- [O] 2D.59-06 (p.279): For additional emphasis the legend EMERGENCY ROUTE or EMERGENCY ROUTE TO may be displayed in a yellow panel with black letters near the top of the sign (see Figure 2D-37).
- **[M]** 2D.59-07 (p.279): Orange or pink shall not be used as alternate colors on permanently-installed signs or plaques for rerouting traffic during an incident or other event. If a route shield is displayed as part of the message, the wording of the sign or plaque shall be EMERGENCY ROUTE TO as shown in Figure 2D-37.
- [O] 2D.59-08 (p.279): An EMERGENCY ROUTE TO plaque with either a white legend and border on a green background (M4-11bP) or black legend and border on a yellow background (M4-11cP) may be added to the top of a conventional Route assembly on a diversion route to provide direction back to the original route downstream of the incident (see Figures 2D-37 and 2D-38).
- [O] 2D.59-09 (p.279): A combination warning and regulatory message sign with flashing beacons mounted above and the legend, WHEN FLASHING [ROUTE] CLOSED AHEAD/ USE EMERGENCY ROUTE [NEXT RIGHT or EXIT XX] may be used in advance of the emergency route entrance to inform road users of the closure and require exiting the primary route and use of the emergency route (see Figures 2D-37 and 2D-38).
- [O] 2D.59-10 (p.279): The End Emergency Route (M4-12) sign may be use at a point along the emergency route just prior to the junction where traffic is to reenter the primary route past the closed section of roadway (see Figure 2D-37 and 2D-38). Month 2023December 2023 DecemberMonth 2023

*Also governed by Section 2N.09:*

- **[M]** 2N.09-01 (p.534): Shelter Directional (EM4-1 series) signs (see Figure 2N-1) shall be used to direct the public to selected shelters that have been licensed and marked for emergency use.
- **[M]** 2N.09-02 (p.534): The installation of Shelter Directional signs shall comply with established signing standards. Where used, the signs shall not be installed in competition with other necessary highway regulatory, guide, and warning signs.
- **[M]** 2N.09-03 (p.534): The Shelter Directional sign shall be a horizontally-oriented rectangle. Except as provided in Paragraph 4 of this Section, the Shelter Directional signs shall have a black legend and border on a white background.
- [O] 2N.09-04 (p.534): When Shelter Directional signs are used in an incident situation, such as during the aftermath of a nuclear or biological attack, the background color may be fluorescent pink (see Chapter 6O).
- [O] 2N.09-05 (p.534): The distance to the shelter may be omitted from the sign when appropriate.
- [O] 2N.09-06 (p.534): Shelter Directional signs may display one of the following legends, or others designating similar emergency facilities: A. EMERGENCY (EM4-1), B. HURRICANE (EM4-1a), C. FALLOUT (EM4-1b), or D. CHEMICAL (EM4-1c).
- [O] 2N.09-07 (p.535): If appropriate, the name of the facility may be used.
- [O] 2N.09-08 (p.535): The Shelter Directional signs may be installed on the Interstate Highway System or any other major highway system when it has been determined that a need exists for such signs as part of a State or local shelter plan.
- [O] 2N.09-09 (p.535): The Shelter Directional signs may be used to identify different routes to a shelter to provide for rapid movement of large numbers of persons.
- **[R]** 2N.09-10 (p.535): The Shelter Directional sign should be used sparingly and only in conjunction with approved plans of State and local authorities.
- **[R]** 2N.09-11 (p.535): The Shelter Directional sign should not be posted more than 5 miles from a shelter. (This page intentionally left blank)

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-18"></a>
#### Section 2D.18 BY-PASS Auxiliary Plaque (M4-2P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-2P](symbols/M4-2P.png) | **M4-2P** | By-Pass (plaque) | Optional (2D.18-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

*Also governed by Section 2D.16:*

- [O] 2D.16-01 (p.220): Alternative Route auxiliary plaques (see Figure 2D-5) displaying legends such as ALTERNATE, BY-PASS, BUSINESS, or TRUCK, may be used to indicate an alternate route of the same number between two points on that route.
- **[M]** 2D.16-02 (p.220): If used, the Alternative Route auxiliary plaques shall be mounted directly above a route sign.

- [O] 2D.18-01 (p.220): The BY-PASS (M4-2P) auxiliary plaque (see Figure 2D-5) may be used to designate a route that branches from the numbered route through a city, bypasses a part of the city or congested area, and rejoins the numbered route beyond the city.
- **[M]** 2D.18-02 (p.220): If used, the BY-PASS auxiliary plaque shall be mounted directly above a route sign.

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-19"></a>
#### Section 2D.19 BUSINESS Auxiliary Plaque (M4-3P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-3P](symbols/M4-3P.png) | **M4-3P** | Business (plaque) | Optional (2D.19-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

*Also governed by Section 2D.16:*

- [O] 2D.16-01 (p.220): Alternative Route auxiliary plaques (see Figure 2D-5) displaying legends such as ALTERNATE, BY-PASS, BUSINESS, or TRUCK, may be used to indicate an alternate route of the same number between two points on that route.
- **[M]** 2D.16-02 (p.220): If used, the Alternative Route auxiliary plaques shall be mounted directly above a route sign.

- [O] 2D.19-01 (p.220): The BUSINESS (M4-3P) auxiliary plaque (see Figure 2D-5) may be used to designate an alternate route that branches from a numbered route, passes through the business portion of a city, and rejoins the numbered route beyond that area.
- **[M]** 2D.19-02 (p.220): If used, the BUSINESS auxiliary plaque shall be mounted directly above a route sign.

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-20"></a>
#### Section 2D.20 TRUCK Auxiliary Plaque (M4-4P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-4P](symbols/M4-4P.png) | **M4-4P** | Truck (plaque) | Optional (2D.20-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1 |

*Also governed by Section 2D.16:*

- [O] 2D.16-01 (p.220): Alternative Route auxiliary plaques (see Figure 2D-5) displaying legends such as ALTERNATE, BY-PASS, BUSINESS, or TRUCK, may be used to indicate an alternate route of the same number between two points on that route.
- **[M]** 2D.16-02 (p.220): If used, the Alternative Route auxiliary plaques shall be mounted directly above a route sign.

- [O] 2D.20-01 (p.220): The TRUCK (M4-4P) auxiliary plaque (see Figure 2D-5) may be used to designate an alternate route that branches from a numbered route, when it is desirable to encourage or require commercial vehicles to use the alternate route.
- **[M]** 2D.20-02 (p.220): If used, the TRUCK auxiliary plaque shall be mounted directly above a route sign.

<a id="sec-2D-21"></a>
#### Section 2D.21 TO Auxiliary Plaque (M4-5P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-5P](symbols/M4-5P.png) | **M4-5P** | To (plaque) | Optional (2D.21-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

- [O] 2D.21-01 (p.220): The TO (M4-5P) auxiliary plaque (see Figure 2D-5) may be used to provide directional guidance to a particular road facility from other highways in the vicinity (see Section 2D.34).
- **[M]** 2D.21-02 (p.220): If used, the TO auxiliary plaque shall be mounted directly above a route sign or an auxiliary plaque for an alternative route. If a Cardinal Direction auxiliary plaque is also included in the assembly, the TO auxiliary plaque shall be mounted directly above the Cardinal Direction auxiliary plaque. DecemberMonth 2023

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-22"></a>
#### Section 2D.22 END Auxiliary Plaque (M4-6P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-6P](symbols/M4-6P.png) | **M4-6P** | End (plaque) | Recommended (2D.22-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

- **[R]** 2D.22-01 (p.221): The END (M4-6P) auxiliary plaque (see Figure 2D-5) should be used where the route being traveled ends, usually at a junction with another route.
- **[M]** 2D.22-02 (p.221): If used, the END auxiliary plaque shall be mounted either directly above a route sign or above a sign for an alternative route that is part of the designation of the route being terminated.

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-23"></a>
#### Section 2D.23 BEGIN Auxiliary Plaque (M4-14P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-14P](symbols/M4-14P.png) | **M4-14P** | Begin (plaque) | Optional (2D.23-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

- [O] 2D.23-01 (p.221): The BEGIN (M4-14P) auxiliary plaque (see Figure 2D-5) may be used where a route begins, usually at a junction with another route.
- **[M]** 2D.23-02 (p.221): If used, the BEGIN auxiliary plaque shall be mounted at the top of the first Confirming assembly (see Section 2D.33) for the route that is beginning.
- **[R]** 2D.23-03 (p.221): If a BEGIN auxiliary plaque is included in the first Confirming assembly, a Cardinal Direction auxiliary plaque should also be included in the assembly.
- **[M]** 2D.23-04 (p.221): If a Cardinal Direction auxiliary plaque is also included in the assembly, the BEGIN auxiliary plaque shall be mounted directly above the Cardinal Direction auxiliary plaque.

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-24"></a>
#### Section 2D.24 TEMPORARY Auxiliary Plaques (M4-7P and M4-7aP)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-7P](symbols/M4-7P.png) | **M4-7P** | Temporary (plaque) | Optional (2D.24-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M4-7aP](symbols/M4-7aP.png) | **M4-7aP** | Temporary (plaque) | Optional (2D.24-01) | 24 x 12 | — | 36 x 18 | 2D-1 p.207 | 2E-1, 9A-1 |

- [O] 2D.24-01 (p.221): The TEMPORARY (M4-7P) or the TEMP (M4-7aP) auxiliary plaque (see Figure 2D-5) may be used for an interim period to designate a section of highway that is not planned as a permanent part of a numbered route, but that connects completed portions of that route.
- **[M]** 2D.24-02 (p.221): If used, the TEMPORARY or TEMP auxiliary plaque shall be mounted directly above the route sign, above a Cardinal Direction auxiliary plaque, or above an auxiliary plaque for an alternate route that is a part of the route designation.
- **[M]** 2D.24-03 (p.221): TEMPORARY or TEMP auxiliary plaques shall be promptly removed when the temporary route is abandoned.

*Also governed by Section 9D.08:*

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-26"></a>
#### Section 2D.26 Advance Turn Arrow Auxiliary Plaques (M5-1P, M5-2P, and M5-3P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M5-1P](symbols/M5-1P.png) | **M5-1P** | Advance Turn Arrow Auxiliary Plaques | Mandatory (2D.26-02) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M5-2P](symbols/M5-2P.png) | **M5-2P** | Advance Turn Arrow (plaque) | Mandatory (2D.26-02) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M5-3P](symbols/M5-3P.png) | **M5-3P** | Circular Intersection Advance Turn Arrow | Mandatory (2D.26-02) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1 |

- **[M]** 2D.26-01 (p.221) ◆ M5-1P, M5-2P: If used, the Advance Turn Arrow auxiliary plaque (see Figure 2D-6) shall be mounted directly below the route sign in Advance Route Turn assemblies, and shall display a right or left arrow, the shaft of which is bent at a 90-degree angle (M5-1P) or at an oblique angle (M5-2P).
- **[M]** 2D.26-02 (p.221) ◆ M5-3P: If used, the Circular Intersection Advance Turn Arrow (M5-3P) auxiliary plaque (see Figure 2D-6) shall be used only on the approach to a circular intersection to depict a movement along the circulatory roadway around the central island and to the left, relative to the approach roadway and entry into the intersection.
- **[R]** 2D.26-03 (p.221) ◆ M5-3P: If the M5-3P plaque is used, then this arrow type should also be used consistently on any regulatory laneuse signs (see Chapter 2B), Destination signs (see Section 2D.36), and pavement markings (see Part 3) for a particular destination or movement. Month 2023December 2023

*Also governed by Section 9D.08:*

- **[R]** 9D.08-07 (p.1078) ◆ M5-1P, M5-2P: If used, Advance Turn Arrow (M5 series) and Directional Arrow (M6 series) auxiliary plaques should be mounted below the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078) ◆ M5-1P, M5-2P: If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-2D-27"></a>
#### Section 2D.27 Lane Designation Auxiliary Plaques (M5-4P, M5-5P, and M5-6P)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M5-4P](symbols/M5-4P.png) | **M5-4P** | Lane Designation Auxiliary Plaques | Mandatory (2D.27-02) | 24 x 18 | — | 36 x 24 | 2D-1 p.207 | 2E-1 |
| ![M5-5P](symbols/M5-5P.png) | **M5-5P** | Lane Designation (plaque) | Mandatory (2D.27-02) | 24 x 18 | — | 36 x 24 | 2D-1 p.207 | 2E-1 |
| ![M5-6P](symbols/M5-6P.png) | **M5-6P** | Lane Designation (plaque) | Mandatory (2D.27-02) | 24 x 18 | — | 36 x 24 | 2D-1 p.207 | 2E-1 |

- [O] 2D.27-01 (p.222): A Lane Designation (M5-4P, M5-5P, or M5-6P) auxiliary plaque (see Figure 2D-6) may be mounted directly below the route sign in an Advance Route Turn assembly on multi-lane roadways to allow road users to move into the appropriate lane prior to reaching the intersection or interchange.
- **[M]** 2D.27-02 (p.222): If used, the Lane Designation auxiliary plaques shall be used only where the designated lane is a mandatory movement lane and shall be located adjacent to the full-width portion of the mandatory movement lane. The Lane Designation auxiliary plaques shall not be installed adjacent to a through lane in advance of a lane that is being added or along the taper for a lane that is being added.

<a id="sec-2D-28"></a>
#### Section 2D.28 Directional Arrow Auxiliary Plaques (M6 Series)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M6-1P](symbols/M6-1P.png) | **M6-1P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M6-2P](symbols/M6-2P.png) | **M6-2P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M6-2aP](symbols/M6-2aP.png) | **M6-2aP** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1 |
| ![M6-3P](symbols/M6-3P.png) | **M6-3P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M6-4P](symbols/M6-4P.png) | **M6-4P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M6-5P](symbols/M6-5P.png) | **M6-5P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M6-6P](symbols/M6-6P.png) | **M6-6P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |
| ![M6-7P](symbols/M6-7P.png) | **M6-7P** | Directional Arrow (plaque) | Optional (2D.28-03) | 21 x 15 | — | 30 x 21 | 2D-1 p.207 | 2E-1, 9A-1 |

- **[M]** 2D.28-01 (p.222): If used, the Directional Arrow auxiliary plaque (see Figure 2D-6) shall be mounted below the route sign and any other auxiliary plaques in Directional assemblies (see Section 2D.32), and shall display a single-headed or double-headed arrow pointing in the general direction that the route follows.
- **[M]** 2D.28-02 (p.222): A Directional Arrow auxiliary plaque that displays a double-headed arrow shall not be mounted in any Directional assembly in advance of or at a circular intersection.
- [O] 2D.28-03 (p.222) ◆ M6-2aP: The diagonal downward-pointing arrow auxiliary (M6-2aP) plaque may be used in a Directional assembly at the far corner of an intersection to indicate the immediate entry point to a freeway or expressway entrance ramp (see Section 2D.50).
- **[M]** 2D.28-04 (p.222) ◆ M6-2aP: The M6-2aP plaque shall not be used on the approach to or on the near side of an intersection, such as to designate an approach lane. DecemberMonth 2023

*Also governed by Section 9D.08:*

- **[R]** 9D.08-07 (p.1078) ◆ M6-1P, M6-2P, M6-3P, M6-4P, M6-5P, M6-6P, M6-7P: If used, Advance Turn Arrow (M5 series) and Directional Arrow (M6 series) auxiliary plaques should be mounted below the appropriate Bicycle Route signs.
- **[M]** 9D.08-10 (p.1078) ◆ M6-1P, M6-2P, M6-3P, M6-4P, M6-5P, M6-6P, M6-7P: If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.
- [O] 9D.08-23 (p.1079) ◆ M6-3P: Straight-through movements may be indicated by a Directional assembly with a route sign displaying the number of the continuing route and a M6-3P Directional Arrow – Through auxiliary plaque.

<a id="sec-2D-36"></a>
#### Section 2D.36 Destination Signs (D1 Series)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D1-1](symbols/D1-1.png) | **D1-1** | Destination (1 line) | Optional (2D.36-02) | Varies x 18 | — | — | 2D-1 p.207 | 2E-1, 9A-1 |
|  | **D1-1a** | Destination and Distance (1 line) | Optional (2D.36-02) | Varies x 18 | — | — | 2D-1 p.207 | 2E-1, 9A-1 |
| ![D1-2](symbols/D1-2.png) | **D1-2** | Destination (2 lines) | Optional (2D.36-02) | Varies x 30 | — | — | 2D-1 p.207 | 2E-1, 9A-1 |
| ![D1-2a](symbols/D1-2a.png) | **D1-2a** | Destination and Distance (2 lines) | Optional (2D.36-02) | Varies x 30 | — | — | 2D-1 p.207 | 2E-1, 9A-1 |
| ![D1-3](symbols/D1-3.png) | **D1-3** | Destination (3 lines) | Optional (2D.36-02) | Varies x 42 | — | — | 2D-1 p.208 | 2E-1, 9A-1 |
| ![D1-3a](symbols/D1-3a.png) | **D1-3a** | Destination and Distance (3 lines) | Optional (2D.36-02) | Varies x 42 | — | — | 2D-1 p.208 | 2E-1, 9A-1 |

- **[M]** 2D.36-01 (p.232): Except on approaches to interchanges (see Section 2D.49), the Destination (D1-1 through D1-3) signs (see Figure 2D-9), if used, shall be a horizontal rectangle displaying the name of a city, town, village, or other traffic generator, and a directional arrow.
- [O] 2D.36-02 (p.232): The distance (see Section 2D.43) to the place named may also be displayed on the Destination (D1-1a through D1-3a) signs (see Figure 2D-9). If several destinations are to be displayed at a single point, the several names may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for such a group of destinations.
- **[R]** 2D.36-03 (p.232): Adequate separation should be made between any destinations or group of destinations in one direction and those in other directions by suitable design of the arrow, spacing of lines of legend, heavy lines entirely across the sign, or separate signs.
- **[M]** 2D.36-05 (p.232): Except as otherwise provided in this Manual, an arrow pointing to the right shall be at the extreme right of the sign, and an arrow pointing left or up shall be at the extreme left. The distance numerals, if used, shall be placed to the right of the destination names.
- [O] 2D.36-06 (p.232): An arrow pointing up may be placed at the extreme right of the sign when the sign is mounted to the left of the traffic to which it applies.
- **[R]** 2D.36-07 (p.232): Unless a sloping arrow will convey a clearer indication of the direction to be followed, the directional arrows should be horizontal or vertical.
- **[R]** 2D.36-08 (p.232): If several individual name signs are assembled into a group, all signs in the assembly should be of the same horizontal width.
- **[R]** 2D.36-09 (p.232): Destination signs should be used: A. At the intersections of U.S. or State numbered routes with Interstate, U.S., or State numbered routes; and B. At points where they serve to direct traffic from U.S. or State numbered routes to the business section of towns, or to other destinations reached by unnumbered routes. DecemberMonth 2023
- **[M]** 2D.36-10 (p.233): Where a total of three or fewer destinations are displayed on the Advance guide (see Section 2E.23) and Supplemental guide (see Section 2E.51) signs, no more than three destination names shall be displayed on a Destination sign. Where four destinations are displayed on the Advance guide and Supplemental guide signs, no more than four destination names shall be displayed on a Destination sign.
- **[R]** 2D.36-11 (p.233): If space permits, four destinations should be displayed on two separate signs at two separate locations.
- [O] 2D.36-12 (p.233): Where space does not permit, or where all four destinations are in one direction, a single sign may be used. Where a single sign is used and all destinations are in the same direction, the arrow may be placed below the destinations for the purpose of enhancing the conspicuity of the arrow.
- **[M]** 2D.36-13 (p.233): Where a single four-name sign assembly is used, a heavy line approximating the width of the sign border entirely across the sign or separate signs shall be used to separate destinations by direction. Month 2023December 2023
- **[R]** 2D.36-14 (p.234): The closest destination lying straight ahead should be at the top of the sign or assembly, and below it the closest destinations to the left and to the right, in that order. The destination displayed for each direction should ordinarily be the next county seat or the next principal city, rather than a more distant destination. In the case of overlapping routes, only one destination should be displayed in each direction for each route.
- **[M]** 2D.36-15 (p.234): If more than one destination is displayed in the same direction, the name of a nearer destination shall be displayed above the name of a destination that is farther away.
- [O] 2D.36-17 (p.234): Overhead Destination signs may be used to provide lane assignment and destination information for some or all of the lanes on the approach to a multi-lane intersection. Destination information may include cardinal directions, route numbers, street names, and/or place names.
- [O] 2D.36-18 (p.234): Overhead signs using the Arrow-per-Lane sign design configuration (see Figure 2D-10) may be used to provide lane assignments for some or all lane destinations at the approach to a multi-lane intersection (see Section 2D.37).

*Also governed by Section 2D.42:*

- **[R]** 2D.42-01 (p.239): When used in high-speed areas, Destination signs should be located 200 feet or more in advance of the intersection, and following any Junction or Advance Route Turn assemblies that might be required. In rural areas, the minimum distance between a Destination sign and either an Advance Route Turn assembly or a Junction assembly should be 200 feet.
- [O] 2D.42-02 (p.239): In urban areas, advance distances shorter than those specified in Paragraph 1 of this Section may be used.
- [O] 2D.42-03 (p.239): Because the Destination sign is of lesser importance than the Junction, Advance Route Turn, or Directional assemblies, the Destination sign may be eliminated where the distance in which to provide adequate sign spacing is limited.

*Also governed by Section 9D.01:*

- **[M]** 9D.01-04 (p.1069): Because of their smaller size, Bicycle Destination and Distance signs shall not be used as a substitute for vehicular destination signs when the message is also intended to be applicable to motorists.
- [O] 9D.01-05 (p.1069): Bicycle Destination and Distance (D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, D1-3c, D2-1a, D2-2a, and D2-3a) signs may be installed to provide direction, destination, and distance information as needed for bicycle travel. If several destinations are to be shown at a single location, they may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for the destinations.
- [O] 9D.01-06 (p.1069) ◆ D1-1, D1-1a: Destination (D1-1 and D1-1a) signs (see Section 2D.36) and Street Name (D3-1) signs (see Section 2D.45) may be installed instead of or in addition to Bicycle Destination signs as needed if the Destination or Street Name sign applies to motorists and bicyclists.
- [O] 9D.01-07 (p.1069): Distance (D2-1 through D2-3) signs (see Section 2D.43) may be installed instead of, or in addition to, Bicycle Distance (D2-1a through D2-3a) signs, as needed, if the destination and distance information applies to motorists and bicyclists.
- **[R]** 9D.01-08 (p.1069): Adequate separation should be made between any destination or group of destinations in one direction and those in other directions by suitable design of the arrow, spacing of lines of legend, heavy lines entirely across the sign, or separate signs.
- **[R]** 9D.01-09 (p.1069): Where a Bicycle Destination sign with distance information is located less than ½ mile from the destination, the distance displayed should be to the nearest ¼ mile. Where the distance to be displayed on a Bicycle Destination sign is less than ¼ mile, the distance should be displayed in feet, rather than miles, to the nearest 50 feet.
- [O] 9D.01-10 (p.1069): Distances may be displayed in fractions of a mile to the nearest ¹⁄10 mile to communicate distance information on Bicycle Destination signs where the distance to a destination is desired to be more precise than ¼-mile increments.
- **[M]** 9D.01-12 (p.1069): An arrow pointing to the right, if used, shall be at the extreme right-hand side of the sign. An arrow pointing left or up, if used, shall be at the extreme left-hand side of the sign. The distance numerals, if used, shall be placed to the right of the destination names.
- **[M]** 9D.01-13 (p.1069): Except as provided in Paragraph 14 of this Section, a bicycle symbol shall be placed next to each destination or group of destinations. Figure 9D-1. Guide Signs and Plaques for Bicycle Facilities (Sheet 1 of 3)
- [O] 9D.01-14 (p.1070): An oversized bicycle symbol may be displayed as the top line of a Bicycle Destination sign instead of individual bicycle symbols for each of the destination/distance lines.
- **[M]** 9D.01-15 (p.1070): If an arrow is at the extreme left, the bicycle symbol shall be placed to the right of the respective arrow.

<a id="sec-2D-38"></a>
#### Section 2D.38 Combination Lane-Use/Destination Overhead Guide Sign (D15-1)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D15-1](symbols/D15-1.png) | **D15-1** | Combination Lane Use / Destination | Optional (2D.38-01) | Varies x 96 | — | — | 2D-1 p.208 | 2E-1 |

- [O] 2D.38-01 (p.237): At intersection approaches involving multiple turn lanes and destinations, a Combination Lane-Use/ Destination (D15-1) overhead guide sign (see Figure 2D-9) that combines a lane-use regulatory sign with destination information such as a cardinal direction, a route number, a street name, and/or a place name may be used.
- [S] 2D.38-02 (p.237): At such locations, the combined information on the D15-1 signs can be even more effective than separate lane- use and guide signs for conveying to unfamiliar drivers which lane or lanes to use for a particular destination.
- [S] 2D.38-03 (p.237): Figure 2D-9 shows an example of a D15-1 sign that combines lane-use and street name information and an example of a D15-1 sign that combines lane-use, cardinal direction, and route number information.
- **[M]** 2D.38-04 (p.238): The Combination Lane-Use/Destination (D15-1) overhead guide sign shall be used only where the designated lane is a mandatory movement lane. The D15-1 sign shall not be used for lanes with optional movements.
- **[M]** 2D.38-05 (p.238): The D15-1 sign shall have a green background with a white border. As shown in Figure 2D-9, the lane- use sign (see Chapter 2B) shall be placed near the bottom of the sign and the destination information shall be placed near the top of the sign. The D15-1 sign shall be located over the approximate center of the lane to which it applies.

<a id="sec-2D-39"></a>
#### Section 2D.39 Destination Signs at Circular Intersections

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D1-1d](symbols/D1-1d.png) | **D1-1d** | Circular Intersection Destination (1 line) | Optional (2D.39-02) | Varies x 18 | — | — | 2D-1 p.207 | — |
|  | **D1-1e** | Circular Intersection Departure Guide | Optional (2D.39-02) | Varies x 42* | — | — | 2D-1 p.207 | — |
| ![D1-2d](symbols/D1-2d.png) | **D1-2d** | Circular Intersection Destination (2 lines) | Optional (2D.39-03) | Varies x 30 | — | — | 2D-1 p.207 | — |
| ![D1-3d](symbols/D1-3d.png) | **D1-3d** | Circular Intersection Destination (3 lines) | Optional (2D.39-03) | Varies x 42 | — | — | 2D-1 p.208 | — |
| ![D1-5](symbols/D1-5.png) | **D1-5** | Circular Intersection Diagrammatic Destination | Optional (2D.39-06) | Varies x 72* | — | — | 2D-1 p.208 | — |
| ![D1-5a](symbols/D1-5a.png) | **D1-5a** | Circular Intersection Diagrammatic Destination, | Optional (2D.39-06) | Varies x 78* | — | — | 2D-1 p.208 | — |

*Also governed by Section 2D.36:*

- **[M]** 2D.36-01 (p.232) ◆ D1-1d, D1-1e, D1-2d, D1-3d: Except on approaches to interchanges (see Section 2D.49), the Destination (D1-1 through D1-3) signs (see Figure 2D-9), if used, shall be a horizontal rectangle displaying the name of a city, town, village, or other traffic generator, and a directional arrow.
- [O] 2D.36-02 (p.232) ◆ D1-1d, D1-1e, D1-2d, D1-3d: The distance (see Section 2D.43) to the place named may also be displayed on the Destination (D1-1a through D1-3a) signs (see Figure 2D-9). If several destinations are to be displayed at a single point, the several names may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for such a group of destinations.
- **[R]** 2D.36-03 (p.232): Adequate separation should be made between any destinations or group of destinations in one direction and those in other directions by suitable design of the arrow, spacing of lines of legend, heavy lines entirely across the sign, or separate signs.
- **[M]** 2D.36-05 (p.232): Except as otherwise provided in this Manual, an arrow pointing to the right shall be at the extreme right of the sign, and an arrow pointing left or up shall be at the extreme left. The distance numerals, if used, shall be placed to the right of the destination names.
- [O] 2D.36-06 (p.232): An arrow pointing up may be placed at the extreme right of the sign when the sign is mounted to the left of the traffic to which it applies.
- **[R]** 2D.36-07 (p.232): Unless a sloping arrow will convey a clearer indication of the direction to be followed, the directional arrows should be horizontal or vertical.
- **[R]** 2D.36-08 (p.232): If several individual name signs are assembled into a group, all signs in the assembly should be of the same horizontal width.
- **[R]** 2D.36-09 (p.232): Destination signs should be used: A. At the intersections of U.S. or State numbered routes with Interstate, U.S., or State numbered routes; and B. At points where they serve to direct traffic from U.S. or State numbered routes to the business section of towns, or to other destinations reached by unnumbered routes. DecemberMonth 2023
- **[M]** 2D.36-10 (p.233): Where a total of three or fewer destinations are displayed on the Advance guide (see Section 2E.23) and Supplemental guide (see Section 2E.51) signs, no more than three destination names shall be displayed on a Destination sign. Where four destinations are displayed on the Advance guide and Supplemental guide signs, no more than four destination names shall be displayed on a Destination sign.
- **[R]** 2D.36-11 (p.233): If space permits, four destinations should be displayed on two separate signs at two separate locations.
- [O] 2D.36-12 (p.233): Where space does not permit, or where all four destinations are in one direction, a single sign may be used. Where a single sign is used and all destinations are in the same direction, the arrow may be placed below the destinations for the purpose of enhancing the conspicuity of the arrow.
- **[M]** 2D.36-13 (p.233): Where a single four-name sign assembly is used, a heavy line approximating the width of the sign border entirely across the sign or separate signs shall be used to separate destinations by direction. Month 2023December 2023
- **[R]** 2D.36-14 (p.234): The closest destination lying straight ahead should be at the top of the sign or assembly, and below it the closest destinations to the left and to the right, in that order. The destination displayed for each direction should ordinarily be the next county seat or the next principal city, rather than a more distant destination. In the case of overlapping routes, only one destination should be displayed in each direction for each route.
- **[M]** 2D.36-15 (p.234): If more than one destination is displayed in the same direction, the name of a nearer destination shall be displayed above the name of a destination that is farther away.
- [O] 2D.36-17 (p.234): Overhead Destination signs may be used to provide lane assignment and destination information for some or all of the lanes on the approach to a multi-lane intersection. Destination information may include cardinal directions, route numbers, street names, and/or place names.
- [O] 2D.36-18 (p.234): Overhead signs using the Arrow-per-Lane sign design configuration (see Figure 2D-10) may be used to provide lane assignments for some or all lane destinations at the approach to a multi-lane intersection (see Section 2D.37).

- [O] 2D.39-02 (p.238) ◆ D1-1d, D1-1e: Exit Destination (D1-1d and D1-1e) signs (see Figure 2D-11) with diagonal upward-pointing arrows or Directional assemblies (see Section 2D.32) may be used to designate a particular exit from a circular intersection.
- [O] 2D.39-03 (p.238) ◆ D1-2d, D1-3d: Destination (D1-2d and D1-3d) signs (see Figure 2D-11) with curved-stem arrows may be used on approaches to circular intersections to represent the left-turn movements.
- [O] 2D.39-06 (p.238) ◆ D1-5, D1-5a: A Destination (D1-5 or D1-5a) sign (see Figure 2D-11) with a diagram of the circular intersection may be used on approaches to circular intersections.
- [S] 2D.39-09 (p.238) ◆ D1-5, D1-5a: Circular Intersection Diagrammatic (D1-5 or D1-5a) signs might be preferable where space is available and where the geometry of the circular intersection is non-typical, such as where more than four legs are present or where the legs are not at approximately 90-degree angles to each other. In such cases, minimizing the amount of legend for each destination and designing the sign so that the arrows for each destination clearly align with the roadway geometry will aid road user understanding of the sign and navigation through the area.

<a id="sec-2D-43"></a>
#### Section 2D.43 Distance Signs (D2 Series)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D2-1](symbols/D2-1.png) | **D2-1** | Distance (1 line) | Recommended (2D.43-03) | Varies x 18 | — | — | 2D-1 p.208 | 2E-1, 9A-1 |
| ![D2-2](symbols/D2-2.png) | **D2-2** | Distance (2 lines) | Recommended (2D.43-03) | Varies x 30 | — | — | 2D-1 p.208 | 2E-1, 9A-1 |
| ![D2-3](symbols/D2-3.png) | **D2-3** | Distance (3 lines) | Recommended (2D.43-03) | Varies x 42 | — | — | 2D-1 p.208 | 2E-1, 9A-1 |

- **[M]** 2D.43-01 (p.239): If used, the Distance (D2-1 through D2-3) signs (see Figure 2D-9) shall be a horizontal rectangle of a size appropriate for the required legend, displaying the names of no more than three cities, towns, junctions, or other traffic generators, and the distance (to the nearest mile) to those places.
- **[M]** 2D.43-02 (p.239): The distance numerals shall be placed to the right of the destination names as shown in Figure 2D-9.
- **[R]** 2D.43-03 (p.239): The distance displayed should be selected on a case-by-case basis by the jurisdiction that owns the road or by statewide policy. A well-defined central area or central business district should be used where one exists. In other cases, the layout of the community should be considered in relation to the highway being signed and the decision based on where it appears that most drivers would feel that they are in the center of the community in question.
- **[R]** 2D.43-04 (p.239): The top name on the Distance sign should be that of the next place on the route having a post office or a railroad station, a route number or name of an intersected highway, or any other significant geographical identity. The bottom name on the sign should be that of the next major destination or control city. If three destinations are displayed, the middle line should be used to indicate communities of general interest along the route or important route junctions.
- [O] 2D.43-05 (p.239): The choice of names for the middle line may be varied on successive Distance signs to give road users additional information concerning communities served by the route. Month 2023December 2023
- **[R]** 2D.43-06 (p.243): The control city should remain the same on all successive Distance signs throughout the length of the route until that city is reached.
- [O] 2D.43-07 (p.243): If more than one distant point may properly be designated, such as where the route divides at some distance ahead to serve two destinations of similar importance, and if these two destinations cannot appear on the same sign, the two names may be alternated on successive signs.
- [O] 2D.43-08 (p.243): On a route continuing into another State, destinations in the adjacent State may be displayed.

*Also governed by Section 2D.44:*

- **[R]** 2D.44-01 (p.243): If used, Distance signs should be installed on important routes leaving municipalities and just beyond intersections of numbered routes in rural areas. If used, they should be placed just outside the municipal limits or at the edge of the built-up area if it extends beyond the limits.
- **[R]** 2D.44-02 (p.243): Where overlapping routes separate a short distance from the municipal limits, the Distance sign at the municipal limits should be omitted. The Distance sign should be installed approximately 300 feet beyond the separation of the two routes.
- **[R]** 2D.44-03 (p.243): Where, just outside of an incorporated municipality, two routes are concurrent and continue concurrently to the next incorporated municipality, the top name on the Distance sign should be that of the place where the routes separate; the bottom name should be that of the city to which the greater part of the through traffic is destined.

*Also governed by Section 9D.01:*

- [O] 9D.01-07 (p.1069): Distance (D2-1 through D2-3) signs (see Section 2D.43) may be installed instead of, or in addition to, Bicycle Distance (D2-1a through D2-3a) signs, as needed, if the destination and distance information applies to motorists and bicyclists.

<a id="sec-2D-45"></a>
#### Section 2D.45 Street Name Signs (D3-1 and D3-1a)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D3-1](symbols/D3-1.png) | **D3-1** | Street Name (1 line) | Recommended (2D.45-02) | Varies x 48 | — | — | 2D-1 p.208 | 2E-1, 9A-1 |
| ![D3-1a](symbols/D3-1a.png) | **D3-1a** | Street Name (1 line) | Recommended (2D.45-02) | Varies x 48 | — | — | 2D-1 p.208 | 2E-1 |

- **[R]** 2D.45-02 (p.247): Street Name (D3-1 or D3-1a) signs (see Figure 2D-14) should be installed in urban areas at all street intersections regardless of other route signs that might be present and should be installed in rural areas to identify important roads that are not otherwise signed.
- **[R]** 2D.45-03 (p.247): To minimize wrong-way movements onto freeway or expressway exit ramps, Street Name signs should not be used at the intersection of a freeway or expressway exit ramp with the crossroad to display the name of the freeway or expressway to traffic on the crossroad.
- [O] 2D.45-04 (p.247) ◆ D3-1a: For streets that are part of a U.S., State, or county numbered route, a D3-1a Street Name sign (see Figure 2D-14) that incorporates a route shield may be used to assist road users who might not otherwise be able to associate the name of the street with the route number.
- **[M]** 2D.45-05 (p.247): The lettering for names of streets and highways on Street Name signs shall be composed of a combination of lower-case letters with initial upper-case letters (see Section 2A.08).
- **[R]** 2D.45-06 (p.247): The determination of letter heights to be used on Street Name signs should be based on, but not limited to, the following considerations: A. Use of Advance Street Name signs (see Section 2D.46); B. Number of lanes on the intersection approach; C. Length of turn lanes; D. Distance the Street Name sign is located across the intersection (if a sign is not provided on the near side of the intersection).
- **[R]** 2D.45-07 (p.247): Letter heights on street name signs should be as shown in Table 2D-6.
- [O] 2D.45-08 (p.248): For two-lane local roadways with speed limits of 25 mph or less, the lettering on post-mounted Street Name signs may be composed of initial upper-case letters at least 4 inches in height and lower-case letters at least 3 inches in nominal loop height.
- [O] 2D.45-11 (p.248): Each Street Name sign in a sign assembly may use different letter heights determined by the speed limit of the street that each sign faces.
- [O] 2D.45-12 (p.248): The letter height of the street name descriptor (such as St, Ave, or Rd), the directional legend (such as NW), or any other supplemental legend (such as block or house numbers) on the D3-1 and D3-1a signs may be smaller than that of the street name itself.
- **[R]** 2D.45-13 (p.248): The letter height of the street name descriptor, the directional legend, or any other supplemental legend on the D3-1 and D3-1a signs should be at least two-thirds of the letter height of the street name itself, but not less than 3 inches for the initial upper-case letters and not less than 2.25 inches for the nominal loop height of the lower-case letters.
- **[R]** 2D.45-14 (p.248): Conventional abbreviations (see Section 1D.08) should be used except for the street name itself. Acceptable abbreviations for street name descriptors such as “Ave” for Avenue and “Blvd” for Boulevard should be as provided in Table 2D-3 (see Section 2D.07). The street name descriptors that are provided in Table 2D-4 should not be abbreviated (see Section 2D.07).
- [O] 2D.45-15 (p.248): Block or house numbers may be displayed as a supplemental legend on a Street Name sign to aid emergency responders and road users in locating addresses.
- **[R]** 2D.45-16 (p.248): If block or house numbers are displayed on a Street Name sign where only a single Street Name sign is provided for the crossroad, the block or house numbers for the left and right blocks should be positioned at the left and right sides of the sign, respectively.
- **[R]** 2D.45-17 (p.248): If block or house numbers are displayed on a Street Name sign where two Street Name signs are provided for the crossroad, such as on diagonally opposite corners of an intersection, each Street Name sign should display only the block or house numbers associated with that block of the crossroad.
- [O] 2D.45-18 (p.248) ◆ D3-1: A pictograph (see definition in Section 1C.02) representing the municipality, in accordance with the provisions of Section 2A.04, may be used on a D3-1 sign. For street networks under the primary jurisdiction of another governmental-approved entity, such as within a college or university campus, within a military base, or within a transportation facility (such as an airport or port), a pictograph representing that entity, in accordance with the provisions of Section 2A.04, may be used on a D3-1 sign within the jurisdictional boundaries of that entity. DecemberMonth 2023
- **[M]** 2D.45-19 (p.249) ◆ D3-1a: Pictographs shall not be displayed on D3-1a or Advance Street Name (D3-2) signs (see Section 2D.46).
- **[M]** 2D.45-20 (p.249) ◆ D3-1: If a pictograph is used on a D3-1 sign, the height and width of the pictograph shall not exceed the uppercase letter height of the principal legend of the sign.
- **[R]** 2D.45-21 (p.249): The pictograph should be positioned to the left of the street name.
- **[R]** 2D.45-22 (p.249) ◆ D3-1: Pictographs should not be used on a D3-1 sign that contains directional arrows.
- **[M]** 2D.45-23 (p.249): The Street Name sign shall be retroreflective or illuminated in accordance with the provisions of Section 2A.21.
- [O] 2D.45-24 (p.249): The border may be omitted from a post-mounted Street Name sign.
- **[R]** 2D.45-25 (p.249): The decision to omit the border from a post-mounted Street Name sign should be based on such factors as the visual complexity of the environment and the degree of conspicuity needed to provide for adequate recognition of the sign by the road user.
- [O] 2D.45-26 (p.249): An alternative background color (see Paragraph 28 of this Section) other than the standard guide sign color of green may be used for Street Name (D3-1 or D3-1a) signs where the highway agency determines this is necessary to assist road users in determining jurisdictional authority for roads.
- **[M]** 2D.45-27 (p.249): Alternative background colors shall not be used for Advance Street Name (D3-2) signs (see Section 2D.46).
- **[M]** 2D.45-28 (p.249): The only acceptable alternative background colors for Street Name (D3-1 or D3-1a) signs shall be blue, brown, or white. Regardless of whether green, blue, or brown is used as the background color for Street Name (D3-1 or D3-1a) signs, the legend (and border, if used) shall be white. For Street Name signs that use a white background, the legend (and border, if used) shall be black.
- **[R]** 2D.45-29 (p.249): An alternative background color for Street Name signs, if used, should be applied to the Street Name (D3-1 or D3-1a) signs on all roadways under the jurisdiction of a particular highway agency.
- **[R]** 2D.45-30 (p.249): In business or commercial areas and on principal arterials, Street Name signs should be placed at least on diagonally opposite corners. In residential areas, at least one Street Name sign should be mounted at each intersection. Signs naming both streets should be installed at each intersection. They should be mounted with their faces parallel to the streets they name.
- **[R]** 2D.45-31 (p.249): Where used, Street Name signs should display their legends on both the front and back sides of the sign to facilitate navigation for pedestrians.
- [O] 2D.45-32 (p.249): To optimize visibility, Street Name signs may be mounted overhead. Street Name signs may also be placed above a regulatory or STOP or YIELD sign with no required vertical separation.
- **[R]** 2D.45-33 (p.249): In urban or suburban areas, especially where Advance Street Name signs for signalized and other major intersections are not used, the use of overhead Street Name signs should be strongly considered.
- [O] 2D.45-34 (p.249) ◆ D3-1: At intersection crossroads where the same road has two different street names for each direction of travel, both street names may be displayed on the same Street Name (D3-1) sign along with Type D directional arrows, except where one arrow would point in a direction opposing the flow of traffic on a one-way street or where a turn in the direction of the arrow is not allowed.
- [O] 2D.45-35 (p.249): On lower-speed roadways, historic street name signs within locally identified historic districts that are consistent with the criteria contained in 36 CFR 60.4 for such structures and districts may remain in service without complying with the provisions of Paragraphs 3, 4, 6, 9, 12 through 14, and 18 through 20 of this Section.
- **[R]** 2D.45-36 (p.249): Streets or segments of a street that have been memorialized or dedicated should not use a second Street Name sign to display the memorial or dedication name (see Section 2D.56). When signed, the Memorial or Dedication sign should be located to minimize its conspicuity to and potential for confusion. Month 2023December 2023

*Also governed by Section 9D.01:*

- [O] 9D.01-06 (p.1069) ◆ D3-1: Destination (D1-1 and D1-1a) signs (see Section 2D.36) and Street Name (D3-1) signs (see Section 2D.45) may be installed instead of or in addition to Bicycle Destination signs as needed if the Destination or Street Name sign applies to motorists and bicyclists.

<a id="sec-2D-46"></a>
#### Section 2D.46 Advance Street Name Signs (D3-2 Series)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **D3-2** | Advance Street Name (2 lines) | Optional (2D.46-03) | Varies x 54 | — | — | 2D-1 p.208 | 2E-1 |

- [S] 2D.46-01 (p.250): Advance Street Name (D3-2) signs (see Figure 2D-14) identify a downstream intersection. Although this is often the next intersection, it could also be several intersections away in cases where the next signalized intersection is referenced.
- **[M]** 2D.46-02 (p.250): Advance Street Name (D3-2) signs, if used, shall supplement rather than be used instead of the Street Name (D3-1 or D3-1a) signs at the intersection.
- [O] 2D.46-03 (p.250): Advance Street Name (D3-2) signs may be installed in advance of signalized or unsignalized intersections to provide road users with advance information to identify the name(s) of the next intersecting street to prepare for crossing traffic and to facilitate timely deceleration and/or lane changing in preparation for a turn.
- **[R]** 2D.46-04 (p.250): On arterial highways in rural areas, Advance Street Name signs should be used in advance of all signalized intersections and in advance of all intersections with mandatory turn lanes.
- **[R]** 2D.46-05 (p.250): In urban areas, Advance Street Name signs should be used in advance of all signalized intersections on major arterial streets, except where signalized intersections are so closely spaced that advance placement of the signs is impracticable.
- **[R]** 2D.46-06 (p.250): The heights of the letters on Advance Street Name signs should comply with the provisions of Section 2D.05.
- **[M]** 2D.46-07 (p.250): If used, Advance Street Name signs shall have a white legend and border on a green background. Alternative background colors shall not be used on Advance Street Name signs.
- **[M]** 2D.46-08 (p.250): If used, Advance Street Name signs shall provide the name(s) of the intersecting street(s) on the top line(s) of the legend and the distance to the intersecting streets or messages such as NEXT SIGNAL, NEXT INTERSECTION, NEXT CIRCLE, or directional arrow(s) on the bottom line of the legend.
- **[M]** 2D.46-09 (p.250): Pictographs shall not be displayed on Advance Street Name signs.
- [O] 2D.46-10 (p.250): Directional arrow(s) may be placed to the right or left of the street name or message such as NEXT SIGNAL, as appropriate, rather than on the bottom line of the legend. Curved-stem arrows may be used on Advance Street Name signs on approaches to circular intersections.
- [O] 2D.46-11 (p.250): For intersecting crossroads where the same road has a different street name for each direction of travel, the different street names may be displayed on the same Advance Street Name sign along with directional arrows.
- [O] 2D.46-12 (p.250): In advance of two closely-spaced intersections where it is impracticable to install separate Advance Street Name signs, the Advance Street Name sign may include the street names for both intersections along with appropriate supplemental legends for both street names, such as NEXT INTERSECTION, 2ND INTERSECTION, or NEXT LEFT and NEXT RIGHT, or directional arrows.
- **[R]** 2D.46-13 (p.250): If two street names are used on the Advance Street Name sign, the street names should be displayed in the following order: A. For a single intersection where the same road has a different street name for each direction of travel, the name of the street to the left should be displayed above the name of the street to the right; or B. For two closely-spaced intersections, the name of the first street encountered should be displayed above the name of the second street encountered, and the arrow associated with the second street encountered should be an advance arrow, such as the arrow shown on the W16-6P arrow plaque (see Figure 2C-16).
- [O] 2D.46-14 (p.250): An Advance Street Name (W16-8P or W16-8aP) plaque (see Section 2C.65) with black legend on a yellow background, installed to supplement an Intersection (W2 series) or Advance Traffic Control (W3 series) warning sign may be used instead of an Advance Street Name guide sign. DecemberMonth 2023

<a id="sec-2D-47"></a>
#### Section 2D.47 Parking Area Guide Sign (D4-1)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D4-1](symbols/D4-1.png) | **D4-1** | Parking Area Directional | Optional (2D.47-01) | 30 x 24 | 18 x 15 | — | 2D-1 p.208 | — |

- [O] 2D.47-01 (p.251): The Parking Area (D4-1) guide sign (see Figure 2D-14) may be used to show the direction to a nearby public parking area or parking facility.
- **[M]** 2D.47-02 (p.251): The smaller size of 18 x 15 inches for the Parking Area guide sign shall be limited to minor, lowspeed streets.
- **[R]** 2D.47-03 (p.251): If used, the Parking Area guide sign should be installed on major thoroughfares at the nearest point of access to the parking facility and where it can advise drivers of a place to park. The sign should not be used more than four blocks from the parking area.

<a id="sec-2D-48"></a>
#### Section 2D.48 PARK - RIDE Sign (D4-2)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D4-2](symbols/D4-2.png) | **D4-2** | Park - Ride | Optional (2D.48-01) | 30 x 36 | 24 x 30 | 36 x 48 | 2D-1 p.208 | 2E-1 |

- [O] 2D.48-01 (p.251): A PARK - RIDE (D4-2) sign (see Figure 2D-14) may be used to direct road users to park-and-ride facilities.
- **[M]** 2D.48-02 (p.251): The signs shall display the word message PARK - RIDE and direction information (arrow or word message).
- [O] 2D.48-03 (p.251): PARK - RIDE signs may display the local transit pictograph and/or carpool symbol.
- **[M]** 2D.48-04 (p.251): If used, the local transit pictograph and/or carpool symbol shall be located in the top part of the sign above the message PARK - RIDE. In no case shall the vertical dimension of the local transit pictograph and/or carpool symbol exceed 18 inches.
- **[R]** 2D.48-05 (p.251): If the function of the parking facility is to provide parking for persons using public transportation, the local transit pictograph should be used on the guide sign. If the function of the parking facility is to serve carpool riders, the carpool symbol should be used on the guide sign. If the parking facility serves both functions, both the pictograph and carpool symbol should be used.
- **[M]** 2D.48-06 (p.251): These signs shall have a white legend and border on a rectangular green background. The carpool symbol shall be as shown for the D4-2 sign. The color of the local transit pictograph shall be selected by the local transit authority.
- [O] 2D.48-07 (p.251): To increase the target value and contrast of the local transit pictograph, and to allow the local transit pictograph to retain its distinctive color and shape, the pictograph may be included within a white border or placed on a white background. Month 2023December 2023

<a id="sec-2D-50"></a>
#### Section 2D.50 Freeway Entrance Signs (D13-3 and D13-3a)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **D13-3** | Freeway Entrance | Optional (2D.50-01) | 48 x 30 | — | — | 2D-1 p.208 | 2E-1 |
|  | **D13-3a** | Freeway Entrance (Directional) | Optional (2D.50-01) | 48 x 42 | — | — | 2D-1 p.208 | 2E-1 |

- [O] 2D.50-01 (p.254): FREEWAY ENTRANCE (D13-3) signs or FREEWAY ENTRANCE with diagonal downward-pointing arrow (D13-3a) signs (see Figure 2D-18) may be used on entrance ramps near the crossroad to inform road users of the freeway or expressway entrance, as appropriate.
- [O] 2D.50-02 (p.254): The D13-3 and D13-3a signs may display an alternate legend in place of FREEWAY, such as EXPRESSWAY or PARKWAY, as appropriate, or may display the name of an unnumbered highway.
- [O] 2D.50-03 (p.254) ◆ D13-3a: A Directional assembly (see Section 2D.32) with a diagonal downward-pointing arrow (M6-2aP) auxiliary plaque (see Section 2D.28) may be used at the far left-hand corner of an intersection with a freeway or expressway entrance ramp as an alternative to the D13-3a sign, facing left-turning traffic on the conventional road approach to indicate the immediate point of entry to the freeway or expressway and distinguish the entrance ramp from an adjoining exit ramp terminal at the same intersection with the conventional road (see Figure 2D-18). A similar Directional assembly may be used at the far right-hand corner of an intersection with a freeway or expressway entrance ramp where the entrance ramp and a crossroad or side road follow one another in close succession on the conventional road approach and the point of entry to the freeway or expressway might be difficult for the road user to distinguish from the crossroad or side road on the conventional road approach (see Figure 2D-20).

<a id="sec-2D-51"></a>
#### Section 2D.51 WEIGH STATION Signing (D8 Series)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **D8-1** | Advance Weigh Station Distance | Optional | 78 x 60 | 60 x 48 | 96 x 72 | 2D-1 p.208 | 2E-1 |
|  | **D8-1a** | Weigh Station Ahead | Optional | 66 x 48 | 48 x 36 | — | 2D-1 p.208 | — |
|  | **D8-2** | Weigh Station Advance Direction | Optional | 84 x 72 | 66 x 54 | 108 x 90 | 2D-1 p.208 | 2E-1 |
|  | **D8-3** | Weigh Station Entrance Direction | Optional | 66 x 60 | 48 x 42 | 84 x 78 | 2D-1 p.208 | 2E-1 |

- **[M]** 2D.51-03 (p.261) ◆ D8-1, D8-2, D8-3: The standard sequence of signs for a Weigh Station on a conventional highway shall include three basic signs (see Figure 2D-23): A. Weigh Station Advance (D8-1) sign, B. Weigh Station Advance Direction (D8-2) sign, and C. Weigh Station Entrance Direction (D8-3) sign.
- **[R]** 2D.51-04 (p.261) ◆ D8-3: A Gore sign with the same basic legend as the Weigh Station Entrance Direction (D8-3) sign should also be used to emphasize the entrance to the weigh station.
- [O] 2D.51-05 (p.261): Where State law requires trucks of a certain weight to enter the Weigh Station, a Weigh Station (R13-1) regulatory sign (see Section 2B.65) may be located following the Advance Weigh Station Ahead sign (see Figure 2D-23).
- [O] 2D.51-06 (p.261): Where only commercial vehicle inspections are conducted in the inspection area, the WEIGH STATION legend of the D8 series signs may be replaced with the alternate legend, COMMERCIAL VEHICLE INSPECTION.
- **[R]** 2D.51-07 (p.261) ◆ D8-1, D8-2: The Weigh Station Advance Direction (D8-2) Sign or the Weigh Station Advance (D8-1) sign should display, either on the sign or on a supplemental plaque or sign panel, the changeable legend OPEN or CLOSED.
- **[M]** 2D.51-08 (p.261): When the WEIGH STATION legend of the D8 series signs is replaced with the COMMERCIAL VEHICLE INSPECTION legend, as provided in Paragraph 6 of this Section, the WEIGH STATION legend of the R13-1 sign shall likewise be replaced with the alternate legend.

*Also governed by Section 2E.54:*

- **[M]** 2E.54-03 (p.370) ◆ D8-1, D8-2, D8-3: The standard sequence of signs for a Weigh Station on an expressway or freeway shall include four basic signs (see Figure 2E-59): A. An Advance Weigh Station Distance (D8-1) sign with the distance 1 MILE displayed, B. An Advance Weigh Station Distance (D8-1) sign with the distance ½ MILE displayed, or a Weigh Station Advance Direction (D8-2) sign, C. A Weigh Station Entrance Direction (D8-3) sign, and D. A Weigh Station Gore sign (with the same legend as the Entrance Direction (D8-3) sign).
- [O] 2E.54-04 (p.370) ◆ D8-1: When spacing of 1 mile and ½ mile are not practical for the D8-1 signs, the 1 MILE and ½ MILE distances on the D8-1 signs may be adjusted to match the spacing determined by engineering judgment.
- [O] 2E.54-06 (p.370) ◆ D8-1, D8-2, D8-3: Where only commercial vehicle inspections are conducted in the inspection area and vehicles are not weighed, the WEIGH STATION legend of the D8 series signs may be replaced with the alternate legend, COMMERCIAL VEHICLE INSPECTION AREA.
- **[M]** 2E.54-07 (p.370) ◆ D8-1, D8-2, D8-3: When the WEIGH STATION legend of the D8 series signs is replaced with COMMERCIAL VEHICLE INSPECTION AREA legend as provided for in Paragraph 6 of this Section, the WEIGH STATION legend of the R13-1 sign shall be replaced with the alternate legend INSPECTION AREA.
- **[R]** 2E.54-09 (p.370) ◆ D8-1, D8-2: The required changeable legend display OPEN or CLOSED describe in Paragraph 8 of this Section should be displayed within and at the bottom of the Weigh Station Advance Direction (D8-2) sign or the Advance Weigh Station Distance (D8-1) sign, or on a supplemental plaque or sign panel.

<a id="sec-2D-52"></a>
#### Section 2D.52 Crossover Signs (D13-1 and D13-2)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D13-1](symbols/D13-1.png) | **D13-1** | Crossover | Optional (2D.52-01) | 60 x 30 | — | 78 x 42 | 2D-1 p.208 | 2E-1 |
| ![D13-2](symbols/D13-2.png) | **D13-2** | Crossover | Optional (2D.52-01) | 60 x 30 | — | 78 x 42 | 2D-1 p.208 | 2E-1 |

- [O] 2D.52-01 (p.261): Crossover signs may be installed on divided highways to identify median openings not otherwise identified by warning or other guide signs.
- **[M]** 2D.52-02 (p.261) ◆ D13-1: A Crossover (D13-1) sign (see Figure 2D-24) shall not be used to identify a median opening that is permitted to be used only by official or authorized vehicles.
- **[R]** 2D.52-03 (p.261): If used, the Crossover sign should be installed immediately beyond the median opening, either on the righthand side of the roadway or in the median.
- [O] 2D.52-04 (p.261) ◆ D13-2: The Advance Crossover (D13-2) sign (see Figure 2D-24) may be installed in advance of the Crossover sign to provide advance notice of the crossover.
- **[R]** 2D.52-05 (p.261): The distance displayed on the Advance Crossover sign should be 1 MILE, ½ MILE, or ¼ MILE, unless unusual conditions require some other distance. If used, the sign should be installed either on the right-hand side of the roadway or in the median at approximately the distance displayed on the sign. Month 2023December 2023

<a id="sec-2D-53"></a>
#### Section 2D.53 Truck and Passing Lane Signs (D17-1 through D17-4)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D17-1](symbols/D17-1.png) | **D17-1** | Next Truck Lane | Recommended (2D.53-01) | 42 x 48 | — | 60 x 66 | 2D-1 p.208 | 2E-1 |
| ![D17-2](symbols/D17-2.png) | **D17-2** | Advance Truck Lane | Recommended (2D.53-01) | 42 x 42 | — | 60 x 54 | 2D-1 p.208 | 2E-1 |
| ![D17-3](symbols/D17-3.png) | **D17-3** | Next Passing Lane | Recommended (2D.53-01) | 42 x 48 | — | 60 x 66 | 2D-1 p.208 | 2E-1 |
| ![D17-4](symbols/D17-4.png) | **D17-4** | Advance Passing Lane | Recommended (2D.53-01) | 42 x 42 | — | 60 x 54 | 2D-1 p.208 | 2E-1 |

- **[R]** 2D.53-01 (p.263) ◆ D17-2: If an extra lane has been provided to the right-hand side of the travel lane for use by trucks and other slowmoving traffic, an Advance Truck Lane (D17-2) sign (see Figure 2D-25) should be installed in advance of the lane.
- **[R]** 2D.53-02 (p.263) ◆ D17-1: If a series of truck lanes is provided along a highway, a Next Truck Lane (D17-1) sign (see Figure 2D-25) should be installed after each truck lane segment.
- **[R]** 2D.53-03 (p.263) ◆ D17-4: If an extra lane has been provided to the left-hand side of the travel lane for passing slower moving vehicles in the travel lane, an Advance Passing Lane Advance (D17-4) sign (see Figure 2D-25) should be installed in advance of the lane.
- **[R]** 2D.53-04 (p.263) ◆ D17-3: If a series of passing lanes are provided along a highway, a Next Passing Lane (D17-3) sign (see Figure 2D-25) should be installed after each passing lane segment.

<a id="sec-2D-54"></a>
#### Section 2D.54 Emergency and Slow Vehicle Turn-Out Signs (D17-5 through D17-7)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![D17-5](symbols/D17-5.png) | **D17-5** | Advance Emergency Turn-Out | Recommended (2D.54-01) | 60 x 36 | — | 78 x 54 | 2D-1 p.208 | 2E-1 |
| ![D17-6](symbols/D17-6.png) | **D17-6** | Emergency Turn-Out (Directional) | Recommended (2D.54-01) | 60 x 36 | — | 78 x 60 | 2D-1 p.208 | 2E-1 |
| ![D17-7](symbols/D17-7.png) | **D17-7** | Advance Slow Vehicle Turn-Out | Recommended (2D.54-01) | 72 x 36 | — | 96 x 54 | 2D-1 p.208 | 2E-1 |

- **[R]** 2D.54-01 (p.266) ◆ D17-5, D17-6: If an emergency turn-out area has been provided where a shoulder is not available for emergency stopping or where there is part-time shoulder use by traffic (see Section 2G.23), Emergency Turn-Out signs should be installed. The Advance Emergency Turn-Out Advance (D17-5) sign (see Figure 2D-28) should be installed between ¼ mile and 500 feet in advance of the turn-out area. The Emergency Turn-Out Directional (D17-6) sign (see Figure 2D-28) should be installed near the beginning of the turn-out area.
- **[R]** 2D.54-02 (p.266) ◆ D17-7: If a slow vehicle turn-out area has been provided for slow-moving traffic, an Advance Slow Vehicle Turn-Out (D17-7) sign (see Figure 2D-28) should be installed in advance of the turn-out area.

<a id="sec-2D-57"></a>
#### Section 2D.57 National Scenic Byways Sign and Plaque (M10-1 and M10-1aP)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **M10-1** | National Scenic Byway | Optional (2D.57-02) | 24 x 24 | — | — | 2D-1 p.207 | 2E-1 |
|  | **M10-1aP** | National Scenic Byway (plaque) | Optional (2D.57-02) | 24 x 12 | — | — | 2D-1 p.207 | 2E-1 |

- [O] 2D.57-02 (p.273): State and local highway agencies may install the National Scenic Byways (M10-1) sign or (M10-1aP) plaque (see Figure 2D-33) at entrance points to a route that has been recognized by the U.S. Secretary of Transportation as a National Scenic Byway or an All-American Road. The M10-1 sign may be installed as independent Directional (see Section 2D.32) or Confirming (see Section 2D.33) assemblies at periodic intervals along the designated route and near intersections where the designated route turns or follows a different numbered highway. The M10-1aP plaque may be installed below a route sign in a Confirming assembly. At locations where roadside features have been developed to enhance the traveler’s experience such as rest areas, historic sites, interpretive facilities, or scenic overlooks, the National Scenic Byways sign or plaque may be placed on the associated sign assembly to inform travelers that the site contributes to the byway travel experience.
- **[R]** 2D.57-03 (p.273) ◆ M10-1: Where the byway is identified only by the National Scenic Byways sign, the Directional assembly should consist of the M10-1 sign and an M5 series or M6 series auxiliary plaque when indication of a turn is necessary to remain on the byway route.
- **[R]** 2D.57-04 (p.274): Where the name of the byway is to be displayed on identification signs or plaques along the byway route, the name should be displayed in a Directional or Confirming assembly as follows (see Figure 2D-34): A. On a Byway Identification (M10-2aP) plaque (see Section 2D.58) mounted below the M10-1 sign; or B. On a Byway Identification (M10-2) sign (see Section 2D.58) with the M10-1aP plaque mounted below the sign.
- **[R]** 2D.57-05 (p.274): In either case, the size of the National Scenic Byways (M10-1) sign, (M10-1aP) plaque, Byway Identification (M10-2) sign, and Byway Identification (M10-2aP) plaque should be consistent with that specified for route signs (see Section 2D.10) for the roadway classification.
- **[R]** 2D.57-06 (p.274): Where the name of the byway is to be displayed along the byway route as provided in Paragraph 4 of this Section, the byway Directional or Confirming assemblies should be located separately from any Route Sign assemblies or Destination guide signs.
- **[M]** 2D.57-07 (p.274): When a National Scenic Byways sign is installed on a National Scenic Byway or an All-American Road, the design shown for the M10-1 sign or M10-1aP plaque in Figure 2D-33 shall be used. Use of this design shall be limited to routes that have been designated as a National Scenic Byway or All-American Road by the U.S. Secretary of Transportation.
- **[M]** 2D.57-08 (p.274): If used, the M10-1 sign or M10-1aP plaque shall be placed such that the highway route signs have primary visibility for the road user.
- **[M]** 2D.57-09 (p.274): The M10-1 sign or the M10-1aP plaque shall not be installed as sign panels on a guide sign or as part of a guide sign assembly.

<a id="sec-2D-58"></a>
#### Section 2D.58 State-Designated Scenic Byway, Historic Trail, and Auto Tour Route Signs

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **M10-2** | Byway Identification | Optional (2D.58-05) | 24 x 24 | — | — | 2D-1 p.207 | — |
|  | **M10-2aP** | Byway Identification (plaque) | Optional (2D.58-07) | 24 x 12 | — | — | 2D-1 p.207 | — |
|  | **M10-3** | State Scenic Byway System | Optional (2D.58-06) | 24 x 24 | — | — | 2D-1 p.207 | — |
|  | **M10-3a** | State Scenic Byway - Simple Graphic and Byway | Optional (2D.58-06) | 24 x 24 | — | — | 2D-1 p.207 | — |
|  | **M10-3bP** | Scenic Byway (plaque) | Optional (2D.58-05) | 24 x 12 | — | — | 2D-1 p.207 | — |
|  | **M11-1** | National Historic Trail - Identification | Optional (2D.58-09) | 24 x 24 | — | — | 2D-1 p.207 | — |
|  | **M11-1aP** | National Historic Trail - Historic Route (plaque) | Optional (2D.58-09) | 24 x 12 | — | — | 2D-1 p.207 | — |
|  | **M11-1bP** | National Historic Trail - Crossing (plaque) | Optional (2D.58-09) | 24 x 12 | — | — | 2D-1 p.207 | — |
|  | **M11-1cP** | National Historic Trail - Auto Tour Route (plaque) | Optional (2D.58-09) | 24 x 12 | — | — | 2D-1 p.207 | — |
|  | **M11-1dP** | National Historic Trail - Distance (plaque) | Optional (2D.58-09) | 24 x 12 | — | — | 2D-1 p.207 | — |

- [O] 2D.58-05 (p.274) ◆ M10-2, M10-3bP: Identification signs for a State scenic byway may be installed along conventional roads that have been designated as part of a State scenic byway system. A Byway Identification (M10-2) sign (see Figure 2D-34) with the name of the byway displayed may be installed in a Directional or Confirming assembly with the SCENIC BYWAY (M10-3bP) plaque (see Figure 2D-34) mounted below the M10-2 sign.
- [O] 2D.58-06 (p.274) ◆ M10-2, M10-3, M10-3a: Where a National Scenic Byway is part of a State scenic byway system, the National Scenic Byways (M10-1aP) plaque (see Section 2D.57) may be installed in a Directional or Confirming assembly below the Byway Identification (M10-2) sign or State Scenic Byway (M10-3 or M10-3a) sign (see Figure 2D-34) for the State scenic byway.
- [O] 2D.58-07 (p.274) ◆ M10-2aP, M10-3: A State Scenic Byway System (M10-3) sign may be installed in a Directional or Confirming assembly with the name of the byway displayed on a Byway Identification (M10-2aP) plaque below the sign (see Figure 2D-34).
- [O] 2D.58-08 (p.274) ◆ M10-3a, M10-3bP: A State Scenic Byway (M10-3a) sign with a simple graphic and the name of the byway displayed may be installed in a Directional or Confirming assembly with the SCENIC BYWAY (M10-3bP) plaque mounted below the M10-3a sign.
- [O] 2D.58-09 (p.274) ◆ M11-1, M11-1aP, M11-1bP, M11-1cP, M11-1dP: Identification signs for a historic trail, such as the National Historic Trails administered by the National Park Service, may be installed along segments of conventional roads that coincide with the original route of the trail. National Historic Trail Identification (M11-1) signs (see Figure 2D-34) may be installed in a Directional or Confirming assembly with a HISTORIC ROUTE (M11-1aP), CROSSING (M11-1bP), or AUTO TOUR ROUTE (M11-1cP) auxiliary plaque (see Figure 2D-34) mounted below the M11-1 sign. The beginning and end of a historic trail route or auto tour route may be indicated with a BEGIN (M4-14P) or END (M4-6P) auxiliary plaque (see Figure 2D-5) with a white legend and border on a brown background mounted above the historic trail identification sign. The length of the route may be identified by a NEXT XX MILES (M11-1dP) auxiliary plaque mounted below the M11-1aP or M11-1cP auxiliary plaque. DecemberMonth 2023

<a id="sec-2D-59"></a>
#### Section 2D.59 Emergency Routing Signs and Plaques (M4-11 and M4-12 Series)

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-11](symbols/M4-11.png) | **M4-11** | Emergency Route | Optional (2D.59-09) | 30 x 30 | — | — | 2D-1 p.207 | — |
|  | **M4-11a** | Emergency Route | Optional | 30 x 30 | — | — | 2D-1 p.207 | — |
| ![M4-11bP](symbols/M4-11bP.png) | **M4-11bP** | Emergency Route To (plaque) | Optional | 30 x 18 | — | — | 2D-1 p.207 | — |
| ![M4-11cP](symbols/M4-11cP.png) | **M4-11cP** | Emergency Route To (plaque) | Optional | 30 x 18 | — | — | 2D-1 p.207 | — |
| ![M4-12](symbols/M4-12.png) | **M4-12** | End Emergency Route | Optional (2D.59-09) | 24 x 18 | — | — | 2D-1 p.207 | — |

- [O] 2D.59-02 (p.279) ◆ M4-11, M4-11a, M4-11bP, M4-11cP: EMERGENCY ROUTE (M4-11 and M4-11a) signs and EMERGENCY ROUTE TO (M4-11bP and M4-11cP) plaques mounted on a directional assembly may be permanently installed on conventional roadways to provide trailblazing along a designated diversionary route to bypass a traffic incident.
- **[M]** 2D.59-04 (p.279): Emergency Routing signs and plaques shall only be installed at departure points and along diversion routes for directing road users around highway segments in areas that are more susceptible to traffic incidents (see Figure 2D-38). EMERGENCY ROUTE and EMERGENCY ROUTE TO signs shall be placed at each turning decision point along the designated route until it rejoins the original route or until other directional signs leading back to the original route are provided.
- **[M]** 2D.59-05 (p.279): Emergency Routing signs shall have a white legend and border on a green background.
- [O] 2D.59-06 (p.279): For additional emphasis the legend EMERGENCY ROUTE or EMERGENCY ROUTE TO may be displayed in a yellow panel with black letters near the top of the sign (see Figure 2D-37).
- **[M]** 2D.59-07 (p.279): Orange or pink shall not be used as alternate colors on permanently-installed signs or plaques for rerouting traffic during an incident or other event. If a route shield is displayed as part of the message, the wording of the sign or plaque shall be EMERGENCY ROUTE TO as shown in Figure 2D-37.
- [O] 2D.59-08 (p.279) ◆ M4-11bP, M4-11cP: An EMERGENCY ROUTE TO plaque with either a white legend and border on a green background (M4-11bP) or black legend and border on a yellow background (M4-11cP) may be added to the top of a conventional Route assembly on a diversion route to provide direction back to the original route downstream of the incident (see Figures 2D-37 and 2D-38).
- [O] 2D.59-09 (p.279): A combination warning and regulatory message sign with flashing beacons mounted above and the legend, WHEN FLASHING [ROUTE] CLOSED AHEAD/ USE EMERGENCY ROUTE [NEXT RIGHT or EXIT XX] may be used in advance of the emergency route entrance to inform road users of the closure and require exiting the primary route and use of the emergency route (see Figures 2D-37 and 2D-38).
- [O] 2D.59-10 (p.279) ◆ M4-12: The End Emergency Route (M4-12) sign may be use at a point along the emergency route just prior to the junction where traffic is to reenter the primary route past the closed section of roadway (see Figure 2D-37 and 2D-38). Month 2023December 2023 DecemberMonth 2023

### Chapter 2E Guide Signs, Freeways and Expressways

<a id="sec-2E-23"></a>
#### Section 2E.23 Interchange Advance Guide Signs (E1-1 through E1-3)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E1-1** | Interchange Advance Guide (1 destination) | Mandatory (2E.23-02) | Varies | 2E-1 p.294 | — |
|  | **E1-2** | Interchange Advance Guide (2 destinations) | Mandatory (2E.23-02) | Varies | 2E-1 p.294 | — |
|  | **E1-3** | Interchange Advance Guide (3 destinations) | Mandatory (2E.23-02) | Varies | 2E-1 p.294 | — |
|  | **E1-5P** | 1-, 2-Digit Exit Number | Optional | 114 x 30 | 2E-1 p.294 | — |
|  | **E1-5aP** | LEFT | Optional | 132 x 30 | 2E-1 p.294 | — |
|  | **E1-5bP** | Left Exit Number | Optional | 138 x 30 | 2E-1 p.294 | — |
|  | **E1-5cP** | 3-Digit Exit Number (with single-letter suffix) | Optional | 156 x 30 | 2E-1 p.294 | — |
|  | **E1-5dP** | 1-, 2-Digit Exit Number (with dual-letter suffix) | Optional | 168 x 30 | 2E-1 p.294 | — |
|  | **E1-5eP** | 3-Digit Exit Number (with dual-letter suffix) | Optional | 186 x 30 | 2E-1 p.294 | — |
|  | **E1-5fP** | 1-, 2-Digit Exit Number | Optional | 114 x 54 | 2E-1 p.294 | — |
|  | **E1-5gP** | 3-Digit Exit Number | Optional | 132 x 54 | 2E-1 p.294 | — |
|  | **E1-5hP** | 1-, 2-Digit Exit Number (with single-letter suffix) | Optional | 138 x 54 | 2E-1 p.294 | — |
|  | **E1-5iP** | 3-Digit Exit Number (with single-letter suffix) | Optional | 156 x 54 | 2E-1 p.294 | — |
|  | **E1-5jP** | 1-, 2-Digit Exit Number (with dual-letter suffix) | Optional | 168 x 54 | 2E-1 p.294 | — |
|  | **E1-5kP** | 3-Digit Exit Number (with dual-letter suffix) | Optional | 186 x 54 | 2E-1 p.294 | — |
|  | **E1-5mP** | Left (plaque) | Optional | 72 x 30 | 2E-1 p.294 | — |

- **[M]** 2E.23-02 (p.312): Except as provided in Paragraph 16 of this Section, and in Paragraph 18 of Section 2E.25, at least one Interchange Advance guide sign shall be used for all interchange classifications.
- **[R]** 2E.23-03 (p.312): At major and intermediate interchanges (see Section 2E.11), at least two Interchange Advance guide signs should be used, placed at ½ mile and at 1 mile in advance of the exit. A third Interchange Advance guide sign should be placed at 2 miles in advance of the exit if spacing permits.
- **[R]** 2E.23-04 (p.312): At minor interchanges, the Interchange Advance guide sign should be located ½ to 1 mile from the exit gore.
- **[M]** 2E.23-06 (p.312): Except as provided in Section 2E.28, the legend on Interchange Advance guide signs shall contain the distance message. For each direction of travel, the legend on the Interchange Advance guide signs shall be the same as the legend on the Exit Direction sign, except that the last line shall be the distance message. The distance message shall read XX MILE(S) where exit numbers are used. Where exit numbers are not used, the distance message shall read EXIT XX MILE(S) for an interchange with one exit ramp, and EXITS XX MILE(S) for an interchange with two or more exit ramps.
- **[R]** 2E.23-07 (p.312): Where an Interchange Advance guide sign is located more than 1,000 feet to ½ mile but not more than 1 mile from the exit, the distance displayed should be to the nearest ¼ mile. Where the distance to be displayed on an Interchange Advance guide sign is 1,000 feet or less, the distance should be displayed in feet, rather than miles, to the nearest 100 feet.
- **[M]** 2E.23-08 (p.312): When a distance is displayed in miles, fractions of a mile, rather than decimals, shall be displayed in all cases.
- **[M]** 2E.23-09 (p.312): For numbered exits, the exit number used with the Interchange Advance guides signs shall be displayed using an Exit Number plaque above and abutting the Interchange Advance guide sign.
- **[M]** 2E.23-10 (p.312) ◆ E1-5P, E1-5aP, E1-5bP, E1-5cP, E1-5dP, E1-5eP, E1-5fP, E1-5gP, E1-5hP, E1-5iP, E1-5jP, E1-5kP, E1-5mP: For numbered exits to the right, an Exit Number (E1-5P through E1-5eP) plaque (see ~~Figure 2E-9~~ ) shall be added to the top right-hand edge of the sign.
- **[M]** 2E.23-11 (p.312) ◆ E1-5P, E1-5aP, E1-5bP, E1-5cP, E1-5dP, E1-5eP, E1-5fP, E1-5gP, E1-5hP, E1-5iP, E1-5jP, E1-5kP, E1-5mP: For numbered exits to the left, a Left Exit Number (E1-5fP through E1-5kP) plaque (see ~~Figure 2E-9~~ ) shall be added above the top left-hand edge of the sign (see ~~Figures 2E-~~ 18 and 2E-34).
- **[M]** 2E.23-12 (p.312) ◆ E1-5mP: For unnumbered exits to the left, a LEFT (E1-5mP) plaque (see ~~Figure 2E-~~ 9) shall be added to the top left-hand edge of the sign, abutting the sign. DecemberMonth 2023
- **[M]** 2E.23-14 (p.314): Interchange Advance guide signs for multi-lane exits having an optional exit lane that also carries the through route at major interchanges (see ~~Figures 2E-~~ 36, 2E-37, and 2E-42) and for splits with an option lane (see ~~Figures 2E-3~~ 8 and 2E-39) shall be Overhead Arrow-per-Lane signs designed in accordance with Sections 2E.39 and 2E.40.
- [O] 2E.23-15 (p.314): Where the distance between interchanges is more than 1 mile, but less than 2 miles, the first Interchange Advance guide sign may be closer than 2 miles, but not placed so as to overlap the signing for the preceding exit. Duplicate Interchange Advance guide signs or Interchange Sequence Series signs may be placed in the median on the opposite side of the roadway and are not included in the minimum requirements of interchange signing.
- **[R]** 2E.23-16 (p.314): Where there is less than 800 feet between the theoretical gores of successive interchange entrance or exit ramps, Interchange Sequence Series signs (see Section 2E.24) should be used instead of Interchange Advance guide signs for the affected interchanges.
- **[R]** 2E.23-17 (p.314): The Interchange Advance guide signs for the last exit from a highway before it becomes a facility on which toll payments are required should include the LAST EXIT BEFORE TOLL (W16-16P) plaque (see Section 2F.10 and Figure 2F-4). The plaque should be installed above the Interchange Advance guide signs, but below the Exit Number or LEFT plaque, if used.

<a id="sec-2E-24"></a>
#### Section 2E.24 Interchange Sequence Signs (E9-1 and E9-2)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E9-1** | Interchange Sequence (2 interchanges) | Recommended (2E.24-02) | Varies | 2E-1 p.295 | — |
|  | **E9-2** | Interchange Sequence (3 interchanges) | Recommended (2E.24-02) | Varies | 2E-1 p.295 | — |
|  | **E11-2** | Left (panel) | Optional | 60 x 18 | 2E-1 p.295 | — |

- [S] 2E.24-01 (p.314) ◆ E9-1, E9-2: Interchanges are sometimes closely spaced, particularly through large urban areas, so that typical guide signs cannot be adequately spaced. In such cases, Interchange Sequence signs identifying the next two (E9-1) or three (E9-2) interchanges (see Figure 2E-10) can provide the necessary exit destination guidance.
- **[R]** 2E.24-02 (p.314): Where there is less than 800 feet between the theoretical gores of successive interchange entrance or exit ramps, Interchange Sequence signs should be used instead of Interchange Advance guide signs for the affected interchanges.
- **[R]** 2E.24-03 (p.314) ◆ E9-1, E9-2: If used, Interchange Sequence (E9-1 or E9-2) signs should be used over the entire length of a route in an urban area.
- **[M]** 2E.24-05 (p.314): Interchange Sequence signs shall be installed in a series. Interchange Sequence signs shall display the next two or three interchanges by name or route number with distances to the nearest ¼ mile.
- **[M]** 2E.24-06 (p.314): The first Interchange Sequence sign in the series shall be located in advance of the first Interchange Advance guide sign for the first interchange.
- **[M]** 2E.24-07 (p.314) ◆ E11-2: Where the exit direction is to the left, a LEFT (E11-2) sign panel (see ~~Figure 2E-1~~ 7) shall be displayed on the same line immediately to the right of the interchange name or route number.
- **[M]** 2E.24-08 (p.314): Interchange Sequence signs shall not be substituted for Exit Direction signs.
- **[R]** 2E.24-09 (p.314): Interchange Sequence signs should be located in the median. After the first sign of the series, subsequent Interchange Sequence signs should be placed approximately midway between interchanges. DecemberMonth 2023
- **[M]** 2E.24-10 (p.316): Interchange Sequence signs located in the median shall be installed at overhead sign height (see Section 2A.14).
- [O] 2E.24-11 (p.316): Interchange numbers may be displayed to the left of the interchange name or route number.

<a id="sec-2E-25"></a>
#### Section 2E.25 Exit Direction Signs (E4 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E4-1** | Exit Direction (1 destination) | Recommended (2E.25-03) | Varies | 2E-1 p.294 | — |
|  | **E4-2** | Exit Direction (2 destinations) | Recommended (2E.25-03) | Varies | 2E-1 p.294 | — |
|  | **E4-3** | Exit Direction (3 destinations) | Recommended (2E.25-03) | Varies | 2E-1 p.294 | — |
|  | **E13-2** | Exit Direction Advisory Speed (panel) | Optional (2E.25-16) | 162 x 24 | 2E-1 p.295 | — |

- **[M]** 2E.25-02 (p.316): Exit Direction signs shall be used at major and intermediate interchanges. Populations or other similar information shall not be displayed on Exit Direction signs.
- **[R]** 2E.25-03 (p.316): Exit Direction signs should be used at minor interchanges (see Section 2E.30).
- **[R]** 2E.25-05 (p.316): When post-mounted, the Exit Direction sign should be installed at the beginning of the deceleration lane taper. When mounted overhead, the Exit Direction sign should be installed over the exiting lane in the vicinity of the theoretical gore. If there is less than 300 feet from the beginning of the taper to the theoretical gore, the Exit Direction sign should be installed overhead (see ~~Figure 2E-~~ 13).
- **[M]** 2E.25-06 (p.317): Except where Overhead Arrow-per-Lane guide signs are used (see Sections 2E.40 and 2E.42, and Paragraph 7 of this Section), where a through lane is being terminated (dropped) at an exit, the Exit Direction sign shall be placed overhead at the theoretical gore (see ~~Figures 2E-~~ 18, 2E-19, 2E-33, 2E-42, and 2E-46).
- **[M]** 2E.25-07 (p.317): Except as provided in Paragraph 4 of Section 2E.40, where Overhead Arrow-per-Lane guide signs are used for the Interchange Advance guide sign(s) for a multi-lane exit having an optional exit lane that also carries the through route or for a split with an option lane (see Section 2E.40), an Overhead Arrow-per-Lane guide sign shall also be used instead of the Exit Direction sign and located near, but not downstream from, the point where the outside edge of the dropped lane begins to diverge from the main roadway (see ~~Figures 2E-~~ 36 through 2E-38). The Overhead Arrow-per-Lane guide sign shall be designed in accordance with the provisions of Section 2E.40. Month 2023December 2023
- **[M]** 2E.25-08 (p.318): The following provisions shall govern the design and application of overhead Exit Direction signs: A. The sign shall display the Exit Number plaque (if exit numbering is used), the route number, cardinal direction, and destination, as applicable, with a diagonally upward-pointing directional arrow (see ~~Figure 2E-1~~ 2). B. The message EXIT ONLY in black on a yellow sign panel (E11-1d or E11-1e) shall be used on the overhead Exit Direction sign to advise road users of a lane drop situation (see ~~Figures 2E-1~~ 8, 2E-19, 2E-42, and 2E-44). The sign shall comply with the provisions of Section 2E.28.
- **[M]** 2E.25-09 (p.318): For numbered exits to the right, an Exit Number (E1-5P through E1-5eP) plaque (see ~~Figure 2E-9~~ ) shall be added above the top right-hand edge of the sign.
- **[M]** 2E.25-10 (p.318): For numbered exits to the left, a Left Exit Number (E1-5fP through E1-5kP) plaque (see ~~Figure 2E-9~~ ) shall be added above the top left-hand edge of the sign.
- **[M]** 2E.25-11 (p.318): For unnumbered exits to the left, a LEFT (E1-5mP) plaque (see ~~Figure 2E-~~ 9) shall be added above the top left-hand edge of the sign.
- **[R]** 2E.25-13 (p.318): At multi-exit interchanges, the Exit Direction sign should be located directly over the exiting lane for the first exit, in accordance with this Section. An Interchange Advance guide sign for the second exit should be installed at the same location, normally over the right-hand through lane. Only for those conditions where the through movement is not evident should a confirmatory message (a Pull-Through sign as shown in ~~Figure 2E-~~ 16) be used over the left-hand lane(s) to guide road users traveling through an interchange (see Section 2E.43 for additional information on sign spreading).
- **[R]** 2E.25-14 (p.318): Where the freeway or expressway is on an overpass, the Exit Direction sign for the second exit should be installed on an overhead support over the exit lane in advance of the gore point, as near as practicable to the theoretical gore. Where the freeway or expressway passes under the crossroad and the exit ramp is located beyond the overcrossing structure, the overhead Exit Direction sign for the second exit should be placed either on the overcrossing structure (see ~~Figures 2E-~~ 29 through 2E-31) or on a separate structure located immediately in front of the overcrossing structure.
- [O] 2E.25-15 (p.318) ◆ E13-2: Where extra emphasis of an especially low advisory ramp speed is needed, an Exit Direction Advisory Speed (E13-2) sign panel (see Figure 2E-14) may be placed at the bottom of the Exit Direction sign to supplement, but not to replace, the exit or ramp advisory speed warning signs.
- [O] 2E.25-16 (p.318) ◆ E13-2: Warning Beacons in compliance with Paragraph 17 of this Section may be used with the E13-2 sign panel.
- **[M]** 2E.25-17 (p.318) ◆ E13-2: Where Warning Beacons are used in conjunction with the E13-2 sign panel within a guide sign (see ~~Figure 2E-~~ 14), the nearest edges of the beacons shall be placed at least 12 inches from the edges of the E13-2 sign panel, from the edges of the guide sign, and from any other legend within the guide sign. The design and operation of Warning Beacons shall otherwise comply with the provisions of Chapter 4S of this Manual.
- [O] 2E.25-18 (p.319): In cases, where sight distance is restricted because of structures or unusual alignment, principally in urban areas, making it impossible to locate the Exit Direction sign without violating the required minimum spacing between major guide signs (see Section 2E.23), Interchange Sequence signs (see Section 2E.24) may be substituted for an Interchange Advance guide sign.
- **[R]** 2E.25-19 (p.319): At the last exit from a highway before it becomes a facility on which toll payments are required, the LAST EXIT BEFORE TOLL (W16-16P) plaque (see Section 2F.10 and Figure 2F-4) should be installed above the Exit Direction sign, but below the Exit Number or LEFT plaque, if used.

<a id="sec-2E-26"></a>
#### Section 2E.26 Exit Gore Signs and Plaque (E5-1 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E5-1** | Exit Gore | Mandatory (2E.26-02) | 72 x 60 | 2E-1 p.294 | — |
|  | **E5-1a** | Exit Gore | Mandatory (2E.26-02) | 156 x 60 | 2E-1 p.294 | — |
|  | **E5-1bP** | Exit Gore Number | Mandatory (2E.26-02) | 120 x 30 | 2E-1 p.294 | — |
|  | **E5-1c** | Narrow Exit Gore | Mandatory (2E.26-02) | 60 x 90* | 2E-1 p.294 | — |

- **[M]** 2E.26-02 (p.319): The gore shall be defined as the area located between the main roadway and the ramp just beyond where the ramp branches from the main roadway. An Exit Gore sign shall be located in the gore for each ramp that departs from the main roadway of a freeway or expressway, or departs from a collectordistributor roadway, and shall display the word EXIT (E5-1) if interchange exit numbering is not used or EXIT XX (E5-1a or E5-1c) if interchange exit numbering is used, and an appropriate diagonally upwardpointing arrow. If suffix letters are used for exit numbering at a multi-exit interchange, the suffix letter shall also be included on the Exit Gore (E5-1a or E5-1c) sign or Exit Gore Number (E5-1bP) plaque and shall be separated from the exit number by a space having a width of between ½ and ¾ of the height of the suffix letter. Breakaway or yielding supports shall be used.
- **[R]** 2E.26-03 (p.319): The arrow should be aligned to approximate the angle of departure. Each gore should be treated similarly, whether the interchange has one exit roadway or multiple exits.
- [O] 2E.26-04 (p.319) ◆ E5-1a, E5-1c: The Narrow Exit Gore (E5-1c) sign (see ~~Figure 2E-1~~ 5) may be used in gore areas of limited width where the width of the Exit Gore (E5-1a) sign would not permit sufficient lateral offset (see Section 2A.16), such as for ramp departures that are nearly parallel to the main roadway where the Exit Gore sign would be mounted on a narrow island or barrier. Where the E5-1c sign is mounted at a height of 14 feet or more from the roadway, the directional arrow may point diagonally downward.
- **[R]** 2E.26-05 (p.319) ◆ E5-1a, E5-1c: The E5-1c sign should not be used in gore areas where an E5-1a sign could be installed with sufficient lateral offset.
- [O] 2E.26-06 (p.320): Where extra emphasis of an especially low advisory ramp speed is needed, the Confirmation Advisory Speed (W13-1aP) plaque (see Section 2C.59) indicating the advisory speed may be mounted below the Exit Gore sign (see ~~Figure 2E-~~ 15) to supplement, but not to replace, the exit or ramp advisory speed warning signs.
- [O] 2E.26-07 (p.320): To improve the visibility of the gore for exiting drivers, a Type 1 object marker (see Chapter 2C) may be installed 4 feet above the ground line on each sign support below the Exit Gore sign.
- [O] 2E.26-08 (p.320) ◆ E5-1, E5-1bP: An Exit Gore Number (E5-1bP) plaque (see ~~Figure 2E-~~ 15) may be installed above an existing Exit Gore (E5-1) sign when an unnumbered exit is converted to a numbered exit until such time as an E5-1 sign is being replaced for other reasons (see Paragraph 9 of this Section).
- **[M]** 2E.26-09 (p.320) ◆ E5-1, E5-1a, E5-1bP: An Exit Gore (E5-1a) sign shall be used when the replacement of an existing assembly of an E5-1 sign and E5-1bP plaque becomes necessary.

<a id="sec-2E-27"></a>
#### Section 2E.27 Pull-Through Signs (E6-1 Series and E6-2 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E6-1** | Pull-Through | Recommended (2E.27-02) | Varies | 2E-1 p.294 | — |
|  | **E6-1a** | Pull-Through (Destination) | Recommended (2E.27-02) | Varies | 2E-1 p.294 | — |
|  | **E6-2** | Pull-Through (Down Arrows) | Recommended (2E.27-02) | Varies | 2E-1 p.294 | — |
|  | **E6-2a** | Pull-Through (Destination, Down Arrows) | Recommended (2E.27-02) | Varies | 2E-1 p.295 | — |

- [S] 2E.27-01 (p.320): Pull-Through (E6-1 series and E6-2 series) signs (see Figure 2E-16) are overhead guide signs intended for through traffic.
- **[R]** 2E.27-02 (p.320): Pull-Through signs should be used where the geometrics of a given interchange are such that it is not clear to the road user as to which is the through roadway, or where additional route guidance is desired. Pull-Through signs with down arrows should be used where the alignment of the through lanes is curved and the exit direction is straight ahead, where the number of through lanes is not readily evident, and at multi-lane exits where there is a reduction in the number of through lanes. Pull-Through signs should not be used at exits with option lanes where full-width Overhead Arrow-per-Lane signs are being used.
- **[M]** 2E.27-03 (p.320): When used, Pull-Through signs shall display the route shield and the cardinal direction for the through route.
- [O] 2E.27-04 (p.320): Pull-Through signs may display the control city and down arrows (see ~~Figure 2E-1~~ 6 and Section 2E.18).

<a id="sec-2E-28"></a>
#### Section 2E.28 Signing for Interchange Lane Drops without an Optional Exit Lane Standard:

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E11-1** | Exit Only (with arrow) | Mandatory (2E.28-03) | 174** x 36 | 2E-1 p.295 | — |
|  | **E11-1a** | Exit | Optional (2E.28-06) | 66 x 18 | 2E-1 p.295 | — |
|  | **E11-1b** | Only | Optional (2E.28-06) | 66 x 18 | 2E-1 p.295 | — |
|  | **E11-1c** | Exit Only | Optional (2E.28-06) | 120 x 18 | 2E-1 p.295 | — |
|  | **E11-1d** | Exit Only (with arrow) | Optional | 174** x 36 | 2E-1 p.295 | — |
|  | **E11-1e** | Exit Only (with two arrows) | Optional | 222** x 36 | 2E-1 p.295 | — |
|  | **E11-1f** | Exit Only (with two arrows) | Mandatory (2E.28-03) | 222** x 36 | 2E-1 p.295 | — |

- **[M]** 2E.28-03 (p.321) ◆ E11-1, E11-1f: Except on Overhead Arrow-per-Lane and Diagrammatic Advance guide signs (see Sections 2E.39 through 2E.41), the EXIT ONLY (down arrow) (E11-1 or E11-1f) sign panel (see Figure 2E-17) shall be used on all overhead Advance guide signs of lane drops (see Figures 2E-18, 2E-19, and 2E-34). The number of arrows on each sign shall correspond to the number of dropped lanes at the location of each sign. Placement of the down arrow shall comply with the provisions of Section 2E.18.
- **[M]** 2E.28-04 (p.321) ◆ E11-1d, E11-1e: For lane drops, the bottom portion of the overhead Exit Direction sign shall be yellow with a black border and shall include a diagonally upward-pointing black directional arrow (left or right, as appropriate) for each lane dropped at the exit (see ~~Figures 2E-~~ 18 and 2E-19). The sign shall be designed and placed so that each arrow is located over the approximate center of each lane being dropped. Except as provided in Paragraph 5 of this Section, the words EXIT and ONLY shall be positioned to the left and right, respectively, of the arrow on the E11-1d sign panel (see ~~Figure 2E-~~ 17) for a single-lane drop. For a two-lane drop, the words EXIT ONLY shall be located between the two arrows on the E11-1e sign panel (see ~~Figure 2E-~~ 17). The number of arrows on the sign shall correspond to the number of dropped lanes at the location of the sign.
- [O] 2E.28-06 (p.321) ◆ E11-1a, E11-1b, E11-1c: EXIT ONLY messages of either the combination of E11-1a and E11-1b, or the E11-1c sign panels (see ~~Figure 2E-1~~ 7) may be used to retrofit existing signing to warn of a lane drop situation ahead.
- **[M]** 2E.28-07 (p.321) ◆ E11-1a, E11-1b, E11-1c: If used to retrofit an existing guide sign, the E11-1a and E11-1b sign panels (see ~~Figure 2E-~~ 17) shall be placed on either side of a white down arrow on an Interchange Advance guide sign and on either side of a white directional arrow on an Exit Direction sign. The E11-1c sign panel (see ~~Figure 2E-~~ 17), if used to retrofit an existing Interchange Advance guide sign, shall be placed between the lower destination message and the white down arrow.

<a id="sec-2E-46"></a>
#### Section 2E.46 Next Exit Plaques (E2-1P and E2-1aP)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E2-1P** | Next Exit (1 line) (plaque) | Optional (2E.46-01) | Varies x 24 | 2E-1 p.294 | — |
|  | **E2-1aP** | Next Exit (2 lines) (plaque) | Optional (2E.46-01) | Varies x 36 | 2E-1 p.294 | — |

- [O] 2E.46-01 (p.364): Where the distance to the next interchange is unusually long, a Next Exit (E2-1P or E2-1aP) plaque (see Figure 2E-49) may be installed to inform road users of the distance to the next interchange.
- **[R]** 2E.46-02 (p.364): The Next Exit plaque should not be used unless the distance between successive interchanges is more than 5 miles.
- **[R]** 2E.46-03 (p.364): Where the Next Exit plaque is used, the E2-1P plaque should be used where the width of the Interchange Advance guide sign is equal to or greater than the width of the E2-1P plaque. The E2-1aP plaque should be used where the width of the E2-1P plaque exceeds the width of the Interchange Advance guide sign.
- **[M]** 2E.46-04 (p.364): The Next Exit plaque shall display the legend NEXT EXIT XX MILES. If the Next Exit plaque is used, it shall be placed below the Interchange Advance guide sign nearest the interchange. It shall be mounted so as to not adversely affect the breakaway feature of the sign support structure.

<a id="sec-2E-48"></a>
#### Section 2E.48 Post-Interchange Distance Signs (E7-1 through E7-3)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E7-1** | Post-Interchange Distance | Optional | Varies | 2E-1 p.295 | — |
|  | **E7-2** | Post-Interchange Distance | Optional | Varies | 2E-1 p.295 | — |
|  | **E7-3** | Post-Interchange Distance | Optional | Varies | 2E-1 p.295 | — |

- **[M]** 2E.48-01 (p.364): If used, the Post-Interchange Distance sign (see Figure 2E-50) shall consist of a one-line, two-line, or three-line sign displaying the names of significant destination points and the distances to those points. The top line of the sign shall identify the next meaningful interchange with the name of the community near or through which the route passes, or if there is no community, the route number or name of the intersected highway.
- [O] 2E.48-03 (p.364): The text identification of a route may be displayed instead of a route shield, such as “U S XX,” “[State abbreviation] XX” (such as “Del XX”), or “County XX.” DecemberMonth 2023
- **[R]** 2E.48-04 (p.365): If a second line is used, it should be reserved for communities of general interest that are located on or immediately adjacent to the route or for major traffic generators along the route.
- [O] 2E.48-05 (p.365): The choice of names for the second line, if it is used, may be varied on successive Distance signs to give road users maximum information concerning communities served by the route.
- **[M]** 2E.48-06 (p.365): The third, or bottom line, shall contain the name and distance to a control city (if any) that has national significance for travelers using the route.
- **[R]** 2E.48-07 (p.365): Distances to the same destinations should not be shown more frequently than at 5-mile intervals. The distances displayed on these signs should be the actual distance to the destination points and not to the exit from the freeway or expressway. The distance displayed for each community should comply with the provisions of Section 2D.43.

<a id="sec-2E-49"></a>
#### Section 2E.49 Post-Interchange Travel Time Sign (E7-4)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E7-4** | Post-Interchange Travel Time | Optional | Varies | 2E-1 p.295 | — |

- **[M]** 2E.49-03 (p.365): If used, the PostInterchange Travel Time (E7-4) sign (see Figure 2E-51) shall replace of the PostInterchange Distance sign in the series of post-interchange signs (see Section 2E.47).
- **[M]** 2E.49-04 (p.365): The PostInterchange Travel Time sign shall comply with the provisions of
- **[M]** 2E.49-05 (p.365): Travel times shall not be used on Interchange guide signs (see Section 2E.21). Month 2023December 2023

<a id="sec-2E-50"></a>
#### Section 2E.50 Distance and Travel Time Sign (E7-5) and Comparative Travel Time Sign (E7-6)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E7-5** | Distance and Travel Time | Optional | Varies | 2E-1 p.295 | — |
|  | **E7-6** | Comparative Travel Time | Optional | Varies | 2E-1 p.295 | — |

- **[M]** 2E.50-04 (p.366) ◆ E7-5: The Distance and Travel Time (E7-5) sign (see Figure 2E-52) shall display a major destination, landmark, or junction; a distance message; and a travel time message, each on a separate line. The distance units shall be displayed in the distance message. The travel time shall be displayed in a changeable message element and the abbreviation MINS shall follow the changeable message element. The Distance and Travel Time sign shall not display distance and time to more than one destination or junction.
- **[M]** 2E.50-05 (p.366) ◆ E7-6: The Comparative Travel Time (E7-6) sign (see ~~Figure 2E-~~ 52) shall display a major destination, landmark, or junction, and two alternative routes with travel time messages. Each alternative route and associated travel time message shall be on a separate line. The travel time shall be displayed in a changeable message element and the abbreviation MINS shall follow the changeable message element.
- **[M]** 2E.50-06 (p.366): Comparative travel times shall not be used to promote different modes of travel, such as personal vehicle highway travel compared with transit, or different forms of transit.
- **[R]** 2E.50-07 (p.366): Where used, the Distance and Travel Time sign should be located between interchanges and away from the sequence of interchange guide signs or other major signs.
- **[R]** 2E.50-08 (p.366): Where used, the Comparative Travel Time sign should be located in advance of the sequence of interchange guide signs to provide adequate time for the road user to decide whether to reroute.

<a id="sec-2E-51"></a>
#### Section 2E.51 Supplemental Guide Signs (E3 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E3-1** | Supplemental (1 destination) | Recommended (2E.51-04) | Varies | 2E-1 p.294 | — |
|  | **E3-2** | Supplemental (2 destinations) | Recommended (2E.51-04) | Varies | 2E-1 p.294 | — |

- **[R]** 2E.51-02 (p.367): Use of Supplemental guide signs should be limited to situations where there is a demonstrated need to sign for more destinations from an interchange than those that are displayed on the Interchange Advance guide and Exit Direction signs.
- **[R]** 2E.51-03 (p.367): A Supplemental guide sign should not be installed unless a destination meets the criteria established by the State or agency policy. States and other agencies should adopt an appropriate policy for installing Supplemental guide signs using the “AASHTO Guidelines for the Selection of Supplemental Guide Signs for Traffic Generators Adjacent to Freeways.” In developing policies for such signing, such items as population, amount of traffic generated, distance from the route, and the significance of the destination, should be taken into account.
- **[R]** 2E.51-04 (p.367): No more than one Supplemental guide sign should be used on each interchange approach.
- **[R]** 2E.51-05 (p.367): A Supplemental guide sign should display no more than two destinations and no more than three lines of destination names. Destination names should be followed by the interchange number (and suffix), or if interchanges are not numbered, by the legend NEXT RIGHT or SECOND RIGHT or both, as appropriate. The Supplemental guide sign should be installed as an independent guide sign assembly.
- **[R]** 2E.51-06 (p.367): Where two or more Interchange Advance guide signs are used, the Supplemental guide sign should be installed approximately midway between two of the Interchange Advance guide signs. If only one Interchange Advance guide sign is used, the Supplemental guide sign should follow it by at least 800 feet. If the interchanges are numbered, the interchange number Figure 2E-54. Examples of Supplemental should be used for the action message. Guide Signs for a Park-and-Ride Facility
- **[R]** 2E.51-07 (p.367): A Supplemental guide sign should not be installed in the same location with or where it will detract from guide signs for a different interchange.
- **[M]** 2E.51-08 (p.367): No more than two supplemental traffic generator destinations shall be signed from a single interchange approach and four from a single interchange along the main roadway (see Paragraphs 4 and 5 of this Section regarding the number of Supplemental guide signs at an interchange and the number of destinations displayed on a Supplemental guide sign).
- **[M]** 2E.51-09 (p.367): Supplemental guide signs shall not be placed at the same location as Interchange Advance guide, Exit Direction, or other signs related to an exit or interchange. B – Route without exit numbering
- **[M]** 2E.51-10 (p.367): Guide signs for park-and-ride facilities shall be considered as Supplemental guide signs (see Figure 2E-54).
- **[M]** 2E.51-11 (p.367): Guide signs for recreational or cultural interest destinations (see Chapter 2M) shall be considered as Supplemental guide signs, except where the interchange provides direct access to such a destination and the destination is instead displayed on the Interchange Advance guide and Exit Direction signs. Month 2023December 2023
- [O] 2E.51-12 (p.368): The pictograph of a transit provider (see definition in Section 1C.02) may be displayed on the Park – Ride Supplemental guide sign or on a Supplemental guide sign for a transit facility.
- **[R]** 2E.51-13 (p.368): The use of a transit pictograph and/or the carpool symbol on the PARK – RIDE Supplemental guide sign should comply with the provisions of Paragraph 5 of Section 2D.48.
- **[M]** 2E.51-14 (p.368): When a transit pictograph is displayed on the PARK – RIDE Supplemental guide sign, it shall be located on the same line as the carpool symbol, if used, above the word legend.
- **[M]** 2E.51-15 (p.368): The maximum dimension (height or width) of a pictograph on a sign shall not exceed two times the upper-case letter height of the destination or PARK – RIDE legend.

<a id="sec-2E-52"></a>
#### Section 2E.52 Community Interchanges Identifcation Signs (E9i -4 and E9-5)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E9-4** | Community Interchanges (2 interchanges) | Optional | Varies | 2E-1 p.295 | — |
|  | **E9-5** | Community Interchanges (3 interchanges) | Optional (2E.52-05) | Varies | 2E-1 p.295 | — |

- [S] 2E.52-01 (p.368): For suburban or rural communities served by two or three interchanges, Community Interchanges Identification (E9-4 and E9-5) signs (see Figure 2E-55) reduce the amount of information displayed on the Interchange Advance guide and Exit Direction signs by eliminating repetition of the same destinations for separate interchanges.
- **[R]** 2E.52-02 (p.368): In these cases, the name of the community followed by the word Exits should be displayed on the top line; the lines below should display the destination, road name or route number, and the corresponding distances to the nearest ¼ mile.
- **[R]** 2E.52-03 (p.368): The sign should be located in advance of the first Interchange Advance guide sign for the first interchange within the community (see Figure 2E-56).
- **[R]** 2E.52-04 (p.368): The legend displayed on the Interchange Advance guide and Exit Direction signs for each interchange should be consistent with the interchange names displayed on the Community Interchanges Identification sign. The name of the community displayed on the Community Interchanges Identification signs should be omitted from the legends of the Interchange Advance guide and Exit Direction signs.
- [O] 2E.52-05 (p.368): If interchanges are not conveniently identifiable or if there are more than three interchanges to be identified, the Next Exits sign (see Section 2E.53) may be used.

<a id="sec-2E-53"></a>
#### Section 2E.53 Next Exits Signs (E9-3 and E9-3a)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **E9-3** | Next Exits (1 destination) | Optional | Varies | 2E-1 p.295 | — |
|  | **E9-3a** | Next Exits (2 destinations) | Optional | Varies | 2E-1 p.295 | — |

- [O] 2E.53-02 (p.368): Such regions or areas may be indicated by a Next Exits (E9-3 or E9-3a) sign (see Figure 2E-57) located in advance of the Advance guide sign or signs for the first interchange.
- **[R]** 2E.53-03 (p.368): The sign legend should identify the region or area followed by the words NEXT XX EXITS.
- **[R]** 2E.53-04 (p.368): The legend displayed on the Interchange Advance guide and Exit Direction signs for each interchange should not display the region or area name that is displayed on the Next Exits sign (see Figure 2E-58). DecemberMonth 2023

<a id="sec-2E-56"></a>
#### Section 2E.56 Eisenhower Interstate System Signs (M1-10 and M1-10a)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **M1-10** | Eisenhower Interstate System | Optional (2E.56-01) | 36 x 36 | 2E-1 p.295 | — |
|  | **M1-10a** | Eisenhower Interstate System | Optional (2E.56-01) | 36 x 36 | 2E-1 p.295 | — |

- [O] 2E.56-01 (p.374): The Eisenhower Interstate System (M1-10 and M1-10a) signs (see Figure 2E-61) may be used, in accordance with Paragraphs 2 and 3 of this Section, on Interstate highways at periodic intervals and in rest areas, scenic overlooks, or other similar roadside facilities on the Interstate Highway System.
- **[M]** 2E.56-02 (p.374) ◆ M1-10a: If used, the M1-10a sign shall be used only in rest areas or other similar facilities where the sign can be viewed by occupants of parked vehicles or by pedestrians. The M1-10a sign shall not be installed on Interstate highway mainlines, ramps, or other roadways where it can be viewed by vehicular traffic.
- **[M]** 2E.56-03 (p.374): The M1-10 and M1-10a signs shall not be used as part of a Junction, Advance Route Turn, Directional, or Trailblazer Assembly, or as part of a guide sign or similar assembly providing direction to a route or destination. DecemberMonth 2023

### Chapter 2F Toll Road Signs

<a id="sec-2F-04"></a>
#### Section 2F.04 Regulatory Signs for Toll Plazas

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-28](symbols/R3-28.png) | **R3-28** | Toll Rate | Optional (2F.04-14) | — | — | 114 x 48 | 114 x 48 | — | — | 2F-1 p.381 | — |
| ![R3-29P](symbols/R3-29P.png) | **R3-29P** | Pay Toll (plaque) | Optional (2F.04-10) | — | — | 24 x 18 | 24 x 18 | — | — | 2F-1 p.381 | — |
| ![R3-30P](symbols/R3-30P.png) | **R3-30P** | Take Ticket (plaque) | Optional (2F.04-10) | — | — | 24 x 18 | 24 x 18 | — | — | 2F-1 p.381 | — |

- [O] 2F.04-10 (p.383) ◆ R3-29P, R3-30P: A STOP (R1-1) sign may be installed to require all vehicles to come to a complete stop to pay a toll in an attended or exact change lane, even if that lane is also available for optional use by vehicles with registered ETC accounts. A PAY TOLL (R3-29P) or TAKE TICKET (R3-30P) plaque (see Figure 2F-2), as appropriate to the operation, may be installed directly under the STOP (R1-1) sign for a toll plaza lane, if needed.
- [O] 2F.04-14 (p.384) ◆ R3-28: A Toll Rate (R3-28) sign (see Figure 2F-2) may be installed in advance of the toll plaza to indicate the toll applicable to the various vehicle types.
- **[R]** 2F.04-15 (p.384) ◆ R3-28: If used, the Toll Rate (R3-28) sign should be located between the toll plaza and the first advance sign informing road users of the toll plaza.
- **[R]** 2F.04-16 (p.384) ◆ R3-28: The R3-28 sign should not contain more than three lines of legend. Each line that shows a toll amount should display only a single toll amount.

<a id="sec-2F-05"></a>
#### Section 2F.05 Electronic Toll Collection (ETC) Account-Only Regulatory Sign and Plaque (R3-31 and R3-32P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **R3-31** | ETC Account-Only | Optional | 24 x 24 | 24 x 24 | 36 x 36 | 36 x 36 | 24 x 24 | 36 x 36 | 2F-1 p.381 | — |
|  | **R3-32P** | No Cash (plaque) | Optional | 24 x 12 | 24 x 12 | 36 x 18 | 36 x 18 | 24 x 12 | 36 x 18 | 2F-1 p.381 | — |

- **[M]** 2F.05-01 (p.384) ◆ R3-31: In any route sign assembly providing directions to a toll facility, or to a tolled segment of a highway, where electronic toll collection (ETC) is the only payment method accepted and all vehicles are required to have a registered ETC account, the ETC Account-Only (R3-31) sign (see Figure 2F-3) shall be mounted directly below the route sign of the numbered or named toll facility. The R3-31 sign shall have a white border and purple background and incorporate the pictograph adopted by the toll facility’s ETC payment system and the word ONLY in black letters on a white panel set on the purple background of the sign.
- [O] 2F.05-02 (p.384): The NO CASH (R3-32P) plaque (see Figure 2F-3) with a black legend and border on a white background may be mounted directly below the R3-31 sign in a Directional or other sign assembly.

<a id="sec-2F-06"></a>
#### Section 2F.06 Pay Toll and Take Ticket Advance Warning Signs (W9-6 and W9-6e)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W9-6](symbols/W9-6.png) | **W9-6** | Pay Toll XX Miles | Recommended (2F.06-02) | 96 x 66 | 96 x 66 | 96 x 66 | 96 x 66 | — | — | 2F-1 p.381 | — |
| ![W9-6e](symbols/W9-6e.png) | **W9-6e** | Take Ticket XX Miles | Recommended (2F.06-02) | 114 x 48 | 114 x 48 | 114 x 48 | 114 x 48 | — | — | 2F-1 p.381 | — |

- **[M]** 2F.06-01 (p.385): The Pay Toll (W9-6) and Take Ticket (W9-6e) Advance Warning signs shall display the distance to the toll plaza and, except for toll-ticket facilities, the toll for passenger or 2-axle vehicles (see Figure 2F-4). Where the toll for passenger or 2-axle vehicles is variable by time of day, a changeable message element shall be incorporated into the W9-6 sign to display the toll in effect.
- **[R]** 2F.06-02 (p.385) ◆ W9-6: The Pay Toll Advance Warning (W9-6) sign should be installed at approximately 1 mile and ½ mile in advance of mainline toll plazas at which some or all lanes are required to come to a stop to pay a toll (see Sections 2F.14 and 2F.15).
- **[R]** 2F.06-03 (p.385) ◆ W9-6e: The Take Ticket Advance Warning (W9-6e) sign should be installed overhead at approximately 1 mile and ½ mile in advance of mainline toll plazas at which some or all lanes are required to come to a stop to take a toll ticket (see Sections 2F.14 and 2F.15).
- **[R]** 2F.06-04 (p.385): The Pay Toll and Take Ticket Advance Warning signs should be mounted overhead.
- [O] 2F.06-05 (p.385): If there is insufficient space for the W9-6 or W9-6e sign at the 1-mile or ½-mile advance location, the Pay Toll or Take Ticket Advance Warning (W9-6bP or W9-6gP) plaque (see Section 2F.07) may be installed at those advance locations above the appropriate guide sign(s) that relate to toll payment types.
- [O] 2F.06-06 (p.385): An additional W9-6 or W9-6e sign may be installed approximately 2 miles in advance of a mainline toll plaza. This sign may be either mounted overhead or post-mounted.
- [O] 2F.06-07 (p.385): If the visibility of a ramp toll plaza at which some or all lanes are required to come to a stop to pay a toll or take a ticket is limited, the W9-6 or W9-6e sign may also be installed in advance of the ramp toll plaza.

<a id="sec-2F-07"></a>
#### Section 2F.07 Pay Toll and Take Ticket Advance Warning Plaques (W9-6bP, W9-6dP, and W9-6gP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W9-6bP](symbols/W9-6bP.png) | **W9-6bP** | Pay Toll and Take Ticket Advance Warning Plaques | Optional (2F.07-01) | — | — | — | — | — | — | text | — |
| ![W9-6gP](symbols/W9-6gP.png) | **W9-6gP** | Take Ticket XX | Optional (2F.07-01) | 216 x 30 | 216 x 30 | 216 x 30 | 216 x 30 | — | — | 2F-1 p.381 | — |

- [O] 2F.07-01 (p.385): The Pay Toll or Take Ticket Advance Warning (W9-6bP and W9-6gP) plaques (see Figure 2F-4) may be installed above the appropriate guide sign(s) relating to toll payment types at the 1-mile and/or ½-mile advance locations on the approach to a toll plaza if there is insufficient space for the W9-6 or W9-6e sign (see Section 2F.06) at those advance locations.
- **[M]** 2F.07-02 (p.385): The W9-6bP and W9-6gP plaques shall display the distance to the toll plaza and, except for toll-ticket facilities, the toll for passenger or 2-axle vehicles. Where the toll for passenger or 2-axle vehicles is variable by time of day, a changeable message element shall be incorporated into the W9-6bP plaque to display the toll in effect.
- [O] 2F.07-03 (p.385): The distance to the toll plaza may be omitted from the W9-6bP and W9-6gP plaques if the distance is displayed on the guide sign that the plaque accompanies.
- [O] 2F.07-04 (p.385): The Pay Toll (W9-6dP) plaque may be used if the toll information is displayed on the guide sign that the plaque accompanies.
- [O] 2F.07-05 (p.385) ◆ W9-6bP: The toll for passenger or 2-axle vehicles may be omitted from the W9-6bP plaque if the toll information is displayed on the guide sign that the plaque accompanies.

<a id="sec-2F-08"></a>
#### Section 2F.08 Stop Ahead Pay Toll and Take Ticket Warning Signs (W9-6a and W9-6f)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W9-6a](symbols/W9-6a.png) | **W9-6a** | Stop Ahead Pay Toll | Recommended (2F.08-02) | 114 x 66 | 114 x 66 | 114 x 66 | 114 x 66 | — | — | 2F-1 p.381 | — |
| ![W9-6f](symbols/W9-6f.png) | **W9-6f** | Stop Ahead Take Ticket | Recommended (2F.08-02) | 114 x 48 | 114 x 48 | 114 x 48 | 114 x 48 | — | — | 2F-1 p.381 | — |

- **[M]** 2F.08-01 (p.385) ◆ W9-6a: The Stop Ahead Pay Toll (W9-6a) warning sign (see Figure 2F-4) shall display the toll for passenger or 2-axle vehicles. Where the toll for passenger or 2-axle vehicles is variable by time of day, a changeable message element shall be incorporated into the W9-6a sign to display the toll in effect.
- **[R]** 2F.08-02 (p.385) ◆ W9-6a: The Stop Ahead Pay Toll (W9-6a) sign should be installed downstream from the W9-6 sign that is ½ mile in advance of a mainline toll plaza where some or all of the lanes are required to come to a stop to pay a toll (see Sections 2F.14 and 2F.15).
- **[R]** 2F.08-03 (p.387) ◆ W9-6f: The Take Ticket (W9-6f) warning sign (see Figure 2F-4) should be installed downstream from the W9-6e sign that is ½ mile in advance of a mainline toll plaza where some or all of the lanes are required to come to a stop to take a toll ticket (see Sections 2F.14 and 2F.15).
- **[R]** 2F.08-04 (p.387): The W9-6a and W9-6f signs should be mounted overhead. The location of the overhead sign should coincide with the approximate location where the mainline lanes begin to widen on the approach to the toll plaza lanes.
- **[R]** 2F.08-05 (p.387): Where open-road tolling is used in addition to a toll plaza at a particular location, the W9-6a or W9-6f sign should be located such that the message is clearly related to the lanes that access the toll plaza and not to the open-road tolling lanes.
- [O] 2F.08-06 (p.387): If there is insufficient space for the W9-6a or W9-6f sign at the recommended location, the Stop Ahead Pay Toll (W9-6cP) or the Stop Ahead Take Ticket (W9-6hP) plaque (see Section 2F.09) may be installed at that location above the appropriate guide sign that relates to toll payment types.
- [O] 2F.08-07 (p.387): If the visibility of a ramp toll plaza at which some or all lanes are required to come to a stop to pay a toll or take a ticket is limited, the W9-6a or W9-6f sign may also be installed in advance of the ramp toll plaza.

<a id="sec-2F-09"></a>
#### Section 2F.09 Stop Ahead Pay Toll and Take Ticket Warning Plaques (W9- 6cP and W9-6hP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W9-6cP](symbols/W9-6cP.png) | **W9-6cP** | Stop Ahead
Pay Toll | Optional (2F.09-01) | 264* x 30 | 264* x 30 | 264* x 30 | 264* x 30 | — | — | 2F-1 p.381 | — |
| ![W9-6dP](symbols/W9-6dP.png) | **W9-6dP** | Stop Ahead Pay | Optional (2F.09-01) | 114 x 48 | 114 x 48 | 114 x 48 | 114 x 48 | — | — | 2F-1 p.381 | — |
| ![W9-6hP](symbols/W9-6hP.png) | **W9-6hP** | Stop Ahead Take | Optional (2F.09-01) | 282 x 30 | 282 x 30 | 282 x 30 | 282 x 30 | — | — | 2F-1 p.381 | — |

*Also governed by Section 2F.07:*

- [O] 2F.07-01 (p.385): The Pay Toll or Take Ticket Advance Warning (W9-6bP and W9-6gP) plaques (see Figure 2F-4) may be installed above the appropriate guide sign(s) relating to toll payment types at the 1-mile and/or ½-mile advance locations on the approach to a toll plaza if there is insufficient space for the W9-6 or W9-6e sign (see Section 2F.06) at those advance locations.
- **[M]** 2F.07-02 (p.385): The W9-6bP and W9-6gP plaques shall display the distance to the toll plaza and, except for toll-ticket facilities, the toll for passenger or 2-axle vehicles. Where the toll for passenger or 2-axle vehicles is variable by time of day, a changeable message element shall be incorporated into the W9-6bP plaque to display the toll in effect.
- [O] 2F.07-03 (p.385): The distance to the toll plaza may be omitted from the W9-6bP and W9-6gP plaques if the distance is displayed on the guide sign that the plaque accompanies.
- [O] 2F.07-04 (p.385) ◆ W9-6dP: The Pay Toll (W9-6dP) plaque may be used if the toll information is displayed on the guide sign that the plaque accompanies.
- [O] 2F.07-05 (p.385): The toll for passenger or 2-axle vehicles may be omitted from the W9-6bP plaque if the toll information is displayed on the guide sign that the plaque accompanies.

- [O] 2F.09-01 (p.387) ◆ W9-6cP: The Stop Ahead Pay Toll (W9-6cP) warning plaque (see Figure 2F-4) may be installed above the appropriate guide sign at the location specified for the Stop Ahead Pay Toll (W9-6a) sign (see Section 2F.08) if there is insufficient space for the W9-6a sign at that location and the toll information is displayed on the guide sign that the plaque accompanies.
- [O] 2F.09-02 (p.387) ◆ W9-6hP: The Take Ticket (W9-6hP) warning plaque (see Figure 2F-4) may be installed above the appropriate guide sign at the location specified for the Take Ticket (W9-6f) sign (see Section 2F.08) if there is insufficient space for the W9-6f sign at that location.

<a id="sec-2F-10"></a>
#### Section 2F.10 LAST EXIT BEFORE TOLL Warning Plaques (W16-16P and W16-16aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ![W16-16P](symbols/W16-16P.png) | **W16-16P** | Ticket (plaque) | Recommended (2F.10-01) | — | — | — | — | — | — | 2F-1 p.381 | — |
| ![W16-16aP](symbols/W16-16aP.png) | **W16-16aP** | Last Exit Before Toll | Recommended (2F.10-01) | — | — | 144 x 54 | 144 x 54 | — | — | 2F-1 p.381 | — |

- **[R]** 2F.10-01 (p.387): The LAST EXIT BEFORE TOLL (W16-16P or W16-16aP) warning plaque (see Figure 2F-4) should be used to notify road users of the last exit from a highway before it becomes a facility on which toll payments are required. The plaque should be installed above the appropriate guide signs for the exit (see Sections 2E.23 and 2E.25), but below the Exit Number or LEFT plaque if used.

<a id="sec-2F-11"></a>
#### Section 2F.11 TOLL Warning Plaque (W16-17P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **W16-17P** | Toll (plaque) | Optional | 24 x 12 | 24 x 12 | 36 x 18 | 36 x 18 | 24 x 12 | 36 x 18 | 2F-1 p.381 | — |

- **[M]** 2F.11-01 (p.387): The TOLL (W16-17P) warning plaque (see Figure 2F-3) shall have a black legend and border on a yellow background and shall be mounted directly above the route sign of a numbered toll highway or, if used, above the cardinal direction and alternative route auxiliary signs, in any route sign assembly providing direction to a toll highway or to a segment of a highway on which the payment of a toll is required.

<a id="sec-2F-12"></a>
#### Section 2F.12 Toll Facility and Toll Plaza Guide Signs – General

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **M4-17** | Toll Collector | Optional | — | — | 48 x 48 | 48 x 48 | — | — | 2F-1 p.381 | — |
|  | **M4-18** | Exact Change | Optional | — | — | 48 x 48 | 48 x 48 | — | — | 2F-1 p.381 | — |

- **[M]** 2F.12-14 (p.392) ◆ M4-17: Signs for attended lanes at toll plazas shall incorporate the Toll Collector (M4-17) symbol panel (see Figure 2F-9).
- **[M]** 2F.12-16 (p.392) ◆ M4-18: Signs for Exact Change lanes at toll plazas shall incorporate the Exact Change (M4-18) symbol panel and, except for ticketed systems, display the amount of the toll for passenger vehicles (see Figure 2F-9).
- **[M]** 2F.12-18 (p.392): When used, the M4-17 and M4-18 symbol panels shall be used only as panels within guide signs. The M4-17 and M4-18 symbols or panels shall not be used as an independent sign or within a sign assembly.

### Chapter 2G Preferential and Managed Lane Signs

<a id="sec-2G-04"></a>
#### Section 2G.04 Vehicle Occupancy Definition Signs (R3-10 Series and R3-13 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-10](symbols/R3-10.png) | **R3-10** | Vehicle Occupancy Definition | Mandatory (2G.04-01) | 30 x 42 | 30 x 42 | 36 x 60 | 78 x 96 | 78 x 96 | 2G-1 p.407 | — |
| ![R3-10a](symbols/R3-10a.png) | **R3-10a** | ILEV | Mandatory (2G.04-01) | 30 x 42 | 30 x 42 | 36 x 60 | 78 x 96 | 78 x 96 | 2G-1 p.407 | — |
| ![R3-13](symbols/R3-13.png) | **R3-13** | Preferential Lane Vehicle | Mandatory (2G.04-01) | 66 x 36 | 66 x 36 | 84 x 48 | 144 x 78 | 144 x 78 | 2G-1 p.407 | — |
|  | **R3-13a** | Preferential Lane Vehicle | Mandatory (2G.04-01) | 66 x 36 | 66 x 36 | 84 x 48 | 144 x 78 | 144 x 78 | 2G-1 p.407 | — |

- **[M]** 2G.04-01 (p.412) ◆ R3-10, R3-13, R3-13a: The R3-10, R3-13, and R3-13a Vehicle Occupancy Definition signs (see Figure 2G-1) shall be used where agencies determine that it is appropriate to provide a sign that defines the minimum occupancy of vehicles that are allowed to use an HOV lane.
- **[R]** 2G.04-02 (p.412) ◆ R3-10a: The Inherently Low Emission Vehicle (ILEV) (R3-10a) sign (see Figure 2G-1) should be used when it is permissible for a properly labeled and certified ILEV, regardless of the number of occupants, to use an HOV lane. When used, the ILEV signs should be post-mounted in advance of and at intervals along the HOV lane based upon engineering judgment and the placement of other Preferential Lane regulatory signs. The R3-10a sign is only applicable to HOV lanes and should not to be used with other preferential lane applications.
- **[M]** 2G.04-05 (p.412) ◆ R3-13, R3-13a: For barrier-separated, buffer-separated, or contiguous preferential lanes where access between the preferential and general-purpose lanes is restricted to designated locations on freeways and expressways, an overhead Vehicle Occupancy Definition (R3-13 or R3-13a) sign shall be installed at least ½ mile in advance of the beginning of or initial entry point to an HOV lane. These signs shall only be displayed in advance of the beginning of or initial or intermediate entry point to HOV lanes.
- **[M]** 2G.04-06 (p.412) ◆ R3-10: For buffer-separated or contiguous HOV lanes where access is restricted to designated locations on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign shall be located at intervals not greater than ½ mile along the length of designated gaps where vehicles are allowed to legally access the HOV lane, and within designated enforcement areas as defined by the operating agency.
- [O] 2G.04-07 (p.412) ◆ R3-10: For buffer-separated or contiguous HOV lanes where access is restricted to designated locations on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign may be located at intervals of approximately ½ mile along the length of the HOV lane.
- [O] 2G.04-08 (p.415) ◆ R3-10: For barrier-separated HOV lanes on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign may be located at intervals of approximately ½ mile along the length of the HOV lane, at intermediate entry points, and at designated enforcement areas as defined by the operating agency.
- **[M]** 2G.04-09 (p.415) ◆ R3-10a: For buffer-separated or contiguous HOV lanes where continuous access with the adjacent generalpurpose lanes is provided on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R310) sign, and ILEV (R3-10a) signs, if appropriate, shall be located at intervals not greater than ½ mile along the length of the HOV lane.
- **[R]** 2G.04-10 (p.415): On freeways and expressways, the signs within each Preferential Lane regulatory sign sequence should be separated by a minimum distance of 800 feet and a maximum distance of 1,000 feet.
- **[R]** 2G.04-11 (p.415): On conventional roads, the distance between Preferential Lane regulatory signs within each sequence should be determined by engineering judgment based on speed, block length, distances from adjacent intersections, and other site-specific considerations.
- **[M]** 2G.04-12 (p.415) ◆ R3-10, R3-10a: For all types of direct access ramps that provide access to or lead to HOV lanes, a post-mounted Vehicle Occupancy Definition (R3-10) sign, and an ILEV (R3-10a) sign, if appropriate, shall be used at the beginning or initial entry point for the direct access ramp.

<a id="sec-2G-05"></a>
#### Section 2G.05 Preferential Lane Operation Signs (R3-11 Series and R3-14 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-11](symbols/R3-11.png) | **R3-11** | Preferential Lane Operation Signs | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11a](symbols/R3-11a.png) | **R3-11a** | Preferential Lane Operation | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11b](symbols/R3-11b.png) | **R3-11b** | Preferential Lane Operation | Optional (2G.05-11) | — | — | — | — | — | text | — |
|  | **R3-11c** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11d](symbols/R3-11d.png) | **R3-11d** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11e](symbols/R3-11e.png) | **R3-11e** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11f](symbols/R3-11f.png) | **R3-11f** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11g](symbols/R3-11g.png) | **R3-11g** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
| ![R3-11hP](symbols/R3-11hP.png) | **R3-11hP** | Motorcycles Allowed (plaque) | Optional (2G.05-11) | 30 x 15 | 30 x 15 | 36 x 18 | 78 x 36 | 78 x 36 | 2G-1 p.407 | — |
| ![R3-14](symbols/R3-14.png) | **R3-14** | HOV Lane Operation (overhead) | Optional (2G.05-11) | 72 x 60 | 72 x 60 | 96 x 72 | 144 x 108 | 144 x 108 | 2G-1 p.407 | — |
| ![R3-14a](symbols/R3-14a.png) | **R3-14a** | HOV Lane Operation (overhead) | Optional (2G.05-11) | 72 x 60 | 72 x 60 | 96 x 72 | 144 x 108 | 144 x 108 | 2G-1 p.407 | — |
| ![R3-14b](symbols/R3-14b.png) | **R3-14b** | HOV Lane Operation | Optional (2G.05-11) | 72 x 60 | 72 x 60 | 96 x 72 | 120 x 96 | 120 x 96 | 2G-1 p.407 | — |
| ![R3-14c](symbols/R3-14c.png) | **R3-14c** | Preferential Lane Operation | Optional (2G.05-11) | 90 x 60 | 90 x 60 | 108 x 72 | 156 x 102 | 156 x 102 | 2G-1 p.407 | — |
|  | **R3-14d** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
|  | **R3-14e** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
|  | **R3-14f** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |
|  | **R3-14g** | Preferential Lane Operation Signs (R3-11 Series and R3-14 Series) | Optional (2G.05-11) | — | — | — | — | — | text | — |

- [S] 2G.05-01 (p.415) ◆ R3-11, R3-11a, R3-11b, R3-11c, R3-11d, R3-11e, R3-11f, R3-11g, R3-11hP: The standardized sizes of post-mounted Preferential Lane Operation (R3-11 series) signs are consistent to accommodate any future addition or removal of a single line of legend for each sign. Each size accommodates two lines of legend for the times of day and days of week that the regulation is in effect. Consistent sign sizes are beneficial for agencies when ordering sign materials, as well as when making legend changes to existing signs if changes occur to operating times or occupancy restrictions in the future.
- **[R]** 2G.05-02 (p.415) ◆ R3-11, R3-14, R3-14a, R3-14b, R3-14c, R3-14d, R3-14e, R3-14f, R3-14g: Where the regulation is in effect during more than one time period of the day, such as during the morning and afternoon peak periods, the height of the R3-11 and R3-14 series signs should be suitably increased to accommodate the additional line(s) of legend.
- **[M]** 2G.05-03 (p.415): When used, the post-mounted Preferential Lane Operation (R3-11 series) signs shall be located adjacent to the preferential lane, and the overhead Preferential Lane Operation (R3-14 series) signs shall be mounted directly over the lane.
- **[M]** 2G.05-04 (p.415) ◆ R3-11, R3-11a, R3-11b, R3-11c, R3-11d, R3-11e, R3-11f, R3-11g, R3-11hP: The legend format of the post-mounted Preferential Lane Operation (R3-11 series) signs shall have the following sequence: A. Top Lines: Lanes applicable, such as “RIGHT LANE” or “2 RIGHT LANES” B. Middle Lines: Eligible uses, such as “HOV 2+ ONLY” (or 3+ or 4+, if appropriate) or “BUSES ONLY” or other applicable uses or eligible turning movements C. Bottom Lines: Applicable times and days, such as “7 AM – 9 AM” or “6:30 AM – 9:30 AM, MON-FRI”
- **[M]** 2G.05-05 (p.415) ◆ R3-14, R3-14a, R3-14b, R3-14c, R3-14d, R3-14e, R3-14f, R3-14g: The legend format of the overhead Preferential Lane Operation (R3-14 series) signs shall have the following sequence: A. Top Lines: Eligible uses, such as “HOV 2+ ONLY” (or 3+ or 4+, if appropriate) or “BUSES ONLY” or other applicable uses or eligible turning movements B. Bottom Lines: Applicable times and days, with the time and day placed above the down arrow, such as “7 AM – 9 AM” or “6:30 AM – 9:30 AM, MON-FRI.” When the operating periods exceed the available line width, the hours and days of the week shall be stacked as shown for the R3-14a sign in Figure 2G-1.
- **[M]** 2G.05-06 (p.415) ◆ R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, R3-14g: For preferential lane restrictions that are in effect on a full-time (24 hours per day, seven days per week) basis, the Preferential Lane Operation (R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, and R3-14g) signs that include a period of operation legend shall be modified to display no legend relative to the period of operation except as provided in Paragraph 7 of this Section.
- [O] 2G.05-07 (p.416) ◆ R3-11, R3-11a, R3-11d, R3-11f, R3-14, R3-14d, R3-14f: In lieu of removing the period of operation text from the Preferential Lane Operation signs for full-time operation, the legend 24 HOURS may be substituted for the times and days of the week on the Preferential Lane Operation (R3-11, R3-11a, R3-11d, R3-11f, R3-14, R3-14d, and R3-14f) signs for preferential lane restrictions that are in effect on a full-time basis.
- [S] 2G.05-08 (p.416) ◆ R3-11c: The 24 HOURS legend displayed on the R3-11c sign reinforces the full-time operation where several facilities in the same area have different hours of operation—some part time, others full time, or where the same lane changes from part-time to full-time operation somewhere along its length.
- **[M]** 2G.05-09 (p.416) ◆ R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, R3-14g: The full-time Preferential Lane Operation (R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, and R3-14g) signs that do not display a period of operation legend, as described in Paragraph 6 of this Section, shall not be used where the preferential lane restriction is in effect only on a part-time basis.
- [O] 2G.05-10 (p.416): Where additional movements are allowed from a preferential lane on an approach to an intersection by vehicles not meeting the preferential lane regulation, the format and words used in the legend in the middle lines on the post-mounted Preferential Lane Operation (R3-11 series) signs and on the top line of the overhead Preferential Lane Operation (R3-14 series) signs may be modified to accommodate the allowable movements (such as “HOV 2+ AND RIGHT TURNS ONLY”).
- [O] 2G.05-11 (p.416) ◆ R3-11hP: The MOTORCYCLES ALLOWED (R3-11hP) plaque (see Figure 2G-1) may be used where motorcycles, regardless of the number of occupants, are allowed to use an HOV lane.
- **[M]** 2G.05-12 (p.416) ◆ R3-11, R3-11a, R3-11b: If used, the MOTORCYCLES ALLOWED plaque shall be mounted below a post-mounted Preferential Lane Operation (R3-11, R3-11a, or R3-11b) sign.
- **[M]** 2G.05-13 (p.416): For all barrier-separated or buffer-separated or contiguous preferential lanes where access is restricted to designated locations, an overhead Preferential Lane Operation (R3-14 series) sign shall be used at the beginning or initial entry point on freeways, expressways, and at locations on conventional roadways where the preferential lane is not the outermost (far right or far left) lane of the roadway, and at any intermediate entry points or gaps in the barrier or buffer where vehicles are allowed to legally enter the access-restricted preferential lanes. For all barrier-separated and buffer-separated preferential lanes, post-mounted Preferential Lane Operation (R3-11 series) signs shall be used only as a supplement to the overhead signs on freeways, expressways, and at locations on conventional roadways where the preferential lane is not the outermost lane of the roadway at the beginning or initial entry point, or at any intermediate entry points or gaps in the barrier or buffer.
- **[M]** 2G.05-14 (p.416) ◆ R3-14, R3-14a, R3-14b, R3-14c, R3-14d, R3-14e, R3-14f, R3-14g: For buffer-separated or contiguous preferential lanes where continuous access with the adjacent general-purpose lanes is provided, including those where a preferential lane is added to the roadway (see Figure 2G-2 for HOV lanes) and those where a general-purpose lane transitions into a preferential lane (see Figure 2G-3 for HOV lanes), an overhead Preferential Lane Operation (R3-14 series) sign shall be used at the beginning or initial entry point of the preferential lane on freeways and expressways.
- [O] 2G.05-15 (p.416): On conventional roads where preferential lane operations exist, R3-11 series post-mounted signs may be used in lieu of or in addition to overhead R3-14 series signs, except where overhead signs are required as provided in Paragraph 14 of this Section.
- [O] 2G.05-16 (p.416): Additional overhead (R3-14 series) or post-mounted (R3-11 series) Preferential Lane Operation signs may be provided along the length of any type of preferential lane.
- **[M]** 2G.05-17 (p.416) ◆ R3-11, R3-11a, R3-11b, R3-11c, R3-11d, R3-11e, R3-11f, R3-11g, R3-11hP: For all types of direct access ramps that provide access to or lead to preferential lanes, a post-mounted Preferential Lane Operation (R3-11 series) sign shall be used at the beginning or initial entry point of the direct access ramp.
- [O] 2G.05-18 (p.416) ◆ R3-14, R3-14a, R3-14b, R3-14c, R3-14d, R3-14e, R3-14f, R3-14g: For direct access ramps to preferential lanes, an overhead Preferential Lane Operation (R3-14 series) sign may be used at the beginning or initial entry point to supplement the required post-mounted signs.
- [O] 2G.05-19 (p.416): Lane-use control signals (see Chapter 4T) may be used at access points to preferential lanes to indicate that a ramp or access roadway leading to the preferential lane or facility, or one or more specific lanes of the facility, are open or closed (see Figure 2G-1).

<a id="sec-2G-06"></a>
#### Section 2G.06 Preferential Lane Advance Signs (R3-12, R3-12e, R3-12f, R3-15, R3-15a, and R3-15d)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-12](symbols/R3-12.png) | **R3-12** | Preferential Lane Advance Signs | Recommended (2G.06-01) | 30 x 42 | 30 x 42 | 36 x 60 | 48 x 84 | 48 x 84 | 2G-1 p.407 | — |
| ![R3-12a](symbols/R3-12a.png) | **R3-12a** | Preferential Lane Ends Signs | Mandatory (2G.06-02) | 30 x 42 | 30 x 42 | 36 x 60 | 48 x 84 | 48 x 84 | 2G-1 p.407 | — |
| ![R3-12b](symbols/R3-12b.png) | **R3-12b** | High-Occupancy Vehicles | Mandatory (2G.06-01) | 30 x 42 | 30 x 42 | 36 x 60 | 48 x 84 | 48 x 84 | 2G-1 p.407 | — |
| ![R3-12e](symbols/R3-12e.png) | **R3-12e** | The Preferential Lane Advance | Recommended (2G.06-01) | — | — | — | — | — | text | — |
| ![R3-15](symbols/R3-15.png) | **R3-15** | HOV Lane Ahead (overhead) | Recommended (2G.06-01) | 66 x 36 | 66 x 36 | 84 x 48 | 102 x 60 | 102 x 60 | 2G-1 p.407 | — |
| ![R3-15a](symbols/R3-15a.png) | **R3-15a** | HOV Lane Begins XX Miles | Recommended (2G.06-01) | 78 x 48 | 114 x 72 | 144 x 84 | 150 x 108 | 150 x 108 | 2G-1 p.407 | — |

- **[R]** 2G.06-01 (p.417) ◆ R3-12, R3-12b, R3-15: The Preferential Lane Advance (R3-12, R3-12f, R3-15, and R3-15d) signs (see Figure 2G-1) should be used for advance notification of a barrier-separated, buffer-separated, or contiguous preferential lane that is added to the general-purpose lanes (see Figure 2G-2).
- **[R]** 2G.06-02 (p.417) ◆ R3-12a, R3-12e, R3-15a: The Preferential Lane Advance (R3-12e and R3-15a) signs (see Figure 2G-1) should be used for advance notification of a general-purpose lane that becomes a preferential lane (see Figure 2G-3).
- [O] 2G.06-03 (p.417): The legends on the R3-12f and R3-15d signs may be modified to suit the type of preferential lane.
- **[R]** 2G.06-04 (p.417) ◆ R3-12e, R3-15a: On conventional roads, for general-purpose lanes that become preferential lanes, a post-mounted (R3-12e) or overhead (R3-15a) Preferential Lane Advance sign should be installed in advance of the beginning of or initial entry point to the preferential lane at a distance determined by engineering judgment based on speed, traffic characteristics, and other site-specific considerations. The distance selected should provide adequate opportunity for ineligible vehicles to vacate the lane prior to the beginning of the restriction.
- **[R]** 2G.06-05 (p.417) ◆ R3-15a: On freeways and expressways, for general-purpose lanes that become preferential lanes, an overhead Preferential Lane Advance (R3-15a) sign should be installed at least 1 mile in advance of the beginning of the preferential lane restriction.
- [O] 2G.06-06 (p.417) ◆ R3-12a, R3-12b: Additional post-mounted or overhead Preferential Lane Advance signs may be placed farther in advance of or closer to the beginning or initial entry points to a preferential lane. Section 2G.07 Preferential Lane Ends Signs (R3-12a, R3-12b, R3-12c, R3-12d, R3-12g, R3-12h, R3-15b, R3-15c, and R3-15e)
- [O] 2G.06-07 (p.417) ◆ R3-12a: An overhead Preferential Lane Ends (R3-15b or R3-15e) sign may be installed instead of or in addition to a post-mounted R3-12a or R3-12g sign at the point where a preferential lane and restriction ends and traffic must merge into the general-purpose lanes.
- [O] 2G.06-08 (p.417): An overhead Preferential Lane Ends (R3-15c) sign may be installed instead of or in addition to a post-mounted R3-12c sign at the point where the preferential lane restriction ends and the lane becomes a general-purpose lane.

*Also governed by Section 2G.07:*

- **[M]** 2G.07-01 (p.417) ◆ R3-12b: A post-mounted Preferential Lane Ends (R3-12b or R3-12h) sign (see Figure 2G-1) shall be installed at least ½ mile in advance of the termination of a preferential lane on freeways and expressways.
- **[M]** 2G.07-02 (p.417) ◆ R3-12a: Except as provided in Paragraph 7 of this Section, a post-mounted Preferential Lane Ends (R3-12a or R3-12g) sign shall be installed at the point where a preferential lane and restriction end and traffic must merge into the general-purpose lanes.
- **[M]** 2G.07-03 (p.417): A post-mounted Preferential Lane Ends (R3-12d) sign (see Figure 2G-1) shall be installed at least ½ mile in advance of the point where a preferential lane restriction ends and the lane becomes a general- purpose lane on freeways and expressways.
- **[M]** 2G.07-04 (p.417): Except as provided in Paragraph 8 of this Section, a post-mounted Preferential Lane Ends (R3-12c) sign shall be installed at the point where a preferential lane restriction ends and the lane becomes a general- purpose lane.
- **[R]** 2G.07-05 (p.417): On conventional roads, the distance at which Preferential Lane Ends signs are installed in advance of the termination of a preferential lane and/or restriction should be determined by engineering judgment.
- [O] 2G.07-06 (p.417): The legends on the R3-12g and R3-15e signs may be modified to suit the type of preferential lane.
- [O] 2G.07-07 (p.417) ◆ R3-12a: An overhead Preferential Lane Ends (R3-15b or R3-15e) sign may be installed instead of or in addition to a post-mounted R3-12a or R3-12g sign at the point where a preferential lane and restriction ends and traffic must merge into the general-purpose lanes.
- [O] 2G.07-08 (p.417): An overhead Preferential Lane Ends (R3-15c) sign may be installed instead of or in addition to a post-mounted R3-12c sign at the point where the preferential lane restriction ends and the lane becomes a general-purpose lane.

<a id="sec-2G-07"></a>
#### Section 2G.07 Preferential Lane Ends Signs (R3-12a, R3-12b, R3-12c, R3-12d, R3-12g, R3-12h,

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-12c](symbols/R3-12c.png) | **R3-12c** | Preferential Lane Ends | Mandatory (2G.07-01) | — | — | — | — | — | text | — |
| ![R3-12d](symbols/R3-12d.png) | **R3-12d** | A post-mounted Preferential Lane Ends | Mandatory (2G.07-01) | — | — | — | — | — | text | — |
| ![R3-12f](symbols/R3-12f.png) | **R3-12f** | Preferential Lane Ahead or Ends | Mandatory (2G.07-01) | 30 x 36 | 30 x 36 | 36 x 48 | 48 x 60 | 48 x 60 | 2G-1 p.407 | — |
| ![R3-12g](symbols/R3-12g.png) | **R3-12g** | Preferential Lane Ahead or Ends | Mandatory (2G.07-01) | 30 x 36 | 30 x 36 | 36 x 48 | 48 x 60 | 48 x 60 | 2G-1 p.407 | — |
| ![R3-12h](symbols/R3-12h.png) | **R3-12h** | Preferential Lane Ends | Mandatory (2G.07-01) | 36 x 48 | 36 x 48 | 48 x 66 | 60 x 84 | 60 x 84 | 2G-1 p.407 | — |
| ![R3-15b](symbols/R3-15b.png) | **R3-15b** | HOV Lane Ends (overhead) | Optional (2G.07-07) | 66 x 36 | 66 x 36 | 84 x 48 | 102 x 60 | 102 x 60 | 2G-1 p.407 | — |
| ![R3-15c](symbols/R3-15c.png) | **R3-15c** | Preferential Lane Ends | Optional (2G.07-08) | 66 x 36 | 66 x 36 | 84 x 48 | 102 x 60 | 102 x 60 | 2G-1 p.407 | — |
| ![R3-15d](symbols/R3-15d.png) | **R3-15d** | Preferential Lane Ahead or Ends | Mandatory (2G.07-01) | 42 x 36 | 42 x 36 | 54 x 48 | 72 x 60 | 72 x 60 | 2G-1 p.407 | — |
| ![R3-15e](symbols/R3-15e.png) | **R3-15e** | Preferential Lane Ahead or Ends | Optional (2G.07-07) | 42 x 36 | 42 x 36 | 54 x 48 | 72 x 60 | 72 x 60 | 2G-1 p.407 | — |

*Also governed by Section 2G.06:*

- **[R]** 2G.06-01 (p.417) ◆ R3-12f, R3-15d: The Preferential Lane Advance (R3-12, R3-12f, R3-15, and R3-15d) signs (see Figure 2G-1) should be used for advance notification of a barrier-separated, buffer-separated, or contiguous preferential lane that is added to the general-purpose lanes (see Figure 2G-2).
- **[R]** 2G.06-02 (p.417): The Preferential Lane Advance (R3-12e and R3-15a) signs (see Figure 2G-1) should be used for advance notification of a general-purpose lane that becomes a preferential lane (see Figure 2G-3).
- [O] 2G.06-03 (p.417) ◆ R3-12f, R3-15d: The legends on the R3-12f and R3-15d signs may be modified to suit the type of preferential lane.
- **[R]** 2G.06-04 (p.417): On conventional roads, for general-purpose lanes that become preferential lanes, a post-mounted (R3-12e) or overhead (R3-15a) Preferential Lane Advance sign should be installed in advance of the beginning of or initial entry point to the preferential lane at a distance determined by engineering judgment based on speed, traffic characteristics, and other site-specific considerations. The distance selected should provide adequate opportunity for ineligible vehicles to vacate the lane prior to the beginning of the restriction.
- **[R]** 2G.06-05 (p.417): On freeways and expressways, for general-purpose lanes that become preferential lanes, an overhead Preferential Lane Advance (R3-15a) sign should be installed at least 1 mile in advance of the beginning of the preferential lane restriction.
- [O] 2G.06-06 (p.417): Additional post-mounted or overhead Preferential Lane Advance signs may be placed farther in advance of or closer to the beginning or initial entry points to a preferential lane. Section 2G.07 Preferential Lane Ends Signs (R3-12a, R3-12b, R3-12c, R3-12d, R3-12g, R3-12h, R3-15b, R3-15c, and R3-15e)
- [O] 2G.06-07 (p.417): An overhead Preferential Lane Ends (R3-15b or R3-15e) sign may be installed instead of or in addition to a post-mounted R3-12a or R3-12g sign at the point where a preferential lane and restriction ends and traffic must merge into the general-purpose lanes.
- [O] 2G.06-08 (p.417): An overhead Preferential Lane Ends (R3-15c) sign may be installed instead of or in addition to a post-mounted R3-12c sign at the point where the preferential lane restriction ends and the lane becomes a general-purpose lane.

- **[M]** 2G.07-01 (p.417) ◆ R3-12h: A post-mounted Preferential Lane Ends (R3-12b or R3-12h) sign (see Figure 2G-1) shall be installed at least ½ mile in advance of the termination of a preferential lane on freeways and expressways.
- **[M]** 2G.07-02 (p.417) ◆ R3-12g: Except as provided in Paragraph 7 of this Section, a post-mounted Preferential Lane Ends (R3-12a or R3-12g) sign shall be installed at the point where a preferential lane and restriction end and traffic must merge into the general-purpose lanes.
- **[M]** 2G.07-03 (p.417) ◆ R3-12d: A post-mounted Preferential Lane Ends (R3-12d) sign (see Figure 2G-1) shall be installed at least ½ mile in advance of the point where a preferential lane restriction ends and the lane becomes a general- purpose lane on freeways and expressways.
- **[M]** 2G.07-04 (p.417) ◆ R3-12c: Except as provided in Paragraph 8 of this Section, a post-mounted Preferential Lane Ends (R3-12c) sign shall be installed at the point where a preferential lane restriction ends and the lane becomes a general- purpose lane.
- **[R]** 2G.07-05 (p.417): On conventional roads, the distance at which Preferential Lane Ends signs are installed in advance of the termination of a preferential lane and/or restriction should be determined by engineering judgment.
- [O] 2G.07-06 (p.417) ◆ R3-12g, R3-15e: The legends on the R3-12g and R3-15e signs may be modified to suit the type of preferential lane.
- [O] 2G.07-07 (p.417) ◆ R3-12g, R3-15b, R3-15e: An overhead Preferential Lane Ends (R3-15b or R3-15e) sign may be installed instead of or in addition to a post-mounted R3-12a or R3-12g sign at the point where a preferential lane and restriction ends and traffic must merge into the general-purpose lanes.
- [O] 2G.07-08 (p.417) ◆ R3-12c, R3-15c: An overhead Preferential Lane Ends (R3-15c) sign may be installed instead of or in addition to a post-mounted R3-12c sign at the point where the preferential lane restriction ends and the lane becomes a general-purpose lane.

<a id="sec-2G-09"></a>
#### Section 2G.09 High-Occupancy Vehicle (HOV) Plaque (W16-11P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **W16-11P** | High-Occupancy Vehicles (plaque) | Optional (2G.09-01) | 24 x 12 | 24 x 12 | 30 x 18 | 30 x 18 | 30 x 18 | 2G-1 p.408 | — |

- [O] 2G.09-01 (p.419): In situations where there is a need to warn drivers in an HOV lane of a specific condition, the HOV (W16-11P) plaque (see Figure 2G-4) may be used above a warning sign. The HOV plaque may be used to differentiate a warning sign applicable to the HOV lanes when the sign is also visible to traffic on the adjacent general-purpose roadway. Among the warning signs that may be possible applications of the HOV plaque are the Advisory Exit Speed, Added Lane, and Merge signs.
- [O] 2G.09-02 (p.419): The diamond symbol may be used instead of the word message HOV on the W16-11P plaque. When appropriate, the words LANE or ONLY may be used on this plaque.

<a id="sec-2G-10"></a>
#### Section 2G.10 Preferential Lane Guide Signs – General

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![E8-1](symbols/E8-1.png) | **E8-1** | Preferential Lane Entrance Gore | Optional | — | — | 48 x 96 | 48 x 96 | — | 2G-1 p.408 | — |
| ![E8-1a](symbols/E8-1a.png) | **E8-1a** | Preferential Lane Intermediate | Optional | — | — | 48 x 84 | 48 x 84 | — | 2G-1 p.408 | — |
| ![E8-2](symbols/E8-2.png) | **E8-2** | Preferential Lane Entrance | Optional | — | — | 228 x 72 | 228 x 72 | — | 2G-1 p.408 | — |
| ![E8-2a](symbols/E8-2a.png) | **E8-2a** | Preferential Lane Entrance | Optional | — | — | 186 x 108 | 186 x 108 | — | 2G-1 p.408 | — |
|  | **E8-3** | Preferential Lane Entrance Advance | Optional | — | — | 186 x 96 | 186 x 96 | — | 2G-1 p.408 | — |

- **[M]** 2G.10-09 (p.420): For HOV lanes, the diamond symbol shall appear on each Advance Guide (E8-3) sign (see Figure 2G-5), Preferential Lane Entrance Direction (E8-2 or E8-2a) sign (see Figure 2G-6), and Preferential Lane Entrance Gore (E8-1 or E8-1a) sign (see Figure 2G-7) for the designated entry and exit points for barrierseparated and buffer-separated geometric configurations and direct access ramps to or from such lanes. The diamond symbol shall not be used with preferential lanes for other types of traffic, such as bus lanes or taxi lanes.

<a id="sec-2G-13"></a>
#### Section 2G.13 Signing for Egress from Preferential Lanes to General-Purpose Lanes

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **E8-5** | Intermediate Egress Direction | Mandatory (2G.13-01) | — | — | Varies x 90 | Varies x 90 | — | 2G-1 p.408 | — |
|  | **E8-6** | Advance
Guide | Mandatory (2G.13-01) | — | — | Varies x 84 | Varies x 84 | — | 2G-1 p.408 | — |

- **[M]** 2G.13-01 (p.428): Except as provided in Paragraphs 4 and 5 of this Section, for barrier-separated, buffer-separated, and contiguous preferential lanes where egress is restricted only to designated points, post-mounted Advance Guide (E8-6) and post-mounted Intermediate Egress Direction (E8-5) signs (see Figure 2G-12) shall be installed in the median or on median barriers that separate two directions of traffic prior to and at the intermediate exit points from the preferential lanes to the general-purpose lanes (see Figure 2G-11).

<a id="sec-2G-15"></a>
#### Section 2G.15 Signing for Direct Exits from Preferential Lanes to Another Highway

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![E8-4](symbols/E8-4.png) | **E8-4** | Preferential Lane Direct Exit Gore | Mandatory (2G.15-01) | — | — | 60 x 78 | 60 x 78 | — | 2G-1 p.408 | — |

- **[M]** 2G.15-01 (p.429): For contiguous preferential lanes on the left-hand side of the roadway, Advance Guide signs, Exit Direction signs, and Exit Gore (E8-4) signs (see Figure 2G-15) specifically applicable to the preferential lanes shall be used for exits to direct access ramps, such as HOV lane ramps (see Figure 2G-16) or ramps to park-and-ride facilities.

<a id="sec-2G-18"></a>
#### Section 2G.18 Regulatory Signs for Priced Managed Lanes Standard:

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R3-40](symbols/R3-40.png) | **R3-40** | Occupancy Definition | Optional | — | — | 54 x 66 | 54 x 66 | 66 x 78 | 2G-1 p.407 | — |
| ![R3-42](symbols/R3-42.png) | **R3-42** | Priced Managed Lane Ends | Mandatory (2G.18-09) | — | — | 48 x 60 | 48 x 60 | 60 x 78 | 2G-1 p.407 | — |
| ![R3-42a](symbols/R3-42a.png) | **R3-42a** | Priced Managed Lane Ends | Mandatory (2G.18-09) | — | — | 48 x 66 | 48 x 66 | 60 x 84 | 2G-1 p.407 | — |
| ![R3-42b](symbols/R3-42b.png) | **R3-42b** | Restriction Ends | Mandatory (2G.18-09) | — | — | 48 x 60 | 48 x 60 | 60 x 78 | 2G-1 p.407 | — |
| ![R3-42c](symbols/R3-42c.png) | **R3-42c** | Restriction Ends | Mandatory (2G.18-09) | — | — | 48 x 66 | 48 x 66 | 60 x 84 | 2G-1 p.407 | — |
| ![R3-43](symbols/R3-43.png) | **R3-43** | Priced Managed Lane Vehicle | Optional | — | — | 138 x 66 | 138 x 66 | — | 2G-1 p.407 | — |
| ![R3-44](symbols/R3-44.png) | **R3-44** | Priced Managed Lane Operation | Mandatory (2G.18-06) | — | — | 90 x 84 | 90 x 84 | — | 2G-1 p.407 | — |
| ![R3-44a](symbols/R3-44a.png) | **R3-44a** | Priced Managed Lane Operation | Mandatory (2G.18-06) | — | — | 132 x 84 | 132 x 84 | — | 2G-1 p.407 | — |
|  | **R3-44b** | Priced Managed Lane Operation | Mandatory (2G.18-03) | — | — | 90 x 72 | 90 x 72 | — | 2G-1 p.407 | — |
| ![R3-45](symbols/R3-45.png) | **R3-45** | Priced Managed Lane Ends | Mandatory (2G.18-09) | — | — | 90 x 66 | 90 x 66 | — | 2G-1 p.407 | — |
| ![R3-45a](symbols/R3-45a.png) | **R3-45a** | Priced Managed Lane | Mandatory (2G.18-09) | — | — | 114 x 66 | 114 x 66 | — | 2G-1 p.407 | — |
| ![R3-48](symbols/R3-48.png) | **R3-48** | Priced Managed Lane Toll Rate | Mandatory (2G.18-03) | — | — | Varies | Varies | — | 2G-1 p.407 | — |
| ![R3-48a](symbols/R3-48a.png) | **R3-48a** | Priced Managed Lane Toll Rate | Mandatory (2G.18-03) | — | — | Varies | Varies | — | 2G-1 p.407 | — |

- **[M]** 2G.18-01 (p.435): Except as otherwise provided in this Section, the provisions of Sections 2G.03 through 2G.07 regarding regulatory signs for Preferential lanes shall apply to priced managed lanes operated at all times or at certain times with a toll payment requirement of some or all vehicles to use the lane(s). Such managed lanes shall use changeable message signs or changeable message elements within static signs to display the appropriate regulatory sign messages only when they are in effect.
- **[M]** 2G.18-02 (p.435): Regulatory signs for preferential lanes shall be appropriately modified for adaptation to a priced managed lane, where applicable, as shown in Figure 2G-18.
- **[M]** 2G.18-03 (p.435) ◆ R3-48, R3-48a: Regulatory signs shall be used to indicate the toll charged. If the toll varies the R3-48 and R3-48a signs that are shown in Figure 2G-18 shall be used to display the actual toll amount in effect at any given time.
- **[M]** 2G.18-04 (p.435): When only vehicles with a registered ETC account are allowed to use a managed lane where some or all vehicles are charged a toll, regulatory signs to indicate such a restriction shall be provided and shall incorporate the pictograph adopted by the toll facility’s ETC payment system and the word ONLY (see Section 2G.19 for the incorporation of such regulatory legends into the guide signs for the entrances to such facilities). The display of the ETC system pictograph shall comply with the provisions of Sections 2F.02 and 2F.03 as shown in Figures 2G-18 and 2G-19.
- **[M]** 2G.18-05 (p.435) ◆ R3-40, R3-43: When HOV traffic is allowed to use a priced managed lane without paying a toll and registration in a local program is not required to receive the toll exemption, the Vehicle Occupancy Definition (R3-10 or R3-13) signs (see Section 2G.04) shall be modified to delete the diamond symbol to create priced managed lane Vehicle Occupancy Definition (R3-40 and R3-43) signs to indicate the minimum occupancy related to the management strategy (see Figure 2G-19).
- **[M]** 2G.18-06 (p.435) ◆ R3-44, R3-44a: A priced managed lane HOV Lane Operation (R3-44 or R3-44a) sign (see Figure 2G-18) shall be installed at the beginning or initial entry point, and at any intermediate entry points where vehicles are allowed to legally enter an access-restricted priced managed lane.
- **[M]** 2G.18-07 (p.435): When the vehicle occupancy required for non-toll use of a managed lane is varied as a part of a priced managed lane operational strategy, regulatory signs that include changeable message elements shall be used to display the required vehicle occupancy in effect for non-toll travel.
- [O] 2G.18-08 (p.435): Where registration in a local program or ETC account is required for HOV traffic to travel in a priced managed lane without being charged a toll or by being charged a discounted toll, such information may be displayed on a separate sign within the sequence of the required regulatory and guide signs.
- **[M]** 2G.18-09 (p.435) ◆ R3-42, R3-42a, R3-42b, R3-42c, R3-45, R3-45a: R3-42 series and R3-45 series signs (see Figure 2G-18) shall be installed in accordance with the provisions of Section 2G.07 to indicate the termination of a priced managed lane or restriction. The R3-42, R3-42a, and R3-45 signs shall be used only where the managed lane and restriction end and traffic must merge into the general-purpose lanes. The R3-42b, R3-42c, and R3-45a signs shall be used only where the managed lane restriction ends and the lane becomes a general-purpose lane.

<a id="sec-2G-21"></a>
#### Section 2G.21 Regulatory Signs and Plaques for Part-Time Travel on a Shoulder

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **R3-51** | Part-Time Travel on | Mandatory (2G.21-01) | — | — | 66 x 78 | 66 x 78 | — | 2G-1 p.407 | — |
|  | **R3-51aP** | No Trucks (plaque) | Optional | — | — | 66 x 12 | 66 x 12 | — | 2G-1 p.407 | — |
|  | **R3-51bP** | No Trucks or Buses (plaque) | Optional | — | — | 66 x 24 | 66 x 24 | — | 2G-1 p.407 | — |
|  | **R3-51cP** | Emergency Stopping Only | Optional | — | — | 54 x 42 | 54 x 42 | — | 2G-1 p.407 | — |
|  | **R3-51d** | Part-
Time Travel on Shoulder Variable Operation | Mandatory (2G.21-01) | — | — | 66 x 84 | 66 x 84 | — | 2G-1 p.408 | — |
|  | **R3-52** | Part-Time Travel on Shoulder Ends | Mandatory (2G.21-05) | — | — | 66 x 72 | 66 x 72 | — | 2G-1 p.408 | — |
|  | **R3-52a** | TRAVEL ON SHOULDER
ENDS | Mandatory (2G.21-05) | — | — | 66 x 72 | 66 x 72 | — | 2G-1 p.408 | — |
|  | **R3-52b** | Shoulder Must Exit Advance | Mandatory (2G.21-01) | — | — | 66 x 72 | 66 x 72 | — | 2G-1 p.408 | — |
|  | **R3-52c** | MILE | Recommended (2G.21-04) | — | — | 66 x 72 | 66 x 72 | — | 2G-1 p.408 | — |
|  | **R3-56** | Begin Exit Lane | Recommended (2G.21-06) | — | — | 48 x 72 | 48 x 72 | — | 2G-1 p.408 | — |
|  | **R3-57P** | To Traffic on Shoulder (plaque) | Optional | — | — | 36 x 18 | 36 x 18 | — | 2G-1 p.408 | — |

- **[M]** 2G.21-01 (p.447) ◆ R3-51, R3-51d: Regulatory signs shall be used to notify road users of the periods of operation that travel is allowed on a paved shoulder. The Part-Time Travel on Shoulder Operation (R3-51) sign (see Figure 2G-32) shall be used where traffic is allowed to travel on the shoulder during certain fixed periods of operation. The PartTime Travel on Shoulder Variable Operation (R3-51d) sign (see Figure 2G-32) with two flashing beacons (see Chapter 4S) mounted above it shall be used when the period of operation is variable.
- **[M]** 2G.21-02 (p.447) ◆ R3-51, R3-51aP, R3-51bP, R3-51d: If certain classes of vehicles are not allowed to use the shoulder during these periods, then a Selective Exclusion (R3-51aP or R3-51bP) plaque shall be mounted below the R3-51 or R3-51d sign. If the travel on the shoulder is restricted to certain classes of vehicles, then the regulatory signs shall display that information.
- [O] 2G.21-03 (p.447) ◆ R3-51, R3-51aP, R3-51bP, R3-51cP: The EMERGENCY STOPPING ONLY OTHER TIMES (R3-51cP) plaque may be mounted below the R3-51 sign if the R3-51aP or R3-51bP plaque is not used.
- **[R]** 2G.21-04 (p.447) ◆ R3-52c: The TRAVEL ON SHOULDER BEGINS ½ MILE (R3-52c) sign should be used in advance of the location where part-time travel on shoulder first begins and followed by the DO NOT DRIVE ON SHOULDER (R4-17) sign appropriately spaced downstream.
- **[M]** 2G.21-05 (p.454) ◆ R3-52, R3-52a: Approximately ½ mile from where part-time travel on shoulder ends, the TRAVEL ON SHOULDER ENDS (R3-52a) sign shall be used. At the location provided for traffic to transition from shoulder travel back to permanent highway lane travel, an END TRAVEL ON SHOULDER (R3-52) sign shall be used. After this transition location a DO NOT DRIVE ON SHOULDER (R4-17) sign shall be used.
- **[R]** 2G.21-06 (p.454) ◆ R3-56: Where a shoulder that allows part-time travel is interrupted by a deceleration lane for an exit, the BEGIN EXIT LANE (R3-56) sign should be used at the beginning of the deceleration lane where traffic is allowed to enter during the periods that travel is prohibited on the shoulder.
- **[R]** 2G.21-07 (p.454): On a conventional road where a shoulder that is open to part-time travel becomes a mandatory turn lane, the BEGIN RIGHT TURN LANE (R3-20R) sign should be post-mounted on the right-hand side of the roadway at the upstream end of the turn lane taper of a mandatory right-turn lane. Where the shoulder is on the left-hand side of the roadway, the BEGIN LEFT TURN LANE (R3-20L) sign may be post-mounted on a median (or on the left-hand side of the roadway for a one-way street) at the upstream end of the turn lane taper of a mandatory left-turn lane.
- **[R]** 2G.21-08 (p.454): Where turn-outs are provided for emergency stopping during periods when travel is allowed on the shoulder, the EMERGENCY STOPPING ONLY (R8-7) sign (see Section 2B.52) should be used adjacent to the turn-out (see Drawing D in Figure 2G-32).
- **[R]** 2G.21-09 (p.454) ◆ R3-57P: Where traffic on an entrance ramp is required to yield to traffic using the shoulder of the freeway or expressway mainline during the periods when travel is allowed on the shoulder, the TO TRAFFIC ON SHOULDER (R3-57P) plaque should be mounted below the YIELD (R1-2) sign (see Section 2B.05 and Drawing C in Figure 2G-32).

<a id="sec-2G-22"></a>
#### Section 2G.22 Warning Signs for Part-Time Travel on a Shoulder

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **W3-9** | Traffic Using Shoulder | Recommended (2G.22-01) | — | — | 36 x 48 | 48 x 60 | — | 2G-1 p.408 | — |

- **[R]** 2G.22-01 (p.454): The Traffic Using Shoulder (W3-9) sign should be used on a ramp that enters a freeway or expressway on which part-time travel is allowed on the shoulder. When used, the W3-9 sign should be located on the right-hand side of the ramp from which the shoulder traffic approaches (see Drawing C in Figure 2G-32).
- [O] 2G.22-02 (p.454): A second W3-9 sign may be used on the left-hand side of the ramp opposite the W3-9 sign on the right-hand side of the ramp to provide greater visibility to oncoming traffic.
- [O] 2G.22-03 (p.454): The W3-9 sign may be used on a conventional road that is required to stop for or yield to the through street or highway on which part-time travel is allowed on the shoulder.

<a id="sec-2G-24"></a>
#### Section 2G.24 Lane-Use Control Signals for Part-Time Travel on a Shoulder

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Freeway | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **R3-51e** | TRAVEL ON SHOULDER ON GREEN ARROW ONLY | Optional (2G.24-06) | — | — | 66 x 84 | 66 x 84 | — | 2G-1 p.408 | — |

- [O] 2G.24-06 (p.455): The TRAVEL ON SHOULDER ON GREEN ARROW ONLY (R3-51e) sign (see Drawing A in Figure 2G-32) may be used with a lane-use control signal and may be mounted adjacent to the signal head, elsewhere on the signal support, or post-mounted next to, or in advance of, the signal.

### Chapter 2H General Information Signs

<a id="sec-2H-01"></a>
#### Section 2H.01 Scope

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **I3-5** | Airport | Optional (2H.01-02) | 24 x 24 | 30 x 30 | 2H-1 p.461 | — |
|  | **I3-6** | Bus Station | Optional (2H.01-02) | 24 x 24 | 30 x 30 | 2H-1 p.461 | — |
|  | **I3-7** | Train Station | Optional (2H.01-02) | 24 x 24 | 30 x 30 | 2H-1 p.461 | — |
|  | **I3-8** | Light Rail Transit Station | Optional (2H.01-02) | 24 x 24 | — | 2H-1 p.461 | — |
|  | **I3-9** | Vehicle Ferry Terminal | Optional (2H.01-02) | 24 x 24 | 30 x 30 | 2H-1 p.461 | — |
|  | **I3-10** | Passenger Only Ferry Terminal | Optional (2H.01-02) | 24 x 24 | 30 x 30 | 2H-1 p.461 | — |
|  | **I3-10P** | Ferry (plaque) | Optional (2H.01-02) | 24 x 12 | 30 x 18 | 2H-1 p.461 | — |
|  | **I4-1** | Library | Optional (2H.01-02) | 24 x 24 | — | 2H-1 p.461 | — |
|  | **I4-2** | Recycling Center | Optional (2H.01-02) | 30 x 36 | — | 2H-1 p.461 | — |

- [O] 2H.01-02 (p.459): A General Information (I3-5 through I4-2) symbol sign (see Figure 2H-1) may be used to provide direction to a transportation (I3 series signs) or other (I4 series signs) facility. The symbol sign may be supplemented by an educational plaque where necessary. The name of the facility may be used, if needed, to distinguish between similar facilities in the same area.
- [O] 2H.01-04 (p.459) ◆ I4-2: The Recycling Center (I4-2) symbol sign may be used to direct road users to recycling centers.
- [O] 2H.01-06 (p.459) ◆ I3-10, I3-10P: The Passengers Only Ferry Terminal (I3-10) symbol sign may be used with the FERRY (I3-10P) plaque (see Figure 2H-1) mounted below it in a directional assembly to direct road users to passenger-only ferry terminals.

*Also governed by Section 8B.26:*

- [O] 8B.26-01 (p.1007) ◆ I3-8: The Light Rail Transit Station (I3-8) sign (see Section 2H.01) may be used to direct road users to an LRT station or boarding location. It may be supplemented by the name of the transit system and by arrows as provided in Section 2D.08.

<a id="sec-2H-04"></a>
#### Section 2H.04 Traffc Signal Speed Sign (I1i -1)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **I1-1** | Traffic Signal Speed | Optional (2H.04-01) | 24 x 36 | — | 2H-1 p.461 | — |

- [O] 2H.04-01 (p.460): The Traffic Signal Speed (I1-1) sign (see Figure 2H-1) displaying the legend SIGNALS SET FOR XX MPH may be used to indicate a section of street or highway on which the traffic control signals are coordinated into a progressive system timed for a specified speed at all hours during which they are operated in a coordinated mode.

<a id="sec-2H-05"></a>
#### Section 2H.05 Jurisdictional Boundary Signs (I2-1)

| Sign | Code | Name | Default class | Size table | Also sized in |
|---|---|---|---|---|---|
|  | **I2-1** | Jurisdictional Boundary Signs | Optional (2H.05-01) | text | — |

- [O] 2H.05-01 (p.462): The Jurisdictional Boundary (I2-1) sign may be used to mark the location of the jurisdictional boundary of a State, county, or municipality or the limits of an unincorporated municipal-level community, Tribal Nation, or governmental district where legal jurisdiction, road maintenance responsibility, or emergency response obligation changes.
- **[R]** 2H.05-02 (p.462): If used, the Jurisdictional Boundary sign should be located at or as near as practicable to the jurisdictional boundary without interfering with higher-priority traffic control devices. Notices of statutes or local ordinances should be located separately using regulatory signs (see Chapter 2B).
- **[R]** 2H.05-03 (p.462): If used for an unincorporated community, the community should be one that is readily identifiable on official maps and be consistent with postal mailing addresses.
- **[M]** 2H.05-04 (p.462): In accordance with Section 2H.01, the Jurisdictional Boundary sign shall be rectangular in shape and shall have a white legend on a green background. The sign shall display only the name of the State, county, municipality, Tribal Nation, or other identifiable community, and an appropriate legend such as ENTERING, STATE LINE, County, or the municipal classification.
- **[M]** 2H.05-05 (p.462): Names of elected officials or promotional messages, such as notable accomplishments or claims, shall not be displayed on a Jurisdictional Boundary sign or added as a supplemental sign or plaque.
- [O] 2H.05-06 (p.462): A pictograph representing the jurisdiction may be displayed on the Jurisdictional Boundary sign.
- **[M]** 2H.05-07 (p.462): If a pictograph is displayed on the Jurisdictional Boundary sign, it shall be the official seal of the jurisdiction and shall comply with the provisions of Section 2A.04. The pictograph shall be placed to the left of the legend. The height of the pictograph shall not exceed 2 times the height of the initial upper-case letter of the principal legend.
- **[R]** 2H.05-08 (p.462): Signs should not be used to identify the boundaries of special-purpose governmental districts, such as school districts, sanitary districts, or improvement districts, as such signs are generally promotional in nature and do not provide navigational or orientation assistance in conjunction with official maps that are available to the general public.

<a id="sec-2H-06"></a>
#### Section 2H.06 Geographical Feature Signs (I2-2)

| Sign | Code | Name | Default class | Conventional | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **I2-2** | Geographical Feature | Optional (2H.06-01) | Varies x 36** | 2H-1 p.461 | — |

- [O] 2H.06-01 (p.462): The Geographical Feature (I2-2) sign may be used to mark the locations of land features such as river or stream crossings, and summits, that are identifiable on maps or serve as landmarks in providing navigational orientation or reference to the road user.
- **[R]** 2H.06-02 (p.462): If used, the Geographical Feature sign should display only the name of the geographical feature. Additional information that is unnecessary for navigational or orientation purposes, such as watershed or tributary names, should not be displayed on the sign.

<a id="sec-2H-08"></a>
#### Section 2H.08 Future Interstate Corridor Signs (I2-4 and I2-4a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **I2-4** | Future Interstate Corridor | Optional (2H.08-01) | 54 x 36 | 72 x 48 | 2H-1 p.461 | — |
|  | **I2-4a** | Future I-XX Corridor | Optional (2H.08-01) | 48 x 36 | 66 x 48 | 2H-1 p.461 | — |

- [O] 2H.08-01 (p.463): The Future Interstate Corridor (I2-4 and I2-4a) signs (see Figure 2H-2) may be used sparingly along an existing route that will be reconstructed as an Interstate route or along an existing route adjacent to a corridor through which an Interstate route will be constructed, in accordance with the Policy and Conditions stated in 23 CFR 470, Appendix C.
- [O] 2H.08-02 (p.463): Where the route number has been approved by the FHWA, either the I2-4 or I2-4a sign may be used.
- **[M]** 2H.08-03 (p.463) ◆ I2-4a: The I2-4a sign shall not be used where the route number has not been approved by the FHWA. 04 Future Interstate Corridor signs shall not be located where they could interfere with or detract from other traffic control devices. If used, Future Interstate Corridor signs shall be installed as independent, post-mounted sign assemblies.
- **[M]** 2H.08-05 (p.463): Future Interstate Corridor signs shall not imply that an existing route has already been designated and marked as an Interstate route. Signs indicating that an existing route is designated as a future Interstate route or corridor shall not provide directional or distance information. Route Sign assemblies (see Section 2D.29) of any type shall not be used to sign a route as a future Interstate or other route. The Interstate route marker or likeness thereof shall not be displayed on the Future Interstate Corridor signs.
- **[R]** 2H.08-06 (p.464): Future Interstate Corridor signs should be limited to strategic locations, such as at the beginning of the designated route or corridor, or beyond interchanges connecting from existing Interstate highways.

<a id="sec-2H-09"></a>
#### Section 2H.09 Project Information Sign (I2-5)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **I2-5** | Project Information | Optional | 96 x 48 | 156 x 72 | 2H-1 p.461 | — |

- [S] 2H.09-01 (p.464): The Project Information (I2-5) sign (see Figure 2H-3) provides limited information to road users about a highway construction project on which work is imminently forthcoming or ongoing.
- **[M]** 2H.09-02 (p.464): The Project Information sign legend shall be limited to the following project information: A. The roadway name or route number, B. A brief description or title of the project, C. The completion date expressed in either a month or season (Spring, Summer, Fall, or Winter), and D. The agency name.
- [O] 2H.09-03 (p.464): Project Information signs installed more than one week prior to commencement of work may include a start date.
- **[M]** 2H.09-04 (p.464): Project Information signs shall not be installed more than one month prior to the commencement of work. When installing Project Information signs prior to the commencement of work, the jurisdiction shall have a policy on when the Project Information signs are to be installed. Project Information signs shall be removed at the conclusion of work on the project, even if the final inspection or project closeout has not yet occurred.
- **[M]** 2H.09-05 (p.464): The number of Project Information signs shall be limited to one per direction of travel on the roadway on which the project is based. The location of the Project Information sign shall not interfere with the temporary traffic control zone devices.
- **[M]** 2H.09-06 (p.464): The Project Information sign shall have a white legend on a green background and shall not display Internet addresses, e-mail addresses, or telephone numbers (see Section 2A.04).

<a id="sec-2H-10"></a>
#### Section 2H.10 Grade-Separated Roadway Identifcation Signs (I2i -3 and I2-3a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **I2-3** | Grade Separation Identification | Optional (2H.10-01) | — | Varies x 18 | 2H-1 p.461 | — |
|  | **I2-3a** | Grade Separation Identification (2 lines) | Optional (2H.10-01) | — | Varies x 24 | 2H-1 p.461 | — |

- [O] 2H.10-01 (p.464): The Grade-Separated Roadway Identification (I2-3 and I2-3a) signs (see Figure 2H-4) may be used to identify a grade separation of another highway or other transportation facility such as a railway, bikeway, or pathway.
- **[R]** 2H.10-02 (p.464) ◆ I2-3: Except as provided in Paragraph 4 of this Section, when used to identify an overcrossing structure, the I2-3 sign should be mounted above the travel lanes or shoulder of the highway below.
- **[R]** 2H.10-03 (p.464): When used to identify an undercrossing structure, the I2-3 or I2-3a sign should be post-mounted in advance of the structure as near to it as practicable.
- [O] 2H.10-04 (p.464): When used to identify an overcrossing structure, the I2-3 or I2-3a sign may be post-mounted in front of an overcrossing or may be mounted to the abutment of the overcrossing facing approaching traffic.

<a id="sec-2H-11"></a>
#### Section 2H.11 Reference Location Signs (D10-1 through D10-3) and Intermediate Reference Location Signs (D10-1a through D10-3a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D10-1](symbols/D10-1.png) | **D10-1** | Reference Location (1 digit) | Optional (2H.11-03) | 10 x 18 | 12 x 24 | 2H-1 p.461 | 9A-1 |
| ![D10-1a](symbols/D10-1a.png) | **D10-1a** | Intermediate Reference Location (2 digits) | Optional (2H.11-03) | 10 x 27 | 12 x 36 | 2H-1 p.461 | 9A-1 |
| ![D10-2](symbols/D10-2.png) | **D10-2** | Reference Location (2 digits) | Optional (2H.11-03) | 10 x 27 | 12 x 36 | 2H-1 p.461 | 9A-1 |
| ![D10-2a](symbols/D10-2a.png) | **D10-2a** | Intermediate Reference Location (3 digits) | Optional (2H.11-03) | 10 x 36 | 12 x 48 | 2H-1 p.461 | 9A-1 |
| ![D10-3](symbols/D10-3.png) | **D10-3** | Reference Location (3 digits) | Optional (2H.11-03) | 10 x 36 | 12 x 48 | 2H-1 p.461 | 9A-1 |
| ![D10-3a](symbols/D10-3a.png) | **D10-3a** | Intermediate Reference Location (4 digits) | Optional (2H.11-03) | 10 x 48 | 12 x 60 | 2H-1 p.461 | 9A-1 |

- [S] 2H.11-01 (p.466): There are two types of reference location signs: A. Reference Location (D10-1 through D10-3) signs (see Figure 2H-5) show an integer distance point along a highway, and B. Intermediate Reference Location (D10-1a through D10-3a) signs (see Figure 2H-6) show the same information as Reference Location signs, but they also show a tenth-of-a-mile decimal so that they can be installed between integer distance points along a highway.
- **[M]** 2H.11-02 (p.466): Except when Enhanced Reference Location signs (see Section 2H.12) are used instead, Reference Location (D10-1 through D10-3) signs shall be placed on all expressway facilities that are located on a route where there is reference location sign continuity and on all freeway facilities to assist road users in estimating their progress, to provide a means for identifying the location of emergency incidents and traffic crashes, and to aid in highway maintenance and servicing.
- [O] 2H.11-03 (p.466): Reference Location (D10-1 through D10-3) signs may be installed along any section of a highway route or ramp to assist road users in estimating their progress, to provide a means for identifying the location of emergency incidents and traffic crashes, and to aid in highway maintenance and servicing.
- [O] 2H.11-04 (p.466): To augment the Reference Location sign system, Intermediate Reference Location (D10-1a through D10-3a) signs, which show the tenth of a mile with a decimal point, may be installed at one tenth of a mile, two tenths of a mile, or one-half mile intervals.
- **[M]** 2H.11-05 (p.466): When Intermediate Reference Location (D10-1a through D10-3a) signs are used to augment the reference location sign system, the reference location sign at the integer mile point shall display a decimal point and a zero numeral.
- **[M]** 2H.11-06 (p.466): Reference Location and Intermediate Reference Location signs shall have a minimum mounting height of 4 feet, measured vertically from the bottom of the sign to the elevation of the near edge of the roadway, and shall not be governed by the mounting height requirements prescribed in Section 2A.15.
- **[M]** 2H.11-07 (p.466): The distance numbering shall be continuous for each route within a State, except where overlaps occur (see Section 2E.22). Where routes overlap, reference location sign continuity shall be established for only one of the routes. If one of the overlapping routes is an Interstate route, that route shall be selected for continuity of distance numbering.
- **[M]** 2H.11-08 (p.466): The route selected for continuity of distance numbering shall also have continuity in interchange exit numbering (see Section 2E.22).
- **[R]** 2H.11-09 (p.467): On a route without continuity of distance numbering, the first reference location sign beyond the overlap should indicate the total distance traveled on the route (including on the portion that did not have continuity of distance numbering) so that road users will have a means of correlating their travel distance between reference location signs with that shown on their odometer.
- **[M]** 2H.11-10 (p.467): For divided highways, the distance measurement shall be made on the northbound and eastbound roadways. The reference location signs for southbound or westbound roadways shall be set at locations directly opposite the reference location signs for the northbound or eastbound roadways.
- **[M]** 2H.11-11 (p.467): Zero distance shall begin at the south and west State lines, or at the south and west terminus points where routes begin within a State.
- **[M]** 2H.11-12 (p.467): Except as provided in Paragraph 13 of this Section, reference location signs shall be installed on the right-hand side of the roadway.
- [O] 2H.11-13 (p.467): Where conditions limit or restrict the use of reference location signs on the right-hand side of the roadway, they may be installed in the median. On two-lane conventional roadways, reference location signs may be installed on one side of the roadway only and may be installed back-to-back. Reference location signs may be placed up to 30 feet from the edge of the pavement.
- [O] 2H.11-14 (p.467): If a reference location sign cannot be installed in the correct location, it may be moved in either direction as much as 50 feet.
- **[R]** 2H.11-15 (p.467): If a reference location sign cannot be placed within 50 feet of the correct location, it should be omitted. Section 2H.12 Enhanced Reference Location Signs (D10-4) and Intermediate Enhanced Reference Location Signs (D10-5)

*Also governed by Section 9D.10:*

- [S] 9D.10-01 (p.1080): There are two types of reference location signs: A. Reference Location (D10-1, D10-2, and D10-3) signs (see Figure 9D-1) show an integer distance point along a shared-use path; and B. Intermediate Reference Location (D10-1a, D10-2a, and D10-3a) signs (see Figure 9D-1) show the same information as Reference Locations signs, but they also show a tenth-of-a-mile decimal so that they can be installed between integer distance points along a shared-use path.
- [O] 9D.10-02 (p.1080): Reference Location (D10-1 through D10-3) signs may be installed along any section of a shared-use path to assist users in estimating their progress, to provide a means for identifying the location of emergency incidents and crashes, and to aid in maintenance and servicing.
- [O] 9D.10-03 (p.1080) ◆ D10-1a, D10-3a: To augment the reference location sign system, Intermediate Reference Location (D10-1a to D10-3a) signs, which show the tenth of a mile with a decimal point, may be installed at one-tenth-of-a-mile intervals, or at some other regular spacing.
- **[R]** 9D.10-04 (p.1080): If Intermediate Reference Location (D10-1a through D10-3a) signs are used to augment the reference location sign system, the Reference Location sign at the integer mile point should display a decimal point and a zero numeral.
- **[R]** 9D.10-05 (p.1080): Reference location signs for shared-use paths should have a minimum mounting height of 2 feet, measured vertically from the bottom of the sign to the elevation of the near edge of the shared-use path, and should not be governed by the mounting height requirements prescribed in Section 9A.02.
- [O] 9D.10-06 (p.1081): Reference location signs may be installed on one side of the shared-use path only and may be installed back-to-back.
- [O] 9D.10-07 (p.1081): If a reference location sign cannot be installed in the correct location, it may be moved in either direction as much as 50 feet.
- **[R]** 9D.10-08 (p.1081): If a reference location sign cannot be placed within 50 feet of the correct location, it should be omitted.
- **[R]** 9D.10-09 (p.1081): Zero distance should begin at the south and west terminus points of shared-use paths.

<a id="sec-2H-12"></a>
#### Section 2H.12 Enhanced Reference Location Signs (D10-4) and Intermediate Enhanced Reference

| Sign | Code | Name | Default class | Conventional | Size table | Also sized in |
|---|---|---|---|---|---|---|
|  | **D10-4** | Enhanced Reference Location | Optional (2H.12-03) | 18 x 54 | 2H-1 p.461 | — |
|  | **D10-5** | Intermediate Enhanced Reference Location | Optional (2H.12-03) | 18 x 60 | 2H-1 p.461 | — |

- [O] 2H.12-02 (p.467) ◆ D10-4: An Enhanced Reference Location (D10-4) sign, which enhances the reference location sign system by identifying the route, may be placed on freeways or expressways (instead of reference location signs) or on conventional roads.
- [O] 2H.12-03 (p.467) ◆ D10-5: To augment an enhanced reference location sign system, an Intermediate Enhanced Reference Location (D10-5) sign, which shows the tenth of a mile with a decimal point, may be installed along any section of a highway route or ramp at one tenth of a mile, two tenths of a mile, or one-half mile intervals.
- **[M]** 2H.12-04 (p.467) ◆ D10-5: When an Intermediate Enhanced Reference Location (D10-5) sign is used to augment the reference location sign system, the Enhanced Reference Location sign at the integer mile point shall display a decimal point and a zero numeral.
- **[M]** 2H.12-05 (p.467): Except as provided in Paragraph 6 of this Section, if enhanced reference location signs are used, they shall be vertical signs having a green background with a white legend and border, except for the route

<a id="sec-2H-13"></a>
#### Section 2H.13 Acknowledgment Signs and Plaques (I20 Series)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **I20-1** | Acknowledgment | Optional (2H.13-07) | 36 x 30* | 72 x 48* | 2H-1 p.461 | — |
|  | **I20-2** | Acknowledgment | Optional (2H.13-07) | 36 x 30* | 72 x 48* | 2H-1 p.461 | — |
|  | **I20-3** | Acknowledgment | Optional (2H.13-07) | 42 x 24* | 96 x 36* | 2H-1 p.461 | — |
|  | **I20-4** | Acknowledgment - Rest Area | Optional (2H.13-07) | 56 x 36* | 72 x 48* | 2H-1 p.461 | — |
|  | **I20-4a** | Acknowledgment - Welcome Center | Optional (2H.13-07) | 56 x 36* | 72 x 48* | 2H-1 p.461 | — |
|  | **I20-5P** | Acknowledgment Signs and Plaques (I20 Series) | Optional (2H.13-07) | — | — | text | — |

- **[R]** 2H.13-02 (p.468): A State or local highway agency that elects to have a sponsorship acknowledgement program should develop a policy on Acknowledgment signs and plaques. The policy should require that eligible sponsoring organizations comply with State laws prohibiting discrimination based on race, religion, color, age, sex, national origin, and other applicable laws.
- **[M]** 2H.13-03 (p.469): The State or local acknowledgment sign policy shall include all of the provisions regarding placement and design of Acknowledgment signs and plaques that are contained in this Section.
- **[M]** 2H.13-04 (p.469): Because regulatory, warning, and guide signs have a higher priority, Acknowledgment signs shall only be installed where adequate spacing is available between the Acknowledgment sign and other higher priority signs. Acknowledgment signs shall not be installed in a position where they would obscure the road users’ view of other traffic control devices.
- **[M]** 2H.13-05 (p.469): Acknowledgment signs shall not be installed at any of the following locations: A. On the front or back of, adjacent to, or around any other traffic control device, including traffic signs, highway traffic signals, and changeable message signs; B. On the front or back of, adjacent to, or around the supports or structures of other traffic control devices, or bridge piers; or C. At key decision points where a road user’s attention is more appropriately focused on other traffic control devices, roadway geometry, or traffic conditions, including exit and entrance ramps, merging or weaving areas, lane terminations, intersections, grade crossings, toll plazas, temporary traffic control zones, and areas of limited sight distance.
- **[M]** 2H.13-06 (p.469): Acknowledgment signs and plaques shall have a white legend and border on a blue background. Acknowledgment signs shall be independent post-mounted roadside installations only and shall not be mounted overhead.
- [O] 2H.13-07 (p.469): An Acknowledgment sign may be used to acknowledge the sponsor of a rest area or welcome center.
- **[M]** 2H.13-08 (p.469) ◆ I20-4, I20-4a: Acknowledgment signs for a rest area, when located on the highway mainline, shall be limited to one sign per direction of travel from which the rest area is accessible, shall be located at least 500 feet from other traffic control devices, and shall not display names or representations of specific products or services provided by the sponsor within the rest area. Acknowledgment signs for rest areas shall display the legend REST AREA as the program activity, such as REST AREA SPONSORED BY. In accordance with Paragraph 5 of this Section, the Rest Area and Welcome Center Acknowledgment (I20-4 and I20-4a) signs shall not be combined in the same sign assembly with or substitute for the Rest Area General Service guide signs (see Section 2I.05).
- [O] 2H.13-09 (p.469): An additional Acknowledgment sign may be used within the rest area provided that it is not visible from the highway mainline or ramps to and from the rest area.
- [O] 2H.13-10 (p.469): If a State has officially adopted and is actively promoting a program to encourage the use of safety rest areas through the use of a program name, then that program name may be displayed in smaller lettering below the legend REST AREA on the Rest Area Acknowledgment sign.
- **[M]** 2H.13-11 (p.469): Program names or slogans, as described in Paragraph 14 of this Section, shall not be displayed on the Rest Area General Service guide signs or other types of traffic signs.
- **[R]** 2H.13-12 (p.469): The minimum spacing between Acknowledgment signs and any other traffic control signs, except parking regulation signs, should be: A. 150 feet on roadways with speed limits of less than 30 mph, B. 200 feet on roadways with speed limits of 30 to 45 mph, and C. 500 feet on roadways with speed limits greater than 45 mph.
- **[R]** 2H.13-13 (p.469): If the placement of a newly-installed higher-priority traffic control device, such as a higher-priority sign, a highway traffic signal, or a temporary traffic control device, conflicts with an existing Acknowledgment sign, the Acknowledgment sign should be relocated, covered, or removed.
- [O] 2H.13-14 (p.469): State or local highway agencies may use their own pictograph (see definition in Section 1C.02) and/or a brief jurisdiction-wide program name, such as “Adopt-A-Highway” or “Litter Removal,” as part of any portion of the Acknowledgment sign, provided that the signs comply with the provisions for shape, sign and legend size, color, and lettering style in this Chapter and in Chapter 2A.
- **[R]** 2H.13-15 (p.469): Acknowledgment signs should clearly indicate the type of highway services provided by the sponsor.
- **[M]** 2H.13-16 (p.470): In addition to the general provisions for signs described in Chapter 2A and the sign design principles covered in the “Standard Highway Signs” publication (see Section 1A.05), Acknowledgment sign and plaque designs developed by State or local highway agencies shall comply with the following provisions: A. Neither the sign or plaque design nor the sponsor acknowledgment name or logo shall contain any contact information, directions, slogans (other than a brief jurisdiction-wide program name, if used), telephone numbers, e-mail or Internet addresses, including domain names and uniform resource locators (URLs), metadata tags (“hash-tags”), or quick-response (QR) codes, bar codes, or similar scanning graphics (see Section 2A.04); B. Except for the sponsor acknowledgment logo, all of the lettering shall be in upper-case letters of the Standard Alphabets as provided in the “Standard Highway Signs” publication (see Section 1A.05); C. If a logo, instead of a word legend, is used to represent the sponsor, the logo shall be the primary logo that identifies the sponsoring entity. Secondary or alternate logos, slogans, products, mascots, spokespersons, or other items associated with the sponsoring entity’s commercial advertising or marketing shall not be displayed on Acknowledgment signs or plaques; D. In order to keep the main focus on the highway-related service and not on the sponsor acknowledgment name or logo, the area reserved for the sponsor acknowledgment name or logo shall not be located at the top of the sign or plaque, shall be a maximum of 8 square feet in area, and shall not exceed ¹⁄³ of the total area of the sign; E. The entire sign display area of an Acknowledgment sign assembly shall not exceed 24 square feet; F. The sign or plaque shall not contain any messages, lights, symbols, or logos that resemble any official traffic control devices; G. The sign or plaque shall not contain any external or internal illumination, light-emitting diodes, luminous tubing, fiber optics, luminescent panels, or other flashing, moving, or animated features; H. The sign or plaque shall not distract from official traffic control messages such as regulatory, warning, or guidance messages; I. The area of the plaque shall not exceed the lesser of ¹⁄³ the area of the General Service sign below which it is mounted or 24 square feet; J. The plaque size shall be based on the standard sizes as specified in Table 2H-1. If the size of the General Service sign is oversized for its application (greater than the size specified for the corresponding roadway application in Table 2H-1), or if the size of the General Service sign increases due to modification of the sign legend, a corresponding increase in the size of the plaque shall not be allowed; and K. The sign or plaque shall not display promotional or contact information about the agency’s sponsorship program, including if the sign or plaque does not currently display a sponsor.
- [O] 2H.13-17 (p.470): If a specific outlet of a business with multiple locations in the same area is the sponsoring entity, such as a franchisee, the area reserved for the sponsor acknowledgment name or logo may include the name of the municipality or neighborhood in which the sponsoring entity is located.
- [O] 2H.13-18 (p.470): An Acknowledgment plaque may be mounted below the following General Service signs to acknowledge the sponsor of a corridor-based or region-based highway-related service: A. Radio-Weather Information (D12-1) sign (see Section 2I.09); B. Radio-Traffic Information (D12-1a) sign (see Section 2I.09); C. TRAVEL INFO CALL 511 (D12-5 and D12-5a) signs (see Section 2I.12); and D. Roadside Assistance (D12-6) sign (see Section 2I.13).
- **[M]** 2H.13-19 (p.470): An Acknowledgment plaque shall not be mounted in conjunction with any other sign or traffic control device. An Acknowledgment plaque shall not be used alone or without one of the General Service signs specified in Paragraph 18 of this Section.
- **[M]** 2H.13-20 (p.470): The general restrictions on the type of content allowed for display on Acknowledgment signs (see Paragraph 16 of this Section) shall apply to the legends of Acknowledgment plaques.

<a id="sec-2H-14"></a>
#### Section 2H.14 Alternative Fuels Corridor Sign (D9-19)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **D9-17a** | Next EV Charging | Recommended (2J.06-05) | — | — | text | — |
|  | **D9-19** | Alternative Fuels Corridor | Optional (2H.14-01) | 24 x 24 | 36 x 36 | 2H-1 p.461 | — |
|  | **D9-19aP** | Alternative Fuels Corridor (1 line) (plaque) | Recommended (2H.14-17) | 30 x 9 | 42 x 12 | 2H-1 p.461 | — |
|  | **D9-19bP** | Alternative Fuels Corridor (2 lines) (plaque) | Recommended (2H.14-17) | 30 x 12 | 42 x 18 | 2H-1 p.461 | — |
|  | **W16-19P** | Last In Corridor (plaque) | Optional | 24 x 18 | 24 x 18 | 2H-1 p.461 | — |

- [O] 2H.14-01 (p.471) ◆ D9-19: The Alternative Fuels Corridor (D9-19) sign (see Figure 2H-9) may be used to inform motorists of an alternative fuels corridor highway segment that has been designated by the Secretary of Transportation as “Corridor Ready.”
- **[M]** 2H.14-02 (p.471): Alternative Fuels Corridor signs shall only be used to designate alternative fuels corridor highway segments that have been designated by the Federal Highway Administration as “Corridor Ready.” The appropriate General Service signs or plaques identifying the alternative fuels available in the corridor shall be included with the Alternative Fuels Corridor sign in a sign assembly. The alternative fuel services for an alternative fuels corridor shall be limited to electric vehicle charging, compressed natural gas, liquid natural gas, liquified petroleum, and hydrogen.
- **[M]** 2H.14-04 (p.471): Alternative Fuels Corridor signs shall only be post-mounted on the side of the road and shall not be mounted overhead.
- **[M]** 2H.14-05 (p.471): State or agency variations of the Alternative Fuels Corridor sign shall not be allowed. Acknowledgments of sponsors shall not be allowed in Alternative Fuels Corridor sign assemblies.
- **[M]** 2H.14-06 (p.471): Except as provided in Paragraph 7 of this Section, Alternative Fuels Corridor signs shall be limited to one sign at or near the beginning of the alternative fuels corridor in each direction of travel.
- [O] 2H.14-07 (p.472): For long corridors, such as segments connecting control cities or major urban areas, additional signs may be located beyond major intersections or major interchanges following the typical post-interchange sign sequence.
- [O] 2H.14-08 (p.472): The beginning of an alternative fuels corridor may be indicated with a BEGIN (M4-14P) plaque (see Figure 2H-9) with a white legend and border on a blue background mounted above the alternative fuels corridor sign in the sign assembly.
- [O] 2H.14-09 (p.472): The end of an alternative fuels corridor may be indicated with an END (M4-6P) plaque (see Figure 2H-9) with a white legend and border on a blue background mounted above the Alternative Fuels Corridor sign in the sign assembly.
- **[M]** 2H.14-10 (p.472) ◆ W16-19P: The General Service signs shall not be used in the sign assembly indicating the end of a corridor. 11 When the availability of one or more of the alternative fuel facilities discontinues in an alternative fuels corridor, the LAST IN CORRIDOR (W16-19P) plaque (see Figure 2H-9) shall be included on the last General Service directional assembly on the approach to the interchange or intersection.
- [O] 2H.14-12 (p.472): When the availability of one or more of the alternative fuel facilities discontinues in an alternative fuels corridor, an Alternative Fuels Corridor sign with accompanying General Service signs indicating the types of fuels still available in the corridor may be provided beyond the intersection or interchange where the last discontinued fuel facilities were available.
- [O] 2H.14-13 (p.472) ◆ D9-17a: When the distance between electric vehicle (EV) charging services in an alternative fuels corridor is greater than 50 miles, the Next EV Charging (D9-17a) sign (see Figure 2H-9) may be located after the EV charging directional assembly, but before the EV charging service exit or turn, to inform road users of the extended distance to the next EV charging service.
- **[M]** 2H.14-14 (p.472) ◆ D9-19: The Alternative Fuels Corridor (D9-19) sign shall not be used as a directional sign in a directional assembly, or be combined with other signs, except as provided in this Section.
- [O] 2H.14-15 (p.472): Up to three General Service symbol signs arranged horizontally displaying the alternative fuels available in the designated corridor may be installed below the Alternative Fuels Corridor sign (see Figure 2H-10).
- **[M]** 2H.14-16 (p.472): The size of the General Service symbol signs for the alternative fuels available shall not exceed 18 x 18 inches when mounted with the 24 x 24-inch Alternative Fuels Corridor sign and 24 x 24 inches when mounted with the 36 x 36-inch Alternative Fuels Corridor sign.
- **[R]** 2H.14-17 (p.472) ◆ D9-19aP, D9-19bP: When the number of eligible alternative fuels available in the corridor exceeds three, a separate plaque with the two-letter or three-letter designations (D9-19aP or D9-19bP) of each of the fuels available (see Figure 2H-9) should be used in place of the General Service symbol signs.
- **[M]** 2H.14-18 (p.472): When the Alternative Fuels Corridor sign is used in a designated corridor on a freeway or expressway, the applicable General Service signs shall be installed on the approach to an interchange in the corridor from which the designated fuel services are available. If the services are not visible from the ramp of a single-exit interchange, the service signing shall be repeated at the intersection of the exit ramp and the crossroad (see Figure 2H-10). Where the alternative fuel facility is not located along the crossroad, additional General Service directional assemblies shall be installed in advance of each subsequent turn to reach the facility (see ~~Figure 2~~ H-11).
- **[M]** 2H.14-20 (p.472): Alternative Fuels Corridor sign assemblies shall be limited to those locations where adequate spacing is available between the Alternative Fuels Corridor sign and other signs. Alternative Fuels Corridor signs shall not be installed in a location where they might distract driver’s attention from other traffic control devices or the roadway in a complex roadway environment. If the placement of a newly-installed, higherpriority traffic control device conflicts with an existing Alternative Fuels Corridor sign, the Alternative Fuels Corridor sign shall be relocated, covered, or removed.
- **[M]** 2H.14-21 (p.472): Alternative Fuels Corridor signs shall not be installed on routes other than those officially designated as alternative fuels corridors, even if to provide directional information to such corridors.

*Also governed by Section 2J.06:*

- **[R]** 2J.06-05 (p.500) ◆ D9-17a: When the distance to the next exit providing access to EV charging service is 50 miles or greater, the Next EV Charging (D9-17a) sign should be used (see Figure 2H-9). When used, the Next EV Charging sign should be located directly after the General Service sign for the fuel type displayed in the signing sequence for the exit (see Figure 2H-10).

### Chapter 2I General Service Signs

<a id="sec-2I-02"></a>
#### Section 2I.02 General Service Signs for Conventional Roads

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D9-1](symbols/D9-1.png) | **D9-1** | Telephone | Optional (2I.02-23) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-2](symbols/D9-2.png) | **D9-2** | Hospital | Optional | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-3](symbols/D9-3.png) | **D9-3** | Camping | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-4](symbols/D9-4.png) | **D9-4** | Litter Container | Optional | 24 x 30 | 36 x 48 | 2I-1 p.476 | — |
| ![D9-6](symbols/D9-6.png) | **D9-6** | International Symbol of Accessibility | Optional (2I.02-17) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-6P](symbols/D9-6P.png) | **D9-6P** | Van Accessible (plaque) | Optional | 18 x 9 | — | 2I-1 p.476 | — |
| ![D9-7](symbols/D9-7.png) | **D9-7** | Gas | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-8](symbols/D9-8.png) | **D9-8** | Food | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-9](symbols/D9-9.png) | **D9-9** | Lodging | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-10](symbols/D9-10.png) | **D9-10** | Tourist Information | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-11](symbols/D9-11.png) | **D9-11** | Diesel Fuel | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-11a](symbols/D9-11a.png) | **D9-11a** | Alternative Fuel - Compressed Natural Gas | Optional (2I.02-02) | 24 x 24*** | 30 x 30*** | 2I-1 p.476 | — |
| ![D9-11b](symbols/D9-11b.png) | **D9-11b** | Electric Vehicle Charging | Optional (2I.02-02) | 24 x 24*** | 30 x 30*** | 2I-1 p.476 | — |
| ![D9-11bP](symbols/D9-11bP.png) | **D9-11bP** | Electric Vehicle Charging (plaque) | Optional (2I.02-02) | 24 x 18 | 30 x 24 | 2I-1 p.476 | — |
|  | **D9-11c** | Alternative Fuel - Ethanol | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.476 | — |
| ![D9-11d](symbols/D9-11d.png) | **D9-11d** | Alternative Fuel - Liquefied Natural Gas | Optional (2I.02-02) | 24 x 24*** | 30 x 30*** | 2I-1 p.477 | — |
| ![D9-11e](symbols/D9-11e.png) | **D9-11e** | Alternative Fuel - Liquefied Petroleum Gas | Optional (2I.02-02) | 24 x 24*** | 30 x 30*** | 2I-1 p.477 | — |
| ![D9-11f](symbols/D9-11f.png) | **D9-11f** | Alternative Fuel - Hydrogen | Optional (2I.02-02) | 24 x 24*** | 30 x 30*** | 2I-1 p.477 | — |
| ![D9-11g](symbols/D9-11g.png) | **D9-11g** | Alternative Fuel - Biofuel | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
| ![D9-12](symbols/D9-12.png) | **D9-12** | RV Sanitary Station | Optional (2I.02-19) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
| ![D9-13](symbols/D9-13.png) | **D9-13** | Emergency Medical Services | Optional (2I.02-14) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
| ![D9-13aP](symbols/D9-13aP.png) | **D9-13aP** | Hospital (plaque) | Optional (2I.02-23) | 24 x 12 | 30 x 12 | 2I-1 p.477 | — |
| ![D9-13bP](symbols/D9-13bP.png) | **D9-13bP** | Ambulance Station (plaque) | Optional (2I.02-23) | 24 x 12 | 30 x 15 | 2I-1 p.477 | — |
| ![D9-13cP](symbols/D9-13cP.png) | **D9-13cP** | Emergency Medical Care (plaque) | Optional (2I.02-23) | 24 x 18 | 30 x 24 | 2I-1 p.477 | — |
| ![D9-13dP](symbols/D9-13dP.png) | **D9-13dP** | Trauma Center (plaque) | Optional (2I.02-23) | 24 x 12 | 30 x 15 | 2I-1 p.477 | — |
| ![D9-14](symbols/D9-14.png) | **D9-14** | Police | Optional (2I.02-23) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
|  | **D9-17P** | Next Services Advance (plaque) | Optional (2I.02-16) | 72 x 24 | 114 x 30 | 2I-1 p.477 | — |
| ![D9-20](symbols/D9-20.png) | **D9-20** | Pharmacy | Optional | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
| ![D9-20aP](symbols/D9-20aP.png) | **D9-20aP** | 24-Hour (plaque) | Optional | 24 x 12 | 30 x 12 | 2I-1 p.477 | — |
| ![D9-21](symbols/D9-21.png) | **D9-21** | Telecommunications Device for the Deaf | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
| ![D9-22](symbols/D9-22.png) | **D9-22** | Wireless Internet | Optional (2I.02-02) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |

- [O] 2I.02-02 (p.475): General Service signs (see Figure 2I-1) may be used on conventional roads where such services are infrequent and are found only on an intersecting highway or crossroad.
- **[M]** 2I.02-03 (p.475): All General Service signs and supplemental sign panels shall have a white legend and border on a blue background.
- **[R]** 2I.02-04 (p.475): General Service signs should be installed at a suitable distance in advance of the turn-off point or intersecting highway.
- **[R]** 2I.02-05 (p.475): States that elect to provide General Service signing should establish a statewide policy or warrant for its use, and criteria for the availability of services. Local jurisdictions electing to use such signing should follow State policy for the sake of uniformity.
- [O] 2I.02-06 (p.475): Individual States may sign for whatever alternative fuels are available at appropriate locations.
- **[M]** 2I.02-07 (p.475): To be eligible for an EV Charging General Service sign on a conventional road, the EV chargers provided shall meet the criteria for Direct Current Fast Chargers provided in 23 CFR 680.106 and be in continuous operation at least 16 hours per day, 7 days per week.
- **[M]** 2I.02-08 (p.475): General Service signs, if used at intersections, shall be accompanied by a directional message.
- [O] 2I.02-09 (p.475): The Advance Turn (M5 series) or Directional Arrow (M6 series) auxiliary plaques (see Figure 2I-1) with white arrows on blue backgrounds may be used with General Service symbol signs to create a General Service directional assembly.
- [O] 2I.02-10 (p.475): The General Service sign legends may be either symbols or word messages.
- **[M]** 2I.02-11 (p.475): Symbols and word message General Service legends shall not be intermixed on the same sign.
- **[M]** 2I.02-12 (p.475) ◆ D9-20, D9-20aP: The Pharmacy (D9-20) sign shall only be used to indicate the availability of a pharmacy that is open, with a State-licensed pharmacist present and on duty, 24 hours per day, 7 days per week, and that is located within 3 miles of an interchange on the Federal-aid system. The D9-20 sign shall have a 24 HR (D9-20aP) plaque mounted below it.
- **[M]** 2I.02-13 (p.475) ◆ D9-2, D9-13aP: Use of the Hospital (D9-2) sign or the HOSPITAL (D9-13aP) plaque (see Figure 2I-1) shall be limited to facilities that operate 24 hours per day, 7 days per week.
- [O] 2I.02-14 (p.475) ◆ D9-13: The Emergency Medical Services (D9-13) sign (see Figure 2I-1 and Paragraph 20 of this Section) may be used for facilities that provide emergency medical care but do not operate on a full-time basis.
- [O] 2I.02-16 (p.479) ◆ D9-17P: If the distance to the next point at which services are available is 10 miles or more, a Next Services Advance (D9-17P) plaque (see Figure 2I-2) may be installed below the General Service sign.
- [O] 2I.02-17 (p.479) ◆ D9-6: The International Symbol of Accessibility (D9-6) sign (see Figure 2I-1) may be used beneath General Service signs where paved ramps and rest room facilities accessible to, and usable by, persons with disabilities are provided.
- **[R]** 2I.02-18 (p.479) ◆ D9-6, D9-6P: When the D9-6 sign is used in accordance with Paragraph 16 of this Section, and van-accessible parking is available at the facility, a VAN ACCESSIBLE (D9-6P) plaque (see Figure 2I-1) should be mounted below the D9-6 sign.
- [O] 2I.02-19 (p.479) ◆ D9-12: The Recreational Vehicle Sanitary Station (D9-12) sign (see Figure 2I-1) may be used as needed to indicate the availability of facilities designed for the use of dumping wastes from recreational vehicle holding tanks.
- [O] 2I.02-20 (p.479) ◆ D9-4: The Litter Container (D9-4) sign (see Figure 2I-1) may be placed in advance of roadside turn-outs or rest areas, unless it distracts the driver’s attention from other more important regulatory, warning, or directional signs.
- [O] 2I.02-21 (p.479) ◆ D9-13: The Emergency Medical Services (D9-13) symbol sign (see Figure 2I-1) may be used to identify medical service facilities that have been included in the Emergency Medical Services system under a signing policy developed by the State and/or local highway agency.
- **[M]** 2I.02-22 (p.479): The Emergency Medical Services symbol sign shall not be used to identify services other than qualified hospitals, ambulance stations, and qualified free-standing emergency medical treatment centers. If used, the Emergency Medical Services symbol sign shall be supplemented by a sign or plaque, as provided in Paragraph 22 of this Section, identifying the type of service provided.
- [O] 2I.02-23 (p.479) ◆ D9-1, D9-13aP, D9-13bP, D9-13cP, D9-13dP, D9-14: The Emergency Medical Services symbol sign may be used above the HOSPITAL (D9-13aP) plaque or above a plaque with the legend AMBULANCE STATION (D9-13bP), EMERGENCY MEDICAL CARE (D9-13cP), or TRAUMA CENTER (D9-13dP). The Emergency Medical Services symbol sign may also be used to supplement Telephone (D9-1), Channel 9 Monitored (D12-3) (see Figure 2I-8), or POLICE (D9-14) signs.
- **[M]** 2I.02-24 (p.479): The legend EMERGENCY MEDICAL CARE shall not be used for services other than qualified free-standing emergency medical treatment centers.
- **[R]** 2I.02-25 (p.479): Each State should develop a policy for the implementation of the Emergency Medical Services symbol sign. 26 The State should consider the following guidelines in the preparation of its policy: A. AMBULANCE 1. 24-hour service, 7 days per week. 2. Staffed by two State-certified persons trained at least to the basic level. 3. Vehicular communications with a hospital emergency department. 4. Operator should have successfully completed an emergency-vehicle operator training course. B. HOSPITAL 1. 24-hour service, 7 days per week. 2. Emergency department facilities with a physician (or emergency care nurse on duty within the emergency department with a physician on call) trained in emergency medical procedures on duty. 3. Licensed or approved for definitive medical care by an appropriate State authority. 4. Equipped for radio voice communications with ambulances and other hospitals. C. Channel 9 Monitored 1. Provided by either professional or volunteer monitors. 2. Available 24 hours per day, 7 days per week. 3. The service should be endorsed, sponsored, or controlled by an appropriate government authority to guarantee the level of monitoring.

<a id="sec-2I-03"></a>
#### Section 2I.03 General Service Signs for Freeways and Expressways

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D9-16](symbols/D9-16.png) | **D9-16** | Truck Parking | Mandatory (2I.15-03) | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
| ![D9-16aP](symbols/D9-16aP.png) | **D9-16aP** | Truck External Power (plaque) | Optional | 24 x 24 | 30 x 30 | 2I-1 p.477 | — |
|  | **D9-18** |  | Optional | 108 x 84 | — | 2I-1 p.477 | — |
|  | **D9-18a** | General Services with Exit Number | Optional | 72 x 60 | 102 x 84** (E) | 2I-1 p.477 | — |
|  | **D9-18b** |  | Optional | 108 x 84 | — | 2I-1 p.477 | — |
|  | **D9-18c** | General Services with Action Message | Optional | 72 x 60** | 102 x 84** (E) | 2I-1 p.477 | — |
|  | **D9-18dP** | Rural Interchange General Services | Optional | — | 120 x 36 | 2I-1 p.477 | — |
|  | **D9-18eP** | Rural Interchange General Services | Optional | — | Varies x 24 | 2I-1 p.477 | — |
|  | **D9-18fP** | Rural Interchange General Services | Optional | — | Varies x 42 | 2I-1 p.477 | — |

- [S] 2I.03-01 (p.480) ◆ D9-18, D9-18a, D9-18b, D9-18c, D9-18dP, D9-18eP, D9-18fP: General Service (D9-18 series) signs (see Figure 2I-3) are generally not appropriate at major interchanges (see definition in Section 2E.11) and in urban areas.
- [O] 2I.03-20 (p.482) ◆ D9-18dP, D9-18eP, D9-18fP: At rural interchange areas where limited road user services are available and where it is unlikely that additional services will be provided within the near future, a Rural Interchange General Services (D9-18dP, D9-18eP, or D9-18fP) plaque displaying one to three services (words or symbols) may be mounted below a post-mounted Interchange Advance guide sign.
- [O] 2I.03-25 (p.482) ◆ D9-16: A separate Truck Parking (D9-16) sign (see Figure 2I-1) may be mounted below the other general road user services to direct truck drivers to designated parking areas.
- [O] 2I.03-26 (p.482) ◆ D9-16, D9-16aP: A TRUCK EXTERNAL POWER (D9-16aP) plaque (see Figure 2I-1) may be mounted below the Truck Parking (D9-16) sign to indicate the availability of receptacles providing power for electrical devices within the truck.

*Also governed by Section 2I.15:*

- [O] 2I.15-01 (p.489): General Service signs may be used to display the number of available truck parking spaces at roadside areas such as rest areas, welcome centers, and weigh stations, and at facilities off a highway that are open to the public and provide parking for commercial vehicles 24 hours per day, 7 days per week.
- **[M]** 2I.15-02 (p.489) ◆ D9-16, D9-16aP: The Truck Parking Availability General Service (D9-16b through D9-16e) signs (see Figure 2I-9) shall include a changeable message element with a white changeable legend on a black opaque background that displays only the number of parking spaces currently available at each location or the legend FULL. The upper section of the sign shall display the Truck Parking (D9-16) symbol sign and the legend SPACES OPEN. The sign shall display the number of available truck parking spaces for no more than three parking facilities. Where two lines of legend, such as the location and a distance, are displayed for a parking facility, not more than two parking facilities shall be displayed on the sign.
- **[M]** 2I.15-03 (p.489) ◆ D9-16: Where the truck parking facility is located off the main highway and is accessed from the crossroad, directional assemblies with the Truck Parking (D9-16) sign shall be installed along the ramp and along crossroads where the route to the facility requires a turn, where it is unclear as to which roadway to follow, or where additional guidance is needed.
- [O] 2I.15-05 (p.490): The word FULL in a white legend may be displayed on changeable message elements of a Truck Parking Availability General Service sign when the number of truck parking spaces available at the associated facility reaches a predetermined lower threshold.
- **[R]** 2I.15-06 (p.490): Truck Parking Availability signs should be located 3 to 5 miles in advance of the nearest parking facility. The parking facilities displayed on the sign should be no more than 60 miles from the sign location.

<a id="sec-2I-04"></a>
#### Section 2I.04 Interstate Oasis Signing (D5-12 Series)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **D5-12** | Interstate Oasis | Recommended (2I.04-03) | — | 198 x 60 (F) | 2I-1 p.476 | — |
|  | **D5-12aP** | Interstate Oasis (plaque) | Recommended (2I.04-03) | — | 114 x 48 | 2I-1 p.476 | — |
|  | **D5-12b** | Interstate Oasis Directional | Recommended (2I.04-03) | — | 48 x 36 | 2I-1 p.476 | — |

- **[R]** 2I.04-02 (p.483): If a State elects to provide or allow Interstate Oasis signing (see Figure 2I-4), there should be a statewide policy, program, procedures, and criteria for the designation and signing of a facility as an Interstate Oasis that complies with the FHWA’s policy and with the provisions of this Section.
- **[R]** 2I.04-03 (p.483) ◆ D5-12, D5-12aP: States electing to provide or allow Interstate Oasis signing should use the following signing practices on the freeway for any given exit to identify the availability of a designated Interstate Oasis: A. If adequate sign spacing allows, a separate Interstate Oasis (D5-12) sign should be installed in an effective location with spacing of at least 800 feet from other adjacent guide signs, including any Specific Service signs. This Interstate Oasis sign should be located upstream from the Advance Guide sign or between the Advance Guide sign and the Exit Direction sign for the exit leading to the Interstate Oasis. The Interstate Oasis sign should display the words INTERSTATE OASIS and the exit number or, for an unnumbered interchange, an action message such as NEXT RIGHT. B. If the spacing of the other guide signs precludes the use of a separate sign as described in Item A of this Paragraph, an INTERSTATE OASIS (D5-12aP) supplemental plaque should be mounted below an existing D9-18 series General Service sign for the interchange.
- [O] 2I.04-04 (p.483): If Specific Service signing is provided at the interchange, a business designated as an Interstate Oasis and having a business identification sign panel on the Food and/or Gas Specific Service signs may use the bottom portion of the business identification sign panel to display the word OASIS.
- [O] 2I.04-05 (p.483) ◆ D5-12: If Specific Service signing is not provided at the interchange, the name of the business designated as an Interstate Oasis may be displayed on a business identification sign panel, in compliance with the provisions of Sections 2J.03 through 2J.05, below the INTERSTATE OASIS legend on the D5-12 sign.
- **[M]** 2I.04-06 (p.484) ◆ D5-12b: If Specific Service signs containing the OASIS legend as a part of the business identification sign panel(s) are not used on the ramp and if the Interstate Oasis is not clearly visible and identifiable from the exit ramp, an Interstate Oasis Directional (D5-12b) sign shall be provided on the exit ramp to indicate the direction and distance to the Interstate Oasis.
- **[M]** 2I.04-07 (p.484): If needed, additional trailblazer guide signs shall be used along the crossroad to guide road users to an Interstate Oasis.

<a id="sec-2I-05"></a>
#### Section 2I.05 Rest Area and Other Roadside Area Signs (D5-1 through D5-11 Series)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D5-1](symbols/D5-1.png) | **D5-1** | Rest Area Advance | Mandatory (2I.05-02) | 78 x 36* | 132 x 60* (F) | 2I-1 p.476 | — |
| ![D5-1a](symbols/D5-1a.png) | **D5-1a** | Rest Area Advance Direction | Mandatory (2I.05-02) | 78 x 36* | 132 x 60* (F) | 2I-1 p.476 | — |
| ![D5-2](symbols/D5-2.png) | **D5-2** | Rest Area Entrance Direction | Mandatory (2I.05-02) | 78 x 36* | 132 x 66* (F) | 2I-1 p.476 | — |
| ![D5-2a](symbols/D5-2a.png) | **D5-2a** | Rest Area Gore | Mandatory (2I.05-02) | 42 x 48* | 78 x 78* (F) | 2I-1 p.476 | — |
| ![D5-5](symbols/D5-5.png) | **D5-5** | Rest Area Directional | Mandatory (2I.05-02) | 42 x 48* | — | 2I-1 p.476 | — |
| ![D5-6](symbols/D5-6.png) | **D5-6** | Next Rest Area | Mandatory (2I.05-02) | 78 x 54* | 132 x 78* (F) | 2I-1 p.476 | — |
| ![D5-9](symbols/D5-9.png) | **D5-9** | Parking Area Advance | Mandatory (2I.05-02) | 96 x 36* | 162 x 60* (F) | 2I-1 p.476 | — |
| ![D5-9a](symbols/D5-9a.png) | **D5-9a** | Parking Area Entrance Direction | Mandatory (2I.05-02) | 96 x 36* | 162 x 60* (F) | 2I-1 p.476 | — |
| ![D5-9b](symbols/D5-9b.png) | **D5-9b** | Parking Area Gore | Mandatory (2I.05-02) | 62 x 48* | 108 x 78* (F) | 2I-1 p.476 | — |
| ![D5-10](symbols/D5-10.png) | **D5-10** | Picnic Area (Roadside Table, Roadside | Mandatory (2I.05-02) | 84 x 36* | 144 x 60* (F) | 2I-1 p.476 | — |
| ![D5-10a](symbols/D5-10a.png) | **D5-10a** | Picnic Area (Roadside Table, Roadside | Mandatory (2I.05-02) | 84 x 36* | 144 x 60* (F) | 2I-1 p.476 | — |
| ![D5-10b](symbols/D5-10b.png) | **D5-10b** | Picnic Area (Roadside Table, Roadside | Mandatory (2I.05-02) | 54 x 48* | 92 x 78* (F) | 2I-1 p.476 | — |
| ![D5-11](symbols/D5-11.png) | **D5-11** | Scenic Area (Scenic View, Scenic | Mandatory (2I.05-02) | 84 x 36* | 144 x 60* (F) | 2I-1 p.476 | — |
| ![D5-11a](symbols/D5-11a.png) | **D5-11a** | Scenic Area (Scenic View, Scenic | Mandatory (2I.05-02) | 84 x 36* | 144 x 60* (F) | 2I-1 p.476 | — |
| ![D5-11b](symbols/D5-11b.png) | **D5-11b** | Overlook) Gore | Mandatory (2I.05-02) | 54 x 48* | 76 x 66* (E) | 2I-1 p.476 | — |

*Also governed by Section 2I.04:*

- **[R]** 2I.04-02 (p.483): If a State elects to provide or allow Interstate Oasis signing (see Figure 2I-4), there should be a statewide policy, program, procedures, and criteria for the designation and signing of a facility as an Interstate Oasis that complies with the FHWA’s policy and with the provisions of this Section.
- **[R]** 2I.04-03 (p.483): States electing to provide or allow Interstate Oasis signing should use the following signing practices on the freeway for any given exit to identify the availability of a designated Interstate Oasis: A. If adequate sign spacing allows, a separate Interstate Oasis (D5-12) sign should be installed in an effective location with spacing of at least 800 feet from other adjacent guide signs, including any Specific Service signs. This Interstate Oasis sign should be located upstream from the Advance Guide sign or between the Advance Guide sign and the Exit Direction sign for the exit leading to the Interstate Oasis. The Interstate Oasis sign should display the words INTERSTATE OASIS and the exit number or, for an unnumbered interchange, an action message such as NEXT RIGHT. B. If the spacing of the other guide signs precludes the use of a separate sign as described in Item A of this Paragraph, an INTERSTATE OASIS (D5-12aP) supplemental plaque should be mounted below an existing D9-18 series General Service sign for the interchange.
- [O] 2I.04-04 (p.483): If Specific Service signing is provided at the interchange, a business designated as an Interstate Oasis and having a business identification sign panel on the Food and/or Gas Specific Service signs may use the bottom portion of the business identification sign panel to display the word OASIS.
- [O] 2I.04-05 (p.483): If Specific Service signing is not provided at the interchange, the name of the business designated as an Interstate Oasis may be displayed on a business identification sign panel, in compliance with the provisions of Sections 2J.03 through 2J.05, below the INTERSTATE OASIS legend on the D5-12 sign.
- **[M]** 2I.04-06 (p.484): If Specific Service signs containing the OASIS legend as a part of the business identification sign panel(s) are not used on the ramp and if the Interstate Oasis is not clearly visible and identifiable from the exit ramp, an Interstate Oasis Directional (D5-12b) sign shall be provided on the exit ramp to indicate the direction and distance to the Interstate Oasis.
- **[M]** 2I.04-07 (p.484): If needed, additional trailblazer guide signs shall be used along the crossroad to guide road users to an Interstate Oasis.

- **[M]** 2I.05-01 (p.484): Rest Area signs (see Figure 2I-5) shall have a retroreflective white legend and border on a blue background.
- **[M]** 2I.05-02 (p.484): Signs that include the legend REST AREA shall be used only where parking and restroom facilities are available.
- **[R]** 2I.05-03 (p.484) ◆ D5-1, D5-1a, D5-9, D5-9a, D5-9b, D5-10, D5-10a, D5-10b: A roadside area that does not contain restroom facilities should be signed to indicate the major road user service that is provided. For example, the sign legends for an area with only parking should use the words PARKING AREA (D5-9 series) instead of REST AREA. The sign legends for an area with only picnic tables and parking should use words such as PICNIC AREA, ROADSIDE TABLE, or ROADSIDE PARK (D5-10 series) instead of REST AREA.
- **[R]** 2I.05-04 (p.484): Rest areas that have tourist information and welcome centers should be signed as provided in Section 2I.08.
- **[R]** 2I.05-05 (p.484) ◆ D5-1, D5-1a, D5-11, D5-11a, D5-11b: Scenic area signing should be consistent with that provided for rest areas, except that the legends should use words such as SCENIC AREA, SCENIC VIEW, or SCENIC OVERLOOK (D5-11 series) instead of REST AREA.
- **[R]** 2I.05-06 (p.484) ◆ D5-1, D5-1a, D5-2, D5-5: If a rest area or other roadside area is provided on a conventional road, a D5-1 and/or D5-1a sign should be installed in advance of the rest area or other roadside area to permit the driver to reduce speed in preparation for leaving the highway. A D5-5 sign (or a D5-2 sign if an exit ramp is provided) should be installed at the turn-off point where the driver needs to leave the highway to access the rest area or other roadside area.
- **[R]** 2I.05-07 (p.484) ◆ D5-1: If a rest area or other roadside area is provided on a freeway or expressway, a D5-1 sign should be placed 1 mile and/or 2 miles in advance of the rest area.
- **[M]** 2I.05-08 (p.484) ◆ D5-2a: A D5-2a sign shall be placed at the rest area or other roadside area exit gore.
- [O] 2I.05-09 (p.484) ◆ D5-1, D5-1a: A D5-1a sign may be placed between the D5-1 sign and the exit gore on a freeway or expressway. A second D5-1 sign may be used in place of the D5-1a sign with a distance to the nearest ½ or ¼ mile displayed as a fraction rather than a decimal for distances of less than 1 mile.
- [O] 2I.05-10 (p.484) ◆ D5-6: To provide the road user with information on the location of succeeding rest areas, a Next Rest Area (D5-6) sign (see Figure 2I-5) may be installed independently or as a supplemental sign mounted below one of the REST AREA advance guide signs.
- **[M]** 2I.05-11 (p.484): All signs on freeways and expressways for rest and other roadside areas shall have letter and numeral sizes that comply with the minimum requirements of Tables 2E-2 through 2E-5. The sizes for General Service signs that have standardized designs shall be as shown in Table 2I-1.
- [O] 2I.05-12 (p.484): If the rest area has facilities for persons with disabilities (see Section 2I.02), the International Symbol of Accessibility (D9-6) sign (see Figure 2I-1) may be placed with or beneath an advance guide sign for the rest area.
- [O] 2I.05-13 (p.484): If telecommunication devices for the deaf (TDD) are available at the rest area, the TDD (D9-21) symbol sign (see Figure 2I-1) may be used to supplement the advance guide signs for the rest area.
- [O] 2I.05-14 (p.484): If wireless Internet services are available at the rest area, the Wireless Internet (D9-22) symbol sign (see Figure 2I-1) may be used to supplement the advance guide signs for the rest area.

<a id="sec-2I-06"></a>
#### Section 2I.06 Brake Check Area Signs (D5-13 and D5-14)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D5-13](symbols/D5-13.png) | **D5-13** | Brake Check Area Advance | Recommended (2I.06-01) | 96 x 54 | 132 x 66 | 2I-1 p.476 | — |
| ![D5-14](symbols/D5-14.png) | **D5-14** | Brake Check Area Entrance Direction | Recommended (2I.06-01) | 96 x 54 | 132 x 78 | 2I-1 p.476 | — |

- **[R]** 2I.06-01 (p.484): If an area has been provided for drivers to pull off of the roadway to check the brakes on their vehicle, a Brake Check Area Advance (D5-13) sign (see Figure 2I-6) should be installed in advance of the brake check area, and a D5-14 sign (see Figure 2I-6) should be placed at the entrance to the brake check area.

<a id="sec-2I-07"></a>
#### Section 2I.07 Chain-Up Area Signs (D5-15 and D5-16)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D5-15](symbols/D5-15.png) | **D5-15** | Chain-Up Area Advance | Recommended (2I.07-01) | 72 x 54 | 102 x 66 | 2I-1 p.476 | — |
| ![D5-16](symbols/D5-16.png) | **D5-16** | Chain-Up Area Entrance Direction | Recommended (2I.07-01) | 72 x 54 | 102 x 78 | 2I-1 p.476 | — |

- **[R]** 2I.07-01 (p.486): If an area has been provided for drivers to pull off of the roadway to install chains on their tires, a Chain-Up Area Advance (D5-15) sign (see Figure 2I-6) should be installed in advance of the chain-up area, and a D5-16 sign (see Figure 2I-6) should be placed at the entrance to the chain-up area.

<a id="sec-2I-08"></a>
#### Section 2I.08 Tourist Information and Welcome Center Signs (D5-7 Series and D5-8)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **D5-7** | Rest Area Tourist Info Center Advance | Recommended (2I.08-05) | 90 x 72* | 156 x 108* (F) | 2I-1 p.476 | — |
|  | **D5-7a** | Rest Area Tourist Info Center | Recommended (2I.08-05) | 90 x 72* | 156 x 108* (F) | 2I-1 p.476 | — |
|  | **D5-8** | Rest Area Tourist Info Center Entrance Direction | Recommended (2I.08-05) | 84 x 72* | 138 x 108* (F) | 2I-1 p.476 | — |

*Also governed by Section 2I.05:*

- **[M]** 2I.05-01 (p.484): Rest Area signs (see Figure 2I-5) shall have a retroreflective white legend and border on a blue background.
- **[M]** 2I.05-02 (p.484): Signs that include the legend REST AREA shall be used only where parking and restroom facilities are available.
- **[R]** 2I.05-03 (p.484): A roadside area that does not contain restroom facilities should be signed to indicate the major road user service that is provided. For example, the sign legends for an area with only parking should use the words PARKING AREA (D5-9 series) instead of REST AREA. The sign legends for an area with only picnic tables and parking should use words such as PICNIC AREA, ROADSIDE TABLE, or ROADSIDE PARK (D5-10 series) instead of REST AREA.
- **[R]** 2I.05-04 (p.484): Rest areas that have tourist information and welcome centers should be signed as provided in Section 2I.08.
- **[R]** 2I.05-05 (p.484): Scenic area signing should be consistent with that provided for rest areas, except that the legends should use words such as SCENIC AREA, SCENIC VIEW, or SCENIC OVERLOOK (D5-11 series) instead of REST AREA.
- **[R]** 2I.05-06 (p.484): If a rest area or other roadside area is provided on a conventional road, a D5-1 and/or D5-1a sign should be installed in advance of the rest area or other roadside area to permit the driver to reduce speed in preparation for leaving the highway. A D5-5 sign (or a D5-2 sign if an exit ramp is provided) should be installed at the turn-off point where the driver needs to leave the highway to access the rest area or other roadside area.
- **[R]** 2I.05-07 (p.484): If a rest area or other roadside area is provided on a freeway or expressway, a D5-1 sign should be placed 1 mile and/or 2 miles in advance of the rest area.
- **[M]** 2I.05-08 (p.484): A D5-2a sign shall be placed at the rest area or other roadside area exit gore.
- [O] 2I.05-09 (p.484): A D5-1a sign may be placed between the D5-1 sign and the exit gore on a freeway or expressway. A second D5-1 sign may be used in place of the D5-1a sign with a distance to the nearest ½ or ¼ mile displayed as a fraction rather than a decimal for distances of less than 1 mile.
- [O] 2I.05-10 (p.484): To provide the road user with information on the location of succeeding rest areas, a Next Rest Area (D5-6) sign (see Figure 2I-5) may be installed independently or as a supplemental sign mounted below one of the REST AREA advance guide signs.
- **[M]** 2I.05-11 (p.484): All signs on freeways and expressways for rest and other roadside areas shall have letter and numeral sizes that comply with the minimum requirements of Tables 2E-2 through 2E-5. The sizes for General Service signs that have standardized designs shall be as shown in Table 2I-1.
- [O] 2I.05-12 (p.484): If the rest area has facilities for persons with disabilities (see Section 2I.02), the International Symbol of Accessibility (D9-6) sign (see Figure 2I-1) may be placed with or beneath an advance guide sign for the rest area.
- [O] 2I.05-13 (p.484): If telecommunication devices for the deaf (TDD) are available at the rest area, the TDD (D9-21) symbol sign (see Figure 2I-1) may be used to supplement the advance guide signs for the rest area.
- [O] 2I.05-14 (p.484): If wireless Internet services are available at the rest area, the Wireless Internet (D9-22) symbol sign (see Figure 2I-1) may be used to supplement the advance guide signs for the rest area.

- **[R]** 2I.08-02 (p.486): The number of supplemental sign panels installed with Tourist Information or Welcome Center signs should be limited to three so as not to impose an undue informational load on the road user.
- **[M]** 2I.08-03 (p.486): Tourist Information or Welcome Center signs (see Figure 2I-7) shall have a white legend and border on a blue background. Continuously staffed or unstaffed operation at least 8 hours per day, 7 days per week, shall be required.
- **[M]** 2I.08-04 (p.486): If operated only on a seasonal basis, the Tourist Information or Welcome Center signs shall be removed or covered during the off seasons.
- **[R]** 2I.08-05 (p.486) ◆ D5-7, D5-8: For freeway or expressway rest area locations that also serve as tourist information or welcome centers, the following signing criteria should be used: A. The locations for tourist information and welcome center Advance Guide, Exit Direction, and Exit Gore signs should meet the General Service signing requirements described in Section 2I.03. B. If the signing for the tourist information or welcome center is to be accomplished in conjunction with the initial signing for the rest areas, the message on the Rest Area Tourist Info Center Advance (D5-7) sign should be REST AREA, TOURIST INFO CENTER, XX MILES or REST AREA, STATE NAME (optional), WELCOME CENTER XX MILES. On the Rest Area Tourist Info Center Entrance Direction (D5-8) sign the message should be REST AREA, TOURIST INFO CENTER with a diagonally upward-pointing directional arrow (or NEXT RIGHT), or REST AREA, STATE NAME (optional), WELCOME CENTER with a diagonally upward-pointing directional arrow (or NEXT RIGHT). C. If the initial rest area Advance Guide and Exit Direction signing is in place, these signs should include, on supplemental signs, the legend TOURIST INFO CENTER or STATE NAME (optional), WELCOME CENTER. D. The Exit Gore sign should contain only the legend REST AREA with the arrow and should not be supplemented with any legend pertaining to the tourist information center or welcome center.
- [O] 2I.08-06 (p.486): As an alternative to the supplemental TOURIST INFO CENTER legend, the Tourist Information (D9-10) sign (see Figure 2I-1) may be appended beneath the REST AREA advance guide sign.
- [O] 2I.08-07 (p.487): The name of the State or local jurisdiction may appear on the Advance Guide and Exit Direction tourist information/welcome center signs if the jurisdiction controls the operation of the tourist information or welcome center and the center meets the operating criteria set forth in this Manual and is consistent with State policies.
- **[R]** 2I.08-08 (p.487): For tourist information centers that are located off the freeway or expressway facility, additional signing criteria should be as follows: A. Each State should adopt a policy establishing the maximum distance that a tourist information center can be located from the interchange in order to be included on official signs. B. The location of signing should be in accordance with requirements pertaining to General Service signing (see Section 2I.03). C. Signing along the crossroad should be installed to guide the road user from the interchange to the tourist information center and back to the interchange.
- [O] 2I.08-09 (p.487): As an alternative, the Tourist Information (D9-10) sign (see Figure 2I-1) may be appended to the guide signs for the exit that provides access to the tourist information center. As a second alternative, the Tourist Information sign may be combined with General Service signing.

<a id="sec-2I-09"></a>
#### Section 2I.09 Radio Information Signing (D12-1 Series)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D12-1](symbols/D12-1.png) | **D12-1** | Radio - Weather Information | Optional (2I.09-01) | 84 x 48 | 132 x 84 | 2I-1 p.477 | — |
|  | **D12-1a** | Radio - Traffic Information | Optional (2I.09-01) | 96 x 48 | 120 x 60 | 2I-1 p.477 | — |
|  | **D12-1bP** | Urgent Message When Flashing (plaque) | Optional (2I.09-01) | 84 x 30 | 108 x 36 | 2I-1 p.477 | — |

- [O] 2I.09-01 (p.487) ◆ D12-1, D12-1a: A Radio-Weather Information (D12-1) sign (see Figure 2I-8) may be used in areas where difficult driving conditions commonly result from weather systems. Radio-Traffic Information (D12-1a) signs may be used in conjunction with traffic management systems.
- **[M]** 2I.09-02 (p.487): Radio-Weather and Radio-Traffic Information signs shall have a white legend and border on a blue background. Only the numerical indication of the radio frequency shall be used to identify a station broadcasting travel-related weather or traffic information. No more than three frequencies shall be displayed on each sign. Only radio stations whose signal will be of value to the road user and who agree to broadcast either of the following two items shall be identified on Radio-Weather and Radio-Traffic Information signs: A. Periodic weather warnings at a rate of at least once every 15 minutes during periods of adverse weather; or B. Driving condition information (affecting the roadway being traveled) at a rate of at least once every 15 minutes, or when required, during periods of adverse traffic conditions, and when supplied by an official agency having jurisdiction.
- **[M]** 2I.09-03 (p.487): If a station to be considered operates only on a seasonal basis, its signs shall be removed or covered during the off season.
- **[R]** 2I.09-04 (p.487): The radio station should have a signal strength to adequately broadcast at least 70 miles along the route. Signs should be spaced as needed for each direction of travel at distances determined by an engineering study. The stations to be included on the signs should be selected in cooperation with the association(s) representing major broadcasting stations in the area to provide: (1) maximum coverage to all road users on both AM and FM frequencies; and (2) consideration of 24 hours per day, 7 days per week broadcast capability.
- [O] 2I.09-05 (p.487): The URGENT MESSAGE WHEN FLASHING (D12-1bP) plaque may be mounted below the D12-1 or D12-1a sign if supplemented by Warning Beacons (see Section 4S.03) that flash only when a message related to adverse travel conditions is being broadcast.
- [O] 2I.09-06 (p.487): In roadway rest area locations, a smaller sign using a greater number of radio frequencies, but of the same general design, may be used.
- **[M]** 2I.09-07 (p.487): Radio-Weather and Radio-Traffic Information signs installed in rest areas shall be positioned such that they are not visible from the main roadway.

<a id="sec-2I-10"></a>
#### Section 2I.10 Channel 9 Monitored Sign (D12-3)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D12-3](symbols/D12-3.png) | **D12-3** | Channel 9 Monitored | Optional (2I.10-01) | 84 x 48 | 132 x 84 | 2I-1 p.477 | — |

- [O] 2I.10-01 (p.488): A Channel 9 Monitored (D12-3) sign (see Figure 2I-8) may be installed as needed. Official public agencies or their designees may be displayed as the monitoring agency on the sign.
- **[M]** 2I.10-02 (p.488): Only official public agencies or their designee shall be displayed as the monitoring agency on the Channel 9 Monitored sign.

<a id="sec-2I-11"></a>
#### Section 2I.11 EMERGENCY CALL 911 Sign (D12-4)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D12-4](symbols/D12-4.png) | **D12-4** | Emergency Call 911 | Optional (2I.11-01) | 66 x 30 | 96 x 48 | 2I-1 p.477 | — |

- [O] 2I.11-01 (p.488): An Emergency CALL 911 (D12-4) sign (see Figure 2I-8) may be used for cellular telephone communications.

<a id="sec-2I-12"></a>
#### Section 2I.12 TRAVEL INFO CALL 511 Signs (D12-5 and D12-5a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **D12-5** | Travel Info Call 511 (pictograph) | Optional (2I.12-01) | 48 x 60 | 66 x 72 | 2I-1 p.477 | — |
| ![D12-5a](symbols/D12-5a.png) | **D12-5a** | Travel Info Call 511 | Optional (2I.12-01) | 48 x 36 | 66 x 48 | 2I-1 p.477 | — |

- [O] 2I.12-01 (p.489): A TRAVEL INFO CALL 511 (D12-5 or D12-5a) sign (see Figure 2I-8) may be installed if a 511 travel information services telephone number is available to road users for obtaining traffic, public transportation, weather, construction, or road condition information.
- [O] 2I.12-02 (p.489) ◆ D12-5: The pictograph of the transportation agency or the travel information service or program that is providing the travel information may be displayed in place of the 511 pictograph on the D12-5 sign above the TRAVEL INFO CALL 511 legend.
- **[M]** 2I.12-03 (p.489) ◆ D12-5: The logo of a commercial entity shall not be incorporated within the TRAVEL INFO CALL 511 signs. 04 If the pictograph of the transportation agency or the travel information service or program is used in place of the 511 pictograph on the D12-5 sign (see Paragraph 2 of this Section), the maximum height of the pictograph shall not exceed the height of the 511 pictograph on the standard sign size specified for the roadway classification in Table 2H-1.
- **[M]** 2I.12-05 (p.489): The TRAVEL INFO CALL 511 signs shall have a white legend and border on a blue background.

<a id="sec-2I-13"></a>
#### Section 2I.13 Roadside Assistance Sign (D12-6)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D12-6](symbols/D12-6.png) | **D12-6** | Roadside Assistance | Optional (2I.13-01) | 60 x 42 | 78 x 54 | 2I-1 p.477 | — |

- [O] 2I.13-01 (p.489): A Roadside Assistance (D12-6) sign (see Figure 2I-8) displaying the Highway Assistance cellular telephone code designated for that roadway or jurisdiction may be used along a highway that is served by an authorized roadside assistance program with authorized service vehicles and personnel that provide roadside vehicle repair assistance to road users free of charge.

<a id="sec-2I-14"></a>
#### Section 2I.14 Carpool and Ridesharing Signing (D12-2)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D12-2](symbols/D12-2.png) | **D12-2** | Carpool Information | Optional (2I.14-01) | 60 x 42 | 96 x 66 | 2I-1 p.477 | — |

- [O] 2I.14-01 (p.489): In areas having carpool matching services, a Carpool Information (D12-2) sign (see Figure 2I-8) may be provided adjacent to highways with preferential lanes or along any other highway.
- [O] 2I.14-02 (p.489): Carpool Information signs may include an Internet domain name or telephone number of more than four characters within the legend.
- **[M]** 2I.14-03 (p.489): If a local transit pictograph or carpool symbol is incorporated into the Carpool Information sign, the maximum vertical dimension of the pictograph or symbol shall not exceed 18 inches and the maximum horizontal dimension shall not exceed 30 inches.

<a id="sec-2I-15"></a>
#### Section 2I.15 Signing for Truck Parking Availability (D9-16b through D9-16e)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **D9-16b** | Truck Parking Availability - Exit Number | Optional (2I.15-01) | Varies x 144 | Varies x 144 | 2I-1 p.477 | — |
|  | **D9-16c** | Truck Parking Availability - Distance | Optional (2I.15-01) | Varies x 144 | Varies x 144 | 2I-1 p.477 | — |
|  | **D9-16d** | Signing for Truck Parking Availability (D9-16b through D9-16e) | Optional (2I.15-01) | — | — | text | — |
|  | **D9-16e** | Signing for Truck Parking Availability (D9-16b through D9-16e) | Optional (2I.15-01) | — | — | text | — |

- [O] 2I.15-01 (p.489): General Service signs may be used to display the number of available truck parking spaces at roadside areas such as rest areas, welcome centers, and weigh stations, and at facilities off a highway that are open to the public and provide parking for commercial vehicles 24 hours per day, 7 days per week.
- **[M]** 2I.15-02 (p.489): The Truck Parking Availability General Service (D9-16b through D9-16e) signs (see Figure 2I-9) shall include a changeable message element with a white changeable legend on a black opaque background that displays only the number of parking spaces currently available at each location or the legend FULL. The upper section of the sign shall display the Truck Parking (D9-16) symbol sign and the legend SPACES OPEN. The sign shall display the number of available truck parking spaces for no more than three parking facilities. Where two lines of legend, such as the location and a distance, are displayed for a parking facility, not more than two parking facilities shall be displayed on the sign.
- **[M]** 2I.15-03 (p.489): Where the truck parking facility is located off the main highway and is accessed from the crossroad, directional assemblies with the Truck Parking (D9-16) sign shall be installed along the ramp and along crossroads where the route to the facility requires a turn, where it is unclear as to which roadway to follow, or where additional guidance is needed.
- [O] 2I.15-05 (p.490): The word FULL in a white legend may be displayed on changeable message elements of a Truck Parking Availability General Service sign when the number of truck parking spaces available at the associated facility reaches a predetermined lower threshold.
- **[R]** 2I.15-06 (p.490): Truck Parking Availability signs should be located 3 to 5 miles in advance of the nearest parking facility. The parking facilities displayed on the sign should be no more than 60 miles from the sign location.

### Chapter 2N Emergency Management Signing

<a id="sec-2N-03"></a>
#### Section 2N.03 Evacuation Route Signs (EM1 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM1-1](symbols/EM1-1.png) | **EM1-1** | Evacuation Route | Mandatory (2N.03-01) | 24 x 24* | 2N-1 p.532 | — |
| ![EM1-1a](symbols/EM1-1a.png) | **EM1-1a** | Use of the specific Evacuation Route | Mandatory (2N.03-01) | — | text | — |
| ![EM1-2](symbols/EM1-2.png) | **EM1-2** | Evacuation Route | Mandatory (2N.03-01) | 24 x 24* | 2N-1 p.532 | — |
|  | **EM-1a** | Evacuation Route | Mandatory (2N.03-01) | 24 x 24* | 2N-1 p.532 | — |

- **[M]** 2N.03-01 (p.532) ◆ EM1-2: An Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaque (see ~~Figure 2D~~ -6) shall be installed below the EM1-2 sign. The Advance Turn Arrow or Directional Arrow auxiliary plaque shall have a white arrow and border on a blue background when used with an EM1-2 sign.
- [O] 2N.03-02 (p.532) ◆ EM1-1a: Where different evacuation conditions use different evacuation routes in the same area, the word HURRICANE, or a word that describes some other type of evacuation route, may be added above the EVACUATION ROUTE legend within the blue circular symbol on the EM1-1a sign.
- **[M]** 2N.03-03 (p.532) ◆ EM1-1, EM1-1a: The EM1-1 series signs shall include a white directional arrow. The arrow designs on the EM1-1 series signs shall include a straight, vertical arrow pointing upward, a straight horizontal arrow pointing to the left or right, or a bent arrow pointing to the left or right for advance warning of a turn.
- **[R]** 2N.03-04 (p.532): If used, the Evacuation Route sign, with the appropriate arrow, should be installed 150 to 300 feet in advance of, and at, any turn in an approved evacuation route. The sign should also be installed elsewhere for straightahead confirmation where needed.
- **[R]** 2N.03-05 (p.532): If used in urban areas, the Evacuation Route sign shall be mounted at the right-hand side of the roadway, not less than 7 feet above the top of the curb, and at least 1 foot back from the face of the curb. If used in rural areas, the Evacuation Route sign shall be mounted at the right-hand side of the roadway, not less than 7 feet above the near edge of the pavement and not less than 6 feet or more than 10 feet to the right of the right-hand roadway edge.
- **[R]** 2N.03-06 (p.533): Evacuation Route signs shall not be placed where they will conflict with other signs. Where a conflict in placement would occur between the Evacuation Route sign and a standard regulatory sign, the regulatory sign shall take precedence.
- [O] 2N.03-07 (p.533): In case of a conflict with guide or warning signs, the Evacuation Route sign may take precedence.
- **[R]** 2N.03-08 (p.533): Placement of Evacuation Route signs should be made under the supervision of the officials having jurisdiction over the placement of other traffic signs. Coordination with Emergency Management authorities and agreement between contiguous political entities should occur to assure continuity of routes.
- **[R]** 2N.03-09 (p.533) ◆ EM1-1a, EM1-2: Use of the specific Evacuation Route (EM1-1a and EM1-2) signs should be limited to areas where different evacuation conditions use different evacuation routes.

<a id="sec-2N-04"></a>
#### Section 2N.04 AREA CLOSED Sign (EM2-1)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM2-1](symbols/EM2-1.png) | **EM2-1** | Area Closed | Recommended (2N.04-01) | 30 x 24 | 2N-1 p.532 | — |

- **[R]** 2N.04-01 (p.533): The AREA CLOSED (EM2-1) sign (see Figure 2N-1) should be used to close a roadway in order to prohibit traffic from entering the area. It should be installed on the shoulder as near as practical to the right-hand edge of the roadway, or preferably, on a portable mounting or barricade partly or entirely in the roadway.
- **[R]** 2N.04-02 (p.533): For best visibility, particularly at night, the sign height should not exceed 4 feet measured vertically from the pavement to the bottom of the sign. Unless adequate advance warning signs are used, it should not be placed to create a complete and unavoidable blocked route. Where feasible, the sign should be located at an intersection that provides a detour route.

<a id="sec-2N-05"></a>
#### Section 2N.05 TRAFFIC CONTROL POINT Sign (EM2-2)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM2-2](symbols/EM2-2.png) | **EM2-2** | Traffic Control Point | Recommended (2N.05-01) | 30 x 24 | 2N-1 p.532 | — |

- **[R]** 2N.05-01 (p.533): The TRAFFIC CONTROL POINT (EM2-2) sign (see Figure 2N-1) should be used to designate a location where an official traffic control point has been set up to impose such controls as are necessary to limit congestion, expedite emergency traffic, exclude unauthorized vehicles, or protect the public.
- **[R]** 2N.05-02 (p.533): The sign should be installed in the same manner as the AREA CLOSED sign (see Section 2N.04), and at the point where traffic must stop to be checked.
- **[R]** 2N.05-03 (p.533): A STOP (R1-1) sign (see Section 2B.04) should be used in conjunction with the TRAFFIC CONTROL POINT sign.
- **[R]** 2N.05-04 (p.533): The TRAFFIC CONTROL POINT sign should be mounted directly below the STOP sign.

<a id="sec-2N-06"></a>
#### Section 2N.06 MAINTAIN TOP SAFE SPEED Sign (EM2-3)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM2-3](symbols/EM2-3.png) | **EM2-3** | Maintain Top Safe Speed | Optional (2N.06-01) | 24 x 30 | 2N-1 p.532 | — |

- [O] 2N.06-01 (p.533): The MAINTAIN TOP SAFE SPEED (EM2-3) sign (see Figure 2N-1) may be used on highways where conditions are such that it is prudent to evacuate or traverse an area as quickly as possible.
- [O] 2N.06-02 (p.533): Where an existing Speed Limit (R2-1) sign is in a suitable location, the MAINTAIN TOP SAFE SPEED sign may be mounted directly over the face of the speed limit sign that it supersedes.
- **[R]** 2N.06-04 (p.533): The sign should be installed as needed, in the same manner as other standard speed signs.
- **[M]** 2N.06-05 (p.533): If used in rural areas, the MAINTAIN TOP SAFE SPEED sign shall be mounted on the right-hand side of the road at a horizontal distance of not less than 6 feet or more than 10 feet from the roadway edge, and at a minimum height, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way, of 5 feet. If used in urban areas, the minimum height, measured vertically from the bottom of the sign to the top of the curb, or in the absence of curb, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way, shall be 7 feet, and the nearest edge of the sign shall be not less than 1 foot back from the face of the curb.

<a id="sec-2N-07"></a>
#### Section 2N.07 Permit Required Sign (EM2-4)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM2-4](symbols/EM2-4.png) | **EM2-4** | Permit Required | Mandatory (2N.07-02) | 24 x 30 | 2N-1 p.532 | — |

- [S] 2N.07-01 (p.534): The intent of the Permit Required (EM2-4) sign (see Figure 2N-1) is to notify road users of the presence of the traffic control point so that those who do not have priority permits issued by designated authorities can take another route, or turn back, without making a needless trip and without adding to the screening load at the post. Local traffic, without permits, can proceed as far as the traffic control post.
- **[M]** 2N.07-02 (p.534): If used, the Permit Required (EM2-4) sign shall be used at an intersection that is an entrance to a route on which a traffic control point is located.
- **[M]** 2N.07-03 (p.534): If used, the EM2-4 sign shall be installed in a manner similar to that of the MAINTAIN TOP SAFE SPEED sign (see Section 2N.06).

<a id="sec-2N-08"></a>
#### Section 2N.08 Emergency Aid Center Signs (EM3-1 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM3-1](symbols/EM3-1.png) | **EM3-1** | MEDICAL CENTER | Mandatory (2N.08-01) | 30 x 24 | 2N-1 p.532 | — |
| ![EM3-1a](symbols/EM3-1a.png) | **EM3-1a** | WELFARE CENTER | Mandatory (2N.08-01) | 30 x 24 | 2N-1 p.532 | — |
| ![EM3-1b](symbols/EM3-1b.png) | **EM3-1b** | REGISTRATION CENTER | Mandatory (2N.08-01) | 30 x 24 | 2N-1 p.532 | — |
| ![EM3-1c](symbols/EM3-1c.png) | **EM3-1c** | DECONTAMINATION CENTER | Mandatory (2N.08-01) | 30 x 24 | 2N-1 p.532 | — |

- **[M]** 2N.08-01 (p.534): In the event of emergency, State and local authorities shall establish various centers for civilian relief, communication, medical service, and similar purposes. To guide the public to such centers a series of directional signs shall be used.
- **[M]** 2N.08-02 (p.534): Emergency Aid Center (EM3-1 series) signs (see Figure 2N-1) shall display the designation of the center and an arrow indicating the direction to the center. They shall be installed as needed, at intersections and elsewhere, on the right-hand side of the roadway, in urban areas at a minimum height, measured vertically from the bottom of the sign to the top of the curb, or in the absence of curb, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way, of 7 feet, and not less than 1 foot back from the face of the curb, and in rural areas at a minimum height, measured vertically from the bottom of the sign to the elevation of the near edge of the traveled way, of 5 feet, and at a horizontal distance of not less than 6 feet or more than 10 feet from the roadway edge.
- **[M]** 2N.08-03 (p.534): Emergency Aid Center signs shall display one of the following legends, as appropriate, or others designating similar emergency facilities: A. MEDICAL CENTER (EM3-1), B. WELFARE CENTER (EM3-1a), C. REGISTRATION CENTER (EM3-1b), or D. DECONTAMINATION CENTER (EM3-1c).
- **[M]** 2N.08-04 (p.534): The Emergency Aid Center sign shall be a horizontally-oriented rectangle. Except as provided in Paragraph 5 of this Section, the Emergency Aid Center signs shall have a black legend and border on a white background.
- [O] 2N.08-05 (p.534): When Emergency Aid Center signs are used in an incident situation, such as during the aftermath of a nuclear or biological attack, the background color may be fluorescent pink (see Chapter 6O).

<a id="sec-2N-09"></a>
#### Section 2N.09 Shelter Directional Signs (EM4-1 Series)

| Sign | Code | Name | Default class | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|
| ![EM4-1](symbols/EM4-1.png) | **EM4-1** | EMERGENCY | Mandatory (2N.09-01) | 30 x 24 | 2N-1 p.532 | — |
| ![EM4-1a](symbols/EM4-1a.png) | **EM4-1a** | HURRICANE | Mandatory (2N.09-01) | 30 x 24 | 2N-1 p.532 | — |
| ![EM4-1b](symbols/EM4-1b.png) | **EM4-1b** | FALLOUT | Mandatory (2N.09-01) | 30 x 24 | 2N-1 p.532 | — |
| ![EM4-1c](symbols/EM4-1c.png) | **EM4-1c** | CHEMICAL | Mandatory (2N.09-01) | 30 x 24 | 2N-1 p.532 | — |

- **[M]** 2N.09-01 (p.534): Shelter Directional (EM4-1 series) signs (see Figure 2N-1) shall be used to direct the public to selected shelters that have been licensed and marked for emergency use.
- **[M]** 2N.09-02 (p.534): The installation of Shelter Directional signs shall comply with established signing standards. Where used, the signs shall not be installed in competition with other necessary highway regulatory, guide, and warning signs.
- **[M]** 2N.09-03 (p.534): The Shelter Directional sign shall be a horizontally-oriented rectangle. Except as provided in Paragraph 4 of this Section, the Shelter Directional signs shall have a black legend and border on a white background.
- [O] 2N.09-04 (p.534): When Shelter Directional signs are used in an incident situation, such as during the aftermath of a nuclear or biological attack, the background color may be fluorescent pink (see Chapter 6O).
- [O] 2N.09-05 (p.534): The distance to the shelter may be omitted from the sign when appropriate.
- [O] 2N.09-06 (p.534): Shelter Directional signs may display one of the following legends, or others designating similar emergency facilities: A. EMERGENCY (EM4-1), B. HURRICANE (EM4-1a), C. FALLOUT (EM4-1b), or D. CHEMICAL (EM4-1c).
- [O] 2N.09-07 (p.535): If appropriate, the name of the facility may be used.
- [O] 2N.09-08 (p.535): The Shelter Directional signs may be installed on the Interstate Highway System or any other major highway system when it has been determined that a need exists for such signs as part of a State or local shelter plan.
- [O] 2N.09-09 (p.535): The Shelter Directional signs may be used to identify different routes to a shelter to provide for rapid movement of large numbers of persons.
- **[R]** 2N.09-10 (p.535): The Shelter Directional sign should be used sparingly and only in conjunction with approved plans of State and local authorities.
- **[R]** 2N.09-11 (p.535): The Shelter Directional sign should not be posted more than 5 miles from a shelter. (This page intentionally left blank)

## Part 6 Temporary Traffic Control

### Chapter 6D 

<a id="sec-6D-02"></a>
#### Section 6D.02 STOP/SLOW Paddle for Hand-Signaling

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W20-8** | Slow (on Stop/Slow Paddle) | Optional | 18 x 18 | — | — | 6H-1 p.804 | — |

- **[R]** 6D.02-01 (p.783): The STOP/SLOW paddle (see Figure 6D-1 and Table 6G-1) should be the primary and preferred handsignaling device because the STOP/SLOW paddle gives road users more positive guidance than red flags.
- **[M]** 6D.02-03 (p.783): A STOP/STOP or a SLOW/SLOW paddle may be used in certain situations (see Section 6D.05), provided the device meets the size and shape requirements for the STOP/SLOW paddle.
- **[R]** 6D.02-04 (p.783): The STOP/SLOW paddle should be fabricated from light semi-rigid material.
- [O] 6D.02-06 (p.783): The STOP/SLOW paddle may be modified to improve conspicuity by incorporating either white or red flashing lights on the STOP face, and either white or yellow flashing lights on the SLOW face. The flashing lights may be arranged in any of the following patterns: A. Two white or red lights, one centered vertically above and one centered vertically below the STOP legend; and/or two white or yellow lights, one centered vertically above and one centered vertically below the SLOW legend; B. Two white or red lights, one centered horizontally on each side of the STOP legend; and/or two white or yellow lights, one centered horizontally on each side of the SLOW legend; C. One white or red light centered below the STOP legend; and/or one white or yellow light centered below the SLOW legend; D. A series of eight or more small white or red lights no larger than ¼ inch in diameter along the outer edge of the paddle, arranged in an octagonal pattern at the eight corners of the border of the STOP face; and/ or a series of eight or more small white or yellow lights no larger than ¼ inch in diameter along the outer edge of the paddle, arranged in a diamond pattern along the border of the SLOW face; or E. A series of white lights forming the shapes of the letters in the legend.
- **[M]** 6D.02-07 (p.783): If flashing lights are used on the STOP face of the paddle, their colors shall be all white or all red. If flashing lights are used on the SLOW face of the paddle, their colors shall be all white or all yellow.
- **[M]** 6D.02-08 (p.783): If more than eight flashing lights are used, the lights shall be arranged such that they clearly convey the octagonal shape of the STOP face of the paddle and/or the diamond shape of the SLOW face of the paddle.
- **[M]** 6D.02-09 (p.783): If flashing lights are used on the STOP/SLOW paddle, the flash rate shall be at least 50, but not more than 60, flashes per minute.

### Chapter 6G TTC Regulatory Signs

<a id="sec-6G-03"></a>
#### Section 6G.03 Regulatory Sign Applications

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R1-7a](symbols/R1-7a.png) | **R1-7a** | Wait on Stop - Go on Slow | Optional | 30 x 36 | 30 x 36 | — | 6G-1 p.796 | — |

- **[M]** 6G.03-01 (p.793): If a TTC zone requires regulatory measures different from those existing, the existing permanent regulatory devices shall be removed or covered and superseded by the appropriate temporary regulatory signs. This change shall be made in compliance with applicable ordinances or statutes of the jurisdiction.

<a id="sec-6G-07"></a>
#### Section 6G.07 STAY IN LANE Signs (R4-9 and R4-9a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R4-9a](symbols/R4-9a.png) | **R4-9a** | Stay In Lane To Merge Point | Optional (6G.07-01) | 36 x 48 | 36 x 48 | — | 6G-1 p.796 | — |

- [O] 6G.07-01 (p.795): A STAY IN LANE (R4-9) sign (see Figure 6G-1) may be used where a multi-lane shift has been incorporated as part of the TTC on a highway to direct road users around road work that occupies part of the roadway on a multi-lane highway.
- **[R]** 6G.07-02 (p.795): A STAY IN LANE TO MERGE POINT (R4-9a) sign (see Figure 6G-1) should be used during late merge operations (see Section 6N.19) to direct traffic to use all available lanes until the merge point is reached.

<a id="sec-6G-08"></a>
#### Section 6G.08 Work Zone and Higher Fines Signs and Plaques

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **G20-5aP** | Work Zone (plaque) | Optional (6G.08-01) | 24 x 18 | 30 x 24 | — | 6G-1 p.796 | — |
| ![R2-12](symbols/R2-12.png) | **R2-12** | End Work Zone Speed Limit | Optional (6G.08-01) | 24 x 36 | 36 x 54 | — | 6G-1 p.796 | — |

- [O] 6G.08-01 (p.795): A WORK ZONE (G20-5aP) plaque (see Figure 6G-1) may be mounted above a Speed Limit sign to emphasize that a reduced speed limit is in effect within a TTC zone. An END WORK ZONE SPEED LIMIT (R2-12) sign (see Figure 6G-1) may be installed at the downstream end of the reduced speed limit zone.

<a id="sec-6G-09"></a>
#### Section 6G.09 PEDESTRIAN CROSSWALK Sign (R9-8)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R9-8](symbols/R9-8.png) | **R9-8** | Pedestrian Crosswalk | Optional (6G.09-01) | 36 x 18 | — | — | 6G-1 p.796 | — |

- [O] 6G.09-01 (p.797): The PEDESTRIAN CROSSWALK (R9-8) sign (see Figure 6G-1) may be used to indicate where a temporary crosswalk has been established.
- **[M]** 6G.09-02 (p.797): If a temporary crosswalk is established, it shall be accessible to pedestrians with disabilities in accordance with Section 6C.03.

<a id="sec-6G-10"></a>
#### Section 6G.10 SIDEWALK CLOSED Signs (R9-9, R9-10, R9-11, and R9-11a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R9-9](symbols/R9-9.png) | **R9-9** | Sidewalk Closed | Recommended (6G.10-01) | 24 x 12 | — | — | 6G-1 p.796 | — |
| ![R9-10](symbols/R9-10.png) | **R9-10** | Sidewalk Closed, Use Other Side | Recommended (6G.10-01) | 24 x 12 | — | — | 6G-1 p.796 | — |
| ![R9-11](symbols/R9-11.png) | **R9-11** | Sidewalk Closed Ahead, Cross Here | Recommended (6G.10-01) | 24 x 18 | — | — | 6G-1 p.796 | — |
| ![R9-11a](symbols/R9-11a.png) | **R9-11a** | Sidewalk Closed, Cross Here | Recommended (6G.10-01) | 24 x 12 | — | — | 6G-1 p.796 | — |

- **[R]** 6G.10-01 (p.797): SIDEWALK CLOSED signs (see Figure 6G-1) should be used where pedestrian flow is restricted. Bicyclist/ Pedestrian Detour (M4-9a) signs or Pedestrian Detour (M4-9b) signs should be used where pedestrian flow is rerouted (see Section 6I.02).
- **[R]** 6G.10-02 (p.797) ◆ R9-9: The SIDEWALK CLOSED (R9-9) sign should be installed at the beginning of the closed sidewalk, at the intersections preceding the closed sidewalk, and elsewhere along the closed sidewalk as needed.
- **[R]** 6G.10-03 (p.797) ◆ R9-10: The SIDEWALK CLOSED, (ARROW) USE OTHER SIDE (R9-10) sign should be installed at the beginning of the restricted sidewalk when a parallel sidewalk exists on the other side of the roadway.
- **[R]** 6G.10-04 (p.797) ◆ R9-11: The SIDEWALK CLOSED AHEAD, (ARROW) CROSS HERE (R9-11) sign should be used to indicate to pedestrians that sidewalks beyond the sign are closed and to direct them to open crosswalks, sidewalks, or other travel paths.
- **[R]** 6G.10-05 (p.797) ◆ R9-11a: The SIDEWALK CLOSED, (ARROW) CROSS HERE (R9-11a) sign should be installed just beyond the point to which pedestrians are being redirected.

<a id="sec-6G-11"></a>
#### Section 6G.11 TURN OFF 2-WAY RADIO AND CELL PHONE Sign (R22-2)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R22-2](symbols/R22-2.png) | **R22-2** | Turn Off 2-Way Radio and Cell Phone | Mandatory (6G.11-01) | 42 x 36 | 42 x 36 | — | 6G-1 p.796 | — |

- **[M]** 6G.11-01 (p.797): The TURN OFF 2-WAY RADIO AND CELL PHONE (R22-2) sign (see Figure 6G-1) shall be used to require road users to turn off mobile radio transmitters and cellular telephones where blasting operations occur.

### Chapter 6H TTC Warning Signs

<a id="sec-6H-01"></a>
#### Section 6H.01 Warning Sign Function, Design, and Application

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W9-2** | Lane Ends | Optional (6H.01-09) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.803 | — |

- **[M]** 6H.01-02 (p.798): TTC warning signs shall comply with the Standards for warning signs presented in Part 2 and in the FHWA’s “Standard Highway Signs” publication (see Section 1A.05).
- **[M]** 6H.01-03 (p.798): The sizes for TTC warning signs shall be as shown in Table 6H-1.
- **[M]** 6H.01-04 (p.798): Except as provided in Paragraph 5 of this Section, TTC warning signs shall be diamond-shaped with a black legend and border on an orange background, except for the Grade Crossing Advance Warning (W10-1) sign, which shall have a black legend and border on a yellow background.
- [O] 6H.01-05 (p.798): Warning signs that are required or recommended in Parts 2 or 7 to have a fluorescent yellow-green background may have that color background in TTC zones.
- [O] 6H.01-06 (p.798): Existing warning signs with a yellow background that are still applicable may remain in place.
- [O] 6H.01-07 (p.798): Warning signs used for TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6H.01-08 (p.798): Mounting or space considerations may justify a change from the standard diamond shape to a rectangular shape.
- [O] 6H.01-09 (p.798): In emergencies, available warning signs having yellow backgrounds may be used if signs with orange or fluorescent pink backgrounds are not at hand.
- **[R]** 6H.01-10 (p.798): Where roadway or road user conditions require greater emphasis, larger than standard size warning signs should be used, with the symbol or legend enlarged approximately in proportion to the outside dimensions.
- **[R]** 6H.01-11 (p.798): Where any part of the roadway is obstructed or closed by work activities or incidents, advance warning signs should be installed to alert road users well in advance of these obstructions or restrictions.
- **[R]** 6H.01-12 (p.798): Where road users include pedestrians, the provision of supplemental audible information or detectable barriers or barricades should be provided for people with vision disabilities.
- [O] 6H.01-14 (p.798): Advance warning signs may be used singly or in combination.
- [O] 6H.01-15 (p.798): Where distances are not displayed on warning signs as part of the message, a supplemental plaque with the distance legend may be mounted immediately below the sign on the same support.

<a id="sec-6H-03"></a>
#### Section 6H.03 ROAD (STREET) WORK Sign (W20-1)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W20-1** | Road Work (with distance) | Recommended (6H.03-02) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6H.03-01 (p.802): The ROAD (STREET) WORK (W20-1) sign (see Figure 6H-1), which serves as a general warning of obstructions or restrictions, should be located in advance of the work space or any detour, on the road where the work is taking place.
- **[R]** 6H.03-02 (p.802): Where traffic can enter a TTC zone from a crossroad or a major (high-volume) driveway, an advance warning sign should be used on the crossroad or major driveway.
- [O] 6H.03-03 (p.802): The legend STREET may be substituted for ROAD and the distance legend may be either XX FEET, XX MILES, or AHEAD.

<a id="sec-6H-04"></a>
#### Section 6H.04 DETOUR Sign (W20-2)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W20-2](symbols/W20-2.png) | **W20-2** | Detour (with distance) | Recommended (6H.04-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6H.04-01 (p.802): The DETOUR (W20-2) sign (see Figure 6H-1) should be used in advance of a road user detour over a different roadway or route.
- [O] 6H.04-02 (p.802): The distance legend may be either XX FEET, XX MILES, or AHEAD. Table 6H‑1. Temporary Traffic Control Zone Warning Sign and Plaque Sizes (Sheet 1 of 2)

<a id="sec-6H-05"></a>
#### Section 6H.05 ROAD (STREET) CLOSED Sign (W20-3)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W20-3** | Road Closed (with distance) | Recommended (6H.05-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6H.05-01 (p.805): The ROAD (STREET) CLOSED (W20-3) sign (see Figure 6H-1) should be used in advance of the point where a highway is closed to all road users, or to all but local road users.
- [O] 6H.05-02 (p.805): The legend STREET may be substituted for ROAD and the distance legend may be either XX FEET, XX MILES, or AHEAD.

<a id="sec-6H-06"></a>
#### Section 6H.06 ONE LANE ROAD Sign (W20-4)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W20-4](symbols/W20-4.png) | **W20-4** | One Lane Road (with distance) | Mandatory (6H.06-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[M]** 6H.06-01 (p.805): The ONE LANE ROAD (W20-4) sign (see Figure 6H-1) shall be used only in advance of that point where motor vehicle traffic in both directions must use a common single lane (see Section 6E.01).
- [O] 6H.06-02 (p.805): The distance legend may be either XX FEET, XX MILES, or AHEAD.

<a id="sec-6H-07"></a>
#### Section 6H.07 Lane(s) Closed Signs (W20-5, W20-5a, and W9-3)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W9-3](symbols/W9-3.png) | **W9-3** | Interior Lane Shift Ahead | Mandatory (6H.07-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.803 | — |
| ![W20-5](symbols/W20-5.png) | **W20-5** | Closed Signs | Mandatory (6H.07-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
| ![W20-5a](symbols/W20-5a.png) | **W20-5a** | Lane(s) Closed (with distance) | Mandatory (6H.07-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[M]** 6H.07-01 (p.805): The Lane(s) Closed sign (see Figure 6H-1) shall be used in advance of that point where one or more through lanes of a multi-lane roadway are closed.
- **[M]** 6H.07-02 (p.805) ◆ W20-5, W20-5a: For a single lane closure, the Lane Closed (W20-5) sign (see Figure 6H-1) shall use the legend RIGHT (LEFT) LANE CLOSED. Where two or more adjacent lanes are closed, the W20-5a sign (see Figure 6H-1) shall use the legend XX RIGHT (LEFT) LANES CLOSED.
- [O] 6H.07-03 (p.805): The distance legend may be either XX FEET, XX MILES, or AHEAD.
- **[R]** 6H.07-04 (p.805) ◆ W9-3: The Interior Lane Shift (W9-3) sign (see Figure 6H-1) should be used in advance of that point where work occupies an interior lane(s) and approaching motor vehicle traffic is directed to the right or left of the work zone in the lane(s) by using a shifting taper to route traffic around the closed interior lane(s).

<a id="sec-6H-09"></a>
#### Section 6H.09 ON RAMP Plaque (W13-4P)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W13-4P](symbols/W13-4P.png) | **W13-4P** | On Ramp (plaque) | Recommended (6H.09-01) | 36 x 36 | 36 x 36 | — | 6H-1 p.804 | — |

- **[R]** 6H.09-01 (p.805): When work is being done on a ramp, but the ramp remains open, the ON RAMP (W13-4P) plaque (see Figure 6H-1) should be used to supplement the advance ROAD WORK sign.

<a id="sec-6H-10"></a>
#### Section 6H.10 RAMP NARROWS Sign (W5-4)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W5-4](symbols/W5-4.png) | **W5-4** | Ramp Narrows | Recommended (6H.10-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.803 | — |

- **[R]** 6H.10-01 (p.805): The RAMP NARROWS (W5-4) sign (see Figure 6H-1) should be used in advance of the point where work on a ramp reduces the normal width of the ramp along a part or all of the ramp.

<a id="sec-6H-11"></a>
#### Section 6H.11 SLOW TRAFFIC AHEAD Sign (W23-1)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W23-1](symbols/W23-1.png) | **W23-1** | Slow Traffic Ahead | Optional (6H.11-01) | 48 x 24 | 48 x 24 | — | 6H-1 p.804 | — |

- [O] 6H.11-01 (p.805): The SLOW TRAFFIC AHEAD (W23-1) sign (see Figure 6H-1) may be used on a shadow vehicle, usually mounted on the rear of the most upstream shadow vehicle, along with other appropriate signs for mobile operations to warn of slow moving work vehicles. A ROAD WORK (W20-1) sign may also be used with the SLOW TRAFFIC AHEAD sign.

<a id="sec-6H-12"></a>
#### Section 6H.12 EXIT OPEN and EXIT CLOSED Signs (E5-2 and E5-2a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![E5-2](symbols/E5-2.png) | **E5-2** | Exit Open | Optional (6H.12-01) | 48 x 36 | 48 x 36 | — | 6I-1 p.811 | — |
| ![E5-2a](symbols/E5-2a.png) | **E5-2a** | Exit Closed | Optional (6H.12-01) | 48 x 36 | 48 x 36 | — | 6I-1 p.811 | — |

- [O] 6H.12-01 (p.806): An EXIT OPEN (E5-2) or EXIT CLOSED (E5-2a) sign (see Figure 6H-1) may be used to supplement other warning signs where work is being conducted in the vicinity of an exit ramp and where the exit maneuver for vehicular traffic using the ramp is different from the normal condition.

<a id="sec-6H-13"></a>
#### Section 6H.13 EXIT ONLY Sign (E5-3)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![E5-3](symbols/E5-3.png) | **E5-3** | Exit Only | Optional (6H.13-01) | 48 x 36 | 48 x 36 | — | 6I-1 p.811 | — |

- [O] 6H.13-01 (p.806): An EXIT ONLY (E5-3) sign (see Figure 6H-1) may be used to supplement other warning signs where work is being conducted in the vicinity of an exit ramp and where the exit maneuver for vehicular traffic using the ramp is different from the normal condition.

<a id="sec-6H-15"></a>
#### Section 6H.15 Flagger Signs (W20-7 and W20-7a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W20-7** | Flagger (symbol) | Recommended (6H.15-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
|  | **W20-7a** | Flagger | Recommended (6H.15-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6H.15-01 (p.806) ◆ W20-7: The Flagger (W20-7) sign (see Figure 6H-1) should be used in advance of any point where a flagger is stationed to control road users.
- [O] 6H.15-02 (p.806): A distance legend may be displayed on a supplemental plaque below the Flagger sign. The sign may be used with appropriate legends or in conjunction with other warning signs, such as the BE PREPARED TO STOP (W3-4) sign (see Figure 6H-1).
- [O] 6H.15-03 (p.806): The FLAGGER (W20-7a) word message sign with a distance legend may be substituted for the Flagger (W20-7) sign.

<a id="sec-6H-17"></a>
#### Section 6H.17 Narrow Two-Way Traffic Sign (W6-4)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W6-4](symbols/W6-4.png) | **W6-4** | Narrow Two-Way Traffic | Optional | 12 x 18 | 12 x 18 | — | 6H-1 p.803 | — |

- **[M]** 6H.17-01 (p.806): The Narrow Two-Way Traffic (W6-4) sign (see Figure 6H-1) shall be an upright, retroreflective orange- colored sign placed on a flexible support and sized at least 12 inches wide by 18 inches high.
- [S] 6H.17-02 (p.806): The Narrow Two-Way Traffic (W6-4) sign is intended for mounting only on a flexible support in a series along the center line to separate opposing vehicular traffic on a two-lane, two-way operation.
- **[M]** 6H.17-03 (p.806): Narrow Two-Way Traffic signs shall not be placed within pedestrian crossings.

<a id="sec-6H-18"></a>
#### Section 6H.18 Workers Signs (W21-1 and W21-1a)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W21-1](symbols/W21-1.png) | **W21-1** | Workers | Optional (6H.18-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
|  | **W21-1a** | Workers | Optional (6H.18-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- [O] 6H.18-01 (p.806) ◆ W21-1: A Workers (W21-1) sign (see Figure 6H-1) may be used to alert road users of workers in or near the roadway.
- **[R]** 6H.18-02 (p.806): In the absence of other warning devices, a Workers sign should be used when workers are in the roadway.
- [O] 6H.18-03 (p.807): The WORKERS (W21-1a) word message sign may be used as an alternate to the Workers (W21-1) symbol sign.

<a id="sec-6H-19"></a>
#### Section 6H.19 FRESH OIL (TAR) Sign (W21-2)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W21-2** | Fresh Oil | Recommended (6H.19-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6H.19-01 (p.807): The FRESH OIL (TAR) (W21-2) sign (see Figure 6H-1) should be used to warn road users of the surface treatment.

<a id="sec-6H-20"></a>
#### Section 6H.20 ROAD MACHINERY AHEAD Sign (W21-3)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W21-3](symbols/W21-3.png) | **W21-3** | Road Machinery Ahead | Optional (6H.20-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- [O] 6H.20-01 (p.807): The ROAD MACHINERY AHEAD (W21-3) sign (see Figure 6H-1) may be used to warn of machinery operating in or adjacent to the roadway.

<a id="sec-6H-22"></a>
#### Section 6H.22 Shoulder Work Signs (W21-5, W21-5a, and W21-5b)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W21-5](symbols/W21-5.png) | **W21-5** | Shoulder Work | Optional (6H.22-03) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
| ![W21-5a](symbols/W21-5a.png) | **W21-5a** | Shoulder Closed | Optional (6H.22-03) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
| ![W21-5b](symbols/W21-5b.png) | **W21-5b** | Shoulder Closed (with distance) | Optional (6H.22-03) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[M]** 6H.22-02 (p.807): The Shoulder Work sign shall have the legend SHOULDER WORK (W21-5), RIGHT (LEFT) SHOULDER CLOSED (W21-5a), or RIGHT (LEFT) SHOULDER CLOSED XX FT or AHEAD (W21-5b).
- [O] 6H.22-03 (p.807): The Shoulder Work sign may be used in advance of the point on a non-limited access highway where there is shoulder work. It may be used singly or in combination with a ROAD WORK NEXT XX MILES or ROAD WORK AHEAD sign.
- **[R]** 6H.22-04 (p.807) ◆ W21-5a, W21-5b: On freeways and expressways, the RIGHT (LEFT) SHOULDER CLOSED XX FT or AHEAD (W21-5b) sign followed by RIGHT (LEFT) SHOULDER CLOSED (W21-5a) sign should be used in advance of the point where the shoulder work occurs and should be preceded by a ROAD WORK AHEAD sign.

<a id="sec-6H-23"></a>
#### Section 6H.23 SURVEY CREW Sign (W21-6)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W21-6](symbols/W21-6.png) | **W21-6** | Survey Crew | Recommended (6H.23-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6H.23-01 (p.807): The SURVEY CREW (W21-6) sign (see Figure 6H-1) should be used to warn of surveying crews working in or adjacent to the roadway.

<a id="sec-6H-24"></a>
#### Section 6H.24 UTILITY WORK Sign (W21-7)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W21-7](symbols/W21-7.png) | **W21-7** | Utility Work (with distance) | Optional (6H.24-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- [O] 6H.24-01 (p.807): The UTILITY WORK (W21-7) sign (see Figure 6H-1) may be used as an alternate to the ROAD (STREET) WORK (W20-1) sign for utility operations on or adjacent to a highway.
- [O] 6H.24-03 (p.807): The distance legend may be either XX FEET, XX MILES, or AHEAD.

<a id="sec-6H-25"></a>
#### Section 6H.25 Signs for Blasting Areas

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W22-1](symbols/W22-1.png) | **W22-1** | Blasting Zone Ahead | Mandatory (6H.25-03) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
| ![W22-3](symbols/W22-3.png) | **W22-3** | End Blasting Zone | Mandatory (6H.25-03) | 42 x 36 | 42 x 36 | 36 x 30 | 6H-1 p.804 | — |

- **[M]** 6H.25-03 (p.808): The BLASTING ZONE AHEAD (W22-1) sign (see Figure 6H-1) shall be used in advance of any TTC zone where explosives are being used. The TURN OFF 2-WAY RADIO AND CELL PHONE (R22-2) and END BLASTING ZONE (W22-3) signs shall be used in sequence with this sign.
- **[M]** 6H.25-04 (p.808) ◆ W22-1: The TURN OFF 2-WAY RADIO AND CELL PHONE (R22-2) sign (see Section 6G.11 and Figure 6G-1) shall follow the BLASTING ZONE AHEAD (W22-1) sign and shall be placed at least 1,000 feet before the beginning of the blasting zone.
- **[M]** 6H.25-05 (p.808) ◆ W22-3: The END BLASTING ZONE (W22-3) sign (see Figure 6H-1) shall be placed a minimum of 1,000 feet past the blasting zone.

<a id="sec-6H-28"></a>
#### Section 6H.28 STEEL PLATE AHEAD Sign (W8-24)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W8-24](symbols/W8-24.png) | **W8-24** | Steel Plate Ahead | Optional (6H.28-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.803 | — |

- [O] 6H.28-01 (p.808): A STEEL PLATE AHEAD (W8-24) sign (see Figure 6H-1) may be used to warn road users that the presence of a temporary steel plate(s) might make the road surface uneven and might create slippery conditions during wet weather.

<a id="sec-6H-30"></a>
#### Section 6H.30 Reverse Curve Signs (W1-4 Series)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W1-4b](symbols/W1-4b.png) | **W1-4b** | Reverse Curve (2 or more lanes) | Recommended (6H.30-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.803 | — |
| ![W1-4c](symbols/W1-4c.png) | **W1-4c** | Reverse Curve (2 or more lanes) | Recommended (6H.30-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.803 | — |

*Also governed by Section 2C.07:*

- **[M]** 2C.07-01 (p.155): If Table 2C-4 indicates that a horizontal alignment sign (see Figure 2C-1) is required, recommended, or allowed, the sign installed in advance of the curve shall be a Curve (W1-2) sign unless a different sign is recommended or allowed by the provisions of this Section.
- **[R]** 2C.07-02 (p.155): A Turn (W1-1) sign should be used instead of a Curve (W1-2) sign in advance of a horizontal curve that has an advisory speed of 30 mph or less.
- **[R]** 2C.07-03 (p.155): Where there are two changes in roadway alignment in opposite directions that are separated by a tangent distance of less than 600 feet, the Reverse Turn (W1-3) sign should be used instead of multiple Turn (W1-1) signs or the Reverse Curve (W1-4) sign should be used instead of multiple Curve (W1-2) signs.
- [O] 2C.07-05 (p.155): A Winding Road (W1-5) sign may be used instead of multiple Turn (W1-1) or Curve (W1-2) signs where there are three or more changes in roadway alignment each separated by a tangent distance of less than 600 feet.
- [O] 2C.07-06 (p.155): A NEXT XX MILES (W7-3aP) supplemental distance plaque (see Section 2C.61) may be installed below the Winding Road sign where continuous roadway curves exist for a specific distance.
- [O] 2C.07-07 (p.158): If the curve has a change in horizontal alignment of 135 degrees or more, the Hairpin Curve (W1-11) sign may be used instead of a Turn or Curve sign.
- [O] 2C.07-08 (p.158): If the curve has a change of direction of approximately 270 degrees, such as on a cloverleaf interchange ramp, the 270-degree Loop (W1-15) sign may be used instead of a Turn or Curve sign.
- **[R]** 2C.07-09 (p.158): When the Hairpin Curve sign or the 270-degree Loop sign is installed, either a One-Direction Large Arrow (W1-6) sign or Chevron Alignment (W1-8) signs should be installed on the outside of the turn or curve.

- **[R]** 6H.30-01 (p.809): In order to give road users advance notice of a lane shift, a Reverse Curve (W1-4, W1-4b, or W1-4c) sign (see Figure 6H-1) should be used when a lane (or lanes) is being shifted to the left or right. If the design speed of the curves is 30 mph or less, a Reverse Turn (W1-3) sign should be used.
- **[M]** 6H.30-02 (p.809): If a Reverse Curve (or Turn) sign is used, the direction of the reverse curve (or turn) shall be appropriately illustrated. Except as provided in Paragraph 3 of this Section, the number of lanes illustrated on the sign shall be the same as the number of through lanes available to road users.
- [O] 6H.30-03 (p.809): Where two or more lanes are being shifted, a W1-4 (or W1-3) sign with an ALL LANES (W24-1cP) plaque (see Figure 6H-1) may be used instead of a sign that illustrates the number of lanes.
- [O] 6H.30-04 (p.809): Where more than three lanes are being shifted, the Reverse Curve (or Turn) sign may be rectangular.

*Also governed by Section 9C.01:*

- **[R]** 9C.01-01 (p.1065): To warn bicyclists of unexpected changes in shared-use path direction, appropriate Turn, Curve, or Large Arrow (W1-1 through W1-7) signs (see Figure 9C-1) should be used.
- **[R]** 9C.01-02 (p.1065): The W1-1 through W1-5 signs should be installed at least 50 feet in advance of the beginning of the change of alignment. Figure 9C-1. Warning Signs and Plaques and Object Markers for Bicycle Facilities (Sheet 1 of 2) * A fluorescent yellow-green background color may be used for this sign or plaque. The background color of the plaque should match the color of the warning sign that it supplements.

<a id="sec-6H-31"></a>
#### Section 6H.31 Double Reverse Curve Signs (W24-1 Series)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **W24-1** | Double Reverse Curve (1 lane) | Optional (6H.31-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
| ![W24-1a](symbols/W24-1a.png) | **W24-1a** | Double Reverse Curve (2 lanes) | Optional (6H.31-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
| ![W24-1b](symbols/W24-1b.png) | **W24-1b** | Double Reverse Curve (3 lanes) | Optional (6H.31-01) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |
|  | **W24-1cP** | All Lanes (plaque) | Optional (6H.31-01) | 24 x 18 | 30 x 24 | — | 6H-1 p.804 | — |

- [O] 6H.31-01 (p.809) ◆ W24-1, W24-1a, W24-1b: The Double Reverse Curve (W24-1, W24-1a, or W24-1b) sign (see Figure 6H-1) may be used where the tangent distance between two reverse curves is less than 600 feet, thus making it difficult for a second Reverse Curve (W1-4 series) sign to be placed between the curves. If the design speed of the curves is 30 mph or less, Double Reverse Turn signs may be used.
- **[M]** 6H.31-02 (p.809): If a Double Reverse Curve (or Turn) sign is used, the direction of the double reverse curve (or turn) shall be appropriately illustrated. Except as provided in Paragraph 3 of this Section, the number of lanes illustrated on the sign shall be the same as the number of through lanes available to road users.
- [O] 6H.31-03 (p.809) ◆ W24-1, W24-1cP: Where two or more lanes are being shifted, a W24-1 (or Double Reverse Turn sign showing one lane) sign with an ALL LANES (W24-1cP) plaque (see Figure 6H-1) may be used instead of a sign that illustrates the number of lanes.
- [O] 6H.31-04 (p.809): Where more than three lanes are being shifted, the Double Reverse Curve (or Turn) sign may be rectangular.

<a id="sec-6H-35"></a>
#### Section 6H.35 ROAD WORK NEXT XX MILES Sign (G20-1)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![G20-1](symbols/G20-1.png) | **G20-1** | Road Work Next XX Miles | Recommended (6H.35-01) | 36 x 18 | 48 x 24 | — | 6H-1 p.804 | — |

- **[R]** 6H.35-01 (p.810): The ROAD WORK NEXT XX MILES (G20-1) sign (see Figure 6H-1) should be installed in advance of TTC zones that are more than 2 miles in length.
- [O] 6H.35-02 (p.810): The ROAD WORK NEXT XX MILES sign may be mounted on a Type 3 Barricade. The sign may also be used for TTC zones of shorter length.
- **[M]** 6H.35-03 (p.810): The distance displayed on the ROAD WORK NEXT XX MILES sign shall be stated to the nearest whole mile.

<a id="sec-6H-36"></a>
#### Section 6H.36 END ROAD WORK Sign (G20-2)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![G20-2](symbols/G20-2.png) | **G20-2** | End Road Work | Optional (6H.36-02) | 36 x 18 | 48 x 24 | — | 6H-1 p.804 | — |

- **[R]** 6H.36-01 (p.810): When used, the END ROAD WORK (G20-2) sign (see Figure 6H-1) should be placed near the downstream end of the termination area, as determined by engineering judgment.
- [O] 6H.36-02 (p.810): The END ROAD WORK sign may be installed on the back of a warning sign facing the opposite direction of road users or on the back of a Type 3 Barricade.

<a id="sec-6H-37"></a>
#### Section 6H.37 PILOT CAR FOLLOW ME Sign (G20-4)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![G20-4](symbols/G20-4.png) | **G20-4** | Pilot Car Follow Me | Optional | 36 x 18 | — | — | 6H-1 p.804 | — |

- **[M]** 6H.37-01 (p.810): The PILOT CAR FOLLOW ME (G20-4) sign (see Figure 6H-1) shall be mounted in a conspicuous position on the top or on the rear of a vehicle used for guiding one-way vehicular traffic through or around a TTC zone (see Section 6E.04).

### Chapter 6I TTC Guide Signs

<a id="sec-6I-02"></a>
#### Section 6I.02 Detour Signs and Plaques (M4-8P, M4-8a, M4-8bP, M4-9, M4-9a, M4-9b, M4-9c, and M4-10)

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![M4-8a](symbols/M4-8a.png) | **M4-8a** | End Detour | Optional (6I.02-03) | 24 x 18 | 24 x 18 | — | 6I-1 p.811 | — |
| ![M4-8bP](symbols/M4-8bP.png) | **M4-8bP** | End (plaque) | Optional (6I.02-03) | 24 x 12 | 24 x 12 | — | 6I-1 p.811 | — |
| ![M4-9](symbols/M4-9.png) | **M4-9** | Detour | Optional (6I.02-03) | 30 x 24 | 48 x 36 | — | 6I-1 p.811 | — |
| ![M4-9a](symbols/M4-9a.png) | **M4-9a** | Bike/Pedestrian Detour | Optional (6I.02-03) | 30 x 24 | — | — | 6I-1 p.811 | — |
| ![M4-9b](symbols/M4-9b.png) | **M4-9b** | Pedestrian Detour | Optional (6I.02-03) | 30 x 24 | — | — | 6I-1 p.811 | — |
| ![M4-9c](symbols/M4-9c.png) | **M4-9c** | Bike Detour (with arrow) | Optional (6I.02-03) | 30 x 24 | — | — | 6I-1 p.811 | — |
| ![M4-10](symbols/M4-10.png) | **M4-10** | Detour | Optional (6I.02-03) | 48 x 18 | — | — | 6I-1 p.811 | — |

- **[M]** 6I.02-01 (p.811): Each detour shall be adequately marked with standard temporary route signs and destination signs.
- [O] 6I.02-02 (p.811): Detour signs in TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6I.02-03 (p.811) ◆ M4-10: The Detour Arrow (M4-10) sign (see Figure 6I-1) may be used where a detour route has been established.
- [O] 6I.02-04 (p.811): The DETOUR (M4-8P) plaque (see Figure 6I-1) may be mounted at the top of a route sign assembly to mark a temporary route that detours from a highway, bypasses a section closed by a TTC zone, and rejoins the highway beyond the TTC zone. Table 6I‑1. Temporary Traffic Control Zone Guide Sign and Plaque Sizes Notes: 1. Larger signs may be used wherever necessary for greater legibility or emphasis 2. Dimensions are shown in inches and are shown as width x height
- **[R]** 6I.02-05 (p.812) ◆ M4-10: The Detour Arrow (M4-10) sign should normally be mounted just below the ROAD CLOSED (R11-2, R11-3a, or R11-4) sign. The Detour Arrow sign should include a horizontal arrow pointed to the right or left as required.
- **[R]** 6I.02-06 (p.812) ◆ M4-9: The DETOUR (M4-9) sign (see Figure 6I-1) should be used for unnumbered highways, for emergency situations, for periods of short durations, or where, over relatively short distances, road users are guided along the detour and back to the desired highway without route signs.
- **[R]** 6I.02-07 (p.812) ◆ M4-9: A Street Name sign should be placed above, or the street name should be incorporated into, a DETOUR (M4-9) sign to indicate the name of the street being detoured.
- [O] 6I.02-08 (p.812) ◆ M4-8a, M4-8bP: The END DETOUR (M4-8a) sign or the END (M4-8bP) plaque (see Figure 6I-1) may be used to indicate that the detour has ended.
- **[R]** 6I.02-09 (p.812): When the END DETOUR sign is used on a numbered highway, the sign should be mounted above a route sign after the downstream end of the detour.
- **[R]** 6I.02-10 (p.812) ◆ M4-9a: The Pedestrian/Bicyclist Detour (M4-9a) sign (see Figure 6I-1) should be used where a pedestrian/bicyclist detour route has been established because of the closing of a pedestrian/bicycle facility to through traffic.
- **[M]** 6I.02-11 (p.812): If used, the Pedestrian/Bicyclist Detour sign shall have an arrow pointing in the appropriate direction.
- [O] 6I.02-12 (p.812): The arrow on a Pedestrian/Bicyclist Detour sign may be on the sign face or on a supplemental plaque.
- [O] 6I.02-13 (p.812) ◆ M4-9b, M4-9c: The Pedestrian Detour (M4-9b) sign or Bicyclist Detour (M4-9c) sign (see Figure 6I-1) may be used where a pedestrian or a bicyclist detour route (not both) has been established because of the closing of the pedestrian or bicycle facility to through traffic.

### Chapter 6L 

<a id="sec-6L-03"></a>
#### Section 6L.03 STOP/SLOW Automated Flagger Assistance Devices

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R1-7](symbols/R1-7.png) | **R1-7** | Wait on Stop | Optional | 24 x 30 | 24 x 30 | — | 6G-1 p.796 | — |
| ![R1-8](symbols/R1-8.png) | **R1-8** | Go on Slow | Optional | 24 x 30 | 24 x 30 | — | 6G-1 p.796 | — |

- **[M]** 6L.03-12 (p.828) ◆ R1-7: A WAIT ON STOP (R1-7) sign (see Figure 6L-1) shall be displayed to road users approaching the AFAD.
- [O] 6L.03-13 (p.828) ◆ R1-8: A GO ON SLOW (R1-8) sign (see Figure 6L-1) may also be displayed to road users approaching the AFAD. 14 The WAIT ON STOP/ GO ON SLOW (R1-7a) sign (see Figure 6L-1) may also be used to display both messages to approaching road users.

### Chapter 6N 

<a id="sec-6N-04"></a>
#### Section 6N.04 Work Affecting Pedestrian and Bicycle Facilities

| Sign | Code | Name | Default class | Size table | Also sized in |
|---|---|---|---|---|---|
|  | **W4-9** | Work Affecting Pedestrian and Bicycle Facilities | Optional | text | — |

- **[R]** 6N.04-16 (p.844): If a portion of a bikeway is to be closed due to construction activities and the detoured bikeway follows a complex path not in the original bikeway corridor, then a full detour plan should be developed and implemented. The TTC for the detour of the bikeway should include all necessary advance warning (W21 series) signs, detour (W4-9 series) signs, and any other TTC devices necessary to guide bicyclists along the detour route.

<a id="sec-6N-05"></a>
#### Section 6N.05 Work Outside of the Shoulder

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W21-4](symbols/W21-4.png) | **W21-4** | Slow Moving Vehicle | Recommended (6N.05-02) | 36 x 18 | — | — | 6H-1 p.804 | — |
| ![W21-8](symbols/W21-8.png) | **W21-8** | Mowing Ahead | Optional (6N.05-05) | 36 x 36 | 48 x 48 | 30 x 30 | 6H-1 p.804 | — |

- **[R]** 6N.05-02 (p.845) ◆ W21-4: Where the situations described in Paragraph 1 of this Section exist, a single warning sign, such as ROAD WORK AHEAD (W20-1), should be used. If the equipment travels on the roadway, the equipment should be equipped with appropriate flags, high-intensity rotating, flashing, oscillating, or strobe lights, and/or a SLOW MOVING VEHICLE (W21-4) sign.
- [O] 6N.05-05 (p.845) ◆ W21-8: For mowing operations, the sign MOWING AHEAD (W21-8) may be used.

<a id="sec-6N-19"></a>
#### Section 6N.19 Late Merge

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![W9-2a](symbols/W9-2a.png) | **W9-2a** | Merge Here Take Turns | Optional | 36 x 48 | 36 x 48 | — | 6H-1 p.803 | — |

- **[R]** 6N.19-03 (p.852): Static Late Merge signing should consist of the STAY IN LANE TO MERGE POINT (R9-4a) sign and the MERGE HERE TAKE TURNS (W9-2a) sign (see Figure 6N-1).

### Chapter 6P 

<a id="sec-6P-01"></a>
#### Section 6P.01 Typical Applications

| Sign | Code | Name | Default class | Conventional | Fwy/Expwy | Minimum | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![R9-12](symbols/R9-12.png) | **R9-12** | Bike Lane Closed | Optional (6P.01-04) | 24 x 12 | — | — | 6G-1 p.796 | — |
| ![W20-1b](symbols/W20-1b.png) | **W20-1b** | Path Work (with distance) | Optional (6P.01-04) | 36 x 36 | — | 30 x 30 | 6H-1 p.804 | — |
| ![W20-2a](symbols/W20-2a.png) | **W20-2a** | Bike Detour (with distance) | Optional (6P.01-04) | 36 x 36 | — | 30 x 30 | 6H-1 p.804 | — |
|  | **W20-2b** | Bike Diversion (with distance) | Optional (6P.01-04) | 36 x 36 | — | 30 x 30 | 6H-1 p.804 | — |
| ![W20-3a](symbols/W20-3a.png) | **W20-3a** | Path Closed (with distance) | Optional (6P.01-04) | 36 x 36 | — | 30 x 30 | 6H-1 p.804 | — |
| ![W20-5b](symbols/W20-5b.png) | **W20-5b** | Bike Lane Closed (with distance) | Optional (6P.01-04) | 36 x 36 | — | 30 x 30 | 6H-1 p.804 | — |

- [O] 6P.01-03 (p.857): TTC plans may deviate from the typical applications described in this Chapter to allow for conditions and requirements of a particular site or jurisdiction.
- [O] 6P.01-04 (p.857): Other devices may be added to supplement the devices and device spacing may be adjusted to provide additional reaction time or delineation. Fewer devices may be used based on field conditions.

## Part 7 School Areas

### Chapter 7B School Signs

<a id="sec-7B-02"></a>
#### Section 7B.02 School Area Signs and Plaques

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![S1-1](symbols/S1-1.png) | **S1-1** | School | Optional (7B.02-03) · *Auto* | 36 x 36 | 30 x 30 | 48 x 48 | 7B-1 p.971 | — |
|  | **S4-3P** | School | Optional | 24 x 9 | — | 36 x 12 | 7B-1 p.971 | — |
|  | **S4-7P** | All Year | Optional | 24 x 12 | — | 30 x 18 | 7B-1 p.971 | — |
|  | **S5-2** | End School Zone | Optional | 24 x 30 | — | 36 x 48 | 7B-1 p.971 | — |

- [S] 7B.02-02 (p.972) ◆ S1-1: The School (S1‑1) sign (see Figure 7B‑1) has the following four applications: A. School Area – the S1‑1 sign can be used to warn road users that they are approaching a school area that might include school buildings or grounds, a school crossing, or school related activity adjacent to the highway. B. School Zone – the S1‑1 sign can be used to identify the location of the beginning of a designated school zone. C. School Advance Crossing – if combined with an AHEAD (W16‑9P) plaque or an XX FEET (W16‑2P or W16‑2aP) plaque to comprise the School Advance Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn road users that they are approaching a crossing where schoolchildren cross the roadway (see Section 7B.03). D. School Crossing – if combined with a diagonal downward‑pointing arrow (W16‑7P) plaque to comprise the School Crossing assembly (see Figure 7B‑1), the S1‑1 sign can be used to warn approaching road users of the location of a crossing where schoolchildren cross the roadway (see Section 7B.03).
- [O] 7B.02-03 (p.972) ◆ S1-1: If a school area or school zone is located on a cross street in close proximity to the intersection, a School (S1‑1) sign with a supplemental arrow (W16‑5P or W16‑6P) plaque (see Figure 7B‑1) may be installed on each approach of the street or highway to warn road users making a turn onto the cross street that they will encounter a school area soon after making the turn.
- **[M]** 7B.02-04 (p.972) ◆ S1-1: If a school zone has been designated under State or local statute, a School (S1‑1) sign (see Figure 7B‑1) shall be installed to identify the beginning point(s) of the designated school zone (see Figure 7B‑2).
- [O] 7B.02-05 (p.972) ◆ S1-1, S4-3P: A School Zone (S1‑1) sign may be supplemented with a SCHOOL (S4‑3P) plaque (see Figure 7B‑1).
- [O] 7B.02-06 (p.972) ◆ S1-1, S4-7P: A School Zone (S1‑1) sign may be supplemented with an ALL YEAR (S4‑7P) plaque (see Figure 7B‑1) if the school operates on a 12‑month schedule.
- [O] 7B.02-07 (p.972) ◆ S5-2: The downstream end of a designated school zone may be identified with an END SCHOOL ZONE (S5‑2) sign (see Figures 7B‑1 and 7B‑2).

*Also governed by Section 7B.05:*

- **[M]** 7B.05-07 (p.980) ◆ S4-3P: The static School Speed Limit assembly shall consist of a top plaque (S4‑3P) with the legend SCHOOL, a Speed Limit (R2‑1) sign, and a bottom plaque (S4‑1P, S4‑2P, S4‑4P, or S4‑6P) indicating the specific periods of the day and/or days of the week that the special school speed limit is in effect (see Figure 7B‑1).

<a id="sec-7B-03"></a>
#### Section 7B.03 School Crossing Signs

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **R1-5a** | Yield Here to
School Crossings | Optional (7B.03-11) | 36 x 36 | — | — | 7B-1 p.971 | — |
| ![R1-5c](symbols/R1-5c.png) | **R1-5c** | Stop Here for School Crossing | Optional (7B.03-11) | 36 x 36 | — | — | 7B-1 p.971 | — |
| ![R1-9b](symbols/R1-9b.png) | **R1-9b** | Overhead School Crossing | Optional (7B.03-14) | 90 x 24 | — | — | 7B-1 p.971 | — |
| ![R1-9c](symbols/R1-9c.png) | **R1-9c** | Overhead School Crossing | Optional (7B.03-14) | 90 x 24 | — | — | 7B-1 p.971 | — |

*Also governed by Section 2B.19:*

- [S] 2B.19-01 (p.81) ◆ R1-5a, R1-5c: The R1-5 series signs are intended to mitigate the scenario that can place pedestrians at risk by blocking other drivers’ view of pedestrians and by blocking the pedestrians’ view of the vehicles approaching in the adjacent lanes.
- **[M]** 2B.19-02 (p.81) ◆ R1-5a, R1-5c: Yield Here to (Stop Here for) Pedestrians (R1-5, R1-5a, R1-5b, R1-5c, R1-5d, and R1-5e) signs (see Figure 2B-2) shall be used if yield (stop) lines are used in advance of a marked crosswalk only where it crosses an uncontrolled multi-lane approach. The Stop Here for Pedestrians signs shall only be used where the law specifically requires that a driver must stop for a pedestrian in a crosswalk. The legend STATE LAW shall not be displayed on the R1-5 series signs.
- **[R]** 2B.19-03 (p.81): If yield (stop) lines and Yield Here to (Stop Here for) Pedestrians signs are used in advance of a crosswalk that crosses an uncontrolled multi-lane approach, the signs should be placed 20 to 50 feet in advance of the nearest edge of the crosswalk (see Section 3B.19 and Figure 3B-16).
- **[M]** 2B.19-04 (p.81) ◆ R1-5a, R1-5c: When used with a School Crossing assembly within school zones (see Part 7), the R1-5a and R1-5c signs shall be used in place of the R1-5 and R1-5b signs in accordance with Paragraph 2 of this Section.
- **[M]** 2B.19-05 (p.81): When used with a Trail Crossing assembly (see Section 2C.54), the R1-5d and R1-5e signs shall be used in place of the R1-5 and R1-5b signs in accordance with Paragraph 2 of this Section.
- **[R]** 2B.19-06 (p.81): When Yield Here to (Stop Here for) Pedestrians signs are provided in advance of a crosswalk across an multi-lane approach, parking should be prohibited in the area between the yield (stop) line and the crosswalk.
- **[R]** 2B.19-07 (p.81): Yield (stop) lines and Yield Here to (Stop Here for) Pedestrians signs should not be used in advance of crosswalks that cross an approach to or departure from a roundabout.
- [O] 2B.19-08 (p.81): Yield Here to (Stop Here for) Pedestrians signs may be used in accordance with Paragraphs 2 through 4 of this Section even if yield (stop) lines are not used.
- [O] 2B.19-09 (p.81): A Pedestrian Crossing (W11-2) warning sign may be placed overhead or may be post-mounted with a diagonal downward-pointing arrow (W16-7P) plaque at the crosswalk location where Yield Here to (Stop Here for) Pedestrians signs have been installed in advance of the crosswalk.
- **[M]** 2B.19-10 (p.81): If a W11-2 sign is post-mounted at the crosswalk location where a Yield Here to (Stop Here for) Pedestrians sign is used on the approach, the Yield Here to (Stop Here for) Pedestrians sign shall not be placed on the same post as the W11-2 sign.
- [O] 2B.19-11 (p.81): An advance Pedestrian Crossing (W11-2) warning sign with an AHEAD or a distance supplemental plaque may be used in conjunction with a Yield Here to (Stop Here for) Pedestrians sign on the approach to the same crosswalk.
- [O] 2B.19-12 (p.81): In-Street Pedestrian Crossing signs and Yield Here to (Stop Here for) Pedestrians signs may be used together at the same crosswalk.

*Also governed by Section 2B.20:*

- [O] 2B.20-01 (p.81) ◆ R1-9b, R1-9c: The In-Street Pedestrian Crossing (R1-6 or R1-6a) sign (see Figure 2B-2), In-Street Trail Crossing (R1-6d or R1-6e) sign (see Figure 2B-2), the Overhead Pedestrian Crossing (R1-9 or R1-9a) sign (see Figure 2B-2), or the Overhead Trail Crossing (R1-9d or R1-9e) sign (see Figure 2B-2) may be used to remind road users of laws regarding right-of-way at an unsignalized crosswalk. The legend STATE LAW may be displayed at the top of the R1-6 series and R1-9 series signs if applicable. On the R1-6 series signs, the legends STOP or YIELD may be used instead of the appropriate STOP sign or YIELD sign symbol.
- [O] 2B.20-02 (p.81): Highway agencies may develop and apply criteria for determining the applicability of In-Street Pedestrian Crossing signs.
- **[M]** 2B.20-03 (p.83): The STOP FOR legend shall only be used in States where the State law specifically requires that a driver must stop for a pedestrian or a bicyclist in a crosswalk.
- **[M]** 2B.20-04 (p.83): If used, In-Street Pedestrian or Trail Crossing signs shall only be placed in the roadway at the crosswalk location on the center line, on a median island, on a lane line, or on an edge line.
- **[M]** 2B.20-05 (p.83): The In-Street Pedestrian or Trail Crossing sign shall not be post-mounted on the left-hand or righthand side of the roadway.
- **[M]** 2B.20-07 (p.83): If used, the Overhead Pedestrian or Trail Crossing sign shall be placed over the roadway at the crosswalk location.
- **[M]** 2B.20-08 (p.83): When used at an uncontrolled crossing, the In-Street or Overhead Pedestrian Crossing sign shall be used only as a supplement to a Pedestrian Crossing (W11-2) warning sign with a diagonal downwardpointing arrow (W16-7P) plaque at the crosswalk location.
- **[M]** 2B.20-09 (p.83): When used at an uncontrolled crossing, the In-Street or Overhead Trail Crossing sign shall be used only as a supplement to a Trail Crossing (W11-15) warning sign with a diagonal downward-pointing arrow (W16-7P) plaque at the crosswalk location.
- **[M]** 2B.20-10 (p.83): An In-Street or Overhead Pedestrian or Trail Crossing sign shall not be placed in advance of the crosswalk to educate road users about the State law prior to reaching the crosswalk, nor shall it be installed as an educational display that is not near any crosswalk.
- **[R]** 2B.20-11 (p.83): If an island (see Chapter 3J) is available, the In-Street Pedestrian or Trail Crossing sign, if used, should be placed on the island.
- [O] 2B.20-12 (p.83): In-Street Pedestrian or Trail Crossing signs may be mounted back-to-back in the median or on the center line of an undivided roadway.
- **[M]** 2B.20-13 (p.83): The In-Street Pedestrian or Trail Crossing sign and the Overhead Pedestrian Crossing or Trail sign shall not be used at crosswalks on approaches controlled by a traffic control signal, pedestrian hybrid beacon, or an emergency-vehicle hybrid beacon.
- **[M]** 2B.20-14 (p.83): Except where the In-Street Crossing sign is placed on a physical island, the sign support shall be designed to bend over and then bounce back to its normal vertical position when struck by a vehicle.
- [O] 2B.20-15 (p.83): The In-Street and Overhead Pedestrian and Trail Crossing sign may be used at intersections or midblock pedestrian crossings with flashing beacons.
- **[M]** 2B.20-17 (p.83): The top of an In-Street Pedestrian or Trail Crossing sign shall be a maximum of 4 feet above the pavement surface. The top of an In-Street Pedestrian or Trail Crossing sign placed in an island shall be a maximum of 4 feet above the island surface.
- [O] 2B.20-18 (p.83): The In-Street Pedestrian Crossing or Trail Crossing signs may be used seasonally to prevent damage in winter because of plowing operations, and may be removed at night if the pedestrian activity at night is minimal.
- [O] 2B.20-19 (p.83) ◆ R1-9b, R1-9c: Both sign mounting types, In-Street Crossing (R1-6 series) signs and Overhead Crossing (R1-9 series) signs, may be used together at the same crosswalk.

- [O] 7B.03-11 (p.976) ◆ R1-5a, R1-5c: A Yield Here To (Stop Here For) School Crossing (R1‑5a or R1‑5c) sign (see Figure 7B‑4) may be used, in accordance with the provisions of Section 2B.19, in advance of a marked crosswalk that crosses an uncontrolled multi‑lane approach within school zones.
- [O] 7B.03-14 (p.976) ◆ R1-9b, R1-9c: The Overhead School Crossing (R1‑9b or R1‑9c) sign (see Figure 7B‑1) may be used at school crossings on approaches that are not controlled by a traffic control signal, pedestrian hybrid beacon, or an emergency‑vehicle hybrid beacon. The STATE LAW legend on the R1‑9 series signs may be omitted.

<a id="sec-7B-04"></a>
#### Section 7B.04 School Bus Stop Signs

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
| ![S3-1](symbols/S3-1.png) | **S3-1** | School Bus Stop Ahead | Recommended (7B.04-01) · *Auto* | 36 x 36 | 30 x 30 | 48 x 48 | 7B-1 p.971 | — |
|  | **S3-2** | School Bus Turn Ahead | Optional (7B.04-02) | 36 x 36 | 30 x 30 | 48 x 48 | 7B-1 p.971 | — |

- **[R]** 7B.04-01 (p.978) ◆ S3-1: The School Bus Stop Ahead (S3‑1) sign (see Figure 7B‑1) should be installed in advance of locations where a school bus, when stopped to pick up or discharge passengers, is not visible to road users for an adequate distance and where there is no opportunity to relocate the school bus stop to provide adequate sight distance.
- [O] 7B.04-02 (p.978) ◆ S3-2: The SCHOOL BUS TURN AHEAD (S3‑2) sign (see Figure 7B‑1) may be installed in advance of locations where a school bus turns around on a roadway at a location not visible to approaching road users for a distance as determined by the “0” column under Condition B of Table 2C‑3, and where there is no opportunity to relocate the school bus turn around to provide the distance provided in Table 2C‑3.

<a id="sec-7B-05"></a>
#### Section 7B.05 School Speed Limit Signs and Plaques

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **S4-4P** | When Flashing | Mandatory (7B.05-08) | 24 x 12 | — | 36 x 18 | 7B-1 p.971 | — |
|  | **S4-5** | Reduced School Speed | Mandatory (7B.05-01) | 36 x 36 | 30 x 30 | 48 x 48 | 7B-1 p.971 | — |
|  | **S4-5a** | Reduced School Speed | Recommended (7B.05-13) | 36 x 36 | 30 x 30 | 48 x 48 | 7B-1 p.971 | — |
|  | **S4-6P** | Days of Week | Optional | 24 x 12 | — | 36 x 18 | 7B-1 p.971 | — |
|  | **S5-1** | School Speed Limit XX | Mandatory (7B.05-01) | 24 x 48 | — | 36 x 72 | 7B-1 p.971 | — |
|  | **S5-3** | End School Speed Limit | Optional (7B.05-04) | 24 x 30 | — | 36 x 48 | 7B-1 p.971 | — |

- **[M]** 7B.05-01 (p.978) ◆ S5-1: A School Speed Limit assembly (see Figure 7B‑1) or a School Speed Limit When Flashing (S5‑1) sign (see Figure 7B‑1) shall be used to indicate the speed limit where a reduced school speed limit zone has been established based upon an engineering study or where a reduced school speed limit is specified for such areas by statute. The School Speed Limit assembly or School Speed Limit When Flashing sign shall be placed at or as near as practicable to the point where the reduced school speed limit zone begins (see Figures 7B‑2 and 7B‑4).
- **[M]** 7B.05-02 (p.978) ◆ S5-1: If a reduced school speed limit zone has been established, a School (S1‑1) sign shall be installed in advance (see Table 2C‑3 for advance placement guidelines) of the first School Speed Limit sign assembly or S5‑1 sign that is encountered in each direction as traffic approaches the reduced school speed limit zone (see Figures 7B‑2 and 7B‑4).
- **[M]** 7B.05-03 (p.978) ◆ S5-3: Except as provided in Paragraph 4 of this Section, the downstream end of an authorized and posted reduced school speed limit zone shall be identified with an END SCHOOL SPEED LIMIT (S5‑3) sign (see Figures 7B‑1, 7B‑2, and 7B‑4).
- [O] 7B.05-04 (p.978) ◆ S5-3: If a reduced school speed limit zone ends at the same point as a designated school zone (see Section 7B.02), an END SCHOOL ZONE (S5‑2) sign may be used instead of an END SCHOOL SPEED LIMIT (S5‑3) sign. A standard Speed Limit sign showing the speed limit for the section of highway that is downstream from the authorized and posted reduced school speed limit zone may be mounted on the same post above the END SCHOOL SPEED LIMIT (S5‑3) sign or the END SCHOOL ZONE (S5‑2) sign.
- **[R]** 7B.05-05 (p.978): The beginning point of a reduced school speed limit zone should be at least 200 feet in advance of the school grounds or a school crossing; however, this 200‑foot distance should be increased if the reduced school speed limit is 30 mph or higher. The maximum beginning point of a reduced school speed limit zone should not be greater than 500 feet in advance of the school grounds or a school crossing.
- **[M]** 7B.05-06 (p.978): The School Speed Limit assembly shall be either a static sign assembly, a blank‑out sign, or a changeable message sign (see Chapter 2L).
- **[M]** 7B.05-07 (p.980) ◆ S4-4P, S4-6P: The static School Speed Limit assembly shall consist of a top plaque (S4‑3P) with the legend SCHOOL, a Speed Limit (R2‑1) sign, and a bottom plaque (S4‑1P, S4‑2P, S4‑4P, or S4‑6P) indicating the specific periods of the day and/or days of the week that the special school speed limit is in effect (see Figure 7B‑1).
- **[M]** 7B.05-08 (p.980) ◆ S4-4P, S5-1: When a School Speed Limit When Flashing (S5‑1) sign or a Speed Limit (R2‑1) sign with a supplemental WHEN FLASHING (S4‑4P) plaque is used, a Speed Limit Sign Beacon (see Section 4S.04) shall be used to identify the periods that the school speed limit is in effect.
- **[M]** 7B.05-09 (p.980): Fluorescent yellow‑green pixels shall be used when the “SCHOOL” message is displayed on a changeable message sign for a school speed limit.
- [O] 7B.05-10 (p.980): Changeable message signs may use blank‑out messages or other methods in order to display the school speed limit only during the periods it applies.
- [O] 7B.05-11 (p.980) ◆ S5-1: A Vehicle Speed Feedback (W13‑20aP) plaque that displays the speed of approaching drivers (see Sections 2B.21 and 2C.13), that is part of a School Speed Limit assembly or a School Speed Limit When Flashing (S5‑1) sign, may be used in a school speed limit zone.
- **[R]** 7B.05-12 (p.980): If used, the Vehicle Speed Feedback (W13‑20aP) plaque should only be used during the time period when the school speed limit is in effect.
- **[R]** 7B.05-13 (p.980) ◆ S4-5a: A Reduced School Speed Limit Ahead (S4‑5or S4‑5a) sign (see Figure 7B‑1) should be used to inform road users of a reduced speed zone where the speed limit is being reduced by more than 10 mph, or where engineering judgment indicates that advance notice would be appropriate.
- **[M]** 7B.05-14 (p.980): If used, the Reduced School Speed Limit Ahead sign shall be followed by a School Speed Limit sign or a School Speed Limit assembly.
- **[M]** 7B.05-15 (p.980): The speed limit displayed on the Reduced School Speed Limit Ahead sign shall be identical to the speed limit displayed on the subsequent School Speed Limit sign or School Speed Limit assembly.

*Also governed by Section 7B.06:*

- [O] 7B.06-06 (p.980) ◆ S4-4P: Where appropriate, one of the following plaques may be mounted below the sign that identifies the beginning point of the higher fines zone: A. A S4‑1P plaque (see Figure 7B‑1) specifying the times that the higher fines are in effect, B. A WHEN CHILDREN ARE PRESENT (S4‑2P) plaque (see Figure 7B‑1), or C. A WHEN FLASHING (S4‑4P) plaque (see Figure 7B‑1) if used in conjunction with a yellow flashing beacon.

<a id="sec-7B-06"></a>
#### Section 7B.06 Higher Fines Zone Signs and Plaques in School Areas

| Sign | Code | Name | Default class | Conventional | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|
|  | **S4-1P** | X:XX to X:XX AM | Optional | 24 x 12 | — | 36 x 18 | 7B-1 p.971 | — |
|  | **S4-2P** | When Children Are Present | Optional | 24 x 12 | — | 36 x 18 | 7B-1 p.971 | — |

- [O] 7B.06-06 (p.980): Where appropriate, one of the following plaques may be mounted below the sign that identifies the beginning point of the higher fines zone: A. A S4‑1P plaque (see Figure 7B‑1) specifying the times that the higher fines are in effect, B. A WHEN CHILDREN ARE PRESENT (S4‑2P) plaque (see Figure 7B‑1), or C. A WHEN FLASHING (S4‑4P) plaque (see Figure 7B‑1) if used in conjunction with a yellow flashing beacon.

## Part 8 Railroad and Light Rail Grade Crossings

### Chapter 8B Grade Crossing Signs and Markings

<a id="sec-8B-03"></a>
#### Section 8B.03 Grade Crossing (Crossbuck) Sign (R15-1) and Number of Tracks Plaque (R15-2P) at Active and Passive Grade Crossings

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R15-1](symbols/R15-1.png) | **R15-1** | Grade Crossing (Crossbuck) | Mandatory (8B.03-03) · *Auto* | 48 x 9 | 48 x 9 | — | — | — | 8B-1 p.994 | — |
| ![R15-2P](symbols/R15-2P.png) | **R15-2P** | Number of Tracks (plaque) | Mandatory (8B.03-03) · *Auto* | 27 x 18 | 27 x 18 | — | — | — | 8B-1 p.994 | — |

- **[M]** 8B.03-01 (p.993) ◆ R15-1: The Grade Crossing (R15-1) sign (see Figure 8B-1), commonly identified as the Crossbuck sign, shall be retroreflective white with the words RAILROAD CROSSING in black lettering, mounted as shown in Figure 8B-2.
- **[M]** 8B.03-03 (p.993): As a minimum, one Crossbuck sign shall be used on each highway approach to every highway-rail grade crossing, alone or in combination with other traffic control devices.
- **[M]** 8B.03-04 (p.993): As a minimum, one Crossbuck sign shall be used on each highway approach to every highway-LRT grade crossing where flashing-light signals or automatic gates are used, alone or in combination with other traffic control devices.
- [O] 8B.03-05 (p.993): A Crossbuck sign may be used on a highway approach to a highway-LRT grade crossing where flashing-light signals or automatic gates are not used, alone or in combination with other traffic control devices.
- **[M]** 8B.03-06 (p.993) ◆ R15-2P: If there are two or more tracks at a grade crossing, the number of tracks shall be indicated on a supplemental Number of Tracks (R15-2P) plaque (see Figure 8B-1) of inverted T shape mounted below the Crossbuck sign in the manner shown in Figure 8B-2.
- **[M]** 8B.03-07 (p.993): On each approach to a highway-rail grade crossing and, if used, on each approach to a highwayLRT grade crossing, the Crossbuck sign shall be installed on the right-hand side of the highway on each approach to the grade crossing. Where restricted sight distance or unfavorable highway geometry exists on an approach to a grade crossing, or where there is a one-way multi-lane approach, an additional Crossbuck sign shall be installed on the left-hand side of the highway, possibly placed back-to-back with the Crossbuck sign for the opposite approach, or otherwise located so that two Crossbuck signs are displayed for that approach.
- **[M]** 8B.03-08 (p.993): A strip of retroreflective white material not less than 2 inches in width shall be used on the back of each blade of each Crossbuck sign for the length of each blade at all passive grade crossings, except those where Crossbuck signs have been installed back-to-back or where double-faced Crossbuck signs have been installed.
- [O] 8B.03-09 (p.993): A strip of retroreflective white material not less than 2 inches in width may be used on the back of each blade of each Crossbuck sign for the length of each blade at active grade crossings. Month 2023December 2023 Table 8B-1. Grade Crossing Sign and Plaque Minimum Sizes (Sheet 1 of 2) DecemberMonth 2023
- **[R]** 8B.03-10 (p.995): Minimum clearance dimensions for crossbuck signs relative to the proximity to the nearest rail should conform to the requirements of the railroad company and/or transit agency, and the regulatory agency with statutory authority (if applicable).
- **[R]** 8B.03-11 (p.995): Except as provided in Paragraph 12 of this Section, the mounting height of Crossbuck signs, measured vertically from the center of the sign to the elevation of the near edge of the pavement, should be approximately 9 feet (see Figure 8B-2).
- [O] 8B.03-12 (p.995): The 9-foot mounting height for the Crossbuck sign may be varied as required by local conditions and may be increased to accommodate signs mounted below the Crossbuck sign.

<a id="sec-8B-06"></a>
#### Section 8B.06 Grade Crossing Advance Warning Signs (W10-1 through W10-4)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-1](symbols/W10-1.png) | **W10-1** | Grade Crossing Advance Warning | Mandatory (8B.06-01) · *Auto* | 36 Dia. | 36 Dia. | 48 Dia. | — | 48 Dia. | 8B-1 p.994 | 9A-1 |
| ![W10-2](symbols/W10-2.png) | **W10-2** | Grade Crossing and Intersection Advance Warning | Mandatory (8B.06-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |
| ![W10-3](symbols/W10-3.png) | **W10-3** | Grade Crossing and Intersection | Mandatory (8B.06-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |
| ![W10-4](symbols/W10-4.png) | **W10-4** | Grade Crossing and Intersection | Mandatory (8B.06-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |
| ![W10-21](symbols/W10-21.png) | **W10-21** | Busway Crossing | Mandatory (8B.06-01) | 36x36 | 36x36 | 48x48 | — | 48x48 | 8B-1 p.995 | — |
| ![W10-21aP](symbols/W10-21aP.png) | **W10-21aP** | Signal Ahead (plaque) | Mandatory (8B.06-01) | 30x24 | 30x24 | — | — | — | 8B-1 p.995 | — |

- **[M]** 8B.06-01 (p.1001) ◆ W10-1, W10-2, W10-3, W10-4: A Grade Crossing Advance Warning (W10-1) sign (see Figure 8B-4) shall be used on each highway in advance of every grade crossing, except in the following circumstances: A. On an approach to a grade crossing from an intersection with a parallel highway if the distance from the nearest rail of the tracks to the edge of the parallel roadway is less than 100 feet and W10-2, W10-3, or W10-4 signs are used on the approaches of the parallel highway (see Paragraph 5 of this Section); B. On low-volume, low-speed highways crossing minor spurs or other tracks that are infrequently used and road users are directed by an authorized person on the ground to not enter the crossing at all times that approaching rail traffic is about to occupy the crossing; C. In business or commercial areas where active grade crossing traffic control systems are in use; D. Where physical conditions do not permit even a partially effective display of the sign; or E. At highway-LRT grade crossings where Crossbuck signs are not used (see Section 8B.03).
- **[M]** 8B.06-02 (p.1001): The placement of the Grade Crossing Advance Warning sign shall be in accordance with Section 2C.04 and Table 2C-3.
- **[M]** 8B.06-03 (p.1001) ◆ W10-1: If a YIELD or STOP sign is present at a passive grade crossing, a Yield Ahead (W3-2) or Stop Ahead (W3-1) Advance Warning sign shall also be installed if the criteria for their installation given in Section 2C.35 is met. If a Yield Ahead or Stop Ahead sign is installed on the approach to the crossing, the W10-1 sign shall be installed upstream from the Yield Ahead or Stop Ahead sign. The Yield Ahead or Stop Ahead sign shall be located in accordance with Table 2C-3. The minimum distance between the signs shall be in accordance with Section 2C.04 and Table 2C-3.
- [O] 8B.06-04 (p.1001) ◆ W10-1: On divided highways and one-way streets, an additional W10-1 sign may be installed on the left-hand side of the roadway.
- **[M]** 8B.06-05 (p.1001) ◆ W10-1, W10-2, W10-3, W10-4: If the distance between the tracks and a parallel highway, from the nearest rail of the tracks to the edge of the parallel roadway, is less than 100 feet, a W10-2, W10-3, or W10-4 sign (see Figure 8B-4) shall be installed on each approach of the parallel highway to warn road users making a turn that they will encounter a grade crossing soon after making a turn, and a W10-1 sign for the approach to the tracks shall not be required to be between the tracks and the parallel highway.
- **[M]** 8B.06-06 (p.1001) ◆ W10-2, W10-3, W10-4: If the W10-2, W10-3, or W10-4 sign is used, sign placement in accordance with the guidelines for Intersection Warning signs in Table 2C-3 using the speed of through traffic shall be measured from the highway intersection. Month 2023December 2023
- **[R]** 8B.06-07 (p.1002) ◆ W10-1, W10-2, W10-3, W10-4: If the distance between the tracks and the parallel highway, from the nearest rail of the tracks to the edge of the parallel roadway, is 100 feet or more, a W10-1 sign should be installed in advance of the grade crossing, and the W10-2, W10-3, or W10-4 sign should not be used on the parallel highway.

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-8B-07"></a>
#### Section 8B.07 DO NOT STOP ON TRACKS Sign (R8-8)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R8-8](symbols/R8-8.png) | **R8-8** | Do Not Stop on Tracks | Recommended (8B.07-01) | 24 x 30 | 24 x 30 | 36 x 48 | — | 36 x 48 | 8B-1 p.994 | — |

*Also governed by Section 2B.52:*

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

- **[R]** 8B.07-01 (p.1002): If motor vehicle queues are likely to extend onto the tracks, a DO NOT STOP ON TRACKS (R8-8) sign (see Figure 8B-1) should be used.
- **[R]** 8B.07-03 (p.1002): The R8-8 sign, if used, should be located on the right-hand side of the highway on either the near or far side of the grade crossing, depending upon which position provides better visibility to approaching drivers.
- [O] 8B.07-04 (p.1002): DO NOT STOP ON TRACKS signs may be placed on both sides of the track.
- [O] 8B.07-05 (p.1002): On divided highways and one-way streets, a second DO NOT STOP ON TRACKS sign may be placed on the near or far left-hand side of the highway at the grade crossing to further improve the visibility of the sign. DecemberMonth 2023

<a id="sec-8B-08"></a>
#### Section 8B.08 TRACKS OUT OF SERVICE Sign (R8-9)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R8-9](symbols/R8-9.png) | **R8-9** | Tracks Out of Service | Optional (8B.08-01) | 24 x 24 | 24 x 24 | 36 x 36 | — | 36 x 36 | 8B-1 p.994 | — |

*Also governed by Section 2B.52:*

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

- [O] 8B.08-01 (p.1003): The TRACKS OUT OF SERVICE (R8-9) sign (see Figure 8B-1) may be used at a grade crossing instead of a Crossbuck (R15-1) sign and a Number of Tracks (R15-2P) plaque or instead of a Crossbuck Assembly where railroad or LRT tracks have been temporarily or permanently abandoned, but only until such time that the tracks are removed or covered.
- **[M]** 8B.08-02 (p.1003): Where tracks are out of service, except as provided in Paragraphs 3 and 4 of this Section, traffic control devices and gate arms shall be removed and the signal heads shall be removed or hooded or turned from view to clearly indicate that they are not in operation.
- **[M]** 8B.08-03 (p.1003): Where tracks are out of service, even if a TRACKS OUT OF SERVICE (R8-9) sign has been installed, an Emergency Notification System (I13-1) sign (see Section 8B.27) shall be retained at the grade crossing and shall be visible to road users.
- **[R]** 8B.08-04 (p.1003): Warning signs, such as the Low Ground Clearance Grade Crossing (W10-5) sign and the Skewed Crossing (W10-12) sign, that warn road users about physical roadway conditions at the grade crossing should be left in place after the tracks are taken out of service, until the physical condition is no longer present..
- **[M]** 8B.08-05 (p.1003): The R8-9 sign shall be removed when the tracks have been removed or paved over or when the grade crossing is returned to service. The Emergency Notification System (I13-1) sign shall be removed when the tracks have been removed or paved over.

<a id="sec-8B-09"></a>
#### Section 8B.09 STOP HERE WHEN FLASHING Signs (R8-10 and R8-10a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R8-10](symbols/R8-10.png) | **R8-10** | Stop Here When Flashing | Optional (8B.09-01) | 24 x 36 | 24 x 36 | — | — | 36 x 48 | 8B-1 p.994 | — |
| ![R8-10a](symbols/R8-10a.png) | **R8-10a** | Stop Here When Flashing | Optional (8B.09-01) | 24 x 30 | 24 x 30 | — | — | 36 x 42 | 8B-1 p.994 | — |

*Also governed by Section 2B.52:*

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

- [O] 8B.09-01 (p.1003): The STOP HERE WHEN FLASHING (R8-10 and R8-10a) signs (see Figure 8B-1) may be used at a grade crossing to inform drivers of the location of the stop line or the point at which to stop when the flashing-light signals (see Section 8D.02) are activated.

<a id="sec-8B-11"></a>
#### Section 8B.11 EXEMPT Grade Crossing Plaques (R15-3P and W10-1aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R15-3P](symbols/R15-3P.png) | **R15-3P** | Exempt (plaque) | Optional (8B.11-01) | 24 x 12 | 24 x 12 | — | — | — | 8B-1 p.994 | — |
| ![W10-1aP](symbols/W10-1aP.png) | **W10-1aP** | Exempt (plaque) | Optional (8B.11-01) | 24 x 12 | 24 x 12 | — | — | — | 8B-1 p.994 | — |

*Also governed by Section 8B.06:*

- **[M]** 8B.06-01 (p.1001): A Grade Crossing Advance Warning (W10-1) sign (see Figure 8B-4) shall be used on each highway in advance of every grade crossing, except in the following circumstances: A. On an approach to a grade crossing from an intersection with a parallel highway if the distance from the nearest rail of the tracks to the edge of the parallel roadway is less than 100 feet and W10-2, W10-3, or W10-4 signs are used on the approaches of the parallel highway (see Paragraph 5 of this Section); B. On low-volume, low-speed highways crossing minor spurs or other tracks that are infrequently used and road users are directed by an authorized person on the ground to not enter the crossing at all times that approaching rail traffic is about to occupy the crossing; C. In business or commercial areas where active grade crossing traffic control systems are in use; D. Where physical conditions do not permit even a partially effective display of the sign; or E. At highway-LRT grade crossings where Crossbuck signs are not used (see Section 8B.03).
- **[M]** 8B.06-02 (p.1001): The placement of the Grade Crossing Advance Warning sign shall be in accordance with Section 2C.04 and Table 2C-3.
- **[M]** 8B.06-03 (p.1001): If a YIELD or STOP sign is present at a passive grade crossing, a Yield Ahead (W3-2) or Stop Ahead (W3-1) Advance Warning sign shall also be installed if the criteria for their installation given in Section 2C.35 is met. If a Yield Ahead or Stop Ahead sign is installed on the approach to the crossing, the W10-1 sign shall be installed upstream from the Yield Ahead or Stop Ahead sign. The Yield Ahead or Stop Ahead sign shall be located in accordance with Table 2C-3. The minimum distance between the signs shall be in accordance with Section 2C.04 and Table 2C-3.
- [O] 8B.06-04 (p.1001): On divided highways and one-way streets, an additional W10-1 sign may be installed on the left-hand side of the roadway.
- **[M]** 8B.06-05 (p.1001): If the distance between the tracks and a parallel highway, from the nearest rail of the tracks to the edge of the parallel roadway, is less than 100 feet, a W10-2, W10-3, or W10-4 sign (see Figure 8B-4) shall be installed on each approach of the parallel highway to warn road users making a turn that they will encounter a grade crossing soon after making a turn, and a W10-1 sign for the approach to the tracks shall not be required to be between the tracks and the parallel highway.
- **[M]** 8B.06-06 (p.1001): If the W10-2, W10-3, or W10-4 sign is used, sign placement in accordance with the guidelines for Intersection Warning signs in Table 2C-3 using the speed of through traffic shall be measured from the highway intersection. Month 2023December 2023
- **[R]** 8B.06-07 (p.1002): If the distance between the tracks and the parallel highway, from the nearest rail of the tracks to the edge of the parallel roadway, is 100 feet or more, a W10-1 sign should be installed in advance of the grade crossing, and the W10-2, W10-3, or W10-4 sign should not be used on the parallel highway.

- [O] 8B.11-01 (p.1003): Where authorized by law or regulation, an EXEMPT (R15-3P) plaque (see Figure 8B-1) with a white background may be used below the Crossbuck sign or Number of Tracks plaque, if present, at the grade crossing, and an EXEMPT (W10-1aP) plaque (see Figure 8B-4) with a yellow background may be used below the Grade Crossing Advance Warning (W10-1 through W10-4) sign.
- [O] 8B.11-02 (p.1003) ◆ R15-3P: Where neither the Crossbuck sign nor the advance warning signs exist for a particular highway-LRT grade crossing, an EXEMPT (R15-3P) plaque with a white background may be placed on its own post on the near righthand side of the approach to the crossing.

<a id="sec-8B-12"></a>
#### Section 8B.12 Light Rail Transit Only Lane Signs (R15-4 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **R15-4** | Light Rail Transit Only Lane Signs | Optional (8B.12-02) | — | — | — | — | — | text | — |
| ![R15-4a](symbols/R15-4a.png) | **R15-4a** | Light Rail Only Right Lane | Optional (8B.12-02) | 24 x 30 | 24 x 30 | — | — | — | 8B-1 p.994 | — |
| ![R15-4b](symbols/R15-4b.png) | **R15-4b** | Light Rail Only Left Lane | Optional (8B.12-02) | 24 x 30 | 24 x 30 | — | — | — | 8B-1 p.994 | — |
| ![R15-4c](symbols/R15-4c.png) | **R15-4c** | Light Rail Only Center Lane | Optional (8B.12-02) | 24 x 30 | 24 x 30 | — | — | — | 8B-1 p.994 | — |

- [S] 8B.12-01 (p.1004): The Light Rail Transit Only Lane (R15-4 series) signs (see Figure 8B-1) are used for multi-lane operations, where road users might need additional guidance on lane use and/or restrictions.
- [O] 8B.12-02 (p.1004): Light Rail Transit Only Lane signs may be used on a roadway lane limited to only LRT use to indicate the restricted use of a lane in semi-exclusive and mixed alignments.
- **[R]** 8B.12-03 (p.1004) ◆ R15-4a, R15-4b, R15-4c: If used, the R15-4a, R15-4b, and R15-4c signs should be installed on posts adjacent to the roadway containing the LRT tracks or overhead above the LRT only lane.
- [O] 8B.12-04 (p.1004): If the trackway is paved, preferential lane markings (see Chapter 3E) may be installed, but only in combination with Light Rail Transit Only Lane signs.

<a id="sec-8B-13"></a>
#### Section 8B.13 Do Not Pass Light Rail Transit Signs (R15-5 and R15-5a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R15-5](symbols/R15-5.png) | **R15-5** | Light Rail Do Not Pass (symbol) | Optional (8B.13-02) | 24 x 30 | 24 x 30 | — | — | — | 8B-1 p.994 | — |
| ![R15-5a](symbols/R15-5a.png) | **R15-5a** | Do Not Pass Stopped Train | Optional (8B.13-02) | 24 x 30 | 24 x 30 | — | — | — | 8B-1 p.994 | — |

- [S] 8B.13-01 (p.1004) ◆ R15-5: A Do Not Pass Light Rail Transit (R15-5) sign (see Figure 8B-1) is used to indicate that motor vehicles are not allowed to pass LRT vehicles that are loading or unloading passengers where there is no raised platform or physical separation from the lanes upon which other motor vehicles are operating.
- [O] 8B.13-02 (p.1004) ◆ R15-5: The R15-5 sign may be used in mixed-use alignments and may be mounted overhead where there are multiple lanes.
- [O] 8B.13-03 (p.1004): Instead of the R15-5 symbol sign, a regulatory sign with the word message DO NOT PASS STOPPED TRAIN (R15-5a) may be used (see Figure 8B-1).
- **[R]** 8B.13-04 (p.1004): If used, the R15-5 or R15-5a sign should be located immediately before the LRT boarding area.

<a id="sec-8B-14"></a>
#### Section 8B.14 No Motor Vehicles on Tracks Signs (R15-6 and R15-6a)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R15-6](symbols/R15-6.png) | **R15-6** | No Motor Vehicles On Tracks | Recommended (8B.14-02) | 24 x 24 | 24 x 24 | — | — | — | 8B-1 p.994 | — |
| ![R15-6a](symbols/R15-6a.png) | **R15-6a** | Do Not Drive On Tracks | Recommended (8B.14-02) | 24 x 30 | 24 x 30 | — | — | — | 8B-1 p.994 | — |

- [S] 8B.14-01 (p.1004) ◆ R15-6: The No Motor Vehicles On Tracks (R15-6) sign (see Figure 8B-1) is used where there are adjacent traffic lanes separated from the LRT lane by a curb or pavement markings.
- **[R]** 8B.14-02 (p.1004): The DO NOT ENTER (R5-1) sign should be used where a road user could wrongly enter an LRT only street.
- [O] 8B.14-03 (p.1004): A No Motor Vehicles On Tracks sign may be used to deter motor vehicles from driving on the trackway. It may be installed on a 3-foot flexible post between double tracks, on a post alongside the tracks, or overhead.
- [O] 8B.14-04 (p.1004): Instead of the R15-6 symbol sign, a regulatory sign with the word message DO NOT DRIVE ON TRACKS (R15-6a) may be used (see Figure 8B-1).
- [O] 8B.14-05 (p.1004) ◆ R15-6: A reduced size of 12 x 12 inches may be used if the R15-6 sign is installed between double tracks.
- **[M]** 8B.14-06 (p.1004) ◆ R15-6: The smallest size for the R15-6 sign shall be 12 x 12 inches.

<a id="sec-8B-15"></a>
#### Section 8B.15 Divided Highway with Light Rail Transit Crossing Signs (R15-7 Series)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R15-7](symbols/R15-7.png) | **R15-7** | Light Rail Divided | Optional (8B.15-01) | 24 x 24 | 24 x 24 | — | — | — | 8B-1 p.994 | — |
| ![R15-7a](symbols/R15-7a.png) | **R15-7a** | Light Rail Divided Highway | Optional (8B.15-01) | 24 x 24 | 24 x 24 | — | — | — | 8B-1 p.994 | — |

- [O] 8B.15-01 (p.1004): The Divided Highway with Light Rail Transit Crossing (R15-7 or R15-7a) sign (see Figure 8B-1) may be used as a supplemental sign on the approach legs of a roadway that intersects with a divided highway where LRT equipment operates in the median. The sign may be placed beneath a STOP sign or mounted separately.
- **[R]** 8B.15-02 (p.1004): The number of tracks displayed on the R15-7 or R15-7a sign should be the same as the actual number of tracks. DecemberMonth 2023
- **[M]** 8B.15-03 (p.1005): When the Divided Highway with Light Rail Transit Crossing sign is used at a four-leg intersection, the R15-7 sign shall be used. When used at a T-intersection, the R15-7a sign shall be used.

<a id="sec-8B-16"></a>
#### Section 8B.16 Low Ground Clearance Grade Crossing Sign (W10-5)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **W10-5** | Low Ground Clearance (symbol) | Recommended (8B.16-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |
|  | **W10-5P** | Low Ground Clearance (plaque) | Optional | 30 x 24 | 30 x 24 | — | — | — | 8B-1 p.994 | — |

- **[R]** 8B.16-01 (p.1005) ◆ W10-5: If the highway profile conditions are sufficiently abrupt to create a hang-up situation for long wheelbase vehicles or for trailers with low ground clearance, the Low Ground Clearance Grade Crossing (W10-5) sign (see Figure 8B-4) should be installed in advance of the grade crossing.
- **[M]** 8B.16-02 (p.1005): Because this symbol might not be readily recognizable by the public, the Low Ground Clearance Grade Crossing (W10-5) warning sign shall be accompanied by a LOW GROUND CLEARANCE (W10-5P) educational plaque. The LOW GROUND CLEARANCE educational plaque shall remain in place for at least 3 years after the initial installation of the W10-5 sign (see Section 2A.09).
- **[R]** 8B.16-03 (p.1005) ◆ W10-5: Because other vehicle types and combinations also face the potential risk of hanging up at a grade crossing, word message warning signs and selective exclusion regulatory signs (see Section 2B.45) for specific vehicle types and combinations should be used in addition to, or in place of, the Low Ground Clearance Grade Crossing (W10-5) sign.
- **[R]** 8B.16-05 (p.1005) ◆ W10-5: Auxiliary plaques such as AHEAD, NEXT CROSSING, or USE NEXT CROSSING (with appropriate arrows), or a supplemental distance plaque should be placed below the W10-5 sign at the nearest intersecting highway where a vehicle can detour or at a point on the highway wide enough to permit a U-turn.
- **[R]** 8B.16-06 (p.1005): If engineering judgment of roadway geometric and operating conditions confirms that motor vehicle speeds across the tracks should be below the posted speed limit, a W13-1P advisory speed plaque should be posted.
- **[R]** 8B.16-07 (p.1005): A signed detour should be installed to guide potential hang-up vehicles to alternate nearby crossings to avoid the potential hang-up condition.

<a id="sec-8B-17"></a>
#### Section 8B.17 Light Rail Transit Approaching-Activated Blank-Out Warning Sign (W10-7)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **W10-7** | Light Rail Activated | Optional (8B.17-02) | 24 x 24 | 24 x 24 | — | — | — | 8B-1 p.994 | — |

- [S] 8B.17-01 (p.1005): The Light Rail Transit Approaching-Activated Blank-Out (W10-7) warning sign (see Figure 8B-4) supplements the traffic control devices to warn road users crossing the tracks of approaching LRT equipment.
- [O] 8B.17-02 (p.1005): A Light Rail Transit Approaching-Activated Blank-Out warning sign may be used at signalized intersections near highway-LRT grade crossings or at crossings controlled by STOP signs or automatic gates.
- [S] 8B.17-03 (p.1005): The provisions contained in Chapter 2L for blank-out signs are applicable to the W10-7 sign.

<a id="sec-8B-18"></a>
#### Section 8B.18 Another Train Coming Sign (W10-16)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-16](symbols/W10-16.png) | **W10-16** | Another Train Coming | Optional (8B.18-03) | 30 x 30 | 30 x 30 | — | — | — | 8B-1 p.995 | — |

- **[R]** 8B.18-02 (p.1006): The decision to provide notification of another train should be made by a Diagnostic Team. In making this determination, the Diagnostic Team should consider the pedestrian usage, pedestrian collision history, train speeds and volumes, operating plans and/or schedules, and the presence of a nearby station or transit center.
- [O] 8B.18-03 (p.1006): An ANOTHER TRAIN COMING (W10-16) train-activated blank-out sign (see Figure 8B-4) may be used to provide notification of another train coming. For added sign conspicuity, a Warning Beacon may be used in accordance with the requirements of Section 4S.03.

<a id="sec-8B-19"></a>
#### Section 8B.19 TRAINS MAY EXCEED 80 MPH Sign (W10-8)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-8](symbols/W10-8.png) | **W10-8** | Trains May Exceed 80 MPH | Recommended (8B.19-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |

- **[R]** 8B.19-01 (p.1006): Where trains are permitted to travel at speeds exceeding 80 mph, a TRAINS MAY EXCEED 80 MPH (W10-8) sign (see Figure 8B-4) should be installed facing road users approaching the highway-rail grade crossing.
- **[R]** 8B.19-02 (p.1006): If used, the TRAINS MAY EXCEED 80 MPH signs should be installed between the Grade Crossing Advance Warning (W10-1 through W10-4) sign (see Figure 8B-4) and the highway-rail grade crossing on all approaches to the highway-rail grade crossing. The locations should be determined based on specific site conditions.

<a id="sec-8B-20"></a>
#### Section 8B.20 NO TRAIN HORN Sign or Plaque (W10-9 and W10-9P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-9](symbols/W10-9.png) | **W10-9** | No Train Horn | Mandatory (8B.20-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |
| ![W10-9P](symbols/W10-9P.png) | **W10-9P** | No Train Horn (plaque) | Mandatory (8B.20-01) | 30 x 24 | 30 x 24 | — | — | — | 8B-1 p.994 | 9A-1 |

- **[M]** 8B.20-01 (p.1006): Either a NO TRAIN HORN (W10-9) sign (see Figure 8B-4) or a NO TRAIN HORN (W10-9P) plaque (see Figure 8B-4) shall be installed in each direction at each highway-rail grade crossing where a Quiet Zone has been established in compliance with 49 CFR Part 222. If a W10-9P plaque is used, it shall supplement and be mounted directly below the Grade Crossing Advance Warning (W10-1 through W10-4) sign (see Figure 8B-4).

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-8B-21"></a>
#### Section 8B.21 Storage Space Signs (W10-11, W10-11a, and W10-11b)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-11](symbols/W10-11.png) | **W10-11** | Storage Space (symbol) | Recommended (8B.21-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | — |
| ![W10-11a](symbols/W10-11a.png) | **W10-11a** | Storage Space XX Feet | Recommended (8B.21-01) | 30 x 36 | 30 x 36 | — | — | — | 8B-1 p.994 | — |
| ![W10-11b](symbols/W10-11b.png) | **W10-11b** | Storage Space XX Feet between | Recommended (8B.21-01) | 30 x 36 | 30 x 36 | — | — | — | 8B-1 p.994 | — |

- **[R]** 8B.21-01 (p.1006) ◆ W10-11, W10-11a: A Storage Space (W10-11) sign supplemented by a word message Storage Space Ahead (W10-11a) sign (see Figure 8B-4) should be used where there is a highway intersection in close proximity to the grade crossing and the Diagnostic Team determines that adequate space is not available to store a design vehicle(s) between the highway intersection and the train or LRT equipment dynamic envelope.
- **[R]** 8B.21-02 (p.1006) ◆ W10-11, W10-11a: The Storage Space (W10-11 and W10-11a) signs should be mounted in advance of the grade crossing at an appropriate location to advise drivers of the space available for motor vehicle storage between the highway intersection and the grade crossing.
- [O] 8B.21-03 (p.1006) ◆ W10-11b: A word message Storage Space Behind (W10-11b) sign (see Figure 8B-4) may be mounted beyond the grade crossing at the highway intersection under the STOP or YIELD sign or just prior to the signalized intersection to remind drivers of the storage space between the tracks and the highway intersection.
- **[M]** 8B.21-04 (p.1006) ◆ W10-11: A Storage Space (W10-11) sign shall not be used as a replacement for the required Advance Warning (W10-1) sign. If used, the Storage Space sign shall be used in addition to the W10-1 sign and shall be mounted on a separate post.

<a id="sec-8B-22"></a>
#### Section 8B.22 Skewed Crossing Sign (W10-12)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-12](symbols/W10-12.png) | **W10-12** | Skewed Crossing (symbol) | Optional (8B.22-01) | 36 x 36 | 36 x 36 | 48 x 48 | — | 48 x 48 | 8B-1 p.994 | 9A-1 |

- [O] 8B.22-01 (p.1006): The Skewed Crossing (W10-12) sign (see Figure 8B-4) may be used at a skewed grade crossing to warn road users that the tracks are not perpendicular to the highway.
- **[R]** 8B.22-02 (p.1006): If the Skewed Crossing sign is used, the symbol should show the direction of the crossing (near left to far right as shown on the sign image in Figure 8B-4, or the mirror image if the track goes from far left to near right).
- **[M]** 8B.22-03 (p.1006): The Skewed Crossing sign shall not be used as a replacement for the required Advance Warning (W10-1) sign. If used, the Skewed Crossing sign shall be used in addition to the W10-1 sign and shall be mounted on a separate post. DecemberMonth 2023

*Also governed by Section 9C.08:*

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.
- [O] 9C.08-02 (p.1068): In situations where there is a need to warn road users to watch for bicycles traveling along the highway, the Bicycle Warning (W11-1) sign may be used with the IN ROAD (W16-1P) plaque or the IN STREET (W16-1aP) plaque (see Figure 9C-1).
- **[R]** 9C.08-03 (p.1068): If used, other advance bicycle warning signs should be installed at least 50 feet in advance of the beginning of the condition.
- **[R]** 9C.08-04 (p.1068): Where temporary traffic control zones are present on bikeways, appropriate signs from Part 6 should be used.
- [O] 9C.08-05 (p.1068): Other warning signs described in Chapters 2C and 8C may be installed on bicycle facilities as appropriate.

<a id="sec-8B-23"></a>
#### Section 8B.23 NO GATES OR LIGHTS Plaque (W10-13P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-13P](symbols/W10-13P.png) | **W10-13P** | No Gates or Lights (plaque) | Optional | 30 x 24 | 30 x 24 | — | — | — | 8B-1 p.994 | — |

- [O] 8B.23-01 (p.1007): The NO GATES OR LIGHTS (W10-13P) plaque (see Figure 8B-4) may be mounted below the Grade Crossing Advance Warning (W10-1 through W10-4) sign at grade crossings that are not equipped with automatic gates or automated signals.

<a id="sec-8B-24"></a>
#### Section 8B.24 Next Crossing Plaques (W10-14P and W10-14aP)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-14P](symbols/W10-14P.png) | **W10-14P** | Next Crossing (plaque) | Optional (8B.24-01) | 30 x 24 | 30 x 24 | — | — | — | 8B-1 p.994 | — |
| ![W10-14aP](symbols/W10-14aP.png) | **W10-14aP** | Use Next Crossing (plaque) | Optional (8B.24-01) | 30 x 24 | 30 x 24 | — | — | — | 8B-1 p.994 | — |

- [O] 8B.24-01 (p.1007) ◆ W10-14P: The NEXT CROSSING (W10-14P) plaque (see Figure 8B-4) may be mounted below the Low Ground Clearance (W10-5) sign (see Section 8B.16) or Skewed Crossing (W10-12) sign to indicate to a road user that the warning is associated with the next grade crossing. This plaque may be used where multiple grade crossings exist in close proximity to one another.
- [O] 8B.24-02 (p.1007) ◆ W10-14aP: Where recommended by a Diagnostic Team, the USE NEXT CROSSING (W10-14aP) plaque (see Figure 8B-4) may be mounted below the Low Ground Clearance (W10-5) sign (see Section 8B.16) to advise a road user with a low clearance load to use the crossing after the upcoming crossing to avoid encountering a low ground clearance situation.

<a id="sec-8B-25"></a>
#### Section 8B.25 ROUGH CROSSING Plaque (W10-15P)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![W10-15P](symbols/W10-15P.png) | **W10-15P** | Rough Crossing (plaque) | Optional (8B.25-02) | 30 x 24 | 30 x 24 | — | — | 36 x 30 | 8B-1 p.995 | — |

- [O] 8B.25-01 (p.1007): The ROUGH CROSSING (W10-15P) plaque (see Figure 8B-4) may be mounted below the Grade Crossing Advance Warning (W10-1 through W10-4) sign on the approach to a grade crossing to provide supplemental information that the surface or condition of the grade crossing might require a reduced speed or some other appropriate action by the road user.
- [O] 8B.25-02 (p.1007): If the grade crossing is rough, word message signs such as BUMP, DIP, or ROUGH CROSSING may be installed. A W13-1P advisory speed plaque may be installed below the word message sign in advance of rough crossings.

<a id="sec-8B-27"></a>
#### Section 8B.27 Emergency Notifcation System Sign (I13i -1)

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **I13-1** | Emergency Notification | Mandatory (8B.27-01) | — | — | — | 12 x 9 | — | 8B-1 p.995 | — |

- **[M]** 8B.27-01 (p.1007): The Emergency Notification System (I13-1) sign (see Figure 8B-5) shall be installed on each approach at all highway-rail grade crossings, and at all highway-LRT grade crossings with automatic gates or flashing light-signals, to provide information to road users so that they can notify the railroad company or transit agency about emergencies or malfunctioning traffic control devices.

### Chapter 8D 

<a id="sec-8D-10"></a>
#### Section 8D.10 Movements Prohibited During Preemption

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **R3-1a** | No Right Turn - Train (symbol) | Recommended (8D.10-05) | 24 x 30 | 30 x 36 | — | — | — | 8B-1 p.994 | — |
| ![R3-2a](symbols/R3-2a.png) | **R3-2a** | No Left Turn - Train (symbol) | Recommended (8D.10-05) | 24 x 30 | 30 x 36 | — | — | — | 8B-1 p.994 | — |

*Also governed by Section 2B.26:*

- **[M]** 2B.26-01 (p.89): Movement Prohibition signs (see Figure 2B-4) shall be installed where specific movements are prohibited at an intersection approach except as provided in Paragraphs 13 and 17 of this Section.
- **[R]** 2B.26-02 (p.89): Movement Prohibition signs should only be used to prohibit a turn or through movement from an entire approach and should not be used to designate movements that are required or permitted from a specific lane or lanes on a multi-lane approach.
- **[R]** 2B.26-03 (p.89): Movement Prohibition signs should be placed where they will be most easily seen by road users who might be intending to make the movement.
- **[R]** 2B.26-04 (p.89): If a No Right Turn (R3-1) sign (see Figure 2B-4) is used, at least one should be placed either over the roadway or at a right-hand corner of the intersection.
- **[R]** 2B.26-05 (p.89): If a No Left Turn (R3-2) sign (see Figure 2B-4) is used, at least one should be placed over the roadway, at the far left corner of the intersection, on a median, or in conjunction with the STOP sign or YIELD sign located on the near right corner.
- **[R]** 2B.26-06 (p.89): Except as provided in Item C in Paragraph 11 of this Section for signalized locations, if a NO TURNS (R3-3) sign (see Figure 2B-4) is used, two signs should be used, one at a location specified for a No Right Turn sign and one at a location specified for a No Left Turn sign.
- **[R]** 2B.26-07 (p.89): If a No U-Turn (R3-4) sign (see Figure 2B-4) or a combination No U or Left Turn (R3-18) sign (see Figure 2B-4) is used, at least one should be used at a location specified for a No Left Turn sign.
- **[R]** 2B.26-08 (p.89): If both left turns and U-turns are prohibited, the combination No U or Left Turn (R3-18) sign should be used instead of separate R3-2 and R3-4 signs.
- **[R]** 2B.26-10 (p.89): If a No Straight Through (R3-27) sign (see Figure 2B-4) is used, at least one should be placed either over the roadway or at a location where it can be seen by road users who might be intending to travel straight through the intersection. If turn prohibition signs are installed in conjunction with traffic control signals:
- **[R]** 2B.26-11 (p.89): If turn prohibition signs are installed in conjunction with traffic control signals: A. The No Right Turn sign should be installed adjacent to a signal face viewed by road users in the right-hand lane. B. The No Left Turn (or No U-Turn or combination No U or Left Turn) sign should be installed adjacent to a signal face viewed by road users in the left-hand lane. C. A NO TURNS sign should be placed adjacent to a signal face viewed by all road users on that approach, or two signs should be used.
- [O] 2B.26-12 (p.89): If turn prohibition signs are installed in conjunction with traffic control signals, an additional turn prohibition sign may be post-mounted to supplement the sign mounted overhead.
- [O] 2B.26-13 (p.89): Where ONE WAY signs are used (see Section 2B.49), No Left Turn and No Right Turn signs may be omitted.
- [O] 2B.26-14 (p.89) ◆ R3-1a: Where the movement restriction applies to certain vehicle classes, signs incorporating a supplementary legend, modified as appropriate, may be used to indicate the specific vehicle class restriction (R3-1b through R3-1d) or exception (R3-1e and R3-1f) (see Figure 2B-4). When the movement restriction applies during certain time periods only, the following Movement Prohibition signing alternatives may be used and are listed in order of preference: A. A blank-out or changeable message sign (see Chapter 2L) that displays the prohibited movement only during the time that the movement prohibition is applicable, especially at signalized intersections. B. Permanently-mounted signs incorporating a supplementary legend showing the hours and days during which the prohibition is applicable (R3-1g and R3-1h) (see Figure 2B-4). C. Portable signs, installed by proper authority, located off the roadway at each corner of the intersection. The portable signs are only to be used during the time that the movement prohibition is applicable.
- **[M]** 2B.26-15 (p.91): The blank-out part-time electronic-display Movement Prohibition sign shall consist of a red circle and diagonal with a white prohibited movement on an opaque black background.
- [O] 2B.26-16 (p.91): Movement Prohibition signs may be omitted at a ramp entrance to an expressway or a channelized intersection where the design is such as to indicate clearly the one-way traffic movement on the ramp or turning lane.
- **[M]** 2B.26-17 (p.91): The No Left Turn (R3-2) sign, the No U-Turn (R3-4) sign, and the combination No U or Left Turn (R3-18) sign shall not be used at approaches to roundabouts to prohibit drivers from turning left onto the circulatory roadway of a roundabout.

*Also governed by Section 2B.28:*

- **[M]** 2B.28-01 (p.92): Mandatory Movement Lane Control (R3-5, R3-5a, and R3-7) signs (see Figure 2B-4), if used, shall indicate only the single vehicle movement that is required from the lane.
- **[M]** 2B.28-02 (p.92): The Mandatory Movement Lane Control (R3-5 and R3-5a) symbol signs shall include the legend ONLY and shall be mounted overhead over the specific lanes to which they apply (see Section 2B.27). The R3-7 sign shall be for post-mounting only. The R3-7 sign shall not be mounted at the far side of the intersection.
- **[M]** 2B.28-03 (p.92): When the mandatory movement applies to lanes exclusively designated for HOV traffic, the HOV 2+ (R3-5cP) supplemental plaque shall be used. When the mandatory movement applies to lanes that are not HOV facilities, but are lanes exclusively designated for buses and/or taxis, the TAXI LANE (R3-5dP) and/ or BUS LANE (R3-5gP) supplemental plaques shall be used.
- **[M]** 2B.28-04 (p.93): If used, the Mandatory Movement Lane Control (R3-7) sign shall be located in advance of the intersection, such as near the upstream end of the mandatory movement lane, and/or at the near side of the intersection where the regulation applies.
- **[R]** 2B.28-05 (p.93): The use of the Mandatory Movement Lane Control (R3-7) word message sign should be limited to only locations that are adjacent to the full-width portion of a mandatory turn lane. The R3-7 sign should not be installed adjacent to a through lane in advance of a turn bay taper or adjacent to a turn bay taper.
- **[R]** 2B.28-06 (p.93): Mandatory Movement Lane Control signs should be accompanied by lane-use arrow markings, especially where traffic volumes are high, where there is a high percentage of commercial vehicles, or where other distractions exist.
- **[R]** 2B.28-07 (p.93): Where the restriction does not apply to buses or bicycles an EXCEPT BUSES (R3-7aP) or EXCEPT BICYCLES (R3-7bP) plaque should be used.
- [O] 2B.28-08 (p.93): The Through Only (R3-5a) sign may be used to require a road user in a particular lane to proceed straight through an intersection.
- [O] 2B.28-09 (p.93) ◆ R3-1a: The diamond symbol may be used instead of the word message HOV on the R3-5cP supplemental plaque. 10 Where a mandatory left or U-turn lane is added at a median location, a LANE FOR LEFT TURN ONLY (R3-19) or LANE FOR U TURN ONLY (R3-19a) sign may be post-mounted on the median at the beginning of the taper. Where a U turn and a left turn are both allowed, a LANE FOR U AND LEFT TURNS ONLY (R3-19b) sign may be used. Where a R3-19 series sign is used, Mandatory Movement Lane Control signs along the turn lane in the median may be omitted.
- [O] 2B.28-11 (p.93) ◆ R3-1a: The R3-19 series signs may be used where the added median turn lane is separated from the through lanes by a channelizing or divisional island.
- [O] 2B.28-12 (p.93): On an approach to a mandatory turn lane where traffic regularly enters the shoulder to access the turn lane inappropriately, creating safety or operational issues, a DO NOT DRIVE ON SHOULDER (R4-17) sign (see Section 2B.43) may be used to supplement the standard Mandatory Movement Lane Control (R3-5 and/or R3-7 series) signs.

*Also governed by Section 2B.35:*

- **[M]** 2B.35-03 (p.98): On multi-lane roadways, since road users generally anticipate that they need to be in the left-hand lane when approaching a location where they desire to turn left or make a U-turn, an ALL TURNS FROM RIGHT LANE (R3-23) or a U TURN FROM RIGHT LANE (R3-23a) sign (see Figure 2B-8) shall be installed in advance of the location to inform drivers that left turns and/or U-turns will be made from the right-hand lane.
- [O] 2B.35-04 (p.98): Where a median of sufficient width is available, supplemental regulatory or guide signs may also be placed on the left-hand side of the roadway.
- **[M]** 2B.35-05 (p.98) ◆ R3-2a: The R3-24 series sign with an upward diagonal arrow pointing to the right if the jughandle entrance is designed as an exit ramp (see Drawings A and B in Figure 2B-9), or the R3-25 series sign with a horizontal arrow pointing to the right if the jughandle entrance is designed as an intersection, shall be installed on the right-hand side of the roadway at the entrance to the jughandle. The legend on the sign shall be ALL TURNS, U TURN, or U AND LEFT TURNS, as appropriate.
- **[M]** 2B.35-06 (p.98) ◆ R3-2a: If the jughandle is designed such that the jughandle entrance is downstream of the location where the turn would normally have been made (see Drawing C in Figure 2B-9), the R3-26 series sign with an arrow pointing straight upward shall be installed on the right-hand side of the roadway at the intersection to inform road users that they need to proceed straight through the intersection in order to make a left turn or U-turn. The legend on the sign shall be U TURN or U AND LEFT TURNS, as appropriate.
- [S] 2B.35-07 (p.98) ◆ R3-2a: The R3-24, R3-25, and R3-26 series of signs are designed to be mounted below conventional guide signs.

*Also governed by Section 2G.04:*

- **[M]** 2G.04-01 (p.412): The R3-10, R3-13, and R3-13a Vehicle Occupancy Definition signs (see Figure 2G-1) shall be used where agencies determine that it is appropriate to provide a sign that defines the minimum occupancy of vehicles that are allowed to use an HOV lane.
- **[R]** 2G.04-02 (p.412): The Inherently Low Emission Vehicle (ILEV) (R3-10a) sign (see Figure 2G-1) should be used when it is permissible for a properly labeled and certified ILEV, regardless of the number of occupants, to use an HOV lane. When used, the ILEV signs should be post-mounted in advance of and at intervals along the HOV lane based upon engineering judgment and the placement of other Preferential Lane regulatory signs. The R3-10a sign is only applicable to HOV lanes and should not to be used with other preferential lane applications.
- **[M]** 2G.04-05 (p.412): For barrier-separated, buffer-separated, or contiguous preferential lanes where access between the preferential and general-purpose lanes is restricted to designated locations on freeways and expressways, an overhead Vehicle Occupancy Definition (R3-13 or R3-13a) sign shall be installed at least ½ mile in advance of the beginning of or initial entry point to an HOV lane. These signs shall only be displayed in advance of the beginning of or initial or intermediate entry point to HOV lanes.
- **[M]** 2G.04-06 (p.412): For buffer-separated or contiguous HOV lanes where access is restricted to designated locations on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign shall be located at intervals not greater than ½ mile along the length of designated gaps where vehicles are allowed to legally access the HOV lane, and within designated enforcement areas as defined by the operating agency.
- [O] 2G.04-07 (p.412): For buffer-separated or contiguous HOV lanes where access is restricted to designated locations on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign may be located at intervals of approximately ½ mile along the length of the HOV lane.
- [O] 2G.04-08 (p.415): For barrier-separated HOV lanes on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R3-10) sign may be located at intervals of approximately ½ mile along the length of the HOV lane, at intermediate entry points, and at designated enforcement areas as defined by the operating agency.
- **[M]** 2G.04-09 (p.415): For buffer-separated or contiguous HOV lanes where continuous access with the adjacent generalpurpose lanes is provided on freeways and expressways, the sequence of a post-mounted Preferential Lane Operation (R3-11a) sign (see Section 2G.05) followed by a post-mounted Vehicle Occupancy Definition (R310) sign, and ILEV (R3-10a) signs, if appropriate, shall be located at intervals not greater than ½ mile along the length of the HOV lane.
- **[R]** 2G.04-10 (p.415): On freeways and expressways, the signs within each Preferential Lane regulatory sign sequence should be separated by a minimum distance of 800 feet and a maximum distance of 1,000 feet.
- **[R]** 2G.04-11 (p.415): On conventional roads, the distance between Preferential Lane regulatory signs within each sequence should be determined by engineering judgment based on speed, block length, distances from adjacent intersections, and other site-specific considerations.
- **[M]** 2G.04-12 (p.415): For all types of direct access ramps that provide access to or lead to HOV lanes, a post-mounted Vehicle Occupancy Definition (R3-10) sign, and an ILEV (R3-10a) sign, if appropriate, shall be used at the beginning or initial entry point for the direct access ramp.

*Also governed by Section 2G.05:*

- [S] 2G.05-01 (p.415) ◆ R3-1a: The standardized sizes of post-mounted Preferential Lane Operation (R3-11 series) signs are consistent to accommodate any future addition or removal of a single line of legend for each sign. Each size accommodates two lines of legend for the times of day and days of week that the regulation is in effect. Consistent sign sizes are beneficial for agencies when ordering sign materials, as well as when making legend changes to existing signs if changes occur to operating times or occupancy restrictions in the future.
- **[R]** 2G.05-02 (p.415) ◆ R3-1a: Where the regulation is in effect during more than one time period of the day, such as during the morning and afternoon peak periods, the height of the R3-11 and R3-14 series signs should be suitably increased to accommodate the additional line(s) of legend.
- **[M]** 2G.05-03 (p.415) ◆ R3-1a: When used, the post-mounted Preferential Lane Operation (R3-11 series) signs shall be located adjacent to the preferential lane, and the overhead Preferential Lane Operation (R3-14 series) signs shall be mounted directly over the lane.
- **[M]** 2G.05-04 (p.415) ◆ R3-1a: The legend format of the post-mounted Preferential Lane Operation (R3-11 series) signs shall have the following sequence: A. Top Lines: Lanes applicable, such as “RIGHT LANE” or “2 RIGHT LANES” B. Middle Lines: Eligible uses, such as “HOV 2+ ONLY” (or 3+ or 4+, if appropriate) or “BUSES ONLY” or other applicable uses or eligible turning movements C. Bottom Lines: Applicable times and days, such as “7 AM – 9 AM” or “6:30 AM – 9:30 AM, MON-FRI”
- **[M]** 2G.05-05 (p.415) ◆ R3-1a: The legend format of the overhead Preferential Lane Operation (R3-14 series) signs shall have the following sequence: A. Top Lines: Eligible uses, such as “HOV 2+ ONLY” (or 3+ or 4+, if appropriate) or “BUSES ONLY” or other applicable uses or eligible turning movements B. Bottom Lines: Applicable times and days, with the time and day placed above the down arrow, such as “7 AM – 9 AM” or “6:30 AM – 9:30 AM, MON-FRI.” When the operating periods exceed the available line width, the hours and days of the week shall be stacked as shown for the R3-14a sign in Figure 2G-1.
- **[M]** 2G.05-06 (p.415): For preferential lane restrictions that are in effect on a full-time (24 hours per day, seven days per week) basis, the Preferential Lane Operation (R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, and R3-14g) signs that include a period of operation legend shall be modified to display no legend relative to the period of operation except as provided in Paragraph 7 of this Section.
- [O] 2G.05-07 (p.416): In lieu of removing the period of operation text from the Preferential Lane Operation signs for full-time operation, the legend 24 HOURS may be substituted for the times and days of the week on the Preferential Lane Operation (R3-11, R3-11a, R3-11d, R3-11f, R3-14, R3-14d, and R3-14f) signs for preferential lane restrictions that are in effect on a full-time basis.
- **[M]** 2G.05-09 (p.416): The full-time Preferential Lane Operation (R3-11b, R3-11c, R3-11e, R3-11g, R3-14b, R3-14e, and R3-14g) signs that do not display a period of operation legend, as described in Paragraph 6 of this Section, shall not be used where the preferential lane restriction is in effect only on a part-time basis.
- [O] 2G.05-10 (p.416) ◆ R3-1a: Where additional movements are allowed from a preferential lane on an approach to an intersection by vehicles not meeting the preferential lane regulation, the format and words used in the legend in the middle lines on the post-mounted Preferential Lane Operation (R3-11 series) signs and on the top line of the overhead Preferential Lane Operation (R3-14 series) signs may be modified to accommodate the allowable movements (such as “HOV 2+ AND RIGHT TURNS ONLY”).
- [O] 2G.05-11 (p.416): The MOTORCYCLES ALLOWED (R3-11hP) plaque (see Figure 2G-1) may be used where motorcycles, regardless of the number of occupants, are allowed to use an HOV lane.
- **[M]** 2G.05-12 (p.416): If used, the MOTORCYCLES ALLOWED plaque shall be mounted below a post-mounted Preferential Lane Operation (R3-11, R3-11a, or R3-11b) sign.
- **[M]** 2G.05-13 (p.416) ◆ R3-1a: For all barrier-separated or buffer-separated or contiguous preferential lanes where access is restricted to designated locations, an overhead Preferential Lane Operation (R3-14 series) sign shall be used at the beginning or initial entry point on freeways, expressways, and at locations on conventional roadways where the preferential lane is not the outermost (far right or far left) lane of the roadway, and at any intermediate entry points or gaps in the barrier or buffer where vehicles are allowed to legally enter the access-restricted preferential lanes. For all barrier-separated and buffer-separated preferential lanes, post-mounted Preferential Lane Operation (R3-11 series) signs shall be used only as a supplement to the overhead signs on freeways, expressways, and at locations on conventional roadways where the preferential lane is not the outermost lane of the roadway at the beginning or initial entry point, or at any intermediate entry points or gaps in the barrier or buffer.
- **[M]** 2G.05-14 (p.416) ◆ R3-1a: For buffer-separated or contiguous preferential lanes where continuous access with the adjacent general-purpose lanes is provided, including those where a preferential lane is added to the roadway (see Figure 2G-2 for HOV lanes) and those where a general-purpose lane transitions into a preferential lane (see Figure 2G-3 for HOV lanes), an overhead Preferential Lane Operation (R3-14 series) sign shall be used at the beginning or initial entry point of the preferential lane on freeways and expressways.
- [O] 2G.05-15 (p.416) ◆ R3-1a: On conventional roads where preferential lane operations exist, R3-11 series post-mounted signs may be used in lieu of or in addition to overhead R3-14 series signs, except where overhead signs are required as provided in Paragraph 14 of this Section.
- [O] 2G.05-16 (p.416) ◆ R3-1a: Additional overhead (R3-14 series) or post-mounted (R3-11 series) Preferential Lane Operation signs may be provided along the length of any type of preferential lane.
- **[M]** 2G.05-17 (p.416) ◆ R3-1a: For all types of direct access ramps that provide access to or lead to preferential lanes, a post-mounted Preferential Lane Operation (R3-11 series) sign shall be used at the beginning or initial entry point of the direct access ramp.
- [O] 2G.05-18 (p.416) ◆ R3-1a: For direct access ramps to preferential lanes, an overhead Preferential Lane Operation (R3-14 series) sign may be used at the beginning or initial entry point to supplement the required post-mounted signs.
- [O] 2G.05-19 (p.416): Lane-use control signals (see Chapter 4T) may be used at access points to preferential lanes to indicate that a ramp or access roadway leading to the preferential lane or facility, or one or more specific lanes of the facility, are open or closed (see Figure 2G-1).

- **[R]** 8D.10-01 (p.1027): At a signalized intersection that is located within 100 feet of a grade crossing and the intersection traffic control signals are preempted by the approach of rail traffic, all existing permissive-only turning movements toward the grade crossing should be prohibited, steady red arrow signal indications should be shown to all existing protected/permissive and protected-only turning movements toward the grade crossing, and red signal indications should be shown to the straight-through movement toward the grade crossing during the signal preemption sequences. The prohibition of a permissive-only turning movement toward the grade crossing during preemption should be accomplished through the installation of a blank-out turn prohibition (R3-1a or R3-2a) sign (see Figure 8B-1).
- [S] 8D.10-04 (p.1027): Rail operations can include the use of activated blank-out turn prohibition (R3-1a or R3-2a) signs at unsignalized highway-highway intersections in the vicinity of grade crossings, such as where a semi-exclusive or mixed-use alignment is within or parallel to the roadway where road users are normally permitted to turn across the tracks. Month 2023December 2023
- **[R]** 8D.10-05 (p.1028): An LRT-activated blank-out turn prohibition (R3-1a or R3-2a) sign should be used during preemption where all three of the following conditions are present: A. There is no active warning system for the LRT grade crossing, B. Vehicles traveling along a parallel roadway would normally be permitted to turn left or right to travel across tracks that are located within 100 feet of the highway-highway intersection or within the median of the intersection, and C. The drivers turning at the highway-highway intersection are not controlled by a traffic control signal.
- [S] 8D.10-07 (p.1028): The provisions contained in Chapter 2L for blank-out signs are applicable to R3-1a and R3-2a signs.

<a id="sec-8D-11"></a>
#### Section 8D.11 Pre-Signals at or Near Grade Crossings

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R10-10b](symbols/R10-10b.png) | **R10-10b** | Left (Right) Lane Signal | Optional | 30 x 36 | 30 x 36 | — | 24 x 30 | — | 8B-1 p.994 | — |
| ![R10-10c](symbols/R10-10c.png) | **R10-10c** | Left (Right) Turn Lane Signal | Optional | 30 x 42 | 30 x 42 | — | 24 x 36 | — | 8B-1 p.994 | — |

- **[M]** 8D.11-15 (p.1029): If a separate signal face is provided at a pre-signal for separate control of a mandatory left-turn and/or right-turn lane that extends from the downstream signalized intersection back to and across the grade crossing, the separate signal face shall be devoted exclusively to controlling traffic in the turn lane separately from adjacent lanes, and: A. Shall be visibility-limited from the adjacent through movement, or B. A LEFT (RIGHT) LANE SIGNAL (R10-10b) sign (see Figure 8B-1) shall be mounted adjacent to the separate signal face controlling traffic in a single turn lane or in the turn lane that is farthest from the adjacent through lane(s) if multiple turn lanes are present for a particular turning movement, and a LEFT (RIGHT) TURN LANE SIGNAL (R10-10c) sign (see Figure 8B-1) shall be mounted adjacent to the separate signal face controlling traffic in the other turn lanes if multiple turn lanes are present for a particular turning movement.

### Chapter 8E 

<a id="sec-8E-03"></a>
#### Section 8E.03 Pathway and Sidewalk Grade Crossing Signs and Markings

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
| ![R15-8](symbols/R15-8.png) | **R15-8** | Look | Optional (8E.03-11) | — | — | — | 18 x 9 | — | 8B-1 p.994 | 9A-1 |

- [O] 8E.03-11 (p.1037): The LOOK (R15-8) sign (see Figure 8B-1) may be used at a pathway or sidewalk grade crossing to inform pathway or sidewalk users to look in both directions prior to crossing the track(s).
- **[R]** 8E.03-12 (p.1037): If a LOOK (R15-8) sign is used at a pathway or sidewalk grade crossing, it should be mounted on a separate post that is farther from the pathway or sidewalk than the Crossbuck sign or Crossbuck Assembly.

*Also governed by Section 9B.23:*

- [O] 9B.23-01 (p.1064): At railroad or LRT grade crossings with shared-use paths or separated bikeways, the LOOK (R15-8) sign (see Figure 9B-1) may be mounted on the Crossbuck support below the Crossbuck (R15-1) sign or any other signs, or on a separate post in the immediate vicinity of the grade crossing on the railroad or LRT right-of-way.
- **[R]** 9B.23-02 (p.1064): A LOOK sign should not be mounted on a Crossbuck Assembly that has a YIELD or STOP sign mounted on the same support as the Crossbuck.

<a id="sec-8E-06"></a>
#### Section 8E.06 Channelizing Devices Used with Sidewalk and Pathway Traffc Control Devicesi

| Sign | Code | Name | Default class | Single lane | Multi-lane | Expressway | Minimum | Oversized | Size table | Also sized in |
|---|---|---|---|---|---|---|---|---|---|---|
|  | **I13-2** | Push to Exit | Optional | — | — | — | 18 x 9 | — | 8B-1 p.995 | — |

- [S] 8E.06-05 (p.1040): When used in conjunction with * Swings gates should have automatic gates at a PUSH TO EXIT (I13-2) and DO NOT ENTER (R5-1) pathway or sidewalk signs per Section 8E.06 grade crossing, swing gates are typically equipped with a latching device that permits the swing gate to be opened only from the track side of the swing gate. Push bars, kick plates, or similar devices are also appropriate for use on a swing gate.
- **[R]** 8E.06-07 (p.1040): A swing gate should be equipped with a PUSH TO EXIT (I13-2) sign on the track side of the swing gate, and a DO NOT ENTER (R5-1) sign on the side of the swing gate facing away from the tracks (see Figure 8E-10).

## Part 9 Bicycle Facilities

### Chapter 9B Bicycle Regulatory Signs

<a id="sec-9B-03"></a>
#### Section 9B.03 Advance Intersection Lane Control Signs (R3-8 Series) for Bicycle Lanes

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **R3-8x** | Advance Intersection Lane Control with Bike Lane | Optional | — | Varies x 36 | 9A-1 p.1049 | — |

*Also governed by Section 2B.27:*

- **[M]** 2B.27-01 (p.91): Intersection Lane Control signs (see Figure 2B-4), if used, shall require road users in certain lanes to turn, shall permit turns from a lane where such turns would otherwise not be permitted, shall require a road user to stay in the same lane and proceed straight through an intersection, or shall indicate permitted movements from a lane.
- [S] 2B.27-02 (p.91): Intersection Lane Control signs have three applications: A. Mandatory Movement Lane Control (R3-5 series and R3-7 series) signs, B. Optional Movement Lane Control (R3-6 series) signs, and C. Advance Intersection Lane Control (R3-8 series) signs.
- **[R]** 2B.27-03 (p.92): When Intersection Lane Control signs are mounted overhead, each sign used should be placed over the lane or a projection of the lane to which it applies.
- **[R]** 2B.27-04 (p.92): On signalized approaches where through lanes that become mandatory turn lanes, multiple-lane turns that include shared lanes for through and turning movements, or other lane-use regulations are present that would be unexpected by unfamiliar road users, overhead Intersection Lane Control signs should be installed at the signalized location over the appropriate lanes or projections thereof and in advance of the intersection over the appropriate lanes.
- **[R]** 2B.27-05 (p.92): Where overhead mounting on the approach is impracticable for the Advance and/or Intersection lane Control signs, one of the following alternatives should be employed: A. At locations where through lanes become mandatory turn lanes, a Mandatory Movement Lane Control (R3-7) sign should be post-mounted on the left-hand side of the roadway where a through lane is becoming a mandatory left-turn lane on a one-way street or where a median of sufficient width for the signs is available, or on the right-hand side of the roadway where a through lane is becoming a mandatory right-turn lane. B. At locations where a through lane is becoming a mandatory left-turn lane on a two-way street where a median of sufficient width for the signs is not available, and at locations where multiple-lane turns that include shared lanes for through and turning movements are present, an Advance Intersection Lane Control (R3-8 series) sign should be post-mounted in a prominent location in advance of the intersection, and consideration should be given to the use of an oversized version in accordance with Table 2B-1.
- **[R]** 2B.27-06 (p.92): Use of an overhead sign for one approach lane should not require installation of overhead signs for the other lanes of that approach.
- [O] 2B.27-07 (p.92): Intersection Lane Control signs may be omitted where: A. A turn bay has been provided by physical construction or pavement markings, and B. Only the road users using such turn bays are permitted to make a turn in that direction.
- [O] 2B.27-08 (p.92): At roundabouts, Intersection Lane Control (R3-5, R3-6, and R3-8 series) signs may display any of the arrow symbol options shown in Figure 2B-5.

*Also governed by Section 2B.30:*

- [O] 2B.30-01 (p.93): Advance Intersection Lane Control (R3-8, R3-8a, and R3-8b) signs (see Figure 2B-4) may be used to indicate the configuration of all lanes ahead.
- [O] 2B.30-02 (p.93): The word messages ONLY, THRU, HOV 2+, TAXI, BUS, or BIKE, or the bicycle symbol, may be used within the border in combination with the arrow symbols of the R3-8 sign series. The R3-5cP, R3-5dP, and R3-5gP supplemental plaques may be installed at the top outside border of the R3-8 sign over the applicable lane designation on the sign. The diamond symbol may be used instead of the word message HOV. The minimum allowable vehicle occupancy requirement may vary based on the level established for a particular facility.
- [O] 2B.30-03 (p.94): Where a bicycle lane is between two general-purpose lanes the R3-8 series signs may be modified to show the bicycle lane with a white legend on a black background in accordance with designs of the R3-8x series signs (see Figure 2B-4).
- **[R]** 2B.30-04 (p.94): When used, an Advance Intersection Lane Control sign should be placed at an adequate distance in advance of the intersection, either along the lane tapers or at the beginning of the turn lane so that road users can select the appropriate lane (see Figure 2A-4).
- [O] 2B.30-05 (p.94): An Advance Intersection Lane Control sign may be repeated closer to the intersection along the approach for additional emphasis.
- **[M]** 2B.30-06 (p.94): An Advance Intersection Lane Control (R3-8 series) sign shall not be mounted at the far side of an intersection to which it applies.
- **[M]** 2B.30-07 (p.94): Where three or more approach lanes are available to traffic, Advance Intersection Lane Control (R3-8 series) signs, if used, shall be post-mounted in advance of the intersection and shall not be mounted overhead.
- **[M]** 2B.30-08 (p.94): When only the two outermost lanes of the roadway are shown on a R3-8 sign, the R3-5bP or R3-5fP plaque shall be mounted above the R3-8 sign.

- [O] 9B.03-01 (p.1055): Advance Intersection Lane Control (R3-8 series) signs (see Section 2B.30) may display the arrangement of a conventional or buffer-separated bicycle lane in relation to other lanes in the same direction that are present on a roadway approach to an intersection.
- **[R]** 9B.03-03 (p.1055): On an approach to an intersection with complex geometry that can include multiple through lanes and multiple turn lanes and also includes a bicycle lane, consideration should be given to displaying all allowable movements on separate signs, such as using Mandatory Movement Lane Control (R3-5) signs (see Section 2B.28) for the through lanes and Mandatory Movement Lane Control (R3-7) signs (see Section 2B.28) for the turn lanes, and guide signs for bicycle routes (see Section 9D.02 through 9D.07) and Bicycle Route Sign auxiliary plaques (see Section 9D.08) for the bicycle movement.
- **[M]** 9B.03-04 (p.1055): The portion of the sign face for the bicycle lane shall be limited to the relationship of the bicycle lane to the other lanes on the roadway approach to the intersection. The portion of the sign face for the bicycle lane shall not be modified to display specific, supplementary information about the bicycle lane such as bicycle lane extensions, contiguous buffer spaces, or other ancillary bicycle operations such as two-stage turn boxes or bicycle boxes.
- **[M]** 9B.03-05 (p.1055): Counter-flow bicycle lanes shall not be displayed on Advance Intersection Lane Control signs.
- **[M]** 9B.03-06 (p.1055): The shared-lane marking symbol shall not be displayed on Advance Intersection Lane Control signs.
- **[M]** 9B.03-07 (p.1055): Shared-use paths shall not be displayed on Advance Intersection Lane Control signs.
- **[M]** 9B.03-08 (p.1055): Advance Intersection Lane Control signs that display the bicycle lane shall use a contrasting white legend on a black background for the bicycle lane (see Figure 2B-4). The portion of the display for the bicycle lane shall not use the color green on the sign face in an attempt to be consistent with the greencolored pavement that might be present on the intersection approach.

<a id="sec-9B-04"></a>
#### Section 9B.04 Bicycle Lane Signs and Plaques (R3-17, R3-5hP, R3-17aP, and R3-17bP)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R3-5hP](symbols/R3-5hP.png) | **R3-5hP** | Bike Lane (plaque) | Mandatory (9B.04-01) | — | 30 x 12 | 9A-1 p.1049 | — |
| ![R3-17](symbols/R3-17.png) | **R3-17** | Bike Lane | Mandatory (9B.04-01) | — | 24 x 18 | 9A-1 p.1049 | — |
| ![R3-17aP](symbols/R3-17aP.png) | **R3-17aP** | Ahead, Ends (plaques) | Mandatory (9B.04-01) | — | 24 x 9 | 9A-1 p.1049 | — |
| ![R3-17bP](symbols/R3-17bP.png) | **R3-17bP** | Ahead, Ends (plaques) | Mandatory (9B.04-01) | — | 24 x 9 | 9A-1 p.1049 | — |

*Also governed by Section 2B.27:*

- **[M]** 2B.27-01 (p.91): Intersection Lane Control signs (see Figure 2B-4), if used, shall require road users in certain lanes to turn, shall permit turns from a lane where such turns would otherwise not be permitted, shall require a road user to stay in the same lane and proceed straight through an intersection, or shall indicate permitted movements from a lane.
- [S] 2B.27-02 (p.91) ◆ R3-5hP: Intersection Lane Control signs have three applications: A. Mandatory Movement Lane Control (R3-5 series and R3-7 series) signs, B. Optional Movement Lane Control (R3-6 series) signs, and C. Advance Intersection Lane Control (R3-8 series) signs.
- **[R]** 2B.27-03 (p.92): When Intersection Lane Control signs are mounted overhead, each sign used should be placed over the lane or a projection of the lane to which it applies.
- **[R]** 2B.27-04 (p.92): On signalized approaches where through lanes that become mandatory turn lanes, multiple-lane turns that include shared lanes for through and turning movements, or other lane-use regulations are present that would be unexpected by unfamiliar road users, overhead Intersection Lane Control signs should be installed at the signalized location over the appropriate lanes or projections thereof and in advance of the intersection over the appropriate lanes.
- **[R]** 2B.27-05 (p.92): Where overhead mounting on the approach is impracticable for the Advance and/or Intersection lane Control signs, one of the following alternatives should be employed: A. At locations where through lanes become mandatory turn lanes, a Mandatory Movement Lane Control (R3-7) sign should be post-mounted on the left-hand side of the roadway where a through lane is becoming a mandatory left-turn lane on a one-way street or where a median of sufficient width for the signs is available, or on the right-hand side of the roadway where a through lane is becoming a mandatory right-turn lane. B. At locations where a through lane is becoming a mandatory left-turn lane on a two-way street where a median of sufficient width for the signs is not available, and at locations where multiple-lane turns that include shared lanes for through and turning movements are present, an Advance Intersection Lane Control (R3-8 series) sign should be post-mounted in a prominent location in advance of the intersection, and consideration should be given to the use of an oversized version in accordance with Table 2B-1.
- **[R]** 2B.27-06 (p.92): Use of an overhead sign for one approach lane should not require installation of overhead signs for the other lanes of that approach.
- [O] 2B.27-07 (p.92): Intersection Lane Control signs may be omitted where: A. A turn bay has been provided by physical construction or pavement markings, and B. Only the road users using such turn bays are permitted to make a turn in that direction.
- [O] 2B.27-08 (p.92): At roundabouts, Intersection Lane Control (R3-5, R3-6, and R3-8 series) signs may display any of the arrow symbol options shown in Figure 2B-5.

- **[M]** 9B.04-01 (p.1055): The Bike Lane (R3-17) sign and the BIKE LANE (R3-5hP), AHEAD (R3-17aP), and ENDS (R3-17bP) plaques (see Figure 9B-1) shall be used only in conjunction with marked bicycle lanes as described in Sections 9E.01, 9E.06, and 9E.07.
- **[R]** 9B.04-02 (p.1055): If used, Bicycle Lane signs and plaques should be located at the beginning of the bicycle lane and in advance of the downstream end of the bicycle lane.
- [O] 9B.04-03 (p.1055): Additional Bicycle Lane signs and plaques may be used at periodic intervals along the bicycle lane as determined by engineering judgment based on the operating speed of bicycle and other traffic, block length, distances from adjacent intersections, and other considerations.
- [O] 9B.04-06 (p.1056) ◆ R3-5hP: Where two or more movements from a bicycle lane are allowed, or where the emphasis of allowed bicycle movements is needed, an Optional Movement Lane Control sign (see Section 2B.29) may be supplemented with a BIKE LANE (R3-5hP) plaque above the Optional Movement Lane Control sign.
- [O] 9B.04-07 (p.1056): Where bicycle lanes are located between travel lanes on intersection approaches or where only a single bicycle movement is allowed from a certain bicycle lane, a Mandatory Movement Lane Control sign (see Section 2B.28) may be supplemented with a BIKE LANE plaque to require a bicyclist in a particular bicycle lane at an intersection to stay in the same lane and proceed straight through the intersection, or to indicate a required turn from a particular bicycle lane.

<a id="sec-9B-05"></a>
#### Section 9B.05 BEGIN RIGHT TURN LANE YIELD TO BIKES Sign (R4-4)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R4-4](symbols/R4-4.png) | **R4-4** | Begin Right Turn Lane Yield to Bikes | Optional (9B.05-01) | — | 36 x 30 | 9A-1 p.1049 | — |

- [O] 9B.05-01 (p.1056): Where motor vehicles entering a mandatory right-turn lane must weave across bicyclists in bicycle lanes, the BEGIN RIGHT TURN LANE YIELD TO BIKES (R4-4) sign (see Figure 9B-1) may be used to inform both the motorist and the bicyclist of this weaving maneuver (see Figures 9E-3 and 9E-4).
- **[R]** 9B.05-02 (p.1056): The R4-4 sign should not be used when bicyclists need to move left because of a right-turn lane drop situation.

<a id="sec-9B-06"></a>
#### Section 9B.06 Bicycle Wrong Way Sign and RIDE WITH TRAFFIC Plaque (R5-1b and R9-3cP)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **R5-1b** | Bicycle Wrong Way | Recommended (9B.06-03) | 12 x 18 | 12 x 18 | 9A-1 p.1049 | — |
|  | **R9-3cP** | Ride With Traffic (plaque) | Recommended (9B.06-03) | 12 x 12 | 12 x 12 | 9A-1 p.1049 | — |

- [O] 9B.06-01 (p.1056): The Bicycle WRONG WAY (R5-1b) sign and RIDE WITH TRAFFIC (R9-3cP) plaque (see Figure 9B-1) may be placed facing wrong-way bicyclists, such as on the left-hand side of a roadway.
- [O] 9B.06-02 (p.1056): This sign and plaque may be mounted back-to-back with other signs to minimize visibility to other traffic.
- **[R]** 9B.06-03 (p.1056): The RIDE WITH TRAFFIC plaque should be used only in conjunction with the Bicycle WRONG WAY sign, and should be mounted directly below the Bicycle WRONG WAY sign.

<a id="sec-9B-09"></a>
#### Section 9B.09 No Parking Bike Lane Signs (R7-9 and R7-9a)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R7-9](symbols/R7-9.png) | **R7-9** | No Parking Bike Lane | Mandatory (9B.09-01) | — | 12 x 18 | 9A-1 p.1049 | — |
| ![R7-9a](symbols/R7-9a.png) | **R7-9a** | No Parking Bike Lane | Mandatory (9B.09-01) | — | 12 x 18 | 9A-1 p.1049 | — |

*Also governed by Section 2B.52:*

- [S] 2B.52-01 (p.123): Parking signs pertain to the parking, standing, and stopping of vehicles along the roadway and in designated parking areas. They cover a wide variety of regulations, and only general guidance can be provided here. The word “standing” when used on the R7 and R8 series of signs refers to the practice of a driver keeping the vehicle in a stationary position while continuing to occupy the vehicle. The word “stopping” when used on the R7 and R8 series signs refers to any vehicle, occupied by a driver or not, that stops other than to avoid conflict with other traffic or to comply with official direction. Other types of activities such as active loading, active passenger loading, and/or waiting might be established in State or local codes for use on R7 and R8 series signs.

*Also governed by Section 7B.07:*

- [O] 7B.07-01 (p.983): Parking and stopping regulatory signs may be used to prevent parked or waiting vehicles from blocking pedestrians’ views, and drivers’ views of pedestrians, and to control vehicles as a part of the school traffic plan.

- **[M]** 9B.09-01 (p.1057): If the installation of signs is necessary to restrict parking, standing, or stopping in a bicycle lane, appropriate signs as described in Sections 2B.53 through 2B.55, or the No Parking Bike Lane (R7-9 or R7-9a) signs (see Figure 9B-1) shall be installed.

<a id="sec-9B-11"></a>
#### Section 9B.11 Bicycles Use Ped Signal Sign (R9-5)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-5](symbols/R9-5.png) | **R9-5** | Bicycles Use Pedestrian Signal | Optional (9B.11-01) | 12 x 18 | 12 x 18 | 9A-1 p.1049 | — |

- [O] 9B.11-01 (p.1057): The Bicycles Use Ped Signal (R9-5) sign (see Figure 9B-1) may be used where the crossing of a street by bicyclists is controlled by pedestrian signal indications.
- [O] 9B.11-02 (p.1057): In order to remind drivers who are making turns to yield to or stop for pedestrians or bicyclists, a Turning Vehicles Yield to Pedestrians (R10-15) sign, Turning Vehicles Stop for Pedestrians (R10-15a) sign (see Section 2B.59), or Left Turn Yield to Bicycles (R10-12b) sign (see Section 9B.21) may be used.
- **[R]** 9B.11-03 (p.1057): If used, the R9-5 sign should be installed in the vicinity of where bicyclists will be crossing the street.

<a id="sec-9B-12"></a>
#### Section 9B.12 Bicycles Yield to Peds Sign (R9-6)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-6](symbols/R9-6.png) | **R9-6** | Bicycles Yield to Pedestrians | Optional (9B.12-01) | 12 x 18 | 12 x 18 | 9A-1 p.1049 | — |

- [O] 9B.12-01 (p.1058): The Bicycles Yield to Peds (R9-6) sign (see Figure 9B-1) may be used at locations where a bicyclist is required to cross or share a facility used by pedestrians and is required to yield to the pedestrians.
- **[M]** 9B.12-02 (p.1058): Where the Bicycles Yield to Peds sign is supported by a yield line pavement marking (see Section 3B.19) to establish the yielding point, the sign and the pavement marking shall be installed adjacent to each other.
- **[M]** 9B.12-03 (p.1058): The Bicycles Yield to Peds sign shall not be used in bicycle corridors to establish a programmatic regulation where no yielding point exists.
- **[M]** 9B.12-04 (p.1058): The Bicycles Yield to Peds sign shall not be used in conjunction with a STOP or YIELD sign, Yield Here to Pedestrians Sign, or a Stop Here for Pedestrians Sign.

<a id="sec-9B-13"></a>
#### Section 9B.13 Shared-Use Path Restriction Sign (R9-7)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-7](symbols/R9-7.png) | **R9-7** | Shared-Use Path Restriction | Optional (9B.13-01) | 12 x 18* | — | 9A-1 p.1049 | — |

- [O] 9B.13-01 (p.1058): The Shared-Use Path Restriction (R9-7) sign (see Figure 9B-1) may be installed to supplement a solid white pavement marking line (see Section 9E.13) on facilities that are to be shared by pedestrians and bicyclists in order to provide a separate designated pavement area for each mode of travel. The symbols may be transposed as appropriate.
- **[R]** 9B.13-02 (p.1058): If two-way operation is allowed on the facility for pedestrians and/or bicyclists, the designated pavement area that is provided for each two-way mode of travel should be wide enough to accommodate both directions of travel for that mode.

<a id="sec-9B-14"></a>
#### Section 9B.14 Bicycles Allowed Use of Full Lane Sign (R9-20)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-20](symbols/R9-20.png) | **R9-20** | Bicycles Allowed Use of Full Lane | Optional (9B.14-02) | — | 30 x 30 | 9A-1 p.1049 | — |

- [O] 9B.14-02 (p.1058): The Bicycles Allowed Use of Full Lane (R9-20) sign (see Figure 9B-1) may be used on roadways where no bicycle lanes or adjacent shoulders usable by bicycles are present and where travel lanes are too narrow for bicycles and motor vehicles to operate side-by-side.
- [O] 9B.14-03 (p.1058): The Bicycles Allowed Use of Full Lane sign may be used in locations where it is important to inform road users that bicyclists might occupy the travel lane.
- [O] 9B.14-04 (p.1058): Section 9E.09 describes a shared-lane marking that may be used in addition to or instead of the Bicycles Allowed Use of Full Lane sign to inform road users that bicyclists might occupy the travel lane.

<a id="sec-9B-15"></a>
#### Section 9B.15 Bicycle Passing Clearance Sign (R4-19)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R4-19](symbols/R4-19.png) | **R4-19** | Bicycle Passing Clearance | Optional (9B.15-01) | — | 30 x 30 | 9A-1 p.1049 | — |

- [O] 9B.15-01 (p.1058): The Bicycle Passing Clearance (R4-19) sign (see Figure 9B-1) may be used in jurisdictions that have defined in law or ordinance a specific clearance to be provided by motor vehicles when they pass bicycles.
- [O] 9B.15-02 (p.1058): The specific clearance displayed on the Bicycle Passing Clearance (R4-19) sign may be adjusted to reflect the applicable law or ordinance.
- **[M]** 9B.15-03 (p.1058): The Bicycle Passing Clearance (R4-19) sign shall not be used in jurisdictions that do not have a specific passing clearance to be provided by motor vehicles passing bicycles, as defined in law or ordinance.
- **[R]** 9B.15-04 (p.1058): The Bicycle Passing Clearance (R4-19) sign should not be used on roadways with bicycle lanes or with shoulders usable for bicycle travel.

<a id="sec-9B-16"></a>
#### Section 9B.16 Bicycles Use Shoulder Only Sign (R9-21)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-21](symbols/R9-21.png) | **R9-21** | Bicycles Use Shoulder Only | Optional (9B.16-01) | — | 24 x 30 | 9A-1 p.1049 | — |

- [O] 9B.16-01 (p.1058): The Bicycles Use Shoulder Only (R9-21) sign (see Figure 9B-1) may be used to designate locations on a freeway or expressway where bicycles are allowed, but must remain on an available and usable shoulder.
- **[R]** 9B.16-02 (p.1058): The Bicycles Use Shoulder Only sign should be limited to use on freeways and expressways.
- **[R]** 9B.16-03 (p.1058): The Bicycles Use Shoulder Only sign should be placed adjacent to the entrance ramp or entrance to the freeway at or near the location where the full-width shoulder resumes beyond the entrance ramp taper. Sect. 9B.12 to 9B.16

<a id="sec-9B-17"></a>
#### Section 9B.17 Signing for Bicycles on Freeways and Expressways

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R5-10dP](symbols/R5-10dP.png) | **R5-10dP** | On Freeway (plaque) | Optional (9B.17-04) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-22](symbols/R9-22.png) | **R9-22** | Bicycles Must Exit | Mandatory (9B.17-01) | — | 24 x 30 | 9A-1 p.1049 | — |

- **[M]** 9B.17-01 (p.1059) ◆ R9-22: The Bicycles Must Exit (R9-22) sign (see Figure 9B-1) shall be used in advance of a location where a freeway or expressway becomes prohibited to bicycle travel, and shall be placed in advance of the intersection or exit ramp prior to the prohibited segment of roadway (see Figure 9B-4).
- [O] 9B.17-04 (p.1059) ◆ R5-10dP: The ON FREEWAY (R5-10dP) plaque (see Figure 9B-1) may be used with an appropriate Selective Exclusion sign to indicate a prohibition along ramps leading to an adjacent or parallel freeway.

<a id="sec-9B-18"></a>
#### Section 9B.18 Two-Stage Bicycle Turn Box Regulatory Signing (R9-23 Series)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-23](symbols/R9-23.png) | **R9-23** | Bicycle All Turns from Bike Lane | Mandatory (9B.18-03) | — | 12 x 18 | 9A-1 p.1049 | — |
| ![R9-23a](symbols/R9-23a.png) | **R9-23a** | Bicycle Left Turn from Bike Lane | Mandatory (9B.18-03) | — | 12 x 18 | 9A-1 p.1049 | — |
| ![R9-23b](symbols/R9-23b.png) | **R9-23b** | Bicycle Turn Must Use Turn Box | Mandatory (9B.18-03) | — | 12 x 18 | 9A-1 p.1049 | — |
| ![R9-23c](symbols/R9-23c.png) | **R9-23c** | Bicycle Left Turn Must Use Turn Box | Mandatory (9B.18-03) | — | 12 x 18 | 9A-1 p.1049 | — |

- **[M]** 9B.18-03 (p.1059): Where bicycles are required to use a two-stage bicycle turn box (see Figure 9B-5), the Two-Stage Bicycle Turn Box regulatory sign series (see Figure 9B-5) shall be used.
- **[M]** 9B.18-04 (p.1059): Where bicycles are required to use a two-stage bicycle turn box, the Bicycles All Turns from Bike Lane (R9-23) or Bicycle Left Turn from Bike Lane (R9-23a) advance regulatory sign shall be mounted in advance of the intersection, and at least one Bicycle Turn Must Use Turn Box (R9-23b or R9-23c) sign shall be used at the intersection.
- **[M]** 9B.18-05 (p.1059) ◆ R9-23b: Where used, the Bicycle Turn Must Use Turn Box (R9-23b) sign shall be mounted at the near side of the intersection.
- **[M]** 9B.18-06 (p.1059) ◆ R9-23c: Where used, the Bicycle Turn Must Use Turn Box location (R9-23c) sign shall be mounted at the far side of the intersection.
- [O] 9B.18-07 (p.1059): Where use of a two-stage bicycle turn box is optional, the Two-Stage Bicycle Turn Box guide sign series (see Section 9D.13) may be used to provide directional information.
- [O] 9B.18-08 (p.1059): If used, an appropriately sized Street Name (D3-1) sign (see Section 2D.45) may be installed below the All Turns from Bike Lane sign or Left Turn from Bike Lane sign to identify the crossroad where the turn box will be available.

<a id="sec-9B-19"></a>
#### Section 9B.19 Bicycle Jughandle Signs (R9-24, R9-25, R9-26, and R9-27 Series)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R9-24](symbols/R9-24.png) | **R9-24** | Bicycle Jughandle Signs | Optional (9B.19-02) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-24a](symbols/R9-24a.png) | **R9-24a** | Bicycle All Turns | Optional (9B.19-03) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-25](symbols/R9-25.png) | **R9-25** | Bicycle U and Left Turns | Optional (9B.19-02) | — | 24 x 9 | 9A-1 p.1049 | — |
| ![R9-25a](symbols/R9-25a.png) | **R9-25a** | Bicycle U and Left Turns | Optional (9B.19-04) | — | 24 x 9 | 9A-1 p.1049 | — |
| ![R9-25b](symbols/R9-25b.png) | **R9-25b** | Bicycle U and Left Turns | Optional (9B.19-04) | — | 24 x 9 | 9A-1 p.1049 | — |
| ![R9-26](symbols/R9-26.png) | **R9-26** | Bicycle U Turn | Optional (9B.19-02) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-26a](symbols/R9-26a.png) | **R9-26a** | Bicycle U Turn | Optional (9B.19-05) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-26b](symbols/R9-26b.png) | **R9-26b** | Bicycle U Turn | Optional (9B.19-05) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-27](symbols/R9-27.png) | **R9-27** | Bicycle Left Turn | Optional (9B.19-02) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-27a](symbols/R9-27a.png) | **R9-27a** | Bicycle Left Turn | Optional (9B.19-02) | — | 24 x 6 | 9A-1 p.1049 | — |
| ![R9-27b](symbols/R9-27b.png) | **R9-27b** | Bicycle Left Turn | Optional (9B.19-02) | — | 24 x 6 | 9A-1 p.1049 | — |

- [O] 9B.19-02 (p.1062): The R9-23 sign (see Figure 9B-1) may be used in advance of where bicyclists are required to use the bicycle jughandle turn in order to facilitate all turns.
- [O] 9B.19-03 (p.1062) ◆ R9-24, R9-24a: The R9-24 series sign (see Figure 9B-1) may be used where bicyclists are required to use the bicycle jughandle turn in order to facilitate all turns.
- [O] 9B.19-04 (p.1062) ◆ R9-25, R9-25a, R9-25b: The R9-25 series sign (see Figure 9B-1) may be used where bicyclists are required to use a bicycle jughandle turn to facilitate U-turns and left turns and where right-turning bicyclists are exempted or the right turn is not available or possible (see Figure 9B-6).
- [O] 9B.19-05 (p.1062) ◆ R9-26, R9-26a, R9-26b: The R9-26 series sign (see Figure 9B-1) may be used where bicyclists are required to use a jughandle to facilitate U-turns and where left-turning and right-turning bicyclists are exempted or the left turn or right turn is not available or possible.
- [O] 9B.19-06 (p.1062) ◆ R9-27, R9-27a, R9-27b: The R9-27 series sign (see Figure 9B-1) may be used where bicyclists are required to use a jughandle to facilitate left turns and where U-turning and right-turning bicyclists are exempted or the U-turn or right turn is not available or possible.
- [O] 9B.19-07 (p.1063): A Bicycle Jughandle sign may be used to indicate a jughandle turn initially made by a left turn for a bicycle lane on the left-hand side of a one-way street or for a counter-flow bicycle lane. The legend RIGHT may be substituted for the legend LEFT on Bicycle Jughandle signs to represent bicycle facilities on the left-hand side of the roadway where facilitating a right turn would be applicable.
- **[R]** 9B.19-08 (p.1063): Applications of Bicycle Jughandle signs should be limited to brief independent alignments either through physical separation or islands formed by pavement markings. Bicycle Jughandle signs should not be used for a turning movement facilitated by a two-stage turn box (see Section 9B.18).

<a id="sec-9B-20"></a>
#### Section 9B.20 Bicycle Actuation Signs (R10-4, R10-22, R10-24, R10-25, and R10-26)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R10-22](symbols/R10-22.png) | **R10-22** | Bicycle Detector | Optional (9B.20-01) | 12 x 18 | 12 x 18 | 9A-1 p.1049 | — |
| ![R10-24](symbols/R10-24.png) | **R10-24** | Bike Push Button for Green Light | Optional (9B.20-01) | 9 x 15 | 9 x 15 | 9A-1 p.1049 | — |
| ![R10-26](symbols/R10-26.png) | **R10-26** | Bike Push Button for Green Light (arrow) | Optional (9B.20-01) | 9 x 15 | 9 x 15 | 9A-1 p.1049 | — |

*Also governed by Section 2B.58:*

- **[M]** 2B.58-01 (p.128): Where manual actuation of a traffic signal is required for pedestrians or bicyclists to call a signal phase to cross the roadway, traffic signal signs applicable to pedestrian actuation (see Figure 2B-27) or bicyclist actuation (see Figure 9B-1) shall be mounted immediately above or incorporated into the push button detector units (see Section 4I.05).
- [O] 2B.58-03 (p.128): The following signs may be used as an alternate for the R10-3 and R10-4 signs: A. Push Button to Cross Street Wait for Walk Signal (R10-3a); or B. Push Button to Cross Street Wait for Green Signal (R10-4a).
- [O] 2B.58-04 (p.128): The name of the street to be crossed may be substituted for the word STREET in the legends on the R10-3a and R10-4a signs.
- **[R]** 2B.58-05 (p.128): The finger in the push button symbol on the R10-3, R10-3a, R10-4, and R10-4a signs should point in the same direction as the arrow on the sign. Figure 2B-27. Pedestrian Signs and Plaques (Sheet 1 of 2)
- [O] 2B.58-06 (p.130): Where symbolic pedestrian signal indications are used, an educational sign (R10-3b) may be used instead of the R10-3 sign to improve pedestrian understanding of pedestrian indications at signalized intersections. Where word-legend pedestrian signal indications are being retained for the remainder of their useful service life, the legends WALK/DONT WALK may be substituted for the symbols on the educational sign R10-3b, thus creating educational sign R10-3c. The R10-3d educational sign may be used to inform pedestrians that the pedestrian clearance time is sufficient only for the pedestrian to cross to the median at locations where pedestrians cross in two stages using a median refuge island. The R10-3e educational sign may be used where countdown pedestrian signals have been provided. In order to assist the pedestrian in understanding which push button to push, the R10-3f through R10-3i educational signs that provide the name of the street to be crossed may be used instead of the R10-3b through R10-3e educational signs.
- [O] 2B.58-07 (p.130) ◆ R10-24, R10-26: The R10-24 or R10-26 sign (see Section 9B.20) may be used where a push button detector has been installed exclusively to actuate a green phase for bicyclists.
- [O] 2B.58-08 (p.130): The R10-25 sign (see Figure 2B-27) may be used where a push button detector has been installed for pedestrians to activate In-Roadway Warning Lights (see Chapter 4U) or flashing beacons that have been added to the pedestrian warning signs.

- [O] 9B.20-01 (p.1063) ◆ R10-24, R10-26: Where bicycles are not controlled by pedestrian signal indications, the R10-4, R10-24, or R10-26 sign (see Section 2B.58) may be used.
- **[R]** 9B.20-02 (p.1063) ◆ R10-24, R10-26: If used, the R10-4, R10-24, or R10-26 signs (see Figure 9B-1) should be installed in the vicinity of where bicycles will be crossing the street.
- [O] 9B.20-03 (p.1063): If bicycles are crossing a roadway where In-Roadway Warning Lights (see Section 4U.02) or other warning lights or beacons have been provided, the R10-25 sign may be used.
- [O] 9B.20-04 (p.1063) ◆ R10-22: The Bicycle Detector (R10-22) sign (see Figure 9B-1) may be installed at signalized intersections where pavement markings are used to indicate the location where a bicycle is to be positioned to actuate the signal (see Section 9E.15).
- **[R]** 9B.20-05 (p.1063): If the Bicycle Detector sign is installed, it should be placed at the roadside adjacent to the marking to emphasize the location of the marking.

<a id="sec-9B-22"></a>
#### Section 9B.22 Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![R10-40](symbols/R10-40.png) | **R10-40** | Bicycle Signal | Optional | 12 x 21 | 12 x 21 | 9A-1 p.1049 | — |
| ![R10-40a](symbols/R10-40a.png) | **R10-40a** | Bicycle Signal | Optional | 12 x 21 | 12 x 21 | 9A-1 p.1049 | — |
| ![R10-41](symbols/R10-41.png) | **R10-41** | Bicycle Signal | Optional | 12 x 21 | 12 x 21 | 9A-1 p.1049 | — |
| ![R10-41a](symbols/R10-41a.png) | **R10-41a** | Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c) | Optional | — | — | text | — |
| ![R10-41b](symbols/R10-41b.png) | **R10-41b** | Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c) | Optional | — | — | text | — |
| ![R10-41c](symbols/R10-41c.png) | **R10-41c** | Bicycle Signal Signs (R10-40, R10-40a, R10-41, R10-41a, R10-41b, and R10-41c) | Optional | — | — | text | — |

- **[M]** 9B.22-03 (p.1063): The Bicycle Signal – Mandatory Movement (R10-40 or R10-40a) sign or the Bicycle Signal – Optional Movement (R10-41. R10-41a, R10-41b, or R10-41c) sign shall require bicycles to turn, shall permit turns where such turns would otherwise not be allowed, shall require a bicycle to stay in the same lane and proceed straight through an intersection, or shall indicate allowed movements when a GREEN BICYCLE signal indication is displayed on a bicycle signal face.

### Chapter 9C Bicycle Warning Signs

<a id="sec-9C-03"></a>
#### Section 9C.03 Bicycle Surface Condition Warning Sign (W8-10)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **W8-10** | Bicycle Surface Condition | Optional (9C.03-01) | 18 x 18 | 30 x 30 | 9A-1 p.1050 | — |
|  | **W8-10P** | Slippery When Wet (plaque) | Optional (9C.03-01) | 12 x 9 | 12 x 9 | 9A-1 p.1050 | — |

- [O] 9C.03-01 (p.1066) ◆ W8-10: The Bicycle Surface Condition Warning (W8-10) sign (see Figure 9C-1) may be installed where roadway or shared-use path conditions could cause a bicyclist to lose control of the bicycle.
- [O] 9C.03-02 (p.1066): Signs warning of other conditions that might be of concern to bicyclists, including BUMP (W8-1), DIP (W8-2), PAVEMENT ENDS (W8-3), and any other word message that describes conditions that are of concern to bicyclists, may also be used (see Figure 9C-1). A supplemental plaque may be used to clarify the specific type of surface condition. 03

<a id="sec-9C-06"></a>
#### Section 9C.06 Two-Way Bicycle Cross Traffc Warning Plaque (W16i -21P)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![W16-21P](symbols/W16-21P.png) | **W16-21P** | 2-Way Bicycle Cross Traffic (plaque) | Mandatory (9C.06-01) | — | 24 x 12 | 9A-1 p.1050 | — |

- **[M]** 9C.06-01 (p.1067): When used, the Two-Way Bicycle Cross Traffic (W16-21P) warning plaque (see Figure 9C-1) shall be installed below a STOP or YIELD sign.

<a id="sec-9C-07"></a>
#### Section 9C.07 Bicycle Lane Ends Warning Sign (W9-5) and Bicycles Merging Sign (W9-5a)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![W9-5](symbols/W9-5.png) | **W9-5** | Bicycle Lane Ends | Optional (9C.07-02) | — | 30 x 30 | 9A-1 p.1050 | — |
| ![W9-5a](symbols/W9-5a.png) | **W9-5a** | Bicycles Merging | Optional (9C.07-02) | 18 x 18 | 30 x 30 | 9A-1 p.1050 | 6H-1 |

*Also governed by Section 6P.01:*

- [O] 6P.01-03 (p.857): TTC plans may deviate from the typical applications described in this Chapter to allow for conditions and requirements of a particular site or jurisdiction.
- [O] 6P.01-04 (p.857): Other devices may be added to supplement the devices and device spacing may be adjusted to provide additional reaction time or delineation. Fewer devices may be used based on field conditions.

- [S] 9C.07-01 (p.1067) ◆ W9-5: Where a warning sign is appropriate, the Bicycle Lane Ends (W9-5) warning sign (see Figure 9C-1) is intended to alert road users that a bicycle lane is ending and that bicycles will share or occupy the travel lane after merging.
- [O] 9C.07-02 (p.1067): The Bicycle Lane Ends warning sign may be used in advance of the end of a bicycle lane to warn that a bicycle lane will be ending.
- [O] 9C.07-03 (p.1067): The Bicycles Merging (W9-5a) sign (see Figure 9C-1) may be used where a bicycle merging maneuver might occur. The Bicycles Merging sign may be used in addition to the Bicycle Lane Ends (W9-5) warning sign.
- **[R]** 9C.07-04 (p.1067): To avoid excessive use of signs, the Bicycle Lane Ends warning sign should not be used where a bicycle lane is dropped on the approach to an intersection and resumes immediately after the intersection.
- [O] 9C.07-05 (p.1068): A Bicycles Allowed Use of Full Lane (R9-20) sign (see Section 9B.14) and/or shared-lane markings (see Section 9E.09) may be installed downstream of the merge area.
- [O] 9C.07-06 (p.1068): A W16-2aP supplemental warning plaque may be used to inform road users of the distance to the end of the bicycle lane and/or to the bicycle merge.

<a id="sec-9C-08"></a>
#### Section 9C.08 Other Bicycle Warning Signs

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![W5-4a](symbols/W5-4a.png) | **W5-4a** | Path Narrows | Optional (9C.08-01) | 18 x 18 | — | 9A-1 p.1050 | — |
| ![W7-5](symbols/W7-5.png) | **W7-5** | Hill | Optional (9C.08-01) | 18 x 18 | 30 x 30 | 9A-1 p.1050 | — |

- [O] 9C.08-01 (p.1068): Other bicycle warning signs (see Figure 9C-1) such as PATH NARROWS (W5-4a) and Hill (W7-5) may be installed on shared-use paths to warn bicyclists of conditions not readily apparent.

<a id="sec-9C-09"></a>
#### Section 9C.09 Object Markers

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
|  | **OM3-C** | Object Marker Type 3 | Optional (9C.09-02) | 6 x 18 | 12 x 36 | 9A-1 p.1050 | — |
|  | **OM3-L** | Object Marker Type 3 | Optional (9C.09-02) | 6 x 18 | 12 x 36 | 9A-1 p.1050 | — |
|  | **OM3-R** | Object Marker Type 3 | Optional (9C.09-02) | 6 x 18 | 12 x 36 | 9A-1 p.1050 | — |

- **[M]** 9C.09-01 (p.1068): Obstructions in a shared-use path shall be marked with retroreflective material or appropriate object markers as described in Section 2C.70.
- [O] 9C.09-02 (p.1068): Fixed objects adjacent to shared-use paths may be marked with Type 1, Type 2, or Type 3 object markers. If the object marker is not also intended to be seen by motorists, a smaller version of the Type 3 object marker may be used (see Table 9A-1).

### Chapter 9D Bicycle Guide Signs

<a id="sec-9D-01"></a>
#### Section 9D.01 Bicycle Destination Signs (D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, D1-3c, D2-1a, D2-2a, and D2-3a)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D1-1b](symbols/D1-1b.png) | **D1-1b** | Bicycle Destination Signs | Optional (9D.01-05) | Varies x 6 | Varies x 6 | 9A-1 p.1050 | — |
| ![D1-1c](symbols/D1-1c.png) | **D1-1c** | Bicycle Destination (1 line) | Optional (9D.01-05) | Varies x 6 | Varies x 6 | 9A-1 p.1050 | — |
| ![D1-2b](symbols/D1-2b.png) | **D1-2b** | Bicycle Destination (2 lines) | Optional (9D.01-05) | Varies x 12 | Varies x 12 | 9A-1 p.1050 | — |
| ![D1-2c](symbols/D1-2c.png) | **D1-2c** | Bicycle Destination (2 lines) | Optional (9D.01-05) | Varies x 12 | Varies x 12 | 9A-1 p.1050 | — |
| ![D1-3b](symbols/D1-3b.png) | **D1-3b** | Bicycle Destination (3 lines) | Optional (9D.01-05) | Varies x 18 | Varies x 18 | 9A-1 p.1050 | — |
| ![D1-3c](symbols/D1-3c.png) | **D1-3c** | Bicycle Destination (3 lines) | Optional (9D.01-05) | Varies x 18 | Varies x 18 | 9A-1 p.1050 | — |
| ![D2-1a](symbols/D2-1a.png) | **D2-1a** | Bike Route Destination and Distance (1 Line) | Optional (9D.01-05) | Varies x 12 | Varies x 12 | 9A-1 p.1050 | — |
| ![D2-2a](symbols/D2-2a.png) | **D2-2a** | Bike Route Destination and Distance (2 Lines) | Optional (9D.01-05) | Varies x 15 | Varies x 15 | 9A-1 p.1050 | — |
| ![D2-3a](symbols/D2-3a.png) | **D2-3a** | Bike Route Destination and Distance (3 Lines) | Optional (9D.01-05) | Varies x 18 | Varies x 18 | 9A-1 p.1050 | — |

*Also governed by Section 2D.36:*

- **[M]** 2D.36-01 (p.232) ◆ D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, D1-3c: Except on approaches to interchanges (see Section 2D.49), the Destination (D1-1 through D1-3) signs (see Figure 2D-9), if used, shall be a horizontal rectangle displaying the name of a city, town, village, or other traffic generator, and a directional arrow.
- [O] 2D.36-02 (p.232) ◆ D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, D1-3c: The distance (see Section 2D.43) to the place named may also be displayed on the Destination (D1-1a through D1-3a) signs (see Figure 2D-9). If several destinations are to be displayed at a single point, the several names may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for such a group of destinations.
- **[R]** 2D.36-03 (p.232): Adequate separation should be made between any destinations or group of destinations in one direction and those in other directions by suitable design of the arrow, spacing of lines of legend, heavy lines entirely across the sign, or separate signs.
- **[M]** 2D.36-05 (p.232): Except as otherwise provided in this Manual, an arrow pointing to the right shall be at the extreme right of the sign, and an arrow pointing left or up shall be at the extreme left. The distance numerals, if used, shall be placed to the right of the destination names.
- [O] 2D.36-06 (p.232): An arrow pointing up may be placed at the extreme right of the sign when the sign is mounted to the left of the traffic to which it applies.
- **[R]** 2D.36-07 (p.232): Unless a sloping arrow will convey a clearer indication of the direction to be followed, the directional arrows should be horizontal or vertical.
- **[R]** 2D.36-08 (p.232): If several individual name signs are assembled into a group, all signs in the assembly should be of the same horizontal width.
- **[R]** 2D.36-09 (p.232): Destination signs should be used: A. At the intersections of U.S. or State numbered routes with Interstate, U.S., or State numbered routes; and B. At points where they serve to direct traffic from U.S. or State numbered routes to the business section of towns, or to other destinations reached by unnumbered routes. DecemberMonth 2023
- **[M]** 2D.36-10 (p.233): Where a total of three or fewer destinations are displayed on the Advance guide (see Section 2E.23) and Supplemental guide (see Section 2E.51) signs, no more than three destination names shall be displayed on a Destination sign. Where four destinations are displayed on the Advance guide and Supplemental guide signs, no more than four destination names shall be displayed on a Destination sign.
- **[R]** 2D.36-11 (p.233): If space permits, four destinations should be displayed on two separate signs at two separate locations.
- [O] 2D.36-12 (p.233): Where space does not permit, or where all four destinations are in one direction, a single sign may be used. Where a single sign is used and all destinations are in the same direction, the arrow may be placed below the destinations for the purpose of enhancing the conspicuity of the arrow.
- **[M]** 2D.36-13 (p.233): Where a single four-name sign assembly is used, a heavy line approximating the width of the sign border entirely across the sign or separate signs shall be used to separate destinations by direction. Month 2023December 2023
- **[R]** 2D.36-14 (p.234): The closest destination lying straight ahead should be at the top of the sign or assembly, and below it the closest destinations to the left and to the right, in that order. The destination displayed for each direction should ordinarily be the next county seat or the next principal city, rather than a more distant destination. In the case of overlapping routes, only one destination should be displayed in each direction for each route.
- **[M]** 2D.36-15 (p.234): If more than one destination is displayed in the same direction, the name of a nearer destination shall be displayed above the name of a destination that is farther away.
- [O] 2D.36-17 (p.234): Overhead Destination signs may be used to provide lane assignment and destination information for some or all of the lanes on the approach to a multi-lane intersection. Destination information may include cardinal directions, route numbers, street names, and/or place names.
- [O] 2D.36-18 (p.234): Overhead signs using the Arrow-per-Lane sign design configuration (see Figure 2D-10) may be used to provide lane assignments for some or all lane destinations at the approach to a multi-lane intersection (see Section 2D.37).

*Also governed by Section 2D.43:*

- **[M]** 2D.43-01 (p.239) ◆ D2-1a, D2-2a, D2-3a: If used, the Distance (D2-1 through D2-3) signs (see Figure 2D-9) shall be a horizontal rectangle of a size appropriate for the required legend, displaying the names of no more than three cities, towns, junctions, or other traffic generators, and the distance (to the nearest mile) to those places.
- **[M]** 2D.43-02 (p.239): The distance numerals shall be placed to the right of the destination names as shown in Figure 2D-9.
- **[R]** 2D.43-03 (p.239): The distance displayed should be selected on a case-by-case basis by the jurisdiction that owns the road or by statewide policy. A well-defined central area or central business district should be used where one exists. In other cases, the layout of the community should be considered in relation to the highway being signed and the decision based on where it appears that most drivers would feel that they are in the center of the community in question.
- **[R]** 2D.43-04 (p.239): The top name on the Distance sign should be that of the next place on the route having a post office or a railroad station, a route number or name of an intersected highway, or any other significant geographical identity. The bottom name on the sign should be that of the next major destination or control city. If three destinations are displayed, the middle line should be used to indicate communities of general interest along the route or important route junctions.
- [O] 2D.43-05 (p.239): The choice of names for the middle line may be varied on successive Distance signs to give road users additional information concerning communities served by the route. Month 2023December 2023
- **[R]** 2D.43-06 (p.243): The control city should remain the same on all successive Distance signs throughout the length of the route until that city is reached.
- [O] 2D.43-07 (p.243): If more than one distant point may properly be designated, such as where the route divides at some distance ahead to serve two destinations of similar importance, and if these two destinations cannot appear on the same sign, the two names may be alternated on successive signs.
- [O] 2D.43-08 (p.243): On a route continuing into another State, destinations in the adjacent State may be displayed.

- [S] 9D.01-01 (p.1069): The purpose of Bicycle Destination (D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, and D1-3c) signs (see Figure 9D1) and Bicycle Distance (D2-1a, D2-2a, and D2-3a) signs (see Figure 9D-1) is to provide guidance to bicyclists traveling along a bikeway network directing them to typical bicycle destinations or points of interest. The smaller size of Bicycle Destination and Distance signs can deemphasize the messages to motorists, especially when the direction(s) or destination(s) displayed provides access to routes or pathways where the use of motor vehicles is prohibited or discouraged. Examples include, but are not limited to: A. Bicycles can go in a direction counter to conventional traffic, B. Access to a separated bikeway or shared-use path from a street, C. Access to a bicycle route, D. Bicycles are directed to another roadway or bikeway that facilitates a parallel or alternative route to the same destination, or E. Access to a sidewalk that provides connectivity between bicycle facilities.
- **[M]** 9D.01-04 (p.1069): Because of their smaller size, Bicycle Destination and Distance signs shall not be used as a substitute for vehicular destination signs when the message is also intended to be applicable to motorists.
- [O] 9D.01-05 (p.1069): Bicycle Destination and Distance (D1-1b, D1-1c, D1-2b, D1-2c, D1-3b, D1-3c, D2-1a, D2-2a, and D2-3a) signs may be installed to provide direction, destination, and distance information as needed for bicycle travel. If several destinations are to be shown at a single location, they may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for the destinations.
- [O] 9D.01-06 (p.1069): Destination (D1-1 and D1-1a) signs (see Section 2D.36) and Street Name (D3-1) signs (see Section 2D.45) may be installed instead of or in addition to Bicycle Destination signs as needed if the Destination or Street Name sign applies to motorists and bicyclists.
- [O] 9D.01-07 (p.1069) ◆ D2-1a, D2-2a, D2-3a: Distance (D2-1 through D2-3) signs (see Section 2D.43) may be installed instead of, or in addition to, Bicycle Distance (D2-1a through D2-3a) signs, as needed, if the destination and distance information applies to motorists and bicyclists.
- **[R]** 9D.01-08 (p.1069): Adequate separation should be made between any destination or group of destinations in one direction and those in other directions by suitable design of the arrow, spacing of lines of legend, heavy lines entirely across the sign, or separate signs.
- **[R]** 9D.01-09 (p.1069): Where a Bicycle Destination sign with distance information is located less than ½ mile from the destination, the distance displayed should be to the nearest ¼ mile. Where the distance to be displayed on a Bicycle Destination sign is less than ¼ mile, the distance should be displayed in feet, rather than miles, to the nearest 50 feet.
- [O] 9D.01-10 (p.1069): Distances may be displayed in fractions of a mile to the nearest ¹⁄10 mile to communicate distance information on Bicycle Destination signs where the distance to a destination is desired to be more precise than ¼-mile increments.
- **[M]** 9D.01-12 (p.1069): An arrow pointing to the right, if used, shall be at the extreme right-hand side of the sign. An arrow pointing left or up, if used, shall be at the extreme left-hand side of the sign. The distance numerals, if used, shall be placed to the right of the destination names.
- **[M]** 9D.01-13 (p.1069): Except as provided in Paragraph 14 of this Section, a bicycle symbol shall be placed next to each destination or group of destinations. Figure 9D-1. Guide Signs and Plaques for Bicycle Facilities (Sheet 1 of 3)
- [O] 9D.01-14 (p.1070): An oversized bicycle symbol may be displayed as the top line of a Bicycle Destination sign instead of individual bicycle symbols for each of the destination/distance lines.
- **[M]** 9D.01-15 (p.1070): If an arrow is at the extreme left, the bicycle symbol shall be placed to the right of the respective arrow.

<a id="sec-9D-02"></a>
#### Section 9D.02 Bike Route Guide Signs (D11-1 and D11-1c)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D11-1](symbols/D11-1.png) | **D11-1** | Bike Route | Optional (9D.02-02) | 24 x 18 | 24 x 18 | 9A-1 p.1051 | — |
|  | **D11-1c** | Bike Route with Destination | Optional (9D.02-02) | 24 x 18 | 24 x 18 | 9A-1 p.1051 | — |

- [S] 9D.02-01 (p.1072): The Bike Route Guide (D11-1 or D11-1c) sign (see Figure 9D-1) is used where no unique designation of routes is desired. Sections 9D.04 through 9D.07 contain information for Bicycle Route signs where the bicycle route is designated by number, name, or both.
- [O] 9D.02-02 (p.1072): Bike Route Guide signs may be provided along designated unnumbered, unnamed bicycle routes to inform bicyclists of bicycle route direction changes and to confirm route direction and destination.
- [O] 9D.02-03 (p.1072): If used, Bike Route Guide signs may be repeated at regular intervals so that bicycles entering from side streets will have an opportunity to know that they are on a bicycle route. Similar guide signing may be used for shared roadways with intermediate signs placed for bicycle guidance.
- [O] 9D.02-04 (p.1072): The Alternative Bike Route Guide (D11-1c) sign may be used to display a word legend that provides information on route direction, destination, and/or route name in place of the “BIKE ROUTE” word legend on the D11-1 sign (see Figure 9D-1).
- [O] 9D.02-05 (p.1073): Other plaques such as BEGIN (M4-14P) and END (M4-6P) may be used with Bike Route Guide signs.
- **[R]** 9D.02-06 (p.1073): Travel times should not be used on Bike Route Guide signs.

<a id="sec-9D-03"></a>
#### Section 9D.03 BIKE ROUTE Plaque (D11-1bP)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D11-1bP](symbols/D11-1bP.png) | **D11-1bP** | Bike Route (plaque) | Optional (9D.03-01) | 18 x 6 | 18 x 6 | 9A-1 p.1051 | — |

- [O] 9D.03-01 (p.1073): The BIKE ROUTE (D11-1bP) plaque (see Figure 9D-1) may be installed to supplement: A. The Alternative Bike Route Guide (D11-1c) sign (see Section 9D.02); B. The Bicycle Directional (D11-11) sign (see Section 9D.11) for use on a shared-use path; or C. A Street Name (D3-1) sign (see Section 2D.45).
- [O] 9D.03-02 (p.1074): When installed above or below a Street Name sign, the D11-1bP supplemental plaque may include a bicycle symbol to the left of the BIKE ROUTE legend.
- **[M]** 9D.03-03 (p.1074): The bicycle symbol shall not be used on a Street Name sign. 04 Where a BIKE ROUTE plaque is used in conjunction with a Street Name sign to identify a street that is part of an overall bicycle network, one of the following signs shall also be used systematically to establish the designated bicycle route on the street identified by the BIKE ROUTE plaque: A. Bike Route Guide signs (see Section 9D.02), B. Alternative Bike Route Guide (D11-1c) sign (see Section 9D.02), C. State or Local Bicycle Route (M1-8 and M1-8a) signs (see Section 9D.05), D. Non-Numbered Bicycle Route (M1-8b and M1-8c) signs (see Section 9D.06), or E. United States Bicycle Route (M1-9) sign (see Section 9D.07). BIKE ROUTE plaques shall not incorporate replicas of the United States Bicycle Route, State or Local Bicycle Route, or Non-Numbered Bicycle Route sign to replace or supplement the bicycle symbol.
- [O] 9D.03-06 (p.1074): The BIKE ROUTE plaque and the Street Name sign may be different widths.

<a id="sec-9D-05"></a>
#### Section 9D.05 Numbered Bicycle Route Signs (M1-8 and M1-8a)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![M1-8](symbols/M1-8.png) | **M1-8** | State or Local Bicycle Route | Optional (9D.05-01) | 12 x 18 | 18 x 24 | 9A-1 p.1051 | — |
| ![M1-8a](symbols/M1-8a.png) | **M1-8a** | State or Local Bicycle Route | Optional (9D.05-01) | 12 x 18 | 18 x 24 | 9A-1 p.1051 | — |

- [O] 9D.05-01 (p.1077): To establish a unique identification (route designation) for a State or local bicycle route, the Bicycle Route (M1-8 or M1-8a) sign (see Figure 9D-1) may be used.
- **[M]** 9D.05-02 (p.1077) ◆ M1-8: The Numbered Bicycle Route (M1-8) sign shall display a route designation and shall have a green background with a white legend and border.
- **[M]** 9D.05-03 (p.1077): The Numbered Bicycle Route (M1-8a) sign shall display the same information as the M1-8 sign and in addition shall display a pictograph or words on the upper portion of the sign panel that are associated with the route or with the agency that has jurisdiction over the route.
- **[M]** 9D.05-04 (p.1077): If a Numbered Bicycle Route (M1-8 or M1-8a) sign is used on a roadway, it shall include a bicycle symbol.
- **[R]** 9D.05-05 (p.1077) ◆ M1-8a: If a pictograph is used on the M1-8a sign the maximum dimension (height or width) of the pictograph should not exceed 2 times the height of the route numeral, and should be contained within a green border. The minimum width of the graphic on the M1-8a sign should be ²⁄3 of the sign width, and the maximum width should be 9 ⁄10 of the sign width.
- **[R]** 9D.05-06 (p.1077) ◆ M1-8a: If a bicycle symbol is used on the M1-8a sign, it should have a minimum height of ¼ of the M1-8a sign panel height.

<a id="sec-9D-06"></a>
#### Section 9D.06 Non-Numbered Bicycle Route Signs (M1-8b and M1-8c)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![M1-8b](symbols/M1-8b.png) | **M1-8b** | Non-Numbered Bicycle Route | Optional (9D.06-05) | 12 x 12 | 18 x 18 | 9A-1 p.1051 | — |
| ![M1-8c](symbols/M1-8c.png) | **M1-8c** | Non-Numbered Bicycle Route | Optional (9D.06-05) | 12 x 12 | 18 x 18 | 9A-1 p.1051 | — |

- **[M]** 9D.06-01 (p.1077): Except as provided in Paragraph 2 of this Section, Non-Numbered Bicycle Route (M1-8b and M1-8c) signs (see Figure 9D-1) used on roadways shall have a green background with a white border, and shall include words identifying the bicycle route or a legend consisting of words identifying the bicycle route and a pictograph or bicycle symbol.
- [O] 9D.06-02 (p.1077): Words identifying the bicycle route may be omitted on Non-Numbered Bicycle Route (M1-8b and M1-8c) signs where a pictograph includes the likeness of a bicycle that clearly identifies the route as a bicycle route.
- [O] 9D.06-05 (p.1077): Where a bicycle route is named instead of numbered, the Non-Numbered Bicycle Route sign may be used.
- [O] 9D.06-06 (p.1077): A green background or white border may be omitted on Non-Numbered Bicycle Route (M1-8b or M1-8c) signs used on shared-use paths.
- **[R]** 9D.06-09 (p.1077): In order to provide signing on a facility managed by a transportation agency, a statewide policy for encouraging independent organizations to adopt the Non-Numbered Bicycle Route sign should be established.

<a id="sec-9D-07"></a>
#### Section 9D.07 U.S. Bicycle Route Sign (M1-9)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![M1-9](symbols/M1-9.png) | **M1-9** | U.S. Bicycle Route | Optional | 12 x 18 | 18 x 24 | 9A-1 p.1051 | — |

- **[R]** 9D.07-01 (p.1078): Where a designated bicycle route extends through two or more States, a coordinated submittal by the affected States for an assignment of a U.S. Bicycle Route number designation should be sent to the American Association of State Highway and Transportation Officials.
- **[M]** 9D.07-02 (p.1078): The U.S. Bicycle Route (M1-9) sign (see Figure 9D-1) shall have a green legend and border with a white background and shall display the route designation as assigned by AASHTO.

<a id="sec-9D-08"></a>
#### Section 9D.08 Bicycle Route Sign and Auxiliary Plaques

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![M4-8P](symbols/M4-8P.png) | **M4-8P** | Bicycle Route Auxiliary Signs (plaque) | Mandatory (9D.08-10) | 12 x 6 | 12 x 6 | 9A-1 p.1051 | 6I-1 |

*Also governed by Section 6I.02:*

- **[M]** 6I.02-01 (p.811): Each detour shall be adequately marked with standard temporary route signs and destination signs.
- [O] 6I.02-02 (p.811): Detour signs in TTC incident management situations may have a black legend and border on a fluorescent pink background.
- [O] 6I.02-03 (p.811): The Detour Arrow (M4-10) sign (see Figure 6I-1) may be used where a detour route has been established.
- [O] 6I.02-04 (p.811): The DETOUR (M4-8P) plaque (see Figure 6I-1) may be mounted at the top of a route sign assembly to mark a temporary route that detours from a highway, bypasses a section closed by a TTC zone, and rejoins the highway beyond the TTC zone. Table 6I‑1. Temporary Traffic Control Zone Guide Sign and Plaque Sizes Notes: 1. Larger signs may be used wherever necessary for greater legibility or emphasis 2. Dimensions are shown in inches and are shown as width x height
- **[R]** 6I.02-05 (p.812): The Detour Arrow (M4-10) sign should normally be mounted just below the ROAD CLOSED (R11-2, R11-3a, or R11-4) sign. The Detour Arrow sign should include a horizontal arrow pointed to the right or left as required.
- **[R]** 6I.02-06 (p.812): The DETOUR (M4-9) sign (see Figure 6I-1) should be used for unnumbered highways, for emergency situations, for periods of short durations, or where, over relatively short distances, road users are guided along the detour and back to the desired highway without route signs.
- **[R]** 6I.02-07 (p.812): A Street Name sign should be placed above, or the street name should be incorporated into, a DETOUR (M4-9) sign to indicate the name of the street being detoured.
- [O] 6I.02-08 (p.812): The END DETOUR (M4-8a) sign or the END (M4-8bP) plaque (see Figure 6I-1) may be used to indicate that the detour has ended.
- **[R]** 6I.02-09 (p.812): When the END DETOUR sign is used on a numbered highway, the sign should be mounted above a route sign after the downstream end of the detour.
- **[R]** 6I.02-10 (p.812): The Pedestrian/Bicyclist Detour (M4-9a) sign (see Figure 6I-1) should be used where a pedestrian/bicyclist detour route has been established because of the closing of a pedestrian/bicycle facility to through traffic.
- **[M]** 6I.02-11 (p.812): If used, the Pedestrian/Bicyclist Detour sign shall have an arrow pointing in the appropriate direction.
- [O] 6I.02-12 (p.812): The arrow on a Pedestrian/Bicyclist Detour sign may be on the sign face or on a supplemental plaque.
- [O] 6I.02-13 (p.812): The Pedestrian Detour (M4-9b) sign or Bicyclist Detour (M4-9c) sign (see Figure 6I-1) may be used where a pedestrian or a bicyclist detour route (not both) has been established because of the closing of the pedestrian or bicycle facility to through traffic.

- **[R]** 9D.08-06 (p.1078): If used, Junction (M2-1P), Cardinal Direction (M3 series), and Alternative Route (M4 series) auxiliary plaques should be mounted above the appropriate Bicycle Route signs.
- **[R]** 9D.08-08 (p.1078): Except for the M4-8P plaque, all route sign auxiliary plaques should match the color combination of the route sign that they supplement.
- **[M]** 9D.08-10 (p.1078): If both the Junction (M2-1P), Cardinal Direction (M3 series), or Alternative Route (M4 series) auxiliary plaque and the Advance Turn Arrow (M5 series) or Directional Arrow (M6 series) auxiliary plaques are used on the same sign assembly as a Bicycle Route sign, the Junction, Cardinal Direction, or Alternative Route auxiliary plaque shall be installed above the Bicycle Route sign, and the Advance Turn Arrow or Directional Arrow auxiliary plaque shall be installed below the Bicycle Route sign.

<a id="sec-9D-09"></a>
#### Section 9D.09 Bicycle Parking Area, Sharing Station, and Lockers Guide Signs (D4-3, D4-4, and D4-4a)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D4-3](symbols/D4-3.png) | **D4-3** | Bicycle Parking Area Directional | Optional (9D.09-02) | 18 x 12 | 18 x 12 | 9A-1 p.1050 | — |
| ![D4-4](symbols/D4-4.png) | **D4-4** | Bicycle-Sharing Station Directional | Optional (9D.09-02) | 12 x 18 | 12 x 18 | 9A-1 p.1050 | — |
| ![D4-4a](symbols/D4-4a.png) | **D4-4a** | Bicycle Lockers Directional | Optional (9D.09-02) | 12 x 18 | 12 x 18 | 9A-1 p.1050 | — |

- [O] 9D.09-02 (p.1080) ◆ D4-3: The Bicycle Parking Area (D4-3) guide sign (see Figure 9D-1) may be installed where it is desirable to show the direction to a designated bicycle parking area. The arrow may be reversed as appropriate.
- [O] 9D.09-03 (p.1080) ◆ D4-4: The Bicycle-Sharing Station (D4-4) guide sign (see Figure 9D-1) may be installed to provide directional information to a designated bicycle-sharing system. The arrow may be reversed as appropriate.
- [O] 9D.09-04 (p.1080): The Bicycle-Sharing Station guide sign may be modified with two lines to accommodate installation in constrained areas.
- [O] 9D.09-05 (p.1080) ◆ D4-4a: The Bicycle Lockers (D4-4a) guide sign (see Figure 9D-1) may be installed where it is desirable to show the direction to designated bicycle lockers. The arrow may be reversed as appropriate.
- **[R]** 9D.09-06 (p.1080): If used, the Bicycle-Sharing Station guide sign should be used in conjunction with a regulated bicycle-sharing system such as one that requires the user to pre-register or provide a deposit in order to use a bicycle.
- **[R]** 9D.09-07 (p.1080): Where it is determined that unregulated bicycle-sharing parking facilities necessitate a bicycle parking sign, the Bicycle Parking Area guide sign should be used.
- **[M]** 9D.09-08 (p.1080): In accordance with Section 1D.07, Bicycle Parking Area, Sharing Station, and Lockers guide signs shall not include promotional advertising, business logos, or other identification that would convey the involvement of a public-private partnership for operating the bicycle parking facility or sharing system.

<a id="sec-9D-11"></a>
#### Section 9D.11 Mode-Specifc Directional Guide Signs for Sharedi -Use Paths (D11-11, D11-12, D11-13, and D11-14)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D11-11](symbols/D11-11.png) | **D11-11** | Bicycles Directional | Optional (9D.11-01) | 18 x 18 | — | 9A-1 p.1051 | — |
| ![D11-12](symbols/D11-12.png) | **D11-12** | Pedestrians Directional | Optional (9D.11-01) | 18 x 18 | — | 9A-1 p.1051 | — |
| ![D11-13](symbols/D11-13.png) | **D11-13** | Skaters Directional | Optional (9D.11-01) | 18 x 18 | — | 9A-1 p.1051 | — |
| ![D11-14](symbols/D11-14.png) | **D11-14** | Equestrians Directional | Optional (9D.11-01) | 18 x 18 | — | 9A-1 p.1051 | — |

- [O] 9D.11-01 (p.1081): Where separate pathways are provided for different types of users, mode-specific Directional Guide (D11-11, D11-12, D11-13, and D11-14) signs (see Figure 9D-1) may be used to guide different types of users to the pathway that is intended for their respective modes.
- [O] 9D.11-02 (p.1081): Mode-specific Directional Guide signs may be installed at the entrance to shared-use paths where the signed mode(s) are permitted or encouraged, and periodically along these facilities as needed.
- [O] 9D.11-03 (p.1081) ◆ D11-11: The Bicycle Directional (D11-11) sign, when combined with the BIKE ROUTE (D11-1bP) supplemental plaque, may be substituted for the D11-1 Bike Route Guide sign on shared-use paths.
- [O] 9D.11-04 (p.1081): When some, but not all, non-motorized user types are encouraged or permitted on a shared-use path, modespecific Directional Guide signs may be placed in combination with each other, and in combination with signs (see Section 9B.08) that prohibit travel by particular modes.
- **[M]** 9D.11-05 (p.1081): If used, symbols on Destination Guide signs for shared-use paths shall be limited to those where the symbol displayed is an allowable mode on the path or pathway alignment, and where the symbol is supported by other regulatory signs to convey the operation. Symbols unrelated to the allowable modes that would otherwise display directional navigation to a facility, activity, or point of interest shall not be used.
- **[R]** 9D.11-07 (p.1081): Destination Guide signs for shared-use paths, exclusive of any identification marker used, should be rectangular in shape. Simplicity and uniformity in design, position, and application as described in Section 2A.04 are important and should be incorporated into the sign design.
- **[R]** 9D.11-08 (p.1081): Destination Guide signs for shared-use paths should be limited to three destinations per sign (see Section 2D.06). 09 Abbreviations (see Section 1D.08) should be kept to a minimum, and should include only those that are commonly recognized and understood.
- **[M]** 9D.11-11 (p.1082): The arrow location and priority order of destinations shall follow the provisions described in Sections 2D.08 and 2D.36. Arrows shall be of the designs provided in Section 2D.08.
- **[M]** 9D.11-12 (p.1082): The lettering for destinations on Destination Guide signs for shared-use paths shall be a combination of lower-case letters with initial upper-case letters (see Section 2D.04). All other word messages on Destination Guide signs for shared-use paths shall be in all upper-case letters.
- **[M]** 9D.11-13 (p.1082): Except as provided in Paragraph 15 of this Section, the lettering style used for destination and directional legends on Destination Guide signs for shared-use paths shall comply with the provisions of Section 2D.04.
- [O] 9D.11-14 (p.1082): The distance to the place named may be displayed on the Destination Guide sign. If several destinations are to be displayed at a single point, the several names may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for such a group of destinations.
- [O] 9D.11-15 (p.1082): A lettering style other than the Standard Alphabets provided in the “Standard Highway Signs “ publication (see Section 1A.05) may be used on Destination Guide signs for shared-use paths if an engineering study determines that the legibility and recognition values for the chosen lettering style at minimum letter heights meet or exceed the values for the Standard Alphabets for the same legend height and stroke width. Sect. 9D.12
- **[M]** 9D.11-16 (p.1083): Where a shared-use path is within the highway right-of-way or crosses a street or highway, an alternative lettering style shall not be used.
- [O] 9D.11-17 (p.1083): Pictographs (see definition in Section 1C.02) may be used on Destination Guide signs for shared-use paths.
- **[M]** 9D.11-18 (p.1083): If a pictograph is used, its height shall not exceed 2 times the height of the upper-case letters of the principal legend on the sign.
- **[M]** 9D.11-19 (p.1083): Business logos, commercial graphics, or other forms of advertising (see Section 1D.07) shall not be used on Destination Guide signs for shared-use paths or sign assemblies.
- [O] 9D.11-20 (p.1083): An identification marker may be used in an assembly for Destination Guide signs applied to shared-use paths, or may be incorporated into the overall design of Destination Guide sign, as a means of visually identifying the sign as part of an overall system of signs.
- **[M]** 9D.11-21 (p.1084): The size of an identification marker shall be smaller than the Destination Guide sign. Identification markers shall not be designed to have an appearance that could be mistaken by road users as being a traffic control device.
- **[R]** 9D.11-22 (p.1084): The area of the identification marker should not exceed ¹⁄5 of the area of the Destination Guide sign with which it is mounted in the same sign assembly.
- **[M]** 9D.11-23 (p.1084): Except as provided in Paragraph 26 of this Section, Destination Guide signs for shared-use paths shall have a white legend and border on a green or brown background and shall be consistent with the basic design principles for guide signs.
- **[M]** 9D.11-24 (p.1084): Color coding or pictographs shall not be used to distinguish between different types of destinations. If used, color coding shall be accomplished by the use of different colored square or rectangular panels on the face of the sign, each positioned to the left of the named geographic area to which the color-coding panel applies. The height of the colored square or rectangular panels shall not exceed 2 times the height of the upper-case letters of the principal legend on the sign.
- [O] 9D.11-25 (p.1084): The different colored square or rectangular panels may include either a black or a white (whichever provides the better contrast with the color of the panel) letter, numeral, or other appropriate designation to identify the destination.
- [O] 9D.11-26 (p.1084): Except where a shared-use path is within the highway right-of-way or crosses a street or highway, Destination Guide signs for shared-use paths may use background colors other than green or brown in order to provide a color identification for systematic destinations within the overall guide signing system.
- **[M]** 9D.11-27 (p.1084): The standard colors of red, orange, yellow, purple, or the fluorescent versions thereof, fluorescent yellow-green, and fluorescent pink shall not be used as background colors for Destination Guide signs for shared-use paths, in order to minimize possible confusion with critical, higher-priority regulatory and warning sign color meanings readily understood by path users.
- [O] 9D.11-28 (p.1084): Destination Guide signs for shared-use paths may display telephone numbers, Internet addresses, and e-mail addresses, including domain names and uniform resource locators (URLs).
- **[M]** 9D.11-29 (p.1084): If used, the use of telephone numbers, Internet addresses, and e-mail addresses shall be limited to direct contact information of the jurisdiction with authority of the shared-use path, or contact information for emergency service response, or both. Contact information for advertising purposes shall not be used.

<a id="sec-9D-12"></a>
#### Section 9D.12 Destination Guide Signs for Shared-Use Paths (D11-10a, D11-10b, D11-10c, D11-10d,

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D11-10a](symbols/D11-10a.png) | **D11-10a** | Shared-Use Path Destination (1 line) | Recommended (9D.12-03) | Varies x 6* | — | 9A-1 p.1051 | — |
| ![D11-10b](symbols/D11-10b.png) | **D11-10b** | Shared-Use Path Destination (2 lines) | Recommended (9D.12-03) | Varies x 12* | — | 9A-1 p.1051 | — |
| ![D11-10c](symbols/D11-10c.png) | **D11-10c** | Shared-Use Path Destination (3 lines) | Recommended (9D.12-03) | Varies x 18* | — | 9A-1 p.1051 | — |
| ![D11-10d](symbols/D11-10d.png) | **D11-10d** | Shared-Use Path Destination and Distance (1 line) | Recommended (9D.12-03) | Varies x 6* | — | 9A-1 p.1051 | — |
| ![D11-10e](symbols/D11-10e.png) | **D11-10e** | Shared-Use Path Destination and | Recommended (9D.12-03) | Varies x 12* | — | 9A-1 p.1051 | — |
| ![D11-10f](symbols/D11-10f.png) | **D11-10f** | Shared-Use Path Destination and | Recommended (9D.12-03) | Varies x 18* | — | 9A-1 p.1051 | — |

- **[M]** 9D.12-02 (p.1081): Where bicycle traffic is allowed on the shared-use path, Destination Guide signs for shared-use paths and any identification markers shall be retroreflective.
- **[R]** 9D.12-03 (p.1081): Destination Guide signs for shared-use paths should be installed on independent assemblies and should not be combined with regulatory and warning signs.
- [O] 9D.12-04 (p.1081): Destination Guide signs for shared-use paths may use symbols detailed in the “Standard Highway Signs” publication (see Section 1A.05) in addition to the bicycle symbol to display other modes permitted to use the shared-use path.
- **[M]** 9D.12-05 (p.1081): If used, symbols on Destination Guide signs for shared-use paths shall be limited to those where the symbol displayed is an allowable mode on the path or pathway alignment, and where the symbol is supported by other regulatory signs to convey the operation. Symbols unrelated to the allowable modes that would otherwise display directional navigation to a facility, activity, or point of interest shall not be used.
- **[R]** 9D.12-07 (p.1081): Destination Guide signs for shared-use paths, exclusive of any identification marker used, should be rectangular in shape. Simplicity and uniformity in design, position, and application as described in Section 2A.04 are important and should be incorporated into the sign design.
- **[R]** 9D.12-08 (p.1081): Destination Guide signs for shared-use paths should be limited to three destinations per sign (see Section 2D.06).
- **[R]** 9D.12-09 (p.1081): Abbreviations (see Section 1D.08) should be kept to a minimum, and should include only those that are commonly recognized and understood.
- **[M]** 9D.12-11 (p.1082): The arrow location and priority order of destinations shall follow the provisions described in Sections 2D.08 and 2D.36. Arrows shall be of the designs provided in Section 2D.08.
- **[M]** 9D.12-12 (p.1082): The lettering for destinations on Destination Guide signs for shared-use paths shall be a combination of lower-case letters with initial upper-case letters (see Section 2D.04). All other word messages on Destination Guide signs for shared-use paths shall be in all upper-case letters.
- **[M]** 9D.12-13 (p.1082): Except as provided in Paragraph 15 of this Section, the lettering style used for destination and directional legends on Destination Guide signs for shared-use paths shall comply with the provisions of Section 2D.04.
- [O] 9D.12-14 (p.1082): The distance to the place named may be displayed on the Destination Guide sign. If several destinations are to be displayed at a single point, the several names may be placed on a single sign with an arrow (and the distance, if desired) for each name. If more than one destination lies in the same direction, a single arrow may be used for such a group of destinations.
- [O] 9D.12-15 (p.1082): A lettering style other than the Standard Alphabets provided in the “Standard Highway Signs “ publication (see Section 1A.05) may be used on Destination Guide signs for shared-use paths if an engineering study determines that the legibility and recognition values for the chosen lettering style at minimum letter heights meet or exceed the values for the Standard Alphabets for the same legend height and stroke width.
- **[M]** 9D.12-16 (p.1083): Where a shared-use path is within the highway right-of-way or crosses a street or highway, an alternative lettering style shall not be used.
- [O] 9D.12-17 (p.1083): Pictographs (see definition in Section 1C.02) may be used on Destination Guide signs for shared-use paths.
- **[M]** 9D.12-18 (p.1083): If a pictograph is used, its height shall not exceed 2 times the height of the upper-case letters of the principal legend on the sign.
- **[M]** 9D.12-19 (p.1083): Business logos, commercial graphics, or other forms of advertising (see Section 1D.07) shall not be used on Destination Guide signs for shared-use paths or sign assemblies.
- [O] 9D.12-20 (p.1083): An identification marker may be used in an assembly for Destination Guide signs applied to shared-use paths, or may be incorporated into the overall design of Destination Guide sign, as a means of visually identifying the sign as part of an overall system of signs.
- **[M]** 9D.12-21 (p.1084): The size of an identification marker shall be smaller than the Destination Guide sign. Identification markers shall not be designed to have an appearance that could be mistaken by road users as being a traffic control device.
- **[R]** 9D.12-22 (p.1084): The area of the identification marker should not exceed ¹⁄5 of the area of the Destination Guide sign with which it is mounted in the same sign assembly.
- **[M]** 9D.12-23 (p.1084): Except as provided in Paragraph 26 of this Section, Destination Guide signs for shared-use paths shall have a white legend and border on a green or brown background and shall be consistent with the basic design principles for guide signs.
- **[M]** 9D.12-24 (p.1084): Color coding or pictographs shall not be used to distinguish between different types of destinations. If used, color coding shall be accomplished by the use of different colored square or rectangular panels on the face of the sign, each positioned to the left of the named geographic area to which the color-coding panel applies. The height of the colored square or rectangular panels shall not exceed 2 times the height of the upper-case letters of the principal legend on the sign.
- [O] 9D.12-25 (p.1084): The different colored square or rectangular panels may include either a black or a white (whichever provides the better contrast with the color of the panel) letter, numeral, or other appropriate designation to identify the destination.
- [O] 9D.12-26 (p.1084): Except where a shared-use path is within the highway right-of-way or crosses a street or highway, Destination Guide signs for shared-use paths may use background colors other than green or brown in order to provide a color identification for systematic destinations within the overall guide signing system.
- **[M]** 9D.12-27 (p.1084): The standard colors of red, orange, yellow, purple, or the fluorescent versions thereof, fluorescent yellow-green, and fluorescent pink shall not be used as background colors for Destination Guide signs for shared-use paths, in order to minimize possible confusion with critical, higher-priority regulatory and warning sign color meanings readily understood by path users.
- [O] 9D.12-28 (p.1084): Destination Guide signs for shared-use paths may display telephone numbers, Internet addresses, and e-mail addresses, including domain names and uniform resource locators (URLs).
- **[M]** 9D.12-29 (p.1084): If used, the use of telephone numbers, Internet addresses, and e-mail addresses shall be limited to direct contact information of the jurisdiction with authority of the shared-use path, or contact information for emergency service response, or both. Contact information for advertising purposes shall not be used.

<a id="sec-9D-13"></a>
#### Section 9D.13 Two-Stage Bicycle Turn Box Guide Signs (D11-20 Series)

| Sign | Code | Name | Default class | Off-roadway | Roadway | Size table | Also sized in |
|---|---|---|---|---|---|---|---|
| ![D11-20](symbols/D11-20.png) | **D11-20** | Two-Stage Bicycle Turn Box Advance | Optional (9D.13-04) | — | 12 x 18 | 9A-1 p.1051 | — |
| ![D11-20a](symbols/D11-20a.png) | **D11-20a** | Two-Stage Bicycle Turn Box | Optional (9D.13-04) | — | 12 x 18 | 9A-1 p.1051 | — |

- [O] 9D.13-04 (p.1084): Where a two-stage bicycle turn box is provided, the Two-Stage Bicycle Turn Box guide sign series (see Figure 9D-1) may be used.
- **[M]** 9D.13-05 (p.1084) ◆ D11-20: Where used, the Two-Stage Bicycle Turn Box Advance (D11-20) guide sign shall be mounted in advance of the intersection where the turn box is located.
- **[M]** 9D.13-06 (p.1084) ◆ D11-20a: Where used, the Two-Stage Bicycle Turn Box (D11-20a) guide sign shall be mounted on the far side of the intersection.
- [O] 9D.13-07 (p.1084) ◆ D11-20: Where the Two-Stage Bicycle Turn Box Advance (D11-20) guide sign is used, an additional Two-Stage Bicycle Turn Box Advance guide sign may be mounted on the near side of the intersection where the turn box is located.
- [O] 9D.13-08 (p.1084): If used, an appropriately-sized Street Name (D3-1) sign (see Section 2D.45) may be installed below the TwoStage Bicycle Turn Box Advance guide sign to identify the crossroad where the turn box will be available.
- [O] 9D.13-09 (p.1084): Figure 9D-7 shows an example of Two-Stage Bicycle Turn Box guide signs at a location where the use of the turn box is optional.
