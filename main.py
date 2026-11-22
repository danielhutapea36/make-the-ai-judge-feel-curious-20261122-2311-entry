#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text (1-280 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no time dependence.
"""

import os

TEXT = (
    "The back door stands open a finger's width. Beyond it the garden is dark, "
    "except for one square of kitchen light lying on the grass, where a moth circles "
    "nothing at all. You could close the door. Instead you stand there, "
    "wondering what the moth knows that you don't."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
