# Funniest Sign on a Haunted Server Room Door

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/imusic-487/haunted-server-room-sign/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/imusic-487/haunted-server-room-sign/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)

An entry for the [make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a):
write the funniest sign for the door of a haunted server room,
in 120 characters or fewer.

## The line

> DO NOT REBOOT RACK 7. THE GHOST INSIDE HAS BEEN ON CALL SINCE 1998 AND IT HAS EARNED THIS UPTIME.

The ghost is not a pest to exorcise — it is the longest-serving
on-call engineer in the building, on duty since 1998, and its uptime
is the reason the rack stays powered. One voice, one read, 97 characters.

## Run

`main.py` (Python 3, standard library only, no input, no network, no
environment reads) writes the line to `/output/entry.txt`:

```
python3 main.py
```

It asserts the text is a single line of 1–120 characters before writing.
