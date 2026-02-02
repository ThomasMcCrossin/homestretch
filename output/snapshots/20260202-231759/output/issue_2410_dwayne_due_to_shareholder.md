# Issue: `2410` (Due to shareholder – Dwayne) showed a debit balance

## Symptom (what looked “wrong”)

At FY2025 year‑end (**May 31, 2025**) `2410` briefly showed a **debit** balance (“Dwayne owes the corporation”), which contradicts the intended model: the corporation should generally owe Dwayne for business costs he personally paid (credit cards, reimbursements, mileage/meals, etc.).

## How `2410` is supposed to work in this project

For credit card funded business bills:

- When a Wave bill is paid on **Dwayne’s personal credit card**, we reclass the liability from vendor/AP to shareholder:
  - **Dr `2000` (Accounts payable)**  
  - **Cr `2410` (Due to shareholder – Dwayne)**
- When the corporation later pays the credit card from the bank:
  - **Dr `2410`**
  - **Cr `1000` (Bank)**

If the CC‑paid bills are fully captured, the **CC settlement credits** should be broadly offset by the **bank CC payments debits**, leaving `2410` in a reasonable credit position (net owed to Dwayne).

## Root cause (why it went wrong)

Some Wave bills were recorded as **split payments** (part credit card, part e‑transfer reimbursement / cash portion), using `fresher_debits__split_payments`.

The original CC settlement journalizer (`scripts/78_build_wave_bill_cc_settlement_journals.py`) only posted **full‑bill** AP→shareholder reclass entries. It did **not** post **partial** AP clearance for split CC components.

Result:

- The bank CC payments still debited `2410` (correct: the corp is paying the card),
- but the corresponding **credit** to `2410` for the **split CC bill portions** was missing,
- which pushed `2410` toward a debit balance.

## Evidence: the 3 missing credit components

These bills had explicit CC split rows but no CC settlement journal entry before the fix:

1. **Wave bill `365` – Dollarama – $321.65**
   - Split across 3 CC transactions in `fresher_debits__split_payments`:
     - `3495` $100.00
     - `3496` $100.00
     - `3497` $121.65

2. **Wave bill `486` – Costco – $654.74**
   - Split:
     - CC portion: `3326` $400.00
     - Bank reimbursement portion: $254.74 (handled by wave reimbursement journals)

3. **Wave bill `575` – Costco – $566.01**
   - Split:
     - CC portion: `3131` $400.00
     - Bank reimbursement portion: $166.01 (handled by wave reimbursement journals)

Total missing CC‑portion credits: **$1,121.65**.

## Fix implemented (deterministic, re‑runnable; no “facts” edited)

Updated `scripts/78_build_wave_bill_cc_settlement_journals.py` to:

- Detect bills that have explicit split CC rows (`fresher_debits__split_payments` where `txn_type='CC'`)
- Post **partial** AP→`2410` reclass entries for the CC portion only
  - Journal entry IDs: `WAVE_BILL_CC_SETTLE_SPLIT_<bill_id>_<cc_date>`
  - Amount: sum of CC split amounts **per CC txn date**
- Output now includes `settlement_amount_cents` in `output/wave_bill_cc_settlement_journal_detail.csv`

This keeps the system repeatable (reruns rebuild journals), and avoids manual DB editing.

## Result after rebuild

After rebuilding CC settlement + TB + readiness report:

- `2410` at FY2025 end is now **credit $237.14** (corp owes Dwayne), not debit. See `output/readiness_report.md`.

## Important clarification: “wave_bill_count=0” ≠ “no matching Wave bill”

Some Fresher audit outputs count only **bank-linked** Wave bills. They don’t include cases where the link is via **CC purchase matches** (`CC_PURCHASE` / `cc_txn_id`).

So a row like bank_txn **557** ($4,391.25) can show `wave_bill_count=0` in the *bank‑coverage* style report, even though it **is** correctly represented as a Wave bill and is correctly journalized via the CC‑purchase match path.

## What’s still open

`2410` being a small net credit at FY2025 end is now directionally correct. If you expect a much larger credit balance (e.g., mileage/meals payable), that’s a separate reconciliation step to confirm the mileage/meals journals and any other shareholder payables.

