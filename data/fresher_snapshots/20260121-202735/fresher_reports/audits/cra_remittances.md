# CRA Remittances / Debit Memos (Audit)

DB: `/home/clarencehub/Fresh/Fresher/canteen_reconciliation_v2.db`

Scope end date: `2025-05-31`

## Files

- CSV: `/home/clarencehub/Fresh/Fresher/output/audits/cra_remittances.csv`
- MD: `/home/clarencehub/Fresh/Fresher/output/audits/cra_remittances.md`

## Totals (by FY + kind)

| FY | kind | total |
|---|---|---:|
| FY2025 | GST_HST_REMIT | -17612.64 |
| FY2025 | PAYROLL_REMIT | -10048.56 |
| FY2025 | SERVICE_FEE | -24.00 |

## Notes

- `GST_HST_REMIT`: descriptions contain `GST-B-...` or `GST##-...`.
- `PAYROLL_REMIT`: descriptions contain `EMPTX-...` or `EMPBD-...`.
- `SERVICE_FEE`: `GPFS-SERVICE CHARGE`.
