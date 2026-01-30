# T2 attempts (FY-specific)

This folder organizes multi-attempt, multi-agent work for UFile filing readiness.

Each fiscal year gets its own folder:
- `FY2024/`
- `FY2025/`

Within each year:
- `ufile/exports/`
  - Raw UFile exports for that year (PDFs, printouts, etc.)
  - Do not edit; treat as evidence snapshots.
- `ufile/analyses/<agent>/run_YYYYMMDD_HHMMSS/`
  - All scratch work, extracted text, and final reports for that run.
  - Must include `inputs/`, `work/`, `outputs/`.

This is intentionally separate from `UfileToFill/.../attempts/`, which is where you might drop the original UFile export. We can reference/copy exports into `T2Analysis/.../exports/` when needed for traceability.

