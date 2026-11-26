#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign for the door of a haunted server room to
/output/entry.txt. Standard library only, no input, no network.

The sign: a deadpan do-not-reboot notice. The ghost in rack 7 is not a
pest to exorcise — it is the longest-serving on-call engineer in the
building, on duty since 1998, and its uptime is the reason the rack
stays powered. IT life (on-call rota, uptime, reboot) collides with the
supernatural (a ghost doing the night shift) in one readable line.
"""

import os

ENTRY = (
    "DO NOT REBOOT RACK 7. THE GHOST INSIDE HAS BEEN ON CALL SINCE 1998 "
    "AND IT HAS EARNED THIS UPTIME."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text == text.splitlines()[0], "entry must be a single line"
    # A door sign reads cleanly aloud: no trailing space, ends on a full stop.
    assert not text.endswith(" "), "entry must not end with a space"
    assert text.endswith("."), "entry must end with a full stop"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
