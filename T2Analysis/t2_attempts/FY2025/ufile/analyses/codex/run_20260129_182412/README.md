# Codex run (FY2025 UFile) — forensic diagnosis

## Scope / ATTEMPT_ID
- Fiscal year: `FY2025`
- UFile attempt analyzed: `attempt_002`
- Safety: read-only for `UfileToFill/`, `output/`, `docs/`, `data/`, DBs; all writes are confined to this run directory.

## Inputs used (copied for traceability)
- Parsed bundle: `inputs/parsed_bundle/` (from `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_002/`)
- UFile Messages: `inputs/exports/messages.txt` (from `T2Analysis/t2_attempts/FY2025/ufile/exports/attempt_002/messages.txt`)
- Project expected values + guide: `inputs/project/`
- Accounting outputs used for “go deeper” traces: `inputs/accounting_outputs/`

## How to reproduce
From the repo root:
```bash
RUN_DIR="T2Analysis/t2_attempts/FY2025/ufile/analyses/codex/run_20260129_182412"
PYTHONDONTWRITEBYTECODE=1 python3 "$RUN_DIR/work/analyze_ufile_attempt_v2.py"
```

## Outputs produced
- Primary report: `outputs/ATTEMPT_DIAGNOSIS.md`
- Diagnostics (incl. Messages → screens/fields mapping): `outputs/diagnostics.md`
- Extracted schedules (Schedule 100/125/retained earnings): `outputs/extracted_schedules.md`
- Recalculations (show-your-work): `outputs/recalculations.md`
- Attempt vs project comparison: `outputs/attempt_vs_project_comparison.csv`
- Go deeper: `outputs/9270_trace.md`, `outputs/suspense_accounts_trace.md`

