# UFile T2 Fill Guide — FY2025

**Entity:** 14587430 Canada Inc. (Curly's Canteen)
**BN:** 748003142RC0001
**Tax year:** 2024-06-01 → 2025-05-31 (year-end 05-31)
**NAICS:** 722512

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

## GIFI form / notes (UFile screens)
- In the main GIFI screen, select: **Update Net income and Tax on capital pages from GIFI**.
- IFRS used? **No**.

### Notes checklist (recommended minimal)
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

## Corporate history carryforward (UFile screen)
| Field | Value | Note |
|---|---|---|
| 1st prior year end date | 2024-05-31 | UFile field: End date of prior tax year |
| 1st prior year taxable income | 16,985 | UFile field: Taxable income (Schedule 1 line 400 of the prior year) |
| Eligible RDTOH at prior year-end | 0 | Usually $0 for your file unless you have refundable dividend tax on hand |
| Non-eligible RDTOH at prior year-end | 0 |  |
| Eligible dividend refund (prior year) | 0 |  |
| Non-eligible dividend refund (prior year) | 0 |  |
| Did the corp claim SBD in the prior year? | Yes | Confirm in UFile if it asks; FY2023 stub was inactive, FY2024 claimed SBD as a CCPC. |
| Large corporation amount (prior year) | 0 | UFile field: line 415 of Schedule 200 (prior year) |
| Taxable paid-up capital | 100 | Use share capital unless you have evidence of paid-up capital changes |
| Total assets at prior year-end | 29,788 | UFile field: Total assets as at previous year-end (Schedule 100 GIFI 2599) |
| Capital gain inclusion rate / amount (prior year) |  | Only needed for carryback purposes; leave blank unless applicable |

## Net income (UFile screen)
| Field | Value | Note |
|---|---|---|
| Net income as per financial statements | 28,349 | Should auto-fill from GIFI; otherwise enter from Schedule 1 line 300. |
| Total sales of corporation during this taxation year | 230,907 | Use total revenue (sum of revenue lines; typically matches trade sales 8000). |
| Total gross revenues | 230,907 | Usually same as total sales for your file. |

If UFile auto-populates these from GIFI, do not add manual “additions/deductions” here; use Schedule 1 for tax add-backs (meals 50%, penalties, etc.).

## Tax on capital (UFile screen)
| Field | Value | Note |
|---|---|---|
| Eligible for capital tax exemption? | Yes | For your file, expect capital tax exemption; confirm if UFile still requests fields. |
| Total assets at year-end date from financial statements | 25,977 | If required, use Schedule 100 total assets (GIFI 2599). |
| Retained earnings/deficit at year-end (if required) | 8,104 | If UFile forces a retained earnings element, use Schedule 100 GIFI 3600. |

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
| % gross revenue from internet | 4.35 | This % is easy to misinterpret with Shopify POS; keep consistent year-to-year unless you have a better basis. |
| Top URL(s) | curlyscanteen.ca |  |
| Quarterly instalments – wants considered? | Yes |  |
| Quarterly instalments – perfect compliance? | No |  |

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

## Mailing address (UFile screen)
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

## Location of books & records (UFile screen)
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

## Corporate officers / directors (UFile screen)
| Name | Title | Signing officer? | Elected | Ceased | Non-resident? | Also shareholder? | SIN | Voting/Common/Pref % | Address | Phone | Fax |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas McCrossin | Vice-president | No | 2022-12-09 | 2022-12-09 | No | Yes | XXX-XXX-XXX | 25/25/25 | 31 Duckling Dell, Amherst Nova Scotia B4H 3Y2 | (902) 321-6749 | (000) 000-0000 |
| Dwayne Ripley | President | Yes | 2022-12-08 |  | No | Yes | XXX-XXX-XXX | 75/75/75 | 28 Charles St, Amherst Nova Scotia B4H 3P8 | (902) 669-2700 | (000) 000-0000 |

- Has there been a change of directors since the last return? **No**
- Previous shareholder names: leave blank (no name changes).
- Date the return is signed: fill on filing/signing day (do not carry forward stale dates).

**Note:** If a director “ceased date” is a carryforward artifact but the person is still a director, leave the ceased date blank in UFile for the current filing.

## Refund or balance owing (UFile screen)
| Field | Value |
|---|---|
| Tax payment information (code) | Full balance for every jurisdiction |
| Tax refund information (code) |  |

## Transactions with shareholders/officers/employees (UFile disclosure)
There are transactions with shareholders (dividends, reimbursements, shareholder loan). For T2 disclosure screens, summarize high-level: dividends paid, reimbursements of expenses, shareholder loan receivable (Thomas $2,000) and amounts due to shareholders per Schedule 100 (2781).

## Dividends paid (UFile screen)
| Field | Value | Note |
|---|---|---|
| Taxable dividends paid | 36,900 |  |
| Eligible portion of taxable dividends | 0 | If $0, treat dividends as non-eligible unless you explicitly designate eligible in UFile. |
| Capital dividends (83(2)) | 0 |  |
| Capital gains dividend | 0 |  |

Dividends declared per retained earnings schedule (GIFI 3700). Confirm eligible vs non-eligible in UFile; default expectation is non-eligible.

## General rate income pool (GRIP) (UFile screen)
| Field | Value | Note |
|---|---|---|
| GRIP at end of previous year | 0 |  |
| Amount respecting dividends (entries) | 0 | UFile allows multiple selections; usually 0 for non-eligible dividends only. |
| Specified future tax consequences (before) (entries) | 0 | UFile allows multiple selections. |
| Specified future tax consequences (after) (entries) | 0 | UFile allows multiple selections. |
| Elected excessive eligible dividend designation as ordinary | 0 |  |

Unless you are designating eligible dividends, GRIP is typically $0 / not needed. If you mark any eligible dividends, you must complete this screen.

## Other UFile screens (expected blank / N/A)
| Screen | Has entries? | Note |
|---|---|---|
| Loss carryforwards / carrybacks | No | No losses to carry forward/back. |
| Charitable donations | No | No charitable donations claimed. |
| Reserves | No | No reserves claimed. |
| Capital cost allowance (CCA) | No | No CCA claimed; assets were expensed under capitalization threshold. |
| Non-depreciable capital property | No | No non-depreciable capital property. |
| Deferred income plans | No | No deferred income plans. |
| Status change for the corporation | No | No status change for the corporation. |

## Schedule 100 (GIFI) — Balance sheet (enter these lines, whole dollars)
**Important:** If you complete the retained earnings rollforward (3660/3680/3700/3740), do **not** manually type retained earnings on Schedule 100 (`3600`)—UFile should populate it from the rollforward. Typing `3600` (or `3849`) can trigger BCR errors like “GIFI-FIELD 3849 does not match internal subtotal calculation.”

| GIFI | Description | Amount | Note |
|---|---|---|---|
| 1001 | Cash | 12,472 |  |
| 1121 | Inventory of goods for sale | 10,015 | Physical count 2025-05-16 |
| 1301 | Due from individual shareholder(s) | 2,000 | Shareholder loan receivable (Thomas). Review s.15(2) repayment/exception within 1 year after 2025-05-31. |
| 1484 | Prepaid expenses | 1,490 |  |
| 2620 | Amounts payable and accrued liabilities | 10,013 |  |
| 2680 | Taxes payable (GST/HST, etc.) | 2,663 |  |
| 2781 | Due to individual shareholder(s) | 5,097 | Tie-out: 2400 $3,490.67 (Thomas) + 2410 $1,606.68 (Dwayne); source: readiness_report.md. If UFile doesn't accept 2781, enter this amount on 2780 instead. |
| 3500 | Common shares | 100 |  |

## Schedule 125 (GIFI) — Income statement (enter these lines, whole dollars)
| GIFI | Description | Amount | Note |
|---|---|---|---|
| 8300 | Opening inventory | 2,847 |  |
| 8320 | Purchases / cost of materials | 117,452 | If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500. |
| 8500 | Closing inventory | 10,015 |  |
| 8000 | Trade sales of goods and services | 230,907 |  |
| 8520 | Advertising and promotion | 798 |  |
| 8523 | Meals and entertainment | 408 | 50% add-back = $204 |
| 8622 | Employer's portion of employee benefits | 3,610 |  |
| 8690 | Insurance | 1,951 |  |
| 8710 | Interest and bank charges | 6,694 |  |
| 8810 | Office expenses | 3,903 |  |
| 8813 | Data processing | 1,878 | Computer hardware + SaaS (under capitalization threshold) |
| 8860 | Professional fees | 353 |  |
| 8911 | Real estate rental | 7,137 |  |
| 8960 | Repairs and maintenance | 603 |  |
| 9060 | Salaries and wages | 54,899 |  |
| 9130 | Supplies | 4,629 | Packaging + operating supplies |
| 9131 | Small tools | 479 |  |
| 9225 | Telephone and telecommunications | 465 | Internet |
| 9270 | Other expenses | 293 | Includes CRA penalties $274 (non-deductible) |
| 9275 | Delivery, freight and express | 136 |  |
| 9281 | Vehicle expenses | 4,038 |  |

## Cost of sales tie-check (display-only)
| GIFI | Description | Amount |
|---|---|---|
| 8518 | Cost of sales (expected) | 110,284 |
| 8519 | Gross profit/loss (expected) | 120,623 |

## Tie-check (display-only totals)
| GIFI | Description | Amount |
|---|---|---|
| 1599 | Total current assets (expected) | 25,977 |
| 2599 | Total assets | 25,977 |
| 3640 | Total liabilities and shareholder equity | 25,977 |

## Retained earnings (whole dollars)
| GIFI | Description | Amount | Entry rule |
|---|---|---|---|
| 3660 | Retained earnings/deficit - Start | 16,656 | Enter (opening RE) |
| 3680 | Net income/loss | 28,349 | Enter (net income/loss) |
| 3700 | Dividends declared | 36,900 | Enter (dividends declared) |
| 3740 | Other items affecting retained earnings (rounding) | -1 | Enter only if needed (rounding/other) |
| 3849 | Retained earnings/deficit - End | 8,104 | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |

## Schedule 1 (tax purposes)
| Line | Description | Amount | Calculation |
|---|---|---|---|
| 117 | 50% of meals and entertainment | 204 | 408 * 50% = 204 |
| 300 | Net income per financial statements | 28,349 |  |
| 311 | Penalties and fines (CRA) | 274 |  |
| 400 | Net income for tax purposes | 28,827 | 28349 + 204 + 274 = 28827 |

## High-signal yes/no answers
| Question | Answer | Note |
|---|---|---|
| T2 line 070 (first year after incorporation) | No | 2023 stub T2 already filed as first-year after incorporation (Schedule 24). FY2025 should be No. |
| T2 line 180 (internet income/websites) | Yes | Shopify sales present; likely Yes for internet income/websites (Schedule 88). Confirm store domains in UFile. |
| T2 line 201 (book vs tax net income differs) | Yes | Book vs tax differs due to meals 50% add-back and CRA penalties; Schedule 1 is attached. |
| CCA required / capital assets | No | No capital assets capitalized in these years (below capitalization threshold; expensed). |
