#!/usr/bin/env python3
"""One Emoji, One Smile (u-0xkianno-one-emoji-one-smile-5470751f).

Writes exactly one emoji to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when the harness sets it): a dog's face -- the warmest hello a stranger
can get, no words needed.

The entry is a plain string constant: no network, no randomness, no
external input -- the program is fully deterministic.
"""

import os

# U+1F436 DOG FACE -- one character, 4 bytes UTF-8, no trailing newline.
EMOJI = "\U0001F436"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check: the entry must be exactly one emoji, nothing else.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == EMOJI.encode("utf-8"), raw
    assert len(EMOJI) == 1, len(EMOJI)


if __name__ == "__main__":
    main()
