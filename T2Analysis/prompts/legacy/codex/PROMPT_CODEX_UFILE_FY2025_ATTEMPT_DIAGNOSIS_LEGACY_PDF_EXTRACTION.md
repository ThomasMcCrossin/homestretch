You are Codex CLI (terminal-based coding assistant). Work inside the repository at:

- `/home/clarencehub/t2-final-fy2024-fy2025`

This task is a forensic, audit-style diagnosis of a UFile T2 filing attempt for FY2025.

---

# Non-negotiable safety rules

1) **Read-only** with respect to all existing accounting data and project outputs.
   - **DO NOT edit, delete, or overwrite** anything under:
     - `UfileToFill/`
     - `output/`
     - `docs/`
     - `data/`
     - any DB files
   - **DO NOT “fix” numbers** to force balancing.

2) You **MAY** run commands and scripts, but **all write outputs must go ONLY** into a dedicated run directory under:
   - `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/`

3) You **MAY** create new files under your run directory (markdown report, extracted text, CSVs, JSONs, scratch scripts, venv, etc.).

4) You **MUST NOT** write anywhere else. If a tool tries to write outside your run directory, stop and choose another approach.

5) Treat **both** UFile output and the project accounting outputs as potentially wrong until reconciled.

---

# Dedicated Codex run directory (prevents mixing with Claude runs)

Create a new run directory (recommended):

- `./T2Analysis/tools/new_run_dirs.sh FY2025 ufile codex`

Use the printed path as `RUN_DIR`. Inside `RUN_DIR`, use:
- `inputs/`  (copies of evidence files you relied on)
- `work/`    (intermediate extracted text, scratch scripts, parsed tables)
- `outputs/` (final report + machine-readable tables)

Also write a short `README.md` in `RUN_DIR` describing what you ran and what you concluded.

Important: **Do not place outputs inside `UfileToFill/.../attempts/`**; keep Codex output isolated under `T2Analysis/.../analyses/codex/...`.

---

# Evidence files (read-only sources)

## The attempted FY2025 UFile export (primary evidence)
- `UfileToFill/ufile_packet/years/FY2025/attempts/2025 - 14587430 Canada Inc. - My copy - Tax return.pdf`

## Project “expected” values (may be wrong; must be tested)
- `UfileToFill/ufile_packet/years/FY2025/packet.json`
- `UfileToFill/ufile_packet/packet.json`

## The current FY2025 entry guide (may be wrong; must be tested)
- `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

## UFile GIFI screen catalogs / definitions
- `UfileToFill/GIFI/BalanceSheet.txt`
- `UfileToFill/GIFI/IncomeStatement.txt`
- `UfileToFill/GIFI/NetIncome.txt`
- `UfileToFill/GIFI/TaxOnCapital.txt`
- `UfileToFill/GIFI/NotesChecklist.txt`

Copy only what you need into `inputs/` for traceability (do not move originals).

---

# Objective

Determine (with explicit arithmetic) why the FY2025 UFile attempt produced diagnostics and non-balancing schedules, and decide whether root cause is:

- **A) UFile entry mechanics / UFile auto-calculation behavior**
- **B) Wrong underlying numbers from the project (DB/snapshots/scripts/mappings)**
- **C) A mix**

You are not allowed to fix anything in this run—only diagnose and propose specific next actions.

---

# Method (required)

## A) Extract and catalogue diagnostics from the PDF

1) Extract PDF text to `work/attempt_fy2025.txt`:
   - Prefer `pdftotext` if available.
   - If you need Python tooling (`pdfplumber`), create a venv in `RUN_DIR/work/venv/`.

2) In `outputs/diagnostics.md`, list every diagnostic line:
   - exact text + nearby context
   - classify: Blocking vs Non-blocking

## B) Extract what was actually in the return (verbatim tables)

From the attempt text, extract the complete set of populated lines for:

### Schedule 100 (Balance Sheet)
At minimum: `1001, 1121/1120, 1301, 1484/1480, 2620, 2680, 2781/2780, 3500, 3600, 2599, 3499, 3620, 3640`

### Retained earnings section
`3660, 3680, 3700 (if present), 3849` and any “other items”.

### Schedule 125 (Income Statement)
`8000, 8299, 8300, 8320, 8500, 8518, 8519, 9367, 9368` plus every populated expense line.

Write machine-readable artifacts:
- `outputs/attempt_schedule_100.csv`
- `outputs/attempt_retained_earnings.csv`
- `outputs/attempt_schedule_125.csv`

## C) Independently recompute UFile internal math (show-your-work)

Using only attempt-extracted amounts:
1) Operating expenses = sum of detail expense lines (exclude 9367/9368 totals)
2) COGS from movement: `8300 + 8320 - 8500` (compare to `8518` if present)
3) Gross profit = total revenue - COGS
4) Net income = gross profit - operating expenses
5) Equity = `3500 + 3600`
6) Balance equation = `2599` vs `(3499 + 3620)` and `3640` consistency

Write to `outputs/recalculations.md` with explicit arithmetic.

## D) Compare attempt vs project expected values

Create:
- `outputs/attempt_vs_project_comparison.csv`

Columns:
- Field (GIFI code / schedule line)
- Attempt value
- Project expected value
- Delta
- Likely cause category: Entry/mechanics vs Project number vs Unknown

## E) Hypothesis testing

For each major mismatch, test and document:
1) totals line populated vs internal subtotal mismatch
2) project double-count/omission (project inconsistency)
3) wrong UFile line choice (detail vs total)
4) retained earnings mismatch driven by missing dividends / wrong RE linkage
5) duplicated classification in attempt

## F) Conclusions + next actions

Conclude A/B/C with evidence and provide:
- Fix checklist for UFile UI next attempt (exact actions)
- Fix checklist for project outputs (only if proven)

---

# Final output requirements

Write a single primary report:
- `outputs/ATTEMPT_DIAGNOSIS.md`

It must include:
- Executive summary
- Evidence index
- Diagnostics list
- Extracted S100/S125/RE tables
- Recalculations
- Attempt vs project comparison
- Hypothesis testing results
- Conclusion A/B/C
- Fix checklists

Also include `README.md` at the run root.

Do not make any other changes outside `RUN_DIR/`.

