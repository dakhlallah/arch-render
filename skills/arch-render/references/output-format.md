# Platform Adapters, Defaults & Scene-Setup Mode

> **The output block lives in `SKILL.md` §3 — that is the single canonical format.** This file only
> covers per-platform tuning of the **Final Master Prompt** line, plus the defaults to fall back on.

## Default render style (when the user doesn't specify)

> Photorealistic, premium architectural visualization, realistic daylight, clean composition,
> accurate human scale, sharp materials and details, natural soft shadows, high resolution,
> professional studio quality.

## Default Negative Prompt (trim per project)

> distorted geometry, warped perspective, extra floors, extra windows, crooked lines, bent walls,
> melting structure, unrealistic proportions, blurry, low resolution, oversaturated, cartoonish,
> fisheye distortion, watermark, text, logo, people with deformed faces/hands, duplicated elements,
> cluttered, messy, lens flare overload, fake HDR halos.

---

## Platform adapters (tune the Final Master Prompt per tool)

The output block stays the same; adjust phrasing + add the tool's syntax tail.

- **Midjourney** — descriptive, comma-separated, parameters at the end:
  `... --ar 16:9 --style raw --q 2 --v 6`. Interiors `--ar 3:2`; boards `--ar 4:3`.
  Use `--no <things>` for the negative (MJ ignores a separate Negative Prompt line).
  ⚠️ MJ has no image-preserving mode — for a faithful transform of an uploaded design, prefer Mode B.
- **DALL·E 3 / ChatGPT / Photoshop AI (Generative Fill, Firefly)** — natural full sentences, no
  parameters. Put constraints as sentences ("do not change the layout"). Negative → "avoid …".
- **Stable Diffusion / SDXL / ComfyUI** — weighted keywords; use the Negative Prompt line directly.
  Suggest `Steps 30, CFG 5–7, Sampler DPM++ 2M Karras` + an arch-viz checkpoint. For geometry
  fidelity, recommend **ControlNet (canny/depth/mlsd)** on the input — that's what actually locks it.
- **Leonardo.Ai** — comma keywords + the Negative Prompt field. "Phoenix / PhotoReal, Alchemy ON".
- **GPT Image (in ChatGPT / other hosts)** — excellent **instruction-following** and legible embedded
  text; write clear prose *instructions*, not keyword soup ("Keep the building exactly as in the
  reference. Change only the lighting to…"). It respects explicit do/don't constraints better than most.
  Note: hosted UIs often expose only a **fixed size set** — pick the closest to the input's aspect and
  say so. (The **API**, which this skill uses directly, does not have that limit — see below.)
- **Reve** — strong prompt adherence and typography. Treat like GPT Image: prose instructions, explicit
  constraints. Verify the current parameter set before promising syntax.
- **FLUX (1.1 Pro / dev)** — rich **natural-language** description, not keyword soup; it follows long
  prose well. No weights, no negative prompt (it largely ignores one) — phrase exclusions positively
  ("clean unbroken roofline" beats "no extra floors"). Strong at facade text/signage.
- **Google Imagen** — plain descriptive sentences, no parameter syntax. Conservative safety filter:
  avoid "shot on <camera brand>" phrasing, describe the optics instead ("35mm perspective-corrected").
- **Ideogram** — best-in-class **legible text**; use it when the render must carry a real sign, project
  name or board title. Describe the text in quotes: `a sign reading "RESIDENCE MARAIS"`. Magic Prompt OFF
  for architectural fidelity — it embellishes.
- **Recraft** — vector/graphic strengths. Route **diagrams, boards, icons, site-analysis graphics** here,
  not photoreal renders. Name the style set explicitly.
- **Adobe Firefly / Photoshop Generative Fill** — natural sentences. Its real strength is **local edits
  on an existing render** (swap a sky, extend a foreground, remove a crane) — reach for it for surgical
  fixes rather than a full generation.
- **GPT Image 2 (this skill's built-in renderer)** — feed the Final Master Prompt straight into
  `scripts/render.py` with `--aspect auto`. See `SKILL.md` §4. It takes the user's design **and** style
  references as image inputs in one call (§81), and — unlike most hosted tools — accepts **arbitrary
  output sizes** (any dimensions divisible by 16, longest edge ≤ 3840), which is what lets the skill
  preserve an input's exact aspect ratio.

> **Geometry fidelity across platforms.** Only image-conditioned tools (this skill's GPT Image renderer,
> SD+ControlNet, Firefly on an existing image) can truly hold an uploaded design. Text-only tools
> (Midjourney, Imagen, Ideogram) will *reinterpret* it — say this plainly when the user picks one for a
> preservation task, before they waste a day fighting it.

## Adapting to a model that isn't on this list

New image models ship constantly. Don't guess at syntax you don't know — **classify it, then adapt**:

1. **Is it keyword-weighted or prose-following?** Keyword models (SD lineage) want comma-separated
   tokens, weights and a separate negative prompt. Prose models (GPT Image, FLUX, Imagen, Reve) want
   fluent natural-language instructions and largely ignore a negative prompt — phrase exclusions
   *positively* ("clean unbroken roofline") rather than as negations.
2. **Can it take an image as a condition?** If yes → preservation work is viable; feed the design and
   state the lock explicitly. If no → warn the user it will reinterpret their building.
3. **Does it have a parameter syntax?** If you don't know it **for certain**, omit it. A clean prompt
   with no parameters works everywhere; an invented `--flag` fails loudly and makes the skill look
   unreliable. **Never fabricate model parameters, version numbers or setting names.**
4. **Aspect ratio** — if the model only supports fixed sizes, pick the closest to the input's ratio and
   **tell the user you did**, since it breaks the crop lock.

When unsure, hand over the **universal** block and say which knobs the user should set in their own UI.

## Scene-setup mode (real-3D tools — not a prompt)

**Lumion · Enscape · Twinmotion · Blender · SketchUp · V-Ray** render an actual 3D scene, so a text
prompt is useless. Instead output a short **numbered scene-setup checklist** under Final Master Prompt:

1. **Sun / sky** — time of day, sun angle, HDRI choice, cloud cover
2. **Materials to assign** — per surface, with the PBR maps and real-world texture scale
3. **Vegetation & context** — species, density, surroundings
4. **People & cars** — placement for scale, never crowded
5. **Camera** — height (≈1.6 m eye level), focal length (35–50mm exterior, 24mm interior), two-point
   perspective (keep verticals vertical)
6. **Post** — bloom, AO, depth of field, colour grade, denoise/samples

For Blender specifically: Cycles + a sky HDRI + a 35–50mm camera is the default starting point.

---

> Tell the user which platform the block is tuned for. If they didn't name one, produce a clean
> **universal** block (works in MJ / DALL·E / SD / Leonardo) and offer to render it here (Mode B).
