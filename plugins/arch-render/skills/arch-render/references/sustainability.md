# Sustainability & Net-Zero
> ⚠️ **Design-development guidance, not energy modelling.** Real performance requires a modeller and a
> climate file; nothing here substitutes for that. Figures are indicative and vary sharply by climate,
> code and construction market. **Preservation Contract applies** (see `SKILL.md` §2) — sustainability
> improvements are proposed, never imposed on the user's design.

> **Every figure below is either source-tagged or stated qualitatively.** An untagged number is a bug.
> Sustainability figures date fast and are climate-specific — take real targets from a current framework
> (Passivhaus / LETI / RIBA 2030 / ASHRAE) and real carbon values from product EPDs, not from memory.

## Sections in this file

- §97 · Passive-first design (the hierarchy)
- §98 · Climate-responsive design by climate zone
- §99 · Operational vs embodied carbon
- §100 · Net-zero: what it actually means
- §101 · Envelope & fabric
- §102 · Water, biodiversity & site
- §103 · Certifications (orientation only)
- §104 · Sustainability review output

---

# 97 · Passive-first design (the hierarchy)

There is one correct order of operations. It is not negotiable, and most "sustainable" projects get it
backwards. This is the **energy hierarchy** — reduce demand, then supply efficiently, then generate
renewably, then offset — and it is the shared spine of every serious framework [common practice; the
fabric-first ordering used by Passivhaus, LETI and RIBA 2030].

**1 · Reduce demand — before anything is specified.**
Form and orientation · compactness (form factor = envelope area ÷ treated floor area; a lower ratio
loses less) · glazing ratio and glazing distribution · shading geometry · daylight so the lights stay
off · natural ventilation so the fans stay off · thermal mass or lightweight construction matched to
the climate · plan depth (a floor plate too deep to daylight or cross-ventilate has already failed) ·
buffer spaces, courtyards, atria, verandas, double-skin. **All of this is decided in week one of
concept design and costs nothing.** A building rotated 20° for a better solar aspect costs the same as
one rotated wrong. This is the only stage where you can still remove load rather than serve it.

**2 · Meet the remaining load efficiently — systems.**
Heat pumps over combustion. Heat recovery ventilation where the climate justifies it. Efficient
lighting with daylight and occupancy control. Right-sized plant — oversizing is a permanent efficiency
penalty, not a safety margin. Controls that a real occupant can actually operate; the most common
in-use failure is a good system running in a bad mode for ten years.

**3 · Then, and only then, renewables.**
On-site PV, solar thermal, whatever the site supports. Size it against a *reduced* load, so it is
smaller, cheaper, and can plausibly cover the demand.

**4 · Last, offset the irreducible remainder — reluctantly, and say so.**

**Why renewables-first is greenwashing.** Putting PV on an unshaded, over-glazed, badly oriented,
leaky building is paying to generate energy the building never needed to consume. It is expensive
(panels, inverters, mounting, eventual replacement well within the building's life, embodied carbon in
the array itself — take service life and warranty terms from the actual product datasheet, not from a
rule of thumb), it degrades, and it does nothing for peak cooling load, glare, overheating, or occupant
comfort — all
of which the passive layer would have fixed for free. Worse, the array becomes the story: the render
shows the panels, the press release counts the kilowatt-peak, and nobody publishes the Energy Use
Intensity. **Orientation, massing and shading are free. PV is a purchase.** Spend the free money
first. If a client wants the array before the envelope, that is a marketing decision, not an
engineering one — name it politely and move on.

**Corollary — the demand-reduction moves are also the architecture.** Courtyards, deep reveals,
brise-soleil, loggias, roof overhangs, mass walls, stack towers: passive design is not a bolt-on
technical layer, it is the formal language of nearly every good building built before mechanical
cooling. Treating it as engineering-after-the-fact is what produces buildings that need saving.

---

# 98 · Climate-responsive design by climate zone

What works in Kinshasa is wrong in Copenhagen. Anyone offering a single "sustainable" template across
climates is selling a style, not a strategy. The five broad families below cover most briefs; always
check the actual climate file, the diurnal swing, and the local code — the boundaries between these
zones are fuzzy and the moves blend.

The moves below are **directional, and drawn from vernacular practice** [common practice] — they tell
you *which way* to push, not how far. Every threshold that follows (how much mass, how low a glazing
ratio, how deep an overhang) is a modelled quantity, not a memorised one: take the formal climate-zone
definition and the design conditions from a recognised source [ASHRAE 169 / ASHRAE 90.1 climate zones;
CIBSE Guide A in the UK] and size the actual device against the real solar geometry for your latitude.

## Hot-arid (Cairo, Phoenix, Riyadh, Marrakech)
Big diurnal swing (hot day, cool night), intense sun, dry air, dust.
- **Thermal mass — yes, heavily.** Mass absorbs the day's heat and releases it at night; the swing is
  the resource. Pair mass with **night purge ventilation** — shut the building down by day, flush it
  after dark. Mass without night flushing is a heat battery you never discharge; it makes things worse.
- **Shading:** total and permanent. Deep reveals, mashrabiya/screens, thick walls, arcades, overhangs.
  Sun is the enemy on every facade including the roof.
- **Glazing ratio:** low — indicatively small, punched openings, not walls of glass. Daylight via
  reflection, courtyards and light wells, not by area of aperture.
- **Roof:** high solar reflectance (light colour), insulated, ideally a second sacrificial layer
  (parasol/vented roof) so the sun never touches the actual roof deck.
- **Courtyard logic:** the courtyard is a cool sink and a stack driver — shaded, ideally with water and
  planting for evaporative cooling. This typology exists in every hot-arid vernacular for a reason.
- **Wrong here:** lightweight construction, large glazed walls, and cross-ventilating in the middle of a
  dusty, furnace-hot afternoon — you are importing the outdoor air you spent all morning excluding.

## Hot-humid (Kinshasa, Singapore, Lagos, Miami, Mumbai coast)
Small diurnal swing, high humidity, latent load dominates, diffuse bright sky.
- **Thermal mass — no, or minimal.** Nights are not cool enough to discharge it. Prefer **lightweight,
  well-shaded, well-ventilated** construction. This is the single biggest reversal from hot-arid, and
  the most common mistake made by architects importing a Gulf detail into equatorial Africa.
- **Ventilation is the whole strategy:** maximum cross-ventilation, elongated thin plan on the
  prevailing-breeze axis, high ceilings, operable openings on both sides of every room, ceiling fans
  (air movement over skin is the comfort lever when you cannot dry the air), raised floors, stack and
  ridge venting. Air movement > air temperature here.
- **Shading:** shade everything, but for a *bright diffuse sky* as well as direct sun. Deep overhangs,
  verandas, screens, broad eaves — the roof does most of the work.
- **Glazing:** moderate area but always shaded and always operable; glare and solar gain, not heat
  loss, set the rules. Avoid unshaded glass entirely.
- **Roof:** the primary architectural element — large, overhanging, ventilated, reflective, insulated.
  A shaded ventilated roof plane is worth more than any facade move.
- **Also:** rain is torrential (drainage, overhangs, splash), mould and rot are real (ventilate cavities,
  detail for drying), and where mechanical cooling exists, **dehumidification** is the load, not
  temperature.

## Temperate (London, Paris, Melbourne, Seattle, Beirut)
Mixed heating and cooling seasons; the season that dominates depends on the specific city — check.
- **Mass:** moderate, exposed internally, useful for smoothing summer peaks — but never a substitute
  for insulation.
- **Ventilation:** natural/mixed-mode is genuinely achievable here; openable windows plus night purge in
  summer, heat recovery in winter. Mixed-mode buildings are the temperate sweet spot.
- **Glazing:** the classic **asymmetric distribution** — more on the equator-facing side (south in the
  northern hemisphere) for useful winter gain with a fixed overhang that cuts the high summer sun; less
  on the pole-facing side (heat loss, no gain); genuinely restrained on east and west (see §101).
- **Insulation:** substantial and continuous; airtightness matters and is cheap.
- **Overheating is the emerging risk** — temperate codes were written for heating and many recent
  well-insulated, over-glazed temperate buildings now overheat badly. Design for the summer you will
  have, not the one in the historic weather file.

## Cold (Copenhagen, Stockholm, Toronto, Moscow)
Heating dominates; the fabric is everything.
- **Compactness:** low form factor. Surface area is loss. Complex, articulated, thin-fingered plans are
  a thermal liability.
- **Envelope:** very high insulation thickness, ruthless **airtightness**, triple glazing, obsessive
  thermal-bridge control. Mechanical ventilation with heat recovery is effectively mandatory once the
  envelope is that tight — you cannot rely on leaks for fresh air.
- **Glazing:** modest overall, concentrated where there is useful solar gain; large north (pole-facing)
  glass is a hole in the wall. Passive solar gain is a real asset in cold-sunny climates.
- **Mass:** useful internally to store the gain, but insulation and airtightness outrank it.
- **Summer shading still required** — cold-climate buildings with big south glass and no shading cook in
  July. Design the overhang anyway.
- **Wrong here:** courtyards as a cooling device (they just add envelope), lightweight breezy pavilions.

## Tropical (highland and lowland: Nairobi, Bali, Manaus, tropical Australia)
Overlaps hot-humid at low altitude, but altitude changes everything — tropical highland (Nairobi, Addis,
Bogotá) can be mild-to-cool year-round with strong sun and needs a nearly temperate fabric under a
tropical roof. Read the altitude before the latitude.
- **Lowland tropical:** treat as hot-humid — big shading roof, elevated lightweight construction,
  through-ventilation, generous eaves, verandas as inhabited buffer, screens for insects and rain.
- **Highland tropical:** intense direct sun and cool nights → some mass becomes useful again, shading
  stays essential, and modest heating (or just a good envelope) may be needed at night.
- **Both:** the sun is near-vertical at noon, so **horizontal shading is unusually effective on all
  faces** — but the low sun at sunrise and sunset still hits east/west hard, and monsoon/wet-season
  rain drives the roof and drainage design.

**Universal rule regardless of zone:** get the plan depth, the orientation, and the roof right before
arguing about specification. And check the real climate file — "temperate" Beirut and "temperate"
Seattle are not the same building.

---

# 99 · Operational vs embodied carbon

- **Operational carbon** = emissions from running the building — heating, cooling, ventilation,
  lighting, hot water, plug loads — over its life.
- **Embodied carbon** = emissions from making, transporting, installing, maintaining, replacing and
  eventually demolishing the *stuff* — from cradle to grave. It is spent **up front**, on day one,
  before a single occupant walks in.

**Why embodied now dominates.** Two things happened. Envelopes and systems got much better (so
operational carbon per year fell), and grids decarbonised (so each remaining operational kWh emits less,
and will emit less still every year the building stands). Embodied carbon has not fallen anything like
as fast: cement and primary metals remain carbon-intensive, and the emission is not spread over the
building's life — it is dumped into the atmosphere on day one, in the decade that matters most for
cumulative warming [IPCC — near-term cumulative emissions govern peak warming]. For a new, genuinely
efficient building on a decarbonising grid, embodied carbon can be the **majority of whole-life carbon**,
and a large share of it sits in the structure and substructure [LETI; RIBA 2030 Climate Challenge — both
frameworks now set embodied-carbon targets alongside operational ones]. Chasing the last increments of
operational performance by adding more material is often carbon-negative in the honest sense of the
phrase.

**Getting real numbers.** Do not quote carbon intensities from memory, and do not accept them from a
supplier's brochure. Take them from a product-specific **EPD** (Environmental Product Declaration, to
EN 15804 / ISO 14025) for the actual product being specified, and assess the building against a
recognised methodology [RICS Whole Life Carbon Assessment; EN 15978]. Generic "typical" values for the
same nominal material vary enormously with mix design, recycled content, the electricity grid where it
was made, and transport distance — quoting one as a fact is how greenwashing starts, in both directions.

**Indicative hierarchy of material carbon intensity** — **direction of travel only. These tiers are
ordinal, not quantitative; never convert them into a figure.** Actual values come from the specific EPD:

| Tier | Typical materials | Note |
|---|---|---|
| Highest | Aluminium, virgin steel, cement-rich concrete, plastics/foams, plate glass (esp. triple/curtain wall) | Cement and primary metals carry the bulk of most projects |
| High–moderate | Standard RC frame, blockwork, mortar, plasterboard, mineral wool | Reducible with mix optimisation, GGBS/fly-ash substitution, less material |
| Lower | Brick (fired but durable), lime, cellulose, hemp, straw, cork, natural insulation | Durability matters — a low-carbon material that has to be replaced repeatedly over the study period is not, in whole-life terms, low-carbon |
| Low / sequestering | Timber (glulam, CLT, softwood frame), bamboo, other bio-based | Sequestration is real but **conditional** on sustainable forestry and on the carbon staying locked up — i.e. long life and no landfill/burn at end of life. Do not treat it as a free pass |
| Lowest of all | **Existing structure retained. Reused elements. Nothing built.** | The carbon is already spent; you emit almost nothing by keeping it |

**"The greenest building is the one that already exists."** The order is:

> **Reuse (keep the building) > Retrofit (keep the structure, upgrade it) > Build new (last resort, and prove it).**

Demolition-and-rebuild almost never pays back within a meaningful timeframe, because you spend a large
lump of embodied carbon today to save a stream of operational carbon that a decarbonising grid is
already shrinking. If a client proposes demolishing a structurally sound building to build a more
efficient one, that claim needs a whole-life carbon assessment, not a rendering. Very often the honest
answer is: keep the frame, strip the envelope, fix the fabric, replace the plant.

**Whole-life carbon thinking** = operational + embodied, across every life stage (product, construction,
use, maintenance and replacement, end of life), assessed against a stated study period. Practical design
consequences: design for **long life** (a building nobody wants in a generation is a carbon disaster
regardless of its U-values); design for **loose fit** (structure that can change use); design for
**disassembly** (bolted over glued, exposed over buried, so material can leave as material rather than
rubble); and **use less stuff** — the cheapest tonne of embodied carbon is the one you did not specify.
Structural efficiency (shorter spans, less transfer, no unnecessary basement) beats material swaps.

---

# 100 · Net-zero: what it actually means

These three are routinely conflated, usually deliberately. Keep them apart.

- **Net-zero operational carbon** — over a year, the building's operational emissions net to zero,
  typically via a very low demand plus on-site (or contracted off-site) renewable generation. Says
  **nothing** about the carbon spent building it.
- **Net-zero whole-life carbon** — operational *and* embodied, across the life cycle, net to zero. This
  is the hard one, is rare, and usually leans on offsets somewhere.
- **"Net-zero ready"** — a marketing phrase. Usually means *the building is efficient enough and
  electrified enough that it could be net-zero if someone later added renewables and/or the grid
  decarbonised.* It is a promise about someone else's future action. Treat it as an aspiration, not a
  performance claim.

**EUI is the honest metric.** Energy Use Intensity — annual delivered energy per square metre of floor
area (kWh/m²·yr) — is hard to fake. It does not care about your PV array, your certificate, your
offsets, or your press release. It is what the meters say. Two buildings both claiming "net zero" can
differ several-fold in EUI; the low-EUI one is the better building, permanently, on any grid, under any
tariff, for any owner.

**Do not carry an EUI target in your head, and never state one from memory.** There is no universal
number: targets vary enormously by typology (a data-rich lab and a naturally ventilated school are not
comparable), by climate, and by code, and the published targets are revised as frameworks tighten. Take
the target from a **current, named framework** appropriate to the project — Passivhaus, LETI, RIBA 2030
Climate Challenge, or the local energy code / ASHRAE or CIBSE benchmark — **cite which one you used**,
and have a modeller set it against the real climate file and local benchmarks. **Then demand the number,
and demand it be tracked in operation**, because the design-to-in-use performance gap is large and
routine. A cited target from a real framework is worth more than a confident number from nowhere.

**Why offsets are the weak form.** An offset is a payment made so that emissions can continue.
Quality varies from real to fictional, permanence is often unverifiable, and the emissions are certain
while the sequestration is a promise. A building that hits "net zero" by buying credits has not changed
its physics: it still burns the energy, still costs the occupant the bill, still stresses the grid at
peak, and stops being net zero the moment someone stops paying. **A low-EUI building is net zero by
construction; an offset building is net zero by accounting.** Offsets belong at step 4 of §97, for the
irreducible remainder, and should be declared as such rather than folded into the headline.

**What to ask a client who says "make it net zero":**
1. **Net-zero *what*?** Operational only, or whole-life including embodied? (This changes the project.)
2. **Certified or actual?** Are we chasing a certificate/planning condition, or measured performance?
3. **What EUI target, and who will model it?** No modeller, no climate file, no number → no claim.
4. **On-site renewables, or purchased/offset?** How much of the "net" is generation you can point at?
5. **Is there an existing building on this site?** (If yes, §99 — reuse may beat everything else you are
   about to do.)
6. **Who operates it, and will performance be measured after handover?** In-use metering and a
   post-occupancy review, or the number is fiction.
7. **What is the budget and the code baseline?** Net-zero-by-fabric costs more up front and less
   forever; net-zero-by-offset costs less up front and forever.

Then design to the answers. If the honest answer is "we want the label", say that a low-EUI,
fabric-first, largely-reused building will beat the label and outlive it — then let the client decide.

---

# 101 · Envelope & fabric

The envelope is where sustainability is actually won or lost, and it is won or lost **in the details**,
at 1:5, not in the concept sketch.

**Airtightness.** Uncontrolled air leakage can be a substantial share of heat loss in a poorly built
envelope, and it also drives moisture into the construction where it condenses and rots things. It is
close to free at design stage and expensive to fix afterwards. Rules: draw a **single continuous
airtightness line** on every section — you must be able to trace it around the whole building without
lifting the pen — and hunt the places it breaks (service penetrations, junctions, window reveals, the
roof/wall junction, the floor slab perimeter, recessed lights). Then **test it** (blower door), early
enough that repairs are possible [Passivhaus makes blower-door testing mandatory and sets a hard
numeric limit — take the current limit and its test conditions from the standard itself, since the
permitted value depends on the metric and the reference volume, and do not quote it from memory].
Note that a tight building *requires* deliberate ventilation: tight +
mechanical ventilation with heat recovery in cold climates; tight + generous operable openings and fans
in hot-humid ones. Tight and unventilated is a health problem.

**Continuous insulation.** Insulation works only if it is unbroken. Draw it the same way as the
airtightness line — one continuous stroke around the section. Every stud, rib, tie, balcony, parapet and
slab edge that punches through it is a loss. The rule of thumb: **wrap, don't fill.** Insulation
interrupted by structure loses far more of its nominal performance than the drawing suggests.

**Thermal bridging.** This is the detail that separates a real low-energy building from a brochure one.
Bridges are (a) *repeating* — studs, ties, fixings, dealt with by build-up choice — and (b) *linear /
geometric* — the ones architects create: **cantilevered balcony slabs, parapets, projecting fins,
uninsulated slab edges, structural columns crossing the line, window reveals, the wall/ground junction.**
A continuous concrete slab running from heated interior to open air is a radiator pointed at the sky; it
also produces a cold internal surface where condensation and mould appear, which is a defect claim, not
just an energy cost. Fixes: thermal breaks at balconies, insulated reveals and closers, moving the
structure inboard of the insulation line, or simply **not cantilevering the slab** — support the balcony
independently. **If you make one sustainability contribution to a project as the architect, make it
this one:** the thermal bridge is entirely an architectural decision, and the engineer cannot fix it
afterwards.

**Glazing ratio vs daylight vs heat loss/gain — the classic trade-off.** Glass does four things at once,
and they fight:
- lets in **daylight** (good — displaces electric lighting, and it is the reason to have windows);
- lets in **solar heat** (good in a cold winter, catastrophic in a hot summer);
- lets out **heat** (bad — even excellent glazing is several times worse, per unit area, than a decently
  insulated wall [common practice]; compare the actual U-values of the specified glazing unit and the
  specified build-up rather than assuming);
- lets in **glare** and produces **cold/hot radiant surfaces** near the perimeter (bad — and this, not
  energy, is what makes occupants close the blinds, at which point you have paid for glass, lost the
  daylight, and kept the heat loss).

The useful move is **less glass, better placed** — daylight is a function of head height and position far
more than of sheer area, so a tall, well-positioned, well-shaded window with a light-coloured reveal and
soffit will out-daylight a floor-to-ceiling wall of glass while losing a fraction of the heat. Beyond a
moderate ratio, extra glazing adds heat loss, heat gain and glare while adding almost no useful daylight.
Optimum ratios vary by climate, orientation and code — get them from the modeller — but the *shape* of
the curve is universal: it turns over, and most contemporary facades sit well past the turn. **Do not
state an optimum glazing ratio as a number** — it is a modelled output, specific to the orientation, the
climate and the glazing spec, and any single figure quoted across climates is wrong somewhere.

**Say it plainly: fully-glazed towers are not sustainable buildings.** A sealed all-glass tower has a
high-loss, high-gain envelope in every climate; it needs mechanical cooling essentially year-round
(often even in winter, on the core), it typically has a very high embodied carbon facade (aluminium +
glass, with a service life often shorter than the structure), it glares so badly the blinds go down
permanently, and it needs a large plant just to correct a self-inflicted problem. Bolting PV, a green
wall, a "double skin" or a LEED plaque onto it does not change the physics. Some of the most-awarded
"green" towers of the last two decades have poor measured EUIs. If a client wants a fully-glazed tower,
that is a legitimate aesthetic and commercial choice — but it should not be marketed as a sustainable
one, and you should say so once, clearly, and then get on with making the best version of what they
asked for.

**Shading geometry by orientation — south and west need DIFFERENT solutions.**
(Northern hemisphere; mirror for the southern.)
- **Equator-facing (south):** the sun is **high** in summer and **low** in winter, and it is roughly
  symmetrical about noon. A **horizontal** device — overhang, brise-soleil, projecting balcony, deep
  reveal — is near-perfect: it cuts the high summer sun and lets the low winter sun in underneath. Fixed
  geometry works; you can size it from the solar angles. This is the easy facade.
- **East and west:** the sun is **low** — it comes in near-horizontally, straight down the glass, at
  sunrise and sunset. **A horizontal fin does nothing against a horizontal sun ray.** To shade a low sun
  with an overhang you would need one absurdly deep — it would have to project far enough to block a ray
  arriving only a little above the horizon, which is architecturally impossible on a normal facade
  (check it against a real sun-path diagram for the site's latitude rather than assuming). This is
  why so many "shaded" buildings still cook: someone repeated the south fins around all four sides
  because it looked coherent in elevation. It is a graphic, not a shading device.
  **What actually works on east/west:** vertical fins (and ideally *angled/rotated* vertical fins, so
  they block the low sun without blocking the view); screens, perforated panels, mashrabiya, louvred
  shutters; deep recessed windows; **operable/movable** shading; planting and trees (deciduous can be
  useful east/west in temperate climates); and — best of all — **just put less glass on the east and
  especially the west facade.** West is the worst orientation in almost every climate, because peak
  solar gain coincides with the hottest part of the afternoon and with peak occupancy in offices and
  homes. The correct answer is very often architectural: put the cores, stairs, services, circulation and
  storage on the west.
- **Pole-facing (north):** little direct sun (in the mid/high northern latitudes), but it delivers
  **stable diffuse daylight** — the reason north light is prized in studios and galleries. Shade for
  glare if needed, not for gain; but remember it is a pure heat-loss facade, so do not over-glaze it just
  because it is "safe".
- **Roof / horizontal:** receives the most annual solar radiation of any surface in most climates.
  Insulate it, reflect it, ventilate it, plant it, or put the PV there — but never ignore it. Skylights
  and glazed atrium roofs are the single most efficient way to overheat a building.
- **Internal blinds do not work** for solar control — the heat is already inside the glass. Shade
  **outside** the glass, or between panes at worst. External shading is one of the highest-leverage,
  lowest-tech moves available, and it is architecture.

**Natural ventilation strategies.**
- **Single-sided** — openings on one facade only. Limited reach; useful for shallow rooms only. The
  weakest strategy, and the one most floor plates are accidentally stuck with.
- **Cross-ventilation** — openings on opposite/adjacent facades, driven by wind pressure difference.
  Effective and simple. It **requires a plan that permits it**: a limited depth, and a path — doors,
  transoms, high-level vents, an open plan — that lets the air actually cross. A cellular corridor plan
  kills it stone dead.
- **Stack / buoyancy** — warm air rises and exhausts high (atrium, chimney, ridge vent, solar chimney),
  drawing cool air in low. Works when there is no wind and works best with height and a temperature
  difference; the atrium is the classic architectural instrument for it (and note: an atrium is a
  ventilation and daylight device first, and only incidentally a lobby feature — if it is glazed,
  unshaded and unvented it is a greenhouse bolted into the middle of your building).
- **Night purge** — run ventilation at night to dump the day's heat into exposed thermal mass; essential
  in hot-arid, valuable in temperate summers, useless where nights stay warm and humid.
- **Mixed-mode** — natural when the weather allows, mechanical when it does not, with controls (and
  signals to occupants) that make the switch legible. The realistic best answer in most temperate
  commercial work.
- **Preconditions for any of it:** shallow enough plan, high enough ceilings, openable windows that are
  safe and secure and that occupants are *allowed* to open, acceptable external noise and air quality,
  and a facade design that does not fight the prevailing wind. **Usable plan depth scales with ceiling
  height**, and the limits differ sharply between single-sided and cross-ventilation — take the depth
  limits from a ventilation guide appropriate to your jurisdiction [e.g. CIBSE guidance in the UK] and
  confirm with the services engineer, rather than from a remembered number. Decide this at plan stage;
  you cannot retrofit natural ventilation into a deep sealed floor plate.

---

# 102 · Water, biodiversity & site

**Read the site before you touch it.** An ecological baseline survey — existing trees (and their root
protection areas), hedgerows, watercourses, habitats, soil, hydrology, protected species — comes
*before* the first massing model, not after planning refuses you. Mature trees are irreplaceable on any
project timescale; a 200-year-old tree is not offsettable by a nursery sapling, whatever the arithmetic
says. Set the building where the site is already degraded; keep what is alive. And check the ground:
contamination, water table, flood risk, and whether the site floods *now* or will within the building's
life.

**Rainwater harvesting.** Collect from roofs into storage; use for WC flushing, irrigation, cooling
make-up, cleaning. It only works if the design reserves the space for a tank (basement, undercroft or
above-ground) and the plumbing separation early — it is very hard to add later. Size against local
rainfall pattern and the actual non-potable demand; in a climate with a long dry season, storage volume,
not roof area, is the constraint.

**Greywater recycling.** Treat and reuse water from showers, baths and basins (never WCs — that is
blackwater) for flushing and irrigation. It has a maintenance and energy cost, so it makes sense at
scale (hotels, residential blocks, campuses) and rarely on a small house. Be honest with the client
about the ongoing maintenance burden — abandoned greywater plant is common.

**SUDS (sustainable urban drainage) and permeable surfaces.** The default of "collect all the rain into
a pipe and send it away fast" causes downstream flooding, pollution and dry soils. Instead **slow it,
store it, infiltrate it, and treat it on the way**: permeable paving, gravel and grass instead of
tarmac, swales, rain gardens and bioswales, detention/retention basins, ponds, tree pits that take
runoff, green roofs. The standard planning ambition is to discharge at **no worse than the greenfield
runoff rate** for the site [common practice; in the UK see the CIRIA SuDS Manual and the local lead
local flood authority — the required rate and return period are set locally, so get them from the
authority rather than assuming]. This is landscape architecture doing the work of civil engineering, and
it is cheaper and better-looking than the pipe.

**Urban heat island.** Hard, dark, dry, impermeable cities run measurably hotter than their rural
surroundings, and the effect is **strongest at night** — exactly when people need to cool down
[well-established; the magnitude is city- and weather-specific, so take it from local monitoring data,
not from a generic figure]. It is a public-health issue, not an aesthetic one. Mitigations, roughly in
order of effect: **trees and canopy shade** (they
shade *and* transpire — nothing else does both), vegetated ground, water, **high-albedo (light) roofs
and paving**, permeable surfaces, green roofs and walls, avoiding large unshaded car parks and dark
asphalt, and not exhausting your condenser heat into a street people walk down. Also: reflective glass
facades solve your building's gain by throwing it at your neighbour — this is a real and litigated
problem, and it is worth being the architect who does not do it.

**Green roofs.** Extensive (thin, sedum, low maintenance, light) vs intensive (deep, real planting,
usable, heavy, needs irrigation and access) — pick honestly, because a poorly maintained "biodiverse"
roof becomes a dead brown mat within a couple of summers. Benefits: attenuates runoff, cools the roof surface and the
city, protects the membrane, adds habitat, and modestly improves PV yield by keeping the array cooler
(green roof + PV — "biosolar" — is a genuinely good combination). Costs: structural load, maintenance,
irrigation in dry climates, and no thermal magic — **a green roof is not a substitute for insulation.**

**Biodiversity net gain.** The intent is that the site supports more nature after the project than
before, measured, and secured for the long term. In some jurisdictions this is now statutory rather than
aspirational [England: mandatory Biodiversity Net Gain under the Environment Act — the required
percentage, the metric and the securing period are set by legislation and change, so read the current
rules, do not quote them]. Do it with structure and continuity, not decoration:
native and locally appropriate planting, layered habitat (ground, shrub, canopy), dead wood, water,
connectivity to adjacent green space (a habitat island is barely a habitat), bird/bat/insect provision
integrated into the fabric rather than nailed on, dark corridors (light pollution is an ecological
harm — specify warm, shielded, timed, downward lighting), and a **maintenance plan with a budget**,
because a landscape without maintenance is a landscape that reverts to mown grass within a few years. Be
sceptical of biodiversity claimed via off-site units: same logic as carbon offsets, same weaknesses.

---

# 103 · Certifications (orientation only)

Use these to communicate with clients and planners — not to design. Know what each actually rewards.

**None of the thresholds are reproduced here, deliberately.** Certification criteria, rating bands,
credit weightings and performance limits are revised on their own schedules and differ by scheme
version and region. Describe what each scheme *optimises for* — below — and read the **current version
of the standard** for any number you intend to act on or put in front of a client.

- **LEED** (US, global) — broad points-based checklist across energy, water, materials, site, indoor
  quality. Optimises for **a credible, comparable, market-recognised score** across many categories.
  *Limit:* points are fungible, so a mediocre-energy building can still certify highly by collecting
  cheap credits elsewhere (bike racks, low-VOC paint, a proximate bus stop). Certification is largely at
  **design** stage; it is not a measured-performance guarantee.
- **BREEAM** (UK/Europe) — the older, similar points-based framework; somewhat stronger on management,
  ecology and life-cycle process. *Limit:* same gaming exposure; heavily dependent on the assessor and
  on documentation rather than outcomes.
- **Passivhaus** — narrow, rigorous, **fabric-and-energy-only**, with hard published performance limits
  (space heating/cooling demand, primary energy, airtightness) and **mandatory airtightness testing**
  [Passivhaus; the limits are numeric, versioned and climate-adapted — read them from the standard, and
  note that the classic limits are calibrated to a cool-temperate climate and require adaptation
  elsewhere]. Optimises for **actually low measured demand**, and it works — the
  performance gap is genuinely small. *Limit:* it says nothing about embodied carbon, water,
  biodiversity, site or beauty; it can push toward compact, heavily-insulated, triple-glazed,
  mechanically-ventilated buildings that are formally constrained and, in warm climates, need careful
  adaptation. It is a fabric standard, not a sustainability standard — but it is the most honest one on
  this list.
- **WELL** — occupant **health and wellbeing**: air and water quality, light, thermal and acoustic
  comfort, movement, nourishment. Optimises for the human, not the planet. *Limit:* it is not an
  environmental standard at all — a WELL-certified building can have terrible carbon performance (and
  some of its measures, e.g. more ventilation and lighting, cost energy). Complementary to, never a
  substitute for, an energy or carbon standard.
- **Living Building Challenge** — the most demanding: net-positive energy and water, a red-list of banned
  materials, beauty and equity petals, and — crucially — certification granted only **after a continuous
  period of measured in-use occupancy**, not on design intent [Living Building Challenge — check the
  current required period and conditions in the standard]. Optimises for genuine regenerative
  performance. *Limit:* very hard, very rare, often infeasible on urban/commercial sites and under most
  codes.

**The honest position.** All the points-based systems (LEED, BREEAM, and the rest) can be gamed, and
routinely are — credit-chasing is a consultancy specialism. A certificate is a *design-stage document*;
a meter is a *fact*. **A building with a genuinely low EUI, a low whole-life carbon figure, and a
retained existing structure beats a certified building with none of those, every time.** Pursue
certification when the client needs it for finance, planning, leasing or credibility — those are real
needs and worth serving — but never let the credit list drive the architecture, and never let a plaque
substitute for a number. If asked "which certification should we get?", the correct first answer is
"what EUI are we targeting, and is there a building already on the site?"

---

# 104 · Sustainability review output

Run this **only when a sustainability review is asked for** — never volunteer it, and never fold it into
a render request (see ROUTE FIRST, `SKILL.md` §1). It follows the same rules as the design review in
`ref-advisory.md` §42.

**The rule that overrides everything here: do NOT propose a redesign to hit a green target unless the
user asks for one.** The user's concept — massing, plan, geometry, form, style, materials as expressed —
is locked under the Preservation Contract (`SKILL.md` §2). Sustainability findings are *observations and
concept-preserving options*. "Your west facade is fully glazed" is a finding. "Rotate the building 90°
and reduce it to four storeys" is a redesign, and you do not get to do that uninvited. If the concept
itself is the problem, say so **once**, plainly, as an observation — then offer the best improvements
available *within* the concept, and ask.

**Rate each of the six dimensions /10, with a one-line justification and the biggest single lever:**

```
SUSTAINABILITY REVIEW — <project>
Climate zone / location assumed:
Typology & likely dominant load (heating / cooling / dehumidification / process):

1 · Passive design            /10 — orientation, form factor, plan depth, shading, daylight, natural ventilation
2 · Envelope & fabric         /10 — airtightness, continuity of insulation, thermal bridges, glazing ratio & distribution
3 · Systems                   /10 — electrification, efficiency, right-sizing, controls, renewables (and whether they come too early in the hierarchy)
4 · Embodied carbon           /10 — reuse vs new, structural material & efficiency, facade carbon, durability, design for disassembly
5 · Water                     /10 — rainwater, greywater, SUDS, permeability, demand reduction
6 · Biodiversity & site       /10 — existing ecology retained, habitat, planting, heat island, light pollution

Overall: /10

WHAT THE DESIGN ALREADY DOES WELL
- (be specific; credit the passive moves that are already there, even if unintentional)

BIGGEST RISKS
- (name the one or two things that will actually determine performance — usually west/east glazing,
  a thermal-bridged slab edge, plan depth, or an unshaded roof)

CONCEPT-PRESERVING IMPROVEMENTS  ← the core of the review
For each: what to change · why it works · what it does NOT change about the concept.
- Shading: <add external vertical/angled fins to the west elevation — the massing, plan and glazing
  lines are untouched>
- Envelope detail: <thermal break at the balcony slabs — invisible in elevation>
- Glazing: <same opening rhythm, reduced glass area within each bay / spandrel infill>
- Roof: <reflective + insulated + PV, same roof line>
- Ventilation: <make these windows operable; add high-level vents to the atrium>
- Embodied carbon: <retain the existing frame; cement replacement in the mix; reduce transfer structure>
- Water / landscape: <permeable paving instead of asphalt; retain the existing trees>
(Anything that would alter the massing, plan, style or geometry goes in the next block instead — NOT here.)

WOULD REQUIRE CHANGING THE CONCEPT (listed, not applied — for the user's decision only)
- <e.g. reducing the west glazing ratio below X, or rotating the plan, or reducing plan depth to allow
  cross-ventilation. State the cost of NOT doing it, honestly, and stop.>

WHAT I'D NEED TO SAY ANYTHING PRECISE
- Location & climate file · typology & occupancy · EUI target · code baseline · whether an existing
  building is on the site · construction market. (Say this plainly rather than inventing numbers.)

ONE QUESTION
"Which of these would you like me to apply, keeping your architectural concept exactly as it is?"
```

**Tone.** Senior, specific, unsentimental, non-promotional. Do not congratulate a building for having a
green roof and a PV array if it has a west-facing glass wall and no external shading — name the physics.
Equally, do not moralise: the user asked for a review, not a sermon. Give the finding, give the lever,
give the option, ask the question.

**Never invent numbers.** No fabricated U-values, EUIs, kgCO₂e/m², airtightness results, glazing-ratio
optima, payback periods or percentages — **not even plausible-sounding ones, and especially not
plausible-sounding ones**, because those are the ones that get believed and built on. Give direction and
magnitude instead ("this is likely the dominant heat loss path"; "this will be a significant cooling
load"), state that the figure depends on climate, code and market, and name where the real number comes
from: a **modeller with the climate file** for energy, an **EPD** for material carbon, and the **current
version of a named framework** (Passivhaus / LETI / RIBA 2030 / ASHRAE / CIBSE / local code) for any
target. If you quote a number, say which of those it came from; if you cannot, do not quote it.
An invented number is worse than no number: it is a decision made on a fiction, and in a commercial
context it is a liability with your name on it.
