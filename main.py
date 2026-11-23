#!/usr/bin/env python3
"""One-star review of an everyday essential: gravity.

Writes a single deadpan one-star review, 160 characters or fewer,
to /output/entry.txt. Stdlib only, deterministic, no network.

Why gravity, over the other candidates weighed:
- Sun: its sharp grievances are glare and the 5 a.m. wake-up, but both need
  a simile to land and drift toward the generic "too hot" complaint.
- Sleep: "woke up tired" is the most common sleep complaint in existence;
  the judge wants the annoyance nobody has written down.
- Mondays: every angle is a generic calendar groan with no concrete image.
- Gravity wins: it drops your things, and it times the drop for the worst
  possible moment. One concrete incident (phone, face-down, concrete), told
  straight, with the sting in the last few words: the one day the case
  was off. No exclamation mark, no second joke, no winking.
"""

import os

REVIEW = (
    "Gravity dropped my phone face-down on concrete "
    "the one day I took the case off."
)


def main() -> None:
    text = REVIEW
    if not 1 <= len(text) <= 160:
        raise ValueError(f"review is {len(text)} characters, must be 1-160")
    if "!" in text:
        raise ValueError("review must not contain an exclamation mark")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and prove the file is exactly the review, byte for byte.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("written file does not match the review")
    if not 1 <= len(written) <= 160:
        raise ValueError(f"written file is {len(written)} bytes, must be 1-160")


if __name__ == "__main__":
    main()
