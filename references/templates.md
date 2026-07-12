# Ready-Made Templates

14 starting templates in the master output format. Copy one, swap the **[bracketed]** parts for the
user's project, keep the rest. Always apply the Core Rules (preserve concept, don't invent).
Defaults assume photorealistic daylight unless the template says otherwise.

---

## 1. Exterior render
```
Project Type: [Residential / Commercial] building exterior
Input Reference: [sketch / elevation / SketchUp screenshot / D5 render]
Main Objective: Photorealistic exterior render faithful to the provided design
Architecture Style: [Modern minimalist]
Materials: [exposed concrete, large glass, matte black frames, wood accents]
Camera Angle: Eye-level three-quarter view, 35mm
Lighting: Bright natural daylight, soft crisp shadows, clear sky
Environment: Landscaped lawn, trees, paved walkway, a few people for scale
Important Constraints: Keep exact geometry, floor count, window/door placement; do not redesign
Final Render Prompt: Photorealistic exterior architectural render of a [modern minimalist] [building type], faithful to the provided design, [materials], eye-level three-quarter view, bright natural daylight with soft shadows, landscaped surroundings, people for scale, ultra-detailed, professional arch-viz, high resolution.
Negative Prompt: distorted geometry, extra floors/windows, warped perspective, blurry, low-res, cartoonish, watermark, text
```

## 2. Interior render
```
Project Type: Interior space — [living room]
Input Reference: [plan / sketch / reference photo]
Main Objective: Photorealistic interior render, faithful to the layout
Architecture Style: [Modern, warm minimalist]
Materials: [oak floor, light plaster walls, stone accents, soft textiles]
Camera Angle: Wide-angle at standing eye height, 24mm
Lighting: Natural daylight from windows + warm ambient lights, soft realistic shadows
Environment: Tasteful modern furniture, indoor plants, styled but realistic
Important Constraints: Keep room proportions, window and door positions, circulation
Final Render Prompt: Photorealistic interior render of a [modern] [room type], faithful to the layout, [materials], wide-angle eye-level view, bright natural daylight with warm ambient fill, realistic furniture and decor, soft shadows, cozy and airy, ultra-detailed, magazine quality.
Negative Prompt: distorted perspective, warped walls, floating furniture, blurry, low-res, cluttered, oversaturated, watermark, text
```

## 3. Kitchen render
```
Project Type: Interior — kitchen
Input Reference: [plan / reference]
Main Objective: Photorealistic kitchen render faithful to the layout
Architecture Style: [Modern handleless]
Materials: [matte cabinetry, stone/quartz countertop, backsplash, wood shelving, brushed metal]
Camera Angle: Wide-angle eye-level, 24–28mm, showing the work triangle
Lighting: Natural window light + under-cabinet and ceiling lighting, soft shadows
Environment: Realistic appliances, a few props (board, bowl), clean and styled
Important Constraints: Keep cabinet layout, island position, appliance locations
Final Render Prompt: Photorealistic kitchen interior render, faithful to the layout, [modern handleless] cabinetry, [stone] countertops, [wood] accents, brushed metal fixtures, wide-angle eye-level view, natural light plus warm task lighting, realistic appliances and props, soft shadows, ultra-detailed, premium quality.
Negative Prompt: warped cabinets, misaligned counters, distorted perspective, blurry, low-res, clutter, watermark, text
```

## 4. Bathroom render
```
Project Type: Interior — bathroom
Input Reference: [plan / reference]
Main Objective: Photorealistic bathroom render faithful to the layout
Architecture Style: [Modern spa-like]
Materials: [large-format stone/porcelain tiles, glass shower, matte black fixtures, wood vanity]
Camera Angle: Wide-angle eye-level, 24mm
Lighting: Soft natural light + warm vanity lighting, gentle reflections
Environment: Clean, minimal styling, towels and a plant, realistic water/glass
Important Constraints: Keep fixture positions, shower and vanity layout
Final Render Prompt: Photorealistic bathroom interior render, faithful to the layout, [modern spa-like] design, [stone] tiles, glass shower, matte black fixtures, [wood] vanity, wide-angle view, soft natural and warm light, realistic reflections, minimal styling, ultra-detailed, premium quality.
Negative Prompt: warped tiles, distorted glass, crooked fixtures, blurry, low-res, clutter, watermark, text
```

## 5. Apartment render
```
Project Type: Residential apartment — [interior / building]
Input Reference: [floor plan / sketch]
Main Objective: Photorealistic render faithful to the apartment design
Architecture Style: [Contemporary]
Materials: [light flooring, neutral walls, glass balcony rail, modern furniture]
Camera Angle: [Wide interior eye-level OR exterior three-quarter], appropriate focal length
Lighting: Natural daylight, soft realistic shadows
Environment: Realistic furnishing / balcony view / building context as relevant
Important Constraints: Keep room layout, openings, balcony and circulation
Final Render Prompt: Photorealistic render of a [contemporary] apartment [interior/exterior], faithful to the design, [materials], [camera], natural daylight, realistic furnishing and context, soft shadows, ultra-detailed, professional quality.
Negative Prompt: distorted layout, warped perspective, extra rooms, blurry, low-res, clutter, watermark, text
```

## 6. Tower render
```
Project Type: High-rise tower — exterior
Input Reference: [massing / elevation / model screenshot]
Main Objective: Photorealistic tower render faithful to the massing and facade
Architecture Style: [Modern glass tower]
Materials: [glass curtain wall, metal mullions, stone podium]
Camera Angle: Low wide hero angle looking up, OR aerial three-quarter; 24–35mm
Lighting: [Golden hour / clear daylight], crisp reflections on glass
Environment: Urban context, street life, neighboring buildings, sky with soft clouds
Important Constraints: Keep floor count, footprint, facade rhythm, podium
Final Render Prompt: Photorealistic render of a [modern glass] high-rise tower, faithful to the massing and facade rhythm, [materials], low wide hero angle, [golden-hour] light with crisp glass reflections, realistic urban context and street life, ultra-detailed, professional arch-viz, high resolution.
Negative Prompt: wrong floor count, warped facade, leaning tower, distorted reflections, blurry, low-res, watermark, text
```

## 7. Villa render
```
Project Type: Private villa — exterior
Input Reference: [sketch / elevation / model]
Main Objective: Photorealistic luxury villa render faithful to the design
Architecture Style: [Modern / Mediterranean]
Materials: [stone, plaster, wood, large glass, infinity pool]
Camera Angle: Eye-level three-quarter, 35mm
Lighting: Warm golden-hour sun, long soft shadows
Environment: Landscaped garden, pool, mature trees, paved drive, premium mood
Important Constraints: Keep massing, floor count, openings, pool and terrace positions
Final Render Prompt: Photorealistic render of a luxury [modern] villa, faithful to the design, [stone and glass] materials, infinity pool, eye-level three-quarter view, warm golden-hour light, lush landscaping, premium aspirational mood, ultra-detailed, magazine quality.
Negative Prompt: distorted geometry, extra floors, warped pool/water, blurry, low-res, oversaturated, watermark, text
```

## 8. Facade render
```
Project Type: Facade [redesign / visualization]
Input Reference: [existing photo / elevation]
Main Objective: Restyle ONLY the facade; keep building shape and openings
Architecture Style: [New facade direction]
Materials: [new cladding / screens / color / balconies]
Camera Angle: Straight-on or slight three-quarter elevation
Lighting: Even natural daylight, soft shadows
Environment: Minimal context so the facade reads clearly
Important Constraints: Keep footprint, floor count and window openings exactly; change skin only
Final Render Prompt: Photorealistic facade [redesign] of the building in the reference, keeping the exact footprint, floor count and window openings, applying [new materials/rhythm/color], straight-on three-quarter elevation, even daylight, soft shadows, ultra-detailed, professional quality.
Negative Prompt: changed building shape, moved windows, extra floors, distortion, blurry, low-res, watermark, text
```

## 9. Site analysis (diagram)
```
Project Type: Site analysis diagram
Input Reference: [site plan / map / aerial]
Main Objective: Clear analytical diagram of the site
Architecture Style: Clean infographic / diagrammatic (not photoreal)
Materials: Flat color zones, muted palette + accent colors
Camera Angle: Top-down / slight aerial axonometric
Lighting: Even flat diagram lighting
Environment: Plot boundary, context buildings, green areas, roads
Important Constraints: Keep true plot shape, orientation and access points
Final Render Prompt: Clean architectural site analysis diagram, top-down axonometric, showing plot boundary, sun path, prevailing wind, access and circulation arrows, zoning and green areas, context buildings, labeled, muted palette with accent colors, crisp infographic style, high resolution.
Negative Prompt: photorealistic, cluttered, unreadable labels, distorted plot, blurry, low-res, watermark
```

## 10. Floor plan to 3D
```
Project Type: 2D floor plan → 3D dollhouse render
Input Reference: [floor plan image]
Main Objective: Convert the plan to a faithful 3D cutaway, keeping every wall and room
Architecture Style: [Modern interior]
Materials: [flooring, wall finish, furniture set]
Camera Angle: Top-down angled isometric/axonometric dollhouse, no roof
Lighting: Soft even daylight, gentle shadows
Environment: Furnished rooms matching the plan's function labels
Important Constraints: Keep EVERY wall, door, window, stair and room position exactly as drawn
Final Render Prompt: 3D dollhouse cutaway render generated from the provided 2D floor plan, faithful to every wall, door, window, stair and room position, isometric top-down angled view with no roof, [modern] furnishing matching room functions, realistic flooring and materials, soft daylight, ultra-detailed, clean professional arch-viz.
Negative Prompt: changed layout, moved walls, missing rooms, distorted plan, blurry, low-res, watermark, text
```

## 11. Section render
```
Project Type: Architectural section render
Input Reference: [section drawing / model cut]
Main Objective: Render a faithful sectional cut showing interior floors and structure
Architecture Style: [Modern]
Materials: [structure, slabs, finishes called out]
Camera Angle: Straight-on section / sliced axonometric
Lighting: Soft studio + interior lights, readable depth
Environment: Furnished interiors visible through the cut, ground/landscape line
Important Constraints: Keep floor heights, slab/column positions, stair and circulation
Final Render Prompt: Architectural section render of the building, faithful to floor heights, slabs, columns, stairs and circulation, straight-on cut revealing furnished interiors across levels, soft studio and interior lighting with readable depth, materials clearly expressed, ultra-detailed, professional arch-viz.
Negative Prompt: distorted structure, wrong floor heights, warped section, blurry, low-res, watermark, text
```

## 12. Urban masterplan
```
Project Type: Urban masterplan render
Input Reference: [masterplan / massing model]
Main Objective: Aerial render of the urban scheme, faithful to the layout
Architecture Style: [Contemporary mixed-use]
Materials: Varied building skins, green public realm, paved plazas, water features
Camera Angle: High aerial / bird's-eye three-quarter
Lighting: Clear daylight or golden hour, crisp shadows
Environment: Streets, blocks, parks, plazas, people and traffic at scale, context city
Important Constraints: Keep block layout, street grid, building footprints and densities
Final Render Prompt: Aerial render of an urban masterplan, faithful to the block layout, street grid and building footprints, [contemporary mixed-use] architecture, green public realm and plazas, high bird's-eye three-quarter view, [golden-hour] light, lively streets with people and traffic at scale, ultra-detailed, professional arch-viz, high resolution.
Negative Prompt: distorted grid, melted buildings, wrong footprints, blurry, low-res, watermark, text
```

## 13. Landscape render
```
Project Type: Landscape / public-space render
Input Reference: [landscape plan / sketch]
Main Objective: Photorealistic landscape render faithful to the design
Architecture Style: [Contemporary landscape]
Materials: [paving, decking, planting palette, water, lighting]
Camera Angle: Eye-level or low three-quarter, 35mm
Lighting: Warm natural daylight or golden hour, dappled shade
Environment: People enjoying the space, varied vegetation, seating, water features
Important Constraints: Keep path layout, planting zones, levels and key elements
Final Render Prompt: Photorealistic landscape architecture render, faithful to the design, [paving and planting palette], water features and lighting, eye-level view, warm natural daylight with dappled shade, people enjoying the space, lush realistic vegetation, ultra-detailed, professional quality.
Negative Prompt: distorted paths, fake-looking plants, warped perspective, blurry, low-res, oversaturated, watermark, text
```

## 14. A4 presentation board
```
Project Type: A4 client presentation board
Input Reference: [renders / plans to compose]
Main Objective: Clean A4 layout combining hero render + plans + text space
Architecture Style: Minimal editorial board, [brand colors]
Materials: n/a (graphic layout)
Camera Angle: Flat board layout, portrait or landscape A4
Lighting: n/a
Environment: Generous white space, aligned grid, room for title and notes
Important Constraints: Keep renders undistorted; clean typographic hierarchy; print-ready feel
Final Render Prompt: Minimal A4 architectural presentation board layout, [portrait] orientation, featuring a large hero render, supporting plan/elevation thumbnails, a clean title block and space for descriptive text, aligned grid, generous white space, editorial typography, [brand] accent color, print-ready, professional.
Negative Prompt: cluttered, misaligned, distorted images, busy background, low-res, watermark
```
