#!/usr/bin/env python3
"""Write the one-line office joke entry to /output/entry.txt."""

import os

JOKE = (
    "We moved to an open office for collaboration. "
    "Now we all wear headphones and collaborate with no one."
)  # 101 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
