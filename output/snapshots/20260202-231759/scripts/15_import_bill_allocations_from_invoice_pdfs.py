#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

import pdfplumber

from _lib import (
    DB_PATH,
    PROJECT_ROOT,
    connect_db,
    fiscal_years_from_manifest,
    load_manifest,
    load_yaml,
    sha256_file,
)


METHOD_CATEGORY = "INVOICE_PDF_CATEGORY"
METHOD_TAX_ITC = "INVOICE_PDF_TAX_ITC"
METHOD_CC_FEE = "INVOICE_PDF_CC_FEE"
METHOD_ADJUST = "INVOICE_PDF_ADJUSTMENT"
METHOD_FALLBACK = "INVOICE_RULE_FALLBACK"


DEFAULT_GFS_PDF_DIR = Path("/home/clarencehub/Fresh/dump/gfs_flat")
DEFAULT_CAPITAL_PDF_DIR = Path("/home/clarencehub/Fresh/dump/capitalinvoices")
DEFAULT_MAPPING_PATH = PROJECT_ROOT / "overrides" / "invoice_pdf_mappings.yml"


class ParseError(RuntimeError):
    pass


@dataclass(frozen=True)
class InvoiceCategoryLine:
    category_key: str
    label: str
    subtotal_cents: int


@dataclass(frozen=True)
class ParsedInvoice:
    vendor_key: str
    invoice_number: str
    subtotal_cents: int
    tax_cents: int
    total_cents: int
    lines: list[InvoiceCategoryLine]
    pdf_path: Path | None
    pdf_sha256: str | None


@dataclass(frozen=True)
class WaveBill:
    id: int
    invoice_date: str
    vendor_norm: str
    vendor_raw: str
    invoice_number: str | None
    total_cents: int
    tax_cents: int
    net_cents: int


def dollars_to_cents(s: str) -> int:
    from _lib import dollars_to_cents as _d2c

    return _d2c(s)


def normalize_ws(s: str) -> str:
    return " ".join(str(s).split())


def load_mapping(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing invoice mapping file: {path}")
    data = load_yaml(path)
    if not isinstance(data.get("vendors"), dict):
        raise ValueError(f"Invalid mapping YAML: {path} (missing vendors mapping)")
    return data


def vendor_key_for_bill(vendor_norm: str) -> str | None:
    v = (vendor_norm or "").strip().lower()
    if v.startswith("gfs bill"):
        return "GFS"
    if v.startswith("capital foods bill"):
        return "CAPITAL"
    if v.startswith("black cat importers"):
        return "BLACK_CAT"
    if v.startswith("webstaurant store"):
        return "WEBSTAURANT"
    return None


def find_pdf_for_invoice(invoice_number: str, *, vendor_key: str, gfs_dir: Path, capital_dir: Path) -> Path | None:
    if vendor_key == "GFS":
        hits = sorted(gfs_dir.glob(f"*{invoice_number}*.pdf"))
        return hits[0] if hits else None
    if vendor_key == "CAPITAL":
        hits = sorted(capital_dir.glob(f"*{invoice_number}*.pdf"))
        return hits[0] if hits else None
    return None


def extract_pdf_text(pdf_path: Path) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        parts: list[str] = []
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                parts.append(t)
    return "\n".join(parts)


_MONEY_RE = re.compile(r"\d+\.\d{2}")


def _cents_close(a: int, b: int, tol_cents: int = 2) -> bool:
    return abs(int(a) - int(b)) <= tol_cents


def parse_gfs_summary_amounts(line: str) -> tuple[int, int, int]:
    """
    Parse the rightmost monetary columns from a GFS Group Summary line.

    Variants observed:
    - GST/HST present:  Subtotal  PST/QST Subtotal  GST/HST  Total    (4 amounts)
    - GST/HST omitted:  Subtotal  PST/QST Subtotal  Total              (3 amounts; all equal)
    - Deposit lines:    Amount    Total                              (2 amounts; equal)
    """
    amounts = _MONEY_RE.findall(line)
    if len(amounts) >= 4:
        a, b, c, d = (dollars_to_cents(x) for x in amounts[-4:])
        if _cents_close(a, b) and _cents_close(b + c, d):
            return a, c, d
    if len(amounts) >= 3:
        a, b, c = (dollars_to_cents(x) for x in amounts[-3:])
        if _cents_close(a, b) and _cents_close(b, c):
            return a, 0, c
    if len(amounts) >= 2:
        a, b = (dollars_to_cents(x) for x in amounts[-2:])
        if _cents_close(a, b):
            return a, 0, b
    raise ParseError(f"GFS: could not parse summary amounts from line: {line!r}")


def parse_gfs_invoice(pdf_path: Path, *, invoice_number: str) -> ParsedInvoice:
    pdf_sha = sha256_file(pdf_path)
    text = extract_pdf_text(pdf_path)
    lines = [normalize_ws(l) for l in text.splitlines() if str(l).strip()]

    # Locate "Group Summary" block.
    group_idx = next((i for i, l in enumerate(lines) if l.lower() == "group summary"), None)
    if group_idx is None:
        group_idx = next((i for i, l in enumerate(lines) if "group summary" in l.lower()), None)
    if group_idx is None:
        raise ParseError("GFS: missing 'Group Summary' section")

    header_idx = next((i for i in range(group_idx, len(lines)) if "category recap" in lines[i].lower()), None)
    if header_idx is None:
        raise ParseError("GFS: missing 'CATEGORY RECAP' header in Group Summary")

    parsed_lines: list[InvoiceCategoryLine] = []
    total_line: str | None = None

    # Parse group lines until "Total".
    for l in lines[header_idx + 1 :]:
        if re.match(r"^total\s+\d", l, flags=re.IGNORECASE):
            total_line = l
            break

        key: str | None = None
        label: str | None = None
        m = re.match(r"^(?P<code>[A-Z]{2})\s+(?P<label>[A-Za-z][A-Za-z ]+?)\s", l)
        if m:
            key = m.group("code").strip()
            label = m.group("label").strip()
        elif l.lower().startswith("fuel charge"):
            key = "FUEL_CHARGE"
            label = "Fuel Charge"
        elif "deposit" in l.lower():
            key = "DEPOSIT"
            label = "Deposit"
        else:
            continue

        subtotal_cents, _, _ = parse_gfs_summary_amounts(l)
        parsed_lines.append(InvoiceCategoryLine(category_key=key, label=label, subtotal_cents=subtotal_cents))

    if not total_line:
        raise ParseError("GFS: missing 'Total' line in Group Summary")

    total_amounts = _MONEY_RE.findall(total_line)
    subtotal_cents: int | None = None
    tax_cents: int | None = None
    total_cents: int | None = None
    if len(total_amounts) >= 3:
        maybe_sub = dollars_to_cents(total_amounts[-3])
        maybe_tax = dollars_to_cents(total_amounts[-2])
        maybe_total = dollars_to_cents(total_amounts[-1])
        if _cents_close(maybe_sub + maybe_tax, maybe_total):
            subtotal_cents, tax_cents, total_cents = maybe_sub, maybe_tax, maybe_total
    if subtotal_cents is None and len(total_amounts) >= 2:
        maybe_sub = dollars_to_cents(total_amounts[-2])
        maybe_total = dollars_to_cents(total_amounts[-1])
        if _cents_close(maybe_sub, maybe_total):
            subtotal_cents, tax_cents, total_cents = maybe_sub, 0, maybe_total
    if subtotal_cents is None or tax_cents is None or total_cents is None:
        raise ParseError(f"GFS: could not parse totals from line: {total_line!r}")

    # Sanity checks (do not fail hard; keep deterministic but allow tiny anomalies).
    sum_sub = sum(l.subtotal_cents for l in parsed_lines)
    if abs(sum_sub - subtotal_cents) > 2:
        raise ParseError(
            f"GFS: category subtotals ({sum_sub}) do not match parsed subtotal ({subtotal_cents})"
        )
    if abs((subtotal_cents + tax_cents) - total_cents) > 2:
        raise ParseError("GFS: subtotal+tax does not equal total")

    return ParsedInvoice(
        vendor_key="GFS",
        invoice_number=invoice_number,
        subtotal_cents=subtotal_cents,
        tax_cents=tax_cents,
        total_cents=total_cents,
        lines=parsed_lines,
        pdf_path=pdf_path,
        pdf_sha256=pdf_sha,
    )


def parse_capital_invoice(pdf_path: Path, *, invoice_number: str) -> ParsedInvoice:
    pdf_sha = sha256_file(pdf_path)
    text = extract_pdf_text(pdf_path)
    lines = [normalize_ws(l) for l in text.splitlines() if str(l).strip()]

    subtotal_cents: int | None = None
    tax_cents: int | None = None
    total_cents: int | None = None

    for l in lines:
        m = re.search(r"\bSUB\s+(\d+\.\d{2})\b", l, flags=re.IGNORECASE)
        if m:
            subtotal_cents = dollars_to_cents(m.group(1))
        m = re.search(r"\bTAX\s+(\d+\.\d{2})\b", l, flags=re.IGNORECASE)
        if m:
            tax_cents = dollars_to_cents(m.group(1))
        m = re.search(r"\bTOTAL\s+(\d+\.\d{2})\b", l, flags=re.IGNORECASE)
        if m and "invoice no" not in l.lower():
            total_cents = dollars_to_cents(m.group(1))

    cat_pat = re.compile(r"^\s*(\d{3,4})\s+([A-Z&/ ]{3,})\s+(\d+\.\d{2})\s*$")
    cat_amounts: dict[tuple[str, str], int] = {}
    for l in lines:
        m = cat_pat.match(l)
        if not m:
            continue
        code = m.group(1).strip()
        label = normalize_ws(m.group(2))
        amt = dollars_to_cents(m.group(3))
        cat_amounts[(code, label)] = cat_amounts.get((code, label), 0) + amt

    surcharge_specs = [
        ("FUEL_SURCHARGE", "Fuel Surcharge", r"FUEL SURCHARGE\s+(\d+\.\d{2})"),
        ("ROAD_CARBON_SURCHARGE", "Road Carbon Surcharge", r"ROAD CARBON SURCHARGE[ A-Z]*\s+(\d+\.\d{2})"),
        ("BOTDEP", "Bottle Deposit", r"\bBOTDEP\s+(\d+\.\d{2})"),
        ("OTHER_CHG", "Other Charge", r"\bOTHER CHG-?\s+(\d+\.\d{2})"),
    ]
    surcharge_amounts: dict[tuple[str, str], int] = {}
    for key, label, pat in surcharge_specs:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            amt = dollars_to_cents(m.group(1))
            surcharge_amounts[(key, label)] = surcharge_amounts.get((key, label), 0) + amt

    parsed_lines: list[InvoiceCategoryLine] = []
    for (code, label), amt in sorted(cat_amounts.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        parsed_lines.append(InvoiceCategoryLine(category_key=code, label=label, subtotal_cents=amt))
    for (key, label), amt in sorted(surcharge_amounts.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        parsed_lines.append(InvoiceCategoryLine(category_key=key, label=label, subtotal_cents=amt))

    inferred_sub = sum(l.subtotal_cents for l in parsed_lines)
    if subtotal_cents is None:
        subtotal_cents = inferred_sub
    if tax_cents is None and total_cents is not None:
        tax_cents = total_cents - subtotal_cents
    if total_cents is None and tax_cents is not None:
        total_cents = subtotal_cents + tax_cents

    if subtotal_cents is None or tax_cents is None or total_cents is None:
        raise ParseError("CAPITAL: could not parse SUB/TAX/TOTAL")

    if abs((subtotal_cents + tax_cents) - total_cents) > 2:
        raise ParseError("CAPITAL: subtotal+tax does not equal total")

    # The category/surcharge sum should equal SUB (allow small text-extraction drift).
    if abs(inferred_sub - subtotal_cents) > 2:
        # Keep deterministic: treat remainder as an unmapped charge in the parsed subtotal.
        diff = subtotal_cents - inferred_sub
        parsed_lines.append(InvoiceCategoryLine(category_key="UNMAPPED_SUBTOTAL", label="Unmapped subtotal", subtotal_cents=diff))

    return ParsedInvoice(
        vendor_key="CAPITAL",
        invoice_number=invoice_number,
        subtotal_cents=subtotal_cents,
        tax_cents=tax_cents,
        total_cents=total_cents,
        lines=parsed_lines,
        pdf_path=pdf_path,
        pdf_sha256=pdf_sha,
    )


def load_wave_bills_missing_allocations(conn, *, start_date: str, end_date: str) -> list[WaveBill]:
    rows = conn.execute(
        """
        SELECT wb.id, wb.invoice_date, wb.vendor_norm, wb.vendor_raw, wb.invoice_number,
               wb.total_cents, wb.tax_cents, wb.net_cents
        FROM wave_bills wb
        LEFT JOIN bill_allocations ba ON ba.wave_bill_id=wb.id
        WHERE wb.invoice_date >= ? AND wb.invoice_date <= ?
          AND ba.id IS NULL
        ORDER BY wb.invoice_date, wb.id
        """,
        (start_date, end_date),
    ).fetchall()
    return [
        WaveBill(
            id=int(r["id"]),
            invoice_date=str(r["invoice_date"]),
            vendor_norm=str(r["vendor_norm"]),
            vendor_raw=str(r["vendor_raw"]),
            invoice_number=(str(r["invoice_number"]).strip() if r["invoice_number"] else None),
            total_cents=int(r["total_cents"]),
            tax_cents=int(r["tax_cents"] or 0),
            net_cents=int(r["net_cents"] or 0),
        )
        for r in rows
    ]


def bill_has_any_allocations(conn, wave_bill_id: int) -> bool:
    row = conn.execute("SELECT 1 FROM bill_allocations WHERE wave_bill_id=? LIMIT 1", (wave_bill_id,)).fetchone()
    return bool(row)


def account_for_vendor_line(mapping: dict, *, vendor_key: str, category_key: str, label: str) -> str:
    vendor_cfg = mapping.get("vendors", {}).get(vendor_key, {})
    if vendor_cfg and isinstance(vendor_cfg.get("category_code_to_account_code"), dict):
        m = vendor_cfg["category_code_to_account_code"]
        if category_key in m:
            return str(m[category_key]).strip()

    # Minimal heuristics for common labels.
    label_l = label.lower()
    if "pack" in label_l or "dispos" in label_l or "paper" in label_l:
        return "5200"
    if "clean" in label_l:
        return "5204"
    if "bever" in label_l or "soda" in label_l or "pop" in label_l or "juice" in label_l:
        return "5010"
    if "fuel" in label_l or "carbon" in label_l or "surcharge" in label_l:
        return "5100"

    default_code = vendor_cfg.get("default_account_code") if isinstance(vendor_cfg, dict) else None
    return str(default_code or "5000").strip()


def is_capital_cc_fee(*, wave_total_cents: int, invoice_total_cents: int) -> bool:
    diff = wave_total_cents - invoice_total_cents
    if diff <= 0:
        return False
    # Detect ~3% era; allow loose tolerance because invoice totals vary.
    # (diff / invoice_total) in [2.7%, 3.3%]
    ratio = diff / max(invoice_total_cents, 1)
    return 0.027 <= ratio <= 0.033


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING_PATH)
    ap.add_argument("--gfs-pdf-dir", type=Path, default=DEFAULT_GFS_PDF_DIR)
    ap.add_argument("--capital-pdf-dir", type=Path, default=DEFAULT_CAPITAL_PDF_DIR)
    ap.add_argument("--start-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY min start).")
    ap.add_argument("--end-date", default=None, help="Inclusive YYYY-MM-DD (default: manifest FY max end).")
    ap.add_argument("--reset", action="store_true", help="Delete allocations created by this importer before import.")
    ap.add_argument("--skip-existing", action=argparse.BooleanOptionalAction, default=True)
    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    manifest = load_manifest()
    fys = fiscal_years_from_manifest(manifest)
    default_start = min((fy.start_date for fy in fys), default="2023-06-01")
    default_end = max((fy.end_date for fy in fys), default="2025-05-31")

    start_date = str(args.start_date or default_start)
    end_date = str(args.end_date or default_end)

    mapping = load_mapping(args.mapping)
    tax_cfg = mapping.get("tax") if isinstance(mapping.get("tax"), dict) else {}
    hst_itc = str((tax_cfg or {}).get("hst_itc_account_code") or "2210").strip()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    out_summary = args.out_dir / "invoice_pdf_allocations_import_summary.md"
    out_skipped = args.out_dir / "invoice_pdf_allocations_import_skipped.csv"

    conn = connect_db(args.db)
    skipped_rows: list[dict[str, str]] = []

    considered = 0
    imported = 0
    rows_inserted = 0

    try:
        bills = load_wave_bills_missing_allocations(conn, start_date=start_date, end_date=end_date)
        considered = len(bills)

        conn.execute("BEGIN")

        for bill in bills:
            vkey = vendor_key_for_bill(bill.vendor_norm)
            if vkey is None:
                skipped_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor_norm": bill.vendor_norm,
                        "invoice_number": bill.invoice_number or "",
                        "reason": "unknown_vendor",
                        "details": "",
                    }
                )
                continue

            if args.skip_existing and bill_has_any_allocations(conn, bill.id):
                skipped_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor_norm": bill.vendor_norm,
                        "invoice_number": bill.invoice_number or "",
                        "reason": "already_has_allocations",
                        "details": "",
                    }
                )
                continue

            invoice_number = bill.invoice_number
            if not invoice_number:
                skipped_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor_norm": bill.vendor_norm,
                        "invoice_number": "",
                        "reason": "missing_invoice_number",
                        "details": "",
                    }
                )
                continue

            parsed: ParsedInvoice | None = None
            pdf_path = find_pdf_for_invoice(
                invoice_number,
                vendor_key=vkey if vkey in {"GFS", "CAPITAL"} else "",
                gfs_dir=args.gfs_pdf_dir,
                capital_dir=args.capital_pdf_dir,
            )

            # Parse or fallback rules.
            try:
                if vkey == "GFS" and pdf_path:
                    parsed = parse_gfs_invoice(pdf_path, invoice_number=invoice_number)
                elif vkey == "CAPITAL" and pdf_path:
                    parsed = parse_capital_invoice(pdf_path, invoice_number=invoice_number)
                elif vkey in {"GFS", "CAPITAL"} and not pdf_path:
                    # Missing PDF: fall back to Wave net/tax so downstream document_lines are complete.
                    parsed = ParsedInvoice(
                        vendor_key=vkey,
                        invoice_number=invoice_number,
                        subtotal_cents=bill.net_cents,
                        tax_cents=bill.tax_cents,
                        total_cents=bill.total_cents,
                        lines=[
                            InvoiceCategoryLine(
                                category_key="NO_PDF_NET",
                                label="No PDF; net from Wave",
                                subtotal_cents=bill.net_cents,
                            )
                        ],
                        pdf_path=None,
                        pdf_sha256=None,
                    )
                elif vkey in {"BLACK_CAT", "WEBSTAURANT"}:
                    fb_cfg = mapping.get("vendors", {}).get("FALLBACKS", {}).get(vkey, {})
                    net_acct = str((fb_cfg or {}).get("net_account_code") or ("5000" if vkey == "BLACK_CAT" else "5200"))
                    fb_notes = str((fb_cfg or {}).get("notes") or "").strip()
                    parsed = ParsedInvoice(
                        vendor_key=vkey,
                        invoice_number=invoice_number,
                        subtotal_cents=bill.net_cents,
                        tax_cents=bill.tax_cents,
                        total_cents=bill.total_cents,
                        lines=[InvoiceCategoryLine(category_key=vkey, label=vkey, subtotal_cents=bill.net_cents)],
                        pdf_path=None,
                        pdf_sha256=None,
                    )
                    # Override mapping for this line.
                    mapping.setdefault("_fallback_net_account_override", {})[bill.id] = (net_acct, fb_notes)
                else:
                    reason = "missing_pdf" if vkey in {"GFS", "CAPITAL"} else "no_parser_for_vendor"
                    skipped_rows.append(
                        {
                            "wave_bill_id": str(bill.id),
                            "invoice_date": bill.invoice_date,
                            "vendor_norm": bill.vendor_norm,
                            "invoice_number": invoice_number,
                            "reason": reason,
                            "details": str(pdf_path or ""),
                        }
                    )
                    continue
            except ParseError as e:
                skipped_rows.append(
                    {
                        "wave_bill_id": str(bill.id),
                        "invoice_date": bill.invoice_date,
                        "vendor_norm": bill.vendor_norm,
                        "invoice_number": invoice_number,
                        "reason": "parse_error",
                        "details": str(e),
                    }
                )
                continue

            assert parsed is not None

            if args.reset and not args.dry_run:
                conn.execute(
                    """
                    DELETE FROM bill_allocations
                    WHERE wave_bill_id = ? AND method IN (?, ?, ?, ?, ?)
                    """,
                    (bill.id, METHOD_CATEGORY, METHOD_TAX_ITC, METHOD_CC_FEE, METHOD_ADJUST, METHOD_FALLBACK),
                )

            alloc_rows: list[tuple[str, int, str, str]] = []

            # Categories (pre-tax).
            for line in parsed.lines:
                # Fallback vendor rules store their mapping under a synthetic key.
                if vkey in {"BLACK_CAT", "WEBSTAURANT"}:
                    override = mapping.get("_fallback_net_account_override", {}).get(bill.id)
                    if override:
                        account_code, extra = override
                        note = f"{METHOD_FALLBACK}; {extra}".strip("; ").strip()
                    else:
                        account_code = "5000"
                        note = METHOD_FALLBACK
                    alloc_rows.append((account_code, line.subtotal_cents, METHOD_FALLBACK, note))
                    continue

                account_code = account_for_vendor_line(mapping, vendor_key=parsed.vendor_key, category_key=line.category_key, label=line.label)
                if parsed.pdf_path is None and vkey in {"GFS", "CAPITAL"}:
                    method = METHOD_FALLBACK
                    note = f"no_pdf_fallback; vendor={parsed.vendor_key}; category={line.category_key} {line.label}"
                else:
                    method = METHOD_CATEGORY
                    note = f"vendor={parsed.vendor_key}; category={line.category_key} {line.label}"
                alloc_rows.append((account_code, line.subtotal_cents, method, note))

            # Tax ITC (invoice tax, not Wave tax).
            if parsed.tax_cents:
                tax_note = f"vendor={parsed.vendor_key}; invoice_tax_cents={parsed.tax_cents}"
                if parsed.pdf_path is None and vkey in {"GFS", "CAPITAL"}:
                    tax_note = f"no_pdf_fallback; vendor={parsed.vendor_key}; wave_tax_cents={parsed.tax_cents}"
                alloc_rows.append(
                    (
                        hst_itc,
                        parsed.tax_cents,
                        METHOD_TAX_ITC,
                        tax_note,
                    )
                )

            # Capital 3% CC fee era (Wave total includes fee; invoice PDF does not).
            if parsed.vendor_key == "CAPITAL" and is_capital_cc_fee(wave_total_cents=bill.total_cents, invoice_total_cents=parsed.total_cents):
                cap_cfg = mapping.get("vendors", {}).get("CAPITAL", {})
                fee_acct = str((cap_cfg or {}).get("cc_fee_account_code") or "6210").strip()
                fee_cents = bill.total_cents - parsed.total_cents
                alloc_rows.append(
                    (
                        fee_acct,
                        fee_cents,
                        METHOD_CC_FEE,
                        f"capital_cc_fee_detected; invoice_total_cents={parsed.total_cents}; wave_total_cents={bill.total_cents}",
                    )
                )

            # Final adjustment (keep sums equal to Wave total for downstream document_lines).
            allocated_sum = sum(c for _, c, _, _ in alloc_rows)
            diff = bill.total_cents - allocated_sum
            if diff != 0:
                alloc_rows.append(
                    (
                        "5099",
                        diff,
                        METHOD_ADJUST,
                        f"adjust_to_wave_total; diff_cents={diff}; wave_total_cents={bill.total_cents}",
                    )
                )

            # Insert rows
            if not args.dry_run:
                for account_code, amount_cents, method, notes in alloc_rows:
                    notes_parts = [notes]
                    if parsed.pdf_path:
                        notes_parts.append(f"pdf_path={parsed.pdf_path}")
                    if parsed.pdf_sha256:
                        notes_parts.append(f"pdf_sha256={parsed.pdf_sha256}")
                    notes_parts.append(f"invoice_number={invoice_number}")
                    final_notes = "; ".join([p for p in notes_parts if p])
                    conn.execute(
                        """
                        INSERT INTO bill_allocations(wave_bill_id, account_code, amount_cents, method, notes)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (bill.id, str(account_code).strip(), int(amount_cents), method, final_notes),
                    )
                rows_inserted += len(alloc_rows)
                imported += 1

        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()
    finally:
        conn.close()

    skipped_rows.sort(key=lambda r: (r["reason"], r["invoice_date"], int(r["wave_bill_id"])))

    with out_skipped.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["wave_bill_id", "invoice_date", "vendor_norm", "invoice_number", "reason", "details"],
        )
        w.writeheader()
        for r in skipped_rows:
            w.writerow(r)

    with out_summary.open("w", encoding="utf-8") as f:
        f.write("# Invoice PDF → bill_allocations import\n\n")
        f.write(f"- db: `{args.db}`\n")
        f.write(f"- mapping: `{args.mapping}`\n")
        f.write(f"- scope: `{start_date} → {end_date}`\n")
        f.write(f"- dry_run: `{args.dry_run}`\n")
        f.write(f"- reset: `{args.reset}`\n")
        f.write(f"- skip_existing: `{args.skip_existing}`\n\n")
        f.write("## Methods\n\n")
        f.write(f"- category: `{METHOD_CATEGORY}`\n")
        f.write(f"- tax_itc: `{METHOD_TAX_ITC}` (account `{hst_itc}`)\n")
        f.write(f"- capital_cc_fee: `{METHOD_CC_FEE}`\n")
        f.write(f"- adjustment: `{METHOD_ADJUST}`\n")
        f.write(f"- fallback: `{METHOD_FALLBACK}`\n\n")
        f.write("## Counts\n\n")
        f.write(f"- wave_bills_considered: {considered}\n")
        f.write(f"- bills_imported: {imported}\n")
        f.write(f"- allocation_rows_inserted: {rows_inserted if not args.dry_run else 0}\n")
        f.write(f"- bills_skipped: {len(skipped_rows)}\n\n")
        f.write("## Notes\n\n")
        f.write("- This importer only targets Wave bills missing allocations in scope.\n")
        f.write("- GFS uses the invoice 'Group Summary' category recap.\n")
        f.write("- Capital parses category totals + surcharges from the PDF and adds a Payment Processing Fee line when Wave totals include the ~3% CC fee era.\n")

    print("INVOICE PDF → BILL ALLOCATIONS IMPORT COMPLETE")
    print(f"- summary: {out_summary}")
    print(f"- skipped: {out_skipped}")
    print(f"- bills_imported: {imported}/{considered}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
