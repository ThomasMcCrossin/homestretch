# CRA HST summary (from CRA account export)

This report is derived from the imported CRA export tables in `db/t2_final.db`.
It is intended to support deterministic year-end HST payable modeling and remittance splitting (net tax vs interest/penalties).

## Periods (Net Tax vs Payments)

| period_end | net_tax | payment (bank_date) | bank_txn_id | delta (payment - net_tax) |
|---|---:|---:|---:|---:|
| 2024-03-31 | $3511.60 | $3774.16 (2024-11-13) | 835 | $262.56 |
| 2024-06-30 | $2943.26 | $3064.77 (2024-11-13) | 834 | $121.51 |
| 2024-09-30 | $2524.74 | $2542.18 (2024-11-29) | 798 | $17.44 |
| 2024-12-31 | $8231.53 | $8231.53 (2025-04-22) | 375 | $0.00 |
| 2025-03-31 | $2999.56 | $2999.56 (2025-06-26) | 298 | $0.00 |
| 2025-06-30 | $346.74 |  |  | $-346.74 |

## HST payable at corporate year-end (May 31)

### FY2024 (2023-06-01 → 2024-05-31)

- Net HST payable estimate at 2024-05-31: $6214.37
- Components:
  - 2024-03-31: $3511.60
  - 2024-06-30 (Apr-May portion): $2702.77

### FY2025 (2024-06-01 → 2025-05-31)

- Net HST payable estimate at 2025-05-31: $3346.30
- Components:
  - 2025-03-31: $2999.56
  - 2025-06-30 (Apr-May portion): $346.74

## Notes

- For CRA quarters ending June 30, the Apr-May portion is prorated using Shopify monthly tax as a weighting heuristic.
  - Rationale: June can be operational 'dead time', so a fixed 2/3 split can materially misstate the May 31 accrual.
- If Shopify weights are missing, the fallback is a simple 2/3 proration.
- FY2025 payable includes the Jan-Mar 2025 net tax if it was unpaid at May 31, 2025 (payment occurred after year-end).

## Outputs

- `output/cra_hst_period_summary.csv`

