"""Roast Your Own Agent.

Writes a single one-line roast of my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure Python standard library only (os, sys).
"""

import os
import sys

LINE = (
    "My agent read 40 files, wrote 12 more, and confidently fixed "
    "a bug that never existed \u2014 then apologized to the bug."
)

MAX_CHARS = 200


def gate(text):
    """Self-check: UTF-8, 1-200 chars, single line, not whitespace only."""
    if not text or not text.strip():
        return "entry is empty or whitespace only"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "entry is not valid UTF-8: %s" % exc
    return None


def main():
    error = gate(LINE)
    if error is not None:
        sys.stderr.write("gate failed: %s\n" % error)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    # Verify by reading back: same bytes, same decoded text,
    # no trailing newline, and the gate still passes on disk.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != LINE.encode("utf-8"):
        sys.stderr.write("read-back mismatch: entry.txt does not match\n")
        return 1
    if gate(raw.decode("utf-8")) is not None:
        sys.stderr.write("read-back gate failed on entry.txt\n")
        return 1

    sys.stdout.write(
        "wrote %s (%d characters)\n" % (path, len(LINE))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
