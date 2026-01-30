# UFile copy/paste directory review (critical) — FY2024 + FY2025

Scope: review of `UfileToFill/` (your UFile screen copy/paste exports) and how it should be used to file FY2024 (2023-06-01 → 2024-05-31) and FY2025 (2024-06-01 → 2025-05-31), without drifting from the already-filed 2023 stub return where consistency matters.

Primary numeric source-of-truth (balances/income/tax add-backs):
- `output/snapshots/20260129-192249/output/`
- Validated by `python3 UfileToFill/ufile_packet/tools/validate_packet.py`

Year-specific “enter-this” guides:
- FY2024: `UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md`
- FY2025: `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

---

## 0) The core UFile pitfall you hit (totals not adding)

UFile often **does not include amounts entered on summary GIFI lines** when it auto-calculates totals (e.g., it may ignore `1120` but include `1121–1127`).

**Rule:** enter amounts on **detail** lines, and leave subtotal/total lines blank.

For your file:
- Inventory: enter on `1121` (not `1120`)
- Prepaids/other current assets: enter on `1484` (not `1480`)
- Shareholder payable: enter on `2781` (not `2780`) when amounts are due to *individual* shareholders
- Leave totals like `1599` and `2599` blank; UFile should compute them

Also: Cost of sales often needs the inventory “movement” lines on Schedule 125:
- `8300` Opening inventory
- `8320` Purchases / cost of materials
- `8500` Closing inventory
UFile will then derive `8518` (cost of sales) and `8519` (gross profit). If you enter only `8518`, UFile may still show warnings or fail to tie-out.

If entered correctly, UFile should compute:
- FY2024 `1599` = `2599` = **29,788**
- FY2025 `1599` = `2599` = **25,977**

---

## 0b) Another core pitfall we corrected (wrong GIFI codes)

Earlier drafts used several **obviously wrong** GIFI placements (e.g., putting shipping on farming/trucking codes).

The current packet + guides were rebuilt to align to the **UFile GIFI lists** (`UfileToFill/GIFI/*`) and the
codes UFile actually expects on-screen:

- Inventory: `1121` (not `1120`)
- Prepaids: `1484` (not `1480`)
- Shipping & delivery expense: `9275` (Delivery, freight and express) — **not** `9801` (farming/trucking)
- Packaging & operating supplies: `9130` (Supplies) — not `8810`
- Small tools: `9131` (Small tools)
- Computer hardware + SaaS (expensed): `8813` (Data processing)
- Internet: `9225` (Telephone and telecommunications)

These reclasses **do not change net income** — they only move amounts into the correct UFile boxes so Schedule 125
is credible and tie-outs behave as expected.

## 1) “Do not deviate” fields (carry forward from the filed 2023 return)

These are the high-risk “don’t drift” fields that should remain consistent:

### Identity / classification
- BN: `748003142RC0001`
- Legal name: `14587430 Canada Inc.`
- Jurisdiction: Federal; Permanent establishment: Nova Scotia
- NAICS: `722512 Limited‑Service Eating Places` (seen in both `UfileToFill/Identification of the Corporation/2023.txt` and `.../2024.txt`)

### Addresses / addressees (this is the subtle diff you correctly remembered)
From `UfileToFill/Other Addresses/2023.txt`:
- Mailing addressee: **Dwayne Ripley**
- Books & records addressee: **Curly’s**

Recommendation: keep both FY2024 and FY2025 consistent with those 2023 choices unless you intentionally changed it.

### “First federal return?” / “First year after incorporation?”
The 2023 stub return was already filed as the first federal return / first-year after incorporation.
- FY2024 + FY2025 should be **NOT first return** and **NOT first year after incorporation**.

Evidence: `data/2023 - 14587430 Canada Inc..pdf` shows Incorporation line 070 = Yes and Schedule 24 filed.

---

## 2) Review by UFile screen export (`UfileToFill/`)

This section tells you what to enter (and what to be careful about) for each “screen” you exported.

### A) Identification of the Corporation
Files:
- 2023: `UfileToFill/Identification of the Corporation/2023.txt`
- 2024: `UfileToFill/Identification of the Corporation/2024.txt`

Key points:
- FY2024/FY2025 tax year ends should be **May 31** of the relevant year.
- “Is this the first federal return?” should be **No** for FY2024/FY2025.
- NAICS should stay **722512**.
- Activity description: “Quick Service Restaurant” / “Canteen in an Arena 100%” is reasonable.

**Internet business activities (line 180 / Schedule 88):**
`UfileToFill/Identification of the Corporation/2024.txt` currently has:
- “Earn income from webpages/websites?” = **Yes**
- Number of websites = **1**
- URL = `curlyscanteen.ca`
- % gross revenue from internet = **4.35%**

Critical note: because you use Shopify POS, **card payments can be in-person even though they’re “Shopify payments”**. So do not “compute” internet % from the Shopify gateway totals unless you’re sure it’s online-only. If you don’t know the % for FY2025, use a conservative estimate and document it, or leave blank if UFile allows.

**Quarterly instalments section:**
In `.../2024.txt` it says:
- “Want to be quarterly remitter?” = Yes
- “Perfect compliance history?” = No

That combination is internally inconsistent. If UFile flags it, answer conservatively (typically **No** to quarterly instalments unless you are sure you qualify).

### B) Head Office Address
Files:
- `UfileToFill/Head Office Address/2023.txt`

These appear consistent; keep as-is unless changed in reality.

### C) Other Addresses (mailing + books/records)
Files:
- `UfileToFill/Other Addresses/2023.txt`

Critical diff:
- 2023 books/records addressee: **Curly’s**
- 2024 in-progress shows books/records addressee: **Dwayne Ripley**

Per your instruction (“no deviation from 2023”), use **Curly’s** for FY2024/FY2025.

Also note the “Has address changed since last filing” field: 2023 shows “No Change”; 2024 shows placeholders. Answer consistently based on whether you truly changed anything.

### D) Corporate Officers
Files:
- `UfileToFill/Corporate Officers/2023.txt`

What looks correct:
- Officer identities, SINs, titles, and share %s appear consistent (Thomas 25%, Dwayne 75%).

Red flag to fix in UFile UI:
- Thomas shows a “date ceased” equal to the election date in the export (looks like a carry-forward artifact). If UFile asks, **leave cease date blank** unless the director actually ceased.

### E) Tax Preparer
Files:
- `UfileToFill/Tax Preparer/2023.txt`
- `UfileToFill/Tax Preparer/2024InProgress.txt`

These appear fine; keep representative ID and email consistent.

### F) GIFI (Balance Sheet / Income Statement / Notes / Tax on capital)
Files:
- `UfileToFill/GIFI/*` (catalog of possible lines)

Use the year-specific entry guides (not the raw GIFI catalog):
- FY2024: `UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md`
- FY2025: `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

Key “don’t do this”:
- Don’t type totals like `1599`, `2599`, `3499`, `3640`, etc.
- Don’t type inventory into `1120` or prepaids into `1480` if UFile isn’t counting them.
 - For “Due to shareholder(s) / director(s)” use **`2781`** for your combined amount (individual shareholders). `2780` is a higher-level heading that is often auto-derived from `2781/2782/2783`.

### G) Dividends Paid (FY2025 only)
File:
- `UfileToFill/Dividends Paid/Dividends.txt`

Your accounting output shows FY2025 dividends declared: **$36,900** (Retained earnings schedule / Schedule 125 tie-out).

What to fill:
- Select “Taxable dividend paid” and enter **$36,900**.
- Eligible portion: likely **$0** (most CCPC dividends are non-eligible unless you specifically paid eligible dividends / have GRIP). Confirm in UFile.

### H) GRIP
File:
- `UfileToFill/Dividends Paid/GRIP.txt`
- `UfileToFill/General Rate Income Pool/GeneralRateIncomePool.txt`

If paying only non-eligible dividends, GRIP is typically **$0** and can usually be left blank/zeroed. Only complete if UFile requires due to an “eligible dividend” selection.

### I) Transactions with shareholders/officers/employees
File:
- `UfileToFill/Transaction with shareholders, officers, or employees/transactionswiththem.txt`

For FY2024/FY2025, it is reasonable to disclose transactions because you have:
- Shareholder reimbursements
- Shareholder loan(s) (e.g., Thomas $2,000 due-from at FY2025 end)
- Dividends (FY2025)

This is primarily a disclosure screen; you can keep it high-level (e.g., “Reimbursements of expenses”, “Loans”, “Dividends”) rather than trying to enumerate every reimbursement line.

### J) Corporate History (prior year inputs)
File:
- `UfileToFill/Corporate History/corporateHistory.txt`

This may be used by UFile for instalment history / SBD calculations.

Recommended minimal entries:
- For FY2024 “1st prior year” = the filed 2023 stub year (ends 2023-05-31):
  - Taxable income: **$0**
  - End date: **2023-05-31**
  - Taxable paid-up capital: **$100** (share capital exists; small and consistent)
- For FY2025 “1st prior year” = FY2024 (ends 2024-05-31):
  - Taxable income: **$16,985** (Schedule 1 code C FY2024)
  - End date: **2024-05-31**
  - Taxable paid-up capital: **$100**

### K) Refund or Balance Owing
File:
- `UfileToFill/Refund or Balance Owing/refundorbalanceowing.txt`

Likely selection: “Full balance for every jurisdiction”.

### L) Loss carryforwards / Reserves / Charitable donations / Capital property / CCA
Files:
- `UfileToFill/Loss carry forwards and loss carry backs/losscarryforwardsandlosscarrybacks.txt`
- `UfileToFill/Reserves/Reserves.txt`
- `UfileToFill/Charitable Donations/CharitableDonations.txt`
- `UfileToFill/Non Deperciable Capital Property/capitalpropertynondeprec.txt`
- `UfileToFill/Capital Cost Allowance/*`

Expected for your file:
- Losses: **none**
- Reserves: **none**
- Donations: **none**
- CCA: **see Schedule 8 outputs** (capital items can be expensed in books but claimed for tax via Schedule 8)

Only fill these screens if you truly have these items.

---

## 3) What looks “lazy / risky” in the prior LLM output (so you don’t get burned)

These are the areas where an LLM tends to guess:
- Internet % of revenue (because Shopify POS muddies “internet” vs “in-person”)
- Dividend type (eligible vs non-eligible; GRIP implications)
- Director cease dates (carryforward artifacts)
- “Quarterly instalments” eligibility questions
- “One-month extension of balance-due date” eligibility (depends on CCPC/SBD conditions; wrong answer can affect interest)

Treat those as **must-review in UFile UI**, even if everything else is straight from the packet.

---

## 4) FY2025-specific differences you must enter (not present in the 2024 prefill export)

Your `UfileToFill/` folder currently includes “Identification … /2024.txt” but not a “/2025.txt”.
For FY2025 you should still use the same screen structure, but update the year-specific items:

- Tax year end: **2025-05-31** (year start should be 2024-06-01 in the return)
- Dividends paid: **$36,900** (FY2025 only)
- Due from shareholder(s): **$2,000** on **1301** (FY2025 only)
- Inventory: **$10,015** on **1121** (FY2025)
- Prepaids: **$1,490** on **1484** (FY2025)

Everything else (BN, NAICS, addresses/addressees, officers, preparer) should carry forward unchanged unless you intentionally changed it.

---

## 5) Expected schedules / “Yes” answers (high-level filing shape)

This is the minimal “shape” you should expect for these returns in UFile:

**FY2024**
- GIFI / financial statements: **Yes** (Schedules 100 + 125)
- Schedule 1 (book-to-tax differences): **Yes** (meals 50% add-back + CRA penalties)
- Schedule 50 (shareholders >10%): **Yes**
- Internet income/websites (T2 line 180): **Yes** → UFile will typically want the internet schedule/details (often referred to as “Schedule 88” in the T2 form attachments list)
- First year after incorporation (T2 line 070 / Schedule 24): **No** (already filed in the 2023 stub return)
- CCA / Schedule 8: **Check Schedule 8 outputs** (CCA claimed when asset register has additions)
- Losses: **No**

**FY2025**
- Same as FY2024, plus:
- Dividends paid: **Yes** ($36,900) → expect UFile to ask dividend details; ensure your T5 process aligns with what you enter
