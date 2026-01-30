# Wave bill CC settlement journals (AP → due-to-shareholder)

- Scope: 2023-06-01 → 2025-05-31
- Posted: 337
- Posted split CC settlements: 3
- Manual overrides used: 2
- Skipped (out of scope): 1
- Skipped (bill already has other payment evidence): 2
- Skipped (missing/zero bill total): 0
- Skipped (no CC payment link evidence): 0

Notes:
- This posts only AP-clearing entries for bills marked as credit-card-paid in the snapshot.
- Split CC payments clear AP partially using `fresher_debits__split_payments`.
- Bank CC payments are handled separately by bank debit journals (clearing due-to-shareholder).
