#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, dollars_to_cents, load_yaml


DEFAULT_RULES_PATH = PROJECT_ROOT / "overrides" / "manual_adjustment_journals.yml"


@dataclass(frozen=True)
class JournalLine:
    account_code: str
    debit_cents: int
    credit_cents: int
    description: str | None


def load_adjustments(path: Path) -> list[dict]:
    if not path.exists():
        return []
    data = load_yaml(path)
    adj = data.get("adjustments")
    if adj is None:
        return []
    if not isinstance(adj, list):
        raise SystemExit(f"Expected 'adjustments' to be a list in {path}")
    out: list[dict] = []
    for item in adj:
        if not isinstance(item, dict):
            raise SystemExit(f"Invalid adjustment item in {path}: expected mapping")
        out.append(item)
    return out


def load_accounts(path: Path) -> list[dict]:
    if not path.exists():
        return []
    data = load_yaml(path)
    acct = data.get("accounts")
    if acct is None:
        return []
    if not isinstance(acct, list):
        raise SystemExit(f"Expected 'accounts' to be a list in {path}")
    out: list[dict] = []
    for item in acct:
        if not isinstance(item, dict):
            raise SystemExit(f"Invalid account item in {path}: expected mapping")
        out.append(item)
    return out


def parse_lines(lines_raw: object) -> list[JournalLine]:
    if not isinstance(lines_raw, list) or not lines_raw:
        raise SystemExit("Each adjustment must have a non-empty 'lines' list")
    out: list[JournalLine] = []
    for idx, line in enumerate(lines_raw, start=1):
        if not isinstance(line, dict):
            raise SystemExit("Invalid line: expected mapping")
        account_code = str(line.get("account_code") or "").strip()
        if not account_code:
            raise SystemExit("Line missing account_code")
        debit_raw = line.get("debit")
        credit_raw = line.get("credit")
        debit_cents = dollars_to_cents(debit_raw) if debit_raw not in (None, "") else 0
        credit_cents = dollars_to_cents(credit_raw) if credit_raw not in (None, "") else 0
        if debit_cents and credit_cents:
            raise SystemExit(f"Line {idx} has both debit and credit")
        if debit_cents < 0 or credit_cents < 0:
            raise SystemExit(f"Line {idx} has negative amount (use the correct side)")
        desc = str(line.get("description") or "").strip() or None
        out.append(JournalLine(account_code=account_code, debit_cents=debit_cents, credit_cents=credit_cents, description=desc))
    return out


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--rules", type=Path, default=DEFAULT_RULES_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing manual adjustment journals before insert.")
    args = ap.parse_args()

    source_system = "t2-final"
    source_record_type = "manual_adjustment"

    accounts = load_accounts(args.rules)
    adjustments = load_adjustments(args.rules)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    out_summary_md = args.out_dir / "manual_adjustment_journal_summary.md"
    out_detail_csv = args.out_dir / "manual_adjustment_journal_detail.csv"

    detail_rows: list[dict[str, str]] = []
    inserted = 0

    conn = connect_db(args.db)
    try:
        for acct in accounts:
            account_code = str(acct.get("account_code") or "").strip()
            account_name = str(acct.get("account_name") or "").strip()
            account_type = str(acct.get("account_type") or "").strip()
            if not account_code or not account_name or not account_type:
                raise SystemExit("Each account must have 'account_code', 'account_name', and 'account_type'")

            conn.execute(
                """
                INSERT INTO chart_of_accounts
                  (account_code, account_name, account_type, parent_code, gifi_code, t2125_line,
                   is_active, requires_receipt, is_tax_account, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
                ON CONFLICT(account_code) DO NOTHING
                """,
                (
                    account_code,
                    account_name,
                    account_type,
                    (str(acct.get("parent_code") or "").strip() or None),
                    (str(acct.get("gifi_code") or "").strip() or None),
                    (str(acct.get("t2125_line") or "").strip() or None),
                    1 if str(acct.get("is_active", "1")).strip() not in ("0", "false", "False") else 0,
                    1 if str(acct.get("requires_receipt", "0")).strip() in ("1", "true", "True") else 0,
                    1 if str(acct.get("is_tax_account", "0")).strip() in ("1", "true", "True") else 0,
                ),
            )

        if args.reset:
            conn.execute(
                """
                DELETE FROM journal_entries
                WHERE source_system = ? AND source_record_type = ?
                """,
                (source_system, source_record_type),
            )

        for adj in adjustments:
            adj_id = str(adj.get("id") or "").strip()
            entry_date = str(adj.get("entry_date") or "").strip()
            entry_type = str(adj.get("entry_type") or "ADJUSTMENT").strip()
            description = str(adj.get("description") or "").strip() or None
            notes = str(adj.get("notes") or "").strip() or None
            if not adj_id or not entry_date:
                raise SystemExit("Each adjustment must have 'id' and 'entry_date'")

            je_id = f"MANUAL_ADJ_{adj_id}"
            lines = parse_lines(adj.get("lines"))

            debit_total = sum(l.debit_cents for l in lines)
            credit_total = sum(l.credit_cents for l in lines)
            if debit_total != credit_total:
                raise SystemExit(f"Unbalanced manual adjustment {adj_id}: debit={debit_total} credit={credit_total}")

            conn.execute(
                """
                INSERT OR REPLACE INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id,
                  notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    entry_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    adj_id,
                    notes,
                ),
            )

            for line_number, line in enumerate(lines, start=1):
                conn.execute(
                    """
                    INSERT INTO journal_entry_lines (
                      id, journal_entry_id, line_number,
                      account_code, debit_cents, credit_cents, description
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        f"{je_id}:{line_number}",
                        je_id,
                        line_number,
                        line.account_code,
                        line.debit_cents,
                        line.credit_cents,
                        line.description,
                    ),
                )

                detail_rows.append(
                    {
                        "adjustment_id": adj_id,
                        "journal_entry_id": je_id,
                        "entry_date": entry_date,
                        "entry_type": entry_type,
                        "account_code": line.account_code,
                        "debit": cents_to_dollars(line.debit_cents),
                        "credit": cents_to_dollars(line.credit_cents),
                        "line_description": line.description or "",
                        "journal_description": description or "",
                    }
                )

            inserted += 1

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "adjustment_id",
                "journal_entry_id",
                "entry_date",
                "entry_type",
                "account_code",
                "debit",
                "credit",
                "line_description",
                "journal_description",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Manual adjustment journals\n\n")
            f.write(f"- Rules: `{args.rules}`\n")
            f.write(f"- Scope: deterministic (explicit entry_date per adjustment)\n")
            f.write(f"- Journal entries posted: {inserted}\n")
            f.write(f"- Output detail: `{out_detail_csv}`\n")

        conn.commit()

    finally:
        conn.close()

    print("MANUAL ADJUSTMENT JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- posted: {inserted}")
    print(f"- out: {out_summary_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
