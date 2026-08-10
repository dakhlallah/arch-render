# Technical Coordination — structure · MEP · BIM · accessibility · spec · cost · buildability
> ⚠️ **Architect-level coordination knowledge, not engineering.** This lets you coordinate intelligently
> and spot problems early — it does NOT replace the structural engineer, MEP engineer, fire engineer or
> accessibility consultant, and it is not a substitute for local code. Ranges are indicative and vary by
> market, code and structural system. **Preservation Contract applies** (see `SKILL.md` §2).

> **Every figure below is either source-tagged or stated qualitatively.** An untagged number is a bug —
> report it. Tags mark the tradition a figure comes from, not a guarantee for your jurisdiction: verify locally.

Cross-refs (do not repeat here): code check → `ref-planning.md` §55 · cost & buildability rating → §56 ·
structural logic review → §57 · construction details → §59 · local context → §60 · detailing → §68.
This file is about **coordination between disciplines** — where the drawings of two consultants meet and
one of them is wrong.

---

# 90 · Structural coordination

**Grid discipline.** The grid is the project's spine, not decoration. One grid, named once (letters one
way, numbers the other), used by architecture, structure and MEP. A rational grid buys you: repeatable
formwork, repeatable facade modules, repeatable parking bays, repeatable ductwork. Every grid exception
costs money twice — once in design coordination, once on site. If the plan wants a free-form gesture,
put the gesture in the *skin* or the *roof*, not in the column layout.

**Vertical continuity.** Load-bearing elements must land on load-bearing elements. Columns and shear
walls should stack floor to floor and continue to foundation. The classic architectural sin: a beautiful
open-plan ground floor / lobby / retail unit under a residential grid, so the upper columns land on
nothing. That is a **transfer**.

**Transfer structures** (transfer beams, transfer slabs/plates, hung columns). They are expensive because:
- The transfer element carries the accumulated load of every floor above → very deep, very heavily
  reinforced, sometimes post-tensioned.
- It eats a whole storey of headroom (or forces the floor-to-floor of that level up).
- It is on the critical path — nothing above it proceeds until it's cast and cured.
- It is a single point of structural and programme risk.
Rule: **a transfer is a decision, not an accident.** If you need one, use it deliberately (e.g. one
transfer at podium level between a car-park grid and a residential grid) — never accept three scattered
transfers because nobody checked stacking. Ask early: *can the grid above be nudged to land?* Nudging a
wall in schematic design is free. A transfer beam is not.

**Typical economic spans.** The table below is a *sanity-check* range, not a design value — economic span
depends on loading, depth, fire rating, code, procurement and market. Ranges below are consistent with
published span-range charts in the standard references [AGS] and with everyday practice [common practice];
the depth-to-span ratio you use must come from the structural engineer.

| System | Economic span range [AGS · common practice] | Notes |
|---|---|---|
| RC flat slab (no beams/drops) | ~6–8 m | Flat soffit → best for services & shallow floor build-up. Punching shear at columns governs; drop panels/column heads extend range. |
| RC flat slab with drops / band beams | ~8–10 m | Buys span, costs soffit flatness. |
| Post-tensioned RC slab | ~8–12 m+ | Thinner slab, longer span, fewer columns; needs specialist, complicates future coring/penetrations. |
| RC beam-and-slab | ~6–9 m (slab); beams span further | Deep zone; ducts must cross beams → see §91. |
| Precast hollow-core | ~6–12 m+ | Fast, dry, needs crane access & tolerance discipline. |
| Composite steel beam + metal deck | ~9–15 m (cellular beams further) | Long clear spans; cellular/castellated beams let ducts pass *through* the web — a huge coordination win. |
| Steel long-span truss / portal | ~15–30 m+ | Halls, sports, industrial. |
| Timber CLT floor | ~5–8 m | Light, fast, quiet on carbon; acoustics, fire encapsulation and moisture during construction are the real issues. |
| Glulam beams | ~8–15 m | Exposed structure is the point — so services must be *designed to be seen* or hidden elsewhere. |

Use these as *sanity checks*, never as design values. Beyond the economic span, cost rises steeply and
depth grows fast: the structure stops being a floor and starts being a statement.

**Floor-to-floor budget.** See the arithmetic in §91 — this is where structure and MEP actually meet, and
where a careless slice of extra depth, multiplied by every floor in the stack, becomes an extra storey of
facade nobody budgeted.

**Cantilever reality checks.**
- Rule of thumb only: a cantilever is broadly **a third to a half** of the backspan that anchors it
  [common practice] — beyond that, the backspan needs holding down. If nothing holds it down, it tips.
  The real limit comes from the engineer, not from this rule.
- Deflection, not strength, usually governs. Concrete **creeps**: a cantilever that looks flat on day one
  visibly droops years later. Pre-cambering exists, but it's a compromise.
- Cantilever tips carry the worst vibration and the worst deflection — the exact place architects like to
  put a full-height glass balustrade with a hairline joint. That joint will move.
- Cantilevers are **thermal bridges**. A slab that runs continuous from inside to outside is an energy
  and condensation problem; you need a structural thermal break, and thermal-break products have their
  own load limits that constrain the cantilever. Coordinate this in schematic, not in construction.

**Lateral stability.** The building must resist wind (and, where relevant, seismic). Options: a **core**
(stair/lift shafts working as a concrete tube), **shear walls**, **braced frames**, **moment frames**
(most flexible architecturally, least efficient), or a facade acting as a **tube**. Key architectural
consequences:
- The **core wants to be reasonably central**. A core shoved into a corner creates torsion under wind —
  the building twists — and the engineer will demand more material to fix it.
- Shear walls must be **continuous to foundation** and are extremely unwelcoming to doors and openings.
  Every hole you punch in a shear wall is a negotiation. Pierce a wall in the wrong place and it stops
  being a shear wall.
- Bracing is cheap and honest but occupies the plane of a facade or a partition. Decide early whether it
  is expressed or hidden.
- In seismic zones, symmetry and regularity in plan and section are worth more than any clever detail
  [Eurocode — EN 1998 rewards regularity in plan and elevation; equivalent principles exist in most
  seismic codes]. Soft storeys (a tall, open, glazed ground floor under stiff residential floors) are a
  classic architectural instinct and a classic seismic failure mode. Flag it.

**Where architecture and structure collide — the usual suspects:**
1. Column lands in a parking bay, a door swing, a stair, or the middle of a hotel bathroom.
2. Grid above doesn't stack on grid below → unplanned transfer.
3. Double-height / atrium void removes the diaphragm that was tying the floor together.
4. Stair and lift core moved for planning reasons after the engineer sized it for stability.
5. Facade wants a frameless corner exactly where the engineer wants a column.
6. Roof terrace / planter / pool added late — massive load increase on a slab already designed.
7. Slab edge set out to architectural finish lines instead of structural lines (tolerance disaster, §96).
8. Downstand beam collides with the ceiling height promised in the brief (§91).

---

# 91 · MEP coordination

**The services zone is the #1 cause of floor-to-floor surprises.** Learn the arithmetic and do it on day
one, in schematic design, on the back of an envelope:

```
FLOOR-TO-FLOOR  =  clear height (finished floor → finished ceiling)
                +  ceiling void  (which must contain: duct depth + insulation
                                  + hanger/support zone + drainage falls + lighting depth)
                +  structural depth (slab / beam — use the DEEPEST beam on the route, not the slab)
                +  floor build-up  (screed / raised floor / acoustic layer / finish)
```

**Do not carry generic void or duct depths into this sum.** Duct depth is set by the air volume and the
route: get the depth of the LARGEST duct on the critical route, plus its insulation and hanger zone, from
the MEP engineer *before* fixing floor-to-floor. Get the deepest beam on that same route from the
structural engineer. Anything else is a guess that will be found out in month ten.

Indicative heights, varying with system, code and market:
- **Residential:** clear height commonly ~2.4–2.7 m; floor-to-floor commonly ~2.8–3.2 m [Neufert ·
  common practice] — a small service zone, because services are mostly local (bulkheads, wet-area drops).
  Note many codes also set a *minimum* habitable clear height; check yours.
- **Office:** clear height commonly ~2.6–3.0 m; floor-to-floor commonly ~3.6–4.2 m for a typical
  speculative office [BCO] — the services zone (AHU-fed ducts + sprinklers + lighting + structure) is
  large. Higher-spec and taller-ceiling markets push both figures up.
- **Retail / F&B / labs / hospitals:** bigger again; kitchen extract and medical gases eat void. Get the
  zone from the MEP engineer — there is no useful rule of thumb here.
- **Car park:** driven by the vehicle clear height required *under the lowest obstruction* (a duct, a
  sprinkler pipe, a downstand) — not under the slab. The required clearance is code- and operator-set
  (and accessible/van bays usually demand more). Coordinate ramps and sprinkler mains or you will fail
  on site.

**The lesson:** clear height is a *residual*, not a given. If the client wants a generous clear office,
the engineer wants a deep downstand and the MEP engineer wants a big duct on the same route, one of those
three positions is a lie. Resolve it in week two, not month ten. Coordination trades: use a flat slab (no
downstands), use cellular steel beams (ducts pass *through* the web), zone the services (run the big
ducts in corridors where clear height can drop, keep offices clear), or accept a taller building.

**Risers.**
- Risers **must stack**. Water, drainage, electrical containment and ducts run vertically; a riser that
  jogs floor to floor needs offsets, which means fittings, which means pressure loss, noise, leaks and
  lost floor area. Drainage stacks in particular hate offsets.
- Risers consume a meaningful share of every floorplate, and the share grows with how heavily serviced
  the building is. **Size them with the MEP engineer early** — under-provisioning risers is a classic
  cause of late redesign, and the area you failed to allow for gets stolen from lettable space.
- Size them for **access and future replacement**, not just for today's pipes: you need working space,
  and an access door on a corridor (never through a bedroom or a leased tenancy).
- Provide **spare capacity**. Scope grows; services get added; nobody has ever regretted a slightly
  bigger riser. Agree the spare allowance with the MEP engineer and write it down — a riser sized exactly
  to today's schedule is a riser that will be full on handover day.
- Keep wet risers away from electrical risers. Water and switchgear are old enemies.
- Fire-stopping at every floor penetration — this is a real, drawn, coordinated detail, not a note.

**Plant.**
- **Roof plant**: shorter vertical duct runs to the top floors, no flood risk, easier fresh-air intake and
  discharge, easier future replacement (crane access). Costs: visual impact (it *will* be the tallest
  thing on your elevation — draw it, don't hide it), structural load, acoustic impact on neighbours,
  and often the exact place where the architect wanted a roof terrace.
- **Basement plant**: hidden, structurally easy, but flood-prone, needs mechanical ventilation for itself,
  needs a smoke/ventilation strategy, and needs a replacement route (an equipment hatch/removal route —
  will the chiller ever get out again?).
- **Plant and service space is not a residual — it is a programme item with an area.** How much depends
  entirely on the servicing strategy and the building type: a naturally ventilated, lightly serviced
  building needs little; an office needs real plant rooms; a hospital, a lab or a data-heavy building can
  need a great deal, sometimes whole floors. **Get the plant area from the MEP engineer and put it on the
  plan at concept stage.** The classic mistake is allocating a plant room after the plan is fixed, and
  discovering it doesn't fit.
- Plant needs: intake and discharge separated (no short-circuiting exhaust back into fresh air), maintenance
  access, delivery/replacement route, drainage, and acoustic separation.

**Duct routing vs the structure — what is allowed and what is not:**
- **Never** penetrate a beam near its supports. Shear is highest at the ends. Where a penetration is
  permitted at all, the safe zone is broadly the **middle portion of the span, near the neutral axis
  (mid-depth)** [common practice] — and *only* where the engineer has designed and approved it, at a size
  and spacing they set. Say it plainly: **penetrations are a structural engineer's decision, always.**
- Multiple holes need adequate spacing between them; a row of closely spaced holes is a perforation line.
  The engineer sets the spacing.
- **Never** core or chase a post-tensioned slab without a scan and the engineer's sign-off — you can cut a
  tendon and cause a violent failure.
- **Never** cut a shear wall or a column, ever, for a service. Route around.
- If large ducts must cross a beam grid every bay, **change the structure**, don't fight it: flat slab,
  cellular beams, or run ducts parallel to the beams and cross only where designed to be crossed.
- Design the penetrations **into** the structural drawings at design stage. A hole that's drawn is
  reinforced; a hole that's drilled on site is damage.

**Ceiling void coordination — the order of priority.** Biggest and least flexible goes first:
1. **Drainage / gravity pipework** — it has a *fall* and cannot be moved. Non-negotiable.
2. **Large ducts** (supply, extract, kitchen/car-park extract) — big, rigid, need bend radii.
3. **Structural depth and hangers** — the beams and the things holding everything up.
4. **Sprinklers / wet pipework** — needs falls/drain-down and head coverage geometry.
5. **Small pipes** (heating/chilled water) — some flexibility, but insulation thickness is real and often
   forgotten (an insulated pipe is much fatter than the pipe).
6. **Electrical containment / trays / busbar** — flexible, but needs access and separation from wet services.
7. **Lighting, sensors, speakers, AV** — last in the queue physically, first in the queue visually. Which is
   exactly why they end up nowhere near where the reflected ceiling plan showed them.
Coordinate in that order and the ceiling works. Coordinate in reverse (lighting layout first, "MEP will
find a way") and you get a beautiful RCP and a site full of variation orders.

**Drainage falls are gravity and non-negotiable.** Foul and rainwater drainage runs downhill, at a
minimum gradient set by the local code and the pipe size, from the fixture to the stack to the outfall.
This means:
- A WC far from its stack burns ceiling void *below the floor it serves*: a long horizontal run at a fixed
  fall drops steadily, and everything it drops it takes out of the clear height of the room underneath.
  Move a wet area in plan and you must re-check the room below. Stack wet areas and this problem vanishes.
- Roof drainage, terrace falls, gutters, overflows and gullies must all be drawn and must all fall
  somewhere real. "It drains to the perimeter" is not a drainage strategy.
- Flat roofs are never flat. They need falls, and waterproofing needs an **upstand** at abutments and
  thresholds — traditional waterproofing guidance puts this in the region of ~150 mm above finished level
  [common practice], while accessibility demands a level threshold (§93). That conflict is real, and it is
  resolved with a **drainage channel and a properly detailed junction**, not by wishing it away. Get the
  required upstand from the waterproofing system's own warranty conditions — they, not you, decide.
- Basements below the sewer invert need **pumping** — a pump room, a sump, power, alarms, and a
  maintenance regime. Design it, don't discover it.

**Plant noise and vibration.**
- Airborne noise: plant rooms need mass and separation. Don't put a plant room above a bedroom, next to a
  boardroom, or against a party wall. If you must, you pay for it in acoustic construction.
- **Structure-borne vibration** is the sneaky one: a fan or pump rigidly bolted to a slab transmits
  vibration through the whole frame, and it emerges as a hum three floors away. Anti-vibration mounts,
  inertia bases and flexible connections at every duct/pipe leaving the plant — coordinate the *space*
  for those (they raise the equipment, they need clearance).
- Plant discharge is a *neighbour* issue and a planning-condition issue. Check the boundary noise limit
  that applies to your site — it is set locally and it is enforceable.
- Generators, chillers, cooling towers, and kitchen extract fans are the loudest and most complained-about
  items. Locate them like you mean it.

**Clash hot-spots — check these first, always:**
- Beam vs main duct at the point where the duct leaves the riser (the busiest square metre in the building).
- Drainage from an upper-floor WC vs the ceiling of the space below.
- Sprinkler main vs car-park clear height / ramp headroom.
- Ductwork vs lift overrun and lift pit.
- Structure vs stair headroom (a beam over a stair landing is a permanent duck).
- Riser vs a column that moved.
- Ceiling void depth at corridors (where all the services converge) vs the promised corridor height.
- Plant room door width vs the largest piece of equipment that must one day come out.
- Facade fixing zone vs slab edge tolerance and vs perimeter services (fan coils, trench heating).
- Rooflight / skylight vs roof plant vs PV array vs maintenance access — all four want the same roof.

---

# 92 · BIM coordination

**LOD / LOIN — the honest version.** Level of Development / Level of Information Need answers one
question: *how much can I trust this object?* A wall at an early stage is a placeholder with a thickness;
at a later stage it is a specified build-up with a fire rating and a manufacturer. The failure mode is
**false precision**: a model that *looks* like construction information at concept stage, and gets used
as if it were. State the reliability of the model at each issue. Geometry, information and reliability
are three different things; a beautifully modelled object with no data is decoration. (The formal
framework for information requirements is the ISO 19650 series [ISO] — use its language, and agree the
information need per stage rather than inventing your own ladder.)

**Federated model + clash detection — the workflow:**
1. Each discipline authors its own model (architecture, structure, MEP, sometimes facade/specialist).
2. Models are exchanged on an agreed cycle (weekly and fortnightly are both common; agree yours and hold
   to it) into a **federated** model — they are *linked together*, never merged into one file. Nobody
   edits another discipline's model.
3. Clash detection runs on the federation with agreed rules and tolerances.
4. Clashes are triaged (not "solved" — triaged), assigned an owner, tracked, and closed.
5. Repeat. Coordination is a *rhythm*, not an event.

**Clash types — and what is actually worth resolving:**
- **Hard clash** — two solids occupy the same space. A duct through a beam. These are real and must be
  resolved (or designed as an approved penetration, §91).
- **Soft clash / clearance clash** — objects don't touch but violate a required clearance: maintenance
  access, insulation thickness, code clearance in front of a panel, a door swing. These are *more*
  dangerous than hard clashes because they don't turn red automatically. Set clearance rules deliberately.
- **Workflow / 4D clash** — no geometric clash at all, but a sequencing conflict: the plant can't get into
  the room because the wall is built first; the crane can't reach; two trades need the same space in the
  same week. See §96.
- **What isn't worth resolving:** the raw clash count. A first run can produce a mountain of "clashes"
  that are nothing — insulation touching a hanger, a sprinkler head brushing a ceiling grid, duplicate
  linked geometry. Chasing the number is a vanity metric. **Filter, group by system pair, resolve by
  cause, not by instance.** One column that moved is one decision and a very long clash list.

**Model ownership — write it down before you model anything:**
- Architect: space, envelope, partitions, doors/windows, finishes, ceilings (the *void* is negotiated),
  vertical circulation enclosure, room data.
- Structure: frame, slabs, foundations, cores as structure, approved penetrations.
- MEP: ducts, pipes, drainage, containment, terminals, plant equipment, and the required maintenance
  clearances around them.
- **The contested elements** — always agree these explicitly: who models the ceiling void; who models
  builder's work openings (typically MEP requests them, structure/architect approves them, someone must
  own the object); who models the riser shaft and who models the fire-stopping; who owns the raised floor;
  who owns the facade support brackets. Every one of these is a real project argument. Have it early, in
  a BIM Execution Plan, not on site.

**Common Data Environment (CDE).** One place, one truth, and a defined set of states — Work in Progress →
Shared (coordination) → Published (issued, approved) → Archived [ISO 19650]. The point of a CDE is not
storage — it's **status**. The single most common cause of a building being built wrong is a contractor
working from a superseded file that someone emailed. If it isn't in the CDE with a revision and a status,
it isn't issued. "I sent you the latest one on WhatsApp" is not a document control system.

**IFC / openBIM.** Exchange between authoring tools happens through a neutral format (IFC being the
common one [ISO 16739]). Practical truths:
- IFC exchange is for **coordination and information handover**, not for round-trip editing. Do not model
  in one tool, export, edit the export, and expect to bring it home.
- Classification matters more than geometry on export — an object exported as a generic "proxy" carries no
  meaning and is useless downstream.
- Agree the exchange format, the classification and the coordinate system **before** the first exchange.
- **Shared origin / coordinate system.** Agree a project base point and survey point, and *use them*.
  A huge share of all "the models don't line up" problems are a shared-origin problem, not a design problem.

**"The model is not the drawing."** The model is a coordinated 3D hypothesis. The **drawing (and the
specification) is the contract**. A model can be geometrically perfect and contractually silent: it does
not carry tolerances, workmanship, sequencing, performance requirements, or the words "or equal and
approved". Two consequences: (a) never assume a contractor will build what's in the model if it's not in
the issued documents; (b) never assume a dimension scaled off a model is a dimension you have committed
to. Drawings are dimensioned deliberately; models are modelled approximately.

**What an architect must coordinate BEFORE issuing — the pre-issue checklist:**
- [ ] Grid and levels agreed and identical across all discipline models (§90).
- [ ] Shared origin/coordinate system verified across the federation.
- [ ] Structure received and linked at the current revision (not last month's).
- [ ] MEP received and linked; ceiling void and riser sizes reconciled with the sections (§91).
- [ ] Floor-to-floor arithmetic checked against the actual deepest beam and the actual biggest duct.
- [ ] All builder's work openings requested, drawn and approved by structure — no unapproved holes.
- [ ] Risers stack floor to floor and reach the plant.
- [ ] Drainage from every wet area reaches a stack with a plausible fall.
- [ ] Escape routes, door swings, refuges and accessible clearances still work after coordination (§93) —
      services love to shrink a corridor.
- [ ] Clashes triaged and either closed or explicitly listed as open with an owner and a date.
- [ ] Drawings and model agree — and where they disagree, the drawing is right and the model gets fixed.
- [ ] Revision, status and the list of assumptions/exclusions stated on the issue.
Issue with a known, stated list of open items. Issuing while pretending nothing is open is how projects
lose trust.

---

# 93 · Accessibility & inclusive design
> ⚠️ Requirements are **jurisdiction-specific** (ADA / ICC A117.1 in the US, Approved Document Part M in
> England, EN 17210 and national annexes in Europe, and others elsewhere). The numbers below are
> **indicative orders of magnitude to design with — they are not code.** Where a figure differs between
> traditions, both are given, and the *stricter applicable* one governs. Verify every one against the
> applicable local standard and, on any serious project, an accessibility consultant. Accessible design is
> also a legal obligation in most jurisdictions, not a courtesy.

**Principles first — design the journey, not the checklist.** A building is accessible when a person can
complete the whole sequence independently and with dignity:
**approach → arrive → enter → circulate (horizontal + vertical) → use (WC, seat, counter, controls) →
egress (including in an emergency).**
A compliant WC at the end of a route with an unchamfered lip at the door is not accessible. **The weakest
link defines the whole route.** And "accessible" is not only wheelchair users: it covers ambulant disabled
people, people with visual or hearing impairments, cognitive differences, older people, people with
buggies, people with luggage, and — eventually — everyone.

**Reject the segregated solution.** A grand front stair with a hidden ramp round the back is bad design,
and increasingly bad law. Integrate the level route into the main approach. If the site slopes, make the
landscape do the work.

**Key dimensions — indicative, verify locally:**
- **Wheelchair turning circle / 360° turn:** ~1500 mm diameter is the standard working figure
  [Approved Doc M]; the US equivalent turning space is 60 in ≈ 1525 mm [ADA]. A 90° turn needs less; a
  T-turn is the recognised alternative in tight spaces.
- **Clear door width (the *clear opening*, not the leaf size):** design in the region of ~800–900 mm clear
  [Approved Doc M · ADA] — ADA's minimum clear opening is 32 in ≈ 815 mm [ADA], and Part M sets minimum
  effective clear widths that vary with approach direction and building type [Approved Doc M]. **The clear
  opening is reduced by the leaf thickness and the stop — a "900 mm door" is not a 900 mm clear opening.**
  Also allow the **latch-side clearance** (space beside the handle to pull the door open from a
  wheelchair): ~300 mm on the pull side is the Part M nib [Approved Doc M]; ADA requires more, typically
  18 in ≈ 455 mm for a front pull approach [ADA]. Doors that fail accessibility usually fail here.
- **Corridors:** a clear width allowing passing and turning; local codes set the minimum, and fire escape
  width may set a bigger one. Take the greater.
- **Ramp gradient:** the recognised band runs from ~1:12 (the steepest, and a *maximum* in the codes that
  allow it, for short runs only) to ~1:20 (gentler, longer runs permitted) [ADA · Approved Doc M]. Part M
  ties the permitted gradient to the length of the run — the longer the run, the gentler it must be.
  **Gentler is always better. 1:12 is a limit, not a target.**
- **Ramp landings:** a level landing at top, at bottom, at every change of direction, and at intervals
  along a long run (the maximum rise per flight is code-set — look it up). Landings must be genuinely
  level and long enough to stop, rest, and open a door on — a landing a door swings into is not a landing.
- **Handrails** to both sides of ramps and stairs, continuous, at the code-set height, with extensions
  beyond the top and bottom nosing so a person knows the run has ended [ADA · Approved Doc M].
- **Reach ranges:** controls, switches, handles, card readers and counters must sit in a comfortable
  seated reach band — broadly ~400–1200 mm above floor as an indicative zone [ADA · Approved Doc M];
  the codes define the low and high limits and the effect of an obstruction precisely, so use them. If
  it's above shoulder height or below knee height for a seated person, it's out of reach.
- **Accessible WC:** the plan is not "a bigger cubicle". It is a specific geometry — a clear transfer
  space to **one side** of the WC pan, grab rails in a defined arrangement, basin reachable from the pan,
  outward-opening (or sliding) door, alarm cord reachable **from the floor**. Handedness matters: where
  there are several, provide a **mix of left- and right-hand transfer** layouts. **Take the layout and
  every dimension straight from the applicable standard** [Approved Doc M · ADA] — do not improvise it,
  and do not remember it.
- **Level thresholds:** the target is a genuinely level entry. Where a threshold is unavoidable
  (weathering, drainage), keep the upstand to the minimum the code allows and chamfer it. Resolve the
  waterproofing/level conflict with a **drainage channel and a well-detailed junction**, not with a step.
  This is one of the most common failures in built work — the architect drew "level", the site built a lip.
- **Tactile and wayfinding:** tactile paving at hazards and crossings; visual contrast (luminance contrast,
  not just colour — colour-blind users get nothing from red-on-green) between floor/wall, wall/door,
  door/handle, and on nosings; legible signage at a consistent height with good contrast and sans-serif
  type; hearing enhancement (induction loop) at reception, counters, and assembly spaces; and clear,
  intuitive plan legibility — a plan you can understand is an accessible plan.
- **Parking, drop-off, approach:** accessible bays close to the accessible entrance, with a level route
  from bay to door, and a hatched transfer zone beside/behind the bay. The *number* of accessible bays
  required is set by code as a proportion of total bays — look it up for your jurisdiction, don't guess.
- **Lifts:** at least one accessible lift serving every floor of the accessible route, with a car size that
  accepts a wheelchair (and, for many building types, a stretcher), reachable controls, audible/visual
  floor announcement, and a mirror to reverse out safely. Car and door dimensions are standard-set
  [ISO 8100 / EN 81-70 for accessibility to lifts] — take them from the standard and the lift consultant.

**Evacuation for people who cannot use stairs.** This is the one architects forget, and it is a
life-safety issue, not a nicety.
- Lifts are normally not usable in a fire unless they are specifically **evacuation lifts / firefighting
  lifts** with the required protection, power supply and management.
- Therefore provide **refuge areas** — a protected space (typically within a protected stair enclosure or
  lobby) where a person can wait safely, out of the escape flow, for assisted evacuation. It needs an
  adequate clear space that does not obstruct the stair (the required clear space is code-set), and a
  **two-way communication device** to a managed point. A refuge with no way to call for help is a cupboard.
- The refuge must be paired with a **management plan** (Personal Emergency Evacuation Plans) — the
  architecture provides the space; the operator provides the procedure. Say this to the client explicitly:
  you cannot design your way out of the management obligation.
- Horizontal evacuation (moving to another fire compartment on the same level) is the better strategy in
  hospitals, care and large complex buildings — coordinate it with the fire engineer.

**Coordination note:** accessibility is the discipline most often *destroyed by other disciplines late in
the day.* A duct drops the corridor ceiling, a fan coil eats the wall behind the WC grab rail, a
structural column moves and kills the turning circle, a threshold gains a lip for drainage. **Re-check
accessible clearances after every coordination round** (see the §92 checklist).

---

# 94 · Material specification

**Performance vs prescriptive.**
- **Prescriptive spec:** names the product ("Manufacturer X, product Y, colour Z"). You get exactly what
  you designed. You also carry the risk if it doesn't perform, and you lose competitive pricing.
- **Performance spec:** names the requirement ("a rainscreen achieving [these] fire, weathertightness,
  wind-load, and durability criteria"). The contractor/specialist proposes the product and carries more of
  the risk. You get buildability and price, but you lose control of appearance unless you constrain it.
- **The real answer is a hybrid, and the skill is knowing which to use where.** Specify *performance* for
  things you don't want to design (waterproofing systems, curtain wall engineering, fixings) and
  *prescriptive* for the things the whole concept depends on (the stone, the visible metal, the
  handrail profile). Never performance-spec the thing that *is* the architecture.

**The spec triangle — performance / cost / maintenance.** Every material choice sits somewhere in this
triangle and you cannot max all three. State the trade explicitly to the client:
- High performance + low cost → high maintenance (they will pay later, and resent you).
- High performance + low maintenance → high cost (make the case in whole-life terms, §95).
- Low cost + low maintenance → compromised performance or lifespan.
The most useful question you can ask a client: **"who will own this building a decade or two from now,
and will they have a budget?"** A material that needs annual specialist re-oiling is not a material —
it's a subscription.

**Fire performance / reaction to fire.**
> ⚠️ Classification systems are **jurisdiction-specific** (Euroclass A1/A2/B/C/… under EN 13501 in Europe;
> different systems and test standards elsewhere), and rules on external wall build-ups have tightened
> significantly in many jurisdictions after major fires. **Never assert a class, a rating or a height
> threshold from memory. Verify against the current local regulation and the fire engineer.**
What an architect must actually hold in their head:
- **Reaction to fire** (does the material contribute to the fire) and **fire resistance** (how long an
  element keeps doing its job: loadbearing capacity / integrity / insulation) are **different things**.
  Don't confuse a class with a rating.
- **The system is tested, not the material.** A cladding panel is not "fire rated" — the *build-up* (panel
  + cavity + insulation + membrane + fixings + cavity barriers) is tested as a system. Substituting one
  layer voids the test. This is exactly what "or equal and approved" gets wrong (below).
- Height, occupancy and escape strategy drive the rules. Facades on tall and/or high-risk buildings face
  the strictest limits, often excluding combustible materials entirely. **The height at which those limits
  bite is set locally and has been changing — look it up for this project, every project.**
- Cavity barriers and fire-stopping at every compartment line and every service penetration are part of
  the spec, drawn and coordinated — not a site afterthought.

**Durability and weathering.**
- Design for **how it will look in ten years**, not on handover day. Everything weathers. The question is
  whether it weathers *well* (patinating copper, silvering timber, greying zinc, weathering steel) or
  *badly* (streaking white render, chalking paint, staining light stone under a badly detailed coping).
- **Water is the enemy and gravity is its ally.** Design for run-off: drips, throatings, overhangs,
  coping falls and generous projections. Every horizontal surface is a dirt shelf; every vertical joint is
  a drainage channel. Streaked facades are a *detailing* failure, not a material failure (§68).
- Match material to exposure: salt air, freeze-thaw, UV, tropical rain and humidity (see `ref-planning.md`
  §60), pollution, and mechanical wear at low level. The base of a wall lives a different life to the top.
- **Bimetallic/galvanic corrosion:** don't put dissimilar metals in wet contact. Also check thermal
  movement compatibility across a junction — two materials that expand differently will tear the sealant.

**Buildability of the junction, not just the material.** Nobody builds a material; they build a *junction*.
A gorgeous stone and a gorgeous glass are irrelevant if the place they meet demands a tolerance no site
trade can hold, a trade sequence that doesn't exist, and an operative on a ladder reaching backwards.
Before you commit: draw the corner, draw the head, draw the sill, draw the base, and draw the movement
joint. If you can't draw it, you can't build it (§96, and `ref-planning.md` §59/§68).

**Lead times and availability.**
- Long-lead items (unitised curtain walling, lifts, switchgear, chillers, generators, bespoke joinery,
  specific stone from a specific quarry, architectural metalwork) are ordered far ahead of installation,
  and on many projects they, not the design, are the critical path. **Get the actual lead time from the
  supplier for this project, in this market, this year** — lead times move with demand and they have moved
  violently in recent years. Identify long-lead items early and get them into procurement.
- **Availability is local** (`ref-planning.md` §60). A material that is standard in one market may be an
  import, a customs problem and a long wait in another. Specifying it anyway is a fantasy, and the
  substitution you'll be forced to accept will be worse than the one you'd have chosen deliberately.
- Check the **trade** exists locally, not just the material. A material with no one competent to install
  it is a defect waiting to happen.

**"Or equal and approved" — what it really means.** It means the contractor may propose an alternative,
and **you** must judge equivalence — and if you don't judge it properly, you have effectively let the
contractor specify your building. Do this:
1. State **which properties define equivalence** — appearance, finish, tolerance, fire class, warranty,
   system test evidence, embodied carbon, maintenance regime. If you don't say what "equal" means, "equal"
   means "cheaper".
2. Require the substitution request in writing with **test evidence for the system**, not a datasheet for
   a component.
3. Require a **sample and/or a mock-up** for anything visible.
4. Reserve the right to refuse. And be prepared to actually refuse.
5. Never let a substitution slide through late in the programme because it's "just" one layer — see fire,
   above. One layer is the whole system.

---

# 95 · Cost-aware design & value engineering

**Where the cost actually sits.** Proportions vary enormously by building type, procurement route and
market — **do not carry percentages around in your head; get the cost plan from the QA/cost consultant.**
What *is* stable is the *structure* of the problem: cost concentrates in a small number of packages, and
design decisions in those packages move the number far more than anything else.
- **Facade / envelope** — typically one of the single largest packages, and directly proportional to the
  *area of envelope*, which you control with form (below). Complexity multiplies it: every unique panel,
  every non-orthogonal corner, every different glass type.
- **Structure and substructure** — frame, plus foundations, plus anything below ground.
- **MEP** — often a very large share, and rising as buildings get more serviced and more regulated. It is
  driven by servicing *strategy*, not by fittings.
- **Groundworks / basement / site** — the biggest source of nasty surprises: poor ground, high water table,
  contamination, retaining, diversions, existing services. **A basement is expensive per m² and its cost
  is highly site-dependent.** Question every basement level. The deeper you go, the worse the rate gets —
  a second basement level typically costs more per m² than the first.
- **Fit-out and finishes** — highly visible, and therefore the first thing everyone attacks in VE, which is
  usually wrong (below).
- **Prelims / preliminaries and programme** — time literally costs money. A design that adds months to the
  programme adds those months of site overheads.

**Form factor is the cheapest lever you have.** Cost and energy both scale with the **ratio of envelope
area to enclosed volume**. A compact, deep-plan, rational form has less facade per m² of floor, less
heat loss, less structure per m², and less scaffolding. Articulation, wings, notches, setbacks, atria
and cranked plans all *add envelope*. This is not an argument for boxes — it is an argument for
**spending your complexity budget where it does work.** Get the base form efficient, then be lavish in
one or two places that the whole building is remembered for.

**Repetition and standardisation.** The second one is always cheaper than the first. Repetition buys:
reusable formwork, a single facade module produced on a line, one window type ordered in bulk, a trade
that learns the detail and gets faster with every repeat, and fewer coordination errors. Rationalise:
- one structural grid, few spans,
- a small family of window/panel sizes (a handful of types, not dozens — and actually count them on your
  own drawings; the number will be higher than you think),
- stacked wet areas and stacked risers (§91),
- repeated unit/room types.
You can have variety in *arrangement* without variety in *components*. That is the whole trick.

**Value engineering done RIGHT.** VE is not "make it cheaper". VE is **deliver the same value for less
cost** — which means you must first say, out loud, what the value *is*.
- Protect the concept. Identify the two or three moves the building cannot lose (the section, the light,
  the one material you actually touch, the public room). Ring-fence them, in writing, at the start of the
  VE process — before the spreadsheet arrives.
- Then cut **systemically**, not cosmetically: simplify the structural grid; reduce the envelope area;
  reduce the number of unique components; shorten the servicing runs; delete a basement level; reduce
  floor-to-floor by fixing the coordination (§91) instead of by lowering the ceiling; rationalise the
  facade into fewer types at the same quality.
- Spend the saving *back* into the ring-fenced moves. That's the job.

**Value engineering done WRONG — "salami slicing".** Shaving a little off the quality of everything, over
and over, until nothing is any good and the building has no reason to exist. Symptoms: the stone becomes
a stone-effect panel, the panel becomes render, the render becomes paint; the timber window becomes PVC;
the double-height lobby quietly loses its height; the landscape becomes tarmac. Each cut is individually
defensible and collectively fatal. **Cost has been reduced; value has been destroyed.** Say this to the
client in those words — it is your job to say it, and it is the moment the architect earns the fee.

**The 5 questions to ask before cutting anything:**
1. **What value does this element deliver — and to whom?** (User experience, brand, rent, planning consent,
   compliance, energy, durability.)
2. **Is it load-bearing for the concept?** If removing it means the building no longer does the thing it
   was designed to do, it is not a candidate — find the money elsewhere.
3. **What does it cost over the building's life, not on day one?** A cheaper facade with a shorter
   maintenance cycle can overtake the expensive one well inside the client's ownership horizon. Argue
   whole-life, with the cost consultant's numbers — not with a hunch, and not with mine.
4. **What does this cut drag with it?** Cuts have consequences: a cheaper glass spec changes the solar
   gain, which changes the cooling load, which changes the plant, which changes the riser, which changes
   the plan. Many "savings" are just cost transfers into another package. Check the chain.
5. **Is there a systemic alternative that saves more and hurts less?** Almost always yes, and almost
   always it is upstream — in the form, the grid, the repetition or the coordination — not in the finishes.
If you cannot answer all five, you are not doing VE; you are just cutting.

---

# 96 · Buildability review

**Sequence — can it actually be built, in an order that works?** Walk the build in your head, in time.
- Can the crane reach it? Is there a crane? What's the heaviest lift, and the longest reach?
- Does the thing that gets installed first need to be there before the thing that encloses it? (The classic:
  the plant cannot be craned in because the roof was completed. Or: the structure is complete, and now the
  oversized glass panel has to pass through an undersized opening.)
- Scaffolding and temporary works: how do you support the cantilever *while* you build it? What holds the
  retaining wall up while you dig? Temporary works are real works, and they are a real cost.
- Wet trades vs dry trades: concrete needs curing time and it is on the critical path. Drying-out time is
  real. A finish that goes on before the building is watertight will fail.
- Follow-on trades: can trade B work while trade A is still there, or does the programme force them to
  serialise? Serialised trades = time = money.
- **Ask: what is the last thing to be installed and how does it get in?** Answer this for the biggest
  plant item, the longest facade panel, and the lift. Then ask **how does it get out again in 20 years?**

**Tolerances — why the CAD-perfect junction fails on site.** CAD has infinite precision. Site does not.
Every material and every trade has its own **tolerance**, and the spread between them is large: cast
in-situ structural concrete is a *coarse* trade, structural steel is finer, and factory-made components
(curtain wall, joinery) are finer still — often by an order of magnitude [common practice]. The permitted
deviations are set by national execution standards and by the specification, so **take the actual numbers
from the applicable standard and state them in the spec** — never assume them. The rules that follow do
not depend on the numbers:
- **A junction between a coarse trade and a fine trade must contain a tolerance-absorbing device**:
  an adjustable bracket, a shadow gap, a packing zone, a cover flashing, a movement joint, a scribed
  fillet. If two elements meet with a hairline joint and no adjustment, one of them will be visibly out.
- **Design the tolerance, don't hope for it.** The most beautiful detail in the world is the one that
  still looks intentional when the slab edge comes out where the concrete trade — not you — put it. A
  **shadow gap is not a style — it's a tolerance strategy that happens to look good.**
- Set out from **structural** lines with a stated tolerance, and let the finish absorb the difference.
  Setting the structure out to architectural finish lines is how you eat the tolerance twice.
- Beware "tolerance stack-up": several components each within their (individually acceptable) tolerance can
  accumulate into a visibly wrong result at the end of a run. Check the run, not the piece.
- Movement is not tolerance, and you need both: thermal, structural (deflection, creep, shrinkage), and
  settlement movement all need joints. A slab above a window head **deflects** — if the window is packed
  tight to the soffit, the slab will break the glass. Leave a head deflection gap, and get the required
  allowance from the structural engineer, who is the only person who knows how much the slab will move.

**Access — for construction AND for the whole life of the building.**
- Construction access: site boundary, delivery route, laydown space, crane position, hoist position. On a
  tight urban site these constraints can legitimately reshape the design — better to know in schematic.
- **Maintenance and replacement access is a design responsibility, not the operator's problem.** For every
  element ask: how do you clean it, how do you inspect it, how do you replace a broken one?
  - Glass: how does the cleaning cradle/BMU reach it? Where does the BMU live, and what does it weigh
    (it's a structural load and it's on your roof, competing with plant, PV and terrace)?
  - Lamps, filters, valves, dampers, sensors: is there an access panel, is it reachable, and is it in an
    acceptable place visually? Every access panel is an architectural decision that MEP will otherwise
    make for you.
  - Plant: replacement route and doorway sizes (§91).
  - Facade panel: can one broken panel be replaced from outside, or does it require dismantling the
    facade from a corner? Ask this of every unitised system.
- If you can't reach it, you can't maintain it — and it will simply stop working and stay broken.

**Standard vs bespoke.**
- Standard components: known price, known lead time, known performance, known warranty, someone knows how
  to fit them, and a spare still exists years later.
- Bespoke: prototype risk, unknown price until tendered, longer lead, a single supplier holding you
  hostage, no spares, and a real chance that the first one produced is not what you drew.
- **Be bespoke on purpose and rarely.** Concentrate bespoke effort where it is seen and felt. Use standard
  components everywhere else — and detail them well, because a well-detailed standard component beats a
  badly-detailed bespoke one, every time and for less money.
- Any bespoke element that matters deserves a **prototype / mock-up** approved before production.
  A visual mock-up (looks) and a performance mock-up (does it leak) are different tests; on a serious
  facade you want both.

**Trades interface risk.** Most defects don't happen inside a package — they happen **between** packages.
The waterproofer, the cladder and the window installer all meet at the sill; the leak will be at the sill;
and each will blame the other two.
- **Name an owner for every interface.** The junction belongs to somebody, in writing.
- Reduce the *number* of interfaces where you can (fewer materials meeting at a corner; one specialist for
  a whole build-up rather than three).
- Where an interface is unavoidable and critical (waterproofing junctions, facade-to-roof, facade-to-ground,
  balcony thresholds, penetrations through the waterline), **draw it, big, and sequence it explicitly.**
  These few details are where the litigation lives.
- Watch the sequence of responsibility: a membrane laid by trade A and then walked on and punctured by
  trade B is A's detail, B's damage and your problem.

**What a contractor prices as RISK** (i.e. what you are paying a premium for, whether you know it or not):
- Anything undefined, ambiguous or "to be confirmed" — ambiguity is priced high, always. **Every "TBC" on
  a tender drawing is a blank cheque you signed.**
- Bespoke items with no precedent and no price history.
- Difficult access, restricted hours, tight urban sites, live/occupied buildings, phased handovers.
- Unknown ground (no site investigation = a big number, or a big claim later).
- Complex interfaces with unclear ownership.
- Tight or unrealistic tolerances, and tight or unrealistic programmes.
- Design that is visibly incomplete at tender — the contractor prices the *worst* reasonable interpretation,
  and then claims the difference anyway.
**Corollary, and the most useful sentence in this file: clarity is cheaper than ambiguity.** A well-drawn,
well-specified, fully coordinated design is not an academic virtue — it is the cheapest way to build.
