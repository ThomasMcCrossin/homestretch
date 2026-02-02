# Jesse Goodwin: bank payroll payments vs payroll CSV exports (FY2024)

Scope: 2023-06-01 → 2024-05-31 (FY2024)

## Totals

- Export net pay total (CSV-derived): **$4,733.29**
- Bank payroll paid (categorized payroll, “Jesse”): **$5,191.25**
- Bank minus export net: **$457.96**
- Bank payments with no nearby export pay period end (±14 days): **$247.28** across **3** txns

## Bank payments that do not match any export pay period (by date proximity)

| bank_txn_id | txn_date | amount | verified | note |
|---:|---|---:|---:|---|
| 1366 | 2024-01-22 | $41.01 | 0 | no export pay period end within 14 days |
| 1367 | 2024-01-22 | $91.45 | 0 | no export pay period end within 14 days |
| 1362 | 2024-01-23 | $114.82 | 0 | no export pay period end within 14 days |

These are the cleanest “no CSV match” candidates: there is no export pay period end within the chosen window.

## Pay periods where bank-paid amount differs from export net pay

Assignment rule: each bank payment is assigned to the nearest export `pay_period_end` within ±14 days.

| pay_period_end | export_net | bank_sum | delta | bank_txns |
|---|---:|---:|---:|---:|
| 2023-09-17 | $88.63 | $349.71 | $261.08 | 2 |
| 2023-12-10 | $194.62 | $266.87 | $72.25 | 2 |
| 2023-11-05 | $372.16 | $352.29 | $-19.87 | 1 |
| 2023-10-29 | $326.33 | $310.03 | $-16.30 | 1 |
| 2023-11-12 | $278.15 | $264.97 | $-13.18 | 1 |
| 2023-10-22 | $279.64 | $266.46 | $-13.18 | 1 |
| 2023-10-08 | $279.64 | $266.46 | $-13.18 | 1 |
| 2023-10-01 | $276.25 | $263.60 | $-12.65 | 1 |
| 2024-03-03 | $212.16 | $200.02 | $-12.14 | 1 |
| 2023-11-26 | $221.33 | $211.95 | $-9.38 | 1 |
| 2023-11-19 | $177.07 | $170.36 | $-6.71 | 1 |
| 2023-10-15 | $177.07 | $170.36 | $-6.71 | 1 |

### Detail: 2023-09-17 (delta $261.08)

Export rows:

| source_row | gross | net |
|---:|---:|---:|
| 4 | $90.00 | $88.63 |

Assigned bank txns:

| bank_txn_id | txn_date | amount | days_from_end |
|---:|---|---:|---:|
| 1669 | 2023-09-13 | $127.50 | 4 |
| 1663 | 2023-09-18 | $222.21 | 1 |

### Detail: 2023-12-10 (delta $72.25)

Export rows:

| source_row | gross | net |
|---:|---:|---:|
| 16 | $206.25 | $194.62 |

Assigned bank txns:

| bank_txn_id | txn_date | amount | days_from_end |
|---:|---|---:|---:|
| 1448 | 2023-12-11 | $72.25 | 1 |
| 1449 | 2023-12-11 | $194.62 | 1 |

### Detail: 2023-11-05 (delta $-19.87)

Export rows:

| source_row | gross | net |
|---:|---:|---:|
| 11 | $401.25 | $372.16 |

Assigned bank txns:

| bank_txn_id | txn_date | amount | days_from_end |
|---:|---|---:|---:|
| 1524 | 2023-11-06 | $352.29 | 1 |

## Data quality note: export row with gross but blank net

At least one export row has a non-zero gross pay but a blank/zero net pay. Example:

| pay_period_end | source_row | gross | net |
|---|---:|---:|---:|
| 2023-12-31 | 19 | $91.45 | $0.00 |

This can cause “bank vs export net” mismatches even when the bank payment was legitimate payroll.