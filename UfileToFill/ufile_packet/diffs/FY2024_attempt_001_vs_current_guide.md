# UFile attempt vs current guide — FY2024 (attempt_001)

This report compares your **previous UFile attempt** (from the exported PDF parse bundle) to the **current fill guide** (authoritative enter-this source).

## Quick answer
- Yes: the current guides are updated to reflect the latest asset + CCA/book overlay work.
- Your prior attempt differs materially from the current guide (most importantly: the **Costco iPad** is now treated as a **book fixed asset** with **book amortization mirroring tax CCA**).

## Highest-signal changes (what you will actually feel in UFile)
### Balance sheet / fixed assets
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 2781 | Due to individual shareholder(s) | 0 | 3,639 | 3,639 | ADD (missing in attempt) | Tie-out: 2400 $2,669.99 (Thomas) + 2410 $908.16 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 2780 |  | 3,578 | 0 | -3,578 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 1740 | Machinery, equipment, furniture and fixtures | 1,650 | 2,298 | 648 | CHANGE (update amount) |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -330 | -508 | -178 | CHANGE (update amount) |  |
| 2680 | Taxes payable (GST/HST, etc.) | 6,767 | 6,757 | -10 | CHANGE (update amount) |  |
| 3740 |  | 1 | 0 | -1 | CLEAR / DO NOT ENTER (extra in attempt) |  |

### Income statement
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 8320 | Purchases / cost of materials | 112,126 | 111,220 | -906 | CHANGE (update amount) | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 8810 | Office expenses | 1,370 | 1,998 | 628 | CHANGE (update amount) |  |
| 9270 | Other expenses | 346 | 71 | -275 | CHANGE (update amount) | Includes CRA penalties $71 (non-deductible) |
| 8670 | Amortization of tangible assets | 330 | 508 | 178 | CHANGE (update amount) |  |
| 9130 | Supplies | 5,561 | 5,494 | -67 | CHANGE (update amount) | Packaging + operating supplies |
| 9281 | Vehicle expenses | 4,403 | 4,454 | 51 | CHANGE (update amount) |  |
| 8960 | Repairs and maintenance | 458 | 429 | -29 | CHANGE (update amount) |  |

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
| A | Net income (loss) per financial statements | 18,395 |  |
| 104 | Accounting amortization | 508 |  |
| 121 | Non-deductible meals and entertainment (50%) | 259 |  |
| 128 | Non-deductible fines and penalties | 71 |  |
| 206 | Capital items expensed | 0 |  |
| 403 | Capital cost allowance (Schedule 8) | 508 |  |
| 500 | Total additions | 838 |  |
| 510 | Total deductions | 508 |  |
| C | Net income (loss) for tax purposes | 18,725 |  |
Note: If UFile auto-populates Schedule 1 line 403 from Schedule 8, do **not** manually enter 403 in the Schedule 1 grid.
CCA is entered on the **Capital cost allowance** screen from Schedule 8 (total CCA claimed: 508).

### High-signal yes/no answers
| Question | Answer | Note |
|---|---|---|
| T2 line 070 (first year after incorporation) | No | 2023 stub T2 (2022-12-08 → 2023-05-31) already answered Incorporation=Yes and filed Schedule 24; FY2024 should be No. |
| T2 line 180 (internet income/websites) | Yes | Shopify sales present; likely Yes for internet income/websites (Schedule 88). Confirm store domains in UFile. |
| T2 line 201 (book vs tax net income differs) | Yes | Book vs tax differs due to meals 50% add-back and CRA penalties; Schedule 1 is attached. |
| CCA required / capital assets | Yes | CCA claimed per Schedule 8. Total CCA: 508. Classes: 8, 50. |
| Book fixed assets present | Yes | Book fixed assets present (capitalized in GIFI). |

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
| 2781 | Due to individual shareholder(s) | 0 | 3,639 | 3,639 | ADD (missing in attempt) | Tie-out: 2400 $2,669.99 (Thomas) + 2410 $908.16 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 1740 | Machinery, equipment, furniture and fixtures | 1,650 | 2,298 | 648 | CHANGE (update amount) |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -330 | -508 | -178 | CHANGE (update amount) |  |
| 2680 | Taxes payable (GST/HST, etc.) | 6,767 | 6,757 | -10 | CHANGE (update amount) |  |
| 2780 |  | 3,578 | 0 | -3,578 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 3740 |  | 1 | 0 | -1 | CLEAR / DO NOT ENTER (extra in attempt) |  |
| 1599 |  | 29,788 | 0 | -29,788 | AUTO (do not type; ok if printed) |  |
| 2008 |  | 1,650 | 0 | -1,650 | AUTO (do not type; ok if printed) |  |
| 2009 |  | -330 | 0 | 330 | AUTO (do not type; ok if printed) |  |
| 2599 |  | 31,108 | 0 | -31,108 | AUTO (do not type; ok if printed) |  |
| 3139 |  | 13,032 | 0 | -13,032 | AUTO (do not type; ok if printed) |  |
| 3499 |  | 13,032 | 0 | -13,032 | AUTO (do not type; ok if printed) |  |
| 3600 |  | 17,976 | 0 | -17,976 | AUTO (do not type; ok if printed) |  |
| 3620 |  | 18,076 | 0 | -18,076 | AUTO (do not type; ok if printed) |  |
| 3640 |  | 31,108 | 0 | -31,108 | AUTO (do not type; ok if printed) |  |
| 3680 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |  |
| 3849 |  | 17,976 | 0 | -17,976 | AUTO (do not type; ok if printed) |  |
| 1001 | Cash | 26,292 | 26,292 | 0 | OK |  |
| 1121 | Inventory of goods for sale | 2,847 | 2,847 | 0 | OK |  |
| 1484 | Prepaid expenses | 649 | 649 | 0 | OK |  |
| 2620 | Amounts payable and accrued liabilities | 2,687 | 2,687 | 0 | OK |  |
| 3500 | Common shares | 100 | 100 | 0 | OK |  |

## Retained earnings rollforward — delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 3680 | Net income/loss | 17,975 | 18,395 | 420 | CHANGE (update amount) | Enter (net income/loss) |
| 3740 |  | 1 | 0 | -1 | CHANGE (update amount) | Enter only if needed (rounding/other) |
| 3849 | Retained earnings/deficit - End | 17,976 | 18,395 | 419 | CHANGE (update amount) | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |
| 3660 | Retained earnings/deficit - Start | 0 | 0 | 0 | OK | Enter (opening RE) |
| 3700 |  | 0 | 0 | 0 | OK | Enter (dividends declared) |

## Income statement (GIFI Schedule 125) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action | Guide note |
|---|---|---:|---:|---:|---|---|
| 8320 | Purchases / cost of materials | 112,126 | 111,220 | -906 | CHANGE (update amount) | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 8670 | Amortization of tangible assets | 330 | 508 | 178 | CHANGE (update amount) |  |
| 8810 | Office expenses | 1,370 | 1,998 | 628 | CHANGE (update amount) |  |
| 8960 | Repairs and maintenance | 458 | 429 | -29 | CHANGE (update amount) |  |
| 9130 | Supplies | 5,561 | 5,494 | -67 | CHANGE (update amount) | Packaging + operating supplies |
| 9270 | Other expenses | 346 | 71 | -275 | CHANGE (update amount) | Includes CRA penalties $71 (non-deductible) |
| 9281 | Vehicle expenses | 4,403 | 4,454 | 51 | CHANGE (update amount) |  |
| 8089 |  | 181,235 | 0 | -181,235 | AUTO (do not type; ok if printed) |  |
| 8299 |  | 181,235 | 0 | -181,235 | AUTO (do not type; ok if printed) |  |
| 8518 |  | 109,279 | 0 | -109,279 | AUTO (do not type; ok if printed) |  |
| 8519 |  | 71,956 | 0 | -71,956 | AUTO (do not type; ok if printed) |  |
| 9367 |  | 53,981 | 0 | -53,981 | AUTO (do not type; ok if printed) |  |
| 9368 |  | 163,260 | 0 | -163,260 | AUTO (do not type; ok if printed) |  |
| 9369 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |  |
| 9970 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |  |
| 9999 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |  |
| 8000 | Trade sales of goods and services | 181,235 | 181,235 | 0 | OK |  |
| 8300 | Opening inventory | 0 | 0 | 0 | OK |  |
| 8500 | Closing inventory | 2,847 | 2,847 | 0 | OK |  |
| 8520 | Advertising and promotion | 1,606 | 1,606 | 0 | OK |  |
| 8523 | Meals and entertainment | 518 | 518 | 0 | OK | 50% add-back = $259 |
| 8622 | Employer's portion of employee benefits | 1,463 | 1,463 | 0 | OK |  |
| 8690 | Insurance | 1,851 | 1,851 | 0 | OK |  |
| 8710 | Interest and bank charges | 2,218 | 2,218 | 0 | OK |  |
| 8813 | Data processing | 1,135 | 1,135 | 0 | OK | Computer hardware + SaaS (under capitalization threshold) |
| 8860 | Professional fees | 879 | 879 | 0 | OK |  |
| 8911 | Real estate rental | 8,235 | 8,235 | 0 | OK |  |
| 9060 | Salaries and wages | 23,485 | 23,485 | 0 | OK |  |
| 9131 | Small tools | 23 | 23 | 0 | OK |  |
| 9275 | Delivery, freight and express | 100 | 100 | 0 | OK |  |

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
