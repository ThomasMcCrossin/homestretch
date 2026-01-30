# Findings (fresh-eyes audit)

## 1) Your current reports are likely stale vs the DB

- DB mtime: `2026-01-15T16:02:30`
- Newest file in `output/latest`: `2026-01-15T09:55:14`
- If the DB is newer than `output/latest`, counts will “feel wrong” because you’re looking at old exports.

## 2) CC payments are mostly not Wave-linked (by design or missing data)

- Card 8154: 161 bank CC payments totaling $89,082.19; Wave-linked via `bank_allocations` $16,168.12 (18.1%).
  - Zero Wave-link payments: 138 totaling $72,914.07
- Card 0318: 203 bank CC payments totaling $29,821.20; Wave-linked via `bank_allocations` $16,647.62 (55.8%).
  - Zero Wave-link payments: 84 totaling $13,485.98

## 3) Wave bills matched to CC purchases (CC_PURCHASE only)

- Card 7022: 118 Wave bills matched via `match_type=CC_PURCHASE` totaling $69,445.16
- Card 0318: 129 Wave bills matched via `match_type=CC_PURCHASE` totaling $15,777.73
- Card 8154: 23 Wave bills matched via `match_type=CC_PURCHASE` totaling $15,455.79
- Card 4337: 28 Wave bills matched via `match_type=CC_PURCHASE` totaling $3,626.94

## 4) Systemic issue found: a CC purchase linked to multiple Wave bills breaks 06b matching

- CC purchase txn `387` 2025-05-12 card 0318 amount $408.58 merchant `BELL ALIANT OBM` has 4 `wave_matches` rows (split).
  - wave_match 635: SPLIT_PAYMENT -> wave_bill 674 (row 675) 2025-03-31 BELL $132.68
  - wave_match 636: SPLIT_PAYMENT -> wave_bill 691 (row 692) 2025-04-30 BELL $131.53
  - wave_match 637: SPLIT_PAYMENT -> wave_bill 695 (row 696) 2025-04-30 BELL $3.86
  - wave_match 638: SPLIT_PAYMENT -> wave_bill 715 (row None) 2025-02-27 OTHER $59.97
  - Matching bank CC payments by exact amount/card (examples):
    - bank_txn 350 2025-05-13 $408.58 Internet Banking INTERNET TRANSFER000000124759 4500*********
  - Why this matters: `06b_build_cc_payment_allocations.py` currently treats each wave_match row as a separate “candidate purchase”, so split purchases look ambiguous and are skipped (so the bank CC payment ends up 0% linked even though we have evidence).

## 5) Where to look next

- `cc_payment_bank_to_wave_coverage.csv` shows every bank CC payment and whether it links to Wave bills.
- `cc_payment_zero_wave_coverage_purchase_context.csv` gives quick context (what purchases happened since the prior payment) for the 0%-linked payments.
- If you want, I can propose a fix that (a) dedupes split purchases during matching and (b) allocates split purchases across their Wave bills instead of skipping them.
