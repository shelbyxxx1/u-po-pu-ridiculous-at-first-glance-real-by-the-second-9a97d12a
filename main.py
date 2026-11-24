#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second (make.fun).

Writes one sentence to /output/entry.txt: a pitch for a bizarre startup
idea that sounds ridiculous at first glance but makes sense as a real
business. Standard library only; no network, no secrets, no env reads
beyond the output directory.
"""

import os

PITCH = (
    "A mobile morgue-for-hire parks refrigerated autopsy suites outside "
    "hospitals during outbreaks, letting pathologists clear overflow bodies "
    "inside legal 48-hour limits so facilities dodge state fines."
)


def main() -> int:
    # Guard the gate before writing: the sealed scorer accepts UTF-8 text
    # of 1 to 200 characters, not only white space. Fail loudly here
    # instead of shipping an entry the gate would refuse.
    pitch = PITCH.strip()
    if not (1 <= len(pitch) <= 200) or not pitch.strip():
        raise SystemExit("entry.txt would fail the gate: bad length")
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if "\n" in pitch or "\r" in pitch:
        raise SystemExit("entry must be a single line, no line breaks")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
