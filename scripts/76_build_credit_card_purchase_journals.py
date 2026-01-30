#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    allocation_rounding,
    connect_db,
    fiscal_years_from_manifest,
    load_manifest,
    load_yaml,
)


DEFAULT_CONFIG_PATH = PROJECT_ROOT / "overrides" / "journalization_config.yml"


@dataclass(frozen=True)
class CCTxn:
    id: str
    txn_date: str
    merchant: str
    txn_type: str
    debit_cents: int
    credit_cents: int
    card_last4: str

    @property
    def gross_cents(self) -> int:
        if self.txn_type == "PURCHASE":
            return self.debit_cents
        if self.txn_type == "REFUND":
            return self.credit_cents
        return 0


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    return load_yaml(path)


def parse_iso(d: str | None) -> date | None:
    if not d:
        return None
    return date.fromisoformat(d)


def scope_window(fys) -> tuple[str, str]:
    start = min(fy.start_date for fy in fys)
    end = max(fy.end_date for fy in fys)
    return start, end


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def split_tax_inclusive(amount_cents: int, *, rate: Decimal) -> tuple[int, int]:
    if amount_cents == 0:
        return (0, 0)
    if rate <= 0:
        return (amount_cents, 0)
    gross = Decimal(int(amount_cents))
    denom = Decimal("1") + rate
    net = (gross / denom).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    net_cents = int(net)
    tax_cents = int(amount_cents) - net_cents
    return (net_cents, tax_cents)


def match_cc_vendor_key(merchant: str) -> str | None:
    m = (merchant or "").lower()
    if "costco" in m:
        return "COSTCO"
    if "superstore" in m:
        return "ATLANTIC_SUPERSTORE"
    if "wal-mart" in m or "walmart" in m:
        return "WALMART"
    if "pharmasave" in m or "pharma save" in m:
        return "PHARMASAVE"
    if "canadian tire" in m and "gas" not in m:
        return "CANADIAN_TIRE"
    return None


def find_matching_wave_bill_id(conn, *, vendor_key: str, amount_cents: int, txn_date: str, window_days: int = 2) -> int | None:
    d = parse_iso(txn_date)
    if not d:
        return None
    start = (d - timedelta(days=window_days)).isoformat()
    end = (d + timedelta(days=window_days)).isoformat()
    row = conn.execute(
        """
        SELECT id
        FROM wave_bills
        WHERE vendor_key = ?
          AND total_cents = ?
          AND invoice_date >= ? AND invoice_date <= ?
        ORDER BY invoice_date, id
        LIMIT 1
        """,
        (vendor_key, int(amount_cents), start, end),
    ).fetchone()
    return int(row["id"]) if row else None


def fetch_latest_profile_weights(conn, *, vendor_key: str, entity: str) -> list[tuple[str, float]]:
    # Prefer manual override profiles when present.
    row = conn.execute(
        """
        SELECT id
        FROM vendor_profiles
        WHERE vendor_key = ?
          AND entity = ?
          AND method = 'MANUAL_OVERRIDE'
        ORDER BY created_at DESC, id DESC
        LIMIT 1
        """,
        (vendor_key, entity),
    ).fetchone()
    if not row:
        row = conn.execute(
            """
            SELECT id
            FROM vendor_profiles
            WHERE vendor_key = ?
              AND entity = ?
            ORDER BY created_at DESC, id DESC
            LIMIT 1
            """,
            (vendor_key, entity),
        ).fetchone()
    if not row:
        return []
    profile_id = int(row["id"])
    rows = conn.execute(
        """
        SELECT account_code, percent
        FROM vendor_profile_splits
        WHERE profile_id = ?
        ORDER BY account_code
        """,
        (profile_id,),
    ).fetchall()
    out: list[tuple[str, float]] = []
    for r in rows:
        code = (r["account_code"] or "").strip()
        pct = float(r["percent"] or 0.0)
        if code and pct > 0:
            out.append((code, pct))
    # Vendor-specific cleanup:
    # Costco sample-derived splits sometimes include internal placeholder 9100 (Pending Receipt - No ITC).
    # That bucket is an artifact and must be redistributed across the real buckets by renormalizing
    # weights without 9100. allocation_rounding() handles renormalization.
    if vendor_key == "COSTCO":
        out = [(c, p) for c, p in out if c != "9100"]
    return out


def default_account_for_merchant(merchant: str) -> tuple[str, str]:
    m = (merchant or "").lower()
    if "freight" in m or "shipping" in m or "freightcom" in m:
        return ("5100", "keyword:freight")
    if "shell" in m or "irving" in m or "petro" in m or "esso" in m or "ultramar" in m:
        return ("9200", "keyword:fuel")
    if "dollarama" in m:
        return ("6600", "keyword:dollarama")
    if "kent " in m or m.startswith("kent"):
        return ("6300", "keyword:kent_repairs")
    return ("5020", "default:cogs_supplements")


def fetch_cc_txns(conn, *, start_date: str, end_date: str) -> list[CCTxn]:
    rows = conn.execute(
        """
        SELECT
          id,
          txn_date,
          COALESCE(NULLIF(TRIM(merchant_parsed), ''), description) AS merchant,
          txn_type,
          CAST(debit_cents AS INTEGER) AS debit_cents,
          CAST(credit_cents AS INTEGER) AS credit_cents,
          COALESCE(card_last4, '') AS card_last4
        FROM fresher_debits__cc_transactions
        WHERE txn_date >= ? AND txn_date <= ?
          AND txn_type IN ('PURCHASE', 'REFUND')
        ORDER BY txn_date, CAST(id AS INTEGER)
        """,
        (start_date, end_date),
    ).fetchall()
    out: list[CCTxn] = []
    for r in rows:
        out.append(
            CCTxn(
                id=str(r["id"]),
                txn_date=str(r["txn_date"]),
                merchant=str(r["merchant"] or ""),
                txn_type=str(r["txn_type"] or ""),
                debit_cents=int(r["debit_cents"] or 0),
                credit_cents=int(r["credit_cents"] or 0),
                card_last4=str(r["card_last4"] or ""),
            )
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    ap.add_argument("--entity", default="corp")
    ap.add_argument("--reset", action="store_true", help="Delete existing credit-card purchase journals before insert.")
    ap.add_argument("--clear-only", action="store_true", help="Delete existing credit-card purchase journals and exit.")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    cfg = load_config(args.config)
    tax_cfg = cfg.get("tax", {}) if isinstance(cfg.get("tax"), dict) else {}
    payroll_cfg = cfg.get("payroll", {}) if isinstance(cfg.get("payroll"), dict) else {}
    source_cfg = (cfg.get("journal_sources") or {}).get("credit_card_purchases") if isinstance(cfg.get("journal_sources"), dict) else {}

    hst_rate = Decimal(str(tax_cfg.get("hst_rate") if "hst_rate" in tax_cfg else "0.15"))
    hst_itc_code = str(tax_cfg.get("hst_itc_code") or "2210").strip()
    itc_start_date = str(tax_cfg.get("itc_start_date") or "2024-02-26").strip()
    itc_start = date.fromisoformat(itc_start_date)

    dwayne_payable_code = str(payroll_cfg.get("due_to_shareholder_dwayne_code") or "2410").strip()

    source_system = str((source_cfg or {}).get("source_system") or "t2-final")
    source_record_type = str((source_cfg or {}).get("source_record_type") or "credit_card_purchases")
    entry_type = str((source_cfg or {}).get("entry_type") or "PURCHASE")

    start_date, end_date = scope_window(fys)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary_md = args.out_dir / "cc_purchase_journal_summary.md"
    out_detail_csv = args.out_dir / "cc_purchase_journal_detail.csv"
    out_skipped_csv = args.out_dir / "cc_purchase_journal_skipped.csv"

    conn = connect_db(args.db)
    try:
        if args.clear_only:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )
            conn.commit()
            print("CC PURCHASE JOURNALS CLEARED")
            print(f"- db: {args.db}")
            print(f"- source_record_type: {source_record_type}")
            return 0

        if args.reset:
            conn.execute(
                "DELETE FROM journal_entries WHERE source_system = ? AND source_record_type = ?",
                (source_system, source_record_type),
            )

        txns = fetch_cc_txns(conn, start_date=start_date, end_date=end_date)

        posted = 0
        skipped = 0
        used_default = 0
        used_profile = 0

        detail_rows: list[dict[str, str]] = []
        skipped_rows: list[dict[str, str]] = []

        for t in txns:
            gross = t.gross_cents
            if gross <= 0:
                continue

            vendor_key = match_cc_vendor_key(t.merchant) or ""
            matched_wave_bill_id = None
            if vendor_key:
                matched_wave_bill_id = find_matching_wave_bill_id(
                    conn,
                    vendor_key=vendor_key,
                    amount_cents=gross,
                    txn_date=t.txn_date,
                    window_days=2,
                )

            if matched_wave_bill_id is not None:
                skipped += 1
                skipped_rows.append(
                    {
                        "cc_txn_id": t.id,
                        "txn_date": t.txn_date,
                        "txn_type": t.txn_type,
                        "amount": cents_to_dollars(gross),
                        "merchant": t.merchant,
                        "vendor_key": vendor_key,
                        "reason": "matched_wave_bill",
                        "wave_bill_id": str(matched_wave_bill_id),
                    }
                )
                continue

            txn_d = date.fromisoformat(t.txn_date)
            allow_itc = txn_d >= itc_start

            primary_account, primary_reason = default_account_for_merchant(t.merchant)
            if primary_account == "9200":
                allow_itc = False

            net_cents, tax_cents = (gross, 0)
            if allow_itc:
                net_cents, tax_cents = split_tax_inclusive(gross, rate=hst_rate)

            allocations: list[tuple[str, int, str]] = []  # (account_code, cents, method)
            used_profile_for_txn = False

            if vendor_key:
                weights = fetch_latest_profile_weights(conn, vendor_key=vendor_key, entity=args.entity)
                if weights:
                    used_profile_for_txn = True
                    used_profile += 1
                    for account_code, cents in allocation_rounding(net_cents, weights):
                        if cents:
                            allocations.append((account_code, cents, f"VENDOR_PROFILE:{vendor_key}"))
                else:
                    used_default += 1
                    allocations.append((primary_account, net_cents, primary_reason))
            else:
                used_default += 1
                allocations.append((primary_account, net_cents, primary_reason))

            if tax_cents:
                allocations.append((hst_itc_code, tax_cents, f"ITC_ESTIMATE:{hst_rate}"))

            je_id = f"CC_PURCHASE_{t.id}"
            description = f"CC {t.txn_type.title()} - {t.merchant}".strip()
            notes = (
                f"cc_txn_id={t.id}; txn_type={t.txn_type}; card_last4={t.card_last4}; "
                f"merchant={t.merchant}; vendor_key={vendor_key}; gross_cents={gross}; net_cents={net_cents}; tax_cents={tax_cents}; "
                f"itc_start_date={itc_start_date}; itc_applied={1 if (tax_cents and allow_itc) else 0}; mapping={primary_reason}"
            )

            conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
            conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))

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
                    t.txn_date,
                    entry_type,
                    description,
                    source_system,
                    source_record_type,
                    t.id,
                    notes,
                ),
            )

            line_number = 1
            debit_total = 0
            credit_total = 0

            if t.txn_type == "PURCHASE":
                for acct, cents, method in allocations:
                    if cents == 0:
                        continue
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
                            acct,
                            cents,
                            0,
                            method,
                        ),
                    )
                    debit_total += cents
                    line_number += 1

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
                        dwayne_payable_code,
                        0,
                        gross,
                        "Due to shareholder (Dwayne) - personal credit card purchase",
                    ),
                )
                credit_total += gross

            elif t.txn_type == "REFUND":
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
                        dwayne_payable_code,
                        gross,
                        0,
                        "Due to shareholder (Dwayne) - personal credit card refund",
                    ),
                )
                debit_total += gross
                line_number += 1

                for acct, cents, method in allocations:
                    if cents == 0:
                        continue
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
                            acct,
                            0,
                            cents,
                            f"REVERSAL:{method}",
                        ),
                    )
                    credit_total += cents
                    line_number += 1

            if debit_total != credit_total:
                conn.execute("DELETE FROM journal_entry_lines WHERE journal_entry_id = ?", (je_id,))
                conn.execute("DELETE FROM journal_entries WHERE id = ?", (je_id,))
                raise SystemExit(f"Unbalanced CC journal {je_id}: debits={debit_total} credits={credit_total}")

            posted += 1
            detail_rows.append(
                {
                    "cc_txn_id": t.id,
                    "txn_date": t.txn_date,
                    "txn_type": t.txn_type,
                    "amount": cents_to_dollars(gross),
                    "amount_cents": str(gross),
                    "merchant": t.merchant,
                    "vendor_key": vendor_key,
                    "net_cents": str(net_cents),
                    "tax_cents": str(tax_cents),
                    "mapping": "VENDOR_PROFILE" if used_profile_for_txn else primary_reason,
                    "journal_entry_id": je_id,
                }
            )

        with out_detail_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "cc_txn_id",
                "txn_date",
                "txn_type",
                "amount",
                "amount_cents",
                "merchant",
                "vendor_key",
                "net_cents",
                "tax_cents",
                "mapping",
                "journal_entry_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(detail_rows)

        with out_skipped_csv.open("w", encoding="utf-8", newline="") as f:
            fieldnames = [
                "cc_txn_id",
                "txn_date",
                "txn_type",
                "amount",
                "merchant",
                "vendor_key",
                "reason",
                "wave_bill_id",
            ]
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(skipped_rows)

        with out_summary_md.open("w", encoding="utf-8") as f:
            f.write("# Credit card purchase journals (shareholder-paid)\n\n")
            f.write(f"- Scope: {start_date} → {end_date}\n")
            f.write(f"- CC txns considered (PURCHASE+REFUND): {len(txns)}\n")
            f.write(f"- Posted: {posted}\n")
            f.write(f"- Skipped (matched to Wave bills): {skipped}\n")
            f.write(f"- Used vendor profile: {used_profile}\n")
            f.write(f"- Used default mapping: {used_default}\n")
            f.write("\nNotes:\n")
            f.write(f"- ITC estimation starts at {itc_start_date} (HST rate {hst_rate}).\n")
            f.write("- Payments on the personal cards are ignored; only purchases/refunds are posted.\n")

        conn.commit()

    finally:
        conn.close()

    print("CC PURCHASE JOURNALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {out_summary_md}")
    print(f"- posted: {posted}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
