You are Claude Code (agentic coding assistant). Work inside the repository at:

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

# Dedicated Claude run directory (prevents mixing with Codex runs)

Create a new run directory (recommended):

- `./T2Analysis/tools/new_run_dirs.sh FY2025 ufile claude`

Use the printed path as `RUN_DIR`. (If you cannot run the script, create the same structure manually.)

Inside `RUN_DIR`, use this structure:

- `inputs/`  (copies of evidence files you relied on)
- `work/`    (intermediate extracted text, scratch notebooks/scripts, parsed tables)
- `outputs/` (final report + final machine-readable tables)

Also write a short `README.md` in `RUN_DIR` describing:
- what you ran
- what evidence you used
- what you concluded

Important: **Do not place outputs inside `UfileToFill/.../attempts/`**; keep Claude output isolated under `T2Analysis/.../analyses/claude/...`.

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

1) Extract the full text of the PDF to `work/attempt_fy2025.txt`.
   - Prefer `pdftotext` if installed.
   - If you need a Python dependency (e.g., `pdfplumber`), create a venv **inside** `RUN_DIR/work/venv/`.
2) In `outputs/diagnostics.md`, list every diagnostic line:
   - include exact text
   - include page section context if available (“Diagnostics page 1 of 3”, etc.)
   - classify: Blocking vs Non-blocking

## B) Extract what was actually in the return (verbatim tables)

From the attempt text, extract the complete set of populated lines for:

### Schedule 100 (Balance Sheet)
At minimum capture: `1001, 1121/1120, 1301, 1484/1480, 2620, 2680, 2781/2780, 3500, 3600, 2599, 3499, 3620, 3640`

### Retained earnings section
Capture: `3660, 3680, 3700 (if present), 3849` and any “other items” lines.

### Schedule 125 (Income Statement)
Capture: `8000, 8299, 8300, 8320, 8500, 8518, 8519, 9367, 9368` plus every expense line populated.

Output machine-readable artifacts:
- `outputs/attempt_schedule_100.csv`
- `outputs/attempt_retained_earnings.csv`
- `outputs/attempt_schedule_125.csv`

## C) Independently recompute UFile internal math (show-your-work)

Using only amounts extracted from the attempt:

1) Recompute **Operating expenses** = sum of all detail expense lines (exclude 9367/9368 totals).
2) Recompute **COGS** both ways (if possible):
   - from movement: `8300 + 8320 - 8500`
   - from `8518` if populated
3) Recompute **Gross profit**: `total revenue - COGS`
4) Recompute **Net income**: `gross profit - operating expenses`
5) Recompute **Shareholder equity**: `3500 + 3600`
6) Recompute the **balance equation**: `2599` vs `(3499 + 3620)` and also `3640` consistency.

For each, provide:
- equation
- substituted values
- resulting delta

Write these reconciliations to:
- `outputs/recalculations.md`

## D) Compare attempt vs project expected values (prove which side is off)

Create a comparison table with columns:
- Field (GIFI code / schedule line)
- Attempt value (from PDF)
- Project expected value (from packet/snapshot artifacts)
- Delta
- Likely cause category:
  - Entry/mechanics issue
  - Underlying accounting/project number issue
  - Unknown (needs more evidence)

Write:
- `outputs/attempt_vs_project_comparison.csv`
- and summarize key deltas in the report.

## E) Hypothesis testing (do not assume a winner)

For each major mismatch, explicitly test at least these hypotheses:

1) UFile totals line populated vs internal subtotal mismatch (detail lines disagree with totals).
2) Project double-counted or omitted something (project numbers internally inconsistent).
3) Wrong UFile line choice (detail vs total, e.g., `1120` vs `1121`, `1480` vs `1484`, `2780` vs `2781`, `8299` usage).
4) Retained earnings mismatch caused by missing dividends input (3700) or wrong RE opening/closing linkage.
5) Duplicate classification in the attempt (same expense effectively entered twice under different codes).

Document which hypothesis is supported/rejected and why.

## F) Conclusions + next actions

Decide whether the primary root cause is A, B, or C and justify.

Then provide two checklists:

### 1) “Fix in UFile UI next attempt”
Exact steps like “clear line X”, “enter only on codes A/B/C”, “recalculate”, “verify tie-out”.

### 2) “Fix in project outputs (if needed)”
Only if you can prove a project-side inconsistency. Specify:
- what schedule/line is wrong
- what the corrected value should be
- what evidence supports it

---

# Final output requirements

Create a single primary report:
- `outputs/ATTEMPT_DIAGNOSIS.md`

It must include:
- Executive summary
- Evidence index (every file you used)
- Diagnostics list (blocking vs non-blocking)
- Extracted Schedule 100/125/RE tables
- Recalculations (show your work)
- Attempt vs project comparison table
- Hypothesis test results
- Final conclusion: A/B/C
- Fix checklists

Also create:
- `README.md` at the run root summarizing how to reproduce.

Do not make any other changes outside `RUN_DIR/`.

