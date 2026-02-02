#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

from _lib import DB_PATH, PROJECT_ROOT, connect_db, load_yaml


DEFAULT_OVERRIDES_PATH = PROJECT_ROOT / "overrides" / "gifi_code_overrides.yml"


@dataclass(frozen=True)
class RangeRule:
    start: int
    end: int
    gifi_code: str


def parse_int(s: str) -> int | None:
    s = (s or "").strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def normalize_gifi_code(code: str) -> str:
    code = (code or "").strip()
    if not code:
        return ""
    if not code.isdigit():
        raise ValueError(f"Invalid GIFI code (non-numeric): {code!r}")
    if len(code) != 4:
        raise ValueError(f"Invalid GIFI code (expected 4 digits): {code!r}")
    return code


def load_overrides(path: Path) -> tuple[dict[str, str], list[RangeRule]]:
    data = load_yaml(path)
    block = data.get("gifi_code_overrides")
    if not isinstance(block, dict):
        return ({}, [])

    exact_raw = block.get("exact") if isinstance(block.get("exact"), dict) else {}
    exact: dict[str, str] = {}
    for k, v in exact_raw.items():
        acct = str(k).strip()
        code = normalize_gifi_code(str(v))
        if acct and code:
            exact[acct] = code

    ranges_raw = block.get("ranges") if isinstance(block.get("ranges"), list) else []
    ranges: list[RangeRule] = []
    for r in ranges_raw:
        if not isinstance(r, dict):
            continue
        start = parse_int(str(r.get("start") or ""))
        end = parse_int(str(r.get("end") or ""))
        gifi = normalize_gifi_code(str(r.get("gifi_code") or ""))
        if start is None or end is None or not gifi:
            continue
        if start > end:
            start, end = end, start
        ranges.append(RangeRule(start=start, end=end, gifi_code=gifi))

    ranges.sort(key=lambda rr: (rr.start, rr.end, rr.gifi_code))
    return exact, ranges


def infer_override(account_code: str, *, exact: dict[str, str], ranges: list[RangeRule]) -> str | None:
    account_code = (account_code or "").strip()
    if not account_code:
        return None
    if account_code in exact:
        return exact[account_code]
    n = parse_int(account_code)
    if n is None:
        return None
    for rr in ranges:
        if rr.start <= n <= rr.end:
            return rr.gifi_code
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES_PATH)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    args = ap.parse_args()

    exact, ranges = load_overrides(args.overrides)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = args.out_dir / "gifi_code_overrides_applied.csv"
    out_md = args.out_dir / "gifi_code_overrides_applied.md"

    conn = connect_db(args.db)
    try:
        rows = conn.execute(
            """
            SELECT account_code, account_name, COALESCE(gifi_code, '') AS gifi_code
            FROM chart_of_accounts
            ORDER BY CAST(account_code AS INTEGER), account_code
            """
        ).fetchall()

        changes: list[dict[str, str]] = []
        for r in rows:
            acct = str(r["account_code"] or "").strip()
            old = str(r["gifi_code"] or "").strip()
            new = infer_override(acct, exact=exact, ranges=ranges)
            if not new:
                continue
            if new == old:
                continue
            conn.execute(
                "UPDATE chart_of_accounts SET gifi_code = ? WHERE account_code = ?",
                (new, acct),
            )
            changes.append(
                {
                    "account_code": acct,
                    "account_name": str(r["account_name"] or ""),
                    "old_gifi_code": old,
                    "new_gifi_code": new,
                }
            )

        conn.commit()

    finally:
        conn.close()

    # Report
    changes.sort(key=lambda d: (parse_int(d["account_code"]) or 10**9, d["account_code"]))
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["account_code", "account_name", "old_gifi_code", "new_gifi_code"])
        w.writeheader()
        w.writerows(changes)

    with out_md.open("w", encoding="utf-8") as f:
        f.write("# GIFI code overrides applied\n\n")
        f.write(f"- db: {args.db}\n")
        f.write(f"- overrides: {args.overrides}\n")
        f.write(f"- updated accounts: {len(changes)}\n")
        f.write("\nOutputs:\n\n")
        f.write(f"- {out_csv}\n")

    print("GIFI CODE OVERRIDES APPLIED")
    print(f"- db: {args.db}")
    print(f"- updated accounts: {len(changes)}")
    print(f"- out: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
