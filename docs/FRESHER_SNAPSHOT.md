# Fresher → T2-final snapshot (frozen reconciliation-as-data)

This project is trying to **stop relying on “whatever scripts ran last”** and instead treat the reconciliation outcome as **immutable data** with explicit provenance.

Fresher already contains the reconciliation decisions we made (manual Wave bill inserts/deletes/edits, bank classifications, links, etc.), but those decisions currently live inside:
- SQLite DB state (`canteen_reconciliation_v2.db`, `credits_reconciliation.db`)
- override files (`/home/clarencehub/Fresh/Fresher/overrides/*`)
- generated reports (`/home/clarencehub/Fresh/Fresher/output/latest/*`, `/home/clarencehub/Fresh/Fresher/output/audits/*`)

The goal of this snapshot is to **freeze the *result*** into a folder inside `t2-final-fy2024-fy2025/` so downstream work (trial balance → GIFI schedules) can treat it as a **source of truth** without re-running Fresher scripts or “SQL patches”.

## What the snapshot contains

Running `scripts/40_snapshot_fresher_state.py` creates:

```
data/fresher_snapshots/<snapshot_id>/
  snapshot_manifest.yml              # file list + sha256 (authoritative)
  db/
    canteen_reconciliation_v2.db     # copied (read-only source snapshot)
    credits_reconciliation.db        # copied (read-only source snapshot)
  tables/
    debits/*.csv                     # exports of *all* tables from canteen_reconciliation_v2.db
    credits/*.csv                    # exports of *all* tables from credits_reconciliation.db
  fresher_overrides/                 # copied from /home/clarencehub/Fresh/Fresher/overrides/
  fresher_reports/
    latest/                          # copied from /home/clarencehub/Fresh/Fresher/output/latest/
    audits/                          # copied from /home/clarencehub/Fresh/Fresher/output/audits/
  fresher_credits_reports/
    output/                          # copied from /home/clarencehub/Fresh/Fresher/credits/output/
```

## Why both DB + CSV exports?

- The copied DBs are the **exact** reconciliation end-state and are the easiest way to retain full detail.
- The CSV exports are for **human review, diffing, and re-import into other systems** without SQLite-specific tooling.

## Invariants / intent

- The snapshot is **append-only**: never edit files in a snapshot folder.
- If reconciliation decisions change, generate a **new** snapshot and update `manifest/sources.yml` to point at it.
- GIFI generation should depend on:
  - snapshot facts + explicit account mapping overrides,
  - **not** Fresher code execution order.
