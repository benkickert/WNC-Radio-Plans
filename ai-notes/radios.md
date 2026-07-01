# Hardware — The Radio Fleet

> **Last updated:** 2026-06-25
> The radios these CSVs are built for, and how they map to the files.

## Owner location

**Fairview, NC** (just southeast of Asheville, in the mountains of Western North
Carolina / Buncombe County). This anchors the "local" / "AVL" scope: the baseline
and the home end of the AVL→ATL corridor are centered here. Terrain is
mountainous, so line-of-sight to repeaters varies a lot by site.

## Why "lowest common denominator" (LCD)

The owner standardizes codeplugs so one file works across the fleet. Two hard rules
(see [`conventions.md`](conventions.md)):

- **`Name` ≤ 8 characters**
- **≤ 200 channels per codeplug**

The **200-channel cap comes from the TID radios** (TD-H9 / TD-H8 hold 200). The
UV-5R mini and UV-5G Plus actually hold **999**, but the owner keeps every
multi-radio plan to ≤ 200 for cross-radio consistency. The **Arcshell AR-5 is a
16-channel special case** — it gets its own tiny dedicated codeplug, so the 200 rule
doesn't apply to it.

## The radios (all programmed via CHIRP / CSV)

| Radio | TX capability | Memory | Notes |
|-------|---------------|-------:|-------|
| **TID TD-H9** | **Ham + GMRS** ("Normal"/Unlocked), 10 W | 200 | Adds 1.25 m (220 MHz) TX, APRS/GPS. RX incl. AM airband; mil-UHF 350–390 only. See details below. |
| **TID TD-H8** | **Ham + GMRS** ("Normal"/Unlocked mode), 10 W | 200 | 8-band; RX AM airband + mil-UHF (per spec; see caveat). Most capable airport-file radio. See details below. |
| **Baofeng UV-5R mini** | Ham (open dual-band), 5/2 W | 999 | UV-5R-family driver in CHIRP. Wide RX incl. AM airband. See details below. |
| **Arcshell AR-5** | 16-ch **UHF-only** (406.1–470 MHz) | **16** | **Special case.** Rotary-knob, no display → `Name` blank; its codeplug (`Complete Radio Plans/Arcshell with Fletcher on 8.csv`) is GMRS-simplex. No VHF/airband/mil. See details below. |
| **Baofeng UV-5G Plus** | **GMRS** (GMRS-9 family) | 999 | GMRS TX only; RX 136–174 & 400–520 (gets 2m/70cm ham + NOAA, *not* airband/mil). See details below. |

"Normal" mode on the TD radios means they transmit on **both ham and GMRS** — they
are *not* GMRS-locked, so they take any plan.

## Per-radio details

Codeplug-relevant specs as confirmed (distilled from spec sheets; ignores
battery/antenna/marketing).

### Baofeng UV-5G Plus
- **CHIRP model:** select **"UV-5G Plus"** on import.
- **TX:** GMRS only, **5 W** (GMRS-licensed). Not for ham/VHF/UHF TX.
- **Memory:** **999 channels.** CH **1–30 are preset GMRS** (22 channels + 8 repeater
  pairs); CH **31–999 are freely programmable** for GMRS/VHF/UHF (subject to the
  GMRS-only TX lock — extra freqs are usable for **RX/scan**).
- **RX (scan) range:** 136–173.99 & 400–519.99 MHz. → **can receive** 2 m (144–148)
  and 70 cm (420–450) ham and **NOAA weather**; also FM broadcast 76–108. So it can
  **monitor ham repeaters** even though it can't TX on them. **Cannot receive** VHF
  airband (118–136 AM) or UHF-mil (225–400) — relevant to the airport files (see
  [`open-questions.md`](open-questions.md) 5c). 999-ch memory holds any ≤ 200 plan.

### Baofeng UV-5R Mini  (a.k.a. GT-5R Mini)
- **CHIRP model:** UV-5R-family driver (also BT app "OLA Radio"; CPS/keypad).
- **TX:** ham, dual-band — VHF 136–174 & UHF 400–480 MHz. **Power 5 / 2 W = High / Low**
  (so its CHIRP power levels are **High/Low**, not wattage strings — relevant to
  [`open-questions.md`](open-questions.md) 6).
- **Memory:** **999 channels.**
- **RX (scan) range:** FM 76–108, **Airband 108–136 (AM)**, VHF 136–174, UHF
  **350–390** & 400–520, NOAA. → **Can receive the airport AM airband files** (the
  CLT/AVL VHF airband) and **partial UHF-mil** (350–390 only: AVL `351.800` yes, but
  `257.800`/`269.575` no). NOAA RX only (no auto weather-alert).
- **Use in plans:** full ham + GMRS analog + airband/airport monitoring.

### TID TD-H8 (3rd Gen)
- **CHIRP model:** TD-H8 (also ODmaster BT app, web programmer, CPS).
- **Modes:** Ham / GMRS / **Normal (Unlocked)** — owner runs **Normal** (ham + GMRS TX).
- **TX:** VHF 136–174 & UHF 400–470 MHz. **10 W** high power.
- **Memory:** **200 channels** (owner-confirmed).
- **RX (scan) range:** AM **108–136 (airband)**; FM 50–76 & 76–108; VHF 136–174;
  UHF 400–520; **NOAA (with weather alerts)**. The TD-H8 product spec also lists
  VHF **174–350** & UHF **350–400** RX (which would cover the AVL mil freqs
  `257.800`/`269.575`/`351.800`), **but** the TD-H9 page's comparison grid shows the
  TD-H8 with only `220–230` + `350–390` RX. → Airband + `351.800` are solid; treat
  **`257.800`/`269.575` RX as claimed-but-unverified — confirm on the radio.**
  Still the most capable airport-file radio in the fleet.
- **Use in plans:** everything — full ham + GMRS + airband + mil-UHF monitoring.

### TID TD-H9
- **CHIRP model:** TD-H9 (also ODmaster BT app/web). Adds APRS/GPS, spectrum
  analyzer, SMS — none codeplug-relevant.
- **Modes:** Unlocked **Ham + GMRS** (owner runs Normal). **10 W.**
- **TX:** 136–174, **220–259**, 300–390, 400–590 MHz — notably **can TX 1.25 m
  (220 MHz)**, so it could use the SERA 220 band plan (no codeplug uses 220 yet).
- **Memory:** **200 channels** (owner-confirmed; the "128 MB" in marketing is flash
  storage, not memory-channel count).
- **RX (scan) range:** FM 76–108, **AM 108–136 (airband)**, VHF 136–174, 220–230,
  UHF **350–390**, 400–520, NOAA. → Airband **yes**; mil-UHF **only 350–390** (AVL
  `351.800` yes; `257.800`/`269.575` **no**) — i.e. less mil coverage than the TD-H8.
- Airband AM files work; the AVL mil channels mostly won't (RX-wise).

### Arcshell AR-5
- **16-channel UHF-only handheld**, **406.1–470 MHz** (TX/RX). Covers GMRS (462/467)
  and 70 cm; **no VHF** (no 2 m, no MURS), **no airband, no mil, no NOAA, no FM bcast**.
  FCC 2ARTCARAR (FRS-class).
- **Channel select is a 16-position rotary knob** — no display, no alpha names (that's
  why its codeplug leaves `Name` blank). Voice-prompts the channel number.
- **CHIRP:** has an **"AR-5" model**, but it's a **rebranded BF-888S** (888S-class
  16-ch UHF radio) — *not* a UV-5R. 16-channel ceiling.
- **Power:** vendor doesn't publish wattage; the existing codeplug uses `5.0W`
  (verify the radio's real max / CHIRP label).
- **Special case:** its own 16-channel codeplug
  (`Complete Radio Plans/Arcshell with Fletcher on 8.csv` — GMRS simplex + the
  Fletcher repeater). Exempt from the ≤ 200-channel rule.

## Radio capabilities — reference only (do NOT auto-filter plans)

> **Process rule (owner-set):** **Do not "clean" or tailor a codeplug to the radio it's
> destined for.** Build plans to the standard SOPs (full content per the plan's design).
> The owner decides any radio-specific trimming **on a one-off basis and will ask** for
> it. The capability facts below are reference for answering *those* requests — not a
> cue to pre-filter anything yourself.

The capabilities, for when the owner *does* ask:
- **TD-H9 / TD-H8** (ham + GMRS TX, 200 ch): can use any content.
- **UV-5R mini** (ham + GMRS TX): full analog ham/GMRS; also RX airband.
- **UV-5G Plus** (GMRS TX only, but **RX ham 2 m/70 cm + NOAA**): can *transmit* only on
  GMRS, but can still *monitor* ham repeaters and weather — so ham entries aren't
  useless on it.
- **Arcshell AR-5** (16-ch UHF-only): GMRS/70 cm only; its own dedicated codeplug.

## CHIRP / programming notes

- All five use CHIRP. Each model has its own CHIRP **driver/radio model** — when
  importing a CSV, select the correct model in CHIRP so it maps columns and clamps
  values (power levels, tuning steps, name length) to what that radio supports.
- **`Power` strings must be ones the selected radio recognizes.** `10W`/`2.0W`/
  `6.0W` work for the high-power TID units; lower-power UV-5R-class radios may only
  expose `High`/`Med`/`Low` or different wattages. If a power value is rejected on
  import, adjust it to that radio's available levels.
- **8-char `Name` limit** is safe across this whole fleet — keep it.
- **Narrowband (`NFM`)** required channels (GMRS 8–14, MURS 1–3) are honored by all;
  don't switch them to `FM`.
- The two **CSV profiles** in this folder both import; for any of these radios the
  full Profile A layout is fine. When pulling rows from the lean Profile B pool,
  convert to Profile A (add the missing columns) before loading — see
  [`sops.md`](sops.md).
