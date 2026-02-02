#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, FiscalYear, connect_db, fiscal_years_from_manifest, load_manifest


@dataclass(frozen=True)
class Account:
    account_code: str
    account_name: str
    account_type: str
    gifi_code: str
    t2125_line: str


def cents_to_dollars(cents: int) -> str:
    return f"{cents / 100:.2f}"


def load_accounts(conn) -> dict[str, Account]:
    rows = conn.execute(
        """
        SELECT account_code, account_name, account_type,
               COALESCE(gifi_code, '') AS gifi_code,
               COALESCE(t2125_line, '') AS t2125_line
        FROM chart_of_accounts
        """
    ).fetchall()
    out: dict[str, Account] = {}
    for r in rows:
        out[str(r["account_code"])] = Account(
            account_code=str(r["account_code"]),
            account_name=str(r["account_name"] or ""),
            account_type=str(r["account_type"] or ""),
            gifi_code=str(r["gifi_code"] or ""),
            t2125_line=str(r["t2125_line"] or ""),
        )
    return out


def net_by_account_up_to(conn, *, end_date_inclusive: str) -> dict[str, int]:
    rows = conn.execute(
        """
        SELECT jl.account_code,
               SUM(CAST(jl.debit_cents AS INTEGER)) AS deb,
               SUM(CAST(jl.credit_cents AS INTEGER)) AS cred
        FROM journal_entries je
        JOIN journal_entry_lines jl ON jl.journal_entry_id = je.id
        WHERE je.entry_date <= ?
        GROUP BY jl.account_code
        """,
        (end_date_inclusive,),
    ).fetchall()
    out: dict[str, int] = {}
    for r in rows:
        deb = int(r["deb"] or 0)
        cred = int(r["cred"] or 0)
        out[str(r["account_code"])] = deb - cred
    return out


def net_by_account_before(conn, *, start_date_exclusive: str) -> dict[str, int]:
    rows = conn.execute(
        """
        SELECT jl.account_code,
               SUM(CAST(jl.debit_cents AS INTEGER)) AS deb,
               SUM(CAST(jl.credit_cents AS INTEGER)) AS cred
        FROM journal_entries je
        JOIN journal_entry_lines jl ON jl.journal_entry_id = je.id
        WHERE je.entry_date < ?
        GROUP BY jl.account_code
        """,
        (start_date_exclusive,),
    ).fetchall()
    out: dict[str, int] = {}
    for r in rows:
        deb = int(r["deb"] or 0)
        cred = int(r["cred"] or 0)
        out[str(r["account_code"])] = deb - cred
    return out


def build_tb_for_fy(
    fy: FiscalYear,
    *,
    accounts: dict[str, Account],
    closing_net: dict[str, int],
    opening_net: dict[str, int],
    retained_earnings_code: str = "3100",
) -> list[dict[str, str]]:
    pl_codes = {a.account_code for a in accounts.values() if a.account_type in ("revenue", "expense")}
    prior_pl_net = sum(opening_net.get(code, 0) for code in pl_codes)

    rows: list[dict[str, str]] = []
    all_codes = set(accounts.keys()) | set(closing_net.keys()) | set(opening_net.keys())

    for code in sorted(all_codes, key=lambda x: (int(x) if x.isdigit() else 10**9, x)):
        acct = accounts.get(code)
        if not acct:
            # Shouldn't happen because journal lines enforce FK, but keep safe.
            continue

        close = int(closing_net.get(code, 0))
        open_ = int(opening_net.get(code, 0))

        if code == retained_earnings_code:
            net = close + prior_pl_net
        elif acct.account_type in ("revenue", "expense"):
            net = close - open_
        else:
            net = close

        if net == 0:
            continue

        debit = net if net > 0 else 0
        credit = -net if net < 0 else 0
        rows.append(
            {
                "fy": fy.fy,
                "account_code": acct.account_code,
                "account_name": acct.account_name,
                "account_type": acct.account_type,
                "gifi_code": acct.gifi_code,
                "t2125_line": acct.t2125_line,
                "debit": cents_to_dollars(debit),
                "credit": cents_to_dollars(credit),
                "net_cents": str(net),
            }
        )

    # Validate TB balances to zero.
    total_net = sum(int(r["net_cents"]) for r in rows)
    if total_net != 0:
        raise SystemExit(f"TB out of balance for {fy.fy}: net_cents={total_net}")
    return rows


def build_gifi_totals(tb_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_gifi: dict[str, int] = defaultdict(int)
    for r in tb_rows:
        gifi = (r.get("gifi_code") or "").strip()
        if not gifi:
            continue
        by_gifi[gifi] += int(r["net_cents"])

    out: list[dict[str, str]] = []
    for gifi_code in sorted(by_gifi.keys(), key=lambda x: (int(x) if x.isdigit() else 10**9, x)):
        net = int(by_gifi[gifi_code])
        if net == 0:
            continue
        out.append(
            {
                "gifi_code": gifi_code,
                "net_cents": str(net),
                "balance": "DR" if net > 0 else "CR",
                "amount": cents_to_dollars(abs(net)),
            }
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--retained-earnings-code", default="3100")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    if not fys:
        raise SystemExit("No fiscal_years found in manifest/sources.yml")

    args.out_dir.mkdir(parents=True, exist_ok=True)

    conn = connect_db(args.db)
    try:
        accounts = load_accounts(conn)

        for fy in fys:
            closing_net = net_by_account_up_to(conn, end_date_inclusive=fy.end_date)
            opening_net = net_by_account_before(conn, start_date_exclusive=fy.start_date)

            tb_rows = build_tb_for_fy(
                fy,
                accounts=accounts,
                closing_net=closing_net,
                opening_net=opening_net,
                retained_earnings_code=args.retained_earnings_code,
            )

            tb_path = args.out_dir / f"trial_balance_{fy.fy}.csv"
            with tb_path.open("w", encoding="utf-8", newline="") as f:
                fieldnames = [
                    "fy",
                    "account_code",
                    "account_name",
                    "account_type",
                    "gifi_code",
                    "t2125_line",
                    "debit",
                    "credit",
                    "net_cents",
                ]
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(tb_rows)

            gifi_rows = build_gifi_totals(tb_rows)
            gifi_path = args.out_dir / f"gifi_totals_{fy.fy}.csv"
            with gifi_path.open("w", encoding="utf-8", newline="") as f:
                fieldnames = ["gifi_code", "balance", "amount", "net_cents"]
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(gifi_rows)

        conn.commit()

    finally:
        conn.close()

    print("TRIAL BALANCE + GIFI TOTALS BUILT")
    print(f"- db: {args.db}")
    print(f"- out: {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

