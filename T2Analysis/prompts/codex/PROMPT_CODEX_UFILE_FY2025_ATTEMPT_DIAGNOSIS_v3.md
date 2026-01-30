You are Codex CLI. Work inside:

- `/home/clarencehub/t2-final-fy2024-fy2025`

This is a **read‑only forensic review** of FY2025 UFile Attempt 4 with a special focus on **merchant/processing fees**.

---

# Non‑negotiable safety rules

1) **Read‑only** with respect to existing data:
   - Do NOT edit, delete, or overwrite anything under `UfileToFill/`, `output/`, `docs/`, `data/`, or any DB files.
2) **All outputs must go only** to a new run directory under `T2Analysis/`.
3) Treat both UFile output and project accounting outputs as potentially wrong until reconciled.

---

# Create a dedicated Codex run directory

Run:
- `./T2Analysis/tools/new_run_dirs.sh FY2025 ufile codex`

Use that `RUN_DIR`:
- `RUN_DIR/inputs/` (copies of evidence used)
- `RUN_DIR/work/` (scratch)
- `RUN_DIR/outputs/` (final report + tables)

---

# Evidence (required)

**Attempt 4 (canonical)**
- PDF: `T2Analysis/t2_attempts/FY2025/ufile/exports/attempt_004/ufile_return.pdf`
- Messages: `T2Analysis/t2_attempts/FY2025/ufile/exports/attempt_004/messages.txt`
- Parsed bundle: `T2Analysis/t2_attempts/FY2025/ufile/parses/attempt_004/`

**Project expectations**
- Packet: `UfileToFill/ufile_packet/years/FY2025/packet.json`
- Guide: `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`
- Snapshot outputs: `output/snapshots/20260129-192249/output/`

Copy the exact files you use into `RUN_DIR/inputs/` (do not move originals).

---

# Objective

1) Confirm Attempt 4 is internally consistent (no BCR blockers).
2) Reconcile **merchant/processing fees**:
   - Why do we have **two numbers** in FY2025:
     - 5300 Merchant account fees (Wave bills)
     - 6210 Shopify payout fees (bank inflows)
   - Determine whether this is **valid two‑stream fees** or a **double‑count**.
3) Provide **clear next actions** without changing source data.

---

# Required analysis steps

## A) Diagnostics summary
Use `messages.txt` + `tables/diagnostics.csv` to list each warning, the screen it maps to, and whether it is blocking.

Output: `RUN_DIR/outputs/diagnostics.md`

## B) Attempt 4 vs Packet (critical deltas only)
Compare Attempt 4 tables (`schedule_100.csv`, `schedule_125.csv`, `retained_earnings.csv`) against packet tables:
- `UfileToFill/ufile_packet/tables/schedule_100_FY2025.csv`
- `UfileToFill/ufile_packet/tables/schedule_125_FY2025.csv`
- `UfileToFill/ufile_packet/tables/schedule_1_FY2025.csv`

Output: `RUN_DIR/outputs/attempt_vs_packet.csv`

## C) Merchant fee deep dive (focus)

From the DB (`db/t2_final.db`):
- Sum FY2025 5300 vs 6210
- Break down by `source_system` / `source_record_type`
- Identify the largest Wave bills that hit 5300 (e.g., “Shopify – Bill 2024 CC Fees”).
- Identify Shopify payout fee lines that hit 6210.

Then decide:
1) Are Wave bills **separate charges** (e.g., merchant account fees not netted in payouts)?  
2) Or are they duplicating payout deductions (double‑count risk)?

Output: `RUN_DIR/outputs/merchant_fees_review.md`

## D) Recommendations (no edits)
Provide specific next steps if duplication is suspected (which source to trust, how to verify).

Output: `RUN_DIR/outputs/next_actions.md`

---

Deliverable: a short, evidence‑cited forensic report in `RUN_DIR/outputs/` with no data changes.

