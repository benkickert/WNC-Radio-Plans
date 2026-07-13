# Conventions

> **Last updated:** 2026-07-13
> The owner's house style. Follow these so new files match the existing ones.
> (Inferred from the current files — confirm with the owner where noted.)

## Folder taxonomy (where a file lives = what it is)

- **`Complete Radio Plans/`** — **finished codeplugs** meant to be loaded onto a
  radio as a whole. A file belongs here only once it's a complete plan meeting every
  LCD rule below (≤200 channels, ≤8-char names, correct slot split, valid band/tone
  data). These are the files you actually flash.
- **`CHIRP Lists/`** — **component lists you pull from** to assemble complete plans;
  not complete plans themselves. These range from raw source pools (e.g. the
  multi-state repeater database — over the cap, unslotted) to clean, well-formed
  thematic blocks (e.g. the simplex list, the airport/emergency monitoring sets).
  Even a clean CHIRP List is a *building block*, not a finished codeplug — combine
  it with others into a Complete Radio Plan. Distinguish the two by **role**
  (component vs whole plan), not just by readiness.
- **`References/`** — the **source-of-record**: the authoritative source material
  behind every CHIRP List (band plans, club/agency lists, the scoring/badge decoder,
  the airport & SAR/interop frequency references, etc.). When you build or verify a
  list, the source goes here. Not CSVs loaded on a radio.
- **`ai-notes/`** — this maintenance documentation; covers the whole repo, stays at
  the root. (Distinct from `References/`: ai-notes explains *the repo*; References
  holds *external* material the owner collects.)
- **`IMG Files/`** — **finished radio images** (CHIRP `.img`) built *from* the
  Complete Radio Plan CSVs: the owner imports a plan CSV into CHIRP under a radio
  model and saves the resulting radio image here. These are **outputs**, not editable
  sources — the CSV stays the source of truth; regenerate the `.img` if the plan
  changes. Model-specific binary, so a `.img` is **not** cross-radio like an LCD CSV.

`Complete Radio Plans/` holds two kinds of codeplug: **universal/LCD** files meant to load on
the whole fleet, and **radio-specific** files tuned to one radio's quirks (e.g.
`Arcshell with Fletcher on 8.csv` — blank names, 5 W, GMRS-only). A radio-specific
file may deviate from the universal conventions where that radio requires it; note
the deviation in [`inventory.md`](inventory.md).

When you create a new file, decide its folder by readiness, not by topic. A
work-in-progress that isn't yet normalized stays in `CHIRP Lists/` (or a clearly
named draft) until it passes the SOP 4 validation checklist.

## Provenance / sourcing standard (the core rule)

Data flows in **one direction**, and every channel is traceable back to a source:

```
References/  ──>  CHIRP Lists/  ──>  Complete Radio Plans/
(authoritative    (every channel       (assembled ONLY from
 source material)  traces to a          CHIRP Lists — no channel
                   References entry)     introduced at plan level)
```

1. **Every channel in a CHIRP List must be verifiable against a document in
   `References/`.** If the source isn't captured there yet, add it — a new
   `References/` doc is fine (see the airport and SAR/interop references). No
   unsourced channels in `CHIRP Lists/`.
2. **A Complete Radio Plan is assembled only by pulling rows from `CHIRP Lists/`** —
   never by hand-entering a channel straight into a plan. If a plan needs something
   no list has yet, **make or extend a CHIRP List first** (sourced per rule 1), then
   pull from it.
3. **When sources disagree,** resolve to the most authoritative one and record the
   resolution in the relevant `References/` doc, so the contradiction stays settled.
   **Source-priority rule (owner-set):** for coordinated / band-plan channels (SERA
   repeater pairs; NIFOG SAR & interop channels), the **band-plan standard outranks an
   agency or club document** — e.g. where a CMC/SAR sheet disagrees with NIFOG, use the
   NIFOG frequency/tone and note the override. The band plan is the higher authority.

This keeps the chain auditable end to end: a plan → its CHIRP Lists → their
References. Maintaining that chain is the whole point of the folder split.

## Hard constraints — "lowest common denominator" (LCD)

The owner standardizes codeplugs to load across the fleet. Two firm rules:

1. **`Name` ≤ 8 characters.** Always.
2. **≤ 200 channels per codeplug.** Total rows (excluding the header) must not
   exceed 200. **Basis:** the TID radios (TD-H9 / TD-H8) hold exactly 200; the
   UV-5R mini and UV-5G Plus hold 999, but the owner keeps every multi-radio plan to
   ≤ 200 for consistency. See [`radios.md`](radios.md). *(The way to use the extra
   memory on the 999-channel radios is a **supplement plan at slots 201+** — an add-on
   loaded on top of a universal plan, never an over-200 base plan. See below.)*

**Exception — Arcshell AR-5:** it holds only **16** channels and is a special case
with its own tiny dedicated codeplug; the ≤ 200 rule doesn't apply to it.

Any multi-radio file intended to load on a radio must satisfy both rules. (The big
state pool does **not** yet — it's raw source, see [`inventory.md`](inventory.md).)

## The three kinds of Complete Radio Plan

Everything in `Complete Radio Plans/` is one of these. **Default to universal.**

1. **Universal (LCD) plan — the default.** Loads on the whole fleet: ≤ 200 channels,
   ≤ 8-char names, `Name`/slot/tone rules all obeyed. Unless a plan is explicitly
   labeled otherwise, it is universal. (`local baseline`, `Extended Baseline`,
   `AVL to KY`, and the quiet-scan variant.)
2. **Radio-specific plan.** Tuned to one radio's quirks and named for it (e.g.
   `Arcshell with Fletcher on 8.csv` — blank names, 5 W, GMRS-only, 16 ch). May break
   the universal conventions where that radio demands it; note the deviation in
   [`inventory.md`](inventory.md).
3. **Supplement plan (slots 201+) — for high-memory radios.** See below.

## Supplement plans — adding channels above slot 200

The ≤ 200 cap exists for the **TID radios** (TD-H9 / TD-H8 hold exactly 200). The
**UV-5R Mini and UV-5G Plus hold 999**, so on those radios there is room to carry
*extra* channels **on top of** a universal plan without compromising it. That's what a
**supplement plan** is: a Complete Radio Plan whose slots **start at 201**, designed to
be loaded **in addition to** a ≤ 200 universal plan, not instead of it.

**Rules for a supplement:**
- **Slots start at 201** and never overlap a base plan's 1–200. This is what keeps the
  two loadable together — CHIRP merges by `Location`, so a supplement simply fills the
  empty memories above the base plan.
- **The universal plan stays untouched.** Never renumber or trim a base plan to make
  room; the whole point is that the base is unchanged and still flashes to the TIDs.
- **The slot-100 service split does not extend above 200.** That split governs the
  1–199 / 100+ layout of a base plan. Above 200 you're in supplement space — organize
  it in **thematic blocks with gaps**, the same way the base plan blocks its ranges.
- **Everything else still applies:** `Name` ≤ 8 chars, house `Power`/tone values,
  Profile A columns, and the **provenance rule** (assemble only by pulling rows from
  `CHIRP Lists/`).
- **Name the file with its slot range** — `<Purpose> (201+).csv` — so it's obvious at a
  glance that it's an add-on, not a whole codeplug.
- **Know which radios can take it:** UV-5R Mini and UV-5G Plus (999 memories) only. The
  **TD-H9/TD-H8 cannot** — they stop at 200, so a supplement is silently useless there.
  The AR-5 (16 ch) certainly cannot. See [`radios.md`](radios.md).

**Loading:** in CHIRP, import the universal plan first, then import the supplement into
the same image; the supplement lands in memories 201+ and both write to the radio
together. Build one per [`sops.md`](sops.md) SOP 6.

## Memory-slot (`Location`) governing rule

**Split by service at slot 100:**

- **Slots 1–99 → GMRS / MURS / listen-only** (weather and any RX-only channels).
- **Slots 100–200 → amateur (ham) radio.**

So the usable layout is roughly **99 non-ham + 101 ham = ≤200 total.**

## Block scheme within that split

Slots are grouped by service, with **gaps left between blocks for expansion**.
Observed in `local baseline.csv`:

| Range | Reserved for |
|------:|--------------|
| 1–22   | GMRS simplex (matches the 22 GMRS channel numbers) |
| 23–48  | GMRS repeaters |
| 49–80  | *(free — expansion)* |
| 81–85  | MURS |
| 86–90  | *(free — expansion)* |
| 91–97  | NOAA weather (listen-only) |
| 98–99  | *(free)* |
| **100** | **— service boundary: ham starts here —** |
| 100–122 | Local ham (2 m / 70 cm) |
| 123–129 | *(free)* |
| 130–179 | Corridor / travel ham repeaters |
| 180–200 | *(free — ham expansion, up to the 200 cap)* |

**Rules:**
- Keep ham ≥ 100 and GMRS/MURS/listen-only ≤ 99 — don't mix across the boundary.
  *Exception:* a big **monitoring/scanner block** (e.g. Local Emergency / CMC) may sit
  in a high "monitoring" section (≈ 160–200) when 1–99 is full — a deliberate
  relaxation, to be flagged in that plan's [`inventory.md`](inventory.md) entry.
- Add new entries within the matching block; if a block fills, use the gap above
  the next block rather than renumbering everything.
- Watch the **200-channel ceiling** when adding — there are only ~101 ham slots. If a
  plan is full and the content is *extra* (monitoring, destination, seasonal), don't
  squeeze it in — put it in a **supplement plan at 201+** (above) for the high-memory
  radios instead of degrading the universal plan.

The block table above is the **baseline layout**. Other plan types keep
the same ≤99/≥100 split but arrange blocks differently. In particular, **trip plans
(SOP 3) = the full `local baseline.csv` + route repeaters appended after**, with a
small gap between baseline and trip blocks: route GMRS **starts at slot 50** (local
GMRS ends at 48; stays before MURS), and route ham **starts at slot 150** (local ham
ends at 130). See
[`sops.md`](sops.md) SOP 3 and each plan's [`inventory.md`](inventory.md) entry.

## `Name` conventions (≤ 8 chars)

Names are abbreviated to fit the radio display. Patterns seen:

- **`G` prefix** = GMRS repeater (`GAlexndr`, `GBearwal`, `GPisgahF`).
- **`V` suffix** = VHF / 2 m repeater (`BakersV`, `PisgahV`, `SpiveyV`).
- **`U` suffix** = UHF / 70 cm repeater (`BearU1`, `ClngmnU2`, `CoweeU`).
- **Numeric suffix** distinguishes multiple repeaters at one site (`BearV1`,
  `BearV2`, `BearV3`).
- **`LP`** = low-power channel (GMRS 8–14: `GMRS8LP`).
- **`R`** = repeater variant of a simplex channel (`GMRS15R`).
- **`WX`** = NOAA weather (`WX1AVL`).
- **`*`** marks the **national GMRS travel/calling channel** — it appears only on
  `GMRS20R*` because **462.675 + 141.3** is the widely-recognized GMRS travel
  frequency and tone.

Place/site names are truncated to 8 chars (`ClngmnV` = Clingmans, `Waynesv` =
Waynesville). Be consistent with an existing abbreviation if the site already
appears elsewhere.

## Tone / signaling defaults

- Toneless channels carry **placeholder** values `rToneFreq=88.5`, `cToneFreq=88.5`,
  `DtcsCode=023`, `DtcsPolarity=NN`, `CrossMode=Tone->Tone`. These are inert until
  `Tone` selects a mode. Leave them as-is; don't read meaning into them.
- **Repeater tone standard (owner preference):** when a repeater **broadcasts a tone on
  its output** (the common case), use **`TSQL`** with **`rToneFreq == cToneFreq ==` the
  real tone**. TSQL gates RX so squelch opens only for that repeater — essential on
  crowded/shared channels (especially the 8 GMRS repeater outputs) to tell *which*
  repeater you're hearing. (All-`Tone`/carrier-RX makes co-channel repeaters
  indistinguishable — the owner tried that and rejected it.) Use **`Tone`** (encode-only,
  carrier RX) ONLY for a repeater that needs an input tone but does **not** broadcast one
  on output (there, TSQL would mute it). Use **carrier** (no tone) for open repeaters.
  `local baseline.csv` follows this (set 2026-06-29): toned repeaters = TSQL, tone-less =
  carrier.
- **Always set `rToneFreq == cToneFreq` on a TSQL row** (and `DtcsCode == RxDtcsCode` on
  DTCS). The old split — `rToneFreq=88.5` with the real tone only in `cToneFreq` — is the
  bug that can make CHIRP write **88.5 as the TX tone** and fail to key the repeater.
  Never leave that placeholder on a toned row.
- **DTCS repeater:** use `DTCS` with `DtcsCode == RxDtcsCode` (decodes the code on RX, so
  it distinguishes like TSQL). `DTCS` imports everywhere — avoid `Cross` on the LCD
  baseline since simpler radios may not support it.

## Mode / power defaults

- `Mode`: `FM` except narrowband-required channels (`NFM` for GMRS 8–14 and MURS
  1–3).
- `TStep`: `5.00` everywhere (Profile A).
- `Power` (Profile A): `10W` ham/GMRS-high, `2.0W` GMRS low-power, `6.0W` weather.
- `Skip` (Profile A): `S` = skipped during scan; blank = included. General rule:
  repeaters are scanned, simplex/utility/weather are skipped — but the exact policy
  depends on the **plan type** (below).

## Plan types & scan (`Skip`) policy

Different plan archetypes have different scan rules. Set `Skip` per the plan's type:

- **Home / default plan** (e.g. `local baseline.csv`):
  scan = the **local** repeaters + the 2m/70cm calling freqs. Everything else is
  `Skip=S`: GMRS simplex, ham simplex, the **generic GMRS travel-tone block**
  (`GMRS15R`–`22R`), any non-local GMRS/ham, MURS, and WX. (Updated 2026-07-01: the
  generic GMRS block is skipped — it's a travel-tone convenience set, not an everyday-
  scan target. Only the *named local* repeaters and the calling freqs scan.)
- **Trip / route plan** (see [`sops.md`](sops.md) SOP 3): scan = **all repeaters**
  (the baseline's generic + local repeaters, plus the appended route GMRS + route ham)
  + the 2m/70cm calling freqs. All simplex (GMRS *and* ham), MURS, and WX are `Skip=S`.
  **Keep duplicate repeaters both in scan.**
- **Radio-specific plan** (e.g. the AR-5 file): per that radio's use.
- **Quiet-scan variant of a regional plan** (e.g. `Extended Baseline (skip all but
  local).csv`): **same channels, home scan.** Carry the full regional set in the radio
  but scan only the *immediate-area* repeaters + the calling freqs — i.e. the home
  plan's scan policy applied to a bigger channel list. Everything distant is `Skip=S`
  and switched into scan **at the radio** when the owner actually travels. Name it
  `<Parent Plan> (skip all but local).csv` and keep its channel content identical to
  the parent — **only `Skip` may differ.**

Constant across types: the **2m & 70cm national calling freqs are always in scan**;
**MURS and WX are never in scan**.

## Round-tripping through CHIRP / a radio (don't bake radio values into a CSV)

Exporting a CSV **from CHIRP after it has been loaded into a radio** rewrites values to
that radio's conventions. Observed on a UV-5R Mini export (2026-07-10):

- `Power` is rewritten to the radio's own levels (`10W` → `5.0W`, `2.0W` → `1.0W`).
- `TSQL` rows are collapsed to CHIRP's internal form: `rToneFreq=88.5` with the real
  tone only in `cToneFreq` (the split this repo deliberately avoids — see the tone
  standard above).
- Channels already sitting in the radio's memory come along too (the Mini's 999-slot
  memory contributed 11 leftover repeaters at slots 989–999).

None of that hurts *that* radio, but it makes the CSV radio-specific and drops it out of
the provenance chain. **Rule: a CSV in this repo carries house values** (`10W`/`2.0W`/
`6.0W`, `rToneFreq == cToneFreq`, ≤ 8-char names, ≤ 200 slots) **and lets CHIRP clamp at
import time.** If you edit a plan by way of the radio, port the *intended change* back
into the source CSV (e.g. just the `Skip` column) rather than committing the export.

## Frequent destinations (priority coverage)

The owner regularly visits family in **Somerset, KY** and **Bowling Green, KY**. When
a trip plan's route passes near either, **prioritize good repeater coverage there**
(treat them like a home region — pull the best local repeaters, not just pass-through
ones). Somerset KY = Pulaski County; Bowling Green KY = Warren County (SW KY, *not* on
the I-75 corridor).

## Duplex / offset defaults

- Simplex: `Duplex` empty, `Offset=0.000000`.
- 2 m repeater: `±` with `Offset=0.600000` (a few use `0.840000`/`1.600000`/`2.500000`).
- 70 cm / GMRS repeater: `+` with `Offset=5.000000`.
- Weather: `Duplex=off` (receive-only).

## File-naming convention

Descriptive, human-readable filenames describing scope:
- A route as `<FROM> to <TO>.csv`.
- A multi-state pool as the hyphenated state list (`GA-IL-IN-KY-NC-OH-SC-TN-VA.csv`).
- A role as a plain label (`local baseline.csv`).
- A **supplement plan** as `<Purpose> (201+).csv` — the slot range marks it as an
  add-on for the 999-channel radios (`Scan Channels (201+).csv`).
- A **scan variant** of an existing plan as `<Parent Plan> (skip all but local).csv`.
- **Optional `(MMM-YYYY)` date tag** to mark an older/legacy or dated version
  (e.g. a `(Jun-2026)` suffix) — signals "this one is older."
- A **radio image** (`IMG Files/*.img`) as `<Radio> - <Plan>.img` — the radio model
  first, then the plan it was built from.
