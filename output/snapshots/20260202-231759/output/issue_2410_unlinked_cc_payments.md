# Issue: Unlinked CC payments (no Wave bill link) affecting `2410` (Due to shareholder – Dwayne)

## Symptom

There are **45** bank transactions classified as credit‑card payments in FY scope (**2023-06-01 → 2025-05-31**) totaling **$4,987.96** that have **no supporting linkage** to any Wave bill via:

- `fresher_debits__wave_matches` (`CC_PAYMENT_TRANSFER`)
- `fresher_debits__bank_allocations` (`target_type='WAVE_BILL'`)
- `fresher_debits__wave_bill_funding`
- `fresher_debits__split_payments` (`txn_type='BANK'`)
- `fresher_debits__wave_matches.cc_payment_txn_id` (any match type)

See the current exception list: `output/dwayne_unlinked_payments_report.md`.

### Why this matters

In `scripts/75_build_bank_debit_journals.py`, **unclassified** bank CC payments default to:

- **Dr `2410` (Due to shareholder – Dwayne)** / **Cr `1000` (Bank)**

That is correct **only if** the payment is reasonably understood to be clearing business expenses that were:

- paid on Dwayne’s personal cards, and
- captured elsewhere as Wave expenses/bills (and settled to `2410` via `wave_bill_cc_settlement` or reimbursed via `wave_bill_reimbursement`).

If a CC payment cannot be supported as business activity, it should **not** reduce `2410` — it is more consistent with a shareholder distribution/advance treatment (requires a policy decision).

## What the books currently say (high level)

Across FY2024+FY2025, `2410` is driven by:

- **Bank debits posted to `2410`**: $144,365.22 (debits)
- **Wave bill CC settlements posted to `2410`**: $117,413.42 (credits)
- **Wave bill reimbursements posted to `2410`**: $25,449.62 (credits)
- **Mileage payable posted to `2410`**: $1,396.68 (credits)
- **Meals estimate posted to `2410`**: $210.00 (credits)

Net ending position at FY2025 end is **$104.50 CR** (corp owes Dwayne). See `output/readiness_report.md`.

## Related “gap” concept (more audit-relevant than the raw unlinked-count)

There’s a separate, statement‑style reconciliation in `output/dwayne_cc_payment_gap_summary.md`:

- FY2024 gap: **$516.52** (bank CC payments exceed CC‑paid Wave bills by this amount)
- FY2025 gap: **$2,762.46**

Total: **$3,278.98**.

This **gap** is the amount that most directly represents “payments to the card(s) that are not explained by CC‑paid Wave bills” at a *year summary* level.

## Evidence examples (from the exception list)

From `output/dwayne_unlinked_payments_report.md`, some exceptions have a same‑amount CC purchase nearby (suggesting a 1:1 paydown pattern), but **still** have no Wave bill evidence:

- `bank_txn_id=1551` (2023-10-30) **$586.57** → CC purchase context: “MONCTONCASH&CARRY…”
- `bank_txn_id=350` (2025-05-13) **$408.58** → CC purchase context: “BELL ALIANT…”
- `bank_txn_id=1337` (2024-02-01) **$434.74** → CC purchase context: “AMHERST SUPERSTORE…”

Others have **no** nearby same-amount purchase context and **no** Wave bill candidates.

## Proposed next step (choose one)

This issue is inherently a **policy / evidence** decision. There isn’t a single “obvious” accounting fix without choosing how to treat unsupported CC payments.

### Option A (no DB changes; document + accept)

Treat the 45 items as an accepted limitation of not having a provable 1:1 mapping from bank CC payments → Wave bills.

- Pros: fastest; avoids inventing links; keeps Wave as expense source‑of‑truth.
- Cons: audit trail for a subset of CC payments remains weaker; requires comfort that the *net gap* is acceptable/explainable.

### Option B (strengthen linkage by adding missing expense evidence)

For any of the 45 that are truly business:

1) locate the missing vendor invoice/receipt, then
2) add it to the expense source‑of‑truth (Wave bill or a clearly labeled “external receipt” process), and
3) link/reclass accordingly (so it’s no longer an exception).

This is the cleanest “audit‑ready” outcome, but requires documents.

### Option C (reclass unsupported CC payments as shareholder distributions/advances)

If a CC payment can’t be supported as business, reclass it away from “clearing `2410`” (e.g., dividend/advance policy).

- Pros: prevents unsupported payments from understating `2410`.
- Cons: changes shareholder distribution totals; must align with how you want to treat these for tax reporting.

## Confirmation needed before implementation

Which path do you want for these 45 CC payments?

- **A**: leave as-is, just document (no accounting changes)
- **B**: try to locate invoices/receipts and add missing expenses
- **C**: reclass unsupported CC payments away from `2410` (dividend/advance policy)
