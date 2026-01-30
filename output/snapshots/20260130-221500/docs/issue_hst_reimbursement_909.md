# Issue: $2,000 HST reimbursement inside bank_txn 909 (CRA “Non-reporting period”)

## What happened (facts)

- `bank_txn_id=909` (2024-10-22) is a **$3,000 e-transfer to Thomas**.
- Wave-bill matching evidence ties **$1,000** of that transfer to Wave bills `720/721` (GFS).
- The remaining **$2,000** is not a Wave bill payment — it is an **HST payment to CRA** that Thomas paid personally and the corp reimbursed in the same transfer.

In the books, this is represented by the reimbursement journal:

- `WAVE_BILL_REIMBURSE_909`:
  - Dr `2000` Accounts payable: $1,000 (moves the Wave bills to shareholder-funded)
  - Dr `2200` HST payable: $2,000 (HST paid by shareholder; reimbursed)
  - Cr `2400` Due to shareholder – Thomas: $3,000

## Why CRA calls it “Non-reporting period” (and why that’s okay)

The CRA HST account export includes an internal holding bucket labelled **“Non-reporting period”**. Payments can land there first and later be transferred to a specific reporting period once the period exists/has been assessed.

For this specific $2,000:

- CRA shows a **Payment** effective 2024-10-22 in the “Non-reporting period”.
- CRA later shows a **transfer out** of that same $2,000 from the “Non-reporting period”.
- CRA then shows a **transfer in** of $2,000 to the **2024-03-31** reporting period.

So the $2,000 is **applied to a period** — it just moves through CRA’s internal staging bucket in the export.

## What this means for our T2 work

- This is not “missing” or “unexplained” money.
- It is an HST settlement that should stay in the accounting narrative as:
  - “HST paid by shareholder; reimbursed” (clears/affects HST payable).
- Any confusing wording like “non-reporting” should be treated as a **CRA export label**, not an accounting conclusion.

