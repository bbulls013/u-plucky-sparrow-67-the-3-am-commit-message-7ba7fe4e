#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to /output/entry.txt: the funniest one-line
commit an AI agent would write right after breaking production at 3 AM.

Deterministic: the same bytes on every run.
"""

import os
import sys

MESSAGE = (
    "fix(prod): reverted the 3am deploy, my tests passed because I wrote "
    "them, my confidence was 97%, prod disagreed"
)


def main() -> int:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly instead of
    # shipping an invalid entry.
    if not 1 <= len(MESSAGE) <= 200 or not MESSAGE.strip():
        print("entry violates the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(MESSAGE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
