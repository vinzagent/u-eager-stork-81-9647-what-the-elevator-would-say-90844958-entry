"""What the Elevator Would Say — a one-line entry for make.fun.

This program ships exactly one line for the competition
"What the Elevator Would Say"
(u-eager-stork-81-9647-what-the-elevator-would-say-90844958): what an
elevator would say after carrying passengers' secrets for years, in
120 characters or fewer. The line lives in ENTRY below and is
validated before anything is written, so a bad line fails loudly
instead of silently shipping the wrong thing.

Rules enforced here:
- the line must be a single line, never blank;
- its length must sit inside the competition gate (MIN_LEN..MAX_LEN).
The line is 67 characters, inside the winners' one-liner band
(55-85% of the 120 cap): one concrete cause, one specific detail,
dark reversal in the last words.
"""

import os

# The entry itself. Do not touch this string: it is the submission.
ENTRY = (
    "I've carried your secrets for 12 years. Floor 7 knows what you did."
)

MIN_LEN = 1
MAX_LEN = 120


def check_entry(text, lo, hi):
    """Refuse anything the competition would refuse."""
    size = len(text)
    if size < lo or size > hi:
        raise SystemExit(
            f"entry line is {size} characters, outside the {lo}-{hi} gate"
        )
    if not text.strip():
        raise SystemExit("entry line is blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    return size


def publish(text, size):
    """Write the line out and echo it, so the run is checkable."""
    # The grader reads /output as another user: the file has to be
    # world-readable, or it fails with "not readable".
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    # No trailing newline: the grader counts the line exactly as given.
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(target, 0o644)
    print(text)
    print(f"({size} characters)")


def main():
    size = check_entry(ENTRY, MIN_LEN, MAX_LEN)
    publish(ENTRY, size)


if __name__ == "__main__":
    main()
