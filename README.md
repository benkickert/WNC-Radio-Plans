# CHIRP CSVs — WNC Radio Codeplugs

Working repository for building [CHIRP](https://chirpmyradio.com/) codeplugs (radio
channel-memory files) as CSVs — GMRS, MURS, NOAA weather, and amateur (ham) 2 m / 70 cm.
Centered on **Western North Carolina (Fairview / Asheville)**, with a multi-state pool
for travel. The CSV is the source of truth; the radio is downstream.

## Folder layout

```
Complete Radio Plans/  finished codeplugs to flash whole (≤200 ch, ≤8-char names, slotted)
CHIRP Lists/           building-block lists you pull from (raw pools AND clean blocks)
References/            source-of-record behind every list (band plans, club/agency lists, exports)
ai-notes/              maintenance documentation — how the repo works
IMG Files/             full CHIRP .img radio images built from the plans (outputs, not sources)
```

## Start here

**Read [`ai-notes/README.md`](ai-notes/README.md) first.** It orients any human (or AI)
working in this folder and links the rest of the docs:

| To… | See |
|-----|-----|
| Understand the CHIRP CSV format & columns | [`ai-notes/file-format.md`](ai-notes/file-format.md) |
| Know what each CSV contains | [`ai-notes/inventory.md`](ai-notes/inventory.md) |
| Follow the naming / slot conventions | [`ai-notes/conventions.md`](ai-notes/conventions.md) |
| Know the radios & which CSV suits which | [`ai-notes/radios.md`](ai-notes/radios.md) |
| Build or edit a CSV (step-by-step) | [`ai-notes/sops.md`](ai-notes/sops.md) |
| See unresolved questions / queued work | [`ai-notes/open-questions.md`](ai-notes/open-questions.md), [`ai-notes/todo.md`](ai-notes/todo.md) |

## Core rules

- **Two hard LCD limits:** channel `Name` ≤ 8 chars, ≤ 200 channels per codeplug.
- **Slot split at 100:** GMRS / MURS / listen-only on slots 1–99, amateur on 100+.
- **Provenance chain:** `References/` → `CHIRP Lists/` → `Complete Radio Plans/`. Every
  list channel traces to a reference; every plan is assembled only by pulling from lists.
- **Tone standard:** `TSQL` (`rTone==cTone`) when a repeater broadcasts its tone; `Tone`
  (encode-only) when it doesn't, so a receive tone never mutes a repeater you want to hear.
