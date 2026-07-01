# TODO — Queued Build Tasks

> Created 2026-06-29. Tasks to build next session.
> **All must follow the standards set this session:**
> - **Provenance chain** — `References/` → `CHIRP Lists/` → `Complete Radio Plans/`.
>   Every list channel traces to a source; plans are assembled ONLY from CHIRP Lists
>   (see [`conventions.md`](conventions.md)).
> - **LCD rules** — `Name` ≤ 8 chars, ≤ 200 channels, ham ≥ 100 / GMRS ≤ 99.
> - **Tone standard** — `TSQL` when the repeater broadcasts a tone (with
>   `rToneFreq == cToneFreq`); `Tone` (encode-only) only for input-tone-only repeaters;
>   carrier when none. Never leave the `88.5` placeholder on a toned row.
> - **Verify** each repeater's freq/offset/tone against the club lists AND RepeaterBook,
>   the way the baseline was checked.

---

## 1. KY travel list — Bowling Green + Somerset  ✅ DONE 2026-07-01
**Built as `Complete Radio Plans/AVL to KY.csv` (141 ch)** + two reusable destination
CHIRP Lists (`KY Somerset (LCARA).csv`, `KY Bowling Green (KCARC).csv`). See
[`inventory.md`](inventory.md). Original spec below (kept for reference):

A trip/route Complete Radio Plan per **SOP 3**: full `local baseline.csv` + route
repeaters appended (route GMRS from slot **50**, route ham from slot **150**), ordered
in drive sequence.
- **Priority destinations (treat as home regions):** **Somerset, KY** (Pulaski Co —
  LCARA) and **Bowling Green, KY** (Warren Co — KY Colonels). Pull their *best* local
  repeaters, not just pass-through ones.
- **Sources:** ham pool `CHIRP Lists/GA-IL-…VA.csv`, `CHIRP Lists/GMRS GA-IL-…csv`, plus
  the `References/` LCARA (Somerset) and KY Colonels (Bowling Green) club docs for the
  destination repeaters those pools don't carry.
- **Routes:** cover AVL→Somerset (I-75 corridor) and AVL→Bowling Green (Cumberland Pkwy /
  Nashville corridor). De-dupe against the baseline's local blocks.
- Name `AVL to KY.csv`. (A prior version was discarded in the cleanup — rebuild to the
  current standard, including the foolproof tones.)

## 2. Definitive NC supplement list (CHIRP List)
A fully-verified statewide-NC **building block** (GMRS + ham) to combine with the
baseline for NC-wide coverage — the refined successor to
`CHIRP Lists/NC Coverage (GMRS + Ham).csv`.
- **"Definitive" =** every channel sourced and **tone-verified** to the current standard
  (TSQL-when-broadcasting, `rTone == cTone`), freqs consistent across RepeaterBook +
  any club data.
- Source from the two pools; favor geographic spread across the NC regions the baseline
  doesn't already cover. Keep GMRS ≤ 99 / ham ≥ 100 slotting for a building block.
- Cross-check downlink tones against RepeaterBook (same method used on the baseline) so
  TSQL vs encode-only is correct per repeater.

## 3. Maximal list (Complete Radio Plan)
Recreate the "kitchen-sink" plan (prior `Maximal Default.csv` was discarded):
baseline core + the NC supplement (#2) + regional GMRS/ham + KY destination repeaters +
local monitoring (Airport / Local Emergency / CMC), **≤ 200 channels**, scan kept lean
(local repeaters + the two calling freqs only; everything added `Skip=S`).
- **Assemble ONLY from CHIRP Lists** (provenance rule) — build/extend the needed lists
  first, then pull from them.
- Monitoring blocks (airport / emergency / CMC) sit in a high "monitoring" section
  (≈ 160–199) per the slot-rule relaxation in [`conventions.md`](conventions.md).
- Apply the foolproof tone standard throughout.
