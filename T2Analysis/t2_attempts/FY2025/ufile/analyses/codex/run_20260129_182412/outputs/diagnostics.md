# Diagnostics + UFile Messages (FY2025, attempt_002)

## Parsed diagnostics (from diagnostics.csv) — full list
- **Non-blocking**: error and warning messages shown below and in the data editor, then make the required
- **Blocking**: GIFI-FIELD 3849 does not match internal subtotal calculation.
- **Non-blocking**: . GIFI-FIELD 3849:$45,005 Calculation:$8,104 Difference:$36,901
- **Non-blocking**: GIFI-FIELD 2599:$25,977 (GIFI-FIELD 3499 + GIFI-FIELD 3620): $62,878 Difference:$36,901
- **Non-blocking**: Diagnostics page 1 of 3
- **Non-blocking**: Diagnostics page 2 of 3
- **Blocking**: This return is ineligible for federal efile due to the following reason(s):
- **Non-blocking**: Diagnostics page 3 of 3
- **Non-blocking**: Was an amount included in the opening balance of retained earnings or equity, in order to correct an error, to
- **Non-blocking**: BCR validity checks relate mainly to incomplete or inconsistent data entry. Review the error and warning messages

## Parsed diagnostics — actionable subset
- **Blocking**: GIFI-FIELD 3849 does not match internal subtotal calculation.
- **Non-blocking**: . GIFI-FIELD 3849:$45,005 Calculation:$8,104 Difference:$36,901
- **Non-blocking**: GIFI-FIELD 2599:$25,977 (GIFI-FIELD 3499 + GIFI-FIELD 3620): $62,878 Difference:$36,901
- **Blocking**: This return is ineligible for federal efile due to the following reason(s):

### Cross-check against full_text.txt
- FOUND: error and warning messages shown below and in the data editor, then make the required
- FOUND: GIFI-FIELD 3849 does not match internal subtotal calculation.
- FOUND: . GIFI-FIELD 3849:$45,005 Calculation:$8,104 Difference:$36,901
- FOUND: GIFI-FIELD 2599:$25,977 (GIFI-FIELD 3499 + GIFI-FIELD 3620): $62,878 Difference:$36,901
- FOUND: Diagnostics page 1 of 3
- FOUND: Diagnostics page 2 of 3
- FOUND: This return is ineligible for federal efile due to the following reason(s):
- FOUND: Diagnostics page 3 of 3
- FOUND: Was an amount included in the opening balance of retained earnings or equity, in order to correct an error, to
- FOUND: BCR validity checks relate mainly to incomplete or inconsistent data entry. Review the error and warning messages

## UFile Messages (from messages.txt)
- **Blocking**: GIFI 100 does not balance (GIFI field 2599 does not equal GIFI fields 3499+3620).
  - Expected screen: GIFI → Balance sheet (Schedule 100) → Totals (2599/3499/3620/3640)
  - Likely action: Ensure liabilities (3499) + equity (3620) equals total assets (2599). Most often caused by retained earnings (3600/3849) not matching the retained earnings reconciliation (3660/3680/3700/3701/3740).
- **Blocking**: BAR CODE RETURN (BCR) VALIDITY CHECKS FAILED
  - Expected screen: EFILE / Bar code return (BCR) / Review messages
  - Likely action: Resolve blocking GIFI errors, then recalculate; bar codes will generate only after validity checks pass.
- **Blocking**: No bar codes were generated
  - Expected screen: EFILE / Bar code return (BCR) / Review messages
  - Likely action: Resolve blocking GIFI errors, then recalculate; bar codes will generate only after validity checks pass.
- **Non-blocking**: An amount entered in GIFI fields �3700 or 3701� on GIFI � Balance sheet page, the section "Dividends paid" is missing. Click here to verify your data.
  - Expected screen: Interview/Setup → Dividends paid (UFile screen)
  - Likely action: If dividends are declared (3700/3701), complete the 'Dividends paid' section. If no dividends were paid/declared, clear dividends declared to avoid inconsistent screens.
- **Non-blocking**: Tax year presumed to be 365 days according to begin date of operations or incorporation date.
  - Expected screen: Interview/Setup → Identification / fiscal period
  - Likely action: Confirm begin/end of tax year and incorporation/operations dates so UFile does not presume a 365‑day year.
- **Non-blocking**: There is no entry in the income source section; all income is considered as active business income.
  - Expected screen: Interview/Setup → Income source section
  - Likely action: Confirm income source classification (e.g., active business vs property/other). If left blank, UFile assumes all income is active business income.
- **Non-blocking**: Dividends declared have been entered in GIFI but dividends paid has not been entered.
  - Expected screen: Interview/Setup → Dividends paid (UFile screen)
  - Likely action: If dividends are declared (3700/3701), complete the 'Dividends paid' section. If no dividends were paid/declared, clear dividends declared to avoid inconsistent screens.
- **Non-blocking**: No instalments required since total tax instalments calculated are less than or equal to $3,000.
  - Expected screen: Information message (instalments)
  - Likely action: No action required unless instalments were expected.
- **Blocking**: GIFI-Field 3849 does not match internal subtotal calculation.
  - Expected screen: GIFI → Balance sheet (Schedule 100) → Retained earnings reconciliation (3660/3680/3700/3701/3740/3849)
  - Likely action: Clear any manual override on ending retained earnings (3849 / 3600) and let it compute from start (3660) + net income (3680) − dividends declared (3700/3701) ± other items (3740).
- **Non-blocking**: GIFI-Field 3849:$45005 Calculation:$8104 Difference:$36901
  - Expected screen: GIFI → Balance sheet (Schedule 100) → Retained earnings reconciliation (3849)
  - Likely action: This is the numeric detail for the 3849 mismatch. Fix by removing overrides on 3600/3849 and completing rollforward inputs (3660/3680/3700/3740).
- **Non-blocking**: GIFI sch. 100 - total assets does not equal total liabilities plus shareholder equity.
  - Expected screen: GIFI → Balance sheet (Schedule 100) → Totals (2599/3499/3620/3640)
  - Likely action: Ensure liabilities (3499) + equity (3620) equals total assets (2599). Most often caused by retained earnings (3600/3849) not matching the retained earnings reconciliation (3660/3680/3700/3701/3740).
- **Non-blocking**: GIFI-Field 2599:$25977 (GIFI-Field 3499 + GIFI-Field 3620): $62878 Difference:$36901
  - Expected screen: GIFI → Balance sheet (Schedule 100) → Totals (2599 vs 3499+3620)
  - Likely action: This is the numeric detail for the balance-sheet mismatch. Fix the retained earnings linkage so 3620 brings (3499+3620) back to 2599.
