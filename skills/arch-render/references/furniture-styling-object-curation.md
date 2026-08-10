# Furniture, Styling, and Object Curation

Use this module automatically with the Room-by-Room Floor-Plan Prompt Library and whenever the user
requests furnishing, styling, object curation, FF&E schedules, room completeness checks, or layered
lighting. Generate advisory proposals and prompts only; do not buy products or call paid image tools
without separate authorization.

## Architecture and circulation lock

Treat every object, finish, palette, curtain, luminaire, artwork, plant, and accessory as a reversible
proposal. Never alter, conceal, or imply changes to walls, doors, windows, openings, stairs, structure,
fixed services, room dimensions, circulation, camera locks, or approved Design DNA.

Do not place furniture across door swings, required circulation, stairs, maintenance zones, access
panels, radiators, diffusers, returns, controls, glazing, or fire/life-safety equipment. Use project code,
accessibility, manufacturer, and ergonomic criteria only when supplied or verified. Otherwise label
clearances and suitability `Requires verification`.

## Room inputs

For each stable Space ID from `room-by-room-prompt-library.md`, record:

- source label, documented dimensions, openings, fixed elements, adjacency, and circulation;
- room function and user needs when known;
- shared Interior Identity, target style, color direction, quality tier, location, and budget when known;
- unknown ceiling height, service points, wall build-up, electrical locations, daylight conditions,
  acoustic needs, accessibility needs, household characteristics, and procurement constraints.

Do not guess an unlabeled room's function or imply that a proposed object fits when dimensions are
missing. Continue with a clearly labeled conceptual kit where useful and identify what must be measured.

## Object inventory

Create a complete but restrained inventory appropriate to the room. Consider only relevant categories:

- primary furniture: sofa, bed, dining table, desk, storage, vanity, media unit;
- secondary furniture: chairs, side tables, benches, stools, nightstands, consoles;
- textiles: rugs, curtains, sheers, blinds, cushions, throws, bedding, upholstery;
- lighting: ambient, task, accent, decorative, portable, integrated, and controls;
- art and display: artwork, mirrors, sculpture, books, display objects;
- planting: plants, planters, maintenance and daylight suitability;
- accessories: trays, vessels, tableware, desk objects, bathroom accessories, functional storage;
- technology and equipment: television, audio, appliances, charging, cable management, only when
  appropriate and compatible with the documented room;
- safety, accessibility, maintenance, and cleaning considerations.

For every proposed item provide:

```text
Item ID and Space ID:
Category and item:
Purpose and priority: essential | recommended | optional
Proposed quantity:
Approximate dimensions or acceptable range:
Material, finish, texture, and color:
Placement and orientation:
Style relationship:
Cost tier: premium | mid-range | budget
Product reference and verification status:
Comparable products or performance criteria:
Clearance, access, services, and coordination:
Pros, cons, maintenance, and alternatives:
Source / assumption / verification required:
```

Approximate dimensions are selection targets, not measured facts. Check them against verified room
dimensions, doorways, lifts, stairs, installation routes, clearances, and manufacturer data before
specification or purchase.

## Product, texture, and material library

Prefer authentic products and official manufacturer sources. Verify current product name, collection,
dimensions, materials, finishes, region, availability, and links when possible. Label anything not
verified `Unverified reference — confirm with manufacturer or dealer`. Never fabricate a product,
price, certification, warranty, lead time, stock status, or environmental claim.

Use well-known manufacturers as genuine basis-of-design references or translate their relevant
high-level attributes into neutral selection criteria. Do not recommend counterfeits, deceptive replicas,
or copying protected distinctive designs. Give comparable products based on function, dimensions,
material, durability, maintenance, and price tier rather than superficial imitation.

Build one deduplicated library across the project:

```text
Library ID | linked Item IDs | material/product | finish | color | texture | care | durability |
verified source | alternatives | cost tier | sustainability evidence | status
```

For custom or generic materials, link to the PBR workflow in `material-reference-spec-mode.md` only when
the user requests texture prompts; do not automatically multiply every furniture material into ten PBR
prompts unless that mode is active.

## Room completeness check

Check function before decoration. For each room classify:

- `Complete` — essential function and coordination are covered;
- `Missing essential` — the room cannot support its stated use;
- `Recommended addition` — meaningful comfort, lighting, storage, acoustic, or visual benefit;
- `Optional styling` — decorative enhancement with no functional requirement;
- `Over-furnished` — clutter, blocked circulation, competing focal points, or maintenance burden;
- `Requires verification` — source or user information is insufficient.

Do not add a rug, artwork, plant, television, curtain, or accessory merely to fill a checklist. Explain
the purpose, benefit, drawback, and coordination impact of every addition.

## Layered lighting

Create a conceptual lighting kit for each room:

- ambient light for general visibility and spatial coherence;
- task light for documented activities;
- accent light for architecture, art, texture, or focal elements;
- decorative light as a visible object and mood layer;
- daylight integration, glare control, switching/dimming scenes, color consistency, maintenance access,
  and coordination with ceilings, sprinklers, detectors, diffusers, returns, and furniture.

Do not invent electrical capacity, circuiting, fixture quantity, photometric performance, emergency
lighting, code compliance, or installation details. Photometric calculations and final electrical design
require verified geometry, reflectances, fixture files, applicable standards, and qualified professionals.

## Deliverables per room

For every Space ID produce:

1. room objective and source constraints;
2. complete object inventory;
3. FF&E schedule;
4. furniture material and finish schedule;
5. color palette with approximate HEX/RGB and approximate RAL/NCS only when useful;
6. styling kit with essential, recommended, and optional layers;
7. layered lighting concept;
8. room completeness check;
9. one copy-ready AI visualization prompt including geometry locks and a negative prompt;
10. unresolved measurements, approvals, product checks, and professional verification.

Use the shared Interior Identity from `room-by-room-prompt-library.md` verbatim across every room. If the
package is long, deliver numbered parts while keeping one project index and stable IDs.

## User-approved prompt

Use this wording verbatim when the user requests the compact module prompt:

```text
Add module called Furniture, Styling, and Object Curation. For every room, generate a full inventory of objects, like sofas, TV, rugs, curtains, wall lights, art, plants, accessories. For each item, include purpose, approximate dimensions, material, finish, color palette, texture, placement, style, and cost tier. Build a texture and material library for all furniture items with real product references when possible, similar to well-known manufacturers. Perform a room completeness check, identify missing objects like rugs or wall art, and recommend additions. Design layered lighting, ambient, task, accent, and decorative. Generate for each room a full furniture schedule, material schedule, color palette, styling kit, and AI image prompt. Always maintain the exact architecture. Do not alter walls, doors, or windows. The goal is room by room, ready to use prompts plus a complete FF&E package.
```
