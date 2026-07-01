# Open Questions

> **Last updated:** 2026-07-01
> Things inferred but not confirmed by the owner. A future AI should resolve these
> with the owner and then fold the answer into the relevant note file (and delete
> the question here).

> **RESOLVED (2026-06-25):**
> - Q1/Q2/Q3 — score/flag system + link source: documented in
>   `References/repeater-scores.app - Scoring Explained.txt` and [`file-format.md`](file-format.md).
> - Q4 — the `*` (`GMRS20R*`): marks the **national GMRS travel channel** (462.675 /
>   141.3). Folded into [`conventions.md`](conventions.md) naming conventions.
> - Q5 — radio variants: **TD-H9 & TD-H8 are "Normal" mode = ham + GMRS** (not
>   locked); UV-5R mini = ham, UV-5G Plus = GMRS, AR-5 = special case. See
>   [`radios.md`](radios.md).
> - Q5b — capacities: TD-H9/H8 = **200**, UV-5R mini & UV-5G Plus = **999**,
>   AR-5 = **16** (special case). The 200-channel cap is the TD limit; owner keeps
>   all multi-radio plans ≤ 200. See [`radios.md`](radios.md) / [`conventions.md`](conventions.md).
> - Q5c — airband (AM) / UHF-mil RX (for the airport files), per radio — see
>   [`radios.md`](radios.md) "Per-radio details":
>     - **TD-H8:** airband yes; mil-UHF per spec covers 257.8/269.575/351.8 but a
>       second source disagrees → **verify 257.8/269.575 on the radio**. Most capable.
>     - **TD-H9:** airband yes; mil-UHF 350–390 only (AVL 351.8 yes; 257.8/269.575 no).
>     - **UV-5R Mini:** airband yes; mil-UHF 350–390 only (351.8 yes; 257/269 no).
>     - **UV-5G Plus:** no airband, no mil.
>     - **AR-5:** no — UHF-only 406.1–470 (no airband, no mil, no VHF).
> - Q7 — `local baseline.csv` is the owner's first plan but **just one of many**
>   Complete Radio Plans, **not** a propagating master. See [`inventory.md`](inventory.md).

## 6. Per-radio `Power` level strings  *(still open — revisit)*
`10W`/`2.0W`/`6.0W` are used in Profile A. **Confirm these import cleanly on each
radio**, or note the level strings each model expects, so pulls can target the
right values.
- Data point: **UV-5R Mini = High / Low** (5 W / 2 W) — uses named levels, not
  wattage strings, so a `10W` value would just clamp to High.
- Data point: **TD-H8 = 10 W**, **TD-H9 = 10 W** (TID radios are 10 W class). Exact
  CHIRP level labels (High/Mid/Low vs wattage) TBC.
- UV-5G Plus = 5 W GMRS. AR-5 = vendor doesn't publish wattage (codeplug uses 5.0W).
- Still open: the exact CHIRP **label strings** each radio expects (High/Mid/Low vs
  wattage). Verify in CHIRP when convenient.

## 7. Provenance backfill — existing files predate the sourcing standard  *(open — cleanup roadmap)*
The provenance standard (`References/` → `CHIRP Lists/` → `Complete Radio Plans/`; see
[`conventions.md`](conventions.md)) is now the rule, but the **existing files predate
it** and don't all comply yet:
- ✅ **CHIRP Lists are now fully sourced (2026-06-29):** airport (FAA Chart Supplement
  via AirNav + CLT ATCT SOP), CMC (CMC radio ops manual + NIFOG), Simplex (SERA FUPs),
  Local Emergency (RadioReference Buncombe), NC Coverage (derived from the two pools),
  and the two pools self-sourced (ham = repeater-scores.app download; GMRS = RepeaterBook).
- 🟨 **`local baseline.csv` backfill — mostly done (2026-07-01).** New sourced CHIRP
  Lists now cover the previously-unsourced baseline blocks:
  - `CHIRP Lists/GMRS and MURS.csv` — GMRS simplex 1–22 + generic repeaters 23–30 +
    MURS 81–85. Source: new `References/FCC GMRS Channel Plan.txt` and
    `References/FCC MURS Channel Plan.txt`.
  - `CHIRP Lists/local gmrs repeaters.csv` — local WNC GMRS 31–46. Source:
    `References/Local GMRS Repeaters.txt` + `References/RB - GMRS/rb_chirp_2606251318.csv`
    (NC), cross-referenced.
  - `CHIRP Lists/local WNC ham.csv` — local WNC ham 110–130. Source:
    `References/WCARS Repeater List.txt`.
  - `CHIRP Lists/NOAA weather.csv` — WX 91–97. Source: new
    `References/NOAA Weather Radio Channels.txt`.
  - **Ham simplex + calling now covered too (2026-07-01):** the two national calling
    freqs (446.000/146.520) were added to `CHIRP Lists/Simplex - 2m and 70cm.csv` at
    slots 100/101 (matching the baseline), and the ham-simplex block (baseline 102–109)
    is a subset of that list. **The baseline is now fully reconstructible from CHIRP
    Lists** — no baseline row lacks a backing list.
  - ✅ **Spivey fix applied (2026-07-01):** `GSpiveyM` (Spivey Mtn GMRS, 462.725) is
    **encode-only** per three sources (RepeaterBook NC export, the GMRS pool, and the
    WNC-GMRS list). It was `TSQL 141.3` in the baseline — which mutes RX so Spivey
    couldn't be heard. **Fixed to `Tone` 141.3 in `local baseline.csv` slot 32** and in
    `local gmrs repeaters.csv`. (Owner rule: TSQL when the repeater broadcasts a tone;
    `Tone` (encode-only) when it doesn't, so comms are never missed.)
  - ✅ **Ham tone-mode audit (`local WNC ham.csv` + baseline 112–130, 2026-07-01):**
    all toned local ham repeaters verified against **RepeaterBook uplink/downlink** (see
    `References/RepeaterBook WNC Ham Tones.txt`). WCARS lists only the *access* (uplink)
    tone, which can't justify `TSQL`; RepeaterBook shows these repeaters transmit **no**
    matching output tone (downlink blank / CSQ / mismatched). So all 11 were set to
    **`Tone`** (encode-only) — key with the access tone, carrier RX so never missed
    (ham outputs are unique freqs → no source-confusion downside). Applied to both the
    list and the baseline.
    - ⚠️ **`CashrsV` conflict (open):** RepeaterBook shows 151.4 (in+out) for KD4CED
      145.350; WCARS lists 100.0. List/baseline encode RB's 151.4; **owner to confirm**
      the correct access tone. (RX is carrier either way, so the repeater is heard.)
  - ✅ **GMRS local repeaters — output tone RESOLVED (2026-07-01):** the WNC Radio
    Project's own codeplug (`References/Baofeng_5R_MINI_WNC_PUBLIC.csv`) programs **all**
    local GMRS repeaters as `TSQL` (and its ham repeaters as `Tone`), an authoritative
    operator source. `GEchoMtn`/`GFlatTop` are WNC-RP's own repeaters → `TSQL` confirmed;
    `GPisgahF`/`GSwannan`/`GWeaverv` are `TSQL` in their codeplug with no contradicting
    reference → kept `TSQL`. No change needed (they were already `TSQL`).
  - ⚠️ **`GSpiveyM` GMRS mode conflict (open):** the WNC-RP codeplug uses `TSQL` 141.3,
    but RepeaterBook's GMRS export explicitly marks Spivey `Tone` (encode-only) while
    marking its neighbors `TSQL` — i.e. RB has specific data that Spivey is encode-only,
    whereas WNC-RP set *all* GMRS to `TSQL` uniformly (and doesn't operate Spivey). Kept
    `Tone` (never-miss). **Owner to decide** if they'd rather trust WNC-RP and use `TSQL`
    for source-ID on the shared 462.725 channel.
  - ✅ **New items from the WNC-RP codeplug added (2026-07-01, owner-approved):**
    (a) `GClyde` 462.625/94.8 `TSQL` re-added to `local gmrs repeaters.csv` (slot 47);
    (b) `SpiveyU` 442.650 70cm `Tone` 100.0 added to `local WNC ham.csv` (slot 131);
    (c) name aliases "Big Willow"=`GDavisMt`, "Echo Lake"=`GEchoMtn` kept as-is, noted
    in-row. **These are in the building-block LISTS only — not yet in `local baseline.csv`**
    (GClyde was previously a baseline channel; pending owner decision on baseline adds).
This is the multi-step cleanup the owner is working through (2026-06 → 2026-07).
