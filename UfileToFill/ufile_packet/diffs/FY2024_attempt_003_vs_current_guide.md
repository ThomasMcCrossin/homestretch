# UFile attempt vs current guide — FY2024 (attempt_003)

This report compares your **previous UFile attempt** (from the exported PDF parse bundle) to the **current fill guide** (authoritative enter-this source).

## Filing blockers (from your exported PDF package)
- **Schedule 8 missing from the PDF** (but current outputs claim CCA of 508). In UFile, enter assets on **Capital cost allowance** and re-export the package.
- **Schedule 7 missing from the PDF** (typical when there is taxable income and the small business deduction applies). In UFile, complete the SBD/GRIP section so SCH 7 is generated, then re-export the package.

## Quick answer
- Yes: the current guides are updated to reflect the latest asset + CCA/book overlay work.
- Your prior attempt differs materially from the current guide: CCA is expected (Schedule 8 claim 508); ensure Schedule 8 is entered in UFile.

## Highest-signal changes (what you will actually feel in UFile)
### Balance sheet / fixed assets
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|

### Income statement
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|

## Notes / reminders to apply (from the current guide)
### Must-check before filing / exporting
- Confirm the UFile tax year dates are **exactly** `2023-06-01` to `2024-05-31`.
- Confirm the T2 jacket address fields are filled (Head office + Mailing if different).
- On Schedule 125, fill the business/operation description fields if UFile leaves them blank.
- If you are claiming CCA: enter Schedule 8 via **Capital cost allowance** (do not rely on Schedule 1 alone).
- When you export/print a "package" PDF from UFile, make sure the export includes required schedule forms.

After exporting, run this completeness check (fails if required schedule forms like 8/88 are missing from the PDF):

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2024 --pdf /path/to/ufile_export.pdf
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
| A | Net income (loss) per financial statements | 18,456 |  |
| 104 | Accounting amortization | 508 |  |
| 121 | Non-deductible meals and entertainment (50%) | 259 |  |
| 128 | Non-deductible fines and penalties | 71 |  |
| 206 | Capital items expensed | 0 |  |
| 403 | Capital cost allowance (Schedule 8) | 508 |  |
| 500 | Total additions | 838 |  |
| 510 | Total deductions | 508 |  |
| C | Net income (loss) for tax purposes | 18,786 |  |
Note: If UFile auto-populates Schedule 1 line 403 from Schedule 8, do **not** manually enter 403 in the Schedule 1 grid.
CCA is entered on the **Capital cost allowance** screen from Schedule 8 (total CCA claimed: 508).

### Small business deduction (Schedule 7)
For a CCPC with active business income and positive taxable income, Schedule 7 is typically expected.

- In UFile, make sure the **small business deduction** section is completed (CCPC = Yes, no associated corps unless real).
- After your next PDF export, confirm the package includes **T2 SCH 7** (run the completeness checker in the Must-check section).

### High-signal yes/no answers
| Question | Answer | Note |
|---|---|---|
| T2 line 070 (first year after incorporation) | No | 2023 stub T2 (2022-12-08 → 2023-05-31) already answered Incorporation=Yes and filed Schedule 24; FY2024 should be No. |
| T2 line 180 (internet income/websites) | Yes | Shopify sales present; likely Yes for internet income/websites (Schedule 88). Confirm store domains in UFile. |
| T2 line 201 (book vs tax net income differs) | Yes | Book vs tax differs due to meals 50% add-back and CRA penalties; Schedule 1 is attached. |
| CCA required / capital assets | Yes | CCA claimed per Schedule 8. Total CCA: 508. Classes: 8, 50. |
| Book fixed assets present | Yes | Book fixed assets present (capitalized in GIFI). |

### Taxable dividend paid (UFile screen)
None.

### Notes to financial statements (copy/paste)
Paste into UFile (Notes checklist screen) if you are including notes with the filing copy:

```text
14587430 Canada Inc. (Curly's Canteen)
Notes to the financial statements
Year ended May 31, 2024

1. Nature of operations
The corporation carries on Quick Service Restaurant.

2. Basis of presentation
These financial statements have been prepared on the accrual basis of accounting using the historical cost basis.

3. Revenue recognition
Revenue is recognized at the time goods are sold and services are rendered. Amounts are presented net of refunds and discounts.

4. Inventory
Inventory consists of food and beverage inventory held for resale and is valued at the lower of cost and net realizable value. For FY2024, a formal physical inventory count process was implemented in the subsequent fiscal year; accordingly, the inventory balance at May 31, 2024 was estimated by management using an itemized schedule at cost.

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
| 8 | General equipment | 0 | 1,650 | 330 | 1,320 |
| 50 | Computer hardware and systems software | 0 | 648 | 178 | 470 |

### Schedule 8 asset additions (audit trail)
| Asset ID | Description | Date | Class | Cost |
|---|---|---|---|---|
| costco_freezer_2024_03_13 | Hisense freezer (Costco) | 2024-03-13 | 8 | 550 |
| ams_lb9_vending_machine_2024_02_20 | AMS-LB9 vending machine (Electric Kitty) | 2024-02-20 | 8 | 1,100 |
| costco_ipad_air_2023_12_08 | iPad Air 5 64GB (Costco) | 2023-12-08 | 50 | 648 |

### UFile Schedule 8 entry lines (per asset)
| Class | Addition description | Date acquired/available | Cost | Proceeds (if disposed) | Disposed description (if any) |
|---|---|---|---|---|---|
| 8 | Hisense freezer (Costco) | 2024-03-13 | 550 | 0 |  |
| 8 | AMS-LB9 vending machine (Electric Kitty) | 2024-02-20 | 1,100 | 0 |  |
| 50 | iPad Air 5 64GB (Costco) | 2023-12-08 | 648 | 0 |  |

## Balance sheet (GIFI Schedule 100) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 1599 |  | 29,788 | 0 | -29,788 | AUTO (do not type; ok if printed) |  |
| 2008 |  | 2,298 | 0 | -2,298 | AUTO (do not type; ok if printed) |  |
| 2009 |  | -508 | 0 | 508 | AUTO (do not type; ok if printed) |  |
| 2599 |  | 31,578 | 0 | -31,578 | AUTO (do not type; ok if printed) |  |
| 3139 |  | 13,022 | 0 | -13,022 | AUTO (do not type; ok if printed) |  |
| 3499 |  | 13,022 | 0 | -13,022 | AUTO (do not type; ok if printed) |  |
| 3600 |  | 18,456 | 0 | -18,456 | AUTO (do not type; ok if printed) |  |
| 3620 |  | 18,556 | 0 | -18,556 | AUTO (do not type; ok if printed) |  |
| 3640 |  | 31,578 | 0 | -31,578 | AUTO (do not type; ok if printed) |  |
| 1001 | Cash | 26,292 | 26,292 | 0 | OK |  |
| 1121 | Inventory of goods for sale | 2,847 | 2,847 | 0 | OK |  |
| 1484 | Prepaid expenses | 649 | 649 | 0 | OK |  |
| 1740 | Machinery, equipment, furniture and fixtures | 2,298 | 2,298 | 0 | OK |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -508 | -508 | 0 | OK |  |
| 2620 | Amounts payable and accrued liabilities | 2,687 | 2,687 | 0 | OK |  |
| 2680 | Taxes payable (GST/HST, etc.) | 6,757 | 6,757 | 0 | OK |  |
| 2781 | Due to individual shareholder(s) | 3,578 | 3,578 | 0 | OK | Tie-out: 2400 $2,669.99 (Thomas) + 2410 $908.16 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 3500 | Common shares | 100 | 100 | 0 | OK |  |

## Retained earnings rollforward — delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 3660 | Retained earnings/deficit - Start | 0 | 0 | 0 | OK | Enter (opening RE) |
| 3680 | Net income/loss | 18,456 | 18,456 | 0 | OK | Enter (net income/loss) |
| 3700 |  | 0 | 0 | 0 | OK | Enter (dividends declared) |
| 3740 |  | 0 | 0 | 0 | OK | Enter only if needed (rounding/other) |
| 3849 | Retained earnings/deficit - End | 18,456 | 18,456 | 0 | OK | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |

## Income statement (GIFI Schedule 125) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 8089 |  | 181,235 | 0 | -181,235 | AUTO (do not type; ok if printed) |  |
| 8299 |  | 181,235 | 0 | -181,235 | AUTO (do not type; ok if printed) |  |
| 8518 |  | 108,373 | 0 | -108,373 | AUTO (do not type; ok if printed) |  |
| 8519 |  | 72,862 | 0 | -72,862 | AUTO (do not type; ok if printed) |  |
| 9367 |  | 54,406 | 0 | -54,406 | AUTO (do not type; ok if printed) |  |
| 9368 |  | 162,779 | 0 | -162,779 | AUTO (do not type; ok if printed) |  |
| 9369 |  | 18,456 | 0 | -18,456 | AUTO (do not type; ok if printed) |  |
| 9970 |  | 18,456 | 0 | -18,456 | AUTO (do not type; ok if printed) |  |
| 9999 |  | 18,456 | 0 | -18,456 | AUTO (do not type; ok if printed) |  |
| 8000 | Trade sales of goods and services | 181,235 | 181,235 | 0 | OK |  |
| 8300 | Opening inventory | 0 | 0 | 0 | OK |  |
| 8320 | Purchases / cost of materials | 111,220 | 111,220 | 0 | OK | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 8500 | Closing inventory | 2,847 | 2,847 | 0 | OK |  |
| 8520 | Advertising and promotion | 1,606 | 1,606 | 0 | OK |  |
| 8523 | Meals and entertainment | 518 | 518 | 0 | OK | 50% add-back = $259 |
| 8622 | Employer's portion of employee benefits | 1,463 | 1,463 | 0 | OK |  |
| 8670 | Amortization of tangible assets | 508 | 508 | 0 | OK |  |
| 8690 | Insurance | 1,851 | 1,851 | 0 | OK |  |
| 8710 | Interest and bank charges | 2,218 | 2,218 | 0 | OK |  |
| 8810 | Office expenses | 1,998 | 1,998 | 0 | OK |  |
| 8813 | Data processing | 1,135 | 1,135 | 0 | OK | Computer hardware + SaaS (under capitalization threshold) |
| 8860 | Professional fees | 879 | 879 | 0 | OK |  |
| 8911 | Real estate rental | 8,235 | 8,235 | 0 | OK |  |
| 8960 | Repairs and maintenance | 429 | 429 | 0 | OK |  |
| 9060 | Salaries and wages | 23,485 | 23,485 | 0 | OK |  |
| 9130 | Supplies | 5,494 | 5,494 | 0 | OK | Packaging + operating supplies |
| 9131 | Small tools | 23 | 23 | 0 | OK |  |
| 9270 | Other expenses | 71 | 71 | 0 | OK | Includes CRA penalties $71 (non-deductible) |
| 9275 | Delivery, freight and express | 100 | 100 | 0 | OK |  |
| 9281 | Vehicle expenses | 4,393 | 4,393 | 0 | OK |  |

## Schedule 8 / CCA (UFile Capital cost allowance screen)
Expected classes (from the current guide):
| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---:|---:|---:|---:|
| 8 | General equipment | 0 | 1,650 | 330 | 1,320 |
| 50 | Computer hardware and systems software | 0 | 648 | 178 | 470 |

Expected asset additions (audit list):
| Asset ID | Description | Date | Class | Cost |
|---|---|---|---|---:|
| costco_freezer_2024_03_13 | Hisense freezer (Costco) | 2024-03-13 | 8 | 550 |
| ams_lb9_vending_machine_2024_02_20 | AMS-LB9 vending machine (Electric Kitty) | 2024-02-20 | 8 | 1,100 |
| costco_ipad_air_2023_12_08 | iPad Air 5 64GB (Costco) | 2023-12-08 | 50 | 648 |

UFile entry lines (per asset):
| Class | Addition description | Date acquired/available | Cost | Proceeds (if disposed) | Disposed description (if any) |
|---|---|---|---:|---:|---|
| 8 | Hisense freezer (Costco) | 2024-03-13 | 550 | 0 |  |
| 8 | AMS-LB9 vending machine (Electric Kitty) | 2024-02-20 | 1,100 | 0 |  |
| 50 | iPad Air 5 64GB (Costco) | 2023-12-08 | 648 | 0 |  |

PDF package form presence (from the attempt export):
- Schedule 8 form header present in PDF? **No**
- Schedule 7 form header present in PDF? **No**

If a schedule form is missing from the exported PDF, it usually means UFile didn’t include it in the export/print package settings (or the schedule detail wasn’t entered).

Run the checker after your next export:

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2024 --pdf /path/to/ufile_export.pdf
```
