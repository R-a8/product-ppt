---
name: product-ppt
description: 图像主导的中文产品路演 PPT 工作流——把产品介绍、商业计划或项目资料做成一套以图为主、文字辅助、可原生编辑的 PPTX。当用户要做产品 PPT、产品介绍、路演 PPT、项目介绍、竞赛答辩 PPT、创业融资 BP、pitch deck，或要求重写、换版、美化、排版、修改已有的产品演示 PPTX 时触发。不用于纯数据报告、纯动画视频或单页海报。
---

# Product PPT

Build a Chinese product pitch deck that a first-time viewer can understand without the presenter explaining every slide. The deck is visual-first but every image must explain the product, its interaction, its process, or its value; text stays native and editable; facts are separated into current state, pending work, and targets.

Typical inputs: a product document, a patent or technology list, market notes, an existing PPTX to revise, or a plain-text brief. Typical output: a 16:9 PPTX with generated or sourced visuals, consistent header system, and per-page visual QA.

## Non-negotiable outcomes

- Every claim traces to the user's source material or an explicit assumption. Targets, current traction, and deprecated figures are visibly separated and never merged.
- Body copy follows [references/copy-rules.md](references/copy-rules.md): complete Chinese sentences a presenter could read aloud, the five-step argument chain (problem, existing products, their pricing, the gap, then the product thesis), and three-tier fact labeling (current / in progress / target). Keyword strings and slogan fragments are not explanations.
- No redundant explanation: every sentence adds new information. Fact tiers are carried by wording ('计划', '目标', '尚未', '暂未'), never by a trailing sentence that re-explains what the previous sentence, the title, or the visual already said.
- Each page carries a four-character section title plus a one-line page subtitle, applied identically on every content page.
- Images are large enough to carry the page (roughly 60–70% of evidence-heavy pages) but contain no readable text, logos, or fake data; all typography is native.
- Every page is rendered and inspected at presentation resolution before delivery, not only inside the editor.

## Workflow

1. **Build the source ledger first.** Read the handoff note, product document, and data sources. Record current facts, targets, pending work, and forbidden or deprecated figures. When a reference deck exists, separate which of its attributes the user authorizes (content, title style, palette, layout) and follow that boundary exactly.

2. **Write the narrative before any visuals.** State the product in one repeatable sentence, then lay out the page order using the sequence in [references/content-playbook.md](references/content-playbook.md): problem discovery, existing products and their pricing, the gap, the product thesis, forms, interaction, payoff, core technologies, business, partners, team, future. Adjust the order only when the user's logic requires it.

3. **Write complete slide copy before designing.** Follow the page-level rules in the content playbook and the detailed Chinese copy standards in [references/copy-rules.md](references/copy-rules.md). For each core technology, write only what it is and which failure it prevents — one or two sentences each, not a paragraph of architecture terms.

4. **Apply the deck-wide header system.** On every content page: four-character section title in the primary color, a short accent bar, the page subtitle in muted text, then a hairline divider. The logo sits at the same coordinates top-right; page number and source note share one footer baseline. The cover and closing pages may deviate deliberately.

5. **Plan and acquire visuals.** Inventory user-supplied images first and reuse what is relevant. Then:
   - For product scenes, forms, interaction, memory, and technology evidence, generate coherent 16:9 images with one palette, lighting, and overlay language. Write prompts with the formula in [references/visual-and-image-system.md](references/visual-and-image-system.md): format → scene → product truth → visual explanation → art direction → composition → exclusions. Generate at 2K where available, then normalize. When the user supplies a provider API key, read it from an environment variable or the current session and never persist it into any file.
   - For named competitors, partners, or brands, capture real logos or product images from an image-search page in a real browser (e.g. via Playwright), screenshot the clearest candidate, trim near-white borders, and mark the asset as identification-only in the page footer or manifest.
   - Build a contact sheet after every batch with `scripts/build_contact_sheet.py` and inspect it before placing assets.

6. **Build editable slides.** Keep images, shapes, titles, subtitles, body copy, charts, and footers as separate native layers. When a project pipeline exists (for example an SVG-to-PPTX project), edit its current source files instead of rebuilding from zero. Long sentences get explicit manual line breaks sized to their container, never silent shrink-to-fit.

7. **Run both QA passes.** Use [references/qa-checklist.md](references/qa-checklist.md): first the fact and narrative pass, then render every slide to an image (e.g. PowerPoint export at full size) and inspect each one for clipping, collision, contrast, hierarchy, and header consistency. Fix and re-render until clean.

8. **Deliver the package.** Return the final PPTX path plus the editable source, the generated-image folder or prompt manifest, and speaker notes when present. Name the major changes and flag any unresolved fact or asset risk in one or two sentences.

## Revision rounds

When the user revises a delivered deck, act at the owning layer:

- A wording or emphasis change edits the affected page's copy, then re-render that page.
- A section rewrite (for example "rebuild the product introduction around this logic") re-plans that section's page sequence first, then rewrites copy, then replaces visuals only where the message changed.
- A header or style change applies to every page that uses the system, then the whole deck is re-rendered once.
- Never restart planning from zero when the narrative contract is intact.

## Reference routing

- [references/content-playbook.md](references/content-playbook.md) — source ledger, one-sentence positioning, narrative architecture, page copy rules, product/technology/business writing.
- [references/copy-rules.md](references/copy-rules.md) — detailed Chinese copy standards: complete-sentence rule, argument chain, fact tiers, number style, team credits, technology pages, line breaking, banned words, read-aloud acceptance.
- [references/visual-and-image-system.md](references/visual-and-image-system.md) — palette, image-first page patterns, prompt formula, image families, data visualization, editable-slide rules, generation access.
- [references/qa-checklist.md](references/qa-checklist.md) — fact pass, image-batch pass, rendered-slide pass, delivery pass.

## Scripts

- `scripts/build_contact_sheet.py` — assemble a labeled contact sheet of a generated-image batch for inspection before placement.
- `scripts/extract_pptx_text.py` — extract all slide text from a PPTX to audit copy, claims, and repeated phrases after export.
