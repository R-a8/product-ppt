#!/usr/bin/env python3
"""Build a labeled contact sheet for a folder of pitch-deck images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def fit_label(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> str:
    if draw.textlength(text, font=font) <= max_width:
        return text
    suffix = "..."
    while text and draw.textlength(text + suffix, font=font) > max_width:
        text = text[:-1]
    return text + suffix


def build_sheet(
    input_dir: Path,
    output: Path,
    columns: int,
    thumb_width: int,
    thumb_height: int,
) -> int:
    images = sorted(
        path for path in input_dir.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    if not images:
        raise SystemExit(f"No supported images found in: {input_dir}")

    columns = max(1, columns)
    rows = (len(images) + columns - 1) // columns
    gap = 20
    label_height = 54
    tile_width = thumb_width
    tile_height = thumb_height + label_height
    sheet_width = columns * tile_width + (columns + 1) * gap
    sheet_height = rows * tile_height + (rows + 1) * gap

    sheet = Image.new("RGB", (sheet_width, sheet_height), "#F3F7FB")
    draw = ImageDraw.Draw(sheet)
    label_font = load_font(17)
    size_font = load_font(14)

    for index, path in enumerate(images):
        row, column = divmod(index, columns)
        x = gap + column * (tile_width + gap)
        y = gap + row * (tile_height + gap)

        with Image.open(path) as source:
            source = ImageOps.exif_transpose(source).convert("RGB")
            original_size = source.size
            thumbnail = ImageOps.contain(source, (thumb_width, thumb_height))

        tile = Image.new("RGB", (tile_width, tile_height), "white")
        paste_x = (thumb_width - thumbnail.width) // 2
        paste_y = (thumb_height - thumbnail.height) // 2
        tile.paste(thumbnail, (paste_x, paste_y))

        tile_draw = ImageDraw.Draw(tile)
        label = fit_label(tile_draw, path.name, label_font, tile_width - 24)
        tile_draw.text((12, thumb_height + 7), label, fill="#17324D", font=label_font)
        dimensions = f"{original_size[0]} x {original_size[1]}"
        tile_draw.text((12, thumb_height + 29), dimensions, fill="#5A7288", font=size_font)

        sheet.paste(tile, (x, y))
        draw.rectangle(
            [x, y, x + tile_width - 1, y + tile_height - 1],
            outline="#BFD8EC",
            width=1,
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92, subsampling=0)
    return len(images)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--output", type=Path, default=Path("contact-sheet.jpg"))
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--thumb-width", type=int, default=480)
    parser.add_argument("--thumb-height", type=int, default=270)
    args = parser.parse_args()

    count = build_sheet(
        input_dir=args.input_dir.resolve(),
        output=args.output.resolve(),
        columns=args.columns,
        thumb_width=args.thumb_width,
        thumb_height=args.thumb_height,
    )
    print(f"Created {args.output.resolve()} from {count} images.")


if __name__ == "__main__":
    main()
