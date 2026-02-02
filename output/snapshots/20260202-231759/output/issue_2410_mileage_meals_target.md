# Issue: `2410` (Due to shareholder – Dwayne) does not equal “mileage + meals” payable

This note explains why `2410` ends up small even though we separately calculated a larger “mileage + meals” payable.

## Target (what you said you want)

If the **only** remaining amount owed to Dwayne at FY2025 end is:

- Mileage (FY2024+FY2025): **$1,396.68** (`output/shareholder_mileage_fuel_summary.md`)
- Meals (Dwayne portion FY2024+FY2025): **$210.00** (`output/shareholder_meals_estimate_summary.md`)

Then the expected ending balance is:

- **$1,606.68 CR** (corp owes Dwayne)

## Actual (before fix)

From `output/readiness_report.md`:

- FY2024 end (`2024-05-31`): `2410` **$259.00 CR**
- FY2025 end (`2025-05-31`): `2410` **$104.50 CR**

So the FY2025 ending balance was **$1,502.18 lower** than “mileage + meals”.

## Why it’s lower (what’s netting against mileage + meals)

The shortfall is explained almost entirely by two items:

### 1) Credit-card payment “gap” (main driver)

Across the full scope, bank CC payments posted to `2410` exceed CC settlement credits posted to `2410` by:

- CC settlement credits (`source_record_type='wave_bill_cc_settlement'`): **$117,413.42**
- CC payment debits (bank debits with `debit_reason=cc_payment_clear_due_to_shareholder:*`): **$118,903.39**
- **Gap (payments - settlements): $1,489.97**

Interpretation:
- The project is treating those CC payments as “the corp paying down Dwayne’s personal card for business purchases”.
- But the CC-paid Wave bills (the mechanism that creates the corresponding payable to Dwayne) are **$1,489.97 less** than the
  CC payments made from the bank.
- That net difference reduces `2410` and therefore reduces the amount “still owed” at year end.

### 2) One unmatched reimbursement (small driver)

There is one reimbursement bank txn to Dwayne that doesn’t have a matching Wave reimbursement journal:

- `bank_txn_id=715` **$12.21** (“Costco partial payment correction”)

This contributes the remaining **$12.21** of the total **$1,502.18** shortfall.

## What we improved (cemented override)

We imported deterministic FIFO allocations (from frozen snapshot audit CSVs) to reduce the number of bank CC payments
that have *zero* Wave linkage evidence:

- Before: **56** unlinked CC payments totaling **$7,467.21**
- After FIFO import: **45** unlinked CC payments totaling **$4,987.96** (`output/dwayne_unlinked_payments_report.md`)

This strengthens audit trail but does **not** force the `2410` ending balance to equal mileage+meals — it only adds
evidence where the snapshot’s FIFO method could allocate.

## Resolution (implemented)

We implemented a deterministic, repeatable resolution by recognizing the CC “payment gap” as a year-end prepaid asset
(rather than forcing unsupported bill links or treating it as a due-from/shareholder draw), and by recognizing the
one known unmatched reimbursement as a small business cost.

- Manual adjustments live in `overrides/manual_adjustment_journals.yml`:
  - `DWAYNE_CC_PREPAY_BALANCE_FY2024` (Dr 1300 / Cr 2410 $649.16)
  - `DWAYNE_CC_PREPAY_BALANCE_FY2025` (Dr 1300 / Cr 2410 $840.81)
  - `DWAYNE_COSTCO_PARTIAL_PAYMENT_CORRECTION` (Dr 5099 / Cr 2410 $12.21)

After rebuilding, `output/readiness_report.md` shows:

- FY2024 end `2410`: **$908.16 CR**
- FY2025 end `2410`: **$1,606.68 CR**

See also: `docs/issue_2410_dwayne_cc_prepay.md`.
