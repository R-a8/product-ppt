# Visual and Image System

## Contents

- Deck visual frame
- Image-first page patterns
- Product-image prompt formula
- Image families
- Data visualization
- Editable-slide rules
- Generation access

## Deck visual frame

Choose one visual system before creating pages. A practical starting point for technology and education products:

| Role | Suggested value |
| --- | --- |
| Background | near-white with a cool tint |
| Primary | deep blue or dark navy |
| Technology accent | cyan or blue |
| Warning or human accent | amber, used sparingly |
| Body text | slate or ink |
| Divider | pale blue-gray |
| Title | large, bold sans serif |
| Body | readable sans serif |

Use a 1280×720 authoring canvas for a 16:9 SVG-to-PowerPoint workflow, or 1920×1080 for direct image and PowerPoint production. Keep page margins stable. Do not let a generated image's composition dictate inconsistent text placement.

## Image-first page patterns

Choose one dominant pattern per page:

### Hero scene

One large cinematic or editorial image occupies 55–75% of the canvas. Text sits in the reserved negative space. Use this for the cover, problem, ideal outcome, product forms, team, social value, and future vision.

### Product proof

Show a phone, device, paper surface, stand, lamp, glasses, or app view at a realistic scale. Add abstract overlays only to explain capture, process, or feedback. Do not show a polished app that claims features the product does not have.

### Process narrative

Use one continuous scene or a left-to-right sequence. The viewer should understand start, action, feedback, and next step without reading a large diagram.

### Technology evidence

Use a close-up of the real material or interaction, then show only the relationships needed to explain the failure: frames, occlusion, changed strokes, semantic alternatives, missing evidence, or first-deviation path. Technical pages still need a human-readable conclusion.

### Ecosystem or partnership map

Use one central capability and named partner groups around it. Keep logos secondary to the explanation of why each partner matters.

## Product-image prompt formula

Write prompts in this sequence:

1. **Format:** 16:9 premium editorial/product render, etc.
2. **Scene:** who is doing what, with which ordinary object or device.
3. **Product truth:** camera angle, device form, physical interaction, feedback surface.
4. **Visual explanation:** translucent path, event nodes, evidence frames, comparison, or memory network.
5. **Art direction:** lighting, material realism, palette, cleanliness.
6. **Composition:** negative space for slide copy and location of main focus.
7. **Exclusions:** no readable text, no logos, no watermark, no fake numbers, no brand imitation, no extra fingers, no duplicated person.

Example skeleton:

> Premium 16:9 product concept scene for [category]. [User] interacts with [ordinary paper, phone, or device] in [setting]. The composition clearly shows [capture angle/product form/interaction]. Subtle [palette] overlays explain [process/evidence/feedback] without readable text. Realistic materials, coherent lighting, [light editorial style]. Strong negative space on [side] for slide copy. No readable text, numbers, formulas, logos, watermark, fake interface labels, duplicated people, or malformed hands.

Avoid prompts that ask the image model to render key Chinese copy. Generate the visual without text and add typography natively.

## Image families

Create a family rather than fourteen unrelated images:

- Same color temperature and lighting.
- Same amount of realism.
- Same overlay thickness and node language.
- Same camera distance for scenes of the same importance.
- Same focal point for product form versus process evidence.
- Human faces only when emotion or context matters; otherwise hands, paper, devices, and silhouette can communicate more reliably.

When generating product variants, list the forms in one prompt so proportions and materials match. When generating technical concepts, create separate prompts for different failure modes rather than asking one image to explain everything.

Before generating a batch, inspect supplied product photos, screenshots, UI captures, and concept renders. Crop and place a real asset when it explains the product better than a new image. Generate new visuals for missing scenes or coherent concept imagery; do not replace real evidence with a prettier fictional interface.

## Data visualization

- Start with the claim: “Revenue is planned to grow through partner annual contracts and consumer subscriptions.”
- Use one chart type. A three-year plan usually works with a column chart plus a small assumptions table.
- Put units and period on the chart.
- Label target values as targets, not actuals.
- Use a single accent color for the current focus and muted colors for context.
- If two market figures come from different methodologies, show them as separate sources; never add them.
- Prefer one large number and one comparative context over a dashboard with ten small metrics.

## Editable-slide rules

- Images may be screenshots or generated raster assets; text must remain native.
- Put title, subtitle, body, chart labels, source, page number, and logo in separate objects.
- Use consistent font families and weights.
- Avoid grouping text with images before export unless the format preserves editability.
- Keep reading order sensible for accessibility.
- When a logo is required on every page, place it in the same coordinates and keep its aspect ratio. Do not stretch it.
- If a page needs a process flow, use native shapes and connectors over a clean background image rather than generating the entire diagram as a bitmap.

## Generation access

Prefer the environment's native image-generation tool. If the user supplies a provider API, read the key from an environment variable and never write it into the skill, prompt manifest, project files, or final response.

For Alibaba DashScope image generation, a practical default is `qwen-image-2.0-pro` with 16:9 output if the account supports it. Generate at a higher resolution such as 2K when available, then resize and crop the accepted asset to the deck canvas. Verify the actual returned dimensions and inspect every result; model names, quotas, and response formats can change.

For each batch, save:

- the prompt manifest as JSON;
- accepted images under one folder;
- rejected variants under another when useful;
- a contact sheet;
- a short note describing which page each accepted image serves.

If generation access is unavailable, use user-supplied images or build the visual with native vector diagrams. Do not pretend a planned image exists.
