# Readiness report (T2 FY2024/FY2025)

This is a snapshot-style status report intended to highlight what is complete, and what still needs a conscious decision.

## Bank coverage (hard requirement)

- Bank txns in scope: 1357
- Missing journalized bank lines: 0
- Duplicate bank journal lines: 0

## Trial balance highlights

### FY2024 (2023-06-01 → 2024-05-31)

- Net income: $16665.62
- Cash (1000+1070): $26291.52
- Accounts payable (2000): $3198.24 (CR)
- Due to shareholder Thomas (2400): $2669.99 (CR)
- Due to shareholder Dwayne (2410): $908.16 (CR)
- Due from shareholder (2500): $0.00 (CR)

### FY2025 (2024-06-01 → 2025-05-31)

- Net income: $31084.90
- Cash (1000+1070): $12471.83
- Accounts payable (2000): $7135.87 (CR)
- Due to shareholder Thomas (2400): $3403.90 (CR)
- Due to shareholder Dwayne (2410): $1606.68 (CR)
- Due from shareholder (2500): $2041.36 (DR)

## Wave bill payments (direct vendor payments)

- Posted entries: 176
- Mismatches (bank != matched bill totals): 2
- Net mismatch cents (sum diff_cents): -518 ($-5.18)

Top mismatches (by absolute diff):

- bank_txn_id 724 on 2024-12-16: bank $761.05 vs bills $766.33 (diff $-5.28)
- bank_txn_id 1081 on 2024-07-02: bank $155.64 vs bills $155.54 (diff $0.10)

## Wave bills reimbursed to shareholders (AP → due-to-shareholder reclass)

- Posted reclass entries: 188
- Allocations auto-scaled (explicit splits over-allocated): 1
- Net remainder cents (bank - bill allocations): 198083 ($1980.83)
- Detail: `output/wave_bill_reimbursement_journal_detail.csv`

## Wave bills paid by credit card (AP → due-to-shareholder reclass)

- Posted reclass entries: 340
- Total reclass cents (sum settlement amounts): 11741342 ($117413.42)
- Unlinked bank CC payments (no Wave bill link evidence): 45 totaling $4987.96
  - By FY: FY2024 $2833.91, FY2025 $2154.05
- Detail: `output/wave_bill_cc_settlement_journal_detail.csv`

## Split CC coverage (guardrail)

- Split CC bills in scope: 3
- Split CC total cents: 112165 ($1121.65)
- Under‑settled split CC bills: 0
- Over‑settled split CC bills: 0

## Due-from-shareholder drivers (bank debits posted to 2500)

- due_from_shareholder: $11000.00

Non-bank adjustments impacting `2500` (review as needed):

- mileage_fuel_payables: $41.36

## Remaining conscious decisions / blockers

- Credit card purchases are intentionally NOT journalized (Wave bills remain the expense source-of-truth).
- CC payments clear `2410` (due-to Dwayne); any debit balance in `2410` represents net owed back to the corp (optionally reclass to `2500`).
- Inventory balances posted (1200, 1210, 1220, 1230): FY2024 $2847.23, FY2025 $10015.47.
- No fixed-asset balances detected on Schedule 100, but CCA must be assessed separately via the tax asset register (`overrides/cca_assets.yml`) and Schedule 8 outputs.
