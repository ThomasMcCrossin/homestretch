#!/usr/bin/env python3
"""
Build per-fiscal-year filing artifacts from the combined `packet.json`.

Why:
- UFile is used one tax year at a time.
- For scalable workflows (other clients/years), we want a year-scoped packet + guide.

This tool is deterministic and read-only relative to the accounting DB/snapshots.
It only writes under `UfileToFill/ufile_packet/years/`.
"""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from render_year_guide_html import render_year_guide_html


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PACKET_PATH = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "packet.json"
OUT_DIR = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "years"
TABLES_DIR = PROJECT_ROOT / "UfileToFill" / "ufile_packet" / "tables"
ACCOUNTING_OUTPUT_DIR = PROJECT_ROOT / "output"


def money(n: int) -> str:
    return f"{n:,}"


def schedule_1_sort_key(code: str) -> tuple[int, object]:
    if code == "A":
        return (-2, 0)
    if code == "C":
        return (2, 0)
    if code.isdigit():
        return (0, int(code))
    return (1, code)


def build_year_packet(packet: dict, fy: str) -> dict:
    entity = packet["entity"]
    year = packet["years"][fy]
    return {
        "meta": {
            "schema_version": packet["meta"]["schema_version"],
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": "tools/build_year_artifacts.py",
            "source_packet": str(PACKET_PATH.relative_to(PROJECT_ROOT)),
            "snapshot_source": packet["meta"]["snapshot_source"],
            "fiscal_year": fy,
        },
        "entity": entity,
        "global_positions": packet.get("global_positions", {}),
        "year": {fy: year},
        "evidence_index": packet.get("evidence_index", []),
        "known_judgments": packet.get("known_judgments", []),
    }


def build_year_guide(packet: dict, fy: str) -> str:
    entity = packet["entity"]
    year = packet["years"][fy]
    period = year["fiscal_period"]
    global_positions = packet.get("global_positions", {})

    schedule_100 = year["schedule_100"]
    schedule_125 = year["schedule_125"]
    retained = year["retained_earnings"]
    schedule_1 = year["schedule_1"]
    positions = year.get("positions", {})

    # UFile UI quirk: summary GIFI lines (e.g., 1120 Inventories, 1480 Other current assets) can be ignored
    # by UFile’s auto-calculated totals. Our schedule exports therefore prefer UFile-friendly detail lines
    # where applicable (e.g., 1121 for inventory; 1484 for prepaid expenses).
    ufile_entry_code_map: dict[str, tuple[str, str]] = {}

    # Totals are useful for tie-checking but should not be manually entered in UFile.
    do_not_enter_codes = {
        "1599": "Total current assets (auto-calculated)",
        "2599": "Total assets (auto-calculated)",
        "3499": "Total liabilities (auto-calculated)",
        "3620": "Total shareholder equity (auto-calculated)",
        "3640": "Total liabilities and shareholder equity (auto-calculated)",
        "8299": "Total revenue (auto-calculated)",
        "8519": "Gross profit/loss (auto-calculated)",
        "9367": "Total operating expenses (auto-calculated)",
        "9368": "Total expenses (auto-calculated)",
        "9970": "Net income/loss before taxes (auto-calculated)",
        "9999": "Net income/loss after taxes (auto-calculated)",
    }

    def build_cogs_entry_rows() -> list[tuple[str, str, int, str]]:
        """
        UFile often expects cost of sales to be entered via 8300/8320/8500
        (and then it auto-calculates 8518/8519). We compute:
          purchases = COGS + closing_inv - opening_inv
        using whole-dollar schedule amounts.
        """
        if "8518" not in schedule_125:
            return []
        cogs = int(schedule_125["8518"]["amount"])

        def year_end_inventory_amount(year_obj: dict) -> int:
            sch100 = year_obj.get("schedule_100", {})
            for code in ("1121", "1120"):
                if code in sch100:
                    return int(sch100[code].get("amount", 0))
            return 0

        # Opening/closing inventory come from Schedule 100 inventories (1121 preferred).
        opening_inv = 0
        closing_inv = 0
        if fy == "FY2024":
            opening_inv = 0
            closing_inv = year_end_inventory_amount(year)
        else:
            # For FY2025+, opening inventory should match prior year closing inventory.
            # If prior year isn't present, fall back to 0.
            prior_fy = f"FY{int(fy[2:]) - 1}"
            opening_inv = year_end_inventory_amount(packet["years"].get(prior_fy, {}))
            closing_inv = year_end_inventory_amount(year)

        purchases = cogs - opening_inv + closing_inv

        rows: list[tuple[str, str, int, str]] = []
        rows.append(("8300", "Opening inventory", opening_inv, ""))
        rows.append(
            (
                "8320",
                "Purchases / cost of materials",
                purchases,
                "If UFile auto-calculates 8320, do NOT type it; use as a tie-check only. Otherwise enter it. Computation: purchases = 8518 - 8300 + 8500.",
            )
        )
        rows.append(("8500", "Closing inventory", closing_inv, ""))
        return rows

    def rows_from_schedule(schedule: dict) -> list[tuple[str, str, int, str]]:
        out = []
        for code, obj in schedule.items():
            amt = int(obj["amount"])
            label = obj.get("label") or ""
            note = obj.get("note") or ""
            if amt == 0:
                continue
            # Cost of sales (8518) is usually better entered via 8300/8320/8500 in UFile.
            if schedule is schedule_125 and code == "8518":
                continue
            if code in do_not_enter_codes:
                # Keep totals out of the entry table; we list them separately as tie-checks.
                continue
            if code in ufile_entry_code_map:
                mapped_code, mapped_label = ufile_entry_code_map[code]
                note = (note + " " if note else "") + f"(Enter in UFile as {mapped_code} {mapped_label})"
                code = mapped_code
                label = mapped_label
            out.append((code, label, amt, note))
        out.sort(key=lambda x: int(x[0]))
        return out

    def md_table(headers: list[str], rows: list[list[str]]) -> str:
        if not rows:
            return "_(none)_"
        out = []
        out.append("| " + " | ".join(headers) + " |")
        out.append("|" + "|".join(["---"] * len(headers)) + "|")
        for r in rows:
            out.append("| " + " | ".join(r) + " |")
        return "\n".join(out)

    def parse_ymd(s: str) -> datetime:
        # Dates in the packet and most outputs are stored as YYYY-MM-DD.
        return datetime.strptime(s, "%Y-%m-%d")

    def date_in_fy(date_ymd: str) -> bool:
        if not date_ymd:
            return False
        try:
            d = parse_ymd(date_ymd).date()
        except Exception:
            return False
        start = parse_ymd(period["start"]).date()
        end = parse_ymd(period["end"]).date()
        return start <= d <= end

    def read_csv_rows(path: Path) -> list[dict[str, str]]:
        if not path.exists():
            return []
        with path.open(newline="") as f:
            return list(csv.DictReader(f))

    # Header
    parts: list[str] = []
    parts.append(f"# UFile T2 Fill Guide — {fy}")
    parts.append("")
    parts.append(f"**Entity:** {entity.get('legal_name')} ({entity.get('operating_name')})")
    parts.append(f"**BN:** {entity.get('bn')}")
    parts.append(f"**Tax year:** {period['start']} → {period['end']} (year-end {entity.get('year_end_month_day')})")
    if entity.get("naics_code"):
        parts.append(f"**NAICS:** {entity['naics_code']}")
    parts.append("")
    parts.append("**Readable view:** open `UFILet2_FILL_GUIDE.html` (bigger text + no horizontal scroll).")
    parts.append("")

    parts.append("## UFile entry rules (important)")
    parts.append("- Enter amounts on the **detail lines** listed below (e.g., use `1121` for inventory, `1484` for prepaid).")
    parts.append(
        "- Leave totals like `1599`/`2599`/`3499`/`3640` blank; UFile usually auto-calculates them. "
        "If it doesn’t, confirm you used the detail lines (especially `1121`, `1484`, `2781`), then use the tie-check totals below."
    )
    parts.append("- On Schedule 125, enter **trade sales** on `8000` (and do **not** enter `8299` total revenue). UFile will compute totals from the detail lines.")
    parts.append("")

    parts.append("## If something looks wrong in UFile (fast troubleshooting)")
    parts.append("- If inventory isn’t included in current assets: ensure it’s entered on **`1121`** (not `1120`).")
    parts.append("- If prepaids aren’t included in current assets: ensure it’s entered on **`1484`** (not `1480`).")
    parts.append("- If shareholder payable isn’t included: try **`2781`**; if UFile rejects it, enter the same amount on **`2780`**.")
    parts.append("- If totals don’t match: delete anything typed into subtotal/total lines (`1599`, `2599`, `3640`, `8299`, `9367`, `9368`, etc.) and re-enter only the detail lines.")
    parts.append("- If Net income screen totals look inflated: you likely double-entered revenue (e.g., `8000` + `8299`). Only enter `8000` and let UFile total it.")
    parts.append("- If you see diagnostics like “`GIFI-FIELD 9367 does not match internal subtotal calculation`”: a total/subtotal line is being populated inconsistently with the expense detail lines. Clear totals (`9367`/`9368`) and rely on the detail expense lines only.")
    parts.append("- If you see diagnostics like “`GIFI-FIELD 3849 does not match internal subtotal calculation`”: retained earnings end (`3849`) / balance sheet retained earnings (`3600`) does not match the retained earnings rollforward. Enter only the rollforward lines (`3660`, `3680`, `3700`, `3740`) and let UFile compute `3849`/`3600`.")
    parts.append("")

    # Minimal identity reminders (carryforward fields people fat-finger)
    parts.append("## Key carryforward fields (match 2023 filing)")
    parts.append(
        md_table(
            ["Field", "Value"],
            [
                ["Mailing addressee", entity.get("mailing_address_addressee") or "(see packet)"],
                ["Books & records addressee", entity.get("books_and_records_addressee") or "(see packet)"],
                ["Head office street", entity.get("head_office_address", {}).get("street", "")],
                [
                    "Head office city/prov/postal",
                    f"{entity.get('head_office_address', {}).get('city','')}, "
                    f"{entity.get('head_office_address', {}).get('province','')} "
                    f"{entity.get('head_office_address', {}).get('postal_code','')}",
                ],
            ],
        )
    )
    parts.append("")

    # Key filing positions / elections (high signal)
    parts.append("## Key positions / elections (high signal)")
    pos_rows: list[list[str]] = []

    def yn(v: object) -> str:
        return "Yes" if v is True else "No" if v is False else str(v)

    if "ifrs" in global_positions:
        pos_rows.append(["IFRS used?", yn(global_positions["ifrs"].get("value")), global_positions["ifrs"].get("note", "")])
    if "practitioner_involvement" in positions:
        pos_rows.append(
            [
                "Practitioner involvement",
                str(positions["practitioner_involvement"].get("value")),
                positions["practitioner_involvement"].get("note", ""),
            ]
        )
    if "functional_currency" in global_positions:
        pos_rows.append(
            [
                "Functional currency",
                str(global_positions["functional_currency"].get("value")),
                global_positions["functional_currency"].get("note", ""),
            ]
        )
    if "language_of_correspondence" in global_positions:
        pos_rows.append(
            [
                "Language of correspondence",
                str(global_positions["language_of_correspondence"].get("value")),
                global_positions["language_of_correspondence"].get("note", ""),
            ]
        )
    if entity.get("corp_type"):
        pos_rows.append(["Corporation type", str(entity.get("corp_type")), ""])
    if "associated_corporations" in global_positions:
        pos_rows.append(
            [
                "Associated corporations?",
                yn(global_positions["associated_corporations"].get("value")),
                global_positions["associated_corporations"].get("note", ""),
            ]
        )
    if "capital_tax_exempt" in global_positions:
        pos_rows.append(
            [
                "Tax on capital exempt?",
                yn(global_positions["capital_tax_exempt"].get("value")),
                global_positions["capital_tax_exempt"].get("note", ""),
            ]
        )
    if "hst_registration_date" in global_positions:
        pos_rows.append(
            [
                "HST registration date",
                str(global_positions["hst_registration_date"].get("value")),
                global_positions["hst_registration_date"].get("note", ""),
            ]
        )
    if "hst_registered" in positions:
        pos_rows.append(["HST reported this year?", yn(positions["hst_registered"].get("value")), positions["hst_registered"].get("note", "")])
    if "inventory_method" in positions:
        pos_rows.append(
            [
                "Inventory method",
                str(positions["inventory_method"].get("value")),
                positions["inventory_method"].get("note", ""),
            ]
        )
    if "tips_handling" in positions:
        pos_rows.append(["Tips handling", str(positions["tips_handling"].get("value")), positions["tips_handling"].get("note", "")])
    if "shareholder_loan_s15_2" in positions:
        pos_rows.append(
            [
                "Shareholder loan at year-end?",
                yn(positions["shareholder_loan_s15_2"].get("value")),
                positions["shareholder_loan_s15_2"].get("note", ""),
            ]
        )

    parts.append(md_table(["Item", "Value", "Note"], pos_rows))
    parts.append("")

    parts.append("## Must-check before filing / exporting a PDF copy")
    parts.append(
        "\n".join(
            [
                f"- Confirm the UFile tax year dates are **exactly** `{period['start']}` to `{period['end']}`.",
                "- Confirm the T2 jacket address fields are filled (Head office + Mailing if different).",
                "- On Schedule 125, fill the business/operation description fields if UFile leaves them blank.",
                "- If you are claiming CCA: enter Schedule 8 via **Capital cost allowance** (do not rely on Schedule 1 alone).",
                "- When you export/print a \"package\" PDF from UFile, make sure the export includes required schedule forms.",
                "",
                "After exporting, run this completeness check (fails if required schedule forms like 8/88 are missing from the PDF):",
                "",
                f"```bash\npython3 T2Analysis/tools/check_ufile_export_completeness.py --fy {fy} --pdf /path/to/ufile_export.pdf\n```",
            ]
        )
    )
    parts.append("")

    # GIFI form + notes checklist + notes to financial statements (UFile screens)
    parts.append("## GIFI form / notes (UFile screens)")
    parts.append("- In the main GIFI screen, select: **Update Net income and Tax on capital pages from GIFI**.")
    parts.append("- IFRS used? **No**.")
    parts.append("")
    parts.append("### Notes checklist (recommended minimal)")
    parts.append(
        md_table(
            ["Field", "Value", "Note"],
            [
                ["Identify person primarily involved with financial info (>50%)", "Yes", ""],
                ["Type of preparer (if asked)", "Other (specify): Management", "Management-prepared, unaudited; no accounting practitioner involvement."],
                ["Accounting practitioner involvement (if asked)", "Other (specify): None", ""],
                ["GIFI checklist items", "101 Notes to financial statements", "Select only if you enter notes; otherwise leave checklist blank."],
            ],
        )
    )
    parts.append("")
    parts.append("### Notes to financial statements (paste-ready starter text)")
    hst_note = (
        "GST/HST registration became effective 2024-02-26; no GST/HST was collected prior to that date. "
        "Some Shopify reports may label pre-registration amounts as “tax”; these amounts are treated as sales/pricing, not GST/HST."
    )
    inv_note = (
        "Inventory is stated at cost. FY2025 closing inventory is based on a physical count near year-end; "
        "FY2024 closing inventory is an estimate based on available records."
    )
    parts.append(
        "\n".join(
            [
                "- Financial statements are management-prepared, unaudited, and prepared on an accrual basis at historical cost.",
                f"- {inv_note}",
                f"- {hst_note}",
            ]
        )
    )
    parts.append("")

    # Corporate history carryforward (UFile screen)
    parts.append("## Corporate history carryforward (UFile screen)")
    ufile_screens = year.get("ufile_screens", {})
    corp_hist = ufile_screens.get("corporate_history", {}) if isinstance(ufile_screens, dict) else {}

    # Back-compat: older packets did not store a corporate_history object.
    if not isinstance(corp_hist, dict) or not corp_hist:
        prior_end = "2023-05-31"
        prior_taxable_income = 0
        prior_paid_up_capital = int(schedule_100.get("3500", {}).get("amount") or 0)
        prior_total_assets = 0
        prior_sbd_claimed: str = "No"

        if fy != "FY2024":
            prior_fy = f"FY{int(fy[2:]) - 1}"
            prior_year = packet["years"].get(prior_fy)
            if prior_year:
                prior_end = prior_year["fiscal_period"]["end"]
                prior_taxable_income = int(
                    (prior_year["schedule_1"].get("C") or prior_year["schedule_1"].get("400") or {"amount": 0}).get("amount") or 0
                )
                prior_total_assets = int(prior_year.get("schedule_100", {}).get("2599", {}).get("amount") or 0)
                # As a CCPC with active business income, prior year generally claims SBD (confirm in UFile).
                prior_sbd_claimed = "Yes"
    else:
        prior_end = str(corp_hist.get("prior_year_end_date") or "2023-05-31")
        prior_taxable_income = int(corp_hist.get("prior_year_taxable_income") or 0)
        prior_paid_up_capital = int(corp_hist.get("prior_year_taxable_paid_up_capital") or 0)
        prior_total_assets = int(corp_hist.get("prior_year_total_assets_gifi_2599") or 0)
        prior_sbd_claimed = "Yes" if corp_hist.get("prior_year_claimed_sbd") is True else "No"

    parts.append(
        md_table(
            ["Field", "Value", "Note"],
            [
                ["1st prior year end date", prior_end, "UFile field: End date of prior tax year"],
                ["1st prior year taxable income", money(prior_taxable_income), "UFile field: Taxable income (Schedule 1 code C of the prior year)"],
                [
                    "Eligible RDTOH at prior year-end",
                    money(int((corp_hist.get("eligible_rdtoh_end_prior_year") if isinstance(corp_hist, dict) else 0) or 0)),
                    "Usually $0 for your file unless you have refundable dividend tax on hand",
                ],
                ["Non-eligible RDTOH at prior year-end", money(int((corp_hist.get("non_eligible_rdtoh_end_prior_year") if isinstance(corp_hist, dict) else 0) or 0)), ""],
                ["Eligible dividend refund (prior year)", money(int((corp_hist.get("eligible_dividend_refund_prior_year") if isinstance(corp_hist, dict) else 0) or 0)), ""],
                ["Non-eligible dividend refund (prior year)", money(int((corp_hist.get("non_eligible_dividend_refund_prior_year") if isinstance(corp_hist, dict) else 0) or 0)), ""],
                ["Did the corp claim SBD in the prior year?", prior_sbd_claimed, "Confirm in UFile if it asks; FY2023 stub was inactive, FY2024 claimed SBD as a CCPC."],
                ["Large corporation amount (prior year)", money(0), "UFile field: line 415 of Schedule 200 (prior year)"],
                ["Taxable paid-up capital", money(prior_paid_up_capital), "Use share capital unless you have evidence of paid-up capital changes"],
                ["Total assets at prior year-end", money(prior_total_assets), "UFile field: Total assets as at previous year-end (Schedule 100 GIFI 2599)"],
                ["Capital gain inclusion rate / amount (prior year)", "", "Only needed for carryback purposes; leave blank unless applicable"],
            ],
        )
    )
    parts.append("")

    # Net income + tax on capital (UFile screens)
    parts.append("## Net income (UFile screen)")
    # Prefer 8299 Total revenue if present (avoid double-counting it with 8000).
    gross_revenue = 0
    if isinstance(schedule_125.get("8299"), dict) and "amount" in schedule_125["8299"]:
        gross_revenue = int(schedule_125["8299"]["amount"])
    else:
        for code, obj in schedule_125.items():
            if not (isinstance(code, str) and code.isdigit()):
                continue
            n = int(code)
            if n == 8299:
                continue
            if 7000 <= n <= 8299:
                try:
                    gross_revenue += int(obj.get("amount", 0))
                except Exception:
                    pass
    parts.append(
        md_table(
            ["Field", "Value", "Note"],
            [
                [
                    "Net income as per financial statements",
                    money(int((schedule_1.get("A") or schedule_1.get("300") or {"amount": 0}).get("amount") or 0)),
                    "Should auto-fill from GIFI; otherwise enter from Schedule 1 code A.",
                ],
                ["Total sales of corporation during this taxation year", money(gross_revenue), "Use total revenue (sum of revenue lines; typically matches trade sales 8000)."],
                ["Total gross revenues", money(gross_revenue), "Usually same as total sales for your file."],
            ],
        )
    )
    parts.append("")
    parts.append(
        "If UFile auto-populates these from GIFI, do not add manual “additions/deductions” here; use Schedule 1 for tax add-backs (meals 50%, penalties, etc.)."
    )
    parts.append("")

    parts.append("## Tax on capital (UFile screen)")
    parts.append(
        md_table(
            ["Field", "Value", "Note"],
            [
                ["Eligible for capital tax exemption?", "Yes", "For your file, expect capital tax exemption; confirm if UFile still requests fields."],
                ["Total assets at year-end date from financial statements", money(int(schedule_100["2599"]["amount"])), "If required, use Schedule 100 total assets (GIFI 2599)."],
                ["Retained earnings/deficit at year-end (if required)", money(int(schedule_100.get("3600", {}).get("amount") or 0)), "If UFile forces a retained earnings element, use Schedule 100 GIFI 3600."],
            ],
        )
    )
    parts.append("")

    # Identification of the corporation (UFile screen)
    ident = ufile_screens.get("identification_of_corporation", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(ident, dict) and ident:
        parts.append("## Identification of the corporation (UFile screen)")
        principal_products = ident.get("principal_products") or []
        principal_products_str = ", ".join(
            [
                f"{p.get('description','')} ({int(p.get('percent_of_revenue') or 0)}%)"
                for p in principal_products
                if isinstance(p, dict) and p.get("description")
            ]
        )
        internet = ident.get("internet_business") or {}
        urls = internet.get("top_urls") if isinstance(internet, dict) else []
        urls_str = ", ".join([u for u in urls if isinstance(u, str)]) if urls else ""

        parts.append(
            md_table(
                ["Field", "Value", "Note"],
                [
                    ["Corporation name", entity.get("legal_name", ""), ""],
                    ["Business number", entity.get("bn", ""), ""],
                    ["Tax year end", period["end"], ""],
                    [
                        "One-month extension of balance due date?",
                        yn(ident.get("one_month_extension_balance_due")),
                        "Carryforward from prior UFile exports; review CCPC/SBD eligibility if you want the extension.",
                    ],
                    ["Charter jurisdiction", str(ident.get("charter_jurisdiction") or ""), ""],
                    ["Incorporation date", str(ident.get("incorporation_date") or ""), ""],
                    ["Beginning date of operations", str(ident.get("operations_start_date") or ""), ""],
                    ["First federal return?", yn(ident.get("is_first_federal_return")), "2023 stub return was the first return; FY2024/FY2025 should be No."],
                    ["Final federal return?", yn(ident.get("is_final_federal_return")), ""],
                    ["Permanent establishment province", str(ident.get("permanent_establishment_province") or ""), ""],
                    ["Language of correspondence", str(ident.get("language_of_correspondence") or ""), ""],
                    ["Corporation email", str(ident.get("email") or ""), ""],
                    ["Active/inactive status", str(ident.get("activity_status") or ""), ""],
                    ["Activity description", str(ident.get("activity_description") or ""), ""],
                    ["NAICS", str(ident.get("naics_code") or entity.get("naics_code") or ""), ""],
                    ["Principal products/services", principal_products_str, ""],
                    ["Has GIFI financials?", yn(ident.get("has_gifi_financials")), "Must be Yes or UFile may wipe GIFI entries."],
                    [
                        "Construction subcontractors?",
                        "",
                        "UFile asks this only if your major business activity is construction; not applicable for a canteen/restaurant.",
                    ],
                    ["Internet income from websites?", yn(internet.get("earns_income") if isinstance(internet, dict) else None), ""],
                    ["# of websites", str(internet.get("number_of_sites") or ""), ""],
                    [
                        "% gross revenue from internet",
                        str(internet.get("percent_gross_revenue_from_internet") or ""),
                        "This % is easy to misinterpret with Shopify POS; keep consistent year-to-year unless you have a better basis.",
                    ],
                    ["Top URL(s)", urls_str, ""],
                    ["Quarterly instalments – wants considered?", yn((ident.get("quarterly_installments") or {}).get("wants_consideration") if isinstance(ident.get("quarterly_installments"), dict) else None), ""],
                    ["Quarterly instalments – perfect compliance?", yn((ident.get("quarterly_installments") or {}).get("perfect_compliance_history") if isinstance(ident.get("quarterly_installments"), dict) else None), ""],
                ],
            )
        )
        parts.append("")

    # Addresses + preparer + officers (mostly identical year-to-year; keep aligned to filed 2023)
    entity_ufile = entity.get("ufile_screens", {}) if isinstance(entity.get("ufile_screens"), dict) else {}

    head_office = entity_ufile.get("head_office_address", {}) if isinstance(entity_ufile, dict) else {}
    if isinstance(head_office, dict) and head_office:
        parts.append("## Head office address (UFile screen)")
        parts.append(
            md_table(
                ["Field", "Value"],
                [
                    ["Addressee", str(head_office.get("addressee") or "")],
                    ["Street", str(head_office.get("street") or "")],
                    ["Additional address info", ""],
                    ["Suite number", ""],
                    ["Post office box number", ""],
                    ["City", str(head_office.get("city") or "")],
                    ["Province", str(head_office.get("province") or "")],
                    ["Postal code", str(head_office.get("postal_code") or "")],
                    ["Person to contact", str(head_office.get("contact_person") or "")],
                    ["Phone (day)", str(head_office.get("phone_day") or "")],
                    ["Fax", str(head_office.get("fax") or "")],
                    ["Changed since last return?", str(head_office.get("changed_since_last_return") or "")],
                ],
            )
        )
        parts.append("")

    other_addrs = entity_ufile.get("other_addresses", {}) if isinstance(entity_ufile, dict) else {}
    if isinstance(other_addrs, dict) and other_addrs:
        mailing = other_addrs.get("mailing", {}) if isinstance(other_addrs.get("mailing"), dict) else {}
        books = other_addrs.get("books_and_records", {}) if isinstance(other_addrs.get("books_and_records"), dict) else {}

        if mailing:
            parts.append("## Mailing address (UFile screen)")
            parts.append(
                md_table(
                    ["Field", "Value"],
                    [
                        ["Addressee", str(mailing.get("addressee") or "")],
                        ["Street", str(mailing.get("street") or "")],
                        ["Additional address info", ""],
                        ["Suite number", ""],
                        ["Post office box number", ""],
                        ["City", str(mailing.get("city") or "")],
                        ["Province", str(mailing.get("province") or "")],
                        ["State", ""],
                        ["Postal code", str(mailing.get("postal_code") or "")],
                        ["U.S.A. ZIP code", ""],
                        ["Foreign postal code", ""],
                        ["Country (if other than Canada)", ""],
                        ["Person to contact", str(mailing.get("contact_person") or "")],
                        ["Phone (day)", str(mailing.get("phone_day") or "")],
                        ["Fax", str(mailing.get("fax") or "")],
                        ["Changed since last return?", str(mailing.get("changed_since_last_return") or "")],
                    ],
                )
            )
            parts.append("")

        if books:
            parts.append("## Location of books & records (UFile screen)")
            parts.append(
                md_table(
                    ["Field", "Value"],
                    [
                        ["Addressee", str(books.get("addressee") or "")],
                        ["Street", str(books.get("street") or "")],
                        ["Additional address info", ""],
                        ["Suite number", ""],
                        ["City", str(books.get("city") or "")],
                        ["Province", str(books.get("province") or "")],
                        ["State", ""],
                        ["Postal code", str(books.get("postal_code") or "")],
                        ["U.S.A. ZIP code", ""],
                        ["Foreign postal code", ""],
                        ["Country (if other than Canada)", ""],
                        ["Person to contact", str(books.get("contact_person") or "")],
                        ["Phone (day)", str(books.get("phone_day") or "")],
                        ["Fax", str(books.get("fax") or "")],
                        ["Changed since last return?", str(books.get("changed_since_last_return") or "")],
                    ],
                )
            )
            parts.append("")

    tax_preparer = entity_ufile.get("tax_preparer", {}) if isinstance(entity_ufile, dict) else {}
    if isinstance(tax_preparer, dict) and tax_preparer:
        parts.append("## Tax preparer (UFile screen)")
        parts.append(
            md_table(
                ["Field", "Value"],
                [
                    ["Addressee", str(tax_preparer.get("addressee") or "")],
                    ["Position/title", str(tax_preparer.get("position_or_title") or "")],
                    ["Contact first name", str(tax_preparer.get("contact_first_name") or "")],
                    ["Contact last name", str(tax_preparer.get("contact_last_name") or "")],
                    ["Phone (day)", str(tax_preparer.get("phone_day") or "")],
                    ["Fax", str(tax_preparer.get("fax") or "")],
                    ["Federal rep ID", str(tax_preparer.get("rep_id") or "")],
                    ["Email", str(tax_preparer.get("email") or "")],
                    ["Street", str(tax_preparer.get("street") or "")],
                    ["City", str(tax_preparer.get("city") or "")],
                    ["Province", str(tax_preparer.get("province") or "")],
                    ["Postal code", str(tax_preparer.get("postal_code") or "")],
                ],
            )
        )
        parts.append("")
        parts.append("Leave **Notes** and **Override** sections blank unless you intentionally need them.")
        parts.append("")

    officers = entity_ufile.get("corporate_officers") if isinstance(entity_ufile, dict) else None
    if isinstance(officers, list) and officers:
        parts.append("## Corporate officers / directors (UFile screen)")
        parts.append(
            md_table(
                [
                    "Name",
                    "Title",
                    "Signing officer?",
                    "Elected",
                    "Ceased",
                    "Non-resident?",
                    "Also shareholder?",
                    "SIN",
                    "Voting/Common/Pref %",
                    "Address",
                    "Phone",
                    "Fax",
                ],
                [
                    [
                        f"{o.get('first_name','')} {o.get('last_name','')}",
                        str(o.get("title") or ""),
                        yn(o.get("is_signing_officer")),
                        str(o.get("elected_date") or ""),
                        str(o.get("ceased_date") or ""),
                        "No",
                        "Yes",
                        str(o.get("sin") or ""),
                        f"{o.get('voting_pct','')}/{o.get('common_pct','')}/{o.get('preferred_pct','')}",
                        f"{o.get('address_street','')}, {o.get('address_city','')} {o.get('address_province','')} {o.get('address_postal_code','')}",
                        str(o.get("phone_day") or ""),
                        str(o.get("fax") or ""),
                    ]
                    for o in officers
                    if isinstance(o, dict)
                ],
            )
        )
        parts.append("")
        parts.append("- Has there been a change of directors since the last return? **No**")
        parts.append("- Previous shareholder names: leave blank (no name changes).")
        parts.append("- Date the return is signed: fill on filing/signing day (do not carry forward stale dates).")
        parts.append("")
        parts.append(
            "**Note:** If a director “ceased date” is a carryforward artifact but the person is still a director, "
            "leave the ceased date blank in UFile for the current filing."
        )
        parts.append("")

    refund_screen = ufile_screens.get("refund_or_balance_owing", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(refund_screen, dict) and refund_screen:
        parts.append("## Refund or balance owing (UFile screen)")
        parts.append(
            md_table(
                ["Field", "Value"],
                [
                    ["Tax payment information (code)", str(refund_screen.get("tax_payment_code") or "")],
                    ["Tax refund information (code)", str(refund_screen.get("refund_code") or "")],
                ],
            )
        )
        parts.append("")

    # Transactions with shareholders/officers/employees (disclosure screen)
    related = ufile_screens.get("transactions_with_shareholders_officers_employees", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(related, dict) and related.get("note"):
        parts.append("## Transactions with shareholders/officers/employees (UFile disclosure)")
        parts.append(str(related.get("note")))
        parts.append("")

    # Dividends paid (FY-specific)
    dividends = ufile_screens.get("dividends_paid", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(dividends, dict) and dividends.get("has_dividends"):
        parts.append("## Dividends paid (UFile screen)")
        parts.append(
            md_table(
                ["Field", "Value", "Note"],
                [
                    ["Taxable dividends paid", money(int(dividends.get("taxable_dividends_paid") or 0)), ""],
                    ["Eligible portion of taxable dividends", money(int(dividends.get("eligible_dividend_portion") or 0)), "If $0, treat dividends as non-eligible unless you explicitly designate eligible in UFile."],
                    ["Capital dividends (83(2))", money(int(dividends.get("capital_dividends") or 0)), ""],
                    ["Capital gains dividend", money(int(dividends.get("capital_gains_dividend") or 0)), ""],
                ],
            )
        )
        if dividends.get("note"):
            parts.append("")
            parts.append(str(dividends.get("note")))
        parts.append("")

    # GRIP (only relevant if eligible dividends are paid/designated)
    grip = ufile_screens.get("general_rate_income_pool", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(grip, dict) and grip:
        parts.append("## General rate income pool (GRIP) (UFile screen)")
        amount_respecting = grip.get("amount_respecting_dividends") if isinstance(grip.get("amount_respecting_dividends"), list) else []
        before = grip.get("specified_future_tax_consequences_before") if isinstance(grip.get("specified_future_tax_consequences_before"), list) else []
        after = grip.get("specified_future_tax_consequences_after") if isinstance(grip.get("specified_future_tax_consequences_after"), list) else []
        parts.append(
            md_table(
                ["Field", "Value", "Note"],
                [
                    ["GRIP at end of previous year", money(int(grip.get("grip_end_prior_year") or 0)), ""],
                    [
                        "Amount respecting dividends (entries)",
                        str(len(amount_respecting)),
                        "UFile allows multiple selections; usually 0 for non-eligible dividends only.",
                    ],
                    [
                        "Specified future tax consequences (before) (entries)",
                        str(len(before)),
                        "UFile allows multiple selections.",
                    ],
                    [
                        "Specified future tax consequences (after) (entries)",
                        str(len(after)),
                        "UFile allows multiple selections.",
                    ],
                    [
                        "Elected excessive eligible dividend designation as ordinary",
                        money(int(grip.get("elected_excessive_eligible_dividend_designation_as_ordinary") or 0)),
                        "",
                    ],
                ],
            )
        )
        if grip.get("note"):
            parts.append("")
            parts.append(str(grip.get("note")))
        parts.append("")

    # Screens expected to be blank / N/A (still useful to confirm in UFile UI)
    blank_screens = [
        ("Loss carryforwards / carrybacks", "losses"),
        ("Charitable donations", "charitable_donations"),
        ("Reserves", "reserves"),
        ("Capital cost allowance (CCA)", "capital_cost_allowance"),
        ("Non-depreciable capital property", "non_depreciable_capital_property"),
        ("Deferred income plans", "deferred_income_plans"),
        ("Status change for the corporation", "status_change_for_corporation"),
    ]
    blank_rows: list[list[str]] = []
    for label, key in blank_screens:
        obj = ufile_screens.get(key, {}) if isinstance(ufile_screens, dict) else {}
        if not isinstance(obj, dict):
            continue
        has_any = None
        for flag_key in ("has_loss_carryforwards", "has_donations", "has_reserves", "has_cca", "has_property", "has_plans", "has_status_change"):
            if flag_key in obj:
                has_any = obj.get(flag_key)
                break
        blank_rows.append([label, yn(has_any) if has_any is not None else "No", str(obj.get("note") or "")])

    parts.append("## Other UFile screens (usually blank / check if applicable)")
    parts.append(md_table(["Screen", "Has entries?", "Note"], blank_rows))
    parts.append("")

    parts.append("## Schedule 100 (GIFI) — Balance sheet (enter these lines, whole dollars)")
    parts.append(
        "**Important:** If you complete the retained earnings rollforward (3660/3680/3700/3740), "
        "do **not** manually type retained earnings on Schedule 100 (`3600`)—UFile should populate it from the rollforward. "
        "Typing `3600` (or `3849`) can trigger BCR errors like “GIFI-FIELD 3849 does not match internal subtotal calculation.”"
    )
    parts.append("")
    schedule_100_rows = [r for r in rows_from_schedule(schedule_100) if r[0] != "3600"]
    parts.append(
        md_table(
            ["GIFI", "Description", "Amount", "Note"],
            [[c, lbl, money(amt), note] for c, lbl, amt, note in schedule_100_rows],
        )
    )
    parts.append("")

    parts.append("## Schedule 125 (GIFI) — Income statement (enter these lines, whole dollars)")
    # Insert cost-of-sales breakdown rows first so the operator fills opening/purchases/closing.
    cogs_rows = build_cogs_entry_rows()
    schedule_125_rows = rows_from_schedule(schedule_125)
    if cogs_rows:
        schedule_125_rows = cogs_rows + schedule_125_rows
    parts.append(
        md_table(
            ["GIFI", "Description", "Amount", "Note"],
            [[c, lbl, money(amt), note] for c, lbl, amt, note in schedule_125_rows],
        )
    )
    parts.append("")

    # Cost of sales tie-check (display-only)
    if "8518" in schedule_125 and "8519" in schedule_125:
        parts.append("## Cost of sales tie-check (display-only)")
        parts.append(
            md_table(
                ["GIFI", "Description", "Amount"],
                [
                    ["8518", "Cost of sales (expected)", money(int(schedule_125["8518"]["amount"]))],
                    ["8519", "Gross profit/loss (expected)", money(int(schedule_125["8519"]["amount"]))],
                ],
            )
        )
        parts.append("")

    # Tie-check totals (display-only)
    if "2599" in schedule_100 and "3640" in schedule_100:
        parts.append("## Tie-check (display-only totals)")
        parts.append(
            md_table(
                ["GIFI", "Description", "Amount"],
                [
                    ["1599", "Total current assets (expected)", money(int(schedule_100["2599"]["amount"]))],
                    ["2599", "Total assets", money(int(schedule_100["2599"]["amount"]))],
                    ["3640", "Total liabilities and shareholder equity", money(int(schedule_100["3640"]["amount"]))],
                ],
            )
        )
        parts.append("")

    parts.append("## Retained earnings (whole dollars)")
    parts.append(
        md_table(
            ["GIFI", "Description", "Amount", "Entry rule"],
            [
                ["3660", retained.get("3660", {}).get("label", ""), money(int(retained.get("3660", {}).get("amount", 0))), "Enter (opening RE)"],
                ["3680", retained.get("3680", {}).get("label", ""), money(int(retained.get("3680", {}).get("amount", 0))), "Enter (net income/loss)"],
                ["3700", retained.get("3700", {}).get("label", ""), money(int(retained.get("3700", {}).get("amount", 0))), "Enter (dividends declared)"],
                ["3740", retained.get("3740", {}).get("label", ""), money(int(retained.get("3740", {}).get("amount", 0))), "Enter only if needed (rounding/other)"],
                ["3849", retained.get("3849", {}).get("label", ""), money(int(retained.get("3849", {}).get("amount", 0))), "Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740)"],
            ],
        )
    )
    parts.append("")

    # Shareholder balances / loans support (working papers)
    sch100_due_from = int(schedule_100.get("1301", {}).get("amount") or 0)
    sch100_due_to = int(schedule_100.get("2781", {}).get("amount") or 0)
    due_from_breakdown_rows = [
        r
        for r in read_csv_rows(ACCOUNTING_OUTPUT_DIR / "due_from_shareholder_breakdown.csv")
        if date_in_fy((r.get("entry_date") or "").strip())
    ]
    if sch100_due_from or sch100_due_to or due_from_breakdown_rows:
        # Keep as a sub-heading so it stays inside the retained earnings section
        # (the final guide reorders sections and would otherwise drop unknown top-level headings).
        parts.append("### Shareholder loans / balances support (working papers)")
        parts.append(
            "CRA frequently asks for support for any due-from-shareholder / due-to-shareholder amounts. "
            "Keep the continuity below with your filing package."
        )
        parts.append("")
        parts.append("Evidence / working papers:")
        parts.append("- `output/due_from_shareholder_breakdown.md` (loan events + net due-from support)")
        parts.append("- `output/due_from_shareholder_breakdown.csv` (same data, machine-readable)")
        parts.append(f"- `output/trial_balance_{fy}.csv` (year-end balances by GL account)")
        parts.append("- `output/manual_adjustment_journal_detail.csv` (any year-end shareholder payable adjustments)")
        parts.append("")
        parts.append(
            f"Year-end summary (from Schedule 100): Due from shareholder (GIFI 1301) = {money(sch100_due_from)}; "
            f"Due to shareholder (GIFI 2781) = {money(sch100_due_to)}."
        )
        parts.append("")

        if due_from_breakdown_rows:
            loan_rows = [
                r
                for r in due_from_breakdown_rows
                if (r.get("bank_txn_category") or "").strip() in ("LOAN_ISSUED", "LOAN_REPAID")
            ]
            other_rows = [r for r in due_from_breakdown_rows if r not in loan_rows]

            parts.append("#### Loan events in this fiscal year (from `output/due_from_shareholder_breakdown.csv`)")
            if loan_rows:
                loan_event_table_rows: list[list[str]] = []
                for r in loan_rows:
                    net = (r.get("net") or "").strip()
                    try:
                        net_amt = float(net) if net else 0.0
                    except Exception:
                        net_amt = 0.0
                    loan_event_table_rows.append(
                        [
                            (r.get("entry_date") or "").strip(),
                            (r.get("shareholder") or "").strip(),
                            (r.get("bank_txn_category") or "").strip(),
                            f"{net_amt:,.2f}",
                            (r.get("journal_entry_id") or "").strip(),
                            (r.get("line_description") or r.get("bank_txn_explanation") or "").strip(),
                        ]
                    )
                parts.append(
                    md_table(
                        ["Date", "Shareholder", "Type", "Net", "Journal entry id", "Description"],
                        loan_event_table_rows,
                    )
                )
                parts.append("")
                parts.append(
                    "Note: a loan can be fully repaid within the year (netting to $0 at year-end) and still needs documentation."
                )
                parts.append("")
            else:
                parts.append("_(none)_")
                parts.append("")

            if other_rows:
                parts.append("#### Other due-from-shareholder components in this fiscal year")
                other_table_rows: list[list[str]] = []
                for r in other_rows:
                    net = (r.get("net") or "").strip()
                    try:
                        net_amt = float(net) if net else 0.0
                    except Exception:
                        net_amt = 0.0
                    other_table_rows.append(
                        [
                            (r.get("entry_date") or "").strip(),
                            (r.get("shareholder") or "").strip(),
                            (r.get("bank_txn_category") or "").strip(),
                            f"{net_amt:,.2f}",
                            (r.get("journal_entry_id") or "").strip(),
                            (r.get("line_description") or r.get("bank_txn_explanation") or "").strip(),
                        ]
                    )
                parts.append(
                    md_table(
                        ["Date", "Shareholder", "Type", "Net", "Journal entry id", "Description"],
                        other_table_rows,
                    )
                )
                parts.append("")
        else:
            parts.append("#### Loan events in this fiscal year")
            parts.append("_(none)_")
            parts.append("")

        # Provide year-end balances for the shareholder-related GL accounts (2400/2410/2500).
        tb_rows = read_csv_rows(ACCOUNTING_OUTPUT_DIR / f"trial_balance_{fy}.csv")
        shareholder_accts = {"2400": "Due to Shareholder - Thomas", "2410": "Due to Shareholder - Dwayne", "2500": "Due from shareholder"}
        tb_keep = [r for r in tb_rows if (r.get("account_code") or "").strip() in shareholder_accts]
        if tb_keep:
            parts.append("#### Year-end shareholder-related balances (from trial balance)")
            bal_rows: list[list[str]] = []
            for r in sorted(tb_keep, key=lambda x: (x.get("account_code") or "")):
                code = (r.get("account_code") or "").strip()
                debit = (r.get("debit") or "0").strip()
                credit = (r.get("credit") or "0").strip()
                net_cents = (r.get("net_cents") or "").strip()
                # Render as signed whole dollars for quick tie-back to Schedule 100.
                amt = 0
                try:
                    amt = int(round(int(net_cents) / 100)) if net_cents else 0
                except Exception:
                    amt = 0
                bal_rows.append(
                    [
                        code,
                        (r.get("account_name") or shareholder_accts.get(code) or "").strip(),
                        debit,
                        credit,
                        money(abs(amt)) + (" DR" if amt >= 0 else " CR"),
                    ]
                )
            parts.append(md_table(["Account", "Name", "Debit", "Credit", "Net (approx)"], bal_rows))
            parts.append("")

        # Mileage reimbursement support (working papers) — do not include in Notes to FS.
        payables_rows = read_csv_rows(ACCOUNTING_OUTPUT_DIR / f"shareholder_mileage_fuel_payables_{fy}.csv")
        thomas_row = None
        dwayne_row = None
        for r in payables_rows:
            if (r.get("shareholder") or "").strip() == "Thomas":
                thomas_row = r
            if (r.get("shareholder") or "").strip() == "Dwayne":
                dwayne_row = r
        if thomas_row or dwayne_row:
            parts.append("#### Shareholder mileage reimbursement (working papers)")
            parts.append("Keep this as working-paper support. Do **not** paste mileage details into Notes to the financial statements.")
            parts.append("")
            parts.append("Evidence / working papers:")
            parts.append("- `output/shareholder_mileage_fuel_summary.md` (human summary)")
            parts.append(f"- `output/shareholder_mileage_fuel_payables_{fy}.csv` (FY totals: mileage, fuel, net)")
            parts.append("- `output/fuel_9200_wave_bills.csv` (fuel detail by bill)")
            parts.append("- `output/mileage_adjustment_summary.md` (documents FY-scoped overlays, if any)")
            parts.append("")
            rows: list[list[str]] = []
            if thomas_row:
                try:
                    th_mileage = int(thomas_row.get("mileage_claim_cents") or 0)
                    th_fuel = int(thomas_row.get("fuel_cents") or 0)
                    th_net = int(thomas_row.get("net_cents") or 0)
                    th_dir = (thomas_row.get("direction") or "").strip()
                except Exception:
                    th_mileage = th_fuel = th_net = 0
                    th_dir = ""
                rows.append(
                    [
                        "Thomas",
                        f"${th_mileage/100:,.2f}",
                        f"${th_fuel/100:,.2f}",
                        f"${abs(th_net)/100:,.2f}",
                        "due to Thomas" if th_dir == "DUE_TO_SHAREHOLDER" else "due from Thomas" if th_dir == "DUE_FROM_SHAREHOLDER" else "",
                    ]
                )
            if dwayne_row:
                try:
                    dw_mileage = int(dwayne_row.get("mileage_claim_cents") or 0)
                except Exception:
                    dw_mileage = 0
                rows.append(["Dwayne", f"${dw_mileage/100:,.2f}", "$0.00", f"${dw_mileage/100:,.2f}", "due to Dwayne"])
            parts.append(md_table(["Shareholder", "Mileage", "Fuel offset", "Net", "Direction"], rows))
            parts.append("")

        parts.append(
            "UFile entry tip: do not enter both `2780` and `2781` for the same payable; that double-counts and can break Schedule 100 totals."
        )
        parts.append("")

    parts.append("## Schedule 1 (tax purposes)")
    parts.append(
        md_table(
            ["Code", "Description", "Amount", "Calculation"],
            [
                [line, obj.get("label", ""), money(int(obj["amount"])), obj.get("calculation", "") or ""]
                for line, obj in sorted(schedule_1.items(), key=lambda kv: schedule_1_sort_key(kv[0]))
            ],
        )
    )
    parts.append(
        "Note: If UFile auto-populates Schedule 1 line 403 from Schedule 8, do **not** manually enter 403 in the Schedule 1 grid."
    )
    schedule_8 = year.get("schedule_8", {}) if isinstance(year.get("schedule_8"), dict) else {}
    total_cca_claim = 0
    if isinstance(schedule_8.get("summary"), dict):
        total_cca_claim = int(schedule_8.get("summary", {}).get("total_cca_claim") or 0)
    if total_cca_claim:
        parts.append(
            f"CCA is entered on the **Capital cost allowance** screen from Schedule 8 (total CCA claimed: {money(total_cca_claim)})."
        )
    parts.append("")

    book_fixed_assets = year.get("book_fixed_assets", []) if isinstance(year.get("book_fixed_assets"), list) else []
    if book_fixed_assets:
        parts.append("## Fixed assets (book)")
        rows = []
        for asset in book_fixed_assets:
            rows.append(
                [
                    str(asset.get("asset_id") or ""),
                    str(asset.get("description") or ""),
                    str(asset.get("book_start_date") or ""),
                    money(int(asset.get("total_cost_dollars") or 0)),
                    money(int(asset.get("reclass_total_dollars") or 0)),
                    money(int(asset.get("amortization_dollars") or 0)),
                    str(asset.get("book_depr_policy") or ""),
                    str(asset.get("component_breakdown") or ""),
                ]
            )
        parts.append(
            md_table(
                ["Asset ID", "Description", "Book start", "Cost", "Reclass", "Amortization", "Policy", "Components"],
                rows,
            )
        )
        parts.append("")

    if schedule_8 and isinstance(schedule_8.get("classes"), dict) and schedule_8["classes"]:
        parts.append("## Schedule 8 / CCA")
        classes = schedule_8.get("classes", {}) if isinstance(schedule_8.get("classes"), dict) else {}
        class_rows = []
        for class_code, obj in sorted(classes.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 10**9):
            class_rows.append(
                [
                    class_code,
                    str(obj.get("description") or ""),
                    money(int(obj.get("opening_ucc") or 0)),
                    money(int(obj.get("additions") or 0)),
                    money(int(obj.get("cca_claim") or 0)),
                    money(int(obj.get("closing_ucc") or 0)),
                ]
            )
        parts.append(
            md_table(
                ["Class", "Description", "Opening UCC", "Additions", "CCA claim", "Closing UCC"],
                class_rows,
            )
        )
        parts.append("")

        assets = schedule_8.get("assets", []) if isinstance(schedule_8.get("assets"), list) else []
        if assets:
            asset_rows = []
            for asset in assets:
                asset_rows.append(
                    [
                        str(asset.get("asset_id") or ""),
                        str(asset.get("description") or ""),
                        str(asset.get("available_for_use_date") or ""),
                        str(asset.get("cca_class") or ""),
                        money(int(asset.get("total_cost_dollars") or 0)),
                    ]
                )
            parts.append("### Schedule 8 asset additions (audit trail)")
            parts.append(md_table(["Asset ID", "Description", "Date", "Class", "Cost"], asset_rows))
            parts.append("")

            # UFile's CCA UI is class-based, but the operator often enters additions per asset line.
            # Keep a tiny copy/paste checklist with the exact data we have (no dispositions expected).
            ufile_rows = []
            for asset in assets:
                ufile_rows.append(
                    [
                        str(asset.get("cca_class") or ""),
                        str(asset.get("description") or ""),
                        str(asset.get("available_for_use_date") or ""),
                        money(int(asset.get("total_cost_dollars") or 0)),
                        "0",
                        "",
                    ]
                )
            parts.append("### UFile Schedule 8 entry lines (per asset)")
            parts.append(
                md_table(
                    ["Class", "Addition description", "Date acquired/available", "Cost", "Proceeds (if disposed)", "Disposed description (if any)"],
                    ufile_rows,
                )
            )
            parts.append("")

    # High-signal yes/no answers that differ year-to-year
    parts.append("## High-signal yes/no answers")
    pos = year.get("positions", {})
    keys = [
        ("first_time_filer_after_incorp_line_070", "T2 line 070 (first year after incorporation)"),
        ("internet_income_line_180", "T2 line 180 (internet income/websites)"),
        ("net_income_diff_line_201", "T2 line 201 (book vs tax net income differs)"),
        ("cca_required", "CCA required / capital assets"),
        ("book_fixed_assets_present", "Book fixed assets present"),
    ]
    rows = []
    for k, label in keys:
        if k in pos:
            v = pos[k]["value"]
            vv = "Yes" if v is True else "No" if v is False else str(v)
            rows.append([label, vv, pos[k].get("note", "")])
    parts.append(md_table(["Question", "Answer", "Note"], rows))
    parts.append("")

    draft = "\n".join(parts).strip() + "\n"

    def section_block(title: str, body: str) -> str:
        body = body.rstrip()
        return f"## {title}\n{body}\n\n" if body else f"## {title}\n_(none)_\n\n"

    def split_sections(text: str) -> tuple[str, dict[str, str]]:
        prefix = text.split("## ", 1)[0]
        sections: dict[str, str] = {}
        for m in re.finditer(r"(?ms)^## ([^\n]+)\n(.*?)(?=^## |\Z)", text):
            heading = m.group(1).strip()
            body = m.group(2).rstrip() + "\n"
            sections[heading] = body
        return prefix, sections

    prefix, sections = split_sections(draft)

    # If we can't find the core sections, fall back to the draft.
    if "Identification of the corporation (UFile screen)" not in sections:
        return draft

    gifi_raw = sections.get("GIFI form / notes (UFile screens)", "")
    if "### Notes checklist" in gifi_raw:
        gifi_intro, notes_block = gifi_raw.split("### Notes checklist", 1)
        gifi_intro = gifi_intro.rstrip() + "\n"
        notes_block = "### Notes checklist" + notes_block
    else:
        gifi_intro = gifi_raw
        notes_block = ""
    if notes_block.startswith("### Notes checklist"):
        notes_block = notes_block.replace("### Notes checklist", "### Checklist", 1)

    # Provide paste-ready notes to financial statements (working-paper friendly).
    # UFile's "Notes checklist" screen doesn't require text entry, but having a standard notes draft
    # prevents follow-up questions when a reviewer expects basic disclosures (inventory, shareholder balances, cap assets).
    end_date_str = period["end"]
    try:
        end_date_pretty = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%B %d, %Y")
    except Exception:
        end_date_pretty = end_date_str
    legal_name = entity.get("legal_name") or ""
    operating_name = entity.get("operating_name") or ""
    activity = ""
    ident = ufile_screens.get("identification_of_corporation", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(ident, dict) and ident.get("activity_description"):
        activity = str(ident.get("activity_description") or "")
    if not activity:
        # Keep this generic if not explicitly provided in the packet.
        activity = "canteen / concession operations"

    # Keep inventory disclosure year-specific:
    # - FY2024: management estimate (first-year; no formal count process yet)
    # - FY2025+: physical count process exists (for this project: first count was near FY2025 year-end)
    inventory_note = ""
    if fy == "FY2024":
        inventory_note = (
            " For FY2024, a formal physical inventory count process was implemented in the subsequent fiscal year; "
            "accordingly, the inventory balance at May 31, 2024 was estimated by management using an itemized schedule at cost."
        )
    elif fy == "FY2025":
        inventory_note = (
            " The inventory balance at May 31, 2025 is based on a physical count performed near year-end "
            "(May 16, 2025) and management adjustments for immaterial movements through year-end."
        )

    fs_notes = f"""```text
{legal_name}{' (' + operating_name + ')' if operating_name else ''}
Notes to the financial statements
Year ended {end_date_pretty}

1. Nature of operations
The corporation carries on {activity}.

2. Basis of presentation
These financial statements have been prepared on the accrual basis of accounting using the historical cost basis.

3. Revenue recognition
Revenue is recognized at the time goods are sold and services are rendered. Amounts are presented net of refunds and discounts.

4. Inventory
Inventory consists of food and beverage inventory held for resale and is valued at the lower of cost and net realizable value.{inventory_note}

5. Property and equipment
Property and equipment are recorded at cost. Amortization is provided on a basis intended to approximate the decline in service potential of the related assets.

6. Income taxes and government remittances
The corporation is a Canadian-controlled private corporation. Income tax expense comprises current tax. Taxes payable on the balance sheet may include GST/HST and other government remittances.

7. Related party transactions and balances
The corporation is controlled by its shareholders. Amounts due to/from shareholders relate primarily to shareholder-paid business expenses and reimbursements and other amounts payable to shareholders. These balances are non-interest-bearing and due on demand unless otherwise agreed.

8. Subsequent events
There have been no subsequent events requiring adjustment to these financial statements.
```"""

    if notes_block:
        notes_block = notes_block.rstrip() + "\n\n### Notes to financial statements (copy/paste)\n" + fs_notes + "\n"
    else:
        notes_block = "### Notes to financial statements (copy/paste)\n" + fs_notes + "\n"

    balance_body = sections.get("Schedule 100 (GIFI) — Balance sheet (enter these lines, whole dollars)", "")
    retained_body = sections.get("Retained earnings (whole dollars)", "")
    tie_body = sections.get("Tie-check (display-only totals)", "")
    fixed_assets_body = sections.get("Fixed assets (book)", "")
    if fixed_assets_body:
        balance_body = balance_body.rstrip() + "\n\n### Fixed assets (book)\n" + fixed_assets_body.strip() + "\n"
    if retained_body:
        balance_body = balance_body.rstrip() + "\n\n### Retained earnings (whole dollars)\n" + retained_body.strip() + "\n"
    if tie_body:
        balance_body = balance_body.rstrip() + "\n\n### Tie-check (display-only totals)\n" + tie_body.strip() + "\n"

    income_body = sections.get("Schedule 125 (GIFI) — Income statement (enter these lines, whole dollars)", "")
    cogs_body = sections.get("Cost of sales tie-check (display-only)", "")
    if cogs_body:
        income_body = income_body.rstrip() + "\n\n### Cost of sales tie-check (display-only)\n" + cogs_body.strip() + "\n"

    income_source_body = (
        "Goal: avoid the UFile warning `INCOMESOURCE` and make the return explicit.\n\n"
        "- In UFile \u2192 **Income source** screen:\n"
        "  - Select **Active business income**.\n"
        "  - Leave **property**, **foreign**, and other income sources unchecked unless you have real amounts.\n"
        "  - Save and re-run diagnostics to confirm the warning clears.\n\n"
        "Expected source for this file: **active business income only** (canteen operations).\n\n"
    )
    schedule_1_body = sections.get("Schedule 1 (tax purposes)", "")
    if schedule_1_body:
        income_source_body += "### Schedule 1 (tax purposes)\n" + schedule_1_body.strip() + "\n\n"
    # Schedule 7 is generated by UFile when the small business deduction (SBD) logic is completed.
    # It is easy to accidentally omit by missing a checkbox/screen, which leads to exports that look incomplete.
    if fy in ("FY2024", "FY2025"):
        income_source_body += (
            "### Small business deduction (Schedule 7)\n"
            "For a CCPC with active business income and positive taxable income, Schedule 7 is typically expected.\n\n"
            "- In UFile, make sure the **small business deduction** section is completed (CCPC = Yes, no associated corps unless real).\n"
            "- After your next PDF export, confirm the package includes **T2 SCH 7** (run the completeness checker in the Must-check section).\n\n"
        )
    high_signal_body = sections.get("High-signal yes/no answers", "")
    if high_signal_body:
        income_source_body += "### High-signal yes/no answers\n" + high_signal_body.strip() + "\n\n"

    cca_body = (
        "Use Schedule 8 outputs; enter class details if claiming CCA.\n\n"
        "If this section is missing/empty in the guide, the packet was likely built from a snapshot that did not include\n"
        "`schedule_8_*.csv`. Rebuild via:\n"
        "`python3 UfileToFill/ufile_packet/tools/refresh_packet_from_current_state.py`\n\n"
    )
    schedule_8_body = sections.get("Schedule 8 / CCA", "")
    if schedule_8_body:
        cca_body += "### Schedule 8 / CCA\n" + schedule_8_body.strip() + "\n\n"

    out: list[str] = []
    out.append(prefix)
    for heading in [
        "UFile entry rules (important)",
        "If something looks wrong in UFile (fast troubleshooting)",
        "Key carryforward fields (match 2023 filing)",
        "Key positions / elections (high signal)",
        "Must-check before filing / exporting a PDF copy",
    ]:
        out.append(section_block(heading, sections.get(heading, "")))

    out.append(section_block("Identification of the corporation (UFile screen)", sections.get("Identification of the corporation (UFile screen)", "")))
    out.append(section_block("Tax preparer (UFile screen)", sections.get("Tax preparer (UFile screen)", "")))
    out.append(section_block("EFILE setup (UFile screen)", "Leave default settings unless you are explicitly instructed to change EFILE options."))
    out.append(section_block("Head office address (UFile screen)", sections.get("Head office address (UFile screen)", "")))
    out.append(section_block("Other addresses (UFile screen)", sections.get("Location of books & records (UFile screen)", "")))
    out.append(section_block("Mailing address of the corporation (UFile screen)", sections.get("Mailing address (UFile screen)", "")))
    out.append(section_block("Corporate officers (UFile screen)", sections.get("Corporate officers / directors (UFile screen)", "")))
    out.append(section_block("Director (UFile screen)", "Use the same director details as listed under **Corporate officers**."))
    out.append(section_block("Director and signing officer (UFile screen)", "Signing officer is **Dwayne Ripley** (see Corporate officers table)."))
    out.append(section_block("GIFI Import (UFile screen)", "If using a GIFI import file, import once before manual edits; otherwise skip this screen."))
    out.append(section_block("GIFI (UFile screen)", gifi_intro))
    out.append(section_block("Balance sheet (GIFI Schedule 100)", balance_body))
    out.append(section_block("Income statement (GIFI Schedule 125)", income_body))
    out.append(section_block("Notes checklist (UFile screen)", notes_block))
    out.append(section_block("Net income (UFile screen)", sections.get("Net income (UFile screen)", "")))
    out.append(section_block("Tax on capital (UFile screen)", sections.get("Tax on capital (UFile screen)", "")))
    out.append(section_block("Status change for the corporation (UFile screen)", "No status change; leave blank."))
    out.append(section_block("Charitable donations (UFile screen)", "No charitable donations claimed."))
    out.append(section_block("Non-depreciable capital property (UFile screen)", "No non-depreciable capital property."))
    out.append(section_block("Income source (UFile screen)", income_source_body.strip()))
    if "Dividends paid (UFile screen)" in sections:
        out.append(section_block("Dividends paid (UFile screen)", sections.get("Dividends paid (UFile screen)", "")))
    else:
        out.append(section_block("Dividends paid (UFile screen)", "No dividends declared or paid."))
    # In UFile, "Taxable dividend paid" is a child screen under Dividends paid and is where
    # Schedule 3 / Schedule 55 are actually driven. Only show it as "None" when there are
    # no dividends; otherwise, provide explicit entry guidance.
    dividends_screen = ufile_screens.get("dividends_paid", {}) if isinstance(ufile_screens, dict) else {}
    if isinstance(dividends_screen, dict) and dividends_screen.get("has_dividends"):
        taxable_div_amt = money(int(dividends_screen.get("taxable_dividends_paid") or 0))
        eligible_amt = money(int(dividends_screen.get("eligible_dividend_portion") or 0))
        taxable_div_body = (
            "Enter the taxable dividends paid details so Schedule 3 / Schedule 55 match the retained earnings rollforward.\n\n"
            f"- Total taxable dividends paid in the tax year: **{taxable_div_amt}**\n"
            f"- Eligible portion: **{eligible_amt}** (default expectation: $0 = non-eligible)\n\n"
            "If UFile asks you to split between connected vs non-connected corporations, "
            "and these dividends were paid to individuals (shareholders), treat them as **other than connected corporations**.\n"
        )
        out.append(section_block("Taxable dividend paid (UFile screen)", taxable_div_body))
    else:
        out.append(section_block("Taxable dividend paid (UFile screen)", "None."))
    out.append(section_block("General rate income pool (GRIP) (UFile screen)", sections.get("General rate income pool (GRIP) (UFile screen)", "")))
    out.append(section_block("Capital cost allowance (UFile screen)", cca_body.strip()))
    out.append(section_block("Loss carry forwards and loss carry backs (UFile screen)", "No losses to carry forward/back."))
    out.append(section_block("Reserves (UFile screen)", "No reserves claimed."))
    out.append(section_block("Deferred income plans (UFile screen)", "No deferred income plans."))
    out.append(
        section_block(
            "Transaction with shareholders, officers, or employees (UFile screen)",
            sections.get("Transactions with shareholders/officers/employees (UFile disclosure)", ""),
        )
    )
    out.append(section_block("Annual return (UFile screen)", "Complete if UFile requires it; no special entries in this packet."))
    out.append(section_block("Instalments paid (UFile screen)", "Leave blank unless you have instalment records to enter."))
    out.append(section_block("Refund or balance owing (UFile screen)", sections.get("Refund or balance owing (UFile screen)", "")))
    out.append(section_block("Capital dividend account (UFile screen)", "No capital dividend account activity."))
    out.append(
        section_block(
            "Corporate history (UFile screen)",
            sections.get("Corporate history carryforward (UFile screen)", ""),
        )
    )

    return "".join(out).rstrip() + "\n"


def write_year_tables(packet: dict, fy: str) -> None:
    """
    Keep `UfileToFill/ufile_packet/tables/` in sync with the current packet.

    These CSVs are intentionally simple and are used for quick review, evidence references,
    and downstream prompts that want structured inputs.
    """

    year = packet["years"][fy]
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    def write_schedule(path: Path, schedule: dict) -> None:
        with path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["GIFI_Code", "Description", "Amount", "Note"])
            for code, obj in sorted(schedule.items(), key=lambda kv: int(kv[0])):
                if not isinstance(obj, dict):
                    continue
                desc = obj.get("label", "") or ""
                amount = int(obj.get("amount", 0) or 0)
                note = obj.get("note", "") or ""
                w.writerow([int(code), desc, amount, note])

    def write_schedule_1(path: Path, schedule_1: dict) -> None:
        with path.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Code", "Description", "Amount", "Calculation"])
            for line, obj in sorted(schedule_1.items(), key=lambda kv: schedule_1_sort_key(kv[0])):
                if not isinstance(obj, dict):
                    continue
                desc = obj.get("label", "") or ""
                amount = int(obj.get("amount", 0) or 0)
                calc = obj.get("calculation", "") or ""
                w.writerow([str(line), desc, amount, calc])

    write_schedule(TABLES_DIR / f"schedule_100_{fy}.csv", year.get("schedule_100", {}))
    write_schedule(TABLES_DIR / f"schedule_125_{fy}.csv", year.get("schedule_125", {}))
    write_schedule_1(TABLES_DIR / f"schedule_1_{fy}.csv", year.get("schedule_1", {}))


def main() -> int:
    packet = json.loads(PACKET_PATH.read_text())
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for fy in sorted(packet["years"].keys()):
        year_dir = OUT_DIR / fy
        year_dir.mkdir(parents=True, exist_ok=True)

        (year_dir / "packet.json").write_text(json.dumps(build_year_packet(packet, fy), indent=2, sort_keys=False) + "\n")
        md_guide = build_year_guide(packet, fy)
        (year_dir / "UFILet2_FILL_GUIDE.md").write_text(md_guide)
        (year_dir / "UFILet2_FILL_GUIDE.html").write_text(render_year_guide_html(packet, fy, md_guide=md_guide))
        write_year_tables(packet, fy)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
