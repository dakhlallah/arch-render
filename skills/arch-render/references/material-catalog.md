# Material Catalog (PBR) — recommendation index

A vendor-neutral, categorized index of realistic architectural materials, organized the way
professional scanned-PBR libraries (A23D and peers) structure their collections. Use it to
**recommend** materials and write prompt fragments — this skill does NOT ship or copy any
proprietary texture files. Each entry: typical variants · standard PBR maps · usage · prompt fragment.

> Standard PBR map set (reference for every material): **Base Color/Albedo · Roughness · Normal ·
> Bump/Height · Displacement · Metalness · Ambient Occlusion · (Opacity / Reflection / Emission /
> Subsurface where relevant)**. Always: seamless, real-world scale, correct UV direction, no
> stretching, no obvious tiling.

---

## WOOD
- **Variants:** Oak · Walnut · Ash · Maple · Teak · Bamboo · Engineered · Veneer · Charred (shou-sugi-ban) ·
  Reclaimed · Timber battens. Patterns: plank, herringbone, chevron, parquet.
- **Use:** floors, wall cladding, ceilings (slats), joinery, furniture.
- **Prompt:** `natural [oak] [herringbone] wood, real grain direction with subtle variation, matte
  satin finish, accurate plank scale, soft realistic roughness`.

## STONE & SLABS
- **Variants:** Marble · Travertine · Limestone · Granite · Quartzite · Slate · Onyx · Sandstone.
  Finishes: polished, honed, brushed, leathered.
- **Use:** floors, feature walls, facades, countertops, vanities.
- **Prompt:** `[honed travertine] slab, natural veining and surface variation, correct edge profile,
  real-world tile scale, physically accurate reflections`.

## CONCRETE & CEMENTITIOUS
- **Variants:** Fair-face/exposed · Board-formed · Precast · Polished · Microcement · Terrazzo.
- **Use:** facades, floors, walls, ceilings.
- **Prompt:** `fair-face concrete, fine aggregate, subtle pores and form-tie marks, natural
  discoloration, construction joints, proper displacement, matte`.

## TILES & CERAMICS
- **Variants:** Porcelain · Ceramic · Large-format · Mosaic · Cement (encaustic) · Zellige.
- **Use:** floors, walls, bathrooms, kitchens, facades.
- **Prompt:** `large-format [porcelain] tile, realistic grout lines and spacing, correct scale, true
  color, low-sheen finish, no repeating-texture artifacts`.

## BRICK & TERRACOTTA
- **Variants:** Clay brick · Engineering brick · Glazed · Terracotta baguettes/panels · Blockwork.
- **Use:** facades, feature walls, paving.
- **Prompt:** `exposed clay brick, crafted bond pattern, natural color variation per brick, recessed
  mortar, weathered realism`.

## METAL
- **Variants:** Steel · Stainless · Black/blackened steel · Brushed aluminum · Brass · Bronze ·
  Copper · Corten · Perforated/expanded mesh · Composite panels (ACP).
- **Use:** facades, screens, railings, frames, fixtures, cladding.
- **Prompt:** `[brushed brass], directional brushed finish, fingerprint and micro-scratch variation,
  correct anisotropic roughness, subtle reflections`. Corten → `weathered corten steel, rich rust
  patina`.

## GLASS
- **Variants:** Clear · Low-iron · Tinted · Frosted/etched · Fluted/reeded · Curtain-wall units · Mirror.
- **Use:** curtain walls, balustrades, partitions, shopfronts.
- **Prompt:** `clear low-iron glass curtain wall, true transparency, correct refraction, layered
  interior + exterior reflections, slim mullions`.

## PLASTER & PAINT & WALL FINISHES
- **Variants:** Smooth plaster · Lime wash · Venetian plaster · Textured render · Acoustic panels ·
  Wallpaper · Decorative panels.
- **Use:** interior/exterior walls, ceilings.
- **Prompt:** `smooth white plaster, soft matte finish, subtle hand-applied variation, realistic
  ambient occlusion in corners`.

## FABRIC, LEATHER & SOFT
- **Variants:** Linen · Wool · Velvet · Bouclé · Leather · Curtains/sheers · Rugs (Persian/modern/jute).
- **Use:** upholstery, drapery, acoustic, styling.
- **Prompt:** `natural [linen] upholstery, realistic weave and fiber detail, soft micro-roughness,
  gentle sheen, correct thread scale`.

## GROUND, LANDSCAPE & NATURE
- **Variants:** Grass/lawn · Ground cover · Gravel · Sand · Soil · Rock · Water · Snow · Wet pavement ·
  Decking · Stone paving · Asphalt · Vegetation (trees/shrubs/palms).
- **Use:** site, landscape, context, hardscape.
- **Prompt:** `realistic landscaped lawn with natural color variation, mature trees, [stone] paving
  with accurate joint scale, believable wet-ground reflections`.

## ROOFING & MISC
- **Variants:** Standing-seam metal · Clay/concrete tile · Slate · Membrane · Green roof · Rubber ·
  Laminate · Wicker · Plastic/composite.
- **Use:** roofs, details, furniture, fittings.
- **Prompt:** `dark standing-seam metal roof, crisp seams, matte finish, accurate panel width`.

---

## How to use in a prompt / materials board
1. Detect the materials present (or implied) in the user's input.
2. Pick the closest catalog entry per surface (floor/wall/facade/ceiling/furniture).
3. Drop the **prompt fragment** into the render prompt (swap the bracketed variant + finish).
4. For a materials board (§46), list each: Material Name · Finish · Color · Texture · Application.
5. Name a **manufacturer reference for inspiration only** (Cosentino, Florim, Havwoods, Flos…),
   never copy proprietary assets — generate original prompts inspired by scanned-quality realism.
