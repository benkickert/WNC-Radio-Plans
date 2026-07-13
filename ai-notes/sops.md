# SOPs — Standard Operating Procedures

> **Last updated:** 2026-06-29
> Step-by-step procedures for common tasks in this folder. Read
> [`file-format.md`](file-format.md), [`conventions.md`](conventions.md), and
> [`radios.md`](radios.md) first.

## SOP 0 — Before any edit

1. Identify which file and which **profile** you're working in (A = 21-col full,
   B = 14-col lean). Don't mix profiles within a file.
2. **Respect the provenance chain** (`References/` → `CHIRP Lists/` →
   `Complete Radio Plans/`; see [`conventions.md`](conventions.md)). Editing a
   **CHIRP List** → every channel must trace to a `References/` source (capture the
   source there if it's missing). Editing a **Complete Radio Plan** → only pull rows
   from CHIRP Lists; never hand-enter a channel.
3. **Build to the plan's standard design — do NOT pre-filter content to the radio it's
   going to.** Radio-specific trimming is the owner's call, requested one-off (see
   [`radios.md`](radios.md) "Radio capabilities"). E.g. don't drop ham from a list
   because a radio is GMRS-TX-only (it can still RX ham), or drop airband because a
   radio can't hear it.
4. Preserve the header row and the `Location` block scheme.
5. If anything is ambiguous, log it in [`open-questions.md`](open-questions.md)
   instead of guessing.

---

## SOP 1 — Add a channel to an existing codeplug

1. Pick a `Location` slot **inside the correct block** (see `conventions.md`); use
   the next free number in that block, or the reserved gap above the next block.
2. Fill columns to match the file's profile. For a repeater you need, at minimum:
   `Frequency` (output), `Duplex` (+/-), `Offset`, `Tone` mode + the matching
   `rToneFreq`/`cToneFreq`/`DtcsCode`, `Mode`.
3. Keep `Name` ≤ 8 chars, matching any existing abbreviation for that site.
4. Leave inert placeholders (`88.5`, `023`, `NN`, `Tone->Tone`) where a field
   doesn't apply.
5. Set `Skip`/`Power`/`TStep` per `conventions.md` (Profile A only).

---

## SOP 2 — Pull repeaters from the big pool into a new codeplug

Source: `CHIRP Lists/GA-IL-IN-KY-NC-OH-SC-TN-VA.csv` (Profile B). Goal: a focused,
loadable codeplug (usually Profile A) **written to `Complete Radio Plans/`**. A file only
graduates from `CHIRP Lists/` to `Complete Radio Plans/` once it passes SOP 4.

1. **Filter** the pool to what you want — by `STATE` in the comment, by `SCORE`
   threshold (higher = better/more desirable), and/or by region along a route.
2. **De-duplicate** against the destination file (same `Frequency` + `Tone` =
   likely the same repeater; watch for sites already in the baseline).
3. **Convert Profile B → Profile A** if the destination is Profile A:
   - Add the missing columns: `TStep` (`5.00`), `Skip` (blank for repeaters),
     `Power` (e.g. `10W` or the radio's level), and the four empty D-STAR columns
     (`URCALL,RPT1CALL,RPT2CALL,DVCODE`).
   - Zero-pad DTCS codes (`23` → `023`).
   - Decide what to do with the `Comment` metadata (keep, simplify, or drop —
     don't silently corrupt it).
4. **Renumber** `Location` into the destination's block scheme — repeaters from
   this pool are ham, so they go in **slots ≥ 100** (see `conventions.md`).
5. **Stay under the 200-channel cap.** The pool has 858 rows; trim to what fits the
   ham side (~slots 100–200) — typically by score threshold and/or route/region.
6. **Sanity-check** offsets/tones against the band plan (see SOP 4).

---

## SOP 3 — Build a trip / route-specific codeplug (owner standard)

> **Updated 2026-06-26 — trip plans are now `local baseline.csv` + route, appended.**
> The earlier "assemble from scratch" recipe is replaced by the baseline model below.

**A trip plan = the full `local baseline.csv` as the baseline, then the route and
destination repeaters appended after it.** This guarantees the home/local set is always
present (if there's no time to reflash after the trip, the radio still has everything
local), and covers the whole route end-to-end. Follows the ≤ 99 GMRS / ≥ 100 ham split.

**Why the baseline:** it's local-only, so there's room for the route repeaters under
the 200-channel cap while still keeping the full home set on the radio.

**Steps:**
1. **Start from `local baseline.csv`** (91 ch) verbatim — slots 1–48 (GMRS simplex,
   generic travel-tone GMRS, local WNC GMRS), 81–85 MURS, 91–97 WX, 100/101 calls,
   102–109 ham simplex, 110–130 local WNC ham. Don't re-pick home repeaters; the
   baseline's full local blocks already cover departure/return.
2. **Append route GMRS** starting at **slot 50** (a 1-slot gap after the local GMRS
   block, which ends at 48; stay before MURS at 81). Curate from `CHIRP Lists/GMRS
   …csv` (open/on-air only), **ordered in the sequence you drive past them.**
3. **Append route ham** starting at **slot 150** (a gap after the local ham block,
   which ends at 130). Select by **quality** (score, wide-area, linked), a **mix of
   2 m and 70 cm**, then **order by drive sequence.** (Selection = quality; ordering =
   geography.) Pull via SOP 2 from `CHIRP Lists/GA-IL-…VA.csv`.
4. **Name** the file `<FROM> to <TO>.csv` in `Complete Radio Plans/`.

**Selection principle (both route blocks):** maximize coverage across the route —
no fixed count. Include the **active, higher-power, wide-area / linked** repeaters;
**drop poor-quality repeaters only where a better overlapping one already covers that
area.** Include **whole linked systems** (hitting one node reaches them all — e.g. the
Knoxville WRJZ925 GMRS system spans Knoxville/Oak Ridge/Pigeon Forge, include all
three). The generic travel-tone block lives in the baseline and is always present and
scanned — **keep route repeaters even when their freq+tone duplicates it** (the owner
wants the duplication; never trim for tone-uniqueness).

**De-dupe against the baseline:** don't re-add a home repeater that's already in the
baseline's local blocks. (The route blocks are only the *non-local* repeaters.)

**Scan policy:** **scan = every repeater + the two calling freqs (100/101); skip
everything else** (all GMRS *and* ham simplex, MURS, WX). The baseline already follows
this, so appended route repeaters just get `Skip` blank. Keep duplicate repeaters both
in scan.

---

## SOP 6 — Build a supplement plan (slots 201+, high-memory radios)

> Added 2026-07-13. A **supplement** is extra content loaded **on top of** a universal
> ≤ 200 plan, using the empty memories above 200 on the **UV-5R Mini / UV-5G Plus**
> (999 ch). It is **not** a standalone codeplug and **won't fit the TD-H9/TD-H8**
> (200 ch) or the AR-5 (16 ch). See [`conventions.md`](conventions.md).

Use it when content is genuinely *additive* — monitoring/scanner sets, destination
blocks, seasonal channels — and you don't want to spend base-plan slots on it.

1. **Decide the base plan it rides on.** A supplement must not collide with the base's
   1–200. (Since every base plan is ≤ 200, any supplement starting at 201 is safe with
   *all* of them — that's the point of the rule.)
2. **Pull rows from `CHIRP Lists/` only** (the provenance rule applies exactly as for a
   universal plan — never hand-enter a channel).
3. **Renumber into thematic blocks from 201 up, leaving gaps** for growth. The
   slot-100 ham/GMRS split does **not** apply up here — organize by purpose instead.
4. **Keep house values:** Profile A columns, `Name` ≤ 8 chars, `10W`/`2.0W`/`6.0W`
   power, `rToneFreq == cToneFreq` on TSQL. CHIRP clamps per-radio at import.
5. **Set `Skip` for the supplement's own purpose** — a monitoring/scan supplement is
   all-scan; a destination supplement follows the trip-plan policy.
6. **RX-only content stays RX-only:** `Duplex=off` on public-safety, airband, and
   weather channels. Never leave a transmit path on a channel you're not licensed for.
7. **Name it `<Purpose> (201+).csv`** and validate per SOP 4, substituting "no slot
   below 201" for the ≤ 200 / slot-100 checks.
8. **Load order in CHIRP:** import the base plan, then import the supplement into the
   same image, then write to the radio.

---

## SOP 4 — Validate before handing off / importing

Check, at minimum:

- **Provenance** (the core standard): in a CHIRP List, every channel traces to a
  `References/` source; in a Complete Radio Plan, every channel was pulled from a
  CHIRP List. No unsourced or hand-entered channels. See [`conventions.md`](conventions.md).
- **Header row present** and matches the file's profile column set.
- **≤ 200 channels total** (LCD cap) and **`Name` ≤ 8 chars** — the two hard rules.
- **`Location` values unique**, within the block scheme, and on the correct side of
  the **slot-100 boundary** (ham ≥ 100; GMRS/MURS/listen-only ≤ 99).
- **No stray commas** in any field (CSV breakage).
- **Frequency sanity:** in a valid band for the service
  - GMRS 462/467 MHz; MURS 151/154 MHz; NOAA WX 162.400–162.550;
  - 2 m ham 144–148; 70 cm ham 420–450.
- **Offset/Duplex match the band convention** (2 m → ±0.6; 70 cm/GMRS-rpt → +5).
  For ham repeaters, cross-check input/output against the **SERA band plans** in
  `References/SERA/` (e.g. `sera-fup-144.pdf` for 2 m, `sera-fup-440.pdf` for 70 cm).
- **Tone fields consistent** with the `Tone` mode (e.g. `TSQL` needs a real
  `cToneFreq`; `Cross` needs a `CrossMode`).
- **Mode** = `NFM` where narrowband is required (GMRS 8–14, MURS 1–3).
- **Power/levels** valid for the target radio (see `radios.md`).

Then in CHIRP: pick the correct radio model, import the CSV, eyeball the memory
grid, and write to radio.

---

## SOP 5 — Keep these notes accurate

After any structural change (new file, new block, new convention, format tweak):
- Update [`inventory.md`](inventory.md) (files/rows/contents),
  [`conventions.md`](conventions.md) (scheme/naming), and/or
  [`file-format.md`](file-format.md) (columns).
- Bump the "Last updated" date in the files you touched.
- Resolve or add entries in [`open-questions.md`](open-questions.md).
