# QA Checklist

Run both passes after the last content edit and after the final PowerPoint export.

## Fact and narrative pass

- The first two pages make the product category, audience, and promised change clear.
- Every market figure has year, scope, and a named source.
- Current traction, planned targets, and aspirational future are visibly different.
- No unsupported customer, contract, patent grant, user count, or revenue claim remains.
- The page sequence answers why, what, how, proof, business, team, and future in a logical order.
- Each page has one conclusion and one reason to exist.
- Core technologies use specific professional terms and explain the failure they prevent.
- Partner names are labeled targets unless signed evidence exists.
- Team roles distinguish advisers and students.

Use `scripts/extract_pptx_text.py` to review the final copy:

```bash
python scripts/extract_pptx_text.py deck.pptx --output deck-text.txt
```

Scan for repeated phrases, leftover placeholder copy, accidental data leakage, and claims that conflict with the source ledger.

## Image-batch pass

- All accepted images follow one palette, lighting, and material language.
- No generated image contains fake readable Chinese, formulas, numbers, logos, watermarks, or malformed hands.
- Product form is understandable from the image.
- Interaction image shows what the user does and what the system returns.
- Technical image shows the actual failure/evidence relation rather than a generic dashboard.
- Negative space is usable for slide copy.
- No image is reused merely because it looks attractive when it does not support the page.

Create and inspect a contact sheet:

```bash
python scripts/build_contact_sheet.py generated-images --output contact-sheet.jpg
```

## Rendered-slide pass

Inspect every slide as a full-size image, not only inside the editor.

- Title, body, image, chart, logo, source, and page number are inside safe margins.
- No text is clipped or hidden behind an image.
- No two objects collide at the actual export resolution.
- Contrast is sufficient for projection.
- Title hierarchy is consistent across the deck.
- Section labels and page names align with the contents page.
- Logos keep their aspect ratio and identical position.
- Charts have readable labels, units, and target/actual status.
- Speaker notes and on-slide text do not contradict each other.
- The final page closes the story without introducing a new claim.

## Delivery pass

- Open the PPTX once after export and confirm the correct page count.
- Check that native text, charts, and shapes remain editable.
- Confirm the final link points to the latest file.
- Include the source-image folder or prompt manifest when image reuse matters.
- Report unresolved risks plainly instead of hiding them behind confident language.
