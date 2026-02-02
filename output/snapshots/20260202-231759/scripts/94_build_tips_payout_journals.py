#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import sqlite3
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"


@dataclass(frozen=True)
class TipsPayoutRow:
    fy: str
    entry_date: str
    tips_payable_cents: int
    cash_account_code: str
    tips_account_code: str
    journal_entry_id: str


def cents_to_dollars(cents: int) -> str:
    return f"{Decimal(cents) / Decimal(100):.2f}"


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def fetch_tips_payable_from_payroll_summary(
    conn: sqlite3.Connection,
    *,
    payroll_je_id: str,
    tips_payable_code: str,
) -> int:
    row = conn.execute(
        """
        SELECT
          COALESCE(SUM(credit_cents), 0) AS credit_cents,
          COALESCE(SUM(debit_cents), 0) AS debit_cents
        FROM journal_entry_lines
        WHERE journal_entry_id = ? AND account_code = ?
        """,
        (payroll_je_id, tips_payable_code),
    ).fetchone()
    credit = int(row["credit_cents"] or 0)
    debit = int(row["debit_cents"] or 0)
    return credit - debit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--reset", action="store_true", help="Delete existing tips payout journal entries before insert.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    bank_debits_cfg = cfg.get("bank_debits", {}) if isinstance(cfg.get("bank_debits"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("tips_payout") if isinstance(cfg.get("journal_sources"), dict) else {}

    tips_payable_code = str(payroll_cfg.get("tips_payable_code") or "2310").strip()
    cash_on_hand_code = str(bank_debits_cfg.get("cash_on_hand_code") or "1070").strip()

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "tips_payout")
    entry_type = str((source_cfg or {}).get("entry_type") or "ADJUSTMENT")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "tips_payout_journal_summary.md"
    out_detail_csv = args.out_dir / "tips_payout_journal_detail.csv"

    conn = connect_db(args.db)
    try:
        if args.reset:
            conn.execute(
                """
                DELETE FROM journal_entries
                WHERE source_system = ? AND source_record_type = ?
                """,
                (source_system, source_record_type),
            )

        detail_rows: list[TipsPayoutRow] = []

        for fy in fys:
            payroll_je_id = f"PAYROLL_SUMMARY_{fy.fy}"
            tips_payable = fetch_tips_payable_from_payroll_summary(
                conn, payroll_je_id=payroll_je_id, tips_payable_code=tips_payable_code
            )
            if tips_payable <= 0:
                continue

            je_id = f"TIPS_PAYOUT_{fy.fy}"
            description = f"Tips payout clearing (assumed paid) - {fy.fy}"
            notes = f"source_payroll_summary={payroll_je_id}; tips_payable_cents={tips_payable}; method=cash_on_hand"

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

            conn.execute(
                """
                INSERT INTO journal_entries (
                  id, entry_date, entry_type, description,
                  source_system, source_record_type, source_record_id, notes, is_posted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (
                    je_id,
                    fy.end_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    fy.fy,
                    notes,
                ),
            )

            # Debit tips payable (reduce liability), credit cash (represent payout from cash drawer).
            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, 1, ?, ?, 0, ?)
                """,
                (
                    f"{je_id}:1",
                    je_id,
                    tips_payable_code,
                    tips_payable,
                    "Clear tips payable (tips paid out)",
                ),
            )
            conn.execute(
                """
                INSERT INTO journal_entry_lines (
                  id, journal_entry_id, line_number,
                  account_code, debit_cents, credit_cents, description
                ) VALUES (?, ?, 2, ?, 0, ?, ?)
                """,
                (
                    f"{je_id}:2",
                    je_id,
                    cash_on_hand_code,
                    tips_payable,
                    "Tips paid out (cash)",
                ),
            )

            detail_rows.append(
                TipsPayoutRow(
                    fy=fy.fy,
                    entry_date=fy.end_date,
                    tips_payable_cents=tips_payable,
                    cash_account_code=cash_on_hand_code,
                    tips_account_code=tips_payable_code,
                    journal_entry_id=je_id,
                )
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "fy",
                    "entry_date",
                    "tips_payable_cents",
                    "tips_payable_amount",
                    "cash_account_code",
                    "tips_account_code",
                    "journal_entry_id",
                ]
            )
            for r in detail_rows:
                w.writerow(
                    [
                        r.fy,
                        r.entry_date,
                        r.tips_payable_cents,
                        cents_to_dollars(r.tips_payable_cents),
                        r.cash_account_code,
                        r.tips_account_code,
                        r.journal_entry_id,
                    ]
                )

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Tips payout journal summary\n\n")
            f.write("This journal clears **tips payable** (2310) to cash on hand.\n\n")
            f.write("Note:\n")
            f.write("- If tips are fully included in payroll e-transfers, the payroll summary will not create tips payable and\n")
            f.write("  this report will show no entries.\n\n")
            if not detail_rows:
                f.write("- No tips payout entries were required.\n")
            else:
                for r in detail_rows:
                    f.write(f"## {r.fy}\n\n")
                    f.write(f"- Journal entry: `{r.journal_entry_id}`\n")
                    f.write(f"- Entry date: {r.entry_date}\n")
                    f.write(f"- Tips cleared: ${cents_to_dollars(r.tips_payable_cents)}\n")
                    f.write(f"- Debit: {r.tips_account_code} (Tips Payable)\n")
                    f.write(f"- Credit: {r.cash_account_code} (Cash on Hand)\n\n")

        conn.commit()

    finally:
        conn.close()

    print("TIPS PAYOUT JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
