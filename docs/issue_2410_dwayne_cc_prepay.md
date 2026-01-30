# Issue #2 (implemented): Dwayne CC “prepay through Nov” and the `2410` CC payment gap

## Symptom

At both fiscal year-ends, `2410` (Due to Shareholder – Dwayne) was materially **lower** than the expected “mileage + meals” payable.

The root driver was that **bank credit-card payments posted to `2410` exceeded the CC-settlement credits posted to `2410`** (i.e., we paid Dwayne’s card more than the CC-paid Wave bills we reclassed AP→`2410` for).

## What this means (in plain English)

If we accept the policy constraint you stated as true:

- the corporation **did not** reimburse personal credit-card spending, and
- those “extra” payments were intentional and would be used to cover **future corporate charges** (your Bell strategy: pay ahead until ~Nov, then start fresh),

…then the “gap” is not an owner draw and it’s not Dwayne owing money back. It’s an **asset** at year-end: effectively a **credit/prepayment sitting on the card** that will be consumed by future business expenses.

## Evidence (Bell example)

The imported bank facts already include explicit Bell “prepay” notes on these FY2025 payments:

- `bank_txn_id=569` (2025-02-11) $132.68 note “Bell Aliant phone/internet”
- `bank_txn_id in {393, 394, 396, 397}` (2025-04-11) each $132.68 note:
  “FY-end Bell prepayment credit $663.40 carried forward to post-FY bills (Jun-Nov 2025).”

That $663.40 equals **5 × $132.68**, consistent with “prepay through (part of) FY2026”.

## Quantified CC payment gap (deterministic)

Defined as:

`sum( bank_debits to 2410 where debit_reason=cc_payment_clear_due_to_shareholder:* )`
minus
`sum( wave_bill_cc_settlement credits to 2410 )`

Results (from the existing journalized facts):

- FY2024 gap: **$649.16**
- FY2025 gap: **$840.81**
- Total at FY2025 end: **$1,489.97**

Additionally, there is one known unmatched reimbursement bank debit:

- `bank_txn_id=715` (2024-12-20) **$12.21** “Costco partial payment correction”

## Implemented accounting treatment (repeatable; no fact edits)

We model the CC gap as a year-end prepaid asset, not a shareholder receivable:

- At FY2024 end (2024-05-31):
  - Dr `1300` Prepaid Expenses **$649.16**
  - Cr `2410` Due to Shareholder – Dwayne **$649.16**
- At FY2025 end (2025-05-31):
  - Dr `1300` Prepaid Expenses **$840.81**
  - Cr `2410` Due to Shareholder – Dwayne **$840.81**

And we recognize the unmatched reimbursement as a business cost:

- 2024-12-20:
  - Dr `5099` COGS – Food – Other **$12.21**
  - Cr `2410` Due to Shareholder – Dwayne **$12.21**

These are encoded as deterministic manual adjustment journals in:

- `overrides/manual_adjustment_journals.yml` (`DWAYNE_CC_PREPAY_BALANCE_FY2024`, `DWAYNE_CC_PREPAY_BALANCE_FY2025`, `DWAYNE_COSTCO_PARTIAL_PAYMENT_CORRECTION`)

## Result (what you wanted)

After rebuild, `output/readiness_report.md` shows:

- FY2024 end `2410`: **$908.16 CR**
- FY2025 end `2410`: **$1,606.68 CR**

Which equals Dwayne’s “mileage + meals” payable for FY2024+FY2025 as previously calculated.

## Audit note / caveat

The FY2025 CC gap includes the explicitly documented Bell prepay credit **$663.40**. The remainder is treated as additional CC prepayment under your stated policy (“no personal reimbursements”).

If you later want to fully substantiate the remainder, the clean path is:

1) produce statements / bill-level evidence for the portion of CC payments not represented as CC-settled Wave bills in the period, and
2) either book missing Wave bills (expense+ITC) or keep as prepaid if it truly relates to post-FY costs.

