# FY2025 — UFile Attempt 2 messages (diagnosis)

Source:
- `taxattemps/FY2025/Attempt 2/messages.txt`

## What failed (why no bar codes / can’t efile)

### 1) “GIFI 100 does not balance” / Total assets mismatch
Message:
- `GIFI field 2599 does not equal GIFI fields 3499+3620`
- `GIFI-Field 2599:$25977 (GIFI-Field 3499 + GIFI-Field 3620): $62878 Difference:$36901`

Interpretation:
- Equity (or liabilities+equity) is overstated by **$36,901** relative to assets.
- The **$36,901** equals FY2025 dividends declared **$36,900** plus rounding **$1**.

Typical root cause:
- Retained earnings end (`3849` / Schedule 100 `3600`) was entered/kept at a value that did not reflect the dividend reduction, while the dividend line existed in retained earnings rollforward (or vice-versa).

### 2) Retained earnings rollforward inconsistency
Message:
- `GIFI-Field 3849 does not match internal subtotal calculation.`
- `GIFI-Field 3849:$45005 Calculation:$8104 Difference:$36901`

Interpretation:
- UFile calculated retained earnings end as **$8,104** from the rollforward lines.
- The value present in `3849` was **$45,005**, overstated by **$36,901**.

Typical root cause:
- `3849` (and/or Schedule 100 `3600`) was populated directly (carryforward/import), instead of letting UFile compute it from:
  - `3660` opening RE
  - `3680` net income
  - `3700` dividends declared
  - `3740` other items (rounding)

## Other warnings (non-blocking)

### Dividends screen missing
Messages:
- “An amount entered in GIFI fields 3700 or 3701… ‘Dividends paid’ section is missing.”
- “Dividends declared have been entered in GIFI but dividends paid has not been entered.”

This is consistent with FY2025 having `3700 = 36,900` and the dividends screen not being completed.

## What to do differently next attempt (FY2025)

Follow:
- `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`
- `UfileToFill/ufile_packet/guides/UFILE_FILING_COMPLETENESS_CHECKLIST.md`

Critical steps:
1) Clear totals/subtotals: `2599`, `3499`, `3620`, `3640`, `9367`, `9368`, `3849`, `3600`.
2) Enter only detail lines:
   - Inventory `1121`, prepaids `1484`, due-to shareholders `2781`, etc.
3) Enter retained earnings rollforward lines (`3660`, `3680`, `3700`, `3740`) and let UFile compute `3849`/`3600`.
4) Complete the Dividends Paid screen if `3700` is non-zero (FY2025: `36,900`).

