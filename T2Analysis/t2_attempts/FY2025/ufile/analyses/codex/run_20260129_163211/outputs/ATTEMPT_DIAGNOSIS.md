# FY2025 UFile T2 attempt diagnosis (forensic, audit-style)

## Executive summary

- **Blocking diagnostics** are driven by two GIFI inconsistencies: (1) `9367` total operating expenses does not equal the sum of expense detail lines, and (2) Schedule 100 does not balance (`2599` ≠ `3499 + 3620`).
- The Schedule 100 imbalance is exactly the Schedule 125 net income (`36,054`), indicating retained earnings/equity was increased by net income but the balance sheet asset/liability inputs did not reflect it.
- Compared to the project packet, the attempt is missing dividends (`3700`) and appears to have entered opening retained earnings incorrectly (`3660`), causing retained earnings (`3600/3849`) to be overstated by the year’s net income.
- The attempt also includes an extra populated expense line (`9220` utilities `465`) that is not present in the project packet (which only has `9225` telephone/internet `465`). Removing `9220` from the attempt’s expense detail sum reconciles it to the project’s operating expense total.
- Overall root cause is **A) UFile entry mechanics / auto-calculation behavior**, plus a small amount of **data entry duplication** (utilities vs telephone). The project packet is internally consistent for FY2025 across Schedule 100/125 and retained earnings.

## Evidence index (files relied on in this run)

Parsed bundle (copied into this run for traceability):
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/meta.json
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/verification_report.md
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/diagnostics.csv
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/schedule_100.csv
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/schedule_125.csv
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/retained_earnings.csv
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/full_text.txt
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/pages/page_012.txt (Schedule 100 spot-check)
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/pages/page_013.txt (Schedule 125 spot-check)
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/pages/page_014.txt (Schedule 125 spot-check)

Project expected values (copied into this run for traceability):
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/project/packet.json
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/project/UFILet2_FILL_GUIDE.md

GIFI catalogs used (copied into this run for traceability):
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/gifi/BalanceSheet.txt
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/gifi/IncomeStatement.txt
- /home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/gifi/NetIncome.txt

## Diagnostics list (blocking vs non-blocking)

| Class | Exact text |
| --- | --- |
| Non-blocking | error and warning messages shown below and in the data editor, then make the required |
| Blocking | GIFI-FIELD 9367 does not match internal subtotal calculation. |
| Blocking | . GIFI-FIELD 9367:$89,155 Calculation:$97,325 Difference:$8,170 |
| Blocking | GIFI-FIELD 2599:$25,977 (GIFI-FIELD 3499 + GIFI-FIELD 3620): $62,031 Difference:$36,054 |
| Non-blocking | Diagnostics page 1 of 3 |
| Non-blocking | Diagnostics page 2 of 3 |
| Blocking | This return is ineligible for federal efile due to the following reason(s): |
| Non-blocking | Diagnostics page 3 of 3 |
| Non-blocking | Was an amount included in the opening balance of retained earnings or equity, in order to correct an error, to |
| Non-blocking | BCR validity checks relate mainly to incomplete or inconsistent data entry. Review the error and warning messages |
| Blocking | BAR CODE RETURN (BCR) VALIDITY CHECKS FAILED |
| Blocking | No bar codes were generated |
| Non-blocking | BCR validity checks relate mainly to incomplete or inconsistent data entry. Review the |
| Non-blocking | GIFI |
| Non-blocking | . |
| Blocking | GIFI sch. 100 - total assets does not equal total liabilities plus shareholder equity. |
| Non-blocking | FEDERAL CORPORATION INTERNET FILING |
| Blocking | The federal BCR is not being generated. |
| Non-blocking | FEDERAL AND/OR PROVINCIAL WARNINGS |
| Non-blocking | Federal |
| Non-blocking | Taxation year presumed to be 365 days according to BEGINDATE or INCORPDATE entry. |
| Non-blocking | Missing entry for INCOMESOURCE; all income is considered as active business income. |

## Extracted schedules (from parsed CSVs)

### Schedule 100 (Balance sheet) – attempt

| Code | Description | Attempt amount | Page |
| --- | --- | --- | --- |
| 1001 | . . . . Cash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 12,472 | 12 |
| 1121 | . . . . Inventory . . . . . . . . of . . goods . . . . . for . . . sale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 10,015 | 12 |
| 1301 | . . . . Due . . . . from . . . . individual . . . . . . . . shareholder(s) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 2,000 | 12 |
| 1484 | . . . . Prepaid . . . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 1,490 | 12 |
| 1599 | . . . . Total . . . . current . . . . . . assets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 25,977 | 12 |
| 2599 | . . . . Total . . . . assets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = | 25,977 | 12 |
| 2620 | . . . . Amounts . . . . . . . payable . . . . . . . and . . . . accrued . . . . . . . liabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 10,013 | 12 |
| 2680 | . . . . Taxes . . . . . payable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 2,663 | 12 |
| 2781 | . . . . Due . . . . to . . individual . . . . . . . . shareholder(s) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 5,097 | 12 |
| 3139 | . . . . Total . . . . current . . . . . . liabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 17,773 | 12 |
| 3499 | . . . . Total . . . . liabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = | 17,773 | 12 |
| 3500 | . . . . Common . . . . . . . . shares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 100 | 12 |
| 3600 | . . . . Retained . . . . . . . . earnings . . . . . . . / . deficit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 44,158 | 12 |
| 3620 | . . . . Total . . . . shareholder . . . . . . . . . . equity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = | 44,258 | 12 |
| 3640 | Total liabilities and shareholder equity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . = | 62,031 | 12 |
| 3660 | . . . . Retained . . . . . . . . earnings . . . . . . . / . deficit . . . . . - . start . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 8,104 | 12 |
| 3680 | . . . . Net . . . income . . . . . . . / . loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 36,054 | 12 |
| 3849 | . . . . Retained . . . . . . . . earnings . . . . . . . / . deficit . . . . . - . end . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = | 44,158 | 12 |

### Schedule 125 (Income statement) – attempt

| Code | Description | Attempt amount | Page |
| --- | --- | --- | --- |
| 0002 | Description of the operation | 3 | 13 |
| 8000 | . . . . Trade . . . . . sales . . . . . of . . goods . . . . . and . . . . services . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 230,907 | 13 |
| 8089 | . . . . Total . . . . sales . . . . . of . . goods . . . . . and . . . . services . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 230,907 | 13 |
| 8299 | . . . . Total . . . . revenue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = | 230,907 | 13 |
| 8300 | . . . . Opening . . . . . . . inventory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 2,847 | 13 |
| 8320 | . . . . Purchases . . . . . . . . . / . cost . . . . of . . materials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 112,866 | 13 |
| 8500 | . . . . Closing . . . . . . inventory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | -10,015 | 13 |
| 8518 | . . . . Cost . . . . of . . sales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + = | 105,698 | 13 |
| 8519 | Gross profit / loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 125,209 | 13 |
| 8520 | . . . . Advertising . . . . . . . . . and . . . . promotion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 798 | 13 |
| 8523 | . . . . Meals . . . . . and . . . . entertainment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 408 | 13 |
| 8622 | . . . . Employers . . . . . . . . . portion . . . . . . of . . employee . . . . . . . . benefits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 3,610 | 13 |
| 8690 | . . . . Insurance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 1,951 | 13 |
| 8710 | . . . . Interest . . . . . . and . . . . bank . . . . charges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 6,694 | 13 |
| 8810 | . . . . Office . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 3,903 | 13 |
| 8813 | . . . . Data . . . . processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 1,878 | 13 |
| 8860 | . . . . Professional . . . . . . . . . . fees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 353 | 13 |
| 8911 | . . . . Real . . . . estate . . . . . rental . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 7,137 | 13 |
| 8960 | . . . . Repairs . . . . . . . and . . . maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 981 | 13 |
| 9060 | . . . . Salaries . . . . . . . and . . . wages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 54,899 | 13 |
| 9130 | . . . . Supplies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 5,348 | 13 |
| 9131 | . . . . Small . . . . . tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 479 | 13 |
| 9220 | . . . . Utilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 465 | 13 |
| 9225 | . . . . Telephone . . . . . . . . . and . . . telecommunications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 465 | 13 |
| 9270 | . . . . Other . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 3,782 | 13 |
| 9275 | . . . . Delivery, . . . . . . . freight . . . . . . and . . . express . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 136 | 14 |
| 9281 | . . . . Vehicle . . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 4,038 | 14 |
| 9367 | . . . . Total . . . . operating . . . . . . . . expenses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 89,155 | 14 |
| 9368 | Total expenses = | 194,853 | 14 |
| 9369 | Net non-farming income . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . + | 36,054 | 13 |
| 9970 | Net income/loss before taxes and extraordinary items . . . . . . . . . . . . . . . . . . . . . . . . . . . . = | 36,054 | 13 |
| 9999 | Net income / loss after taxes and extraordinary items . . . . . . . . . . . . . . . . . . . . . . . . . . . . . = | 36,054 | 13 |

### Spot-checks against extracted page text (confidence checks)

- Schedule 100 source page: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/pages/page_012.txt` (e.g., codes `2599=25,977`, `3640=62,031`, `3600=44,158`).
- Schedule 125 source pages: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/pages/page_013.txt` and `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/inputs/parsed_bundle/pages/page_014.txt` (e.g., `9367=89,155`, `9368=194,853`, `9999=36,054`).

### Retained earnings – attempt vs project (minimum required lines)

Note: `retained_earnings.csv` in this parsed bundle is empty; retained earnings rollforward lines are present inside Schedule 100 in `schedule_100.csv` (codes 3660/3680/3849).

| Code | Attempt amount |
| --- | --- |
| 3660 | 8,104 |
| 3680 | 36,054 |
| 3700 |  |
| 3849 | 44,158 |

| Code | Project expected amount |
| --- | --- |
| 3660 | 16,656 |
| 3680 | 28,349 |
| 3700 | 36,900 |
| 3849 | 8,104 |

## Recalculations (show-your-work)

# Independent recomputation (from parsed attempt amounts only)

## Schedule 125 (Income statement) recomputation

- Total revenue (8299): 230,907
- COGS (8518): 105,698
- Gross profit (computed): 8299 - 8518 = 230,907 - 105,698 = 125,209
- Gross profit (8519 on return): 125,209

### COGS movement check

- Opening inventory (8300): 2,847
- Purchases (8320): 112,866
- Closing inventory (8500 parsed): -10,015 (PDF shows parentheses; treat as -10,015)
- COGS from movement: 8300 + 8320 - abs(8500) = 2,847 + 112,866 - 10,015 = 105,698
- COGS (8518 on return): 105,698

### Operating expenses check

- Total operating expenses (9367 on return): 89,155
- Sum of populated expense detail lines (excluding totals like 9367/9368): 97,325
- Difference (detail sum - 9367): 8,170

### Net income check

- Net income (9999 on return): 36,054
- Net income recomputed using 9367: 8519 - 9367 = 125,209 - 89,155 = 36,054
- Net income recomputed using detail sum: 8519 - sum(expenses) = 125,209 - 97,325 = 27,884

## Schedule 100 (Balance sheet) recomputation

- Total assets (2599): 25,977
- Total liabilities (3499): 17,773
- Total shareholder equity (3620): 44,258
- Total liabilities and shareholder equity (3640): 62,031

### Equity and balance equation

- Equity recompute: 3500 + 3600 = 100 + 44,158 = 44,258 (compare to 3620=44,258)
- Liabilities + equity recompute: 3499 + 3620 = 17,773 + 44,258 = 62,031 (compare to 3640=62,031)
- Balance check: 3640 - 2599 = 62,031 - 25,977 = 36,054

### Retained earnings rollforward (as shown inside Schedule 100)

- Opening RE (3660): 8,104
- Net income/loss (3680): 36,054
- Closing RE (3849): 44,158
- Closing RE recompute (3660 + 3680): 44,158

## Attempt vs project comparison (key lines)

| Code | Attempt | Project expected | Delta (A-E) | Likely cause |
| --- | --- | --- | --- | --- |
| 9220 | 465 |  |  | Entry/mechanics (extra line / classification) |
| 9225 | 465 | 465 | +0 | OK |
| 9367 | 89,155 | 96,860 | -7,705 | Entry/mechanics (total vs detail mismatch) |
| 9368 | 194,853 | 202,558 | -7,705 | Entry/mechanics (total vs detail mismatch) |
| 9999 | 36,054 | 28,349 | +7,705 | Entry/mechanics (driven by 9367 mismatch) |
| 3660 | 8,104 | 16,656 | -8,552 | Entry/mechanics (retained earnings linkage) |
| 3680 | 36,054 | 28,349 | +7,705 | Entry/mechanics (retained earnings linkage) |
| 3700 |  | 36,900 |  | Entry/mechanics (missing dividends) |
| 3849 | 44,158 | 8,104 | +36,054 | Entry/mechanics (retained earnings linkage) |
| 3600 | 44,158 | 8,104 | +36,054 | Entry/mechanics (retained earnings linkage) |
| 3620 | 44,258 | 8,204 | +36,054 | Entry/mechanics (retained earnings linkage) |
| 3640 | 62,031 | 25,977 | +36,054 | Entry/mechanics (retained earnings linkage) |
| 2599 | 25,977 | 25,977 | +0 | OK |
| 3499 | 17,773 | 17,773 | +0 | OK |

Full comparison (all parsed codes + required lines): `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211/outputs/attempt_vs_project_comparison.csv`.

## Hypothesis testing (root cause analysis)

1) **Totals line populated vs internal subtotal mismatch (9367)**
   - Test: sum(populated expense detail lines) = 97,325 vs 9367=89,155 → mismatch 8,170.
   - Result: **Confirmed**. This is a classic UFile GIFI validity failure when both totals and details are entered inconsistently.

2) **Project double-count/omission (project inconsistency)**
   - Test: compare attempt detail lines to project expected codes.
   - Result: The project packet FY2025 Schedule 125 operating expense detail lines sum to 96,860 and reconcile with `9367=96,860`, `9368=202,558`, and `9999=28,349` (per `packet.json`). The attempt diverges due to `9367` being manually set to 89,155 and an extra `9220=465` line; attempt detail sum excluding `9220` is 96,860. **No project inconsistency is required to explain the attempt errors.**

3) **Wrong UFile line choice (detail vs total)**
   - Test: check whether totals like `9367/9368` are present while detail lines are present.
   - Result: **Confirmed**. Both details and totals are present but inconsistent.

4) **Retained earnings mismatch driven by missing dividends / wrong RE linkage**
   - Test: check Schedule 100 retained earnings subsection and whether dividends line `3700` is present/populated.
   - Result: In the attempt, `3660=8,104`, `3680=36,054`, `3849=44,158` and there is **no `3700` dividends** line populated; this forces ending retained earnings to equal opening + net income. This drives `3600/3620/3640` upward and creates the Schedule 100 imbalance. **Confirmed.**

5) **Duplicated classification in attempt**
   - Test: compare attempt vs project for populated expense lines.
   - Result: Attempt includes `9220 Utilities=465` and `9225 Telephone=465`; project includes only `9225=465`. This strongly suggests a duplicated entry in UFile. **Confirmed.**

## Final conclusion (A/B/C)

**A) UFile entry mechanics / auto-calculation behavior** (primary), with a small amount of **UFile data entry duplication** (utilities vs telephone). The parsed attempt’s diagnostics and imbalances can be fully explained by inconsistent entry of total lines (`9367/9368`) and retained earnings rollforward inputs (missing dividends / incorrect opening retained earnings), without requiring any changes to project accounting outputs.

## Fix checklists (proposed next actions; no changes made in this run)

### UFile UI checklist (next attempt)

1) **Schedule 125 totals vs detail**
   - If you enter **expense detail lines** (8520, 8523, …), **do not manually enter** totals like `9367` (Total operating expenses) or `9368` (Total expenses). Leave them blank and let UFile compute.
   - After entry, verify `9367` equals the sum of the populated expense detail lines (UFile’s internal subtotal).

2) **Avoid duplicated expense classification**
   - In the attempt, both `9220` (Utilities) and `9225` (Telephone/telecom) are populated with `465`. If the `465` is internet/phone, use `9225` only and leave `9220` blank (unless there is a separate utilities expense).

3) **Retained earnings rollforward (Schedule 100 subsection)**
   - Enter `3660` as **opening retained earnings (prior year ending)**, not the current-year ending retained earnings.
   - Enter `3700` (Dividends declared) where applicable; otherwise retained earnings will increase by net income and can blow up equity.
   - Prefer letting UFile compute `3849` (ending retained earnings) and `3600` (retained earnings on the balance sheet) from the rollforward.

4) **Balance sheet validity check**
   - Recalculate and confirm `2599` equals `3499 + 3620` and that UFile generates the federal BCR / barcodes.

5) **Non-blocking warnings**
   - Set `INCOMESOURCE` appropriately (active business income) to clear the warning that all income is presumed active.

### Project outputs checklist (only if re-validated / proven wrong)

- Re-validate the project packet FY2025 totals: `9999` should equal `8299 - 9368`; and `2599` should equal `3640`.
- Confirm whether there is **any** FY2025 utilities expense (GIFI `9220`). If not, the attempt’s `9220=465` is a UFile entry duplication.

