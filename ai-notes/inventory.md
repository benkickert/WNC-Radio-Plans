# Inventory — What's in Each CSV

> **Last updated:** 2026-07-13
> Keep this in sync when files are added, removed, or substantially restructured.

The region of interest is **Western North Carolina (Asheville = "AVL") and the
corridor toward Atlanta ("ATL")**, expanding to a multi-state pool.

Files are split into two folders by readiness:
- **`Complete Radio Plans/`** — finished codeplugs to flash whole (normalized to LCD rules).
- **`CHIRP Lists/`** — component lists to pull from (raw pools *and* clean blocks).

---

## `Complete Radio Plans/local baseline.csv` — 91 channels (Profile A)

The everyday WNC memory list — local/WNC content only. It is the folder's **only
universal/LCD codeplug** (the Arcshell file is radio-specific), so it flashes to any
fleet radio for full local coverage. Organized into numbered blocks with gaps for
growth:

| Slots | Block | Scan | Contents |
|------:|-------|------|----------|
| 1–22  | GMRS simplex | skip | All 22 FCC GMRS channels. 1–7 & 15–22 are `FM`/`10W`; 8–14 are the `…LP` low-power interstitial channels, `NFM`/`2.0W`. |
| 23–30 | Generic GMRS repeaters | skip | `GMRS15R`–`GMRS22R` (8 standard pairs, +5 MHz, TSQL travel tone 141.3). Skipped (2026-07-01) — travel-tone set, not everyday scan. |
| 31–47 | Local WNC GMRS repeaters (17) | **scan** | Named `G…` repeaters (`GAlexndr`, `GBearwal`, `GEchoMtn`, `GFlatTop`, `GPisgahF`, `GSwannan`, `GClyde`, etc.). |
| 81–85 | MURS | skip | `MURS1`–`MURS3` (VHF, `NFM`), `MURS4BD`/`MURS5GD` (154 MHz "blue/green dot", `FM`). |
| 91–97 | NOAA weather | skip | `WX1AVL`–`WX7`, all `Duplex=off` (receive-only), `6.0W`. |
| 100/101 | 70cm / 2m calling | **scan** | `70cmCall` (446.000) / `2mCall` (146.520). |
| 102–109 | Ham simplex | skip | 4× 70 cm + 4× 2 m SERA FM simplex options. |
| 110–131 | Local WNC ham | **scan** | Named WNC 2 m (`…V`) and 70 cm (`…U`) repeaters (`BakersV`, `BearU1/2`, `ClngmnV`, `PisgahV`, `SpiveyV`, `SpiveyU`, etc.) — 22 repeaters. |

**Scan policy (41 ch, updated 2026-07-01):** only the **local** repeaters (GMRS 31–47 +
ham 110–131) and the two ham calling freqs (100/101) are in scan. Everything else is
`Skip=S`: all simplex (GMRS 1–22, ham 102–109), the **generic GMRS travel-tone block
(23–30)**, MURS, and WX. (The generic block was moved to skip 2026-07-01 — it's a
"try any open repeater on the travel tone" set, not part of the everyday scan.)

**Role:** the owner's everyday-local plan, and the **core that the other universal plans
build on** — `Extended Baseline`, its quiet-scan variant, and `AVL to KY` all carry it
verbatim at slots 1–131 and append from there. It carries the 8 SERA ham-simplex
channels (102–109) and the 22 local WNC ham repeaters at 110–131. (It is *not* a
propagating master: a change here does not automatically flow into those plans — see
[`open-questions.md`](open-questions.md) Q7.)

**Tones (verified 2026-06-29):** all repeater freqs/offsets cross-checked against the
WCARS + WNC-GMRS club lists and RepeaterBook — fully consistent. Tones set to the
**TSQL-when-broadcasting standard** (see [`conventions.md`](conventions.md)): toned
repeaters use `TSQL` with `rToneFreq == cToneFreq` (RX gated, so you can tell which
repeater you're hearing on shared channels); `GForestC` uses `DTCS` 205/205; tone-less
repeaters stay carrier. The earlier `rToneFreq=88.5` placeholder (the TX-tone bug) is
gone. Added RepeaterBook-confirmed tones to `BearU2`/`BearV1` (91.5, WA4KNI) and `CoweeU`
(131.8). **Cleanup 2026-06-29:** removed `GWaynesv` (duplicate of `GHaywood`) and
`GClyde` (no source in References or any CSV); kept `GTryon` — verified via
`References/RB - GMRS/rb_chirp_2606251318.csv` (Tryon/Landrum 462.650, TSQL 91.5).
`BearU1` (442.45) confirmed sourced from WCARS (WA4TOG Bearwallow, no tone) → carrier
correct. Subsequent slots shifted up to keep the block contiguous (31–46; now 31–47 with
`GClyde` re-added 2026-07-01). **No open
items remain** — every baseline repeater traces to the club lists or RepeaterBook.
**Correction 2026-07-01:** slot 32 `GSpiveyM` (462.725) changed `TSQL`→`Tone` (141.3,
encode-only) — Spivey broadcasts no output tone, so the old `TSQL` muted RX and the
repeater couldn't be heard. Confirmed against RepeaterBook + the GMRS pool + the
WNC-GMRS list.
**Ham tone-mode audit 2026-07-01:** all 11 toned ham repeaters (slots 112–130) changed
`TSQL`→`Tone` (encode-only) after verifying against RepeaterBook uplink/downlink —
these repeaters transmit no matching output tone, so `TSQL` risked muting RX. Carrier
RX has no downside (unique ham output freqs). `CashrsV` also had its access tone updated
100.0→151.4 per RepeaterBook (conflicts with WCARS — flagged). See
`References/RepeaterBook WNC Ham Tones.txt` and [`open-questions.md`](open-questions.md) #7.
Baseline GMRS repeaters (31–47) keep `TSQL`/`DTCS` where the RB-GMRS export confirms an
output tone; the 5 sourced only from the WNC-GMRS club list (`GEchoMtn`, `GFlatTop`,
`GPisgahF`, `GSwannan`, `GWeaverv`) have output tone **unconfirmed** — a pending question
(see open-questions #7).

---

## `Complete Radio Plans/Extended Baseline.csv` — 157 channels (Profile A)

Built 2026-07-01. **The full `local baseline` (slots 1–131) plus best statewide-NC
ham/GMRS and extended coverage into six border metros.** A universal codeplug like the
baseline, extended for regional travel; still ≤ 200 and LCD-compliant.

| Slots | Block | Scan | Contents |
|------:|-------|------|----------|
| 1–131 | Baseline core | (as baseline) | The entire `local baseline.csv` verbatim. |
| 50–65 | Extended GMRS — metros | scan | Knoxville WRJZ925 system (`GKnoxvil`/`GPigeonF`/`GOakRidg`) + `GKnoxFC`; Tri-Cities & corridor (`GJohnsnC`/`GJohnsn2`/`GRoanMtn`/`GHampton`/`GKingspt`/`GBristol`/`GButler`); Upstate/Rock Hill (`GAnderSC`/`GGaffney`/`GYorkSC`/`GRockHil`/`GRockHi2`). |
| 66–80 | Extended GMRS — NC statewide | scan | The 15 GMRS from `NC Coverage` (Newland→Buxton). |
| 150–164 | Extended ham — NC statewide | scan | The 15 ham from `NC Coverage`. |
| 165–168 | Extended ham — top NC | scan | Highest-scored NC ham `NC Coverage` missed: `SnowCmp-` (S11), `Coats-Am`/`HollySpg`/`Wendell-` (S10). |
| 169–184 | Extended ham — metros | scan | Knoxville (`Knox-Sha`/`Knox-WJX`) + I-40 corridor (`TopOfWor`/`Gatlinbu`); Newport/Greeneville (`GreeneVl`); Tri-Cities (`Bristol-`/`JohnsonC`/`Gray-W4Y`/`Mooresbu`); Upstate SC (`MtRest-L`/`Greenvil`/`Gville-P`/`Spartanb`); Rock Hill (`York-W4P`/`FortMill`/`Sharon-W`). |

**Sources (provenance):** assembled only from CHIRP Lists — `NC Coverage (GMRS + Ham).csv`,
the ham pool `GA-IL-…VA.csv` (Profile B → A converted), and the GMRS pool
`GMRS GA-IL-…csv`. Extended-GMRS rows keep the pool's geographic `Comment`; extended-ham
tones are RepeaterBook-derived from the pool (TSQL = matching downlink, `Tone` =
encode-only — same standard as the WNC ham audit).

**Selection:** ham by RepeaterBook score (favoring linked/wide/net systems) + the
corridor/wide-area repeaters that fill gaps *between* the metros (Top-of-the-World,
Mountain Rest, Roan Mtn, the WRJZ925 & WRNU734/WRQK371 linked systems). GMRS by
open/on-air coverage, whole linked systems kept. De-duped against the baseline.

**Scan policy:** every repeater scanned (baseline local + all extended) + the two ham
calling freqs; simplex, generic-GMRS, MURS, and WX skipped. 107 scan / 50 skip.

**Note — GMRS shares 8 output channels:** several extended GMRS entries share
`Frequency`+`Tone` with each other and with baseline/NC blocks (e.g. multiple
462.600/141.3). They're distinct repeaters in different towns kept for labeling and
coverage (the owner's inclusive preference); on air they're the same channel.

**Gaps noted:** Greenville & Spartanburg SC have **no open GMRS** in the pool (all
CLOSED/off-air), so those two metros are ham-only on the GMRS side; nearest open SC GMRS
is Gaffney/York. Newport TN has no dedicated repeater — covered by Greeneville/Cocke-area
and the I-40 corridor set.

---

## `Complete Radio Plans/Extended Baseline (skip all but local).csv` — 157 channels (Profile A)

Added 2026-07-13. **Identical channel content to `Extended Baseline.csv` — only the
`Skip` column differs.** A "carry-everything, scan-nothing-distant" variant: the owner
wants the full regional set *in the radio* but doesn't want the out-of-area repeaters
cluttering the default scan, since any channel can be added to scan at the radio when
travelling. See the **quiet-scan variant** entry in [`conventions.md`](conventions.md).

**Scan policy (41 ch):** the same scan set as `local baseline.csv` — the 17 local WNC
GMRS repeaters (31–47), the 22 local WNC ham repeaters (110–131), and the two ham
calling freqs (100/101). **Everything else is `Skip=S`**, including all extended GMRS
(50–80) and extended ham (150–184) — the blocks that scan in `Extended Baseline.csv`.

**Maintenance:** treat `Extended Baseline.csv` as the parent. If a channel is added or
changed there, mirror it here and set `Skip` per the policy above; don't let the two
files' channel content drift apart.

> **Origin note (2026-07-13):** the owner created this by editing scan flags in CHIRP
> and exporting from the UV-5R Mini, so the first version carried CHIRP's own
> radio-side values: `Power` rewritten `10W`→`5.0W` / `2.0W`→`1.0W`, and TSQL rows
> collapsed to `rToneFreq=88.5` with the tone only in `cToneFreq`. It was **normalized
> back to house values** (10W/2.0W/6.0W, `rToneFreq == cToneFreq`) so the CSV stays
> fleet-neutral and CHIRP does the per-radio clamping at *import* time — see
> [`open-questions.md`](open-questions.md) #6. The export also carried 11 stray
> repeaters at slots 989–999 that were already sitting in the Mini's memory from an
> earlier trip; they were dropped from the CSV (8 duplicate rows already in
> `AVL to KY.csv`; the 3 genuinely-new ones are queued in [`todo.md`](todo.md)).

---

## `Complete Radio Plans/AVL to KY.csv` — 143 channels (Profile A)

Built 2026-07-01; Carthage + Woodbury added 2026-07-13. **KY family-trip plan (SOP 3):** full `local baseline` (1–131) +
route repeaters in drive sequence + heavy destination coverage for Somerset and
Bowling Green. ≤ 200, LCD-compliant.

| Slots | Block | Contents |
|------:|-------|----------|
| 1–131 | Baseline core | The entire `local baseline.csv` verbatim. |
| 50–66 | Route GMRS (drive order) | Trunk AVL→Knoxville (`GPigeonF`/`GSevierv`/`GGatlinb`/`GKnoxvil`/`GKnoxFC`/`GOakRidg`), then Williamsburg, Somerset area (`GSomerse`/`GBeeLick`/`GNancy`), Russell Springs, and the Nashville/I-65 leg (`GNashvil`/`GLebanon`/`GGallatn`/`GHndrsnv`/`GPortlnd`/`GMillrsv`). |
| 150–159 | Route ham — trunk + I-75 | `Madison-` (Hot Springs/Marshall), `NewprtTN` (RB gap-filler), Sevierville ×2, Knoxville ×2; Corbin ×2, London (`London-R` S10). |
| 160–164 | **Somerset destination** | Pulled from `KY Somerset (LCARA).csv`: `SomrstV` (146.880/77.0), `SomrstU` (443.600), `MontcloV` (145.150) + 2 club simplex. |
| 165–173 | Route ham — Cumberland Pkwy & I-40 | `Columbia` KY; Crossville ×2, Cookeville ×2, Lafayette TN; **`CarthgV` (Carthage) + `WoodbryV` (Woodbury/Short Mtn)** — RB gap-fillers added 2026-07-13; Nashville. |
| 174–184 | **Bowling Green destination** | Pulled from `KY Bowling Green (KCARC).csv`: BG ×3, Morgantown, Franklin, Glasgow ×3, Bonnieville ×2, Cane Valley. |

**Sources (provenance):** baseline + the two pools (route, RepeaterBook-derived tones)
+ the two KY club lists (destinations) + `CHIRP Lists/KY route gap-fillers (RepeaterBook).csv`
(`NewprtTN`, `CarthgV`, `WoodbryV` — the three route repeaters absent from the scored
pools; note the pool's "Newport" is coastal **NC**, not the TN route town).

**Route design (owner-set):** the **AVL→Newport→Knoxville trunk is common to every
route, so it's covered best**; from Knoxville the branches are treated equally
(US-27 Oneida/Stearns; I-75 Corbin/London; I-40 Crossville/Gordonsville/Scottsville;
I-40→Nashville→Franklin; Cumberland Pkwy Columbia/Glasgow). Some small route towns
(Oneida, Pine Knot, Stearns, Burnside, Gordonsville, Hartsville, Scottsville,
Goodlettsville) have **no repeater in the pools** — bracketed by the nearest covered
sites. **Carthage is now covered** (2026-07-13): RepeaterBook confirmed KJ4EVS 145.250,
and the wide Short Mountain site at Woodbury was added with it — both sourced outside the
pools via the gap-filler list.

**Tones:** route from the pools (RB-derived TSQL/`Tone`); destinations from the club
PLs as encode-only (`Tone`) where downlink isn't confirmed, so they're never muted
(`SomrstV` is `TSQL` 77.0 — pool-confirmed broadcast). **Flag:** `MorgtnV` 146.655 —
KCARC says "no tone" but the pool shows TSQL 100.0; encoded 100.0 (keys either way).

**Scan:** all repeaters scanned; simplex (incl. the 2 club simplex), generic-GMRS,
MURS, WX skipped. 89 scan / 52 skip.

---

## `Complete Radio Plans/Scan Channels (201+).csv` — 40 channels (Profile A)

Built 2026-07-13. **A supplement plan, not a standalone codeplug** — slots start at
**201**, so it loads *on top of* any universal ≤ 200 plan and fills the empty memory
above it. Only the **999-channel radios (UV-5R Mini, UV-5G Plus)** can hold it; the
TD-H9/TD-H8 stop at 200. See [`conventions.md`](conventions.md) ("Supplement plans")
and [`sops.md`](sops.md) SOP 6.

Purpose: the owner's **monitoring/scanner set** — local emergency services plus both
airports — carried in the spare memory rather than spending base-plan slots on it.

| Slots | Block | Ch. | Pulled from |
|------:|-------|----:|-------------|
| 201–221 | Buncombe County public safety | 21 | `CHIRP Lists/Local Emergency.csv` |
| 225–233 | Asheville airport (KAVL) | 9 | `CHIRP Lists/AVL Airport.csv` |
| 235–244 | Charlotte airport (KCLT) | 10 | `CHIRP Lists/CLT Airport.csv` |

Gaps at 222–224, 234, and 245+ are left for growth (`CMC.csv` is the obvious next
block).

**Sources (provenance):** pulled verbatim from the three CHIRP Lists above — only
`Location` was renumbered. Those lists trace to `References/Buncombe County
Public-Safety Frequencies.txt` (RadioReference) and `References/Airport Frequencies
(KCLT, KAVL).txt` (FAA Chart Supplement / CLT ATCT SOP).

**Everything is receive-only** (`Duplex=off`) — public-safety and airband channels are
monitor-only and must never have a transmit path. **All 40 are in scan** (`Skip` blank);
the plan *is* the scan set.

**Radio caveat (reference, not a filter — the file carries the full set per
[`radios.md`](radios.md)):** the airport blocks are **AM airband**. The UV-5R Mini
receives VHF airband and 351.800 but *not* the AVL mil channels at 257.800/269.575
(slots 225/226); the UV-5G Plus receives **no** airband at all, so on it the 18 airport
channels are dead air while the 21 public-safety channels work fine.

---

## `Complete Radio Plans/Arcshell with Fletcher on 8.csv` — 16 channels (Profile A)

A **radio-specific** codeplug for the **Arcshell AR-5** — not a universal/LCD file.
Primarily GMRS simplex with one repeater channel:

| Slots | Contents |
|------:|----------|
| 1–7  | GMRS simplex channels 1–7 (462.5625–462.7125), `5.0W` |
| 8    | **Fletcher GMRS repeater** — 462.700, `+5.000000`, `TSQL` 141.3/141.3 (rTone==cTone), labeled "Fletcher repeater" (config matches baseline `GFletchr`) |
| 9–16 | GMRS simplex channels 15–22 (462.550–462.725), `5.0W` |

Distinctive traits worth noting (per-radio conventions for the AR-5):
- **`Name` left blank on every channel** — the AR-5 is operated by frequency /
  channel number, so alpha names aren't used here. (Deliberate; differs from the
  ≤8-char-name convention used on the name-capable radios.)
- **`5.0W` power** throughout (AR-5 is a 5 W radio, vs the 10 W TID units).
- **All channels `Skip=S`.**
- Omits the GMRS 8–14 (467 MHz low-power) channels.

Channel 8 was corrected (2026-06-25) to a proper repeater config — `Duplex=+`,
`Offset=5.000000`, `TSQL` 141.3/141.3 — matching baseline `GFletchr`, so it now
transmits through the Fletcher repeater (input 467.700). Power kept at the AR-5's
`5.0W`. (Fixed 2026-07-01: was `rTone 88.5 / cTone 141.3`; corrected to the foolproof
`rTone==cTone==141.3`.)

---

## `CHIRP Lists/GA-IL-IN-KY-NC-OH-SC-TN-VA.csv` — 858 channels (Profile B)

A large **reference pool** of amateur repeaters across 9 states (GA, IL, IN, KY,
NC, OH, SC, TN, VA) — "all the decent repeaters" across those states. This is
**not a finished codeplug and is NOT yet normalized to the owner's needs**: it has
858 rows (far over the 200-channel cap), is in the lean Profile B layout, and is
not slotted into the 1–99 / 100+ scheme. It's a ranked database to *pull from*
when building targeted lists. **Normalizing it** = filter/dedupe → trim to ≤ 200
ham channels → convert Profile B→A → renumber into slots ≥ 100 (see
[`sops.md`](sops.md)).

- **Ham only** — no GMRS, MURS, or weather entries.
- **Row order is by score, descending** (12 at top → 3 at bottom).
- Each row's `Comment` is the **decoded, sortable** form
  `STATE S<NN> | capabilities | tinyurl` (e.g. `GA S12 | Sys, AllStar+EchoLink, Wide,
  Nets | https://…`) — rewritten 2026-06-25 from the raw repeater-scores.app badge.
  Score is zero-padded for text-sorting; see
  [`file-format.md`](file-format.md#the-comment-metadata-code-profile-b).
- Uses the lean column set and unpadded DTCS codes. Comment fields with commas are
  double-quoted (valid CSV).

Typical use: filter by state and/or score threshold to extract a manageable set,
then convert to Profile A and renumber into a target codeplug. See
[`sops.md`](sops.md).

---

## `CHIRP Lists/GMRS GA-IL-IN-KY-NC-OH-SC-TN-VA.csv` — 343 repeaters (Profile A)

The **GMRS** counterpart to the amateur pool: open GMRS repeaters across the same 9
states, built from RepeaterBook web data (which carries Use + Operational Status,
unlike the CHIRP-format export). All are 462.550–462.725 outputs, `+5 MHz`, FM,
`10W`.

- **Filtered (2026-06-25):** only **OPEN** + **on-air** kept. Dropped from the 464
  source rows: **99 CLOSED**, **19 off-air (🔴)**, **3 duplicates** → **343** kept.
  9 rows with RepeaterBook "unknown" status (🟡/⚪) were kept but tagged `unverified`
  in the comment.
- **No score/flags** — GMRS has no nets/AllStar/EchoLink scoring, so instead of the
  amateur badge the **Comment** is geographic/sortable:
  `<ST> | <County> | <Location> | <Owner>[ | unverified]`
  (sorted by state → frequency → town; state-first so a text sort groups by region).
- **Tones decoded** from the RB "uplink / downlink" pair: same CTCSS both ways →
  `TSQL`; uplink-only or mismatched → `Tone` (encode); `Dxxx` → `DTCS`; none/CSQ →
  no tone.
- Raw per-state RepeaterBook CHIRP exports are in `References/RB - GMRS/` (kept as
  source; they lack status so they were **not** the basis for the filter).

---

## `CHIRP Lists/NC Coverage (GMRS + Ham).csv` — 30 channels (Profile A)

A curated **statewide North Carolina** coverage set, pulled from the two state pools
and **excluding anything already in the `local baseline` plan** (which blankets the
WNC mountains). Picks spread west→east across the regions the baseline *doesn't*
cover (foothills → Charlotte → Triad → Triangle → Sandhills → eastern → coast → OBX).

| Slots | Service | Source | Contents |
|------:|---------|--------|----------|
| 60–74 | GMRS (15) | `GMRS GA-IL-…csv` | best-spread open/on-air NC GMRS repeaters; `G…` names (baseline convention). E.g. Newland/Grandfather Mtn, Gastonia, Greensboro, Raleigh, Greenville, Buxton. |
| 160–174 | Ham (15) | `GA-IL-…VA.csv` | highest-scoring NC ham repeaters by region; keeps the `NC Sxx \| caps \| tinyurl` comment. E.g. McCain S12, Raleigh S11, Charlotte, Winston-Salem, Wilmington, Kill Devil Hills, Ocracoke. |

Slot ranges follow the owner's split (GMRS ≤ 99, ham ≥ 100). Selection favored
geographic spread + (for ham) score and wide-area/linked flags. GMRS rows share the
8 standard GMRS channel freqs with baseline GMRS by nature, but are distinct
repeaters (different town/tone). Building block — renumber when merging into a plan.

---

## `CHIRP Lists/` — baseline-block building lists (Profile A, added 2026-07-01)

Four sourced CHIRP Lists that decompose `local baseline.csv` into reusable,
provenance-backed blocks (each channel traces to a `References/` doc). Together with
`Simplex - 2m and 70cm.csv` (ham simplex 102–109) they let the baseline be
reconstituted purely by pulling from lists. Slots match the baseline's block scheme.

| File | Slots | Ch. | Source (`References/`) |
|------|------:|----:|------------------------|
| `GMRS and MURS.csv` | 1–30, 81–85 | 35 | `FCC GMRS Channel Plan.txt`, `FCC MURS Channel Plan.txt` |
| `local gmrs repeaters.csv` | 31–47 | 17 | `Local GMRS Repeaters.txt` + `RB - GMRS/…` + `Baofeng_5R_MINI_WNC_PUBLIC.csv` |
| `local WNC ham.csv` | 110–131 | 22 | `WCARS Repeater List.txt` + `RepeaterBook WNC Ham Tones.txt` + `Baofeng_5R_MINI_WNC_PUBLIC.csv` |
| `NOAA weather.csv` | 91–97 | 7 | `NOAA Weather Radio Channels.txt` |

- **`GMRS and MURS.csv`** — the 22 FCC GMRS channels (1–7 462-interstitial `FM`; 8–14
  467 low-power `NFM`/`2.0W`; 15–22 462-main `FM`), the 8 generic repeater channels
  (`GMRS15R`–`22R`, `+5 MHz`, `TSQL 141.3` travel tone — a *convention*, see the GMRS
  reference), and the 5 MURS channels (151.8xx `NFM`, 154.57/.60 `FM`). Reproduces the
  baseline values verbatim. **Reg note:** house power is `10W`; FCC ceilings are 5 W
  (GMRS 1–7), 0.5 W (8–14), 2 W (MURS) — recorded in the reference docs, not enforced
  in the CSV (power is set per radio).
- **`local gmrs repeaters.csv`** — 17 local WNC GMRS repeaters (added `GClyde`
  462.625/94.8 at slot 47 on 2026-07-01, sourced from the WNC-RP codeplug), each tone cross-
  checked against RepeaterBook NC and/or the WNC Radio Project list (`Comment` names the
  site + source). `GSpiveyM` is `Tone` (encode-only) 141.3 here, not `TSQL` —
  RepeaterBook, the GMRS pool, and the WNC-GMRS list all show Spivey broadcasts no
  output tone, so TSQL would mute RX. The baseline was corrected to match (2026-07-01).
  See [`open-questions.md`](open-questions.md) #7.
- **`local WNC ham.csv`** — 22 local WNC 2 m/70 cm repeaters (added `SpiveyU` 442.650
  70cm `Tone` 100.0 at slot 131 on 2026-07-01, from the WNC-RP codeplug), mapped to WCARS by
  call sign + site (`Comment`). **Tone modes reference-verified against RepeaterBook
  uplink/downlink (2026-07-01) — see `References/RepeaterBook WNC Ham Tones.txt`.**
  WCARS only lists the *access* (uplink) tone, which can't justify `TSQL` (that needs a
  matching *output* tone). RepeaterBook shows these repeaters transmit **no** matching
  output tone (downlink blank / CSQ / mismatched), so all 11 toned repeaters are
  **`Tone` (encode-only)**: key with the access tone, carrier RX so they're never
  missed. (Ham outputs are unique frequencies, so carrier RX has no source-confusion
  downside.) The other 10 have no access tone in WCARS → carrier. **Flag:** `CashrsV`
  tone conflicts between sources (RB 151.4 in+out vs WCARS 100.0) — noted in-row for
  owner verification.
- **`NOAA weather.csv`** — the 7 NWR frequencies (RX-only, `Duplex=off`); `WX1AVL`
  (162.400) is the local Asheville station WXL56 (Mt. Pisgah).

---

## `CHIRP Lists/KY route gap-fillers (RepeaterBook).csv` — 3 channels (Profile A)

Added 2026-07-13. The route repeaters on the AVL→KY corridor that **exist in no pool** —
sourced individually from RepeaterBook detail pages and recorded in
`References/RepeaterBook - KY route gap-fillers.txt`. Pulled into `AVL to KY.csv`.

| Slot | Name | Freq | Tone | Site |
|-----:|------|------|------|------|
| 150 | `NewprtTN` | 147.090 (+0.6) | `Tone` 203.5 | Newport TN KG4LHC — the AVL→Knoxville trunk |
| 151 | `CarthgV` | 145.250 (−0.6) | `Tone` 114.8 | Carthage TN KJ4EVS — I-40, Smith Co (the "no repeater in the pools" gap) |
| 152 | `WoodbryV` | 146.910 (−0.6) | `Tone` 114.8 | Woodbury TN W4YXA, Short Mtn — wide site covering Cookeville→Nashville |

All three are **encode-only `Tone`**: RepeaterBook lists an uplink (access) tone but no
downlink tone, which can't justify `TSQL` — so they key on the access tone and RX stays
carrier, never muted. (Same standard as the WNC ham audit.)

**Why this list exists:** `NewprtTN` had previously been pulled from the References doc
*straight into the plan*, skipping the CHIRP-List tier. This list closes that provenance
gap and gives the two new repeaters a proper home.

⚠️ **`WoodbryV` 146.910 collides with baseline `SpiveyV`** (W4MOE Spivey Mtn, tone 91.5) —
same frequency, different tone and region. Both are kept as separate channels; this is
deliberate, like the shared GMRS outputs.

---

## `CHIRP Lists/` — KY destination lists (Profile A, added 2026-07-01)

Two reusable destination blocks for KY family trips, sourced from the club reference
docs (analog-FM-usable repeaters only). Pulled into `Complete Radio Plans/AVL to KY.csv`.

- **`KY Somerset (LCARA).csv`** (5) — `SomrstV` 146.880 (`TSQL` 77.0, pool-confirmed;
  remote-RX sites use 179.9/136.5/110.9), `SomrstU` 443.600 (`Tone` 100.0), `MontcloV`
  145.150 (`Tone` 77.0), + Somerset/Monticello club simplex. Source:
  `References/Lake Cumberland ARC Repeaters (Somerset KY).txt`.
- **`KY Bowling Green (KCARC).csv`** (11) — BG (`BGrn330`/`BGrn165`/`BGrn444`),
  Morgantown, Franklin, Glasgow ×3, Bonnieville ×2, Cane Valley. Club PLs as encode-only
  `Tone` (or carrier where "no tone"). Source:
  `References/Kentucky Colonels ARC Repeaters (Bowling Green KY).txt`. **Flag:** `MorgtnV`
  KCARC "no tone" vs pool TSQL 100.0 → encoded 100.0.

---

## `CHIRP Lists/` — local monitoring channel sets (Profile A)

Curated RX-focused channel lists for the Asheville area, split by purpose. These
are **listen-only / monitoring** sets (mostly `Duplex=off`) used as building blocks
to drop into a Complete Radio Plans codeplug. They were split out of a single combined
"Airport and Emergency" export; each keeps its original `Location` numbers (in the
140–195 range as exported — **not yet** renumbered to the listen-only ≤ 99 slot
rule; do that when pulling into a Complete Radio Plans file).

| File | Slots | Ch. | Contents |
|------|------:|----:|----------|
| `CLT Airport.csv` | 140–149 | 10 | Charlotte (KCLT) airband — approach/departure sectors, tower. `AM` mode, VHF airband (118–136 MHz). |
| `AVL Airport.csv` | 150–158 | 9 | Asheville (KAVL) airband — tower/CTAF, ground, approach/dep (incl. **three** UHF aero `…U` 257.8/269.575/351.8 MHz), UNICOM, ATIS. `AM` mode. |
| `Local Emergency.csv` | 160–180 | 21 | Buncombe County public safety — EMS, fire dispatch/comm/paging/fireground, VFD repeaters (Fairview/Reynolds/Riceville/Skyland), state fire/EMS, SAR common, schools. `NFM`, carrier (RX-only monitoring). All 21 verified against RadioReference — see `References/Buncombe County Public-Safety Frequencies.txt`. |
| `CMC.csv` | 191–195 | 5 | CMC-SAR / interop — CMCSAR1-3 (CMC ops, `FM`), VSAR16 (National Interop SAR, `NFM`), UTAC41D (UHF interop TAC Direct, `NFM`). All simplex; carrier (no tone). Verified against the CMC radio ops manual + NIFOG; see `References/SAR and Interop Frequencies.txt`. |

> Airband is **AM** and includes UHF aero (250–352 MHz) — only some radios RX these.
> Per-radio (resolved, see [`radios.md`](radios.md)): **TD-H8** = airband + most mil
> (verify 257.8/269.575); **TD-H9** & **UV-5R Mini** = airband + 351.8 only;
> **UV-5G Plus** & **AR-5** = neither.

---

## `CHIRP Lists/Simplex - 2m and 70cm.csv` — 22 channels (Profile A)

A clean, ready-to-pull building block: the **two national FM calling freqs** plus
**10 best 2 m + 10 best 70 cm FM simplex channels** (slots 100–121, ham range).
The calling freqs were **added at slots 100/101 (2026-07-01)** to match the baseline's
slotting; the other 20 rows are *additional* simplex options to have at the ready.

| Slots | Band | Channels |
|------:|------|----------|
| 100 | 70 cm | `70cmCall` 446.000 — national 70 cm FM calling (`10W`) |
| 101 | 2 m | `2mCall` 146.520 — national 2 m FM calling (`10W`) |
| 102–111 | 2 m | `2mSim1`–`2mSim10`: 146.535/.550/.565/.580/.595, 147.525/.540/.555/.570/.585 |
| 112–121 | 70 cm | `70cSim1`–`70cSim10`: 445.925/.950/.975, 446.025/.050/.075/.100/.125/.150/.175 |

Selection rules (so a future AI can extend it consistently):
- **2 m:** only SERA FM-voice simplex from the **non-`*`** sub-bands (146.520–146.595
  and 147.510–147.585). The `*`-marked channels (146.4xx / 147.4xx) were avoided
  because SERA also allows them as repeater inputs in some areas. `147.510` was
  additionally skipped (a distant Rockingham NC repeater uses it as an output).
- **70 cm:** SERA FM simplex sub-band **445.9125–446.1750**, picked on a **25 kHz
  grid** (every other 12.5 kHz channel) for clean wideband-FM spacing.
- **Every frequency was cross-checked against all local repeater/channel CSVs — no
  conflicts.** `Tone` left off (carrier squelch); `FM`; `5.0W` (bump per radio).

---

## `References/` — reference material

External reference material the owner collects (mostly docs; also raw source data).
Not loaded on a radio as-is; used to decode data, validate/label channels, and as
the source behind built CHIRP Lists.

- **`repeater-scores.app - Scoring Explained.txt`** — decodes the
  `STATE/<score><XCWN>` badge in the scored CHIRP List(s). See
  [`file-format.md`](file-format.md#the-comment-metadata-code-profile-b).
- **`WCARS Repeater List.txt`** — Western Carolina Amateur Radio Society **ham**
  repeater list (28 repeaters) for the owner's home region: Buncombe, Haywood,
  Henderson, Macon, Mitchell, Transylvania, Yancey, Madison, Jackson counties.
  Aligned table of Output / Input / Tone In (PL) / Call Sign / Description / County,
  covering 6 m, 2 m, 1.25 m, and 70 cm. Many already appear in the Complete Radio
  Plans; a good source for building/validating a local-repeater CHIRP List.
- **`Baofeng_5R_MINI_WNC_PUBLIC.csv`** — the **WNC Radio Project's own public codeplug**
  (Baofeng UV-5R Mini) — an authoritative *operator* source for the local GMRS repeaters.
  Confirms the tone MODE per service: **all local GMRS repeaters `TSQL`** (they broadcast
  their PL) vs **local ham repeaters `Tone`/encode-only** — corroborating both the GMRS
  list and the ham audit. (Uses CHIRP's `TSQL` convention of tone in `cToneFreq` with
  `rToneFreq=88.5`; this repo keeps the more foolproof `rToneFreq==cToneFreq`.) Also names
  "Big Willow" (=`GDavisMt`) and "Echo Lake" (=`GEchoMtn`), and carries a `Clyde`
  462.625/94.8 and a Spivey 442.650 70cm ham not yet in our lists. Added 2026-07-01.
- **`RepeaterBook WNC Ham Tones.txt`** — per-repeater **uplink vs downlink** tone check
  (from RepeaterBook detail pages) for the local WNC ham repeaters, resolving the
  `TSQL`-vs-`Tone` question that WCARS (uplink only) can't. Source-of-record for the tone
  modes in `CHIRP Lists/local WNC ham.csv`. Added 2026-07-01.
- **`Local GMRS Repeaters.txt`** — local **GMRS** repeater list (14 repeaters; WNC
  Radio Project + others) for the Asheville area. Output / +5 MHz offset / CTCSS /
  weekly net / managing group. These correspond to the named `G…` GMRS repeaters in
  the Complete Radio Plans baseline.
- **`FCC GMRS Channel Plan.txt`** — the 30 GMRS channels (22 simplex + 8 repeater
  pairs) with frequencies, offsets, power/bandwidth limits per 47 CFR Part 95 Subpart E,
  plus the 141.3 Hz "travel tone" convention (with sources). Source-of-record for the
  GMRS side of `CHIRP Lists/GMRS and MURS.csv`. Added 2026-07-01.
- **`FCC MURS Channel Plan.txt`** — the 5 MURS channels (151.820/.880/.940 narrowband,
  154.570/.600 wide) with the 2 W / bandwidth limits per 47 CFR Part 95 Subpart J.
  Source-of-record for the MURS side of `CHIRP Lists/GMRS and MURS.csv`. Added 2026-07-01.
- **`NOAA Weather Radio Channels.txt`** — the 7 NWR frequencies (162.400–162.550, RX-
  only) and the local Asheville station (WXL56, 162.400, Mt. Pisgah). Source-of-record
  for `CHIRP Lists/NOAA weather.csv`. Added 2026-07-01.
- **`RepeaterBook - KY route gap-fillers.txt`** — RB-sourced route repeaters not in the
  scored pools: `NewprtTN` KG4LHC 147.09 (the priority AVL→Knoxville trunk), plus
  **Carthage KJ4EVS 145.250 and Woodbury/Short Mtn W4YXA 146.910** (added 2026-07-13,
  with the off-air Carthage 146.730 flagged do-not-program and the 146.910-vs-`SpiveyV`
  frequency collision noted). Notes that the pool's "Newport" is coastal NC.
  Source-of-record for `CHIRP Lists/KY route gap-fillers (RepeaterBook).csv`.
  Added 2026-07-01.
- **`Lake Cumberland ARC Repeaters (Somerset KY).txt`** — **ham** repeaters for the
  owner's **Somerset / Monticello, KY** family-visit area (LCARA). Analog + digital
  (DMR/D-Star/Fusion) across 2 m / 70 cm / 6 m / 10 m, plus club simplex. Includes a
  note on which are usable on the analog-only fleet (146.880, 443.600, 145.150 + the
  146.580/147.570 simplex).
- **`Kentucky Colonels ARC Repeaters (Bowling Green KY).txt`** — **ham** repeaters for
  the owner's **Bowling Green, KY** family-visit area (KY4BG/KCARC, "partial" club
  list). Covers BG + Morgantown/Franklin/Glasgow/Bonnieville/Cane Valley; analog +
  digital (P25/DMR/D-Star/Fusion). Includes a note on the analog-FM-usable subset.
- **`Airport Frequencies (KCLT, KAVL).txt`** — verified ATC frequency reference for
  Charlotte (KCLT) and Asheville (KAVL): tower / ground / approach-departure sectors,
  ATIS, UNICOM, UHF-mil — with sources (FAA Chart Supplement via AirNav; CLT ATCT SOP).
  Source-of-record for `CHIRP Lists/CLT Airport.csv` and `AVL Airport.csv`.
- **`SAR and Interop Frequencies.txt`** — verified CMC-SAR / interop channel set
  (CMCSAR1-3, VSAR16, UTAC41D) sourced to the CMC radio ops manual + NIFOG, including
  the UTAC41D band-plan override (453.4625, not the manual's .4525) and the mode/tone
  rationale. Source-of-record for `CHIRP Lists/CMC.csv`.
- **`Radio operations manual.docx.pdf`** — the CMC-SAR Baofeng radio operations
  manual: definitive source for the CMC channel set (CMCSAR1-3, VSAR16, UTAC41D),
  naming, and operating practice (carrier squelch, wide FM, UTAC41D TX discipline).
- **`SERA FM Simplex Channels (2m, 70cm).txt`** — the SERA-coordinated FM voice
  simplex sub-bands and channel lists (extracted from `SERA/sera-fup-144.pdf` &
  `sera-fup-440.pdf`). Source-of-record for `CHIRP Lists/Simplex - 2m and 70cm.csv`
  (the 20 simplex channels verified against it 2026-06-29; the two national calling
  freqs at slots 100/101 added 2026-07-01, also SERA-listed).
- **`Buncombe County, North Carolina (NC) Scanner Frequencies and Radio Frequency
  Reference.pdf`** — RadioReference Buncombe County database export (updated
  2026-06-18): the full county conventional + trunked listing. Raw source behind the
  Local Emergency list.
- **`Buncombe County Public-Safety Frequencies.txt`** — the verified subset actually
  used: maps each `Local Emergency.csv` channel to its RR frequency / tone / license /
  description, and notes it's a deliberate Fairview-area subset. Source-of-record for
  `CHIRP Lists/Local Emergency.csv` (all 21 channels verified against RR 2026-06-29).
- **`CHIRP CSV Format and Settings.txt`** — definitive reference for the CHIRP CSV
  column layout and how to set every field, with the full Tone / TSQL / DTCS / Cross
  SOP (compiled from CHIRP's official docs). The format authority behind every CSV here.
- **`CHIRP Tone Programming Examples (CHIRP official).pdf`** — the official CHIRP
  document of 17 worked TX/RX tone scenarios (CSQ / CTCSS / DCS / split-tone). Source
  for the tone-mode SOP.

### `References/RB - GMRS/` — raw RepeaterBook GMRS exports

9 per-state RepeaterBook **CHIRP-format** GMRS exports (one per state, `rb_chirp_*.csv`).
The **source** the `CHIRP Lists/GMRS …csv` list was *not* built from (these lack
Use/Status fields); kept as raw provenance. The cleaned/filtered list came from the
RepeaterBook web data instead. Don't load these directly.

### `References/SERA/` — SERA band plans

SERA (**Southeastern Repeater Association**) is the volunteer frequency coordinator
for GA, KY, MS, NC, SC, TN, VA, and (most of) WV — i.e. the owner's region. These
are SERA's **Frequency Utilization Plans (FUPs)**: per-band maps of where
coordinated repeater inputs/outputs, simplex, link/control, and digital channels
live. Useful for sanity-checking offsets/splits and picking simplex frequencies
(supports SOP 4 validation).

| File | Band | Covers |
|------|------|--------|
| `sera-fup-29.pdf` | 29 MHz (10 m) | 4 repeater pairs, simplex, OSCAR |
| `sera-fup-50.pdf` | 50–54 MHz (6 m) | FM repeater pairs (1 MHz & 500 kHz splits), simplex, digital |
| `sera-fup-144.pdf` | 144–148 MHz (2 m) | FM voice simplex, repeater sub-band pairs (144.510/145.450 NB, 144.520/145.460 wide-offset), digital-only pairs, digital simplex, standard 146–148 repeater band. **Most relevant band for this fleet.** |
| `sera-fup-220.pdf` | 220 MHz (1.25 m) | FM repeater pairs (1.6 MHz split), control/link, simplex, digital |
| `sera-fup-440.pdf` | 420–450 MHz (70 cm) | repeater pairs (NBD/WBD/WBA), itinerant, non-coordinated "backyard", hotspots, simplex, links, ATV |
| `sera-fup-900.pdf` | 902–928 MHz (33 cm) | repeater pairs (incl. Part-15 mitigation alternates), links, simplex |
| `sera-fup-1200.pdf` | 1240–1300 MHz (23 cm) | FM repeater pairs (25 kHz, 12 MHz split) |
| `SERA-CPG-Rev-06-09-2024.pdf` | — | Coordination Policy & Guidelines (rev 2024-06-09): how coordination works, owner/trustee duties, band allocations |

All eight bands present and correct as of 2026-06-25 (an earlier copy of the 2 m
file was a mislabeled duplicate of the 220 plan; re-downloaded and verified).

---

## `IMG Files/` — full radio images built from the CSVs

CHIRP **native radio images** (`.img`) — the finished binary artifact uploaded to a
radio. Each is built by importing a Complete Radio Plan CSV into CHIRP under the
correct radio model and saving the radio image. **Outputs, not sources:** the CSV
remains the editable source of truth; if a plan changes, regenerate the `.img` rather
than hand-editing (an `.img` is model-specific binary, not text-editable).

**Naming:** `<Radio> - <Plan>.img` — the radio model it's for, then the plan it was
built from. (CHIRP's own save-dialog default is `<Radio>_<Model>_<YYYYMMDD>.img`, which
names the radio but not the plan — rename to the convention above when filing one.)

| File | Radio | Built from |
|------|-------|------------|
| `Baofeng_UV-5R Mini_20260710.img` | Baofeng UV-5R Mini | `Extended Baseline (skip all but local).csv` (downloaded from the radio 2026-07-10; also contains 11 leftover repeaters at slots 989–999 from an earlier trip that are **not** in the CSV — see that plan's entry above) |

---

## Relationships

```
References/  (source-of-record — the authoritative source behind every list)
  SERA band plans, repeater-scores.app, WCARS / Local-GMRS / KY club lists,
  Airport Frequencies (KCLT/KAVL), SAR & Interop Frequencies, RB - GMRS exports
      │
      │  every CHIRP List channel must trace to a source here
      ▼
CHIRP Lists/  (building blocks)
  GA-IL-...-VA.csv (ham pool), GMRS GA-IL-...csv (GMRS pool),
  NC Coverage, Simplex, Airport/Emergency/CMC monitoring sets
      │
      │  combine + normalize to LCD rules (≤200 ch, ≤8-char names,
      │  ham ≥100 / GMRS ≤99); convert Profile B → A as needed; pull ONLY from lists
      ▼
Complete Radio Plans/  (finished codeplugs to flash whole)
  universal / LCD (load on the whole fleet, ≤200 ch):
      local baseline.csv                          — everyday WNC plan (91)
      Extended Baseline.csv                       — + statewide NC & border metros (157)
      Extended Baseline (skip all but local).csv  — same channels, local-only scan (157)
      AVL to KY.csv                               — baseline + KY trip route (143)
  radio-specific:
      Arcshell ... on 8.csv                       — AR-5-specific (16-ch, GMRS)
      │
      │  ── on the 999-channel radios only, a supplement loads on TOP of a
      │     universal plan, filling memory above slot 200:
      │        Scan Channels (201+).csv           — emergency + airport monitoring (40)
      │
      │  import into CHIRP under the radio model, save the image
      ▼
IMG Files/*.img  (binary radio images)
      Baofeng_UV-5R Mini_20260710.img
```
