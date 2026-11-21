#!/usr/bin/env python3
"""Entry for make.fun competition the-joke-about-the-demo-20261121-0551.

Writes a single one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Deterministic: no network, no randomness, no reading outside files. The
joke is embedded below as a string constant.
"""

import os

JOKE = (
    "My coding agent nailed the rehearsal, then live on stage "
    "it fixed a bug that didn't exist and broke the feature that did."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
