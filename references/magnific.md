# 88 · Magnific AI Enhancement & Upscale

> The **realism-and-resolution finisher**. Magnific does not compose a scene — it takes an image that is
> already right and adds micro-detail, material grain, light response and pixels. Offer it on **every**
> architectural image upload. **Preservation Contract applies** (`SKILL.md` §2) — and it applies harder
> here than anywhere else in the skill, because Magnific's creativity slider is a redesign machine if you
> let it off the leash.

---

## 88.0 · The one rule — creativity hallucinates architecture

Magnific's `creativity` does not "add realism". It **re-imagines pixels**. Pushed up on a building it
invents mullions, splits windows, grows extra balconies, doubles railings, sprouts fake signage and
re-draws roof edges. On a face that reads as "more detail"; on a facade it reads as **a different
building**.

**Therefore, for architecture:**

| Slider | Arch-safe range | Why |
|---|---|---|
| `creativity` | **−3 … +2** (default **0**) | Above ~+3 it starts editing the design. This is the redesign risk. |
| `resemblance` | **+2 … +6** (default **+4**) | This is the leash. Raise it *first* whenever geometry drifts. |
| `hdr` | **+1 … +5** (default **+3**) | Material depth and light response — the actual win. Above +6 → crunchy, HDR-plague look. |
| `fractality` | **−2 … +3** (default **0**) | Micro-texture density. High values fur up smooth concrete and glass. |

**Facades, mullions, curtain wall, repeated openings and railings are the failure zone.** Any input where
the design is carried by a *grid* (office towers, apartment blocks, glazed facades) → keep `creativity`
≤ 0 and `resemblance` ≥ +4, or run **precision mode** (below), which cannot hallucinate at all.

**When fidelity beats flair, use precision.** `precision: "precision"` swaps the creative sliders for
`sharpness` / `grain` / `ultraDetail` (0–100) and does **no generative re-imagining** — it's a true
upscaler. For a **photo of a built building**, a **competition submission**, or anything a client will
compare against reality, precision is the correct mode, not creative.

---

## 88.1 · What Magnific is for (and what it isn't)

| Use it to | Do **not** use it to |
|---|---|
| Finish a good render — pores in concrete, weave in fabric, grain in timber, dirt in stone | Fix a bad render. Garbage in, sharper garbage out. |
| Rescue a **low-res / small / compressed** image (screenshot, JPEG, client's 900px file) | Change time of day → that's `render.py` or `images_relight` |
| Print / large-format / hoarding output (4x–16x) | Add or move anything architectural — it can't be steered that precisely |
| Kill the "CGI plastic" tell on a D5 / Lumion / Enscape render | Generate a scene from nothing → `images_generate` or `render.py` |
| Push a GPT-Image render (max 3840px) up to true print resolution | Produce a board or document → `board.py` |

**The pairing that actually wins:** `render.py` (GPT Image — composes, relights, materializes, holds the
crop) **→ then Magnific** (finishes and enlarges). Magnific is the *last* step of a pipeline, never the
first. Say this to the user when they ask which to use.

---

## 88.2 · The workflow (live — the MCP is wired)

Magnific runs **for real** through the `magnific` MCP server, so this is an execution path, not just a
prompt to paste. **Every run costs credits → the §2 COST GATE applies: state the run count, wait for a yes.**

1. **Read the image** — run the §85 structured read (`auto-analysis.md` Step 1). Input type, building
   type, interior/exterior, materials, lighting, camera, design intent, **and image quality** (resolution,
   compression, noise, engine tells). Quality drives `scale`; input type drives `precision` vs `creative`.
2. **Get the image into Magnific.**
   - Local file (the normal case) → `creations_request_upload` → `creations_finalize_upload`.
   - Public URL → `creations_upload_image` (one step).
   - Already produced by a Magnific tool this session → reuse its `creationIdentifier` directly.
3. **Price it** — `simulate_cost({tool: "images_upscale", arguments: {...}})`. Read-only, never charges.
   Quote the credits, **then** ask.
4. **Run** — `images_upscale` with the settings from §88.3.
5. **Wait** — `creations_wait([identifier])`, re-poll on `poll_after_seconds`.
6. **LOOK AT IT.** `Read` the returned image and run **§24**. Compare it against the input, specifically
   for **hallucinated architecture**: count the window bays, check mullion spacing, check the railing
   rhythm, check the roof edge. A Magnific pass that changed the building is **rejected and re-run** with
   lower `creativity` / higher `resemblance` (**§83**) — never shipped with a caveat.
7. **Deliver short** (Mode B shape, `SKILL.md` §4): what you ran · the image · one line of offer.

**No negative prompt.** The Magnific upscaler exposes `prompt` only — there is **no negative-prompt
field** on this API. Steer it with `resemblance` and a *short, factual* prompt instead. If the user asks
for a negative prompt, tell them plainly that this model doesn't take one, and that the §23 avoid-list is
enforced through the settings, not through text.

**Keep the guidance prompt SHORT and DESCRIPTIVE.** Magnific's `prompt` is a nudge, not a brief — a
paragraph of §11 quality-tail boilerplate makes it worse, not better. One line naming the *real*
materials and light:

> `board-formed concrete, oxidised bronze mullions, low-iron glass, wet asphalt, overcast north light`

Never write the building's *design* into it. You are describing what is already there so the model
sharpens the right thing — not requesting features.

---

## 88.3 · Settings by input type — the lookup table

`mode` (`ultra` · `ultra-sublime` · `ultra-photo` · `ultra-denoiser`), `engine` (`automatic` ·
`magnific_illusio` · `magnific_sharpy` · `magnific_sparkle`), `presets` (`subtle` · `vivid` · `wild`).
**`presets: "wild"` is never correct for architecture.**

| Input | precision | scale | creativity | hdr | resemblance | fractality | mode / engine | preset |
|---|---|---|---|---|---|---|---|---|
| **D5 / Lumion / Enscape / Twinmotion render** (kill the CGI tell) | creative | 2x | **0** | +3 | +4 | +1 | `ultra-photo` / `magnific_sharpy` | subtle |
| **Corona / V-Ray / Octane / Corona still** (already near-photoreal) | creative | 2x | **−1** | +2 | +5 | 0 | `ultra-photo` / `automatic` | subtle |
| **GPT-Image render from `render.py`** (finish the pipeline) | creative | 2x–4x | **0** | +3 | +4 | +1 | `ultra-photo` / `magnific_sharpy` | subtle |
| **Photo of a built building** | **precision** | 2x | — | — | — | — | `ultra` · sharpness 60 · grain 15 · ultraDetail 55 | — |
| **Interior render** (fabric, timber, stone) | creative | 2x | +1 | +3 | +4 | **+2** | `ultra-photo` / `magnific_sparkle` | subtle |
| **Glazed tower / curtain wall / repeated grid** | **precision** *(or creative at 0)* | 2x | **−2** | +2 | **+6** | −1 | `ultra` / `magnific_sharpy` | subtle |
| **Low-res / compressed / noisy client file** | creative | 4x | 0 | +3 | +5 | 0 | `ultra-denoiser` / `automatic` | subtle |
| **Small screenshot → print / hoarding** | creative | **8x–16x** | −1 | +2 | +5 | 0 | `ultra` / `automatic` | subtle |
| **Aerial / masterplan** (dense small detail) | creative | 4x | 0 | +2 | +5 | +1 | `ultra` / `magnific_sharpy` | subtle |
| **Sketch, plan, elevation, line drawing, diagram** | — | — | — | — | — | — | **STOP** — see below | — |

**Never Magnific a flat drawing.** A sketch, plan, section, elevation or diagram has no realism to
enhance — Magnific will *fur it up*, inventing texture and pseudo-detail across clean linework, and it
will hallucinate. A drawing needs **`render.py` first** (drawing → render), and Magnific *after*, if at
all. Say so and route them.

**Scale reality check:** 16x on a 2000px input is a 32000px file. Pick `scale` from the *delivery* — screen
2x · A3 print 4x · large-format / hoarding 8x+ — not from enthusiasm.

---

## 88.4 · The proposal set (§88's variation menu)

When the user picks Magnific from the §86 menu, offer these as **one compact menu** — do **not** run
twelve renders. Each is a paid call; **name the count and get a yes** (`SKILL.md` §2 cost gate).

Every proposal keeps `resemblance ≥ +4` and `creativity ≤ +2`. **The architecture is identical across all
twelve** — only material response, light and atmosphere move.

```
FINISH        1  Ultra Photorealistic   creative · c 0 · hdr +3 · res +4 · ultra-photo/sharpy
              2  Luxury Edition         creative · c +1 · hdr +4 · res +4 · sparkle · rich material depth
              3  Competition Viz        precision · sharp 65 · grain 20 · crisp, honest, no flair
              4  Real-Estate Marketing  creative · c +1 · hdr +4 · res +4 · bright, warm, saleable
              5  Editorial Architecture creative · c 0 · hdr +2 · res +5 · restrained, print, AD-grade
              6  Minimal Scandinavian   creative · c 0 · hdr +2 · res +5 · pale, soft, low contrast
              7  Modern Contemporary    creative · c 0 · hdr +3 · res +4 · neutral, clean, sharp

ATMOSPHERE    8  Golden Hour   ·  9  Blue Hour  ·  10  Night
              11 Rain          ·  12 Snow
```

**8–12 are NOT Magnific jobs.** Time of day, weather and season are **lighting and scene changes** —
Magnific enhances what's in the pixels, it does not put a sunset there. Route them:

- **8 · 9 · 10 · 11 · 12** → `render.py` (relight / re-weather, geometry + camera + crop locked) → **then**
  Magnific proposal **1** on the result to finish it. Two calls, and say so.
- `images_relight` (Magnific) is a *light-direction* tool (1–4 lights, azimuth/elevation/intensity, gel
  colour) — good for pushing sun angle or adding a warm gel on an existing render, **not** for turning day
  into night. Reach for it only when the ask is genuinely "move the key light".

Tell the user this rather than quietly running the wrong tool. It's the difference between a night render
and a slightly darker day render.

---

## 88.5 · The Magnific output block

Only when the user wants the **settings to run themselves** in the Magnific web app. If they want the
image, **run it and show it** — Mode B shape, no block (`SKILL.md` §4).

```
Input Read:          type · building · int/ext · materials · lighting · camera · design intent · quality
Locked:              geometry · openings · massing · camera · perspective · crop · design intent
Enhancing:           materials · textures · lighting response · vegetation · furniture · atmosphere · resolution
Mode:                creative | precision   (+ why)
Guidance Prompt:     one short factual line — real materials + real light
Negative Prompt:     n/a — the Magnific upscaler takes no negative prompt (steer with resemblance)
Settings:            scale · creativity · hdr · resemblance · fractality · mode · engine · preset
Rendering Strategy:  where Magnific sits in the pipeline (what runs before it, what after)
Expected Outcome:    what will visibly change — and what will NOT
```

`Expected Outcome` must state the **limit** honestly: *"micro-texture in the concrete, believable glass
reflections, 4x resolution — the massing, openings and camera will be pixel-identical, and the sky will
not change."* Setting the ceiling is what stops the user paying for a second pass expecting a redesign.

---

## 88.6 · Failure modes — read the output for these

| Tell | Cause | Fix |
|---|---|---|
| Window bays multiplied / mullions re-drawn / extra balcony | `creativity` too high | Drop to −1, raise `resemblance` to +6, or switch to **precision** |
| Concrete looks like tree bark; smooth surfaces furred | `fractality` too high | Drop to 0 or −1 |
| Crunchy, over-cooked, HDR-plague | `hdr` above +6 | Drop to +2 |
| Vegetation turned to mush / alien plants | Creative pass on soft foliage | Lower creativity; foliage is where it lies most |
| Pseudo-text on signage, hallucinated logos | Magnific "finishing" illegible glyphs | Expected. Never upscale an image whose *text must be legible* — §2: image models don't do text |
| People's faces melted | Small figures + creative mode | Fine at scale-figure size; if they read large, use precision |
| It just looks the same but bigger | Precision mode did its job | That is **correct** for a photo. Only go creative if they want interpretation |

Run **§24** on every Magnific output, plus the one check unique to this section: **count the openings.**
