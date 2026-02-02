# UFile T2 completeness checklist (FY2024 + FY2025)

Purpose: make sure the fill guides are not “missing a screen” that UFile expects, and make common BCR blockers easy to resolve.

Authoritative year guides:
- `UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md`
- `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

## 0) Exported PDF package: verify schedule forms are actually included

UFile can reference schedules (e.g., “from Schedule 8”) without printing the actual schedule forms in the exported PDF, depending on export/print settings.

After exporting your UFile “package” PDF, run:

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2024 --pdf /path/to/ufile_export.pdf
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2025 --pdf /path/to/ufile_export.pdf
```

If it fails, re-export the PDF with the missing schedules included (or enter the schedule detail in UFile so it prints).

## 1) Most common “can’t file / no bar codes” causes (and the fix)

### A) `GIFI 100 does not balance`
Symptom:
- Message like: `GIFI field 2599 does not equal GIFI fields 3499+3620`

Almost always means one of:
- You typed a total/subtotal line (e.g., `2599`, `3499`, `3620`, `3640`, `9367`, `9368`) and it doesn’t match UFile’s internal subtotal; or
- Retained earnings rollforward is inconsistent (especially when dividends exist).

Fix:
- Clear any totals/subtotals (`2599`, `3499`, `3620`, `3640`, `9367`, `9368`, `3849`, `3600`).
- Re-enter only the **detail lines** listed in the year fill guide.
- If dividends exist: enter retained earnings rollforward lines (`3660`, `3680`, `3700`, `3740`) and let UFile compute `3849`/`3600`.

### B) `GIFI-Field 3849 does not match internal subtotal calculation`
Symptom:
- Message like: `GIFI-Field 3849:$X Calculation:$Y Difference:$Z`

Fix:
- Do **not** type `3849` or `3600`.
- Enter only the rollforward lines (`3660`, `3680`, `3700`, `3740`).
- Ensure `3700` matches the year’s dividend decision (FY2025 currently has `3700 = 36,900` from the accounting snapshot).

### C) Dividends declared but “Dividends paid” screen is missing
Symptom:
- Message like: “An amount entered in GIFI fields 3700 or 3701… ‘Dividends paid’ section is missing.”

Fix:
- Complete UFile’s **Dividends paid** screen:
  - Taxable dividends paid = the packet’s `dividends_paid.taxable_dividends_paid`
  - Eligible portion = `0` unless you explicitly decide/designate eligible dividends.
- If you ever set an eligible portion > 0, also complete the **GRIP** screen consistently.

## 2) Screen coverage (“did we answer every screen UFile expects?”)

### Always touch / verify (both years)
- Identification of the corporation (tax year-end, first return = No, NAICS, “Has GIFI financials?” = Yes).
- Head office + mailing + books & records addresses (carryforward addressee consistency from the filed 2023 return).
- Corporate officers / directors (make sure cease dates aren’t a carryforward artifact).
- Tax preparer (rep ID, email, address).
- Transactions with shareholders/officers/employees (high-level disclosure: reimbursements, shareholder loan, dividends if applicable).

### Corporate history (prior-year carryforward)
UFile’s “Corporate History” screen can require a minimal “1st prior year” row:
- Prior year end date
- Prior year taxable income (Schedule 1 code C of prior year)
- Taxable paid-up capital (generally matches share capital for this file)

The year fill guides include a ready-to-type “Corporate history carryforward” table.

### Dividends + GRIP (FY2025 only, if dividends exist)
- Dividends Paid screen must be completed if `3700` is non-zero.
- GRIP screen normally stays $0 / empty if dividends are non-eligible only, but UFile can still show the screen once dividends exist.

### Screens expected to be empty / “No” (both years)
The packet explicitly models these as “No”, with notes:
- Loss carryforwards/carrybacks
- Charitable donations
- Reserves
- CCA / depreciable property (check Schedule 8 outputs)
- Non-depreciable capital property
- Deferred income plans
- Status change for the corporation

If UFile forces a yes/no toggle on these screens, answer “No” and leave detail grids empty **unless** Schedule 8 / CCA is present in the packet.

## 3) Data entry rule that prevents most problems

Enter amounts on **detail lines**, not summary lines:
- Inventory: enter on `1121` (not `1120`)
- Prepaids: enter on `1484` (not `1480`)
- Revenue: enter `8000` (do not enter `8299`)
- COGS: enter `8300/8320/8500` (let UFile derive `8518`)
- Shareholder payable: use `2781` (if rejected, use `2780` as a fallback)
