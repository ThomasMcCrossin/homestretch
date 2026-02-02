# UFile T2 – Filing Packet Index (FY2024 + FY2025)

This `UfileToFill/` directory is a **copy/paste reference** of UFile screens and the CRA GIFI lists.

The **actual, validated** fill guides and structured packet live under `UfileToFill/ufile_packet/`.

## Source-of-truth snapshot (amounts + schedules)

- `output/snapshots/20260129-192249/output/`

## Use these guides while filing in UFile (one year at a time)

- FY2024 (2023-06-01 → 2024-05-31): `UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md`
- FY2025 (2024-06-01 → 2025-05-31): `UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md`

## Packet (for LLM review / structured storage)

- Combined packet (both years): `UfileToFill/ufile_packet/packet.json`
- FY-specific packets:
  - `UfileToFill/ufile_packet/years/FY2024/packet.json`
  - `UfileToFill/ufile_packet/years/FY2025/packet.json`

## Validator (run anytime you change mappings)

`python3 UfileToFill/ufile_packet/tools/validate_packet.py`

## Key UFile entry mapping notes (high impact)

UFile totals can ignore “summary” lines; enter **detail** lines where applicable:

- Inventory: enter on **`1121`** (not `1120`)
- Prepaids: enter on **`1484`** (not `1480`)

We also corrected several mis-mappings that were causing obviously-wrong UFile placements:

- Shipping & delivery expense: **`9275`** (Delivery, freight and express), not farming/trucking `9801`
- Packaging & operating supplies: **`9130`** (Supplies), not `8810`
- Computer hardware + SaaS (expensed): **`8813`** (Data processing), not `8810`
- Internet: **`9225`** (Telephone and telecommunications), not `9220`
