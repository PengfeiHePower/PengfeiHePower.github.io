#!/usr/bin/env python3
"""Resize photos from _life_raw/ into assets/img/life/ with all metadata (EXIF, GPS) removed.

Each photo gets a full-size version for the lightbox (assets/img/life/) and a
small one for cards and grids (assets/img/life/thumb/).

Usage: python3 bin/process_life_photos.py [--force]
"""
import pathlib
import subprocess
import sys
import tempfile

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "_life_raw"
OUT = ROOT / "assets" / "img" / "life"
SIZES = {OUT: (2560, 86), OUT / "thumb": (960, 82)}  # folder: (max side, JPEG quality)
EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".tif", ".tiff", ".webp"}


def load(path):
    if path.suffix.lower() in {".heic", ".heif"}:
        tmp = pathlib.Path(tempfile.mkdtemp()) / (path.stem + ".jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", str(path), "--out", str(tmp)],
                       check=True, capture_output=True)
        path = tmp
    return Image.open(path)


def main():
    force = "--force" in sys.argv
    for folder in SIZES:
        folder.mkdir(parents=True, exist_ok=True)
    for src in sorted(RAW.iterdir()):
        if src.suffix.lower() not in EXTS:
            continue
        name = src.stem.lower().replace(" ", "-") + ".jpg"
        if all((folder / name).exists() for folder in SIZES) and not force:
            continue
        img = ImageOps.exif_transpose(load(src)).convert("RGB")
        for folder, (max_side, quality) in SIZES.items():
            resized = img.copy()
            resized.thumbnail((max_side, max_side), Image.LANCZOS)
            # Copy pixels into a fresh image so no metadata survives.
            clean = Image.new("RGB", resized.size)
            clean.putdata(list(resized.getdata()))
            dst = folder / name
            clean.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
            print(f"{src.name} -> {dst.relative_to(ROOT)} {clean.size[0]}x{clean.size[1]} "
                  f"{dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
