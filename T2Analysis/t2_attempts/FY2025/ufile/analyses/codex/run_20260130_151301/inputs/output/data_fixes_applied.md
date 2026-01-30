# Data fixes applied

- fixes_file: /home/clarencehub/t2-final-fy2024-fy2025/overrides/data_fixes.yml
- dry_run: 0
- dedupe_bank_allocations_deleted_rows: 1

## Wave bill deletions

- wave_bill_id 50: deleted (bill_alloc=2, wave_matches=1, split_payments=0, funding=0, bank_alloc=0, journal_entries=2) — Duplicate Canadian Tire Gas bill (same vendor/date/amount as bill 49); both linked to the same CC payment bank_txn_id=1583.
- wave_bill_id 90: deleted (bill_alloc=8, wave_matches=1, split_payments=0, funding=0, bank_alloc=0, journal_entries=2) — Duplicate/mislinked Pharmasave bill: only one CC purchase exists ($62.54 Pharmasave cc_txn_id=4095), but this bill was matched to Costco gas cc_txn_id=4082.

## CC payment transfer links added

- bank_txn_id 1602 → wave_bill_id 89: inserted (bank_date=2023-10-20, invoice_date=2023-10-14) — Pharmasave CC purchase (cc_txn_id=4095) reimbursed via CC payment to Mastercard (bank_txn_id=1602) — exact amount match.
- bank_txn_id 1020 → wave_bill_id 365: inserted (bank_date=2024-09-18, invoice_date=2024-09-12) — Dollarama split-CC bill total ($321.65) reimbursed via CC payment to Mastercard (bank_txn_id=1020) — exact amount match.

Outputs:

- /home/clarencehub/t2-final-fy2024-fy2025/output/data_fixes_applied.md
- /home/clarencehub/t2-final-fy2024-fy2025/output/data_fixes_applied.csv
