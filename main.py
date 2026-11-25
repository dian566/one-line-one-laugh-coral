#!/usr/bin/env python3
"""One Line, One Laugh entry (make.fun).

The whole entry is a single funny line. This script is the entry's
program: when the grader runs it, it drops that one line into
/output/entry.txt and exits. Nothing else is produced.
"""

import os

LINE = "My smart fridge suggests recipes based on what's expired \u2014 less an appliance, more a judgmental roommate that glows."

LIMIT = 200


def write_line() -> str:
    """Validate the line against the bounty cap and write it out."""
    text = LINE.strip()
    if len(text) < 1 or len(text) > LIMIT:
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(text)
    return text


if __name__ == "__main__":
    write_line()
