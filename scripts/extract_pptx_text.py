#!/usr/bin/env python3
"""Extract slide text from a PPTX for content and claim review."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

try:
    from pptx import Presentation
except ImportError as exc:
    raise SystemExit("python-pptx is required: python -m pip install python-pptx") from exc


def iter_shape_text(shape) -> Iterable[str]:
    if getattr(shape, "has_text_frame", False):
        text = shape.text_frame.text.strip()
        if text:
            yield text

    if getattr(shape, "has_table", False):
        for row in shape.table.rows:
            cells = [cell.text.strip() for cell in row.cells]
            text = " | ".join(cells).strip()
            if text:
                yield text

    if hasattr(shape, "shapes"):
        for child in shape.shapes:
            yield from iter_shape_text(child)


def extract(pptx_path: Path) -> list[dict[str, object]]:
    presentation = Presentation(str(pptx_path))
    slides: list[dict[str, object]] = []
    for index, slide in enumerate(presentation.slides, start=1):
        texts: list[str] = []
        for shape in slide.shapes:
            texts.extend(iter_shape_text(shape))
        slides.append({"slide": index, "texts": texts})
    return slides


def render_text(slides: list[dict[str, object]]) -> str:
    blocks: list[str] = []
    for slide in slides:
        blocks.append(f"## Slide {slide['slide']}")
        texts = slide["texts"]
        if texts:
            blocks.extend(f"- {text}" for text in texts)
        else:
            blocks.append("- [no text]")
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    slides = extract(args.pptx.resolve())
    content = (
        json.dumps(slides, ensure_ascii=False, indent=2) + "\n"
        if args.as_json
        else render_text(slides)
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
        print(f"Wrote {args.output.resolve()} with {len(slides)} slides.")
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
