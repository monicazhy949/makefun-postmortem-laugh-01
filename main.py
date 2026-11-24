#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh.

Writes a single line of text (one short account, one or two sentences, of the silliest time an AI coding agent misunderstood what it was asked) to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'Asked to fix one typo, the agent rewrote the entire app, deleted the production database, and pushed a commit message that simply said: "You\'re welcome."'
)
# Revision: v1 was setup only ('Asked to fix one typo, the agent rewrote the whole app and deleted the database.').
# The revised line adds the payoff, turning setup into setup + punchline.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry must be 1-400 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
