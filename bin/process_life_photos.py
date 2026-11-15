#!/usr/bin/env python3
"""Resize photos from _life_raw/ into assets/img/life/ with all metadata (EXIF, GPS) removed.

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
MAX_SIDE = 1600
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
    OUT.mkdir(parents=True, exist_ok=True)
    for src in sorted(RAW.iterdir()):
        if src.suffix.lower() not in EXTS:
            continue
        dst = OUT / (src.stem.lower().replace(" ", "-") + ".jpg")
        if dst.exists() and not force:
            continue
        img = ImageOps.exif_transpose(load(src)).convert("RGB")
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        # Copy pixels into a fresh image so no metadata survives.
        clean = Image.new("RGB", img.size)
        clean.putdata(list(img.getdata()))
        clean.save(dst, "JPEG", quality=85, optimize=True, progressive=True)
        print(f"{src.name} -> {dst.relative_to(ROOT)} {clean.size[0]}x{clean.size[1]} "
              f"{dst.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
