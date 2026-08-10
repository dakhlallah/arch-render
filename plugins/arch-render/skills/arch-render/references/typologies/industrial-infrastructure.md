# Typology Briefs — Industrial & Infrastructure
> ⚠️ **Indicative standards, not code.** Widely-used rules of thumb for design development; verify against
> local code, the operator's standards and (for data centres) the client's chosen resilience tier.
> Data-centre density figures shift year to year — treat them as of 2026 and re-check.
> **Preservation Contract applies** (see `SKILL.md` §2).

Jurisdiction caveat: numbers below reflect common practice in UK/EU and North American markets (IBC/NFPA,
Approved Document B, Eurocodes, FM Global / NFPA 13 sprinkler families, Uptime Institute tiers). Fire
compartment sizes, travel distances and loading factors vary sharply by country and by insurer — the
insurer often binds harder than the code. Metric primary; imperial in parens where the market speaks it.

---

## Warehouse / Logistics Centre

**Program ratios** — Storage + handling typically **85–95%** of GIA in a big-box distribution shed; office
("hub" or "pod") usually **2–5%**, commonly two storeys at the dock face or a corner; ancillary plant,
sprinkler tank/pump house, gatehouse and welfare the remainder. Inside the shed, the split between racked
storage and handling/marshalling (dock apron, staging, pick faces, VAS areas) is the real design decision —
allow a marshalling band of roughly **25–35 m (80–115 ft)** deep behind the dock line before racking starts.
E-commerce fulfilment shifts the balance hard toward handling/mezzanine pick modules; pure bulk storage
shifts toward racking.

**Key metrics** — Clear internal height (to underside of haunch / lowest obstruction) is the headline
number: **10–12 m (33–40 ft)** for standard distribution, **12–18 m** for high-bay, **>20 m** only for
automated/AS-RS or clad-rack. Column grid usually falls in the **12–24 m** family (e.g. 12×24 m, 15×24 m,
24×24 m) — chosen to suit the racking module, not the other way round. Dock doors: a common planning rule
of thumb is roughly **one dock door per 900–1,400 m² (≈10,000–15,000 ft²)** of GIA for general
distribution, far denser for cross-dock (which can approach one door per 300–500 m² and is doors-led by
definition). Floor loading: **30–50 kN/m²** UDL is typical for modern distribution slabs, with rack-leg
point loads (often **60–90 kN per leg**, sometimes more) governing over UDL; confirm with the racking
supplier. Floor flatness matters as much as strength — free-movement (superflat) tolerances for VNA aisles,
defined-movement classes elsewhere. Yard: **35–50 m (115–165 ft)** clear from dock face to the far obstruction
for a 16.5 m articulated vehicle to reverse in one swing; a **16.5 m (53–54 ft)** artic wants a turning
circle of roughly **24–26 m** kerb radius. Site cover typically **40–50%** once yard, parking, drainage and
landscape buffer are taken.

**Code & compliance drivers** — Sprinklers govern: ESFR at roof level is the default for many rack
configurations, but **ESFR imposes a ceiling-height ceiling of its own** and rack heights, commodity class
(plastics are the killer) and flue spaces are all sprinkler-design inputs — in-rack sprinklers appear the
moment ESFR can't cover the commodity/height combination. Fire compartment sizes are jurisdiction- and
insurer-driven; large undivided volumes are usually only bought with sprinklers plus smoke ventilation
plus a fire-engineered case. Deep plans make **egress travel distance** the plan-shaper: aim exits so no
point exceeds the local limit (order of **45–60 m** unprotected in many sprinklered industrial cases, but
verify) — this is why big sheds have doors at intervals along the long elevations, not just at the ends.
Also: hazardous goods / ADR storage separation, battery-charging rooms (hydrogen ventilation for lead-acid;
thermal-runaway separation for Li-ion), external fire spread / boundary distance, and site drainage +
contaminated firewater attenuation. BREEAM/LEED and EPC targets now routinely shape the envelope and roof
(PV-ready roofs, roof loading allowance for PV).

**Spatial standards** — Dock levellers commonly **2.0–2.5 m wide × 2.5–4.0 m long**, serving a dock door
around **2.7–3.0 m wide × 3.0 m high**; dock height set at **1.2–1.3 m (≈4 ft)** to meet standard trailer
beds. Dock door **pitch on the elevation: 12–15 m centres** is the common rhythm (drives the column grid and
the facade). Aisle widths: **3.2–3.5 m** for counterbalance/reach trucks in wide-aisle, **1.6–2.0 m** for
VNA (very narrow aisle, with wire/rail guidance), **~2.5–2.8 m** for narrow-aisle. Cross aisles every
**~20–30 m** for egress and picking flow. HGV parking bays around **3.5 × 18 m**. Trailer marshalling
requires depth beyond the manoeuvring zone — don't count parked trailers inside the swept path.

**Flow & adjacency logic** — The invariant sequence is **goods in → receiving/QC → put-away → store →
pick → pack/VAS → dispatch marshalling → goods out.** Decide early whether it's an **I-flow** (in one end,
out the other — best for high-volume, needs two yards), a **U-flow** (in and out on the same face — shares
one yard, one gatehouse, fewer doors, most common) or **cross-dock** (in one face, straight out the other,
almost no storage). Then: **people, HGVs and forklifts must never share a surface.** Separate the car park
and staff entrance from the HGV gate; run a protected, barriered, marked pedestrian route from the car park
to the office and from the office into the warehouse; put pedestrian crossings of forklift routes at
controlled points only. Office pod sits on the dock face so supervisors can see the yard, and is the only
place a visitor should reach without a hi-vis. Plant, sprinkler tank and pump house sit outside the
operational yard loop — never where a reversing artic has to negotiate them.

**Common mistakes** — Yard too shallow, so the swept path of a 16.5 m artic clips the building, a column or
a parked trailer (this is *the* classic, and it kills schemes at planning). Column grid set by structural
economy and then discovered to be fighting the racking module — you lose a whole rack run per bay forever.
Under-specifying clear height by measuring to the wrong datum (haunch vs. sprinkler vs. lowest service).
Forgetting the sprinkler tank + pump house + attenuation basin footprint until the site is full. Drawing
dock doors without the 1.2 m level change and the levellers, so the section is a lie. Mixing the visitor
car park with the HGV route. Treating the office as an afterthought bolted on where the last bay was left
over. Ignoring PV roof loading, then adding PV later at structural cost.

**Render notes** — These buildings are **enormous** and renders almost always under-scale them: the single
most convincing move is putting a **16.5 m articulated lorry, a stack of Euro pallets (1200×800 mm) and a
human at the dock** in the frame — the eye calibrates off those and only then reads the 12 m eaves as 12 m.
Use honest materials: horizontal or vertically-ribbed **profiled metal composite panel** with a visible
plank rhythm, a masonry or dark-panel plinth up to ~2–3 m, translucent GRP rooflight strips, and don't
pretend it's a museum. The elevation's rhythm *is* the dock doors and the column grid — keep them regular.
Add the unglamorous truth: line markings, dock bumpers, wheel guides, dock shelters/seals, bollards, mast
lighting columns, gatehouse, palisade or mesh fencing, and a wet, reflective yard slab (a damp apron reads
as real). Long lens, low camera at the yard, or a high oblique showing the roof plane and PV. Avoid the
tell-tale fakes: a spotless empty yard, no line markings, glass office wrapping the whole shed, and a
building that reads as three storeys because there's nothing in frame to say otherwise.

---

## Factory / Light Industrial

**Program ratios** — For a typical light-industrial / manufacturing unit: **production floor 55–70%**,
**warehousing (raw material in + finished goods out) 15–25%**, **office/technical/QA 10–15%**, **plant,
compressor, electrical, welfare and circulation the balance (5–15%)** — plant grows fast the moment there's
process cooling, compressed air, extraction or a cleanroom. Speculative multi-let light industrial ("trade
units") behaves differently: small units, ~10% office, one level-access door plus one dock, low eaves.

**Key metrics** — Clear height **6–10 m (20–33 ft)** for general light industrial; **10–14 m+** where
overhead cranes are involved. If there's a crane, **the crane sets the section**: hook height + crane
girder + clearance drives eaves height, and the crane's wheel loads drive the columns and foundations —
never add a crane after the frame. Column grid **8–15 m** in fine-grain production halls (kept clear over
production lines), widening where flexibility is bought. Floor loading **20–50 kN/m²** UDL for general
production, but **machine point loads and vibration criteria usually govern** — heavy presses, CNC and
metrology equipment need isolated/thickened bases and, for precision work, vibration criteria (VC curves)
that a normal slab won't meet. Power is the other headline: state installed load in **kVA/MVA** and
kW/m² early — it decides substation size and location. Ventilation for process (LEV/extraction) and, for
paint/coating, air-change rates and heat recovery.

**Code & compliance drivers** — Process-specific hazards dominate over generic code: **DSEAR/ATEX zoning**
for flammable solvents, dusts and gases (this determines electrical spec and containment); **explosion
relief** panels for dust-handling; flammable/chemical store separation and bunding; **fire compartmentation
between production, warehouse and office** — the office/welfare block is often required to be a separate
compartment with its own protected escape. Deep production halls again make **travel distance** the driver
of exit positions. Occupational: noise limits inside (hearing conservation), and **plant/acoustic limits at
the site boundary** — planning conditions typically fix a boundary noise level relative to background
(commonly expressed as background +0 to +5 dB at the nearest sensitive receptor, per an
BS 4142-type assessment in the UK); this dictates whether extract fans, chillers and dust collectors get
acoustic enclosures or a screened plant compound. Also: process emissions permits, trade effluent consent,
and interceptors on yard drainage.

**Spatial standards** — Production aisles and gangways: keep a **1.2 m minimum** clear pedestrian gangway,
wider (**≥1.5–2.0 m**) where it's a main route; forklift routes as per the warehouse figures above.
Maintenance access all round major machines — allow the machine's **full swing/withdrawal envelope**, not
its static footprint (a machine you can't pull the spindle out of is a machine you can't service). Level
access doors **4–5 m wide × 4.5–5 m high** for plant/vehicle entry; keep a dedicated **plant-replacement
route** from the yard to every big machine — one day it comes out. Service risers/spines, and either an
overhead service gantry or a below-slab trench system for power/air/data to the lines. Welfare and locker
rooms sized on peak shift headcount, not average.

**Flow & adjacency logic** — Follow the material: **raw goods in → store → pre-process → line(s) →
QA/inspection → finished goods store → dispatch.** Get it running one direction; a factory that doubles
back on itself is a factory whose forklifts collide. Keep the process **linear or U-shaped**, and keep
"dirty" (raw, machining, welding, painting) upstream/downstream-separated from "clean" (assembly, QA,
packing). People flow enters via a **single controlled welfare/locker "airlock"** — staff arrive, change,
then enter the floor; visitors reach the office without crossing the floor at all. Plant (compressors,
chillers, dust extraction, substation) sits in a compound on the noise-tolerant boundary, with its own
maintenance access that never crosses the goods route. Offices/technical overlook the floor — a glazed
supervision window into the hall is one of the few honest bits of glass in the building.

**Common mistakes** — Designing the shell then trying to fit the process into it: **the process is the
brief**; get the equipment layout, utilities loads and clear-height/crane requirements from the process
engineer before fixing a grid. Forgetting the **plant footprint and the substation** — then bolting a
chiller compound onto the entrance elevation. Putting the noisy plant on the boundary facing the housing.
Columns landing in the middle of a production line's future extension. Slab too thin/too flexible for the
machines, or no allowance for future machine bases. Ignoring the machine-removal route. Under-sizing
welfare for shift change. Assuming the office block can share escape with the production hall.

**Render notes** — Scale cues again: **pallets, a forklift, a person in hi-vis and PPE, a roller shutter
with its guide rails.** Materials should be plainly industrial — profiled metal cladding, exposed steel
portal frame or lattice inside, a concrete plinth, banded glazing to the office and a clerestory or
north-light monitor to the hall (north-lights read instantly as "factory" and are honest daylight design,
not decoration). Show the plant compound and the extract stacks rather than airbrushing them out — the
absence of visible plant is the most common giveaway of a fake industrial render. Interiors: the hall
should feel **tall and long**, lit by a mix of high-bay lighting and rooflights, with services, ducts,
cable tray and gantry visible overhead; floor markings, safety barriers, and machine guarding present.
Dusk or overcast light suits these buildings better than golden hour — heroic sunlight on a factory reads
as an advert, not a building.

---

## Data Centre

> All density and efficiency figures below are **as of 2026** and are moving fast with AI/HPC rack densities.
> Re-check against the client's actual rack design; do not carry these numbers forward blindly.

**Program ratios** — The critical split is **white space** (the data halls — the racks themselves) vs
**grey space** (everything that keeps them alive: electrical rooms, UPS, battery, switchgear, generators,
fuel, cooling plant, CRAH/CRAC galleries, water treatment) vs **support** (NOC, build/staging rooms,
storage, loading, security, offices, welfare). As of 2026 a common shape is **white space roughly 30–50% of
gross**, with grey space of similar or larger order and support the balance — and **grey space is growing**
as densities and liquid cooling rise. Two truths follow: (1) a data centre is mostly *not* the data hall;
(2) the higher the rack density, the smaller the white-space fraction relative to the plant serving it.
Never plan a data centre by scaling the halls and hoping the plant fits.

**Key metrics** — The building is sized in **megawatts of IT load, not square metres.** Everything back-
solves from that. Rack density (2026): traditional enterprise/colo racks commonly **5–15 kW/rack**; modern
colo/cloud halls commonly **10–30 kW/rack**; **AI/HPC racks now run 40–130 kW+ and rising**, which is
precisely why air cooling gives way to **direct-to-chip liquid** (and, at the extreme, immersion) — that
transition is the single biggest planning variable in this typology today. White space per MW of IT load:
**roughly 500–1,000 m² per MW at classic ~10 kW/rack air-cooled densities**, shrinking dramatically (to a
few hundred m²/MW or less) as density climbs — quote this as a range, tied to the assumed kW/rack, or
don't quote it. **PUE** (total facility power ÷ IT power): well-run modern facilities land around
**1.2–1.4**; hyperscale best-in-class claims sit nearer **1.1**; legacy rooms **1.6–2.0+**. Also track
**WUE** (water) — increasingly a planning battleground — and grid connection capacity (often the true site
constraint). Floor loading in white space is substantial: modern racks are heavy and, fully populated,
loading of **12–20+ kN/m²** is not unusual (verify against the actual rack schedule; liquid-cooled AI
racks are heavier still and can require structural review of the raised floor / slab-on-grade decision).

**Code & compliance drivers** — **Resilience tier is a client decision that becomes an architectural one:**
**N** = no redundancy; **N+1** = one spare unit per system; **2N** = fully duplicated, independent A/B
paths; **2N+1** at the top. Uptime Institute Tiers I–IV are the common language (broadly: Tier III =
concurrently maintainable, Tier IV = fault tolerant with physically separated, compartmented A/B paths).
**2N and Tier IV are plan-shaping, not equipment-shaping**: they demand two physically separated power and
cooling paths that never share a room, a route or a fire compartment. Fire: sprinklers (often pre-action
double-interlock, to avoid water in a live hall on a single false trip), **VESDA / aspirating smoke
detection**, and in some rooms inert-gas or clean-agent suppression; battery rooms (especially Li-ion) are
now a serious fire-engineering topic in their own right and want separation, detection and thermal-runaway
strategy. Generator fuel storage (bunding, quantity limits), generator **emissions and noise permitting**,
and **boundary acoustic limits** (a yard of 20 diesel generators on test is a planning objection waiting to
happen — expect enclosures and residential-grade attenuation). Egress in deep halls; security compliance
to the operator's standard; EU Energy Efficiency Directive / local reporting on PUE and WUE.

**Spatial standards** — Data hall clear height: **4.0–6.0 m** structural, giving **3.0–4.5 m+** clear above
the floor once containment and cable trays are in — taller for high-density and for hot-aisle containment
with a ceiling plenum. **Raised floor: 600–1,200 mm** where used (deeper as densities and underfloor air
volumes rise) — though many high-density and liquid-cooled designs now go **slab-on-grade with overhead
power/data busway and overhead or in-row cooling**, which is a genuine fork in the design, not a detail.
Rack footprint **600 mm (or 800 mm) wide × 1,000–1,200 mm deep × 42–52U tall**. **Hot/cold aisle pitch**:
cold aisle **1.2 m (4 ft, i.e. two 600 mm floor tiles)**, hot aisle **0.9–1.2 m (3–4 ft)** — so a rack
row-to-row pitch of roughly **2.4–3.0 m** including the rack depth. **Containment is mandatory** in any
serious hall (cold-aisle or hot-aisle) — an uncontained hall is an obsolete hall. Corridors and doors sized
for rack delivery on a pallet (**≥1.5–2.0 m** wide routes, level, no steps, from the loading dock through
the build room to every hall); a proper **loading dock + de-crating/build room** so cardboard never enters
white space. Security: layered zones with mantrap/airlock at the white-space boundary.

**Flow & adjacency logic** — **The power path, the cooling path and the security zoning ARE the plan.**
Draw them first. *Power:* grid/HV intake → transformers → MV/LV switchgear → UPS → battery → PDU → busway →
rack, paralleled by generators + fuel; for 2N/Tier IV the **A and B paths must be physically separated
end-to-end** (separate rooms, separate routes, separate fire compartments, ideally separate sides of the
building). *Cooling:* heat rejection (chillers / dry coolers / adiabatic / cooling towers) → chilled water
or refrigerant loop → CRAH/CRAC or in-row/rear-door/direct-to-chip CDUs → cold aisle → rack → hot aisle →
return; keep it short, keep it redundant, and keep the pipework routes out of the electrical rooms.
*Security:* concentric zones — site perimeter → gatehouse/vehicle trap → building lobby → staff/secure zone
→ data hall airlock → cage/suite. A visitor, a delivery, a rack, a diesel tanker and a fibre engineer all
have different routes and none of them should be the same door. Meet-me rooms / carrier entry: **two
diverse fibre entries from different directions**, physically separated — a single duct entry is a single
point of failure that no amount of 2N gear will fix.

**Common mistakes** — **Treating a data centre as a shed with servers in it.** It is a power and cooling
building with a room for racks in the middle; the plant, not the hall, sets the massing. Under-sizing grey
space and the plant yard (generators, fuel, chillers, water, switchgear) so the scheme dies at RIBA 3.
Designing to a fixed kW/rack figure that the client's roadmap has already outgrown — **build for a density
range and a liquid-cooling upgrade path**, not a single number. Letting the A and B power paths share a
room, a riser or a compartment while still calling it 2N. Ignoring **noise and emissions from generator
testing** at the boundary. Forgetting the rack delivery route from truck to hall (steps, thresholds, a lift
too small, a door 100 mm too narrow). Ignoring water availability/WUE on an adiabatic design. Assuming a
600 mm raised floor still works at 50 kW/rack. Treating security as a door schedule instead of a plan.

**Render notes** — Data centres are **long, blank, and huge** — that's the truth of them, and the honest
render leans into it rather than pretending it's a tech campus. The building is essentially a windowless
box; the design energy legitimately goes into the **facade rhythm (louvre banks, fin systems, perforated
metal screens, colour-blocked panels)**, the **plant yard screening** and the **entrance/office piece** —
so render those and let the rest be mass. Scale cues are essential and easy to get wrong: put in a **truck
at the loading dock, a person at the entrance, the generator enclosures and the chiller/dry-cooler array on
the roof or in the yard** — the plant is the giveaway that this is a real facility and not a rendering of a
warehouse. Show the security layer honestly: perimeter fence, vehicle barrier, gatehouse, camera poles.
Interiors: a data hall render is convincing only if it has **containment doors and roofs, real rack fronts
with blanking panels, structured overhead cable tray or busway, floor tiles with a 600 mm grid, and the
cold aisle actually reading as cold (cool white) against a warmer hot aisle.** The fake tells: glowing blue
cinematic lighting with no containment, infinite rows of racks receding into a mist, no cable management,
no plant anywhere in the scheme, glass curtain wall on a data hall, and a building rendered at half its
real size.

---

## Laboratory-Adjacent Clean Facility (brief)

**Program ratios** — Cleanroom/production suite is rarely more than **30–40%** of gross. Interstitial and
technical space — **plant, AHU decks, gowning, airlocks, corridors, service voids** — routinely equals or
exceeds it; a **walk-on ceiling void / interstitial floor of 2.5–3.5 m** above the suite is normal, and in
pharma the plant-to-clean ratio can approach **1:1 or worse**. Offices/QC/labs and warehouse sit outside
the clean envelope.

**Key metrics** — The classification drives everything: **ISO 14644 Class 5–8** (legacy: Class 100 /
10,000 / 100,000) sets air-change rates, air-change rates set AHU size, AHU size sets plant footprint and
floor-to-floor. Indicative air changes per hour: **ISO 8 ≈ 10–25 ACH; ISO 7 ≈ 30–60 ACH; ISO 6 ≈ 70–160 ACH;
ISO 5 typically unidirectional/laminar flow with ~0.36–0.54 m/s face velocity** (verify against the
validation strategy — these are design starting points, not acceptance criteria). Room **pressure cascade**
typically **10–15 Pa between adjacent classified zones**, positive toward the cleaner room (inverted, i.e.
negative, for containment/biosafety — BSL-3 and cytotoxic/potent-compound suites cascade *inward*, and you
cannot mix the two logics in one suite without airlock design). Floor-to-floor of **5.5–7.0 m+** where an
interstitial deck is used.

**Code & compliance drivers** — GMP (EU GMP Annex 1 for sterile products / FDA cGMP) or BSL containment
levels; HEPA filtration at terminal or in-AHU; validation, qualification (IQ/OQ/PQ) and **change control** —
the building must be designed to be *validatable* and to allow maintenance **without breaching the clean
envelope** (hence the interstitial deck: filters and AHUs are serviced from above, never from inside the
room). Fire and egress must be reconciled with the pressure cascade and the airlocks (an escape door that
dumps a classified room to atmosphere is a design failure). Hazardous materials, solvent stores, gas farms
and effluent kill/decontamination systems. Plant noise at boundary as per the factory case.

**Spatial standards** — Gowning is a **sequence, not a room**: de-gown / gown / airlock, one step per class
change, with a step-over bench and a defined dirty-to-clean direction. **Material airlocks (MAL) and
personnel airlocks (PAL) are always separate.** Doors interlocked. Coved, sealed, washable finishes;
flush-glazed vision panels; no ledges, no exposed fixings, no dust traps. Corridors wide enough for
equipment and trolleys (**≥1.8–2.0 m**), with a defined equipment-replacement route.

**Flow & adjacency logic** — Two independent one-way flows that must never cross: **people** (dirty →
gowning → clean, never reversing) and **materials** (raw → MAL → process → product out via a separate MAL),
plus a **waste route that never runs backwards through a clean corridor.** Cleanest zone at the core,
classes stepping down outward (or, for containment, the reverse). Plant sits above/beside, accessed from
the technical zone only.

**Common mistakes** — Under-sizing plant and the interstitial (the single most common failure — the
cleanroom fits, the AHUs don't). Designing a clean suite you have to enter to maintain. Crossing people and
material flows. Reversing the pressure cascade logic (aseptic vs containment) by copying the wrong
precedent. Forgetting the validation/qualification implications of any change. Leaving no equipment-in/out
route once the walls are up.

**Render notes** — Convincing clean-facility renders are about **flush, seamless, joint-free surfaces**:
coved skirtings, flush ceiling panels on a visible sealed grid, HEPA terminal filter faces, vision panels,
interlocked doors with status lights, stainless steel pass-throughs, epoxy/vinyl welded flooring with a
cove up the wall. Scale and truth cues: gowned figures (bunny suits, correct for the class), a step-over
bench in the gowning room, a trolley, a pass-through hatch. The tells of a fake: a lab rendered as a
white-box gallery with skirting boards and downlights, exposed services, sharp floor-wall junctions, and no
airlock anywhere in the plan. Light it evenly and coldly — clean facilities are flat, bright and shadowless
by design, and a dramatic key light is a lie.
