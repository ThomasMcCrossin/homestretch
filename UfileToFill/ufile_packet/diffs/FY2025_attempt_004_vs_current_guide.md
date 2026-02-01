# UFile attempt vs current guide — FY2025 (attempt_004)

This report compares your **previous UFile attempt** (from the exported PDF parse bundle) to the **current fill guide** (authoritative enter-this source).

## Filing blockers (from your exported PDF package)
- **Schedule 8 missing from the PDF** (but current outputs claim CCA of 1,297). In UFile, enter assets on **Capital cost allowance** and re-export the package.
- **Schedule 7 missing from the PDF** (typical when there is taxable income and the small business deduction applies). In UFile, complete the SBD/GRIP section so SCH 7 is generated, then re-export the package.

## Quick answer
- Yes: the current guides are updated to reflect the latest asset + CCA/book overlay work.
- Your prior attempt differs materially from the current guide: the return now includes **book fixed assets** (GIFI 1740/1741) — your attempt export did not.

## Highest-signal changes (what you will actually feel in UFile)
### Balance sheet / fixed assets
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 3700 |  | -36,900 | 0 | 36,900 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 3660 |  | 16,656 | 0 | -16,656 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 1740 | Machinery, equipment, furniture and fixtures | 0 | 3,518 | 3,518 | ADD (missing in attempt) |  |
| 2620 | Amounts payable and accrued liabilities | 10,013 | 7,405 | -2,608 | CHANGE (update amount) |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | 0 | -1,805 | -1,805 | ADD (missing in attempt) |  |
| 2781 | Due to individual shareholder(s) | 5,097 | 5,011 | -86 | CHANGE (update amount) | Tie-out: 2400 $3,490.67 (Thomas) + 2410 $1,606.68 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 1301 | Due from individual shareholder(s) | 2,000 | 2,041 | 41 | CHANGE (update amount) | Shareholder loan receivable (Thomas). Review s.15(2) repayment/exception within 1 year after 2025-05-31. |
| 2680 | Taxes payable (GST/HST, etc.) | 2,663 | 2,653 | -10 | CHANGE (update amount) |  |

### Income statement
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 8710 | Interest and bank charges | 6,694 | 3,371 | -3,323 | CHANGE (update amount) |  |
| 8670 | Amortization of tangible assets | 0 | 1,297 | 1,297 | ADD (missing in attempt) |  |
| 8813 | Data processing | 1,878 | 2,915 | 1,037 | CHANGE (update amount) | Computer hardware + SaaS (under capitalization threshold) |
| 8810 | Office expenses | 3,903 | 2,939 | -964 | CHANGE (update amount) |  |
| 9281 | Vehicle expenses | 4,038 | 3,510 | -528 | CHANGE (update amount) |  |
| 8320 | Purchases / cost of materials | 117,452 | 117,342 | -110 | CHANGE (update amount) | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 9275 | Delivery, freight and express | 136 | 96 | -40 | CHANGE (update amount) |  |
| 8960 | Repairs and maintenance | 603 | 585 | -18 | CHANGE (update amount) |  |

## Notes / reminders to apply (from the current guide)
### Must-check before filing / exporting
- Confirm the UFile tax year dates are **exactly** `2024-06-01` to `2025-05-31`.
- Confirm the T2 jacket address fields are filled (Head office + Mailing if different).
- On Schedule 125, fill the business/operation description fields if UFile leaves them blank.
- If you are claiming CCA: enter Schedule 8 via **Capital cost allowance** (do not rely on Schedule 1 alone).
- When you export/print a "package" PDF from UFile, make sure the export includes required schedule forms.

After exporting, run this completeness check (fails if required schedule forms like 8/88 are missing from the PDF):

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2025 --pdf /path/to/ufile_export.pdf
```

### Income source screen (clears INCOMESOURCE warning)
Goal: avoid the UFile warning `INCOMESOURCE` and make the return explicit.

- In UFile → **Income source** screen:
  - Select **Active business income**.
  - Leave **property**, **foreign**, and other income sources unchecked unless you have real amounts.
  - Save and re-run diagnostics to confirm the warning clears.

Expected source for this file: **active business income only** (canteen operations).

### Schedule 1 (tax purposes)
| Code | Description | Amount | Calculation |
|---|---|---|---|
| A | Net income (loss) per financial statements | 31,007 |  |
| 104 | Accounting amortization | 1,297 |  |
| 121 | Non-deductible meals and entertainment (50%) | 204 |  |
| 128 | Non-deductible fines and penalties | 274 |  |
| 206 | Capital items expensed | 0 |  |
| 403 | Capital cost allowance (Schedule 8) | 1,297 |  |
| 500 | Total additions | 1,775 |  |
| 510 | Total deductions | 1,297 |  |
| C | Net income (loss) for tax purposes | 31,485 |  |
Note: If UFile auto-populates Schedule 1 line 403 from Schedule 8, do **not** manually enter 403 in the Schedule 1 grid.
CCA is entered on the **Capital cost allowance** screen from Schedule 8 (total CCA claimed: 1,297).

### Small business deduction (Schedule 7)
For a CCPC with active business income and positive taxable income, Schedule 7 is typically expected.

- In UFile, make sure the **small business deduction** section is completed (CCPC = Yes, no associated corps unless real).
- After your next PDF export, confirm the package includes **T2 SCH 7** (run the completeness checker in the Must-check section).

### High-signal yes/no answers
| Question | Answer | Note |
|---|---|---|
| T2 line 070 (first year after incorporation) | No | 2023 stub T2 already filed as first-year after incorporation (Schedule 24). FY2025 should be No. |
| T2 line 180 (internet income/websites) | Yes | Shopify sales present; likely Yes for internet income/websites (Schedule 88). Confirm store domains in UFile. |
| T2 line 201 (book vs tax net income differs) | Yes | Book vs tax differs due to meals 50% add-back and CRA penalties; Schedule 1 is attached. |
| CCA required / capital assets | Yes | CCA claimed per Schedule 8. Total CCA: 1297. Classes: 8, 12, 50. |
| Book fixed assets present | Yes | Book fixed assets present (capitalized in GIFI). |

### Taxable dividend paid (UFile screen)
Enter the taxable dividends paid details so Schedule 3 / Schedule 55 match the retained earnings rollforward.

- Total taxable dividends paid in the tax year: **36,900**
- Eligible portion: **0** (default expectation: $0 = non-eligible)

If UFile asks you to split between connected vs non-connected corporations, and these dividends were paid to individuals (shareholders), treat them as **other than connected corporations**.

### Notes to financial statements (copy/paste)
Paste into UFile (Notes checklist screen) if you are including notes with the filing copy:

```text
14587430 Canada Inc. (Curly's Canteen)
Notes to the financial statements
Year ended May 31, 2025

1. Nature of operations
The corporation carries on Quick Service Restaurant.

2. Basis of presentation
These financial statements have been prepared on the accrual basis of accounting using the historical cost basis.

3. Revenue recognition
Revenue is recognized at the time goods are sold and services are rendered. Amounts are presented net of refunds and discounts.

4. Inventory
Inventory consists of food and beverage inventory held for resale and is valued at the lower of cost and net realizable value. The inventory balance at May 31, 2025 is based on a physical count performed near year-end (May 16, 2025) and management adjustments for immaterial movements through year-end.

5. Property and equipment
Property and equipment are recorded at cost. Amortization is provided on a basis intended to approximate the decline in service potential of the related assets.

6. Income taxes and government remittances
The corporation is a Canadian-controlled private corporation. Income tax expense comprises current tax. Taxes payable on the balance sheet may include GST/HST and other government remittances.

7. Related party transactions and balances
The corporation is controlled by its shareholders. Amounts due to/from shareholders relate primarily to shareholder-paid business expenses and reimbursements and other amounts payable to shareholders. These balances are non-interest-bearing and due on demand unless otherwise agreed.

8. Subsequent events
There have been no subsequent events requiring adjustment to these financial statements.
```

### Capital cost allowance screen (Schedule 8 entry + audit)
Use Schedule 8 outputs; enter class details if claiming CCA.

If this section is missing/empty in the guide, the packet was likely built from a snapshot that did not include
`schedule_8_*.csv`. Rebuild via:
`python3 UfileToFill/ufile_packet/tools/refresh_packet_from_current_state.py`

### Schedule 8 / CCA
| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---|---|---|---|
| 8 | General equipment | 1,320 | 557 | 375 | 1,502 |
| 12 | Tools and utensils under $500 | 0 | 663 | 663 | 0 |
| 50 | Computer hardware and systems software | 470 | 0 | 259 | 211 |

### Schedule 8 asset additions (audit trail)
| Asset ID | Description | Date | Class | Cost |
|---|---|---|---|---|
| nayax_card_reader_2025_02_24 | Nayax card reader for vending machine | 2025-02-24 | 8 | 557 |
| walmart_coffee_grinder_2024_09_17 | Coffee grinder (Walmart) | 2024-09-17 | 12 | 184 |
| shopify_card_reader_2024_11_12 | Shopify card reader hardware | 2024-11-12 | 12 | 479 |

### UFile Schedule 8 entry lines (per asset)
| Class | Addition description | Date acquired/available | Cost | Proceeds (if disposed) | Disposed description (if any) |
|---|---|---|---|---|---|
| 8 | Nayax card reader for vending machine | 2025-02-24 | 557 | 0 |  |
| 12 | Coffee grinder (Walmart) | 2024-09-17 | 184 | 0 |  |
| 12 | Shopify card reader hardware | 2024-11-12 | 479 | 0 |  |

## Balance sheet (GIFI Schedule 100) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 1740 | Machinery, equipment, furniture and fixtures | 0 | 3,518 | 3,518 | ADD (missing in attempt) |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | 0 | -1,805 | -1,805 | ADD (missing in attempt) |  |
| 1301 | Due from individual shareholder(s) | 2,000 | 2,041 | 41 | CHANGE (update amount) | Shareholder loan receivable (Thomas). Review s.15(2) repayment/exception within 1 year after 2025-05-31. |
| 2620 | Amounts payable and accrued liabilities | 10,013 | 7,405 | -2,608 | CHANGE (update amount) |  |
| 2680 | Taxes payable (GST/HST, etc.) | 2,663 | 2,653 | -10 | CHANGE (update amount) |  |
| 2781 | Due to individual shareholder(s) | 5,097 | 5,011 | -86 | CHANGE (update amount) | Tie-out: 2400 $3,490.67 (Thomas) + 2410 $1,606.68 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 3660 |  | 16,656 | 0 | -16,656 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 3700 |  | -36,900 | 0 | 36,900 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 3740 |  | -1 | 0 | 1 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 1599 |  | 25,977 | 0 | -25,977 | AUTO (do not type; ok if printed) |  |
| 2599 |  | 25,977 | 0 | -25,977 | AUTO (do not type; ok if printed) |  |
| 3139 |  | 17,773 | 0 | -17,773 | AUTO (do not type; ok if printed) |  |
| 3499 |  | 17,773 | 0 | -17,773 | AUTO (do not type; ok if printed) |  |
| 3600 |  | 8,104 | 0 | -8,104 | AUTO (do not type; ok if printed) |  |
| 3620 |  | 8,204 | 0 | -8,204 | AUTO (do not type; ok if printed) |  |
| 3640 |  | 25,977 | 0 | -25,977 | AUTO (do not type; ok if printed) |  |
| 3680 |  | 28,349 | 0 | -28,349 | AUTO (do not type; ok if printed) |  |
| 3849 |  | 8,104 | 0 | -8,104 | AUTO (do not type; ok if printed) |  |
| 1001 | Cash | 12,472 | 12,472 | 0 | OK |  |
| 1121 | Inventory of goods for sale | 10,015 | 10,015 | 0 | OK | Physical count 2025-05-16 |
| 1484 | Prepaid expenses | 1,490 | 1,490 | 0 | OK |  |
| 3500 | Common shares | 100 | 100 | 0 | OK |  |

## Retained earnings rollforward — delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 3660 | Retained earnings/deficit - Start | 16,656 | 18,456 | 1,800 | CHANGE (update amount) | Enter (opening RE) |
| 3680 | Net income/loss | 28,349 | 31,007 | 2,658 | CHANGE (update amount) | Enter (net income/loss) |
| 3700 | Dividends declared | -36,900 | 36,900 | 73,800 | CHANGE (update amount) | Enter (dividends declared) |
| 3849 | Retained earnings/deficit - End | 8,104 | 12,562 | 4,458 | CHANGE (update amount) | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |
| 3740 | Other items affecting retained earnings (rounding) | -1 | -1 | 0 | OK | Enter only if needed (rounding/other) |

## Income statement (GIFI Schedule 125) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 8670 | Amortization of tangible assets | 0 | 1,297 | 1,297 | ADD (missing in attempt) |  |
| 8320 | Purchases / cost of materials | 117,452 | 117,342 | -110 | CHANGE (update amount) | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 8710 | Interest and bank charges | 6,694 | 3,371 | -3,323 | CHANGE (update amount) |  |
| 8810 | Office expenses | 3,903 | 2,939 | -964 | CHANGE (update amount) |  |
| 8813 | Data processing | 1,878 | 2,915 | 1,037 | CHANGE (update amount) | Computer hardware + SaaS (under capitalization threshold) |
| 8960 | Repairs and maintenance | 603 | 585 | -18 | CHANGE (update amount) |  |
| 9130 | Supplies | 4,629 | 4,620 | -9 | CHANGE (update amount) | Packaging + operating supplies |
| 9275 | Delivery, freight and express | 136 | 96 | -40 | CHANGE (update amount) |  |
| 9281 | Vehicle expenses | 4,038 | 3,510 | -528 | CHANGE (update amount) |  |
| 8089 |  | 230,907 | 0 | -230,907 | AUTO (do not type; ok if printed) |  |
| 8299 |  | 230,907 | 0 | -230,907 | AUTO (do not type; ok if printed) |  |
| 8518 |  | 110,284 | 0 | -110,284 | AUTO (do not type; ok if printed) |  |
| 8519 |  | 120,623 | 0 | -120,623 | AUTO (do not type; ok if printed) |  |
| 9367 |  | 92,274 | 0 | -92,274 | AUTO (do not type; ok if printed) |  |
| 9368 |  | 202,558 | 0 | -202,558 | AUTO (do not type; ok if printed) |  |
| 9369 |  | 28,349 | 0 | -28,349 | AUTO (do not type; ok if printed) |  |
| 9970 |  | 28,349 | 0 | -28,349 | AUTO (do not type; ok if printed) |  |
| 9999 |  | 28,349 | 0 | -28,349 | AUTO (do not type; ok if printed) |  |
| 8000 | Trade sales of goods and services | 230,907 | 230,907 | 0 | OK |  |
| 8300 | Opening inventory | 2,847 | 2,847 | 0 | OK |  |
| 8500 | Closing inventory | 10,015 | 10,015 | 0 | OK |  |
| 8520 | Advertising and promotion | 798 | 798 | 0 | OK |  |
| 8523 | Meals and entertainment | 408 | 408 | 0 | OK | 50% add-back = $204 |
| 8622 | Employer's portion of employee benefits | 3,610 | 3,610 | 0 | OK |  |
| 8690 | Insurance | 1,951 | 1,951 | 0 | OK |  |
| 8860 | Professional fees | 353 | 353 | 0 | OK |  |
| 8911 | Real estate rental | 7,137 | 7,137 | 0 | OK |  |
| 9060 | Salaries and wages | 54,899 | 54,899 | 0 | OK |  |
| 9131 | Small tools | 479 | 479 | 0 | OK |  |
| 9225 | Telephone and telecommunications | 465 | 465 | 0 | OK | Internet |
| 9270 | Other expenses | 293 | 293 | 0 | OK | Includes CRA penalties $274 (non-deductible) |

## Schedule 8 / CCA (UFile Capital cost allowance screen)
Expected classes (from the current guide):
| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---:|---:|---:|---:|
| 8 | General equipment | 1,320 | 557 | 375 | 1,502 |
| 12 | Tools and utensils under $500 | 0 | 663 | 663 | 0 |
| 50 | Computer hardware and systems software | 470 | 0 | 259 | 211 |

Expected asset additions (audit list):
| Asset ID | Description | Date | Class | Cost |
|---|---|---|---|---:|
| nayax_card_reader_2025_02_24 | Nayax card reader for vending machine | 2025-02-24 | 8 | 557 |
| walmart_coffee_grinder_2024_09_17 | Coffee grinder (Walmart) | 2024-09-17 | 12 | 184 |
| shopify_card_reader_2024_11_12 | Shopify card reader hardware | 2024-11-12 | 12 | 479 |

UFile entry lines (per asset):
| Class | Addition description | Date acquired/available | Cost | Proceeds (if disposed) | Disposed description (if any) |
|---|---|---|---:|---:|---|
| 8 | Nayax card reader for vending machine | 2025-02-24 | 557 | 0 |  |
| 12 | Coffee grinder (Walmart) | 2024-09-17 | 184 | 0 |  |
| 12 | Shopify card reader hardware | 2024-11-12 | 479 | 0 |  |

PDF package form presence (from the attempt export):
- Schedule 8 form header present in PDF? **No**
- Schedule 7 form header present in PDF? **No**

If a schedule form is missing from the exported PDF, it usually means UFile didn’t include it in the export/print package settings (or the schedule detail wasn’t entered).

Run the checker after your next export:

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2025 --pdf /path/to/ufile_export.pdf
```
