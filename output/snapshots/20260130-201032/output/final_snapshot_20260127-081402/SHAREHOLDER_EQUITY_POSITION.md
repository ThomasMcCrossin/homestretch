## Shareholder + Equity Position (Updated Working Paper)

Scope: FY2024 (2023-06-01 → 2024-05-31) and FY2025 (2024-06-01 → 2025-05-31) in `t2-final-fy2024-fy2025`.

Sources used:
- `output/readiness_report.md`
- `output/due_from_shareholder_breakdown.md`
- `output/shareholder_mileage_fuel_summary.md`
- `output/shareholder_meals_estimate_summary.md`
- `output/payroll_summary.md`
- `output/manual_adjustment_journal_detail.csv`
- `/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/output/SHAREHOLDER_INFORMATION.txt` (noted as stale in places)
- `data/2023 - 14587430 Canada Inc..pdf` (nil T2 filed for 2022-12-08 → 2023-05-31)

---

### 1) Share structure timeline (ownership)

- Incorporation date: **2023-06-01**.
- Day 1: **Dwayne 100%**.
- Day 2: **Thomas acquired/transferred 25%** when the business value was **$0**.

**Accounting impact:**  
This is a shareholder-to-shareholder transfer at **FMV ~$0**, so there is **no corporate cash entry** required. It should be reflected in the shareholder register and Schedule 50 (share ownership at year-end), but it does not create a corporate asset or liability unless there was consideration paid to the corporation (none indicated).

---

### 2) Share capital presentation (GIFI 3500)

Corporate records indicate **100 issued shares** and **$100 share capital**.

**Entry posted (no bank deposit required):**
- **Dr 6520 Legal Fees $100**
- **Cr 3000 Share Capital $100**

Rationale: treat the $100 as paid-in via incorporation/setup costs (shareholder-paid). This **avoids inventing a cash deposit** while aligning Schedule 100 with the legal share structure.

Evidence:
- `output/manual_adjustment_journal_detail.csv` → `SHARE_CAPITAL_AT_INCORP`
- `output/gifi_schedule_100_FY2024.csv` and `output/gifi_schedule_100_FY2025.csv` show **GIFI 3500 = $100**.

---

### 3) Shareholder-related balances at year-end (from TB)

From `output/readiness_report.md`:

**FY2024 (as of 2024-05-31)**
- Due to Thomas (2400): **$2,154.72 CR**
- Due to Dwayne (2410): **$908.16 CR**
- Due from shareholder (2500): **$0.00**

**FY2025 (as of 2025-05-31)**
- Due to Thomas (2400): **$2,088.63 CR**
- Due to Dwayne (2410): **$1,606.68 CR**
- Due from shareholder (2500): **$2,041.36 DR**

Due-from drivers:
`output/due_from_shareholder_breakdown.md` shows net **$2,041.36** (Thomas) from bank debits and mileage/fuel netting.

---

### 4) Mileage & fuel reimbursements (shareholder payables/receivables)

From `output/shareholder_mileage_fuel_summary.md`:

**FY2024**
- Thomas: mileage $3,082.46 – fuel $1,276.92 → **$1,805.54 due to Thomas**
- Dwayne: **$788.16 due to Dwayne**

**FY2025**
- Thomas: mileage $2,901.63 – fuel $2,942.99 → **$41.36 due from Thomas**
- Dwayne: **$608.52 due to Dwayne**

---

### 5) Meals estimate (Moncton trips)

From `output/shareholder_meals_estimate_summary.md`:

**FY2024**: $465 total (Thomas $345, Dwayne $120)  
**FY2025**: $390 total (Thomas $300, Dwayne $90)  
These are recorded as expenses with corresponding due-to-shareholder credits.

---

### 6) Shareholder payroll vs dividends (corrections to stale doc)

`/home/clarencehub/curlys-books/t2-filing-fy2024-fy2025/output/SHAREHOLDER_INFORMATION.txt` is **stale**. Corrections now embedded in `output/payroll_summary.md`:

- **2025-01-08 $1,000 to Thomas** is **payroll**, not dividend (rounds out $4,000 net payroll across 2024-12-20 $1,500 + 2024-12-31 $1,500 + 2025-01-08 $1,000).
- **2024-06-17 $4,321.07** cheque is **payroll to Thomas**.

These overrides are explicitly shown in `output/payroll_summary.md` (Bank category overrides section).

---

### 7) Nil T2 filed (2022-12-08 → 2023-05-31)

The filed nil T2 shows **$0 net income** for the stub period. It does **not** contain Schedule 100/125 details and does not constrain FY2024/FY2025 share capital presentation.

---

### 8) Open items / confirmations

- Confirm no additional incorporation costs should be booked beyond the $100 share capital treatment above.
- Confirm whether any additional shareholder payable/receivable items exist outside the current modeled set (mileage, meals, shareholder loan, dividends).

---

### 9) Post-year-end settlements (outside FY scope)

These payments occurred **after FY2025 year-end (2025-05-31)** and are therefore **not reflected** in the FY2024/FY2025 trial balances in this repo (which stop at 2025-05-31).

On **2026-01-27**, you paid Dwayne (separate e-transfers) to settle the corp’s “due to shareholder” balance:
- FY2024 settlement payment: **$492.60**
- FY2025 settlement payment: **$608.52**

Based on the current modeled year-end payables (section 3/4/5), these payments fully clear the FY2024+FY2025 balance:
- FY2024 due to Dwayne at 2024-05-31: **$908.16** (mileage $788.16 + meals $120.00) → remaining after $492.60: **$415.56**
- FY2025 incremental due to Dwayne: **$698.52** (mileage $608.52 + meals $90.00) → remaining after $608.52: **$90.00**

Total remaining due to Dwayne (FY2024 + FY2025): **$0.00** (cleared on 2026-01-27)
