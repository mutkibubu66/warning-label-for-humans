#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes one original single-line safety warning label for every human
being to /output/entry.txt. Pure Python stdlib, no network.

The label: a real warning-label "contains" list (water, unfinished
projects) whose punchline lands in the last few words -- the human
has absolutely no idea what it is doing. Universally true, one idea,
one read. The final ingredient ("absolutely no idea") is deliberately
plain English rather than a percentage: it breaks the list's pattern
at the last moment, which is where the laugh sits.
"""

import os

ENTRY = (
    "WARNING: This human contains 70% water, 30% unfinished projects, "
    "and absolutely no idea what it is doing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
