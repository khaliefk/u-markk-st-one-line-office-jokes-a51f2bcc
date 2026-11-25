#!/usr/bin/env python3
"""One-Line Office Jokes entry for make.fun.

Writes a single original one-line joke about office life to
/output/entry.txt. Standard library only, no network, no input.
"""

import os

ENTRY = "HR said we're a family. So I asked who inherits the printer when it dies again."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, f"entry out of gate: {len(ENTRY)} chars"
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
