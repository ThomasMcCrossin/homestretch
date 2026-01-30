# Run README (template)

## Purpose
Forensic, audit-style diagnosis of the FY2025 UFile T2 attempt using the repo’s pre-generated parsed evidence bundle (text + CSV tables), without modifying any accounting numbers or project outputs.

## Agent
- Codex CLI

## Run directory
`/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_163211`

## Inputs used
- Parsed bundle (copied into `inputs/parsed_bundle/` from `T2Analysis/t2_attempts/FY2025/ufile/parses/latest/`)
  - `inputs/parsed_bundle/meta.json`
  - `inputs/parsed_bundle/verification_report.md`
  - `inputs/parsed_bundle/diagnostics.csv`
  - `inputs/parsed_bundle/schedule_100.csv`
  - `inputs/parsed_bundle/schedule_125.csv`
  - `inputs/parsed_bundle/retained_earnings.csv`
  - `inputs/parsed_bundle/full_text.txt`
  - `inputs/parsed_bundle/pages/page_012.txt`
  - `inputs/parsed_bundle/pages/page_013.txt`
  - `inputs/parsed_bundle/pages/page_014.txt`
- Project “expected” values (copied into `inputs/project/`)
  - `inputs/project/packet.json`
  - `inputs/project/UFILet2_FILL_GUIDE.md`
- GIFI catalogs (copied into `inputs/gifi/`)
  - `inputs/gifi/BalanceSheet.txt`
  - `inputs/gifi/IncomeStatement.txt`
  - `inputs/gifi/NetIncome.txt`

## Commands run
From repo root (to create this run directory):
- `./T2Analysis/tools/new_run_dirs.sh FY2025 ufile codex`

From this run directory:
- `PYTHONDONTWRITEBYTECODE=1 python3 work/analyze_ufile_attempt.py`

## Outputs generated
- `outputs/ATTEMPT_DIAGNOSIS.md` (primary report)
- `outputs/diagnostics.md`
- `outputs/recalculations.md`
- `outputs/attempt_vs_project_comparison.csv`

## Findings summary
- Blocking validity failures are explained by (1) `9367` not matching the sum of expense detail lines, and (2) Schedule 100 not balancing (`2599` ≠ `3499 + 3620`).
- The Schedule 100 imbalance equals the Schedule 125 net income (`36,054`), pointing to retained earnings rollforward / dividends entry mechanics.
- Compared to the project packet, the attempt is missing dividends (`3700`) and appears to have an incorrect opening retained earnings (`3660`), overstating retained earnings/equity by the year’s net income.
