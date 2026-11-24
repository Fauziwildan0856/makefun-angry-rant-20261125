"""Publish one short angry rant as entry.txt.

The program writes a single-line rant about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt, then reads it back to prove the file holds
exactly the rant. Only the Python standard library is used.
"""

import os
import sys

MAX_CHARS = 400

ENTRY = "The self-checkout has decided I am a thief. I scanned the milk. It watched me scan the milk. Now it is screaming 'unexpected item in the bagging area' at a bag that holds only the milk, while a member of staff watches me like a nature documentary. I did not steal the milk. I paid for the milk. The machine is the criminal here."


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print("entry must be 1 to %d characters" % MAX_CHARS, file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("entry OK:", len(ENTRY), "characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
