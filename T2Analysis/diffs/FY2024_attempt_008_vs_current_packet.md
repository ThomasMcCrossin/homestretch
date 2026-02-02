# UFile attempt diff vs current packet — FY2024

- Attempt PDF: `/home/clarencehub/t2-final-fy2024-fy2025/taxattempts/FY2024/1/2024 - 14587430 Canada Inc. - My copy - Tax return (8).pdf`
- Packet snapshot_source: `output/snapshots/20260202-235500/output/`

## Schedule 100 (Balance sheet)

| Code | Description | Attempt | Expected | Delta (expected - attempt) | Notes |
|---|---|---:|---:|---:|---|
| 1001 | Cash | 26,292 | 26,292 | 0 |  |
| 1121 | Inventory of goods for sale | 5,129 | 5,129 | 0 |  |
| 1484 | Prepaid expenses | 649 | 649 | 0 |  |
| 1599 |  | 32,070 |  |  | extra in attempt |
| 1740 | Machinery, equipment, furniture and fixtures | 2,298 | 2,298 | 0 |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -508 | -508 | 0 |  |
| 2008 |  | 2,298 |  |  | extra in attempt |
| 2009 |  | -508 |  |  | extra in attempt |
| 2599 | Total assets | 33,860 | 33,860 | 0 |  |
| 2620 | Amounts payable and accrued liabilities | 2,687 | 2,687 | 0 |  |
| 2680 | Taxes payable (GST/HST, etc.) | 6,757 | 6,757 | 0 |  |
| 2781 | Due to individual shareholder(s) | 3,578 | 3,578 | 0 |  |
| 3139 |  | 13,022 |  |  | extra in attempt |
| 3499 | Total liabilities | 13,022 | 13,022 | 0 |  |
| 3500 | Common shares | 100 | 100 | 0 |  |
| 3600 | Retained earnings/deficit | 18,456 | 20,738 | 2,282 | mismatch |
| 3620 | Total shareholder equity | 18,556 | 20,838 | 2,282 | mismatch |
| 3640 | Total liabilities and shareholder equity | 31,578 | 33,860 | 2,282 | mismatch |
| 3680 | Net income/loss | 18,456 |  |  | extra in attempt |
| 3849 | Retained earnings/deficit - End | 18,456 |  |  | extra in attempt |

## Schedule 125 (Income statement)

| Code | Description | Attempt | Expected | Delta (expected - attempt) | Notes |
|---|---|---:|---:|---:|---|
| 0002 |  | 3 |  |  | extra in attempt |
| 8000 | Trade sales of goods and services | 181,235 | 181,235 | 0 |  |
| 8089 |  | 181,235 |  |  | extra in attempt |
| 8299 | Total revenue | 181,235 | 181,235 | 0 |  |
| 8320 |  | 111,220 |  |  | extra in attempt |
| 8500 |  | -2,847 |  |  | extra in attempt |
| 8518 | Cost of sales | 108,373 | 106,091 | -2,282 | mismatch |
| 8519 | Gross profit/loss | 72,862 | 75,144 | 2,282 | mismatch |
| 8520 | Advertising and promotion | 1,606 | 1,606 | 0 |  |
| 8523 | Meals and entertainment | 518 | 518 | 0 |  |
| 8622 | Employer's portion of employee benefits | 1,463 | 1,463 | 0 |  |
| 8670 | Amortization of tangible assets | 508 | 508 | 0 |  |
| 8690 | Insurance | 1,851 | 1,851 | 0 |  |
| 8710 | Interest and bank charges | 2,218 | 2,218 | 0 |  |
| 8810 | Office expenses | 1,998 | 1,998 | 0 |  |
| 8813 | Data processing | 1,135 | 1,135 | 0 |  |
| 8860 | Professional fees | 879 | 879 | 0 |  |
| 8911 | Real estate rental | 8,235 | 8,235 | 0 |  |
| 8960 | Repairs and maintenance | 429 | 429 | 0 |  |
| 9060 | Salaries and wages | 23,485 | 23,485 | 0 |  |
| 9130 | Supplies | 5,494 | 5,494 | 0 |  |
| 9131 | Small tools | 23 | 23 | 0 |  |
| 9270 | Other expenses | 71 | 71 | 0 |  |
| 9275 | Delivery, freight and express | 100 | 100 | 0 |  |
| 9281 | Vehicle expenses | 4,393 | 4,393 | 0 |  |
| 9367 | Total operating expenses | 54,406 | 54,406 | 0 |  |
| 9368 | Total expenses | 162,779 | 160,497 | -2,282 | mismatch |
| 9369 |  | 18,456 |  |  | extra in attempt |
| 9970 |  | 18,456 |  |  | extra in attempt |
| 9999 | Net income/loss after taxes | 18,456 | 20,738 | 2,282 | mismatch |

## Schedule 1 (Net income for tax purposes)

| Code | Description | Attempt | Expected | Delta (expected - attempt) | Notes |
|---|---|---:|---:|---:|---|
| A | Net income (loss) per financial statements | 18,456 | 20,738 | 2,282 | mismatch |
| C | Net income (loss) for tax purposes | 18,358 | 21,068 | 2,710 | mismatch |
| 104 | Accounting amortization | 508 | 508 | 0 |  |
| 121 | Non-deductible meals and entertainment (50%) | 259 | 259 | 0 |  |
| 128 | Non-deductible fines and penalties |  | 71 |  | missing in attempt |
| 206 | Capital items expensed |  | 0 |  | missing in attempt |
| 403 | Capital cost allowance (Schedule 8) | 865 | 508 | -357 | mismatch |
| 500 | Total additions | 19,223 | 838 | -18,385 | mismatch |
| 510 | Total deductions | 865 | 508 | -357 | mismatch |

## Schedule 8 (CCA) — class summary

| Class | Attempt additions | Expected additions | Attempt CCA | Expected CCA | Notes |
|---:|---:|---:|---:|---:|---|
| 8 | 1,650 | 1,650 | 330 | 330 |  |
| 50 | 648 | 648 | 535 | 178 | cca mismatch |

- Schedule 8 total CCA (attempt): `865`
- Schedule 8 total CCA (expected): `508`

## Retained earnings rollforward

| Code | Description | Attempt | Expected | Delta (expected - attempt) | Notes |
|---|---|---:|---:|---:|---|
| 3660 | Retained earnings/deficit - Start |  | 0 |  | missing in attempt |
| 3680 | Net income/loss |  | 20,738 |  | missing in attempt |
| 3849 | Retained earnings/deficit - End |  | 20,738 |  | missing in attempt |
