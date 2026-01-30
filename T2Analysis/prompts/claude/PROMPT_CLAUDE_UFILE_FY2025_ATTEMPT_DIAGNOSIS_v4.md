You are Claude Code. Work inside:

- `/home/clarencehub/t2-final-fy2024-fy2025`

This is a **read‑only forensic review** of FY2025 UFile Attempt 4 with **extra focus on Shopify/merchant fees and app subscriptions**.

---

# Non‑negotiable safety rules

1) **Read‑only** with respect to existing data:
   - Do NOT edit, delete, or overwrite anything under `UfileToFill/`, `output/`, `docs/`, `data/`, or any DB files.
2) **All outputs must go only** to a new run directory under `T2Analysis/`.
3) Treat both UFile output and project accounting outputs as potentially wrong until reconciled.

---

# Create a dedicated Claude run directory

Run:
- `./T2Analysis/tools/new_run_dirs.sh FY2025 ufile claude`

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
2) **Reconcile Shopify fees vs merchant account fees and identify app subscriptions**:
   - 5300 Merchant account fees (Wave bills)
   - 6210 Shopify payout fees (bank inflows)
   - 6620 Software & SaaS (possible Shopify apps)
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

## C) Shopify/merchant fee deep dive (focus)

From the DB (`db/t2_final.db`) and Wave bills:
1) Sum FY2025 **5300** vs **6210** vs **6620**.
2) List all FY2025 Wave bills that hit **5300** with:
   - bill date, vendor, invoice #, net/tax/total, allocation
3) List Shopify‑related Wave bills (vendor contains “Shopify”) and show which accounts they were allocated to (5300 vs 6620 vs 6600 vs 6550).
4) Pull the Shopify payout fees total from **bank inflows** (6210) and compare to Shopify gateway exports:
   - `output/snapshots/20260129-192249/output/shopify_gateway_reports_selected.csv`
   - `output/snapshots/20260129-192249/output/shopify_gateway_vs_payouts_audit.md`

Decide:
- Are the Wave “Shopify CC Fees” bills **separate** charges (e.g., monthly invoices/apps/chargebacks)?
- Or are they **duplicate** of payout‑net fees?

Output: `RUN_DIR/outputs/merchant_fees_review.md`

## D) Recommendations (no edits)
Provide a concrete next‑step plan to resolve any duplication:
1) which source should be trusted,
2) how to verify with supporting documents,
3) what correction would be required if duplication is confirmed.

Output: `RUN_DIR/outputs/next_actions.md`

---

Deliverable: a short, evidence‑cited forensic report in `RUN_DIR/outputs/` with no data changes.

