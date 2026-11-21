#!/usr/bin/env python3
"""Velmora travel-poster entry for make.fun.

Copies the bundled poster (entry.png, a travel poster for the invented
place Velmora — The Floating Lantern Isles) into $MAKEFUN_OUTPUT_DIR
as entry.png, verifying the copy is byte-identical and passes the
competition gate (PNG, <= 1 MiB, <= 1024x1024 px).

Stdlib only. No network. Deterministic: two runs produce byte-identical
output. The output path is read from the MAKEFUN_OUTPUT_DIR environment
variable and never hardcoded.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

SOURCE_NAME = "entry.png"


def _repo_root() -> str:
    """Directory holding this script (the repository root)."""
    return os.path.dirname(os.path.abspath(__file__))


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _png_dimensions(path: str) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk; raise on bad magic."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file (bad magic bytes)")
    if header[12:16] != b"IHDR":
        raise ValueError("not a PNG file (missing IHDR chunk)")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def _check_gate(path: str) -> None:
    """Enforce the competition gate: whole PNG, <= 1 MiB, <= 1024x1024."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ValueError(f"file is {size} bytes, over the {MAX_BYTES} byte cap")
    width, height = _png_dimensions(path)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(f"image is {width}x{height}, over the {MAX_DIMENSION}x{MAX_DIMENSION} cap")


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    source = os.path.join(_repo_root(), SOURCE_NAME)
    if not os.path.isfile(source):
        print(f"error: bundled poster not found: {source}", file=sys.stderr)
        return 1

    # Gate-check the bundled poster before copying it.
    try:
        _check_gate(source)
    except (OSError, ValueError) as exc:
        print(f"error: bundled poster failed the gate: {exc}", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, SOURCE_NAME)
    shutil.copyfile(source, destination)
    os.chmod(destination, 0o644)

    # Verify the copy: gate + byte-identical to the source.
    try:
        _check_gate(destination)
    except (OSError, ValueError) as exc:
        print(f"error: output failed the gate: {exc}", file=sys.stderr)
        return 1
    if _sha256(source) != _sha256(destination):
        print("error: output is not byte-identical to the source", file=sys.stderr)
        return 1

    print(f"wrote {destination} ({os.path.getsize(destination)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
