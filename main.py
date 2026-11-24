#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single one-line comedy joke to
$MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

JOKE = "I bought noise-canceling headphones so I could hear myself think, and it turns out I have nothing to say."


def main() -> int:
    # Self-check the gate before writing: one line, 1-280 chars, not blank.
    if not (1 <= len(JOKE) <= 280) or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke fails the entry gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
