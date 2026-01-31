#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    allocation_rounding,
    connect_db,
    load_rules,
)


PROFILE_METHOD = "CURB_PG_SAMPLE"
MANUAL_PROFILE_METHOD = "MANUAL_OVERRIDE"
COMPONENT_OVERRIDE_METHOD = "BILL_COMPONENT_OVERRIDE"


def ensure_output_dir() -> Path:
    out_dir = PROJECT_ROOT / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def output_suffix(*, fys: list[str] | None, vendor_keys: list[str] | None) -> str:
    """
    Avoid overwriting the full, all-vendors report when running a targeted rebuild.
    """
    parts: list[str] = []
    if fys:
        parts.append("fy_" + "_".join(sorted({f.strip() for f in fys if f and f.strip()})))
    if vendor_keys:
        parts.append("vendors_" + "_".join(sorted({v.strip() for v in vendor_keys if v and v.strip()})))
    if not parts:
        return ""
    return "__partial__" + "__".join(parts)


@dataclass(frozen=True)
class FiscalYear:
    fy: str
    start_date: str
    end_date: str


def load_fiscal_years(conn: sqlite3.Connection, fy_filters: list[str] | None) -> list[FiscalYear]:
    rows = conn.execute("SELECT fy, start_date, end_date FROM fiscal_years ORDER BY start_date").fetchall()
    fys = [FiscalYear(fy=r["fy"], start_date=r["start_date"], end_date=r["end_date"]) for r in rows]
    if fy_filters:
        allowed = {f.strip() for f in fy_filters if f and f.strip()}
        fys = [f for f in fys if f.fy in allowed]
    if not fys:
        raise SystemExit("No fiscal years found (did you run scripts/00_init_db.py?)")
    return fys


def fetch_latest_profile_id(conn: sqlite3.Connection, *, vendor_key: str, entity: str) -> int | None:
    # Prefer manual override profiles when present.
    row = conn.execute(
        """
        SELECT id
        FROM vendor_profiles
        WHERE vendor_key = ?
          AND entity = ?
          AND method = ?
        ORDER BY created_at DESC, id DESC
        LIMIT 1
        """,
        (vendor_key, entity, MANUAL_PROFILE_METHOD),
    ).fetchone()
    if row:
        return int(row["id"])

    row = conn.execute(
        """
        SELECT id
        FROM vendor_profiles
        WHERE vendor_key = ?
          AND entity = ?
          AND method = ?
        ORDER BY created_at DESC, id DESC
        LIMIT 1
        """,
        (vendor_key, entity, PROFILE_METHOD),
    ).fetchone()
    return int(row["id"]) if row else None


def fetch_profile_weights(conn: sqlite3.Connection, profile_id: int) -> list[tuple[str, float]]:
    rows = conn.execute(
        """
        SELECT account_code, percent
        FROM vendor_profile_splits
        WHERE profile_id = ?
        ORDER BY account_code
        """,
        (profile_id,),
    ).fetchall()
    weights: list[tuple[str, float]] = []
    for r in rows:
        account_code = (r["account_code"] or "").strip()
        percent = float(r["percent"] or 0.0)
        if account_code and percent > 0:
            weights.append((account_code, percent))
    return weights


def normalize_weights_for_vendor(*, vendor_key: str, weights: list[tuple[str, float]]) -> list[tuple[str, float]]:
    """
    Vendor-specific cleanup of sample-derived weights.

    Costco: exclude internal placeholder "Pending Receipt - No ITC" (9100) and renormalize.
    Renormalization is handled by allocation_rounding() which scales weights to their sum.
    """
    if vendor_key == "COSTCO":
        return [(code, pct) for code, pct in weights if code != "9100"]
    return weights


def delete_allocations_for_bills(conn: sqlite3.Connection, wave_bill_ids: list[int]) -> None:
    if not wave_bill_ids:
        return
    placeholders = ",".join("?" for _ in wave_bill_ids)
    conn.execute(f"DELETE FROM bill_allocations WHERE wave_bill_id IN ({placeholders})", wave_bill_ids)


def delete_vendor_profile_allocations_for_bills(conn: sqlite3.Connection, wave_bill_ids: list[int]) -> None:
    """
    Deletes only allocations that this script is responsible for (vendor profile estimates + tax ITC),
    preserving any manual allocations that were intentionally entered elsewhere.
    """
    if not wave_bill_ids:
        return
    placeholders = ",".join("?" for _ in wave_bill_ids)
    conn.execute(
        f"""
        DELETE FROM bill_allocations
        WHERE wave_bill_id IN ({placeholders})
          AND method IN ('VENDOR_PROFILE_ESTIMATE', 'TAX_ITC', '{COMPONENT_OVERRIDE_METHOD}')
        """,
        wave_bill_ids,
    )


def fetch_existing_net_allocated_cents(conn: sqlite3.Connection, *, wave_bill_id: int, hst_itc_code: str) -> int:
    """
    Sum of existing allocations that represent the bill's *net* amount (excluding TAX_ITC and excluding
    any allocations posted directly to the ITC account_code).
    """
    row = conn.execute(
        """
        SELECT COALESCE(SUM(amount_cents), 0) AS n
        FROM bill_allocations
        WHERE wave_bill_id = ?
          AND method NOT IN ('TAX_ITC')
          AND account_code != ?
        """,
        (wave_bill_id, hst_itc_code),
    ).fetchone()
    return int(row["n"] or 0)


def is_excluded_bill(
    *,
    rules: dict,
    wave_bill_id: int,
    source_row: int | None,
    invoice_number: str | None,
    vendor_raw: str,
) -> bool:
    exclude = rules.get("exclude_wave_bills") or {}
    if not isinstance(exclude, dict):
        return False

    invoice_numbers = exclude.get("invoice_numbers") or []
    if isinstance(invoice_numbers, list) and invoice_number:
        if invoice_number in {str(x).strip() for x in invoice_numbers}:
            return True

    vendor_raw_exact = exclude.get("vendor_raw_exact") or []
    if isinstance(vendor_raw_exact, list):
        if vendor_raw in {str(x) for x in vendor_raw_exact}:
            return True

    source_rows = exclude.get("source_rows") or []
    if isinstance(source_rows, list) and source_row is not None:
        if int(source_row) in {int(x) for x in source_rows if str(x).strip()}:
            return True

    wave_bill_ids = exclude.get("wave_bill_ids") or []
    if isinstance(wave_bill_ids, list):
        if wave_bill_id in {int(x) for x in wave_bill_ids if str(x).strip()}:
            return True

    return False


def _bill_component_override_cfg(rules: dict, *, vendor_key: str, wave_bill_id: int) -> dict | None:
    """
    Returns the per-bill override mapping (if present) for a vendor bill.

    Expected shape in overrides/vendor_profile_rules.yml:
      bill_component_overrides:
        COSTCO:
          "143":
            label: ...
            fixed_net_allocations:
              - {account_code, amount_cents, note}
            apply_profile_to_remainder: true
    """
    root = rules.get("bill_component_overrides")
    if not isinstance(root, dict):
        return None
    by_vendor = root.get(vendor_key)
    if not isinstance(by_vendor, dict):
        return None
    cfg = by_vendor.get(str(wave_bill_id)) or by_vendor.get(int(wave_bill_id) if str(wave_bill_id).isdigit() else str(wave_bill_id))
    return cfg if isinstance(cfg, dict) else None


def _apply_bill_component_override(
    conn: sqlite3.Connection,
    *,
    cfg: dict,
    fy: str,
    vendor_key: str,
    wave_bill_id: int,
    invoice_date: str,
    vendor_raw: str,
    invoice_number: str | None,
    bill_net_cents: int,
    detail_rows: list[dict[str, str]],
    summary: dict[tuple[str, str, str], int],
) -> int:
    """
    Inserts fixed allocations for a bill (net-only), returning total inserted cents.

    These allocations are treated as "manual" for the purpose of later profile application:
    the vendor profile is applied only to the remaining net amount.
    """
    alloc_list = cfg.get("fixed_net_allocations") or cfg.get("allocations") or []
    if not isinstance(alloc_list, list) or not alloc_list:
        return 0

    label = str(cfg.get("label") or "").strip()
    inserted = 0
    for item in alloc_list:
        if not isinstance(item, dict):
            continue
        account_code = str(item.get("account_code") or "").strip()
        amount_cents = int(item.get("amount_cents") or 0)
        note = str(item.get("note") or "").strip()
        if not account_code or amount_cents <= 0:
            continue

        inserted += amount_cents
        if inserted > int(bill_net_cents):
            raise SystemExit(
                f"bill_component_overrides {vendor_key} wave_bill_id={wave_bill_id}: "
                f"fixed allocations exceed bill net (inserted={inserted} net_cents={bill_net_cents})"
            )

        notes = f"{fy} {label}".strip()
        if note:
            notes = (notes + " | " if notes else "") + note

        conn.execute(
            """
            INSERT INTO bill_allocations
              (wave_bill_id, account_code, amount_cents, method, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (wave_bill_id, account_code, amount_cents, COMPONENT_OVERRIDE_METHOD, notes),
        )

        detail_rows.append(
            {
                "fy": fy,
                "vendor_key": vendor_key,
                "wave_bill_id": str(wave_bill_id),
                "source_row": "",
                "invoice_date": invoice_date,
                "vendor_raw": vendor_raw,
                "invoice_number": invoice_number or "",
                "net_amount": f"{bill_net_cents/100:.2f}",
                "tax_amount": "",
                "account_code": account_code,
                "amount": f"{amount_cents/100:.2f}",
                "method": COMPONENT_OVERRIDE_METHOD,
                "profile_id": "",
            }
        )
        summary[(fy, vendor_key, account_code)] += int(amount_cents)

    return inserted


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--fy", action="append", dest="fys", help="Limit output to a fiscal year (repeatable).")
    ap.add_argument("--entity", default="corp")
    ap.add_argument("--vendor-key", action="append", dest="vendor_keys", help="Limit to a vendor key (repeatable).")
    ap.add_argument("--reset", action="store_true", help="Delete existing allocations for affected bills before applying.")
    args = ap.parse_args()

    rules = load_rules()
    policy = rules.get("policy") or {}
    if not isinstance(policy, dict) or not policy.get("assume_wave_is_pure_cogs_for_eligible_vendors"):
        raise SystemExit("Policy switch disabled: policy.assume_wave_is_pure_cogs_for_eligible_vendors must be true.")

    eligible_vendor_keys = rules.get("eligible_vendor_keys") or []
    if not isinstance(eligible_vendor_keys, list) or not eligible_vendor_keys:
        raise SystemExit("No eligible_vendor_keys configured in overrides/vendor_profile_rules.yml")

    vendor_keys = args.vendor_keys or [str(v) for v in eligible_vendor_keys]

    tax_cfg = rules.get("tax") or {}
    treat_tax_as_itc = bool(tax_cfg.get("treat_tax_as_hst_itc", True))
    hst_itc_code = str(tax_cfg.get("hst_itc_account_code") or "2210").strip()

    conn = connect_db(args.db)
    out_dir = ensure_output_dir()
    suffix = output_suffix(fys=args.fys, vendor_keys=args.vendor_keys)
    detail_csv_path = out_dir / f"vendor_allocations_by_fy{suffix}.csv"
    summary_csv_path = out_dir / f"vendor_allocations_summary_by_fy{suffix}.csv"
    skipped_csv_path = out_dir / f"vendor_allocations_skipped{suffix}.csv"

    detail_rows: list[dict[str, str]] = []
    skipped_rows: list[dict[str, str]] = []
    summary: dict[tuple[str, str, str], int] = defaultdict(int)  # (fy, vendor_key, account_code) -> cents

    try:
        fys = load_fiscal_years(conn, args.fys)

        for fy in fys:
            for vendor_key in vendor_keys:
                profile_id = fetch_latest_profile_id(conn, vendor_key=vendor_key, entity=args.entity)
                if not profile_id:
                    skipped_rows.append(
                        {
                            "fy": fy.fy,
                            "vendor_key": vendor_key,
                            "wave_bill_id": "",
                            "source_row": "",
                            "invoice_date": "",
                            "vendor_raw": "",
                            "reason": "missing_vendor_profile",
                            "notes": "",
                        }
                    )
                    continue

                weights = fetch_profile_weights(conn, profile_id)
                weights = normalize_weights_for_vendor(vendor_key=vendor_key, weights=weights)
                if not weights:
                    skipped_rows.append(
                        {
                            "fy": fy.fy,
                            "vendor_key": vendor_key,
                            "wave_bill_id": "",
                            "source_row": "",
                            "invoice_date": "",
                            "vendor_raw": "",
                            "reason": "empty_vendor_profile_splits",
                            "notes": f"profile_id={profile_id}",
                        }
                    )
                    continue

                bills = conn.execute(
                    """
                    SELECT id, source_row, invoice_date, vendor_raw, vendor_key, invoice_number, net_cents, tax_cents
                    FROM wave_bills
                    WHERE vendor_key = ?
                      AND invoice_date >= ?
                      AND invoice_date <= ?
                    ORDER BY invoice_date, source_row, id
                    """,
                    (vendor_key, fy.start_date, fy.end_date),
                ).fetchall()

                bill_ids_to_reset: list[int] = []
                for b in bills:
                    wave_bill_id = int(b["id"])
                    source_row = int(b["source_row"]) if b["source_row"] is not None else None
                    invoice_date = str(b["invoice_date"])
                    vendor_raw = str(b["vendor_raw"])
                    invoice_number = (b["invoice_number"] or "").strip() or None
                    net_cents = int(b["net_cents"] or 0)
                    tax_cents = int(b["tax_cents"] or 0)

                    if is_excluded_bill(
                        rules=rules,
                        wave_bill_id=wave_bill_id,
                        source_row=source_row,
                        invoice_number=invoice_number,
                        vendor_raw=vendor_raw,
                    ):
                        if args.reset:
                            bill_ids_to_reset.append(wave_bill_id)
                        skipped_rows.append(
                            {
                                "fy": fy.fy,
                                "vendor_key": vendor_key,
                                "wave_bill_id": str(wave_bill_id),
                                "source_row": str(source_row or ""),
                                "invoice_date": invoice_date,
                                "vendor_raw": vendor_raw,
                                "reason": "excluded_by_override",
                                "notes": "",
                            }
                        )
                        continue

                    bill_ids_to_reset.append(wave_bill_id)
                    if args.reset:
                        continue

                    # If we are not resetting, skip bills that already have allocations.
                    existing = conn.execute(
                        "SELECT COUNT(*) AS n FROM bill_allocations WHERE wave_bill_id = ?",
                        (wave_bill_id,),
                    ).fetchone()
                    if int(existing["n"] or 0) > 0:
                        skipped_rows.append(
                            {
                                "fy": fy.fy,
                                "vendor_key": vendor_key,
                                "wave_bill_id": str(wave_bill_id),
                                "source_row": str(source_row or ""),
                                "invoice_date": invoice_date,
                                "vendor_raw": vendor_raw,
                                "reason": "already_allocated",
                                "notes": "",
                            }
                        )
                        continue

                    allocations = allocation_rounding(net_cents, weights)
                    alloc_sum = sum(a for _, a in allocations)
                    if alloc_sum != net_cents:
                        raise SystemExit(
                            f"Allocation sum mismatch for wave_bill_id={wave_bill_id}: expected {net_cents} got {alloc_sum}"
                        )

                    for account_code, amount_cents in allocations:
                        conn.execute(
                            """
                            INSERT INTO bill_allocations
                              (wave_bill_id, account_code, amount_cents, method, profile_id, notes)
                            VALUES (?, ?, ?, ?, ?, ?)
                            """,
                            (
                                wave_bill_id,
                                account_code,
                                amount_cents,
                                "VENDOR_PROFILE_ESTIMATE",
                                profile_id,
                                f"{fy.fy} profile_id={profile_id}",
                            ),
                        )
                        detail_rows.append(
                            {
                                "fy": fy.fy,
                                "vendor_key": vendor_key,
                                "wave_bill_id": str(wave_bill_id),
                                "source_row": str(source_row or ""),
                                "invoice_date": invoice_date,
                                "vendor_raw": vendor_raw,
                                "invoice_number": invoice_number or "",
                                "net_amount": f"{net_cents/100:.2f}",
                                "tax_amount": f"{tax_cents/100:.2f}",
                                "account_code": account_code,
                                "amount": f"{amount_cents/100:.2f}",
                                "method": "VENDOR_PROFILE_ESTIMATE",
                                "profile_id": str(profile_id),
                            }
                        )
                        summary[(fy.fy, vendor_key, account_code)] += amount_cents

                    if treat_tax_as_itc and tax_cents:
                        conn.execute(
                            """
                            INSERT INTO bill_allocations
                              (wave_bill_id, account_code, amount_cents, method, notes)
                            VALUES (?, ?, ?, ?, ?)
                            """,
                            (wave_bill_id, hst_itc_code, tax_cents, "TAX_ITC", f"{fy.fy} HST ITC"),
                        )
                        detail_rows.append(
                            {
                                "fy": fy.fy,
                                "vendor_key": vendor_key,
                                "wave_bill_id": str(wave_bill_id),
                                "source_row": str(source_row or ""),
                                "invoice_date": invoice_date,
                                "vendor_raw": vendor_raw,
                                "invoice_number": invoice_number or "",
                                "net_amount": f"{net_cents/100:.2f}",
                                "tax_amount": f"{tax_cents/100:.2f}",
                                "account_code": hst_itc_code,
                                "amount": f"{tax_cents/100:.2f}",
                                "method": "TAX_ITC",
                                "profile_id": "",
                            }
                        )
                        summary[(fy.fy, vendor_key, hst_itc_code)] += tax_cents

                if args.reset and bill_ids_to_reset:
                    delete_vendor_profile_allocations_for_bills(conn, bill_ids_to_reset)
                    conn.commit()
                    # After reset, re-run allocations in one pass (no "already_allocated" checks).
                    for b in bills:
                        wave_bill_id = int(b["id"])
                        source_row = int(b["source_row"]) if b["source_row"] is not None else None
                        invoice_date = str(b["invoice_date"])
                        vendor_raw = str(b["vendor_raw"])
                        invoice_number = (b["invoice_number"] or "").strip() or None
                        net_cents = int(b["net_cents"] or 0)
                        tax_cents = int(b["tax_cents"] or 0)

                        if is_excluded_bill(
                            rules=rules,
                            wave_bill_id=wave_bill_id,
                            source_row=source_row,
                            invoice_number=invoice_number,
                            vendor_raw=vendor_raw,
                        ):
                            continue

                        # Optional per-bill overrides (e.g., carve out an asset inside a Costco receipt).
                        override_cfg = _bill_component_override_cfg(rules, vendor_key=vendor_key, wave_bill_id=wave_bill_id)
                        if override_cfg and bool(override_cfg.get("apply_profile_to_remainder", True)):
                            _apply_bill_component_override(
                                conn,
                                cfg=override_cfg,
                                fy=fy.fy,
                                vendor_key=vendor_key,
                                wave_bill_id=wave_bill_id,
                                invoice_date=invoice_date,
                                vendor_raw=vendor_raw,
                                invoice_number=invoice_number,
                                bill_net_cents=net_cents,
                                detail_rows=detail_rows,
                                summary=summary,
                            )

                        # Preserve any existing manual allocations by allocating only the remaining net.
                        existing_net_cents = fetch_existing_net_allocated_cents(
                            conn, wave_bill_id=wave_bill_id, hst_itc_code=hst_itc_code
                        )
                        remaining_net_cents = net_cents - existing_net_cents
                        if remaining_net_cents < 0:
                            raise SystemExit(
                                f"Existing allocations exceed bill net for wave_bill_id={wave_bill_id}: "
                                f"net_cents={net_cents} existing_net_cents={existing_net_cents}"
                            )

                        allocations = allocation_rounding(remaining_net_cents, weights)
                        alloc_sum = sum(a for _, a in allocations)
                        if alloc_sum != remaining_net_cents:
                            raise SystemExit(
                                f"Allocation sum mismatch for wave_bill_id={wave_bill_id}: expected {remaining_net_cents} got {alloc_sum}"
                            )

                        for account_code, amount_cents in allocations:
                            conn.execute(
                                """
                                INSERT INTO bill_allocations
                                  (wave_bill_id, account_code, amount_cents, method, profile_id, notes)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """,
                                (
                                    wave_bill_id,
                                    account_code,
                                    amount_cents,
                                    "VENDOR_PROFILE_ESTIMATE",
                                    profile_id,
                                    f"{fy.fy} profile_id={profile_id} remaining_net_cents={remaining_net_cents}",
                                ),
                            )
                            detail_rows.append(
                                {
                                    "fy": fy.fy,
                                    "vendor_key": vendor_key,
                                    "wave_bill_id": str(wave_bill_id),
                                    "source_row": str(source_row or ""),
                                    "invoice_date": invoice_date,
                                    "vendor_raw": vendor_raw,
                                    "invoice_number": invoice_number or "",
                                    "net_amount": f"{net_cents/100:.2f}",
                                    "tax_amount": f"{tax_cents/100:.2f}",
                                    "account_code": account_code,
                                    "amount": f"{amount_cents/100:.2f}",
                                    "method": "VENDOR_PROFILE_ESTIMATE",
                                    "profile_id": str(profile_id),
                                }
                            )
                            summary[(fy.fy, vendor_key, account_code)] += amount_cents

                        if treat_tax_as_itc and tax_cents:
                            # If another process already posted ITC directly to the ITC account code, do not duplicate it.
                            existing_itc = conn.execute(
                                "SELECT COUNT(*) AS n FROM bill_allocations WHERE wave_bill_id = ? AND account_code = ?",
                                (wave_bill_id, hst_itc_code),
                            ).fetchone()
                            if int(existing_itc["n"] or 0) > 0:
                                continue
                            conn.execute(
                                """
                                INSERT INTO bill_allocations
                                  (wave_bill_id, account_code, amount_cents, method, notes)
                                VALUES (?, ?, ?, ?, ?)
                                """,
                                (wave_bill_id, hst_itc_code, tax_cents, "TAX_ITC", f"{fy.fy} HST ITC"),
                            )
                            detail_rows.append(
                                {
                                    "fy": fy.fy,
                                    "vendor_key": vendor_key,
                                    "wave_bill_id": str(wave_bill_id),
                                    "source_row": str(source_row or ""),
                                    "invoice_date": invoice_date,
                                    "vendor_raw": vendor_raw,
                                    "invoice_number": invoice_number or "",
                                    "net_amount": f"{net_cents/100:.2f}",
                                    "tax_amount": f"{tax_cents/100:.2f}",
                                    "account_code": hst_itc_code,
                                    "amount": f"{tax_cents/100:.2f}",
                                    "method": "TAX_ITC",
                                    "profile_id": "",
                                }
                            )
                            summary[(fy.fy, vendor_key, hst_itc_code)] += tax_cents

                    conn.commit()

        conn.commit()

    finally:
        conn.close()

    detail_rows.sort(key=lambda r: (r["fy"], r["vendor_key"], r["invoice_date"], int(r["source_row"] or 0), r["account_code"]))
    skipped_rows.sort(key=lambda r: (r["fy"], r["vendor_key"], r["invoice_date"], r["reason"], r["vendor_raw"]))

    with detail_csv_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "fy",
            "vendor_key",
            "wave_bill_id",
            "source_row",
            "invoice_date",
            "vendor_raw",
            "invoice_number",
            "net_amount",
            "tax_amount",
            "account_code",
            "amount",
            "method",
            "profile_id",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(detail_rows)

    summary_rows: list[dict[str, str]] = []
    for (fy, vendor_key, account_code), cents in sorted(summary.items(), key=lambda t: (t[0][0], t[0][1], t[0][2])):
        summary_rows.append(
            {
                "fy": fy,
                "vendor_key": vendor_key,
                "account_code": account_code,
                "amount": f"{cents/100:.2f}",
            }
        )

    with summary_csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["fy", "vendor_key", "account_code", "amount"])
        w.writeheader()
        w.writerows(summary_rows)

    with skipped_csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["fy", "vendor_key", "wave_bill_id", "source_row", "invoice_date", "vendor_raw", "reason", "notes"])
        w.writeheader()
        w.writerows(skipped_rows)

    print("VENDOR PROFILE APPLICATION COMPLETE")
    print(f"- generated: {datetime.now().isoformat(timespec='seconds')}")
    print(f"- detail: {detail_csv_path}")
    print(f"- summary: {summary_csv_path}")
    print(f"- skipped: {skipped_csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
