#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import math
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


@dataclass(frozen=True)
class ApplyStats:
    profiles_loaded: int = 0
    documents_touched: int = 0
    lines_inserted: int = 0
    documents_missing_amounts: int = 0


def default_overrides_path() -> Path:
    return SOT_ROOT / "overrides" / "vendor_profile_overrides.json"


def _parse_profiles(path: Path) -> list[dict]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    profiles = raw.get("vendor_profiles")
    if not isinstance(profiles, list):
        raise ValueError("Expected JSON object with key 'vendor_profiles' (list).")
    out: list[dict] = []
    for p in profiles:
        if not isinstance(p, dict):
            continue
        vendor = str(p.get("vendor_normalized") or "").strip().lower()
        key = str(p.get("profile_key") or "").strip()
        splits = p.get("splits") or []
        if not vendor or not key or not isinstance(splits, list) or not splits:
            continue
        norm_splits: list[dict] = []
        for s in splits:
            if not isinstance(s, dict):
                continue
            account_code = str(s.get("account_code") or "").strip()
            percent = s.get("percent")
            if not account_code:
                continue
            if not isinstance(percent, (int, float)):
                continue
            norm_splits.append({"account_code": account_code, "percent": float(percent)})
        if not norm_splits:
            continue
        notes = str(p.get("notes") or "").strip() or None
        out.append({"vendor_normalized": vendor, "profile_key": key, "notes": notes, "splits": norm_splits})
    return out


def _validate_profile(profile: dict) -> None:
    splits = profile["splits"]
    total = sum(float(s["percent"]) for s in splits)
    if not math.isfinite(total) or abs(total - 1.0) > 1e-6:
        raise ValueError(
            f"Profile {profile['profile_key']} for {profile['vendor_normalized']} must sum to 1.0; got {total}"
        )
    for s in splits:
        pct = float(s["percent"])
        if pct < 0:
            raise ValueError(f"Negative percent in profile {profile['profile_key']}: {s}")


def _apportion(total_cents: int, splits: list[dict]) -> list[int]:
    # Hamilton (largest remainder) method; deterministic given split ordering.
    # Works for positive or negative totals.
    if total_cents == 0:
        return [0] * len(splits)

    sign = 1 if total_cents >= 0 else -1
    total_abs = abs(total_cents)

    exacts = [total_abs * float(s["percent"]) for s in splits]
    bases = [int(math.floor(x)) for x in exacts]
    remainder = total_abs - sum(bases)

    fracs = [(i, exacts[i] - bases[i]) for i in range(len(splits))]
    fracs.sort(key=lambda t: (-t[1], t[0]))

    amounts = bases[:]
    for i in range(remainder):
        amounts[fracs[i % len(fracs)][0]] += 1

    return [sign * a for a in amounts]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--overrides", type=Path, default=default_overrides_path())
    ap.add_argument("--reset-vendors", action="store_true", help="Delete existing lines for affected vendors first.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.overrides.exists():
        print(f"No vendor profile overrides file found: {args.overrides}")
        return 0

    profiles = _parse_profiles(args.overrides)
    for p in profiles:
        _validate_profile(p)

    conn = connect_db(args.db)
    stats = ApplyStats(profiles_loaded=len(profiles))
    try:
        apply_migrations(conn)
        conn.execute("BEGIN")

        account_names = {
            str(r["account_code"]): str(r["account_name"])
            for r in conn.execute("SELECT account_code, account_name FROM chart_of_accounts").fetchall()
        }

        for profile in profiles:
            vendor = profile["vendor_normalized"]
            profile_key = profile["profile_key"]
            profile_notes = profile["notes"]
            splits = profile["splits"]

            doc_rows = conn.execute(
                """
                SELECT d.id, d.total_cents, d.tax_cents, d.net_cents
                FROM documents d
                JOIN counterparties c ON c.id=d.counterparty_id
                WHERE c.normalized_name = ?
                  AND d.source_system='T2_FINAL_DB'
                  AND d.source_record_id LIKE 'fresher_debits__wave_bills:%'
                ORDER BY d.doc_date, d.id
                """,
                (vendor,),
            ).fetchall()

            doc_ids = [int(r["id"]) for r in doc_rows]
            if args.reset_vendors and doc_ids:
                placeholders = ",".join(["?"] * len(doc_ids))
                if args.dry_run:
                    print(f"WOULD: DELETE document_lines for vendor={vendor} docs={len(doc_ids)}")
                else:
                    conn.execute(f"DELETE FROM document_lines WHERE document_id IN ({placeholders})", doc_ids)

            for dr in doc_rows:
                doc_id = int(dr["id"])
                total_cents = dr["total_cents"]
                tax_cents = dr["tax_cents"]
                net_cents = dr["net_cents"]

                if total_cents is None and net_cents is None:
                    stats = ApplyStats(
                        profiles_loaded=stats.profiles_loaded,
                        documents_touched=stats.documents_touched,
                        lines_inserted=stats.lines_inserted,
                        documents_missing_amounts=stats.documents_missing_amounts + 1,
                    )
                    continue

                if net_cents is not None:
                    base_cents = int(net_cents)
                elif total_cents is not None and tax_cents is not None:
                    base_cents = int(total_cents) - int(tax_cents)
                else:
                    base_cents = int(total_cents) if total_cents is not None else 0

                if not args.dry_run and not args.reset_vendors:
                    conn.execute("DELETE FROM document_lines WHERE document_id=?", (doc_id,))

                amounts = _apportion(base_cents, splits)
                line_no = 0
                for split, cents in zip(splits, amounts, strict=True):
                    if cents == 0:
                        continue
                    line_no += 1
                    account_code = str(split["account_code"])
                    description = account_names.get(account_code)
                    notes_parts = [
                        f"vendor_profile_override:{profile_key}",
                        f"percent={split['percent']}",
                    ]
                    if profile_notes:
                        notes_parts.append(profile_notes)
                    notes = "; ".join(notes_parts)
                    if args.dry_run:
                        continue
                    conn.execute(
                        """
                        INSERT INTO document_lines(
                          document_id, line_no, description,
                          account_code, amount_cents, tax_cents,
                          method, notes
                        )
                        VALUES (?, ?, ?, ?, ?, NULL, 'MANUAL', ?)
                        """,
                        (doc_id, line_no, description, account_code, int(cents), notes),
                    )
                    stats = ApplyStats(
                        profiles_loaded=stats.profiles_loaded,
                        documents_touched=stats.documents_touched,
                        lines_inserted=stats.lines_inserted + 1,
                        documents_missing_amounts=stats.documents_missing_amounts,
                    )

                if tax_cents is not None and int(tax_cents) != 0:
                    line_no += 1
                    notes = f"vendor_profile_override:{profile_key}; TAX_ITC from document.tax_cents"
                    if args.dry_run:
                        continue
                    conn.execute(
                        """
                        INSERT INTO document_lines(
                          document_id, line_no, description,
                          account_code, amount_cents, tax_cents,
                          method, notes
                        )
                        VALUES (?, ?, 'HST ITC Receivable', '2210', ?, NULL, 'TAX_ITC', ?)
                        """,
                        (doc_id, line_no, int(tax_cents), notes),
                    )
                    stats = ApplyStats(
                        profiles_loaded=stats.profiles_loaded,
                        documents_touched=stats.documents_touched,
                        lines_inserted=stats.lines_inserted + 1,
                        documents_missing_amounts=stats.documents_missing_amounts,
                    )

                stats = ApplyStats(
                    profiles_loaded=stats.profiles_loaded,
                    documents_touched=stats.documents_touched + 1,
                    lines_inserted=stats.lines_inserted,
                    documents_missing_amounts=stats.documents_missing_amounts,
                )

        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()
    finally:
        conn.close()

    print("VENDOR PROFILE OVERRIDES APPLY COMPLETE")
    print(f"- db: {args.db}")
    print(f"- overrides: {args.overrides}")
    print(f"- profiles_loaded: {stats.profiles_loaded}")
    print(f"- documents_touched: {stats.documents_touched}")
    print(f"- document_lines_inserted: {stats.lines_inserted if not args.dry_run else 0}")
    print(f"- documents_missing_amounts: {stats.documents_missing_amounts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

