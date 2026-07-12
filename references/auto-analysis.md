# 85 · Auto-Analysis & Intelligent Prompt Generator

> Fires **automatically** on ANY architectural image upload. No interrogation, no "what style would you
> like?" — analyze, decide, deliver. **Preservation Contract applies** (see `SKILL.md` §2).

---

## The rule

When the user uploads an architectural image and wants a render or a prompt, **do not ask questions.**
Read the image, fill every field below from what you can actually see, default the rest, and hand back a
production-ready prompt. Ask only if something **essential** is genuinely undecidable from the image and
can't be safely defaulted (rare — usually only "which platform?" and even that has a universal default).

---

## Step 1 · Structured read of the image (do this silently)

Detect, from the image itself:

| Field | What to look for |
|---|---|
| **Input type** | sketch · hand drawing · CAD line · plan · section · elevation · facade · BIM/SketchUp/Revit/Rhino/ArchiCAD screenshot · Blender/3ds Max/C4D viewport · clay/white model · D5/Lumion/Enscape/Twinmotion/Unreal/Octane/Redshift render · interior photo · exterior photo · site photo · physical model |
| **Clause it triggers** | flat/line/clay → **preserve** · finished render → **Enhance** · photo of a built building → **preserve, materials-locked** (`source-tools.md`) |
| **Building type** | residential · villa · apartment · tower · office · retail · hospitality · civic · industrial… (→ pull the brief from `typologies/` if the type has real constraints) |
| **Interior or exterior** | and which space, if interior |
| **Design intent** | the parti — what the building is *trying* to do. Say it in one line. |
| **Style / language** | modern · minimalist · Mediterranean · brutalist · parametric · vernacular… |
| **Materials visible** | per surface: facade, roof, frames, ground plane, interior floor/wall/ceiling. Run the **§47 material system** — identify each with a confidence level (**read / estimate / unknown**), and never fabricate one. |
| **Lighting** | direction, hardness, time of day, colour temperature — read the shadows |
| **Camera** | angle, height, approximate lens (24 / 35 / 50 / 85mm), one- or two-point, tilt |
| **Composition & crop** | framing, what's centred, **the aspect ratio** |
| **Environment** | urban / rural / coastal / forest / desert; context buildings; vegetation |
| **Weather & season** | sky, ground wetness, foliage state |
| **Source engine** | if it's a render, which engine's look (affects whether to polish or rebuild) |

**Whatever you cannot see, you do not invent.** If the sketch shows no material, choose a *defensible
default* for the building type and **say you chose it** in one line — don't silently assert it as the
user's intent.

---

## Step 1b · Did they say what they want? (the fork)

| | |
|---|---|
| **Intent stated** — "render this", "make it photoreal", "review it", "generate a prompt", "night version", "turn this into 3D" | **Skip the menu. Execute.** Go to Step 2. Never interrogate a user who already told you the job. |
| **Bare upload, no instruction** — an image and nothing else, or "what do you think of this?" with no verb | **§86 Smart Image Action Menu.** Don't guess which of 23 different jobs they want — guessing burns a paid render on the wrong one. |

---

# 86 · Smart Image Action Menu

Fires **only** on a bare upload with no stated intent. Run the **silent read** (Step 1) first — the menu
is *smart* because it knows what the image is, and says which option fits it.

**Reply shape:** one line of what you see · the **recommended** option and why · the menu · then stop.

> *I've got a **D5 render** of a 4-storey apartment building, 4:3, eye-level three-quarter, overcast.
> For an existing render, **3 · Enhance** is usually what you want — polish realism, keep every
> architectural element. Say a number (or just tell me what you want):*

Then the menu, grouped so it scans. **Numbers are stable — never renumber them:**

```
PROMPTS          1  Generate a professional AI prompt
                21  Generate platform-specific prompts (Midjourney / GPT Image / FLUX / SD…)

RENDER           2  Create a photorealistic render
                 3  Enhance the existing render
                 4  Transform into a different render style
                10  Generate multiple design variations
                20  Upscale & improve image quality
                25 ★ Magnific AI — photoreal finish & upscale (2x–16x, print-ready)

MODIFY           5  Change materials and textures
                 6  Change lighting or time of day
                 7  Interior design enhancement
                 8  Exterior design enhancement
                 9  Landscape enhancement

ANALYSE          11 Review and critique the design
                12 Analyze floor plan or layout
                22 Explain the design
                23 Estimate visible materials

REPRESENT       16 Convert to sketch style
                17 Convert to clay render
                18 Convert to white model
                19 Generate architectural diagrams

PRESENT         13 Create a presentation board
                14 Generate moodboards
                15 Create marketing visuals
                24 ★ Full client presentation package  (plan → approve → produce)
                26 ★ Magnific Production Studio — input → full costed package → client PDF
```

**24** is the bundle: §87 proposes a costed production plan (renders + boards + narrative), you approve
or trim it, then it produces the whole set under one visual identity. Recommend it when the user's
context smells like a pitch — a developer, a competition, a client meeting.

**25 is always on the menu** (see `magnific.md`, §88) — Magnific is the *finisher*: micro-detail, material
grain, real print resolution. **Two exceptions where you must say so instead of offering it blindly:**
- **Flat drawings** (sketch · plan · section · elevation · diagram) — there is no realism to enhance;
  Magnific furs up clean linework and hallucinates. Route to **2** first, Magnific after.
- **Already low-quality composition** — Magnific sharpens a bad render into a sharper bad render. If the
  lighting or materials are the problem, that's **3** or **6**, not 25.

Recommend **25** outright when the input is a **finished render that just needs polish**, or when the
image is **small / compressed / low-res** and the user needs it for print.

**26** is the full production run (`magnific-studio.md`, §89): analyze → sort every deliverable into
**Tier A (derivable from this image) / Tier B (needs a source from you) / Tier C (invention — refused by
default)** → one costed proposal → one approval → a consistent render set under a locked Project Identity
→ a laid-out client PDF. Recommend it over **24** when the user wants renders *and* a deck and Magnific is
the engine. **Never fire it unasked** — "upscale this" is not a proposal request.

**Which to recommend, by what you read in Step 1:**

| The image is… | Recommend | Because |
|---|---|---|
| Finished render (D5 / Lumion / Octane / Corona) | **3 · Enhance** or **25 · Magnific** | Geometry, camera and materials are already right — polish, don't rebuild. **3** if the light or materials still need work; **25** if it just needs realism and resolution |
| Low-res / compressed / small file, or anything headed for **print** | **25 · Magnific** | This is exactly what it's for — 2x–16x, past GPT Image's 3840px ceiling |
| Sketch / hand drawing / CAD line / elevation | **2 · Photorealistic render** | The obvious next step from a flat drawing |
| Floor plan | **12 · Analyze layout** or **2 · Render** (dollhouse) | Offer both — they're the two things people want from a plan |
| Clay / white model / SketchUp screenshot | **2 · Photorealistic render** | Materials + lighting + context is the missing layer |
| Photo of a built building | **6 · Lighting / time of day** | Nothing needs inventing; relight it (materials stay locked) |
| Presentation board / competition panel | **11 · Review** or **13 · Board** | It's already a deliverable — critique or rework the layout |
| Moodboard / reference sheet | **1 · Prompt** or **14 · Moodboard** | It's an input to something else |

**Rules:**
- **One menu, then stop.** Don't render anything, don't critique anything, don't ask a second question.
- **Any answer works** — a number, several numbers, or plain words ("just make it look real"). If they
  answer in prose, act on the prose; don't force them back to the numbers.
- **The menu is a fallback, not a toll booth.** The instant intent is clear — in the first message or the
  next one — skip it forever for that image.
- **Preservation Contract applies to every option on it.** None of the 23 is permission to redesign.

---

## Step 2 · Deliver ONE prompt, immediately

Fill the `SKILL.md` §3 output block from the read above. This is the **best-fit** prompt — the one that
does what the input is obviously asking for:

| Input | Best-fit output |
|---|---|
| Hand sketch / CAD line / elevation | photorealistic render, faithful to the drawing |
| Floor plan | 3D dollhouse cutaway |
| Section | section perspective with furnished interiors |
| Clay / white model / SketchUp screenshot | full photoreal with materials + context |
| **Existing render (D5/Lumion/Octane…)** | **enhancement prompt** — polish realism, keep every architectural element |
| Interior photo | relight / restyle, materials locked unless asked |
| Site photo | context/massing study or site-analysis diagram |
| Physical model | photoreal building, every proportion kept |

State the two lines that matter, then the block. No preamble.

---

## Step 3 · Offer the variations as a MENU (don't dump them)

Prompts are free; **renders are not.** So: generate the primary prompt, then offer the rest as a compact
numbered menu — one line, not nineteen blocks.

> *"Variations ready — say a number, several, or **all**:
> 1 photorealistic · 2 ultra-realistic · 3 day · 4 golden hour · 5 blue hour · 6 sunset · 7 night ·
> 8 rain · 9 fog · 10 snow · 11 summer · 12 autumn · 13 winter · 14 luxury · 15 minimal ·
> 16 competition · 17 real-estate · 18 editorial · 19 cinematic"*

- User picks numbers → generate those **prompts** in full.
- User says **"all"** → generate all of them. They're text; it's fine.
- User wants them **rendered** → that's `--aspect auto` × N paid API calls. **State the count, get a yes**
  (`SKILL.md` §4), and hold the set to one **Project Identity** (**§80**) so they read as one building.

---

## Step 4 · Platform targeting

Default to a **universal** prompt (works across MJ / GPT Image / SD / FLUX / Leonardo) and offer to render
it here. If the user names a platform — GPT Image · Midjourney · Imagen · FLUX · Leonardo · SDXL ·
Ideogram · Recraft · DALL·E · Firefly · Reve — tune with its adapter in `output-format.md`.

**Say which platforms can actually hold the geometry.** Only image-conditioned tools (this skill's GPT
Image renderer, SD+ControlNet, Firefly on an existing image) truly preserve an uploaded design. Text-only
tools (Midjourney, Imagen, Ideogram) **reinterpret** it — if the user's whole point is fidelity to their
drawing, tell them that before they waste a day in Midjourney.

---

## Step 5 · Before returning

Run **§24** silently. Confirm the crop and aspect ratio of the input are carried through (`--aspect auto`),
and that nothing in the prompt asks the model to change something the user didn't ask to change.

---

## Worked shape (what a good reply looks like)

> **Read:** SketchUp clay screenshot · 2-storey Mediterranean villa · exterior · 4:3 · eye-level
> three-quarter, ~35mm · no materials yet (clay) · overcast studio light.
> **Doing:** full preserve clause + photoreal materials & context. I've defaulted the palette to cream
> stucco / stone base / dark bronze frames — say the word if it's something else.
>
> *[the §3 output block]*
>
> Render it now, or pick a variation: 4 golden hour · 7 night · 17 real-estate · … (say a number or "all").

Two lines of read, the block, one line of offer. **Not** a page of analysis.

---
