#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import pdfplumber
import yaml

from _lib import DB_PATH, SOT_ROOT, apply_migrations, connect_db


FY2024_START = "2023-06-01"
FY2025_END = "2025-05-31"


DEFAULT_GFS_PDF_DIR = Path("/home/clarencehub/Fresh/dump/gfs_flat")
DEFAULT_MAPPING_PATH = SOT_ROOT.parent / "overrides" / "invoice_pdf_mappings.yml"


class ParseError(RuntimeError):
    pass


@dataclass(frozen=True)
class InvoiceCategoryLine:
    category_key: str
    label: str
    subtotal_cents: int


@dataclass(frozen=True)
class ParsedInvoice:
    invoice_number: str
    subtotal_cents: int
    tax_cents: int
    total_cents: int
    lines: list[InvoiceCategoryLine]
    pdf_path: Path
    pdf_sha256: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def dollars_to_cents(s: str) -> int:
    s = str(s).strip().replace(",", "")
    return int(round(float(s) * 100))


def normalize_ws(s: str) -> str:
    return " ".join(str(s).split())


def load_mapping(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Invalid mapping YAML: {path}")
    return data


def account_for_gfs_category(mapping: dict, *, category_key: str, label: str) -> str:
    cfg = (mapping.get("vendors") or {}).get("GFS") if isinstance(mapping.get("vendors"), dict) else {}
    m = cfg.get("category_code_to_account_code") if isinstance(cfg, dict) else None
    if isinstance(m, dict) and category_key in m:
        return str(m[category_key]).strip()

    label_l = label.lower()
    if "pack" in label_l or "dispos" in label_l:
        return "5200"
    if "clean" in label_l:
        return "5204"
    if "bever" in label_l:
        return "5010"
    if "fuel" in label_l or "surcharge" in label_l:
        return "5100"

    default_code = cfg.get("default_account_code") if isinstance(cfg, dict) else None
    return str(default_code or "5000").strip()


_MONEY_RE = re.compile(r"\d+\.\d{2}")


def _cents_close(a: int, b: int, tol_cents: int = 2) -> bool:
    return abs(int(a) - int(b)) <= tol_cents


def parse_gfs_summary_amounts(line: str) -> tuple[int, int, int]:
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


def extract_pdf_text(pdf_path: Path) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        parts: list[str] = []
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                parts.append(t)
    return "\n".join(parts)


def parse_gfs_invoice(pdf_path: Path, *, invoice_number: str) -> ParsedInvoice:
    pdf_sha = sha256_file(pdf_path)
    text = extract_pdf_text(pdf_path)
    lines = [normalize_ws(l) for l in text.splitlines() if str(l).strip()]

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
    if len(total_amounts) >= 3:
        maybe_sub = dollars_to_cents(total_amounts[-3])
        maybe_tax = dollars_to_cents(total_amounts[-2])
        maybe_total = dollars_to_cents(total_amounts[-1])
        if _cents_close(maybe_sub + maybe_tax, maybe_total):
            subtotal_cents, tax_cents, total_cents = maybe_sub, maybe_tax, maybe_total
        else:
            subtotal_cents = tax_cents = total_cents = None  # type: ignore[assignment]
    else:
        subtotal_cents = tax_cents = total_cents = None  # type: ignore[assignment]

    if subtotal_cents is None and len(total_amounts) >= 2:
        maybe_sub = dollars_to_cents(total_amounts[-2])
        maybe_total = dollars_to_cents(total_amounts[-1])
        if _cents_close(maybe_sub, maybe_total):
            subtotal_cents, tax_cents, total_cents = maybe_sub, 0, maybe_total

    if subtotal_cents is None or tax_cents is None or total_cents is None:
        raise ParseError(f"GFS: could not parse totals from line: {total_line!r}")

    sum_sub = sum(l.subtotal_cents for l in parsed_lines)
    if abs(sum_sub - subtotal_cents) > 2:
        raise ParseError(f"GFS: category subtotals ({sum_sub}) do not match parsed subtotal ({subtotal_cents})")

    if abs((subtotal_cents + tax_cents) - total_cents) > 2:
        raise ParseError("GFS: subtotal+tax does not equal total")

    return ParsedInvoice(
        invoice_number=invoice_number,
        subtotal_cents=subtotal_cents,
        tax_cents=tax_cents,
        total_cents=total_cents,
        lines=parsed_lines,
        pdf_path=pdf_path,
        pdf_sha256=pdf_sha,
    )


def find_gfs_pdf(invoice_number: str, *, gfs_dir: Path) -> Path | None:
    hits = sorted(gfs_dir.glob(f"*{invoice_number}*.pdf"))
    return hits[0] if hits else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DB_PATH)
    ap.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING_PATH)
    ap.add_argument("--gfs-pdf-dir", type=Path, default=DEFAULT_GFS_PDF_DIR)
    ap.add_argument("--reset", action="store_true", help="Delete existing lines for derived GFS EFT docs before import.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--output-dir", type=Path, default=SOT_ROOT / "output")
    args = ap.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    out_summary = args.output_dir / "derived_gfs_eft_invoice_lines_import_summary.md"
    out_skipped = args.output_dir / "derived_gfs_eft_invoice_lines_import_skipped.csv"

    mapping = load_mapping(args.mapping)
    tax_cfg = mapping.get("tax") if isinstance(mapping.get("tax"), dict) else {}
    hst_itc = str((tax_cfg or {}).get("hst_itc_account_code") or "2210").strip()

    conn = connect_db(args.db)
    skipped: list[dict[str, str]] = []
    docs_considered = 0
    docs_filled = 0
    lines_inserted = 0

    try:
        apply_migrations(conn)
        conn.execute("BEGIN")

        if args.reset and not args.dry_run:
            doc_ids = [
                int(r["id"])
                for r in conn.execute(
                    """
                    SELECT id
                    FROM documents
                    WHERE doc_date >= ? AND doc_date <= ?
                      AND source_record_id LIKE 'derived__gfs_eft_invoice:%'
                    """,
                    (FY2024_START, FY2025_END),
                ).fetchall()
            ]
            if doc_ids:
                placeholders = ",".join(["?"] * len(doc_ids))
                conn.execute(f"DELETE FROM document_lines WHERE document_id IN ({placeholders})", doc_ids)

        rows = conn.execute(
            """
            SELECT d.id, d.doc_type, d.doc_date, d.doc_number, d.total_cents, d.source_record_id
            FROM documents d
            LEFT JOIN document_lines dl ON dl.document_id = d.id
            WHERE d.doc_date >= ? AND d.doc_date <= ?
              AND d.source_record_id LIKE 'derived__gfs_eft_invoice:%'
              AND dl.id IS NULL
            ORDER BY d.doc_date, d.id
            """,
            (FY2024_START, FY2025_END),
        ).fetchall()

        docs_considered = len(rows)

        for r in rows:
            doc_id = int(r["id"])
            doc_total = int(r["total_cents"] or 0)
            source_record_id = str(r["source_record_id"] or "")
            invoice_number = (str(r["doc_number"]).strip() if r["doc_number"] else "") or source_record_id.split(":", 1)[-1]
            sign = 1 if doc_total >= 0 else -1

            pdf_path = find_gfs_pdf(invoice_number, gfs_dir=args.gfs_pdf_dir)
            try:
                if pdf_path:
                    parsed = parse_gfs_invoice(pdf_path, invoice_number=invoice_number)
                    allocs: list[tuple[str, int, str]] = []
                    for line in parsed.lines:
                        acct = account_for_gfs_category(mapping, category_key=line.category_key, label=line.label)
                        allocs.append((acct, sign * line.subtotal_cents, f"category={line.category_key} {line.label}"))
                    if parsed.tax_cents:
                        allocs.append((hst_itc, sign * parsed.tax_cents, "tax_itc"))
                else:
                    allocs = [("5099", doc_total, "no_pdf_fallback")]
            except Exception as e:  # noqa: BLE001 - CLI tool
                skipped.append(
                    {
                        "document_id": str(doc_id),
                        "invoice_number": invoice_number,
                        "reason": "parse_error",
                        "details": str(e),
                    }
                )
                allocs = [("5099", doc_total, "parse_error_fallback")]

            alloc_sum = sum(a for _, a, _ in allocs)
            diff = doc_total - alloc_sum
            if diff != 0:
                allocs.append(("5099", diff, f"adjust_to_doc_total diff={diff}"))

            if args.dry_run:
                docs_filled += 1
                lines_inserted += len(allocs)
                continue

            line_no = 0
            for acct, amt, note in allocs:
                line_no += 1
                notes = [note, f"source={source_record_id}", f"invoice_number={invoice_number}"]
                if pdf_path:
                    notes.append(f"pdf_path={pdf_path}")
                    notes.append(f"pdf_sha256={sha256_file(pdf_path)}")
                conn.execute(
                    """
                    INSERT INTO document_lines(
                      document_id, line_no, description,
                      account_code, amount_cents, tax_cents,
                      method, notes
                    )
                    VALUES (?, ?, NULL, ?, ?, NULL, ?, ?)
                    """,
                    (doc_id, line_no, str(acct).strip(), int(amt), "PARSED", "; ".join(notes)),
                )
            docs_filled += 1
            lines_inserted += len(allocs)

        if args.dry_run:
            conn.rollback()
        else:
            conn.commit()
    finally:
        conn.close()

    skipped.sort(key=lambda x: (x["reason"], int(x["document_id"])))

    with out_skipped.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["document_id", "invoice_number", "reason", "details"])
        w.writeheader()
        for row in skipped:
            w.writerow(row)

    out_summary.write_text(
        "\n".join(
            [
                "# Derived GFS EFT invoice docs → document_lines import",
                "",
                f"- db: `{args.db}`",
                f"- scope: `{FY2024_START} → {FY2025_END}`",
                f"- mapping: `{args.mapping}`",
                f"- dry_run: `{args.dry_run}`",
                f"- reset: `{args.reset}`",
                "",
                "## Counts",
                "",
                f"- derived_docs_missing_lines_considered: {docs_considered}",
                f"- derived_docs_filled: {docs_filled}",
                f"- document_lines_inserted: {lines_inserted if not args.dry_run else 0}",
                f"- skipped_or_fallbacked: {len(skipped)}",
                "",
                "## Notes",
                "",
                "- Uses GFS invoice PDFs when available; otherwise falls back to a single 5099 line equal to the doc total.",
                "- This targets `source_record_id LIKE derived__gfs_eft_invoice:%` documents only.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print("DERIVED GFS EFT DOCUMENT LINES IMPORT COMPLETE")
    print(f"- summary: {out_summary}")
    print(f"- skipped: {out_skipped}")
    print(f"- docs_filled: {docs_filled}/{docs_considered}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
