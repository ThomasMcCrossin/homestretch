# Costco 9100 renormalization — diffs vs pre-change packet

This document shows what changed after removing Costco’s internal placeholder bucket `9100 Pending Receipt - No ITC` from the Costco vendor profile weights (and renormalizing the remaining Costco weights to 100%).

**Baseline (pre-change) snapshot**
- `output/snapshots/20260129-190611/`

**Post-change snapshot**
- `output/snapshots/20260129-192249/`

## What changed (high level)

- Costco’s prior allocations to `9100` (which mapped into **GIFI 9270 Other expenses**) are now redistributed into real buckets (primarily **Cost of sales**, with some **Supplies** and **Repairs & maintenance** depending on the existing Costco weight model).
- Total expense is unchanged. This is a classification-only change.
- The one Costco `MANUAL` allocation remains intact (`wave_bill_id=779`, $400.00).

## FY2024 — GIFI totals deltas (post − pre)

| GIFI | Label | Pre | Post | Delta |
|---:|---|---:|---:|---:|
| 8518 | Cost of sales | 104,712.94 | 109,278.51 | +4,565.57 |
| 9130 | Supplies | 6,276.94 | 5,561.44 | -715.50 |
| 8960 | Repairs & maintenance | 834.18 | 458.21 | -375.97 |
| 9270 | Other expenses | 3,819.99 | 345.89 | -3,474.10 |

Sanity check: `(+4,565.57) + (-715.50) + (-375.97) + (-3,474.10) = 0.00`

### FY2024 — Why 9270 is still not zero

After the change, `9270` is no longer “Costco 9100”. It is now basically only:
- `9150 Penalties - CRA` (the non-deductible penalty amount, which is separately added back on Schedule 1 line 311 in the packet), plus
- a few cents of rounding remainder.

## FY2025 — GIFI totals deltas (post − pre)

| GIFI | Label | Pre | Post | Delta |
|---:|---|---:|---:|---:|
| 8518 | Cost of sales | 105,698.48 | 110,283.92 | +4,585.44 |
| 9130 | Supplies | 5,347.75 | 4,629.17 | -718.58 |
| 8960 | Repairs & maintenance | 980.69 | 603.12 | -377.57 |
| 9270 | Other expenses | 3,781.99 | 292.70 | -3,489.29 |

Sanity check: `(+4,585.44) + (-718.58) + (-377.57) + (-3,489.29) = 0.00`

### FY2025 — Why 9270 is still not zero

Same story as FY2024: the remaining 9270 is essentially CRA penalties + small remainder amounts (not Costco “artifact” spending).

## Remaining 9100 amounts (for audit notes)

Even though Costco allocations to `9100` are now **0**, there are still small amounts posting to `9100` in journal entries due to reimbursement remainder logic and rounding:

- FY2024: `9100` net in journals ≈ **$274.54**
- FY2025: `9100` net in journals ≈ **$18.83**

These are immaterial and are accompanied by journal entry descriptions that point to the specific bank transactions (so they are auditable). If you want, we can later reclass these to a different “clearing” account, but they are **not** the Costco artifact problem.

## What you need to update in UFile

If you previously entered GIFI lines based on the pre-change packet, the lines most likely to need updating are:

- **Schedule 125 — Purchases / inventory lines** (UFile uses these to derive cost of sales):
  - **8300** Opening inventory (entered)
  - **8320** Purchases / cost of materials (entered)
  - **8500** Closing inventory (entered; UFile may display it as a negative line item on printouts)
- **Other expenses (9270)** decreased (both FYs).
- **Supplies (9130)** and **Repairs & maintenance (8960)** decreased (both FYs).
- **8518 Cost of sales** is typically auto-calculated by UFile from 8300/8320/8500 and is included here as a tie-check, not something to type directly.

No other lines were intentionally changed by this Costco fix.
