# UFile T2 – Fill Guide (FY2024 + FY2025, May year-end)

Source-of-truth for amounts (current as of 2026-01-27):
- `output/final_snapshot_20260127-081402/`

This guide is designed to be used as a second-screen checklist while you manually fill UFile (instead of relying on GIFI import).

## Global answers (both returns)

- IFRS: **No** (financial statements not prepared using IFRS).
- Practitioner involvement / review / audit: **None** (management-prepared).

## FY2024 (2023-06-01 → 2024-05-31)

### GIFI → Balance sheet (Schedule 100)
Enter only the following non-zero lines (all amounts in **whole dollars**):

| GIFI code | Description | Amount |
|---:|---|---:|
| 1001 | Cash | 26292 |
| 1120 | Inventories | 2847 |
| 1480 | Other current assets | 649 |
| 2599 | Total assets | 29788 |
| 2620 | Amounts payable and accrued liabilities | 2687 |
| 2680 | Taxes payable (GST/HST, etc.) | 6767 |
| 2781 | Due to individual shareholder(s) | 3578 |
| 3499 | Total liabilities | 13032 |
| 3500 | Common shares | 100 |
| 3600 | Retained earnings/deficit | 16656 |
| 3620 | Total shareholder equity | 16756 |
| 3640 | Total liabilities and shareholder equity | 29788 |

Source: `output/final_snapshot_20260127-081402/gifi_schedule_100_FY2024.csv:1`

Quick tie-check:
- `2599` should equal `3640` (both **29,788**).

### GIFI → Income statement (Schedule 125)
Enter only the following non-zero lines:

| GIFI code | Description | Amount |
|---:|---|---:|
| 8000 | Trade sales of goods and services | 181235 |
| 8299 | Total revenue | 181235 |
| 8518 | Cost of sales | 103343 |
| 8519 | Gross profit/loss | 77892 |
| 8300 | Opening inventory | 1370 |
| 8520 | Advertising and promotion | 1606 |
| 8523 | Meals and entertainment | 518 |
| 8622 | Employer's portion of employee benefits | 1463 |
| 8690 | Insurance | 1851 |
| 8710 | Interest and bank charges | 2218 |
| 8810 | Office expenses | 10455 |
| 8860 | Professional fees | 879 |
| 8911 | Real estate rental | 8235 |
| 8960 | Repairs and maintenance | 834 |
| 9060 | Salaries and wages | 23485 |
| 9270 | Other expenses | 3820 |
| 9281 | Vehicle expenses | 4403 |
| 9801 | Freight and trucking | 100 |
| 9367 | Total operating expenses | 61237 |
| 9368 | Total expenses | 164580 |
| 9970 | Net income/loss before taxes | 16655 |
| 9999 | Net income/loss after taxes | 16655 |

Source: `output/final_snapshot_20260127-081402/gifi_schedule_125_FY2024.csv:1`

Notes:
- `8300` is present in our export; if UFile treats `8300` as *strictly* “Opening inventory” and it causes confusion, flag it and we can reclass it cleanly (it’s a presentation issue; totals can be preserved).

### Retained earnings schedule

| GIFI code | Description | Amount |
|---:|---|---:|
| 3660 | Retained earnings/deficit - Start | 0 |
| 3680 | Net income/loss | 16655 |
| 3740 | Other items affecting retained earnings (rounding) | 1 |
| 3849 | Retained earnings/deficit - End | 16656 |

Source: `output/final_snapshot_20260127-081402/gifi_retained_earnings_FY2024.csv:1`

### Net income / Schedule 1 (tax purposes)
If UFile doesn’t fully auto-populate these, enter:

| Schedule 1 line | Description | Amount |
|---:|---|---:|
| 300 | Net income per financial statements | 16655 |
| 117 | 50% of meals and entertainment | 259 |
| 311 | Penalties and fines (CRA) | 71 |
| 400 | Net income for tax purposes | 16985 |

Source: `output/final_snapshot_20260127-081402/schedule_1_FY2024.csv:1`

### Tax on capital (if UFile asks)
- Eligible for capital tax exemption: **Yes** (small private corp; no capital tax payable expected).
- Total assets at year-end (from financial statements): **29,788** (GIFI `2599`).

## FY2025 (2024-06-01 → 2025-05-31)

### GIFI → Balance sheet (Schedule 100)

| GIFI code | Description | Amount |
|---:|---|---:|
| 1001 | Cash | 12472 |
| 1120 | Inventories | 10015 |
| 1301 | Due from individual shareholder(s) | 2000 |
| 1480 | Other current assets | 1490 |
| 2599 | Total assets | 25977 |
| 2620 | Amounts payable and accrued liabilities | 10013 |
| 2680 | Taxes payable (GST/HST, etc.) | 2663 |
| 2781 | Due to individual shareholder(s) | 5097 |
| 3499 | Total liabilities | 17773 |
| 3500 | Common shares | 100 |
| 3600 | Retained earnings/deficit | 8104 |
| 3620 | Total shareholder equity | 8204 |
| 3640 | Total liabilities and shareholder equity | 25977 |

Source: `output/final_snapshot_20260127-081402/gifi_schedule_100_FY2025.csv:1`

Quick tie-check:
- `2599` should equal `3640` (both **25,977**).

### GIFI → Income statement (Schedule 125)

| GIFI code | Description | Amount |
|---:|---|---:|
| 8000 | Trade sales of goods and services | 230907 |
| 8299 | Total revenue | 230907 |
| 8518 | Cost of sales | 105698 |
| 8519 | Gross profit/loss | 125209 |
| 8520 | Advertising and promotion | 798 |
| 8523 | Meals and entertainment | 408 |
| 8622 | Employer's portion of employee benefits | 3610 |
| 8690 | Insurance | 1951 |
| 8710 | Interest and bank charges | 6694 |
| 8810 | Office expenses | 11608 |
| 8860 | Professional fees | 353 |
| 8911 | Real estate rental | 7137 |
| 8960 | Repairs and maintenance | 981 |
| 9060 | Salaries and wages | 54899 |
| 9220 | Utilities | 465 |
| 9270 | Other expenses | 3782 |
| 9281 | Vehicle expenses | 4038 |
| 9801 | Freight and trucking | 136 |
| 9367 | Total operating expenses | 96860 |
| 9368 | Total expenses | 202558 |
| 9970 | Net income/loss before taxes | 28349 |
| 9999 | Net income/loss after taxes | 28349 |

Source: `output/final_snapshot_20260127-081402/gifi_schedule_125_FY2025.csv:1`

### Retained earnings schedule

| GIFI code | Description | Amount |
|---:|---|---:|
| 3660 | Retained earnings/deficit - Start | 16656 |
| 3680 | Net income/loss | 28349 |
| 3700 | Dividends declared | 36900 |
| 3740 | Other items affecting retained earnings (rounding) | -1 |
| 3849 | Retained earnings/deficit - End | 8104 |

Source: `output/final_snapshot_20260127-081402/gifi_retained_earnings_FY2025.csv:1`

### Net income / Schedule 1 (tax purposes)

| Schedule 1 line | Description | Amount |
|---:|---|---:|
| 300 | Net income per financial statements | 28349 |
| 117 | 50% of meals and entertainment | 204 |
| 311 | Penalties and fines (CRA) | 274 |
| 400 | Net income for tax purposes | 28827 |

Source: `output/final_snapshot_20260127-081402/schedule_1_FY2025.csv:1`

### Tax on capital (if UFile asks)
- Eligible for capital tax exemption: **Yes** (small private corp; no capital tax payable expected).
- Total assets at year-end (from financial statements): **25,977** (GIFI `2599`).

## Suggested “Notes to Financial Statements” text (optional)

If UFile requires or you want to include a short note, here is a conservative pasteable option (edit names/dates as needed):

> The financial statements are management-prepared and unaudited. Revenue is derived from Shopify sales and cash receipts from operations. The corporation began charging/collecting GST/HST effective 2024-02-26. Inventory is recorded at cost; FY2024 closing inventory is an estimate and FY2025 closing inventory is based on a physical count performed on 2025-05-16 (near year-end). Certain expenses were initially paid personally by shareholders and reimbursed by the corporation; shareholder balances are reflected in the balance sheet.

