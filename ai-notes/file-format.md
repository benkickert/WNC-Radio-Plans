# CHIRP CSV File Format

> **Last updated:** 2026-07-13
> Reference for the column layout CHIRP uses, and the two variants present in this folder.
> **Authoritative source:** `References/CHIRP CSV Format and Settings.txt` (plus the
> official `CHIRP Tone Programming Examples` PDF) holds the definitive column and
> tone-mode (Tone/TSQL/DTCS/Cross) spec. This file documents how *this repo* uses it.

## What CHIRP expects

CHIRP imports a CSV whose **first row is a header naming the columns**. Column
*order* is what CHIRP keys on by name; trailing columns may be omitted and CHIRP
fills sensible defaults on import. Each subsequent row is one channel ("memory").

Two distinct export profiles exist in this folder. Both import fine. Pick the one
that matches whatever you're editing — don't mix layouts within a single file.

---

## Profile A — "full" (21 columns)

Used by **`local baseline.csv`** (and the `Arcshell` codeplug). Includes the trailing
D-STAR columns and uses zero-padded DTCS codes.

```
Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,RxDtcsCode,CrossMode,Mode,TStep,Skip,Power,Comment,URCALL,RPT1CALL,RPT2CALL,DVCODE
```

## Profile B — "lean" (14 columns)

Used by **`GA-IL-IN-KY-NC-OH-SC-TN-VA.csv`**. Drops `TStep`, `Skip`, `Power`, and
all four D-STAR columns; the `Comment` field is heavily used; DTCS codes are
**not** zero-padded (`23` instead of `023`).

```
Location,Name,Frequency,Duplex,Offset,Tone,rToneFreq,cToneFreq,DtcsCode,DtcsPolarity,RxDtcsCode,CrossMode,Mode,Comment
```

---

## Column reference

| Column | Meaning | Notes / values seen here |
|--------|---------|--------------------------|
| `Location` | Memory-slot number (integer) | The radio channel index. Owner uses a block scheme — see `conventions.md`. Must be unique within a file. |
| `Name` | Display label | **≤ 8 characters.** Truncated/abbreviated to fit radio displays. |
| `Frequency` | RX frequency in MHz | 6 decimal places, e.g. `462.562500`. For a repeater this is the **output** (what you listen to). |
| `Duplex` | TX offset direction | `` (empty) = simplex; `+` = TX above RX; `-` = TX below RX; `off` = RX-only (used for weather channels); `split` = explicit TX freq. |
| `Offset` | Offset magnitude in MHz | e.g. `0.600000` (2 m), `5.000000` (70 cm / GMRS repeater), `0.000000` for simplex. Combined with `Duplex` sign. |
| `Tone` | Tone mode | `` (none); `Tone` (TX CTCSS only); `TSQL` (CTCSS encode+decode); `DTCS` (digital squelch); `Cross` (different TX/RX tone schemes, see `CrossMode`). |
| `rToneFreq` | CTCSS tone for TX (repeater tone) | Hz, e.g. `88.5`, `141.3`. **`88.5` is the placeholder/default** when no tone applies — don't assume 88.5 is meaningful unless `Tone` is set. |
| `cToneFreq` | CTCSS tone for RX squelch | Used when `Tone`=`TSQL`. |
| `DtcsCode` | DTCS code for TX | e.g. `023`/`23`, `315`. Profile A zero-pads, Profile B does not. `023` is the default placeholder. |
| `DtcsPolarity` | DTCS polarity | `NN` = normal/normal (default). |
| `RxDtcsCode` | DTCS code for RX | Mirrors `DtcsCode` unless cross. |
| `CrossMode` | TX→RX tone combo when `Tone`=`Cross` | e.g. `DTCS->` (DTCS on TX, nothing on RX), `->Tone`. Otherwise the harmless default `Tone->Tone`. |
| `Mode` | Modulation / channel width | `FM` (wide, 25 kHz); `NFM` (narrow, 12.5 kHz — used for GMRS 8–14 low-power & MURS VHF). |
| `TStep` | Tuning step (kHz) | Profile A only. `5.00` throughout. |
| `Skip` | Scan-skip flag | Profile A only. `S` = skip during scan; empty = include in scan. Simplex/weather channels are often `S`. |
| `Power` | TX power level | Profile A only. e.g. `10W`, `2.0W`, `6.0W`. String must match a level the radio recognizes. |
| `Comment` | Free text | Profile B encodes metadata here — see below. Empty in Profile A. |
| `URCALL`,`RPT1CALL`,`RPT2CALL`,`DVCODE` | D-STAR digital fields | Profile A only; empty (these are analog FM channels). |

---

## The `Comment` metadata code (Profile B)

In `GA-IL-IN-KY-NC-OH-SC-TN-VA.csv` the comment was rewritten (2026-06-25) from the
raw repeater-scores.app badge into a **state-first, readable, sortable** form:

```
<STATE> S<NN> | <decoded capabilities> | <tinyurl>
```

Example: `GA S12 | Sys, AllStar+EchoLink, Wide, Nets | https://tinyurl.com/29fqemp4`

- **`<STATE>`** — 2-letter state (GA, IL, IN, KY, NC, OH, SC, TN, VA).
- **`S<NN>`** — score, **zero-padded to 2 digits** (`S03`..`S12`) so a plain text
  sort orders by score. Higher = more signals (nets, links, coverage, public-service
  affiliations). State-first means a text sort groups by state, then by score.
- **decoded capabilities** — plain English, comma-separated; `basic` if none:
  - link: `Sys` (system-linked) / `Link` (other linked)
  - connectivity: `AllStar` / `EchoLink` / `AllStar+EchoLink`
  - `Wide` (wide-area) · `Nets` (≥ 2 nets)
- **tinyurl** — the per-repeater RepeaterBook listing (preserved unchanged).

Because the decoded text contains commas, the **Comment field is double-quoted** in
this file wherever it has more than one capability (valid CSV; CHIRP's csv reader
handles it). Single-capability rows (e.g. `TN S04 | Sys | …`) need no quoting.

This is derived from the original **repeater-scores.app** badge (`ST/SXCWN`); the raw
flag letters and full scoring rules are in
[`References/repeater-scores.app - Scoring Explained.txt`](../References/repeater-scores.app%20-%20Scoring%20Explained.txt).
Mapping from the raw badge: `S`/`L` → Sys/Link; `A`/`E`/`B` → AllStar/EchoLink/
AllStar+EchoLink; `W` → Wide; `N` → Nets. (Scores here are full integers 3–12; the
single-digit/max-9 cap in the doc applies only to the ICOM-5100 Sub Name badge.)

## Reference-derived annotations (appended to `Comment`)

Some CHIRP List rows carry an extra note **appended after a final ` | `**, pulled from
the `References/` docs where a row was **confirmed to be the same repeater** (by town +
freq, not freq alone — GMRS/ham reuse channels, so freq-only matching gives false
hits). These add nets / nodes / club / true site name. Examples:
- ham pool `Somerset` 146.880 → LCARA AllStar/EchoLink + remote-RX tones;
  `BurnsVll` 145.190 → WCARS "N2GE Clingmans Pk / Mt Mitchell"; `MarsHl-W` →
  "K4MFD Wolf Ridge"; KY `Morganto` / `CaneVly-` → KY Colonels club info.
- GMRS pool `Fletcher` 462.700 → "net Sat 8PM (WNC Radio Project)".
- Simplex list `146.580` / `147.570` → Somerset / Monticello KY club simplex.

These travel with the row when pulled into a plan. Add more only on a **confirmed
town+freq match** — never blanket-annotate by frequency.

(The raw repeater-scores.app badge can always be re-derived from the decode above if
a fresh export is ever re-imported.)

---

## Gotchas

- **A repeater's listening frequency is the output.** With `Duplex=+/-` and an
  `Offset`, the radio transmits on output ± offset. Don't put the input freq in
  `Frequency`.
- **`88.5` / `023` are defaults, not data — *unless a tone mode is set*.** They appear on
  toneless channels as placeholders, and the tone is only meaningful when the `Tone`
  column says so. **But 88.5 Hz is also a real CTCSS tone**, and ~60 rows here legitimately
  use it (e.g. `GWeaverv` `TSQL` 88.5, `Crossvil` 443.875 `Tone` 88.5). So: read the
  **`Tone` mode column**, not the number. Mode empty → the 88.5 is inert; mode set → the
  88.5 is real and **must not be stripped**. See [`conventions.md`](conventions.md).
- **`NFM` vs `FM` matters on air.** GMRS channels 8–14 and MURS 1–3 are narrowband
  by regulation; keep them `NFM`.
- **Mixing profiles** (e.g. adding D-STAR columns to Profile B rows) can confuse a
  re-export. Keep a file internally consistent.
