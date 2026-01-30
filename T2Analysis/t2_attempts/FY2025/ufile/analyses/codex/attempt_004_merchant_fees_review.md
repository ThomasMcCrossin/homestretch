# FY2025 — Merchant/processing fees deep dive (Attempt 4 context)

Scope: reconcile “Shopify fees” vs “Merchant account fees” and confirm there is no FY mixing.

## Summary

There are **two distinct fee streams** in FY2025, both mapped to GIFI 8710:

1) **Merchant account fees (acct 5300)** — sourced from **Wave bills**
2) **Shopify payout fees (acct 6210)** — sourced from **Shopify payout bank inflows**

These are **both FY2025 only** (2024‑06‑01 → 2025‑05‑31), not mixed with FY2024.

## FY2025 totals (from db/t2_final.db)

**FY2025 only (2024‑06‑01 → 2025‑05‑31):**
- 5300 Merchant account fees = **$2,969.96**
- 6210 Shopify payout fees = **$2,227.26**

**FY2024 only (2023‑06‑01 → 2024‑05‑31):**
- 6210 Shopify payout fees = **$1,701.70**
- 5300 Merchant account fees = **$0.00**

These totals come from journal entries filtered by entry_date; not cross‑year.

## Where the two numbers come from (FY2025)

### 5300 Merchant account fees (Wave bills)
Source system: `t2-final wave_bill_accrual`

Top items:
- **$2,208.04** — “Shopify - Bill 2024 CC Fees - Invoice 2024”
- **$557.43** — “Nayax - Bill”
- **$174.59** — “Shopify - Bill”
- **$29.90** — “Nayax - Bill”

Concrete wave bills (FY2025) that hit 5300:
| Bill date | Vendor | Invoice # | Net | Tax | Total | Allocation |
|---|---|---|---:|---:|---:|---|
| 2024-12-31 | Shopify - Bill 2024 CC Fees | 2024 | 2,208.04 | 0.00 | 2,208.04 | 5300 |
| 2025-02-13 | Shopify - Bill | (blank) | 44.09 | 6.61 | 50.70 | 5300 + 2210 |
| 2025-03-15 | Shopify - Bill | (blank) | 44.42 | 6.66 | 51.08 | 5300 + 2210 |
| 2025-04-14 | Shopify - Bill | (blank) | 43.00 | 6.02 | 49.02 | 5300 + 2210 |
| 2025-05-14 | Shopify - Bill | (blank) | 43.08 | 6.04 | 49.12 | 5300 + 2210 |
| 2025-02-24 | Nayax - Bill | (blank) | 557.43 | 74.85 | 632.28 | 5300 + 2210 |
| 2025-04-30 | Nayax - Bill | (blank) | 14.95 | 2.09 | 17.04 | 5300 + 2210 |
| 2025-05-31 | Nayax - Bill | (blank) | 14.95 | 2.09 | 17.04 | 5300 + 2210 |

Notes:
- The “Shopify - Bill 2024 CC Fees” is the **dominant** 5300 driver.
- Nayax bills appear to be payment terminal fees (not Shopify payouts).

### 6210 Shopify payout fees (bank inflows)
Source system: `t2-final bank_inflows`

Multiple payout lines (each $10–$120 range) totaling **$2,227.26**

## Why this looks like “double fees”

If Shopify fees are already deducted in **Shopify payout net deposits**, and you also booked a **Wave bill** for Shopify merchant account fees, then:

- you can end up **double‑counting processing fees** (once in payout net adjustment, and again in the Wave bill).

The current books include **both** streams.

Whether that is **correct** depends on:
1) whether the Wave “Shopify CC fees” bills represent **separate charges not already included in payout nets**, and
2) whether the payout fee logic already captured those exact amounts.

## Next forensic checks (no data changes)

1) **Validate the Shopify bill(s):**
   - Pull the Wave bill(s) that hit 5300 and confirm:
     - Do these amounts match any payout‑level fees already captured in 6210?
     - Are they **separate** Shopify charges (e.g., monthly plan, chargebacks, disputes, apps, POS terminal fees)?

2) **Reconcile to Shopify gateway exports:**
   - `output/snapshots/20260129-192249/output/shopify_gateway_reports_selected.csv`
   - `.../shopify_gateway_vs_payouts_audit.md`

3) **Identify app/subscription fees explicitly:**
   - In FY2025, Shopify bills with allocations to **6620 (Software & SaaS)** include:
     - 2024-12-31 Shopify bill (net 35,898, tax 5,385) → 6620
   - Other Shopify bills in FY2025 are allocated to:
     - 6600 Office supplies
     - 6550 Shipping
     - 5300 Merchant account fees
   If you expect 1–2 monthly apps, they should likely appear in **6620** rather than 5300.

4) **If they are duplicates:**
   - Decide which stream is correct (Wave bill vs payout net).
   - Document the resolution before changing any journals.

## Evidence / queries used

- DB tables: `journal_entries`, `journal_entry_lines`
- FY window filter: entry_date between 2024‑06‑01 and 2025‑05‑31
- Account codes: 5300, 6210
