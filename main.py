#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt (single line, under 200 characters).
"""

import os

ENTRY = (
    "I deployed my untested fix straight to production. "
    "It fixed the bug in 12 seconds and deleted 4 years of user data in 11."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
