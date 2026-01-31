You are working inside the repository at:

- `{REPO_ROOT}`

This task is a forensic, audit-style diagnosis of a **UFile T2 filing attempt**.

- Fiscal year: `{FY}`
- Attempt: `{ATTEMPT_ID}`
- Agent: `{AGENT}`

This prompt assumes we use a **parsed evidence bundle** (text + CSV tables) generated from the UFile-exported PDF so the analysis is repeatable and less error-prone.

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
   - `{RUN_DIR}`

3) You **MAY** create new files under your run directory (markdown report, extracted text, CSVs, JSONs, scratch scripts, venv, etc.).

4) You **MUST NOT** write anywhere else. If a tool tries to write outside your run directory, stop and choose another approach.

5) Treat **both** UFile output and the project accounting outputs as potentially wrong until reconciled.

---

# Dedicated run directory (prevents mixing runs)

Use the run directory:
- `{RUN_DIR}`

Inside it, use:
- `inputs/`
- `work/`
- `outputs/`

Also create:
- `RUN_DIR/README.md` summarizing what you ran and how to reproduce.

---

# Evidence (read-only sources)

## Raw UFile export (attempt PDF)
- `{EXPORT_PDF}`

## UFile “Messages” / warnings (required)
- `{MESSAGES_TXT}`

Copy the messages file you relied on into `RUN_DIR/inputs/`.

## Parsed evidence bundle (preferred analysis input)
- `{PARSE_DIR}`

Parsed bundle contains:
  - `meta.json`
  - `verification_report.md`
  - `text/full_text.txt`
  - `tables/schedule_100.csv`
  - `tables/schedule_125.csv`
  - `tables/retained_earnings.csv`
  - `tables/diagnostics.csv`
  - (optional) `ufile_messages.txt`

If the parse bundle is missing or `verification_report.md` shows issues, stop and regenerate the parse bundle before continuing.

For traceability, copy the specific parsed artifacts you relied on into `RUN_DIR/inputs/` (do not move originals).

## Project “expected” values (may be wrong; must be tested)
- `UfileToFill/ufile_packet/packet.json`
- `UfileToFill/ufile_packet/years/{FY}/packet.json`
- `UfileToFill/ufile_packet/years/{FY}/UFILet2_FILL_GUIDE.md`
- `UfileToFill/ufile_packet/years/{FY}/UFILet2_FILL_GUIDE.html` (if present)

## Accounting exports (may be wrong; must be tested)
Use whichever are relevant for your comparisons:
- `output/trial_balance_{FY}.csv`
- `output/gifi_schedule_100_{FY}.csv`
- `output/gifi_schedule_125_{FY}.csv`
- `output/gifi_retained_earnings_{FY}.csv`
- `output/schedule_1_{FY}.csv`
- `output/schedule_8_{FY}.csv` (if CCA exists)

---

# Objective

Determine (with explicit arithmetic) why the `{FY}` UFile attempt produced diagnostics, warnings, and/or non-balancing schedules, and decide whether root cause is:

- **A) UFile entry mechanics / UFile auto-calculation behavior**
- **B) Wrong underlying numbers from the project (DB/snapshots/scripts/mappings)**
- **C) A mix**

You are not allowed to fix anything in this run—only diagnose and propose specific next actions.

---

# FY-specific mandatory checks (must not skip)

## UFile messages mapping (always required)
Read the attempt’s `messages.txt` and for each message:
- restate it verbatim
- identify the likely UFile screen(s)
- explain what it implies (field missing vs mismatch vs informational)
- list the most likely next UI actions (what to enter/clear)

For FY2024 Attempt1, pay special attention to:
- “Depreciation has been entered but CCA class is missing - verify.”
- “There is no entry in the income source section; all income is considered as active business income.”

Write to: `RUN_DIR/outputs/messages_mapping.md`

## PDF package completeness (schedule forms vs references)
UFile can reference schedules without printing the actual schedule forms in the exported PDF (depending on export/print settings and whether the schedule has entered detail).

For the attempt PDF, verify whether the PDF actually contains the **schedule form headers** (e.g., `T2 SCH 8`) for schedules that should be present:
- Schedule 8 (CCA) if any CCA is being claimed / depreciation is referenced
- Schedule 7 (SBD) if CCPC with taxable income / SBD claims
- Schedule 3 (dividends) if dividends/Part IV tax is present
- Schedule 88 if internet income disclosure is present

Prefer to use the automated check and paste its output into your report:
`python3 T2Analysis/tools/check_ufile_export_completeness.py --fy {FY} --pdf {EXPORT_PDF}`

Write to: `RUN_DIR/outputs/pdf_completeness.md`

---

# Method (required)

## 0) Validate the parsed bundle before trusting it

Read `{PARSE_DIR}/verification_report.md`.
If it shows any “Not OK” rows, treat parse outputs as untrusted and regenerate/adjust parsing before continuing.

## A) Diagnostics catalogue (UFile diagnostics + UFile messages)

Use `tables/diagnostics.csv` (cross-check against `text/full_text.txt`) to list every diagnostic line:
- exact text
- classify: Blocking vs Non-blocking

Also incorporate `messages.txt` findings.

Write to: `RUN_DIR/outputs/diagnostics.md`

## B) Extracted schedules (use the CSVs)

Use:
- Schedule 100: `tables/schedule_100.csv`
- Schedule 125: `tables/schedule_125.csv`
- Retained earnings: `tables/retained_earnings.csv`

Spot-check a few lines back to the PDF text for confidence.

Minimum lines to explicitly include in your extracted tables / comparisons (even if zero):
- Schedule 100: `1001, 1121/1120, 1301, 1484/1480, 1740/1741 (if present), 2620, 2680, 2781/2780, 3500, 3600, 2599, 3499, 3620, 3640`
- Retained earnings: `3660, 3680, 3700 (if present), 3740 (if present), 3849`
- Schedule 125: `8000, 8299, 8300, 8320, 8500, 8518, 8519, 9367, 9368` plus **every populated expense line**
- Schedule 1: if present in the PDF/attempt, extract key codes: `A, 104 (if present), 206, 403, 500, 510, C`

## C) Independent recomputation (show-your-work)

Using only parsed attempt amounts:
1) Operating expenses = sum of detail expense lines (exclude totals like 9367/9368).
2) COGS from movement: `8300 + 8320 - 8500`, compare to 8518 if present.
3) Gross profit = total revenue - COGS.
4) Net income = gross profit - operating expenses.
5) Equity = 3500 + 3600.
6) Balance equation: 2599 vs (3499 + 3620) and 3640 consistency.

Write to: `RUN_DIR/outputs/recalculations.md`

## D) Attempt vs project comparison (must include deltas)

Create `RUN_DIR/outputs/attempt_vs_project_comparison.csv`:
- Field (GIFI code / schedule line)
- Attempt value
- Project expected value (from `UfileToFill/ufile_packet/years/{FY}/packet.json` and/or `output/*.csv`)
- Delta
- Likely cause: Entry/mechanics vs Project number vs Unknown

## E) Hypothesis testing (must write conclusions)

For each major mismatch, test and document:
1) totals line populated vs internal subtotal mismatch
2) project double-count/omission (project inconsistency)
3) wrong UFile line choice (detail vs total)
4) retained earnings mismatch driven by missing dividends / wrong RE linkage
5) duplicated classification in attempt
6) CCA/Schedule 8 presence:
   - if UFile says depreciation/CCA exists, confirm Schedule 8 is populated and Schedule 1 code 403 ties
   - if Schedule 8 is present in project outputs but not in attempt, diagnose the UI entry gap

Write to: `RUN_DIR/outputs/hypotheses.md`

## F) Packaging / containers root-cause track (FY2024 + FY2025)

This is a cross-year tax-risk item: take-out containers and primary packaging are often part of finished goods cost and may belong in inventory/COGS timing (depending on how much is on hand at year-end).

Do not “decide policy” blindly. Determine root cause with evidence:

1) Locate packaging-related TB accounts and their mapped GIFI lines for `{FY}`:
   - Typically accounts like `5200/5201/5202/5203` (containers/cups/bags/wrapping/utensils) and where they land (often `9130 Supplies`).
2) Compare to inventory mechanics:
   - opening inventory, closing inventory, and whether year-end count includes packaging on hand.
3) Explain whether this is:
   - mapping-only issue, OR
   - inventory-count/policy issue, OR
   - both
4) Write a concrete, testable fix proposal (but do not implement it in this run).

Write to: `RUN_DIR/outputs/packaging_root_cause.md`

---

# Final output requirements

Write the primary report:
- `RUN_DIR/outputs/ATTEMPT_DIAGNOSIS.md`

It must include:
- Executive summary
- Evidence index (every file you used)
- Diagnostics list (blocking vs non-blocking)
- Messages mapping (warnings → screens/actions)
- Extracted Schedule 100/125/retained earnings (from parsed CSVs)
- Recalculations (show your work)
- Attempt vs project comparison (with deltas)
- Packaging root-cause (linked to inventory/COGS timing)
- Final conclusion: A/B/C
- Fix checklists:
  - UFile UI next attempt (exact actions)
  - Project outputs (only if proven by deltas)

Also create:
- `RUN_DIR/README.md` at the run root summarizing how to reproduce.
