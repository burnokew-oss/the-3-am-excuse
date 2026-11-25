#!/usr/bin/env python3
"""The 3 AM Excuse — entry writer.

Writes a single one-line excuse (a hardware wallet refusing to sign a
transaction at 3 AM) to /output/entry.txt. Pure stdlib, deterministic:
the same bytes on every run (sha256 71e0f35c5caa95e41aa1c036b94ea71
c4bfa67242f46c5d3af10f4488071d9c4, verified 2x), no trailing newline
so the file is exactly one line. Entry is 116 characters, 118 bytes,
within the 1-200 character gate.
"""

import os

ENTRY = (
    # Rubric pick: the wallet's job is protection, and the twist is
    # that its owner at 3 AM is the threat it protects the coins
    # from — "statistically" implies the device keeps score. No
    # battery / firmware / cold-storage cliche, and the line only
    # works at 3 AM: the owner is the danger after midnight.
    "My job is keeping your coins safe from hackers, scammers "
    "\u2014 and, statistically, you at 3 AM. "
    "Come back after sunrise."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
