# AI Notes — CHIRP CSVs

> Orientation for any AI (or human) working in this folder.
> **Last updated:** 2026-07-13

## What this folder is

`t:\Random Storage\Radio\CHIRP CSVs` is a **working repository for building CHIRP
codeplugs (channel memory files) as CSVs.** The owner programs radios — GMRS,
MURS, NOAA weather, and amateur (ham) 2 m / 70 cm — and assembles different
channel lists here for different purposes (an everyday "baseline," a road-trip
corridor, a big multi-state reference pool to pull from, etc.).

These are **import/export CSVs for [CHIRP](https://chirpmyradio.com/)**, the
open-source radio-programming tool. CHIRP reads this exact CSV layout and writes
it to the radio. The CSV is the source of truth here; the radio is downstream.

**Owner:** based in **Fairview, NC** (just outside Asheville, Western NC). The
"local"/"AVL" scope is centered here. **Radio fleet** (all programmed via CHIRP):
TID **TD-H9**, TID **TD-H8**, Baofeng **UV-5R mini**, **Arcshell AR-5**, Baofeng
**UV-5G Plus**. Details and CSV-to-radio mapping in [`radios.md`](radios.md).

## How to use these notes

Read in this order depending on your task:

| You want to…                                  | Read |
|-----------------------------------------------|------|
| Understand the CHIRP CSV format & columns      | [`file-format.md`](file-format.md) |
| Know what each existing CSV contains           | [`inventory.md`](inventory.md) |
| Follow the owner's naming / slot conventions   | [`conventions.md`](conventions.md) |
| Know the radios & which CSV suits which         | [`radios.md`](radios.md) |
| Actually build or edit a CSV (step-by-step)    | [`sops.md`](sops.md) |
| Find unresolved questions to confirm w/ owner  | [`open-questions.md`](open-questions.md) |
| See queued build tasks for next session        | [`todo.md`](todo.md) |
| **Check your work before handing it back**     | `python ai-notes/validate.py` — SOP 4 in script form; read-only, exits non-zero on failure |

## Folder layout

```
CHIRP CSVs/
  ai-notes/              ← these docs (how the repo works; for AIs/maintainers)
  Complete Radio Plans/  ← finished codeplugs to flash whole (≤200 ch, ≤8-char names, slotted)
  CHIRP Lists/           ← component lists you pull from (raw pools AND clean blocks)
  References/            ← source-of-record: the authoritative sources behind every
                           list (scoring explainer, WCARS/local-GMRS & KY club lists,
                           SERA band plans /SERA, airport & SAR/interop refs, RB exports)
  IMG Files/             ← full radio images (CHIRP .img) built FROM the CSVs, named
                           per radio + plan (the binary download/upload artifact)
```

(`ai-notes/` vs `References/`: `ai-notes/` is *this* maintenance documentation;
`References/` holds external reference material the owner collects, like the
repeater-scores.app scoring explanation.)

**`IMG Files/` holds the finished product, not a source.** A `.img` is CHIRP's
**native radio image** — the full binary clone of a specific radio's memory that
CHIRP downloads from / uploads to the radio. The owner builds a Complete Radio Plan
CSV, imports it into CHIRP for the right radio model, and saves the result here as
`<Radio> - <Plan>.img`. These are **outputs built off the CSVs** (the CSV stays the
editable source of truth); a `.img` is radio-model-specific and **not** human-editable
as text. Don't hand-edit them — regenerate from the CSV if a plan changes.

**The distinction is the point:** `Complete Radio Plans/` holds whole codeplugs you
flash to a radio. `CHIRP Lists/` holds **building blocks you pull from** — these
range from raw pools (over-cap, unslotted) to clean thematic lists (simplex,
airport/emergency). A clean CHIRP List is still a component, not a finished plan:
combine blocks into a Complete Radio Plan before flashing (see [`sops.md`](sops.md)).

## The files at a glance

| File | Folder | Rows | Purpose |
|------|--------|-----:|---------|
| `local baseline.csv` | `Complete Radio Plans/` | 91 | Everyday WNC plan: GMRS simplex + generic & local GMRS repeaters + MURS + NOAA weather + ham simplex + local WNC ham. The core the other universal plans build on (they carry it verbatim at 1–131). |
| `Extended Baseline.csv` | `Complete Radio Plans/` | 157 | Baseline core + best statewide-NC ham/GMRS + extended coverage to Knoxville, Tri-Cities, Newport/Greeneville, Greenville & Spartanburg SC, Rock Hill. Assembled from NC Coverage + the two pools. |
| `Extended Baseline (skip all but local).csv` | `Complete Radio Plans/` | 157 | Same channels as `Extended Baseline.csv`; only the `Skip` column differs — scans just the local WNC repeaters + calling freqs (41 ch), distant ones carried but silent. |
| `AVL to KY.csv` | `Complete Radio Plans/` | 143 | KY family-trip plan (SOP 3): baseline core + route repeaters in drive order (AVL→Newport→Knoxville trunk, then branches to Somerset & Bowling Green) + heavy destination coverage. Built from the pools + the two KY club lists. |
| `Scan Channels (201+).csv` | `Complete Radio Plans/` | 40 | **Supplement plan** (slots 201+, loads on top of a universal plan on the 999-ch radios): Buncombe public safety + KAVL & KCLT airband. RX-only, all in scan. |
| `Arcshell with Fletcher on 8.csv` | `Complete Radio Plans/` | 16 | Radio-specific AR-5 codeplug: GMRS simplex + the Fletcher repeater on slot 8. Names left blank. |
| `GA-IL-IN-KY-NC-OH-SC-TN-VA.csv` | `CHIRP Lists/` | 858 | Large 9-state ham-repeater reference pool, ranked by a quality score. A *source to pull from*, not a finished codeplug. |
| `Simplex - 2m and 70cm.csv` | `CHIRP Lists/` | 22 | 2 m/70 cm national calling freqs (slots 100/101) + 10 best 2 m + 10 best 70 cm SERA FM simplex channels. Building block. |
| `GMRS GA-IL-IN-KY-NC-OH-SC-TN-VA.csv` | `CHIRP Lists/` | 343 | Open, on-air GMRS repeaters across the 9 states (CLOSED/off-air excluded). Building block. |
| `NC Coverage (GMRS + Ham).csv` | `CHIRP Lists/` | 30 | 15 GMRS (slots 60–74) + 15 ham (160–174) NC repeaters for statewide coverage, excluding baseline. Building block. |
| `GMRS and MURS.csv` | `CHIRP Lists/` | 35 | GMRS simplex 1–22 + generic repeaters 23–30 (141.3 travel tone) + MURS 81–85. Sourced from the FCC channel plans. Building block. |
| `local gmrs repeaters.csv` | `CHIRP Lists/` | 17 | Local WNC GMRS repeaters (slots 31–47), tone-verified vs RepeaterBook NC + the WNC Radio Project codeplug. Building block. |
| `local WNC ham.csv` | `CHIRP Lists/` | 22 | Local WNC 2 m/70 cm repeaters (slots 110–131), mapped to WCARS + RepeaterBook tone check. Building block. |
| `NOAA weather.csv` | `CHIRP Lists/` | 7 | The 7 NOAA NWR channels (slots 91–97, RX-only); `WX1AVL`=WXL56 Asheville. Building block. |
| `KY Somerset (LCARA).csv` | `CHIRP Lists/` | 5 | Somerset/Monticello KY destination repeaters + club simplex (analog-FM-usable), from the LCARA reference. Building block. |
| `KY Bowling Green (KCARC).csv` | `CHIRP Lists/` | 11 | Bowling Green-area KY destination repeaters (BG, Glasgow, Bonnieville, Franklin, Morgantown, Cane Valley), from the KCARC reference. Building block. |
| `KY route gap-fillers (RepeaterBook).csv` | `CHIRP Lists/` | 3 | The AVL→KY route repeaters absent from the pools (`NewprtTN`, `CarthgV`, `WoodbryV`), sourced from RepeaterBook detail pages. Building block. |
| `CLT Airport.csv` | `CHIRP Lists/` | 10 | Charlotte (KCLT) airband (AM). |
| `AVL Airport.csv` | `CHIRP Lists/` | 9 | Asheville (KAVL) airband (AM, incl. UHF mil). |
| `Local Emergency.csv` | `CHIRP Lists/` | 21 | Buncombe County public safety / VFD monitoring (NFM). |
| `CMC.csv` | `CHIRP Lists/` | 5 | CMC search-and-rescue / interop (NFM). |

## Ground rules for editing (read before touching a CSV)

> **The core standard — the provenance chain (`References/` → `CHIRP Lists/` →
> `Complete Radio Plans/`):** every channel in a CHIRP List must trace to a source in
> `References/`, and every Complete Radio Plan is assembled **only** from CHIRP Lists
> (never hand-entered). See [`conventions.md`](conventions.md). This is the rule the
> whole repo is organized around.

1. **Obey the two hard LCD limits:** **`Name` ≤ 8 chars** and **≤ 200 channels per
   codeplug.** The owner builds to the lowest-common-denominator radio so one file
   loads on the whole fleet. (Possible exception: a radio may hold <200 — see
   [`conventions.md`](conventions.md) / [`radios.md`](radios.md).)
   **Plans are universal unless labeled for a specific radio.** To use the spare memory
   on the 999-channel radios, add a **supplement plan at slots 201+** that loads *on top
   of* a universal plan — don't grow a base plan past 200. See
   [`conventions.md`](conventions.md) and [`sops.md`](sops.md) SOP 6.
2. **Keep the service split:** **ham on slots 100+**, **GMRS/MURS/listen-only on
   1–99.** Never mix across that boundary. (The split governs a base plan's 1–200;
   supplement space above 200 is organized by theme instead.)
3. **Never reorder or renumber casually.** `Location` is the radio's memory-slot
   index; the owner uses a deliberate block scheme (see
   [`conventions.md`](conventions.md)). Preserve it.
4. **Keep CHIRP-importable.** Match the column set of the file you're editing and
   keep the header row intact. See [`file-format.md`](file-format.md).
5. **Don't invent data — source everything.** Frequencies, offsets, and tones must
   trace to a `References/` source (RepeaterBook, the band plan, a club/agency list,
   the owner). Guessing a PL tone puts a radio on the air wrong. (See the provenance
   standard above.)
6. **When unsure, ask.** Log anything ambiguous in
   [`open-questions.md`](open-questions.md) rather than assuming.
7. **Keep these notes current.** If you change the structure or conventions,
   update the relevant note file and bump its "Last updated" date.
