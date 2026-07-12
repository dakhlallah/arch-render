# Arch-Viz Prompt Recipe

Build every render prompt by stacking these layers in order. The **preserve clause** is the
most important part — without it the AI will redesign the building instead of just making it real.

---

## 1. Preserve clause (ALWAYS include for sketch/screenshot → render)

> "This is an architectural render task. Keep the EXACT building geometry, massing, proportions,
> footprint, number of floors, roof shape, and the placement of every window, door and balcony
> from the input image. Do not redesign, move, add or remove any structural element. Only add
> realistic materials, lighting, texture and surroundings to make it look like a real photograph
> of the finished building."

If the input is a rough hand sketch, soften slightly:

> "...interpret the rough sketch faithfully — keep the same overall shape, floor count and opening
> positions — and render it as a finished, photorealistic building."

### Enhance clause (for ALREADY-RENDERED inputs: D5 Render, Cinema 4D, Lumion, Octane, etc.)

When the input is already a 3D render (not a flat sketch), use this instead — the geometry, camera
and base materials are already right, so the job is to polish, not redesign:

> "This is an existing architectural render. Keep the EXACT same building, geometry, camera angle,
> perspective and composition. Do not change the design, the materials the user already chose, or
> the viewpoint. Only enhance photorealism: clean up render noise, improve material detail and
> reflections, add realistic natural lighting and shadows, and add a believable sky, environment
> and landscaping. Make it look like a real photograph of the built project."

See `source-tools.md` for which clause to use per source (D5 / Cinema 4D / screenshot / sketch).

---

## 2. Materials
Name the real materials so surfaces read correctly:
`exposed concrete, large glass curtain walls, natural stone cladding, warm wood slats,
white plaster, brushed metal railings, matte black window frames`

## 3. Lighting & time of day
Pick one (the style preset usually sets this):
`bright midday sun with soft shadows` · `warm golden-hour light, long shadows` ·
`blue-hour dusk with glowing interior lights` · `overcast soft diffused light` ·
`dramatic side lighting`

## 4. Environment & landscaping
Ground the building in a believable place:
`landscaped garden, mature trees, clean paved entrance, low planting, realistic sky with soft clouds,
wet reflective ground (if rainy), urban street context (if city)`

## 5. Scale & life cues (optional but powerful)
`a few people walking for scale, parked cars, outdoor furniture` — makes it feel inhabited and real.

## 6. Camera
`eye-level three-quarter view` (default exterior) · `low wide-angle hero shot` ·
`high aerial / drone view` · `straight-on elevation` · `interior wide-angle at standing eye height`.

## 7. Quality tail (append at the end)
> "Photorealistic architectural visualization, ultra-detailed, professional arch-viz render,
> crisp materials, accurate global illumination, high dynamic range, magazine quality."

---

## Assembled example

```
This is an architectural render task. Keep the EXACT building geometry, massing, proportions,
floor count, roof shape and the placement of every window and door from the input image. Do not
redesign anything — only add realistic materials, lighting and surroundings.

Materials: exposed concrete, large glass curtain walls, warm wood accents, matte black frames.
Lighting: warm golden-hour sun, long soft shadows. Environment: landscaped garden with mature
trees, clean paved entrance, realistic sky. A few people walking for scale, two parked cars.
Camera: eye-level three-quarter view.

Photorealistic architectural visualization, ultra-detailed, professional arch-viz render,
accurate global illumination, magazine quality.
```
