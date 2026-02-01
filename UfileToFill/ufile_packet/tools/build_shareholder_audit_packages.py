#!/usr/bin/env python3
"""
Build FY-scoped shareholder audit packages (working papers) from the current packet snapshot.

Goal:
- Produce a defensible, reproducible evidence bundle for:
  - dividends
  - due-to / due-from shareholder balances + loan events
  - mileage/fuel reimbursement computations
  - payroll-related transactions involving shareholders (e.g., payroll reimbursements paid by Thomas)

Constraints:
- Read-only relative to the accounting DB.
- Prefer the snapshot directory referenced by UfileToFill/ufile_packet/packet.json meta.snapshot_source
  so outputs do not drift from the fill packet evidence.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from render_year_guide_html import render_year_guide_html


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"
OUT_ROOT = PROJECT_ROOT / "audit_packages"

THOMAS_NAME = "Thomas McCrossin"


def round_to_dollar(amount: Decimal) -> int:
    return int(amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def round_cents_to_dollar(cents: int) -> int:
    return round_to_dollar(Decimal(int(cents)) / Decimal(100))


def dollars(cents: int) -> str:
    return f"${cents/100:,.2f}"


def money_int(n: int) -> str:
    return f"{n:,}"


def parse_ymd(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")


def in_period(date_ymd: str, start_ymd: str, end_ymd: str) -> bool:
    if not date_ymd:
        return False
    try:
        d = parse_ymd(date_ymd).date()
        start = parse_ymd(start_ymd).date()
        end = parse_ymd(end_ymd).date()
    except Exception:
        return False
    return start <= d <= end


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, headers: list[str], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in rows:
            w.writerow(list(r))


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "_(none)_"
    out: list[str] = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


@dataclass(frozen=True)
class FyContext:
    fy: str
    start: str
    end: str


def resolve_snapshot_dir(packet: dict) -> Path:
    snap = str(packet.get("meta", {}).get("snapshot_source") or "").strip()
    if not snap:
        raise SystemExit("packet.json missing meta.snapshot_source")
    p = PROJECT_ROOT / snap
    if not p.exists():
        raise SystemExit(f"Snapshot directory not found: {p}")
    return p


def read_snapshot_or_output(snapshot_dir: Path, filename: str) -> list[dict[str, str]]:
    # Prefer snapshot evidence, fall back to current output/ for robustness during dev.
    p = snapshot_dir / filename
    if p.exists():
        return read_csv_rows(p)
    return read_csv_rows(PROJECT_ROOT / "output" / filename)


def main() -> int:
    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    snapshot_dir = resolve_snapshot_dir(packet)
    snapshot_source = str(packet.get("meta", {}).get("snapshot_source") or "").strip().rstrip("/") + "/"
    packet_generated_at = str(packet.get("meta", {}).get("generated_at") or "").strip()

    years = packet.get("years", {})
    if not isinstance(years, dict) or not years:
        raise SystemExit("packet.json missing years")

    # Only build for FY2024/FY2025 by default (matches current project), but keep generic.
    fy_keys = sorted(years.keys())
    first_fy = fy_keys[0] if fy_keys else ""
    for fy in fy_keys:
        year = years[fy]
        period = year.get("fiscal_period", {})
        ctx = FyContext(fy=fy, start=str(period.get("start") or ""), end=str(period.get("end") or ""))
        if not ctx.start or not ctx.end:
            raise SystemExit(f"packet.json missing fiscal_period for {fy}")

        # If this is the first filing year after incorporation/operations begin, UFile/CRA period starts
        # at the operations start date (e.g., 2023-06-10), even if our internal FY rolls from month start.
        filing_start = ctx.start
        ident = year.get("ufile_screens", {}).get("identification_of_corporation", {})
        ops_start = ""
        if isinstance(ident, dict):
            ops_start = str(ident.get("operations_start_date") or "").strip()
        if fy == first_fy and ops_start:
            try:
                if parse_ymd(ops_start) > parse_ymd(filing_start):
                    filing_start = ops_start
            except Exception:
                pass

        out_dir = OUT_ROOT / fy
        out_dir.mkdir(parents=True, exist_ok=True)

        # Load evidence
        tb_rows = read_snapshot_or_output(snapshot_dir, f"trial_balance_{fy}.csv")
        retained_rows = read_snapshot_or_output(snapshot_dir, f"gifi_retained_earnings_{fy}.csv")
        due_from_rows = read_snapshot_or_output(snapshot_dir, "due_from_shareholder_breakdown.csv")
        mileage_rows = read_snapshot_or_output(snapshot_dir, f"shareholder_mileage_fuel_payables_{fy}.csv")
        mileage_adj_rows = read_snapshot_or_output(snapshot_dir, "mileage_adjustment_audit.csv")
        bank_debit_rows = read_snapshot_or_output(snapshot_dir, "bank_debit_journal_detail.csv")
        payroll_cra_match_rows = read_snapshot_or_output(snapshot_dir, "payroll_cra_account_matches.csv")

        # --- Dividends support ---
        dividends_cents = 0
        for r in tb_rows:
            if (r.get("fy") or "").strip() != fy:
                continue
            if (r.get("account_code") or "").strip() != "3400":
                continue
            try:
                dividends_cents += int(r.get("net_cents") or 0)
            except Exception:
                pass
        dividends_dollars = round_cents_to_dollar(dividends_cents)

        re_3700 = 0
        for r in retained_rows:
            code = (r.get("GIFI_Code") or r.get("gifi_code") or "").strip()
            if code != "3700":
                continue
            try:
                re_3700 = int(r.get("Amount") or r.get("amount") or 0)
            except Exception:
                re_3700 = 0
            break

        div_rows: list[list[object]] = []
        div_rows.append([fy, ctx.end, "trial_balance_3400_net_cents", dividends_cents, dollars(dividends_cents)])
        div_rows.append([fy, ctx.end, "rounded_to_dollars", dividends_dollars, money_int(dividends_dollars)])
        div_rows.append([fy, ctx.end, "retained_earnings_3700_dollars", re_3700, money_int(re_3700)])
        write_csv(
            out_dir / "dividends_support.csv",
            ["fy", "as_of", "metric", "value", "display"],
            div_rows,
        )

        # --- Shareholder continuity ---
        # Year-end balances by account (TB)
        tb_by_acct: dict[str, dict[str, object]] = {}
        for r in tb_rows:
            if (r.get("fy") or "").strip() != fy:
                continue
            acct = (r.get("account_code") or "").strip()
            if acct not in ("2400", "2410", "2500"):
                continue
            try:
                cents = int(r.get("net_cents") or 0)
            except Exception:
                cents = 0
            tb_by_acct[acct] = {
                "name": (r.get("account_name") or "").strip(),
                "net_cents": cents,
            }

        cont_rows: list[list[object]] = []
        # Loan events from due_from_shareholder_breakdown (FY-scoped)
        for r in due_from_rows:
            entry_date = (r.get("entry_date") or "").strip()
            if not in_period(entry_date, filing_start, ctx.end):
                continue
            category = (r.get("bank_txn_category") or "").strip()
            if category not in ("LOAN_ISSUED", "LOAN_REPAID"):
                continue
            shareholder = (r.get("shareholder") or "").strip()
            net = (r.get("net") or "").strip()
            try:
                amt = Decimal(net) if net else Decimal("0")
            except Exception:
                amt = Decimal("0")
            cont_rows.append(
                [
                    fy,
                    entry_date,
                    shareholder,
                    category,
                    f"{amt:.2f}",
                    (r.get("journal_entry_id") or "").strip(),
                    (r.get("description") or "").strip(),
                    "due_from_shareholder_breakdown.csv",
                ]
            )

        # Mileage/fuel totals from shareholder_mileage_fuel_payables
        for r in mileage_rows:
            if (r.get("fy") or "").strip() != fy:
                continue
            shareholder = (r.get("shareholder") or "").strip()
            try:
                net_cents = int(r.get("net_cents") or 0)
            except Exception:
                net_cents = 0
            cont_rows.append(
                [
                    fy,
                    ctx.end,
                    shareholder,
                    "MILEAGE_FUEL_NET",
                    f"{Decimal(net_cents) / Decimal(100):.2f}",
                    f"MILEAGE_FUEL_REIMBURSEMENT_{fy}",
                    "Net mileage/fuel reimbursement position for the fiscal year",
                    f"shareholder_mileage_fuel_payables_{fy}.csv",
                ]
            )

        # Year-end balances (explicit)
        for acct in ("2400", "2410", "2500"):
            obj = tb_by_acct.get(acct)
            if not obj:
                continue
            cents = int(obj.get("net_cents") or 0)
            cont_rows.append(
                [
                    fy,
                    ctx.end,
                    "Thomas" if acct == "2400" else "Dwayne" if acct == "2410" else "Shareholder",
                    "YEAR_END_BALANCE",
                    f"{Decimal(cents) / Decimal(100):.2f}",
                    f"trial_balance_{fy}.csv",
                    f"{acct} {(obj.get('name') or '')}".strip(),
                    f"trial_balance_{fy}.csv",
                ]
            )

        write_csv(
            out_dir / "shareholder_continuity.csv",
            ["fy", "date", "shareholder", "category", "amount", "journal_entry_id", "description", "evidence_file"],
            cont_rows,
        )

        # --- Mileage/fuel support ---
        mf_rows: list[list[object]] = []
        for r in mileage_rows:
            if (r.get("fy") or "").strip() != fy:
                continue
            shareholder = (r.get("shareholder") or "").strip()
            mf_rows.append(
                [
                    fy,
                    shareholder,
                    (r.get("trips") or "").strip(),
                    (r.get("kilometres") or "").strip(),
                    int(r.get("mileage_claim_cents") or 0),
                    dollars(int(r.get("mileage_claim_cents") or 0)),
                    int(r.get("fuel_cents") or 0),
                    dollars(int(r.get("fuel_cents") or 0)),
                    int(r.get("net_cents") or 0),
                    dollars(int(r.get("net_cents") or 0)),
                    (r.get("direction") or "").strip(),
                ]
            )

        # FY-scoped overlay signals from mileage_adjustment_audit.csv (keep it explicit for audit)
        # We don't recompute mileage; we document overlays that affect the payable.
        overlays = []
        for r in mileage_adj_rows:
            row_fy = (r.get("fy") or r.get("fiscal_year") or "").strip()
            if row_fy != fy:
                continue
            who = (r.get("shareholder") or "").strip()
            if not who:
                continue
            fuel_adj = (r.get("fuel_adjustment_cents") or "").strip()
            if not fuel_adj:
                continue
            # Only include true overlays (non-zero), otherwise it just clutters the working paper.
            try:
                if int(Decimal(fuel_adj)) == 0:
                    continue
            except Exception:
                pass
            overlays.append((who, fuel_adj, (r.get("notes") or "").strip()))

        write_csv(
            out_dir / "mileage_fuel_support.csv",
            [
                "fy",
                "shareholder",
                "trips",
                "kilometres",
                "mileage_claim_cents",
                "mileage_claim",
                "fuel_cents",
                "fuel",
                "net_cents",
                "net",
                "direction",
            ],
            mf_rows,
        )

        # --- Payroll-related transactions involving Thomas (defensive) ---
        payroll_rows: list[list[object]] = []
        # Bank debit journal: capture rows whose memo/description includes Thomas and looks payroll-related.
        for r in bank_debit_rows:
            date = (r.get("bank_date") or r.get("date") or "").strip()
            if not in_period(date, filing_start, ctx.end):
                continue
            desc = (r.get("debit_reason") or r.get("description") or "").strip()
            if THOMAS_NAME.lower() not in (desc or "").lower():
                continue
            category = (r.get("category") or "").strip()
            evidence_cat = (r.get("evidence_category") or r.get("subcategory") or "").strip()
            # We only want payroll funding / reimbursements involving Thomas, not random name matches.
            if "payroll" not in (category + " " + evidence_cat + " " + desc).lower():
                continue
            try:
                cents = int(Decimal(str(r.get("amount_cents") or "0")))
            except Exception:
                # Some files store dollars; fall back to amount if present.
                try:
                    cents = int(round(Decimal(str(r.get("amount") or "0")) * 100))
                except Exception:
                    cents = 0
            payroll_rows.append(
                [
                    fy,
                    date,
                    "bank_debit_journal_detail.csv",
                    (r.get("journal_entry_id") or "").strip(),
                    category,
                    evidence_cat,
                    cents,
                    dollars(cents),
                    desc,
                ]
            )

        # CRA payroll account matches: these are typically reimbursements paid by Thomas to cover payroll.
        for r in payroll_cra_match_rows:
            txn_date = (r.get("date_received") or r.get("date_posted") or r.get("txn_date") or r.get("date") or "").strip()
            if not in_period(txn_date, filing_start, ctx.end):
                continue
            memo = (r.get("bank_group_txn_description") or r.get("bank_txn_description") or r.get("bank_memo") or "").strip()
            if THOMAS_NAME.lower() not in (memo or "").lower():
                continue
            try:
                cents = int(r.get("amount_cents") or 0)
            except Exception:
                cents = 0
            payroll_rows.append(
                [
                    fy,
                    txn_date,
                    "payroll_cra_account_matches.csv",
                    (r.get("journal_entry_id") or "").strip(),
                    (r.get("bank_group_txn_category") or r.get("bank_txn_category") or r.get("category") or "").strip(),
                    (r.get("transaction_label") or r.get("transaction_type") or "").strip(),
                    cents,
                    dollars(cents),
                    memo,
                ]
            )

        payroll_rows.sort(key=lambda x: (x[1], x[2], x[3]))

        if payroll_rows:
            none_path = out_dir / "payroll_thomas_none_found.md"
            if none_path.exists():
                none_path.unlink()
            write_csv(
                out_dir / "payroll_thomas_support.csv",
                [
                    "fy",
                    "date",
                    "source_file",
                    "journal_entry_id",
                    "category",
                    "subcategory",
                    "amount_cents",
                    "amount",
                    "description",
                ],
                payroll_rows,
            )
        else:
            csv_path = out_dir / "payroll_thomas_support.csv"
            if csv_path.exists():
                csv_path.unlink()
            (out_dir / "payroll_thomas_none_found.md").write_text(
                "\n".join(
                    [
                        f"# Payroll-related transactions involving {THOMAS_NAME} — {fy}",
                        "",
                        "No payroll-related transactions involving Thomas were found in the snapshot evidence searched.",
                        "",
                        "Files searched (snapshot-scoped):",
                        f"- `{snapshot_dir / 'bank_debit_journal_detail.csv'}`",
                        f"- `{snapshot_dir / 'payroll_cra_account_matches.csv'}`",
                        "",
                        f"Name searched: `{THOMAS_NAME}` (case-insensitive).",
                        "",
                    ]
                ).strip()
                + "\n",
                encoding="utf-8",
            )

        # --- Build index.md ---
        legal = str(packet.get("entity", {}).get("legal_name") or "").strip()
        op = str(packet.get("entity", {}).get("operating_name") or "").strip()
        bn = str(packet.get("entity", {}).get("bn") or "").strip()

        year_packet = packet.get("years", {}).get(fy, {})
        sch100 = year_packet.get("schedule_100", {})
        sch100_due_from = int(sch100.get("1301", {}).get("amount") or 0)
        sch100_due_to = int(sch100.get("2781", {}).get("amount") or 0)

        # Basic section summaries
        title = f"Shareholder audit package — {fy}"
        header_lines = [
            f"# {title}",
            "",
            f"Entity: **{legal}{' (' + op + ')' if op else ''}**",
            f"BN: **{bn}**" if bn else "",
            f"Period: **{filing_start} to {ctx.end}**",
            f"Snapshot source: `{snapshot_source}`",
            f"Packet generated at: `{packet_generated_at}`" if packet_generated_at else "",
            "",
            "This folder is **working-paper support**. It is not necessarily entered into UFile unless a screen explicitly asks.",
            "",
        ]
        header_lines = [x for x in header_lines if x != "" or True]

        summary_rows = [
            ["Schedule 100 due from shareholder (GIFI 1301)", money_int(sch100_due_from)],
            ["Schedule 100 due to shareholders (GIFI 2781)", money_int(sch100_due_to)],
            ["Dividends declared (retained earnings rollforward 3700)", money_int(re_3700)],
        ]
        if dividends_dollars != re_3700:
            summary_rows.append(["Dividend tie-out warning", f"TB 3400 rounds to {money_int(dividends_dollars)} but RE 3700 is {money_int(re_3700)}"])

        idx: list[str] = []
        idx.extend([x for x in header_lines if x])
        idx.append("## Year-end highlights")
        idx.append(md_table(["Item", "Amount (dollars)"], summary_rows))
        idx.append("")

        idx.append("## Dividends")
        idx.append(
            "\n".join(
                [
                    "Tie-out:",
                    "- Trial balance: account `3400` (dividends declared)",
                    "- Retained earnings rollforward: `GIFI 3700`",
                    "- UFile screens:",
                    "  - Retained earnings rollforward: enter `3700`",
                    "  - Dividends paid: enter taxable dividends paid (eligible = 0 unless you have eligible dividends)",
                    "",
                    "Evidence:",
                    "- `dividends_support.csv`",
                ]
            )
        )
        idx.append("")

        idx.append("## Loans / due-to / due-from (shareholder continuity)")
        idx.append(
            "\n".join(
                [
                    "This captures dated loan events (if any), the FY mileage/fuel net position, and year-end balances.",
                    "",
                    "Evidence:",
                    "- `shareholder_continuity.csv`",
                    "",
                    "Year-end TB balances (for reference):",
                    md_table(
                        ["Account", "Name", "Net"],
                        [
                            [acct, str(tb_by_acct[acct].get("name") or ""), dollars(int(tb_by_acct[acct].get("net_cents") or 0))]
                            for acct in ("2400", "2410", "2500")
                            if acct in tb_by_acct
                        ],
                    ),
                ]
            )
        )
        idx.append("")

        idx.append("## Mileage / fuel reimbursement support")
        idx.append("Evidence:")
        idx.append("- `mileage_fuel_support.csv`")
        if overlays:
            idx.append("")
            idx.append("FY-scoped overlays applied (defensive disclosure for working papers only):")
            idx.append("")
            idx.append(md_table(["Shareholder", "Fuel adjustment (cents)", "Notes"], [[a, b, c] for a, b, c in overlays]))
        idx.append("")

        idx.append(f"## Payroll-related transactions involving {THOMAS_NAME} (defensive)")
        if payroll_rows:
            idx.append("Evidence:")
            idx.append("- `payroll_thomas_support.csv`")
            idx.append("")
            idx.append(
                "Note: These are payroll-related reimbursements / funding transactions involving Thomas "
                "(e.g., payroll remittance payments/reimbursements). This does **not** necessarily mean wages were paid to Thomas as an employee."
            )
        else:
            idx.append("Evidence:")
            idx.append("- `payroll_thomas_none_found.md`")
        idx.append("")

        index_md = "\n".join(idx).strip() + "\n"
        (out_dir / "index.md").write_text(index_md, encoding="utf-8")
        (out_dir / "index.html").write_text(render_year_guide_html(packet, fy, md_guide=index_md), encoding="utf-8")

    print("SHAREHOLDER AUDIT PACKAGES BUILT")
    print(f"- out_dir: {OUT_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
