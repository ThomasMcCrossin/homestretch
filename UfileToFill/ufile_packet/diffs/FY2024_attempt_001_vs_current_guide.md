# UFile attempt vs current guide — FY2024 (attempt_001)

This report compares your **previous UFile attempt** (from the exported PDF parse bundle) to the **current fill guide** (authoritative enter-this source).

## Quick answer
- Yes: the current guides are updated to reflect the latest asset + CCA/book overlay work.
- Your prior attempt differs materially from the current guide (most importantly: the **Costco iPad** is now treated as a **book fixed asset** with **book amortization mirroring tax CCA**).

## Highest-signal changes (what you will actually feel in UFile)
### Balance sheet / fixed assets
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|
| 2781 | Due to individual shareholder(s) | 0 | 3,578 | 3,578 | MOVE (enter 2781; if rejected, keep 2780) |
| 2780 |  | 3,578 | 0 | -3,578 | OK (fallback if 2781 rejected) |
| 1740 | Machinery, equipment, furniture and fixtures | 1,650 | 2,298 | 648 | CHANGE (update amount) |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -330 | -508 | -178 | CHANGE (update amount) |
| 2680 | Taxes payable (GST/HST, etc.) | 6,767 | 6,757 | -10 | CHANGE (update amount) |
| 3740 |  | 1 | 0 | -1 | CLEAR / DO NOT ENTER (extra in attempt) |

### Income statement
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|
| 8320 | Purchases / cost of materials | 112,126 | 111,220 | -906 | CHANGE (update amount) |
| 8810 | Office expenses | 1,370 | 1,998 | 628 | CHANGE (update amount) |
| 9270 | Other expenses | 346 | 71 | -275 | CHANGE (update amount) |
| 8670 | Amortization of tangible assets | 330 | 508 | 178 | CHANGE (update amount) |
| 9130 | Supplies | 5,561 | 5,494 | -67 | CHANGE (update amount) |
| 8960 | Repairs and maintenance | 458 | 429 | -29 | CHANGE (update amount) |
| 9281 | Vehicle expenses | 4,403 | 4,393 | -10 | CHANGE (update amount) |

## Balance sheet (GIFI Schedule 100) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|
| 2781 | Due to individual shareholder(s) | 0 | 3,578 | 3,578 | MOVE (enter 2781; if rejected, keep 2780) |
| 1740 | Machinery, equipment, furniture and fixtures | 1,650 | 2,298 | 648 | CHANGE (update amount) |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -330 | -508 | -178 | CHANGE (update amount) |
| 2680 | Taxes payable (GST/HST, etc.) | 6,767 | 6,757 | -10 | CHANGE (update amount) |
| 2780 |  | 3,578 | 0 | -3,578 | OK (fallback if 2781 rejected) |
| 3740 |  | 1 | 0 | -1 | CLEAR / DO NOT ENTER (extra in attempt) |
| 1001 | Cash | 26,292 | 26,292 | 0 | OK |
| 1121 | Inventory of goods for sale | 2,847 | 2,847 | 0 | OK |
| 1484 | Prepaid expenses | 649 | 649 | 0 | OK |
| 2620 | Amounts payable and accrued liabilities | 2,687 | 2,687 | 0 | OK |
| 3500 | Common shares | 100 | 100 | 0 | OK |
| 1599 |  | 29,788 | 0 | -29,788 | AUTO (do not type; ok if printed) |
| 2008 |  | 1,650 | 0 | -1,650 | AUTO (do not type; ok if printed) |
| 2009 |  | -330 | 0 | 330 | AUTO (do not type; ok if printed) |
| 2599 |  | 31,108 | 0 | -31,108 | AUTO (do not type; ok if printed) |
| 3139 |  | 13,032 | 0 | -13,032 | AUTO (do not type; ok if printed) |
| 3499 |  | 13,032 | 0 | -13,032 | AUTO (do not type; ok if printed) |
| 3600 |  | 17,976 | 0 | -17,976 | AUTO (do not type; ok if printed) |
| 3620 |  | 18,076 | 0 | -18,076 | AUTO (do not type; ok if printed) |
| 3640 |  | 31,108 | 0 | -31,108 | AUTO (do not type; ok if printed) |
| 3680 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |
| 3849 |  | 17,976 | 0 | -17,976 | AUTO (do not type; ok if printed) |

## Retained earnings rollforward — delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|
| 3680 | Net income/loss | 17,975 | 18,456 | 481 | CHANGE (update amount) |
| 3740 |  | 1 | 0 | -1 | CHANGE (update amount) |
| 3849 | Retained earnings/deficit - End | 17,976 | 18,456 | 480 | CHANGE (update amount) |
| 3660 | Retained earnings/deficit - Start | 0 | 0 | 0 | OK |
| 3700 |  | 0 | 0 | 0 | OK |

## Income statement (GIFI Schedule 125) — full delta table
| Code | Description | Attempt | Expected (current guide) | Delta (expected - attempt) | Action |
|---|---|---:|---:|---:|---|
| 8320 | Purchases / cost of materials | 112,126 | 111,220 | -906 | CHANGE (update amount) |
| 8670 | Amortization of tangible assets | 330 | 508 | 178 | CHANGE (update amount) |
| 8810 | Office expenses | 1,370 | 1,998 | 628 | CHANGE (update amount) |
| 8960 | Repairs and maintenance | 458 | 429 | -29 | CHANGE (update amount) |
| 9130 | Supplies | 5,561 | 5,494 | -67 | CHANGE (update amount) |
| 9270 | Other expenses | 346 | 71 | -275 | CHANGE (update amount) |
| 9281 | Vehicle expenses | 4,403 | 4,393 | -10 | CHANGE (update amount) |
| 8000 | Trade sales of goods and services | 181,235 | 181,235 | 0 | OK |
| 8300 | Opening inventory | 0 | 0 | 0 | OK |
| 8500 | Closing inventory | 2,847 | 2,847 | 0 | OK |
| 8520 | Advertising and promotion | 1,606 | 1,606 | 0 | OK |
| 8523 | Meals and entertainment | 518 | 518 | 0 | OK |
| 8622 | Employer's portion of employee benefits | 1,463 | 1,463 | 0 | OK |
| 8690 | Insurance | 1,851 | 1,851 | 0 | OK |
| 8710 | Interest and bank charges | 2,218 | 2,218 | 0 | OK |
| 8813 | Data processing | 1,135 | 1,135 | 0 | OK |
| 8860 | Professional fees | 879 | 879 | 0 | OK |
| 8911 | Real estate rental | 8,235 | 8,235 | 0 | OK |
| 9060 | Salaries and wages | 23,485 | 23,485 | 0 | OK |
| 9131 | Small tools | 23 | 23 | 0 | OK |
| 9275 | Delivery, freight and express | 100 | 100 | 0 | OK |
| 8089 |  | 181,235 | 0 | -181,235 | AUTO (do not type; ok if printed) |
| 8299 |  | 181,235 | 0 | -181,235 | AUTO (do not type; ok if printed) |
| 8518 |  | 109,279 | 0 | -109,279 | AUTO (do not type; ok if printed) |
| 8519 |  | 71,956 | 0 | -71,956 | AUTO (do not type; ok if printed) |
| 9367 |  | 53,981 | 0 | -53,981 | AUTO (do not type; ok if printed) |
| 9368 |  | 163,260 | 0 | -163,260 | AUTO (do not type; ok if printed) |
| 9369 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |
| 9970 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |
| 9999 |  | 17,975 | 0 | -17,975 | AUTO (do not type; ok if printed) |

## Schedule 8 / CCA (UFile Capital cost allowance screen)
Expected classes (from the current guide):
| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---:|---:|---:|---:|
| 8 | General equipment | 0 | 1,650 | 330 | 1,320 |
| 50 | Computer hardware and systems software | 0 | 648 | 178 | 470 |

PDF package form presence (from the attempt export):
- Schedule 8 form header present in PDF? **No**
- Schedule 7 form header present in PDF? **No**

If a schedule form is missing from the exported PDF, it usually means UFile didn’t include it in the export/print package settings (or the schedule detail wasn’t entered).

Run the checker after your next export:

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2024 --pdf /path/to/ufile_export.pdf
```
