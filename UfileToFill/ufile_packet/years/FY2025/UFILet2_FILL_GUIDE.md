# UFile T2 Fill Guide — FY2025

**Entity:** 14587430 Canada Inc. (Curly's Canteen)
**BN:** 748003142RC0001
**Tax year:** 2024-06-01 → 2025-05-31 (year-end 05-31)
**NAICS:** 722512

**Readable view:** open `UFILet2_FILL_GUIDE.html` (bigger text + no horizontal scroll).
**Audit package (working papers):** open `audit_packages/FY2025/index.html`.
**Review remediation pack (memos):** `audit_packages/FY2025/inventory_margin_memo.html`, `audit_packages/FY2025/fixed_asset_cca_continuity.html`, `audit_packages/FY2025/payables_breakdown.html`.

## UFile entry rules (important)
- Enter amounts on the **detail lines** listed below (e.g., use `1121` for inventory, `1484` for prepaid).
- Leave totals like `1599`/`2599`/`3499`/`3640` blank; UFile usually auto-calculates them. If it doesn’t, confirm you used the detail lines (especially `1121`, `1484`, `2781`), then use the tie-check totals below.
- On Schedule 125, enter **trade sales** on `8000` (and do **not** enter `8299` total revenue). UFile will compute totals from the detail lines.

## If something looks wrong in UFile (fast troubleshooting)
- If inventory isn’t included in current assets: ensure it’s entered on **`1121`** (not `1120`).
- If prepaids aren’t included in current assets: ensure it’s entered on **`1484`** (not `1480`).
- If shareholder payable isn’t included: try **`2781`**; if UFile rejects it, enter the same amount on **`2780`**.
- If totals don’t match: delete anything typed into subtotal/total lines (`1599`, `2599`, `3640`, `8299`, `9367`, `9368`, etc.) and re-enter only the detail lines.
- If Net income screen totals look inflated: you likely double-entered revenue (e.g., `8000` + `8299`). Only enter `8000` and let UFile total it.
- If you see diagnostics like “`GIFI-FIELD 9367 does not match internal subtotal calculation`”: a total/subtotal line is being populated inconsistently with the expense detail lines. Clear totals (`9367`/`9368`) and rely on the detail expense lines only.
- If you see diagnostics like “`GIFI-FIELD 3849 does not match internal subtotal calculation`”: retained earnings end (`3849`) / balance sheet retained earnings (`3600`) does not match the retained earnings rollforward. Enter only the rollforward lines (`3660`, `3680`, `3700`, `3740`) and let UFile compute `3849`/`3600`.

## Key carryforward fields (match 2023 filing)
| Field | Value |
|---|---|
| Mailing addressee | Dwayne Ripley |
| Books & records addressee | Curly's |
| Head office street | 125 Victoria St E |
| Head office city/prov/postal | Amherst, NS B4H1X9 |

## Key positions / elections (high signal)
| Item | Value | Note |
|---|---|---|
| IFRS used? | No | Financial statements not prepared using IFRS |
| Practitioner involvement | none | Management-prepared, unaudited |
| Functional currency | CAD | No functional currency election |
| Language of correspondence | English | Code 1 |
| Corporation type | CCPC |  |
| Associated corporations? | No | No associated corporations |
| Tax on capital exempt? | Yes | Small private corp; no capital tax payable expected |
| HST registration date | 2024-02-26 | Corp began charging/collecting HST on this date |
| HST reported this year? | Yes | Full year of HST collection |
| Inventory method | cost | Physical count 2025-05-16 (near year-end) |
| Tips handling | paid_on_top | FY2025 tips were paid out each pay period: in Dec 2024 tips were embedded into gross+vacation and had deductions taken; in 2025 tips were paid on top of net pay (no deductions). |
| Shareholder loan at year-end? | Yes | Shareholder loan receivable exists at year-end. Review s.15(2) repayment timing and any applicable exceptions. |

## Must-check before filing / exporting a PDF copy
- Confirm the UFile tax year dates are **exactly** `2024-06-01` to `2025-05-31`.
- Confirm the T2 jacket address fields are filled (Head office + Mailing if different).
- On Schedule 125, fill the business/operation description fields if UFile leaves them blank.
- If you are claiming CCA: enter Schedule 8 via **Capital cost allowance** (do not rely on Schedule 1 alone).
- When you export/print a "package" PDF from UFile, make sure the export includes required schedule forms.

After exporting, run this completeness check (fails if required schedule forms like 8/88 are missing from the PDF):

```bash
python3 T2Analysis/tools/check_ufile_export_completeness.py --fy FY2025 --pdf /path/to/ufile_export.pdf
```

## Identification of the corporation (UFile screen)
| Field | Value | Note |
|---|---|---|
| Corporation name | 14587430 Canada Inc. |  |
| Business number | 748003142RC0001 |  |
| Tax year end | 2025-05-31 |  |
| One-month extension of balance due date? | No | Carryforward from prior UFile exports; review CCPC/SBD eligibility if you want the extension. |
| Charter jurisdiction | Federal |  |
| Incorporation date | 2022-12-08 |  |
| Beginning date of operations | 2023-06-10 |  |
| First federal return? | No | 2023 stub return was the first return; FY2024/FY2025 should be No. |
| Final federal return? | No |  |
| Permanent establishment province | Nova Scotia |  |
| Language of correspondence | English |  |
| Corporation email | tom@curlys.ca |  |
| Active/inactive status | Regular corp. (specify activity) |  |
| Activity description | Quick Service Restaurant |  |
| NAICS | 722512 |  |
| Principal products/services | Canteen in an Arena (100%) |  |
| Has GIFI financials? | Yes | Must be Yes or UFile may wipe GIFI entries. |
| Construction subcontractors? |  | UFile asks this only if your major business activity is construction; not applicable for a canteen/restaurant. |
| Internet income from websites? | Yes |  |
| # of websites | 1 |  |
| % gross revenue from internet | 4.78 | Computed from Shopify “Net payments by gateway” by sales channel: (Online Store + Shop) / (all channels). |
| Top URL(s) | curlyscanteen.ca |  |
| Quarterly instalments – wants considered? | Yes |  |
| Quarterly instalments – perfect compliance? | No |  |

## Tax preparer (UFile screen)
| Field | Value |
|---|---|
| Addressee | Thomas McCrossin |
| Position/title | Income Tax Preperation |
| Contact first name | Thomas |
| Contact last name | McCrossin |
| Phone (day) | (902) 321-6749 |
| Fax | (000) 000-0000 |
| Federal rep ID | JC98XW5 |
| Email | thomas.mccrossin@outlook.com |
| Street | 31 Duckling Dell |
| City | Amherst |
| Province | Nova Scotia |
| Postal code | B4H 3Y2 |

Leave **Notes** and **Override** sections blank unless you intentionally need them.

## EFILE setup (UFile screen)
Leave default settings unless you are explicitly instructed to change EFILE options.

## Head office address (UFile screen)
| Field | Value |
|---|---|
| Addressee | Dwayne Ripley |
| Street | 125 Victoria St E |
| Additional address info |  |
| Suite number |  |
| Post office box number |  |
| City | Amherst |
| Province | Nova Scotia |
| Postal code | B4H 1X9 |
| Person to contact | Dwayne Ripley |
| Phone (day) | (902) 667-2875 |
| Fax | (000) 000-0000 |
| Changed since last return? | No Change |

## Other addresses (UFile screen)
| Field | Value |
|---|---|
| Addressee | Curly's |
| Street | 125 Victoria St E |
| Additional address info |  |
| Suite number |  |
| City | Amherst |
| Province | Nova Scotia |
| State |  |
| Postal code | B4H 1X9 |
| U.S.A. ZIP code |  |
| Foreign postal code |  |
| Country (if other than Canada) |  |
| Person to contact | Thomas McCrossin |
| Phone (day) | (902) 321-6749 |
| Fax | (000) 000-0000 |
| Changed since last return? | No Change |

## Mailing address of the corporation (UFile screen)
| Field | Value |
|---|---|
| Addressee | Dwayne Ripley |
| Street | 125 Victoria St E |
| Additional address info |  |
| Suite number |  |
| Post office box number |  |
| City | Amherst |
| Province | Nova Scotia |
| State |  |
| Postal code | B4H 1X9 |
| U.S.A. ZIP code |  |
| Foreign postal code |  |
| Country (if other than Canada) |  |
| Person to contact | Thomas McCrossin |
| Phone (day) | (902) 321-6749 |
| Fax | (000) 000-0000 |
| Changed since last return? | No Change |

## Corporate officers (UFile screen)
| Name | Title | Signing officer? | Elected | Ceased | Non-resident? | Also shareholder? | SIN | Voting/Common/Pref % | Address | Phone | Fax |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas McCrossin | Vice-president | No | 2022-12-09 | 2022-12-09 | No | Yes | XXX-XXX-XXX | 25/25/25 | 31 Duckling Dell, Amherst Nova Scotia B4H 3Y2 | (902) 321-6749 | (000) 000-0000 |
| Dwayne Ripley | President | Yes | 2022-12-08 |  | No | Yes | XXX-XXX-XXX | 75/75/75 | 28 Charles St, Amherst Nova Scotia B4H 3P8 | (902) 669-2700 | (000) 000-0000 |

- Has there been a change of directors since the last return? **No**
- Previous shareholder names: leave blank (no name changes).
- Date the return is signed: fill on filing/signing day (do not carry forward stale dates).

**Note:** If a director “ceased date” is a carryforward artifact but the person is still a director, leave the ceased date blank in UFile for the current filing.

## Director (UFile screen)
Use the same director details as listed under **Corporate officers**.

## Director and signing officer (UFile screen)
Signing officer is **Dwayne Ripley** (see Corporate officers table).

## GIFI Import (UFile screen)
If using a GIFI import file, import once before manual edits; otherwise skip this screen.

## GIFI (UFile screen)
- In the main GIFI screen, select: **Update Net income and Tax on capital pages from GIFI**.
- IFRS used? **No**.

## Balance sheet (GIFI Schedule 100)
**Important:** If you complete the retained earnings rollforward (3660/3680/3700/3740), do **not** manually type retained earnings on Schedule 100 (`3600`)—UFile should populate it from the rollforward. Typing `3600` (or `3849`) can trigger BCR errors like “GIFI-FIELD 3849 does not match internal subtotal calculation.”

| GIFI | Description | Amount | Note |
|---|---|---|---|
| 1001 | Cash | 12,472 |  |
| 1121 | Inventory of goods for sale | 10,015 | Physical count 2025-05-16 |
| 1301 | Due from individual shareholder(s) | 2,041 | Shareholder loan receivable (Thomas). Review s.15(2) repayment/exception within 1 year after 2025-05-31. |
| 1484 | Prepaid expenses | 1,490 |  |
| 1740 | Machinery, equipment, furniture and fixtures | 3,518 |  |
| 1741 | Accum amort - machinery/equip/furn/fixtures | -1,582 |  |
| 2620 | Amounts payable and accrued liabilities | 7,405 |  |
| 2680 | Taxes payable (GST/HST, etc.) | 2,653 |  |
| 2781 | Due to individual shareholder(s) | 5,011 | Tie-out: 2400 $3,490.67 (Thomas) + 2410 $1,606.68 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 3500 | Common shares | 100 |  |

### Fixed assets (book)
| Asset ID | Description | Book start | Cost | Reclass | Amortization | Policy | Components |
|---|---|---|---|---|---|---|---|
| ams_lb9_vending_machine_2024_02_20 | AMS-LB9 vending machine (Electric Kitty) | 2024-02-20 | 1,100 | 0 | 176 | mirror_tax | account=6600 gifi=8810 amount_cents=110000 vendor=Electric Kitty - Bill invoice_date=2024-02-20 |
| costco_freezer_2024_03_13 | Hisense freezer (Costco) | 2024-03-13 | 550 | 0 | 88 | mirror_tax | account=6600 gifi=8810 amount_cents=54999 vendor=Costco - Bill invoice_date=2024-03-13 |
| costco_ipad_air_2023_12_08 | iPad Air 5 64GB (Costco) | 2023-12-08 | 648 | 0 | 62 | mirror_tax | account=6600 gifi=8810 amount_cents=64839 vendor=Costco - Bill 22134500703182312081530 invoice_date=2023-12-08 |
| nayax_card_reader_2025_02_24 | Nayax card reader for vending machine | 2025-02-24 | 557 | 557 | 111 | mirror_tax | account=5300 gifi=8710 amount_cents=55743 vendor=Nayax - Bill invoice_date=2025-02-24 |
| shopify_card_reader_2024_11_12 | Shopify card reader hardware | 2024-11-12 | 479 | 479 | 96 | mirror_tax | account=6600 gifi=8810 amount_cents=45900 vendor=Shopify - Bill invoice_date=2024-11-12 | account=6550 gifi=9275 amount_cents=2000 vendor=Shopify - Bill invoice_date=2024-11-12 |
| walmart_coffee_grinder_2024_09_17 | Coffee grinder (Walmart) | 2024-09-17 | 184 | 184 | 184 | mirror_tax | account=6600 gifi=8810 amount_cents=18367 vendor=Walmart - Bill invoice_date=2024-09-17 |

### Retained earnings (whole dollars)
| GIFI | Description | Amount | Entry rule |
|---|---|---|---|
| 3660 | Retained earnings/deficit - Start | 20,381 | Enter (opening RE) |
| 3680 | Net income/loss | 29,305 | Enter (net income/loss) |
| 3700 | Dividends declared | 36,900 | Enter (dividends declared) |
| 3740 | Other items affecting retained earnings (rounding) | -1 | Enter only if needed (rounding/other) |
| 3849 | Retained earnings/deficit - End | 12,785 | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |

### Shareholder loans / balances support (working papers)
CRA frequently asks for support for any due-from-shareholder / due-to-shareholder amounts. Keep the continuity below with your filing package.

Evidence / working papers:
- `output/due_from_shareholder_breakdown.md` (loan events + net due-from support)
- `output/due_from_shareholder_breakdown.csv` (same data, machine-readable)
- `output/trial_balance_FY2025.csv` (year-end balances by GL account)
- `output/manual_adjustment_journal_detail.csv` (any year-end shareholder payable adjustments)

Year-end summary (from Schedule 100): Due from shareholder (GIFI 1301) = 2,041; Due to shareholder (GIFI 2781) = 5,011.

#### Loan events in this fiscal year (from `output/due_from_shareholder_breakdown.csv`)
| Date | Shareholder | Type | Net | Journal entry id | Description |
|---|---|---|---|---|---|
| 2024-06-17 | Dwayne | LOAN_ISSUED | 9,000.00 | BANK_DEBIT_1086 | Shareholder loan to Dwayne - $9,000 |
| 2025-04-29 | Thomas | LOAN_ISSUED | 2,000.00 | BANK_DEBIT_362 | Shareholder loan to Thomas - $2,000 |
| 2025-05-22 | Dwayne | LOAN_REPAID | -9,000.00 | BANK_INFLOW_SHAREHOLDER_LOAN_REPAYMENT_347 | Shareholder loan repayment |

Note: a loan can be fully repaid within the year (netting to $0 at year-end) and still needs documentation.

#### Other due-from-shareholder components in this fiscal year
| Date | Shareholder | Type | Net | Journal entry id | Description |
|---|---|---|---|---|---|
| 2025-05-31 | Thomas |  | 41.36 | MILEAGE_FUEL_REIMBURSEMENT_FY2025 | Net due from shareholder - Thomas (fuel exceeds mileage) FY2025 |

#### Year-end shareholder-related balances (from trial balance)
| Account | Name | Debit | Credit | Net (approx) |
|---|---|---|---|---|
| 2400 | Due to Shareholder - Thomas | 0.00 | 3403.90 | 3,404 CR |
| 2410 | Due to Shareholder - Dwayne | 0.00 | 1606.68 | 1,607 CR |
| 2500 | Due from Shareholder | 2041.36 | 0.00 | 2,041 DR |

#### Shareholder mileage reimbursement (working papers)
Keep this as working-paper support. Do **not** paste mileage details into Notes to the financial statements.

Evidence / working papers:
- `output/shareholder_mileage_fuel_summary.md` (human summary)
- `output/shareholder_mileage_fuel_payables_FY2025.csv` (FY totals: mileage, fuel, net)
- `output/fuel_9200_wave_bills.csv` (fuel detail by bill)
- `output/mileage_adjustment_summary.md` (documents FY-scoped overlays, if any)

| Shareholder | Mileage | Fuel offset | Net | Direction |
|---|---|---|---|---|
| Thomas | $2,901.63 | $2,942.99 | $41.36 | due from Thomas |
| Dwayne | $608.52 | $0.00 | $608.52 | due to Dwayne |

UFile entry tip: do not enter both `2780` and `2781` for the same payable; that double-counts and can break Schedule 100 totals.

### Tie-check (display-only totals)
| GIFI | Description | Amount |
|---|---|---|
| 1599 | Total current assets (expected) | 27,954 |
| 2599 | Total assets | 27,954 |
| 3640 | Total liabilities and shareholder equity | 27,954 |

## Income statement (GIFI Schedule 125)
| GIFI | Description | Amount | Note |
|---|---|---|---|
| 8300 | Opening inventory | 5,129 |  |
| 8320 | Purchases / cost of materials | 117,342 | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 8500 | Closing inventory | 10,015 |  |
| 8000 | Trade sales of goods and services | 230,907 |  |
| 8520 | Advertising and promotion | 798 |  |
| 8523 | Meals and entertainment | 408 | 50% add-back = $204 |
| 8622 | Employer's portion of employee benefits | 3,610 |  |
| 8670 | Amortization of tangible assets | 717 |  |
| 8690 | Insurance | 1,951 |  |
| 8710 | Interest and bank charges | 3,371 | Includes bank charges + payment processing fees. In Option 1 (book fixed assets), capitalized items originally expensed here are removed via the book overlay (see breakdown below). |
| 8810 | Office expenses | 2,939 |  |
| 8813 | Data processing | 2,915 | Computer hardware + SaaS (under capitalization threshold) |
| 8860 | Professional fees | 353 |  |
| 8911 | Real estate rental | 7,137 |  |
| 8960 | Repairs and maintenance | 585 |  |
| 9060 | Salaries and wages | 54,899 |  |
| 9130 | Supplies | 4,620 | Packaging + operating supplies |
| 9131 | Small tools | 479 |  |
| 9225 | Telephone and telecommunications | 465 | Internet |
| 9270 | Other expenses | 293 | Includes CRA penalties $274 (non-deductible) |
| 9275 | Delivery, freight and express | 96 |  |
| 9281 | Vehicle expenses | 3,510 |  |

### Interest and bank charges (8710) — breakdown (working-paper)
This is informational only (UFile entry is the whole-dollar amount shown on Schedule 125). It helps explain why your UFile attempt may differ after the book fixed-asset overlay.

| Account | Name | Base amount |
|---|---|---|
| 5300 | Merchant Processing Fees | $204.49 |
| 6000 | Bank Charges & Fees | $1,122.71 |
| 6210 | Payment Processing Fees | $2,227.26 |
| 8100 | Interest Expense - Bank | $374.03 |

Overlay adjustments affecting 8710 (capitalized items removed from expense):

| Asset | Entry | Account | Overlay amount | Description |
|---|---|---|---|---|
| nayax_card_reader_2025_02_24 | reclass_expense_credit | 5300 | $-557.43 | Nayax card reader for vending machine |

| Component | Amount |
|---|---|
| Base trial balance (sum of accounts mapped to GIFI 8710) | $3,928.49 |
| Book fixed-asset overlay net impact on 8710 | $-557.43 |
| Final (base + overlay) (rounded in Schedule 125) | $3,371.06 |
| Schedule 125 line 8710 (whole dollars to enter in UFile) | 3,371 |

### Cost of sales tie-check (display-only)
| GIFI | Description | Amount |
|---|---|---|
| 8518 | Cost of sales (expected) | 112,456 |
| 8519 | Gross profit/loss (expected) | 118,451 |

## Notes checklist (UFile screen)
### Checklist (recommended minimal)
| Field | Value | Note |
|---|---|---|
| Identify person primarily involved with financial info (>50%) | Yes |  |
| Type of preparer (if asked) | Other (specify): Management | Management-prepared, unaudited; no accounting practitioner involvement. |
| Accounting practitioner involvement (if asked) | Other (specify): None |  |
| GIFI checklist items | 101 Notes to financial statements | Select only if you enter notes; otherwise leave checklist blank. |

### Notes to financial statements (paste-ready starter text)
- Financial statements are management-prepared, unaudited, and prepared on an accrual basis at historical cost.
- Inventory is stated at cost. FY2025 closing inventory is based on a physical count near year-end; FY2024 closing inventory is an estimate based on available records.
- GST/HST registration became effective 2024-02-26; no GST/HST was collected prior to that date. Some Shopify reports may label pre-registration amounts as “tax”; these amounts are treated as sales/pricing, not GST/HST.

### Notes to financial statements (copy/paste)
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
Inventory consists of food and beverage inventory held for resale and is valued at the lower of cost and net realizable value. Cost is determined using a method applied consistently by management. The inventory balance at May 31, 2025 is based on a physical count performed near year-end (May 16, 2025) and management adjustments for immaterial movements through year-end.

5. Property and equipment
Property and equipment are recorded at cost. Amortization is provided on a basis intended to approximate the decline in service potential of the related assets.

6. Income taxes and government remittances
The corporation is a Canadian-controlled private corporation. Income tax expense comprises current tax. Taxes payable on the balance sheet may include GST/HST and other government remittances.

7. Related party transactions and balances
The corporation is controlled by its shareholders. Amounts due to/from shareholders relate primarily to shareholder-paid business expenses and reimbursements and other amounts payable to shareholders. These balances are non-interest-bearing and due on demand unless otherwise agreed.

8. Subsequent events
There have been no subsequent events requiring adjustment to these financial statements.
```

## Net income (UFile screen)
| Field | Value | Note |
|---|---|---|
| Net income as per financial statements | 29,305 | Should auto-fill from GIFI; otherwise enter from Schedule 1 code A. |
| Total sales of corporation during this taxation year | 230,907 | Use total revenue (sum of revenue lines; typically matches trade sales 8000). |
| Total gross revenues | 230,907 | Usually same as total sales for your file. |

If UFile auto-populates these from GIFI, do not add manual “additions/deductions” here; use Schedule 1 for tax add-backs (meals 50%, penalties, etc.).

## Tax on capital (UFile screen)
| Field | Value | Note |
|---|---|---|
| Eligible for capital tax exemption? | Yes | For your file, expect capital tax exemption; confirm if UFile still requests fields. |
| Total assets at year-end date from financial statements | 27,954 | If required, use Schedule 100 total assets (GIFI 2599). |
| Retained earnings/deficit at year-end (if required) | 12,785 | If UFile forces a retained earnings element, use Schedule 100 GIFI 3600. |

## Status change for the corporation (UFile screen)
No status change; leave blank.

## Charitable donations (UFile screen)
No charitable donations claimed.

## Non-depreciable capital property (UFile screen)
No non-depreciable capital property.

## Income source (UFile screen)
Goal: avoid the UFile warning `INCOMESOURCE` and make the return explicit.

- In UFile → **Income source** screen:
  - Select **Active business income**.
  - Leave **property**, **foreign**, and other income sources unchecked unless you have real amounts.
  - Save and re-run diagnostics to confirm the warning clears.

Expected source for this file: **active business income only** (canteen operations).

### Schedule 1 (tax purposes)
| Code | Description | Amount | Calculation |
|---|---|---|---|
| A | Net income (loss) per financial statements | 29,305 |  |
| 104 | Accounting amortization | 717 |  |
| 121 | Non-deductible meals and entertainment (50%) | 204 |  |
| 128 | Non-deductible fines and penalties | 274 |  |
| 206 | Capital items expensed | 0 |  |
| 403 | Capital cost allowance (Schedule 8) | 717 |  |
| 500 | Total additions | 1,195 |  |
| 510 | Total deductions | 717 |  |
| C | Net income (loss) for tax purposes | 29,783 |  |
Note: If UFile auto-populates Schedule 1 line 403 from Schedule 8, do **not** manually enter 403 in the Schedule 1 grid.
CCA is entered on the **Capital cost allowance** screen from Schedule 8 (total CCA claimed: 717).

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
| CCA required / capital assets | Yes | CCA claimed per Schedule 8. Total CCA: 717. Classes: 8, 12, 50. |
| Book fixed assets present | Yes | Book fixed assets present (capitalized in GIFI). |

## Dividends paid (UFile screen)
| Field | Value | Note |
|---|---|---|
| Taxable dividends paid | 36,900 |  |
| Eligible portion of taxable dividends | 0 | If $0, treat dividends as non-eligible unless you explicitly designate eligible in UFile. |
| Capital dividends (83(2)) | 0 |  |
| Capital gains dividend | 0 |  |

Dividends declared per retained earnings schedule (GIFI 3700). Confirm eligible vs non-eligible in UFile; default expectation is non-eligible.

## Taxable dividend paid (UFile screen)
Enter the taxable dividends paid details so Schedule 3 / Schedule 55 match the retained earnings rollforward.

- Total taxable dividends paid in the tax year: **36,900**
- Eligible portion: **0** (default expectation: $0 = non-eligible)

If UFile asks you to split between connected vs non-connected corporations, and these dividends were paid to individuals (shareholders), treat them as **other than connected corporations**.

## General rate income pool (GRIP) (UFile screen)
| Field | Value | Note |
|---|---|---|
| GRIP at end of previous year | 0 |  |
| Amount respecting dividends (entries) | 0 | UFile allows multiple selections; usually 0 for non-eligible dividends only. |
| Specified future tax consequences (before) (entries) | 0 | UFile allows multiple selections. |
| Specified future tax consequences (after) (entries) | 0 | UFile allows multiple selections. |
| Elected excessive eligible dividend designation as ordinary | 0 |  |

Unless you are designating eligible dividends, GRIP is typically $0 / not needed. If you mark any eligible dividends, you must complete this screen.

## Capital cost allowance (UFile screen)
Use Schedule 8 outputs; enter class details if claiming CCA.

If this section is missing/empty in the guide, the packet was likely built from a snapshot that did not include
`schedule_8_*.csv`. Rebuild via:
`python3 UfileToFill/ufile_packet/tools/refresh_packet_from_current_state.py`

### Schedule 8 / CCA
### Schedule 8 printing checklist (UFile)
- If the exported PDF package is missing Schedule 8, it usually means you did not complete the **Capital cost allowance** screen for the year/class.
- Recommended workflow when filing FY2024 and FY2025 together: create/finish FY2024 first, then **carryforward** into FY2025 so opening UCC values and classes come through cleanly.
- If you cannot carryforward: in FY2025, manually enter the **opening UCC** per class to match FY2024 closing UCC, and enter the current-year additions. Re-export the package and re-check completeness.

| Class | Description | Opening UCC | Additions | CCA claim | Closing UCC |
|---|---|---|---|---|---|
| 8 | General equipment | 1,320 | 1,036 | 471 | 1,885 |
| 12 | Tools and utensils under $500 | 0 | 184 | 184 | 0 |
| 50 | Computer hardware and systems software | 113 | 0 | 62 | 51 |

### Schedule 8 asset additions (audit trail)
| Asset ID | Description | Date | Class | Cost | AIIP? | AII factor |
|---|---|---|---|---|---|---|
| nayax_card_reader_2025_02_24 | Nayax card reader for vending machine | 2025-02-24 | 8 | 557 | yes | 2.0 |
| walmart_coffee_grinder_2024_09_17 | Coffee grinder (Walmart) | 2024-09-17 | 12 | 184 | no | 1.0 |
| shopify_card_reader_2024_11_12 | Shopify card reader hardware | 2024-11-12 | 8 | 479 | yes | 2.0 |

### UFile Schedule 8 entry lines (per asset)
UFile fields to use (avoid accidental dispositions):
- Use **Date acquired** and **Date property became available for use** (these are addition fields).
- Do **not** enter the date into any *disposition* date fields unless you are actually disposing of property.
- For additions to show up, enter the cost under the appropriate additions bucket: **AIIP** (default for these assets), or **Non-accelerated**, or **DIEP** if intentionally designated.
| Class | Addition description | Date acquired | Available for use | Cost | AIIP additions | Non-accelerated additions | DIEP additions | Proceeds (if disposed) | AII factor | Base factor | Disposed description (if any) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | Nayax card reader for vending machine | 2025-02-24 | 2025-02-24 | 557 | 557 | 0 | 0 | 0 | 2.0 | 1.00 |  |
| 12 | Coffee grinder (Walmart) | 2024-09-17 | 2024-09-17 | 184 | 0 | 184 | 0 | 0 | 1.0 | 1.0 |  |
| 8 | Shopify card reader hardware | 2024-11-12 | 2024-11-12 | 479 | 479 | 0 | 0 | 0 | 2.0 | 1.00 |  |

## Loss carry forwards and loss carry backs (UFile screen)
No losses to carry forward/back.

## Reserves (UFile screen)
No reserves claimed.

## Deferred income plans (UFile screen)
No deferred income plans.

## Transaction with shareholders, officers, or employees (UFile screen)
There are transactions with shareholders (dividends, reimbursements, shareholder loan). For T2 disclosure screens, summarize high-level: dividends paid, reimbursements of expenses, shareholder loan receivable (Thomas $2,000) and amounts due to shareholders per Schedule 100 (2781).

## Annual return (UFile screen)
Complete if UFile requires it; no special entries in this packet.

## Instalments paid (UFile screen)
Leave blank unless you have instalment records to enter.

## Refund or balance owing (UFile screen)
| Field | Value |
|---|---|
| Tax payment information (code) | Full balance for every jurisdiction |
| Tax refund information (code) |  |

## Capital dividend account (UFile screen)
No capital dividend account activity.

## Corporate history (UFile screen)
| Field | Value | Note |
|---|---|---|
| 1st prior year end date | 2024-05-31 | UFile field: End date of prior tax year |
| 1st prior year taxable income | 20,711 | UFile field: Taxable income (Schedule 1 code C of the prior year) |
| Eligible RDTOH at prior year-end | 0 | Usually $0 for your file unless you have refundable dividend tax on hand |
| Non-eligible RDTOH at prior year-end | 0 |  |
| Eligible dividend refund (prior year) | 0 |  |
| Non-eligible dividend refund (prior year) | 0 |  |
| Did the corp claim SBD in the prior year? | Yes | Confirm in UFile if it asks; FY2023 stub was inactive, FY2024 claimed SBD as a CCPC. |
| Large corporation amount (prior year) | 0 | UFile field: line 415 of Schedule 200 (prior year) |
| Taxable paid-up capital | 100 | Use share capital unless you have evidence of paid-up capital changes |
| Total assets at prior year-end | 33,503 | UFile field: Total assets as at previous year-end (Schedule 100 GIFI 2599) |
| Capital gain inclusion rate / amount (prior year) |  | Only needed for carryback purposes; leave blank unless applicable |
