# CC payment -> Wave linkage audit (read-only)

- DB (read-only): `/home/clarencehub/Fresh/Fresher/canteen_reconciliation_v2.db`
- Scope end_date (bank_txn_date <=): `2025-05-31`

## What this answers

- For each bank CC payment debit, how much is actually linked to Wave bills via `bank_allocations` (CC chain and manual split).
- Which Wave bills those allocations point to.
- Which CC purchases are Wave-matched but *not* linked to any bank CC payment (a gap in the chain).
- What merchants dominate unmatched CC purchases on the canteen cards.

## Card-level totals

- Card 8154: bank CC payments 161 totaling $89,082.19; wave-linked $16,168.12 (18.1%) across 23 payments
  - CC purchases (all): 440 totaling $73,706.59
  - CC payments (all, from CC data): 236 totaling $168,433.88
  - Wave-matched CC purchases: 23 totaling $15,455.79
- Card 0318: bank CC payments 203 totaling $29,821.20; wave-linked $16,647.62 (55.8%) across 119 payments
  - CC purchases (all): 589 totaling $129,615.90
  - CC payments (all, from CC data): 206 totaling $31,882.75
  - Wave-matched CC purchases: 135 totaling $17,574.85

## Files

- `cc_payment_bank_to_wave_coverage.csv`: one row per bank CC payment with wave allocation coverage
- `cc_payment_bank_to_wave_allocations.csv`: allocation detail rows (bank CC payment -> wave bill)
- `wave_matched_cc_purchases_without_bank_cc_payment_link.csv`: wave-matched CC purchases that are not linked to any bank CC payment (missing chain)
- `unmatched_cc_purchases_by_merchant_canteen_cards.csv`: unmatched CC purchases by merchant for canteen cards
