# UFile T2 attempt diagnosis (FY2025, attempt_002)

## Executive summary
- Blocking failures are driven by **retained earnings linkage on Schedule 100**: attempt shows `3849/3600=45,005`, but the retained earnings rollforward computes `3849=8,104` (difference `36,901`). This also makes Schedule 100 not balance (`2599=25,977` vs `3499+3620=62,878`).
- Schedule 125 totals are internally consistent in this attempt (no Schedule 125 subtotal diagnostics); the primary defect is confined to the **balance sheet retained earnings / dividends paid screens**.

## Evidence index (copied into this run)
- Parsed bundle meta: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/meta.json`
- Parsed bundle verification report: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/verification_report.md`
- Parsed diagnostics: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/tables/diagnostics.csv`
- Parsed Schedule 100 table: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/tables/schedule_100.csv`
- Parsed Schedule 125 table: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/tables/schedule_125.csv`
- Parsed retained earnings table: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/tables/retained_earnings.csv`
- Parsed full text: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/text/full_text.txt`
- Spot-check pages: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/text/pages/page_012.txt`
- Spot-check pages: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/text/pages/page_013.txt`
- Spot-check pages: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/parsed_bundle/text/pages/page_014.txt`
- UFile Messages: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/exports/messages.txt`
- Project expected packet (FY2025): `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/project/packet_FY2025.json`
- Project expected packet (all years): `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/project/packet_all_years.json`
- Entry guide: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/project/UFILet2_FILL_GUIDE.md`
- Trial balance (FY2025): `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/accounting_outputs/trial_balance_FY2025.csv`
- Vendor allocations: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/accounting_outputs/vendor_allocations_by_fy.csv`
- Vendor allocation summary: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/accounting_outputs/vendor_allocations_summary_by_fy.csv`
- Project-generated UFile GIFI export (FY2025): `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/inputs/accounting_outputs/ufile_gifi_FY2025.csv`

## Diagnostics list (blocking vs non-blocking)

### Parsed diagnostics (from diagnostics.csv) — full list
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

### Parsed diagnostics — actionable subset
- **Blocking**: GIFI-FIELD 3849 does not match internal subtotal calculation.
- **Non-blocking**: . GIFI-FIELD 3849:$45,005 Calculation:$8,104 Difference:$36,901
- **Non-blocking**: GIFI-FIELD 2599:$25,977 (GIFI-FIELD 3499 + GIFI-FIELD 3620): $62,878 Difference:$36,901
- **Blocking**: This return is ineligible for federal efile due to the following reason(s):

### UFile Messages (actionable subset)
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

## Extracted schedules (from parsed CSVs)

## Schedule 100 (Balance sheet) — required lines
| Code | Attempt amount | Page | Description |
|---:|---:|---:|---|
| 1001 | 12,472 | 12 | . . . . Cash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 1121 | 10,015 | 12 | . . . . Inventory . . . . . . . . of . . goods . . . . . for . . . sale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 1120 |  |  |  |
| 1301 | 2,000 | 12 | . . . . Due . . . . from . . . . individual . . . . . . . . shareholder(s) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 1484 | 1,490 | 12 | . . . . Prepaid . . . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 1480 |  |  |  |
| 2620 | 10,013 | 12 | . . . . Amounts . . . . . . . payable . . . . . . . and . . . . accrued . . . . . . . liabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 2680 | 2,663 | 12 | . . . . Taxes . . . . . payable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 2781 | 5,097 | 12 | . . . . Due . . . . to . . individual . . . . . . . . shareholder(s) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 2780 |  |  |  |
| 3500 | 100 | 12 | . . . . Common . . . . . . . . shares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 3600 | 45,005 | 12 | . . . . Retained . . . . . . . . earnings . . . . . . . / . deficit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 2599 | 25,977 | 12 | . . . . Total . . . . assets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = |
| 3499 | 17,773 | 12 | . . . . Total . . . . liabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = |
| 3620 | 45,105 | 12 | . . . . Total . . . . shareholder . . . . . . . . . . equity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = |
| 3640 | 62,878 | 12 | Total liabilities and shareholder equity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . = |

## Retained earnings — required lines
| Code | Attempt amount | Page | Description |
|---:|---:|---:|---|
| 3660 | 16,656 | 12 | . . . . Retained . . . . . . . . earnings . . . . . . . / . deficit . . . . . - . start . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 3680 | 28,349 | 12 | . . . . Net . . . income . . . . . . . / . loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 3700 | -36,900 | 12 | . . . . Dividends . . . . . . . . declared . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 3701 |  |  |  |
| 3849 | 45,005 | 12 | . . . . Retained . . . . . . . . earnings . . . . . . . / . deficit . . . . . - . end . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = |

## Schedule 125 (Income statement) — required lines
| Code | Attempt amount | Page | Description |
|---:|---:|---:|---|
| 8000 | 230,907 | 13 | . . . . Trade . . . . . sales . . . . . of . . goods . . . . . and . . . . services . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8299 | 230,907 | 13 | . . . . Total . . . . revenue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = |
| 8300 | 2,847 | 13 | . . . . Opening . . . . . . . inventory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8320 | 112,866 | 13 | . . . . Purchases . . . . . . . . . / . cost . . . . of . . materials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8500 | -10,015 | 13 | . . . . Closing . . . . . . inventory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8518 | 105,698 | 13 | . . . . Cost . . . . of . . sales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = |
| 8519 | 125,209 | 13 | Gross profit / loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| 9367 | 96,860 | 14 | . . . . Total . . . . operating . . . . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9368 | 202,558 | 14 | Total expenses = |

## Schedule 125 — populated expense detail lines
| Code | Attempt amount | Page | Description |
|---:|---:|---:|---|
| 8520 | 798 | 13 | . . . . Advertising . . . . . . . . . and . . . . promotion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8523 | 408 | 13 | . . . . Meals . . . . . and . . . . entertainment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8622 | 3,610 | 13 | . . . . Employers . . . . . . . . . portion . . . . . . of . . employee . . . . . . . . benefits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8690 | 1,951 | 13 | . . . . Insurance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8710 | 6,694 | 13 | . . . . Interest . . . . . . and . . . . bank . . . . charges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8810 | 3,903 | 13 | . . . . Office . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8813 | 1,878 | 13 | . . . . Data . . . . processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8860 | 353 | 13 | . . . . Professional . . . . . . . . . . fees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8911 | 7,137 | 13 | . . . . Real . . . . estate . . . . . rental . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 8960 | 981 | 13 | . . . . Repairs . . . . . . . and . . . maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9060 | 54,899 | 13 | . . . . Salaries . . . . . . . and . . . wages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9130 | 5,348 | 13 | . . . . Supplies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9131 | 479 | 13 | . . . . Small . . . . . tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9225 | 465 | 13 | . . . . Telephone . . . . . . . . . and . . . telecommunications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9270 | 3,782 | 13 | . . . . Other . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9275 | 136 | 13 | . . . . Delivery, . . . . . . . freight . . . . . . and . . . express . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |
| 9281 | 4,038 | 14 | . . . . Vehicle . . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + |

## Recalculations (show your work)

All recomputations below use only parsed attempt amounts (not project expected values).

## Schedule 125 arithmetic
- Detail operating expenses sum (exclude totals 9367/9368): **96,860**
- Reported 9367 Total operating expenses: **96,860** (difference: 0)
- COGS from movement (8300 + 8320 + 8500; 8500 is printed as a negative): **105,698**; reported 8518: **105,698**
- Gross profit calc (8299 − 8518): **125,209**; reported 8519: **125,209**
- Net income calc (gross profit − op ex): **28,349**; reported 9999: **28,349**

## Schedule 100 arithmetic
- Equity calc (3500 + 3600): **45,105**; reported 3620: **45,105**
- Balance check: assets 2599 **25,977** vs (liabilities 3499 + equity 3620) **62,878** (difference: 36,901)
- Reported 3640 Total liabilities and shareholder equity: **62,878**

## Retained earnings rollforward arithmetic (why GIFI 3849 fails)
- Computed end (3660 + 3680 + 3700 + 3740): **16,656 + 28,349 + -36,900 + -1 = 8,104**
- Reported 3849 end retained earnings: **45,005** (difference: **36,901**)

## Attempt vs project comparison (key lines)

Full CSV: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/outputs/attempt_vs_project_comparison.csv`

| Code | Attempt | Project expected | Delta (attempt-project) | Likely cause |
|---:|---:|---:|---:|---|
| 2599 | 25,977 | 25,977 | 0 |  |
| 3499 | 17,773 | 17,773 | 0 |  |
| 3500 | 100 | 100 | 0 |  |
| 3600 | 45,005 | 8,104 | 36,901 | Entry/mechanics (retained earnings linkage) |
| 3620 | 45,105 | 8,204 | 36,901 | Entry/mechanics (retained earnings linkage) |
| 3640 | 62,878 | 25,977 | 36,901 | Entry/mechanics (retained earnings linkage) |
| 3660 | 16,656 | 16,656 | 0 |  |
| 3680 | 28,349 | 28,349 | 0 |  |
| 3700 | -36,900 | 36,900 | 0 |  |
| 3849 | 45,005 | 8,104 | 36,901 | Entry/mechanics (retained earnings linkage) |
| 9270 | 3,782 | 3,782 | 0 |  |
| 9367 | 96,860 | 96,860 | 0 |  |
| 9999 | 28,349 | 28,349 | 0 |  |

## Go-deeper traces

- GIFI 9270 trace: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/outputs/9270_trace.md`
- Suspense/placeholder accounts: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412/outputs/suspense_accounts_trace.md`

## Hypothesis testing (root cause A/B/C)

### 1) Totals line populated vs internal subtotal mismatch
- **Confirmed** for retained earnings: Attempt shows `3849=45,005`, but internal calculation shown in Messages/Diagnostics is `8,104` (difference `36,901`). This indicates a manual override or mis-linked screen entry.

### 2) Project double-count/omission (project inconsistency)
- **Not supported by evidence** for this defect: project packet and project-generated `output/ufile_gifi_FY2025.csv` both indicate `3600/3849=8,104` for FY2025.

### 3) Wrong UFile line choice (detail vs total)
- Not observed on Schedule 125 in this attempt (9367 matches expense detail sum).

### 4) Retained earnings mismatch driven by missing dividends / wrong linkage
- **Confirmed**: dividends declared (`3700=36,900`) exists, but UFile warns the 'Dividends paid' section is missing and retained earnings ending value is not reflecting dividends in the rollforward.

### 5) Duplicated classification in attempt
- No duplication detected in this attempt’s Schedule 125 vs project for the previously-seen utilities/telecom issue; re-check in `attempt_vs_project_comparison.csv` if needed.

## Conclusion

- Root cause classification: **A) UFile entry mechanics / auto-calculation behavior** (with a likely manual override on retained earnings or incomplete dividends paid screen), not a proven project-number error.

## Fix checklist — UFile UI next attempt (do not change numbers yet)

1. In the **GIFI → Balance sheet (Schedule 100)** screen, locate retained earnings fields:
   - Verify ending retained earnings `3600` matches retained earnings reconciliation ending `3849`.
   - If UFile allows overrides, clear the override so `3849` is computed from `3660 + 3680 − 3700/3701 ± 3740`.
2. In the **Dividends paid** section referenced by UFile Messages:
   - If dividends were declared (`3700/3701`), enter the corresponding dividends paid information (or explicitly set declared dividends to zero if incorrect).
3. Recalculate and confirm Messages no longer show:
   - `GIFI-Field 3849 does not match internal subtotal calculation`
   - `GIFI 100 does not balance ...` / `total assets does not equal total liabilities plus shareholder equity`

## Fix checklist — project outputs (only if later proven wrong)

- None required based on this attempt’s evidence. If future attempts still mis-link 3849/3600 after UI fixes, investigate the project’s UFile entry guide workflow ordering for dividends/retained earnings.
