# SPDX-License-Identifier: MIT
"""Emit the competition one-liner to /output/entry.txt."""
from pathlib import Path

JOKE = "My smart fridge suggests recipes based on what's expired — less an appliance, more a judgmental roommate that glows."
MAX_CHARS = 200
TARGET = Path("/output/entry.txt")


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry length {len(line)} outside 1..{MAX_CHARS}"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(line, encoding="utf-8")


main()
