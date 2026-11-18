#!/usr/bin/env python3
"""news-image-20261118 entry: write the front page to /output/entry.png.

The artwork lives in this repository as a base64 text file
(``entry.png.b64``) so the whole entry stays plain UTF-8, which is what
the submission tooling can push. At run time this program decodes that
file and writes the image out as ``entry.png`` inside the output
directory the grader points at (``$MAKEFUN_OUTPUT_DIR``, falling back
to ``/output``).

There is no network access, no randomness, and no dependency beyond
the standard library, so two runs of this program always produce
exactly the same bytes. Before writing, the decoded data is checked
for the PNG signature and the IHDR dimensions, so a corrupted payload
fails loudly instead of silently producing a broken file.

The picture itself: a newspaper front page for Wednesday 18 November
2026, "THE WORLD TODAY". The lead story is the world gathering in
Manila — Trump landing for the Quad talks ahead of a China visit, Modi
rallying ASEAN leaders — drawn as a dusk skyline with the four Quad
flags. Four more stories get large-type cards: Ukraine striking the
Crimean Bridge for a second day, Iran's drone attack on a US radar
site in Bahrain, Cyclone Akvan bearing down on India's east coast,
and four allies demanding aid access for flooded Gaza while Britain
sanctions settlement firms. A footer strip carries the rest of the
day: Dhoni retiring from the IPL, Amazon's $7bn renewables plan for
India, Canada-China trade deals, the EU's €45bn Ukraine loan, and
Baidu's AI-bubble warning. The image was drawn programmatically
(render.py, Pillow) so every word is perfectly legible.
"""

import base64
import os
import struct
import sys
from pathlib import Path

SOURCE_NAME = "entry.png.b64"
OUTPUT_NAME = "entry.png"
# A PNG starts with this 8-byte signature, then the IHDR chunk whose
# payload carries width and height (4 bytes each, big-endian).
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_DIMENSION = 1024
MAX_BYTES = 1_048_576


def output_directory() -> Path:
    """Where the grader wants the image (env var, else /output)."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def check_png_complete(data: bytes) -> None:
    """Walk the PNG chunk list and confirm the file ends at IEND.

    Each chunk is length (4 bytes) + type (4) + payload + CRC (4).
    A truncated payload stops mid-chunk or never reaches IEND, so
    this catches a cut-off file that the header checks alone miss.
    """
    pos = 8  # past the PNG signature
    while pos + 8 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        chunk_type = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise ValueError(f"truncated PNG: {chunk_type!r} chunk runs past the end")
        if chunk_type == b"IEND":
            if end != len(data):
                raise ValueError("trailing bytes after the PNG IEND chunk")
            return
        pos = end
    raise ValueError("no PNG IEND chunk found (file is truncated)")


def load_image_bytes() -> bytes:
    """Decode the stored artwork and sanity-check it is a PNG."""
    source = Path(__file__).resolve().parent / SOURCE_NAME
    text = source.read_text(encoding="ascii")
    data = base64.b64decode("".join(text.split()), validate=True)
    if len(data) > MAX_BYTES:
        raise ValueError(f"image is {len(data)} bytes, over the 1 MiB limit")
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("decoded data is not a PNG (bad signature)")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(f"image is {width}x{height}, over the 1024x1024 limit")
    check_png_complete(data)
    return data


def main() -> int:
    data = load_image_bytes()
    out_dir = output_directory()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / OUTPUT_NAME
    out_path.write_bytes(data)
    print(f"wrote {out_path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
