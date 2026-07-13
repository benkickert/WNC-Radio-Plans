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

## 1b. Carthage TN gap-filler + fix the radio's Knoxville offset  *(added 2026-07-13)*

**Background (already evaluated — don't redo).** The UV-5R Mini export carried 11
repeaters the owner hand-entered on a Bowling Green → Asheville drive months ago (radio
memory 989–999). They are the **least-verified data in the system** — hand-entered at the
plan/radio level, below every tier of the provenance chain — so they were evaluated
against `References/` first, then the CHIRP Lists, and dropped from the CSV. Outcome:

- **8 were duplicates** of rows already in `AVL to KY.csv` (Cookeville, Newport 147.09,
  Knoxville-Sharps, Crossville, Lafayette, BGrn330/BGrn165/BGrn444). Nothing to do.
- **`NewP22m` 146.730 — refuted.** `References/RepeaterBook - KY route gap-fillers.txt`
  enumerates Newport TN's repeaters (147.090 + 443.300 + 443.750); **there is no 146.730
  in Newport.** The pool's TN 146.730 is **Lafayette** (TSQL 114.8), which the radio also
  had as `LaFTN2m` — so this was a mislabeled duplicate with the tone dropped. Nothing to
  add.
- **`woodBTN2m` 146.910 — unsupported.** In this repo 146.910 is **`SpiveyV` (W4MOE,
  Spivey Mtn)**, the local WNC repeater in the baseline; no TN repeater exists at 146.910
  anywhere in the pool. A carrier-squelch 146.910 just hears Spivey. Only worth chasing
  if "Woodbury TN" turns out to be real on RepeaterBook.

**✅ Carthage + Woodbury sourced and pulled in (2026-07-13) — DONE.** Verified on
RepeaterBook, recorded in `References/RepeaterBook - KY route gap-fillers.txt`, added to
the new `CHIRP Lists/KY route gap-fillers (RepeaterBook).csv`, and pulled into
`AVL to KY.csv` at slots 171–172 in drive order (Cookeville → Carthage → Woodbury →
Nashville; the Bowling Green block shifted 172–182 → 174–184). Plan is now 143 ch.
- `CarthgV` 145.250 −0.600 — **KJ4EVS, Carthage** (Smith Co), open/on-air, SERA. Uplink
  114.8, **no downlink** → `Tone` (encode-only). *The radio had it as TSQL 114.8, which
  would have muted RX.*
- `WoodbryV` 146.910 −0.600 — **W4YXA, Short Mountain, Woodbury** (Cannon Co), open/
  on-air, wide site. Uplink 114.8, **no downlink** → `Tone`. *The radio had it on carrier
  with no tone, so it would never have keyed the repeater.* (`woodBTN2m` was therefore a
  real repeater after all — just misprogrammed. Note 146.910 also = baseline `SpiveyV`,
  tone 91.5; kept as separate channels.)
- Also learned: Carthage **146.730 K4TP is OFF-AIR** — do not program. (The live 146.730
  on this route is Lafayette TN, already at slot 170.)

**⚠️ Remaining — owner action on the radio (no CSV change):** the UV-5R Mini's `Knox2m`
(145.370) is programmed **`+0.400`**. The ham pool has `Knox-Sha` at the standard 2 m
**`−0.600`** (Tone 100.0, S08, Sharps Ridge), and `AVL to KY.csv` carries it correctly —
so the **radio is wrong** and that channel has never keyed Knoxville. Reflashing the
radio from `AVL to KY.csv` fixes it, along with the two misprogrammed repeaters above.

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
