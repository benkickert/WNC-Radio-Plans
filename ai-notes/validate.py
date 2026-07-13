#!/usr/bin/env python3
"""SOP 4 validator — run from the repo root:  python ai-notes/validate.py

Checks every Complete Radio Plan and CHIRP List against the rules in conventions.md.
Exits non-zero if anything fails. Read-only; it never edits a CSV.
"""
import csv
import glob
import os
import sys

HAM = lambda f: 144 <= f < 148 or 420 <= f < 450
BANDS = [  # (low, high, label) — frequency sanity per service
    (118, 137, "VHF airband (AM)"), (144, 148, "2 m ham"), (151, 155, "MURS/public-safety VHF"),
    (155, 160, "public-safety VHF"), (162.4, 162.56, "NOAA WX"), (250, 400, "UHF aero/mil"),
    (420, 450, "70 cm ham"), (450, 471, "public-safety UHF / GMRS"),
]


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def check(path, rows, is_plan):
    """Return a list of problem strings for one file."""
    errs = []
    name = os.path.basename(path)
    locs = [int(r["Location"]) for r in rows]

    supplement = min(locs) > 200          # a 201+ add-on for the 999-ch radios
    radio_specific = "Arcshell" in name   # AR-5: 16 ch, blank names, exempt
    pool = len(rows) > 200 and not supplement  # the raw multi-state pools are over-cap by design

    if is_plan:
        if len(rows) > 200 and not supplement:
            errs.append(f"over the 200-channel cap ({len(rows)})")
        if supplement and min(locs) <= 200:
            errs.append("supplement plan has a slot at/below 200 — would collide with a base plan")
    if len(set(locs)) != len(locs):
        dupes = {l for l in locs if locs.count(l) > 1}
        errs.append(f"duplicate Location(s): {sorted(dupes)}")

    for r in rows:
        n, loc, tone = r["Name"], int(r["Location"]), r["Tone"]
        try:
            freq = float(r["Frequency"])
        except ValueError:
            errs.append(f"{loc} {n}: unparseable Frequency {r['Frequency']!r}")
            continue

        if len(n) > 8 and not radio_specific:
            errs.append(f"{loc} {n!r}: Name is {len(n)} chars (max 8)")

        # Slot-100 service split governs a base plan's 1-200 only; not supplements or pools.
        if is_plan and not supplement and not radio_specific:
            if HAM(freq) and loc < 100:
                errs.append(f"{loc} {n}: ham frequency below slot 100")
            if not HAM(freq) and loc >= 100 and not (76 <= freq < 108):
                errs.append(f"{loc} {n}: non-ham frequency at/above slot 100")

        # Tone consistency. NOTE: 88.5 is a REAL tone — only the *split* is the bug.
        # Never flag a set tone mode merely for holding 88.5. See conventions.md.
        if tone == "TSQL" and r["rToneFreq"] != r["cToneFreq"]:
            errs.append(f"{loc} {n}: TSQL with split tones "
                        f"(rTone={r['rToneFreq']} != cTone={r['cToneFreq']}) — "
                        f"CHIRP may TX the wrong tone and fail to key the repeater")
        if tone == "DTCS" and r["DtcsCode"] != r["RxDtcsCode"]:
            errs.append(f"{loc} {n}: DTCS with split codes "
                        f"({r['DtcsCode']} != {r['RxDtcsCode']})")
        if tone == "Cross" and not r["CrossMode"]:
            errs.append(f"{loc} {n}: Tone=Cross but CrossMode is empty")

        # Duplex / offset sanity
        if r["Duplex"] in ("+", "-") and float(r["Offset"] or 0) == 0:
            errs.append(f"{loc} {n}: Duplex {r['Duplex']} with a zero Offset")
        if r["Duplex"] == "" and float(r["Offset"] or 0) != 0:
            errs.append(f"{loc} {n}: simplex (empty Duplex) but Offset is {r['Offset']}")

        # Receive-only content must stay receive-only.
        rx_only = (162.4 <= freq <= 162.56) or (118 <= freq < 137) or (250 <= freq < 400)
        if rx_only and r["Duplex"] != "off":
            errs.append(f"{loc} {n}: {freq} is receive-only (weather/airband/mil) "
                        f"but Duplex is {r['Duplex']!r}, not 'off'")

        if not any(lo <= freq <= hi for lo, hi, _ in BANDS):
            errs.append(f"{loc} {n}: {freq} MHz is outside every expected band")

        for col, val in r.items():
            if col != "Comment" and val and "," in val:
                errs.append(f"{loc} {n}: stray comma in {col} — breaks the CSV")

    return errs


def main():
    files = ([(p, True) for p in sorted(glob.glob("Complete Radio Plans/*.csv"))] +
             [(p, False) for p in sorted(glob.glob("CHIRP Lists/*.csv"))])
    if not files:
        sys.exit("no CSVs found — run this from the repo root")

    failed = 0
    for path, is_plan in files:
        rows = load(path)
        errs = check(path, rows, is_plan)
        label = os.path.basename(path)
        if errs:
            failed += 1
            print(f"\nFAIL  {label}  ({len(rows)} ch)")
            for e in errs:
                print(f"        {e}")
        else:
            print(f"ok    {label}  ({len(rows)} ch)")

    print()
    if failed:
        print(f"{failed} file(s) failed validation.")
        sys.exit(1)
    print(f"All {len(files)} files pass SOP 4.")


if __name__ == "__main__":
    main()
