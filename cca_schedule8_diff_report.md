commit ffb80be917a49f5e0ef173909fd8eb2b54fbd80b
Author: Thomas McCrossin <thomas.mccrossin@outlook.com>
Date:   Fri Jan 30 23:25:58 2026 +0000

    Add CCA Schedule 8 layer and modernize Schedule 1

diff --git a/UfileToFill/ufile_packet/UFILet2_UFILE_COPYPASTE_REVIEW.md b/UfileToFill/ufile_packet/UFILet2_UFILE_COPYPASTE_REVIEW.md
index 713d90b..c7df051 100644
--- a/UfileToFill/ufile_packet/UFILet2_UFILE_COPYPASTE_REVIEW.md
+++ b/UfileToFill/ufile_packet/UFILet2_UFILE_COPYPASTE_REVIEW.md
@@ -198,7 +198,7 @@ Recommended minimal entries:
   - End date: **2023-05-31**
   - Taxable paid-up capital: **$100** (share capital exists; small and consistent)
 - For FY2025 “1st prior year” = FY2024 (ends 2024-05-31):
-  - Taxable income: **$16,985** (Schedule 1 line 400 FY2024)
+  - Taxable income: **$16,985** (Schedule 1 code C FY2024)
   - End date: **2024-05-31**
   - Taxable paid-up capital: **$100**
 
@@ -220,7 +220,7 @@ Expected for your file:
 - Losses: **none**
 - Reserves: **none**
 - Donations: **none**
-- CCA: **none** (you are not capitalizing assets in these years; expensing under threshold)
+- CCA: **see Schedule 8 outputs** (capital items can be expensed in books but claimed for tax via Schedule 8)
 
 Only fill these screens if you truly have these items.
 
@@ -264,7 +264,7 @@ This is the minimal “shape” you should expect for these returns in UFile:
 - Schedule 50 (shareholders >10%): **Yes**
 - Internet income/websites (T2 line 180): **Yes** → UFile will typically want the internet schedule/details (often referred to as “Schedule 88” in the T2 form attachments list)
 - First year after incorporation (T2 line 070 / Schedule 24): **No** (already filed in the 2023 stub return)
-- CCA / Schedule 8: **No** (no capital assets capitalized)
+- CCA / Schedule 8: **Check Schedule 8 outputs** (CCA claimed when asset register has additions)
 - Losses: **No**
 
 **FY2025**
diff --git a/UfileToFill/ufile_packet/diffs/COMPARE_2023_FILED_VS_PACKET.md b/UfileToFill/ufile_packet/diffs/COMPARE_2023_FILED_VS_PACKET.md
index 0a8573c..3bf616f 100644
--- a/UfileToFill/ufile_packet/diffs/COMPARE_2023_FILED_VS_PACKET.md
+++ b/UfileToFill/ufile_packet/diffs/COMPARE_2023_FILED_VS_PACKET.md
@@ -69,7 +69,7 @@ The 2023 filed return was a **nil return** for the stub period (2022-12-08 to 20
 
 | Field | 2023 Filed Value |
 |-------|------------------|
-| Net income (line 300) | $0 |
+| Net income (Schedule 1 code A) | $0 |
 | Taxable income (line 360) | $0 |
 | Part I tax payable (line 700) | $0 |
 | Business limit (line 410) | $239,726 |
@@ -119,7 +119,7 @@ The 2023 filed return was a **nil return** for the stub period (2022-12-08 to 20
 | First year after incorporation? (T2 line 070) | Yes | No (FY2024/FY2025) | 2023 stub already filed as first-time filer (Schedule 24) |
 | Internet income (line 180)? | No | Yes (implied by Shopify sales) | New activity |
 | Schedule 1 differences (line 201)? | No | Yes (meals add-back, penalties) | Active year has adjustments |
-| Net income (line 300) | $0 | $16,655 (FY2024), $28,349 (FY2025) | Expected: active operations |
+| Net income (Schedule 1 code A) | $0 | $16,655 (FY2024), $28,349 (FY2025) | Expected: active operations |
 | Taxable income (line 360) | $0 | $16,985 (FY2024), $28,827 (FY2025) | Expected: active operations |
 | Schedule 100/125 attached? | No | Yes | Expected: active year requires GIFI |
 | Business limit (line 410) | $239,726 (prorated 175 days) | $500,000 (full year) | Expected: full year limit |
diff --git a/UfileToFill/ufile_packet/guides/UFILE_FILING_COMPLETENESS_CHECKLIST.md b/UfileToFill/ufile_packet/guides/UFILE_FILING_COMPLETENESS_CHECKLIST.md
index 1b7fcc1..fcf1ee1 100644
--- a/UfileToFill/ufile_packet/guides/UFILE_FILING_COMPLETENESS_CHECKLIST.md
+++ b/UfileToFill/ufile_packet/guides/UFILE_FILING_COMPLETENESS_CHECKLIST.md
@@ -52,7 +52,7 @@ Fix:
 ### Corporate history (prior-year carryforward)
 UFile’s “Corporate History” screen can require a minimal “1st prior year” row:
 - Prior year end date
-- Prior year taxable income (Schedule 1 line 400 of prior year)
+- Prior year taxable income (Schedule 1 code C of prior year)
 - Taxable paid-up capital (generally matches share capital for this file)
 
 The year fill guides include a ready-to-type “Corporate history carryforward” table.
@@ -66,12 +66,12 @@ The packet explicitly models these as “No”, with notes:
 - Loss carryforwards/carrybacks
 - Charitable donations
 - Reserves
-- CCA / depreciable property
+- CCA / depreciable property (check Schedule 8 outputs)
 - Non-depreciable capital property
 - Deferred income plans
 - Status change for the corporation
 
-If UFile forces a yes/no toggle on these screens, answer “No” and leave detail grids empty.
+If UFile forces a yes/no toggle on these screens, answer “No” and leave detail grids empty **unless** Schedule 8 / CCA is present in the packet.
 
 ## 3) Data entry rule that prevents most problems
 
@@ -81,4 +81,3 @@ Enter amounts on **detail lines**, not summary lines:
 - Revenue: enter `8000` (do not enter `8299`)
 - COGS: enter `8300/8320/8500` (let UFile derive `8518`)
 - Shareholder payable: use `2781` (if rejected, use `2780` as a fallback)
-
diff --git a/UfileToFill/ufile_packet/packet.json b/UfileToFill/ufile_packet/packet.json
index 451cb25..728ab86 100644
--- a/UfileToFill/ufile_packet/packet.json
+++ b/UfileToFill/ufile_packet/packet.json
@@ -1,6 +1,6 @@
 {
   "meta": {
-    "schema_version": "1.1.0",
+    "schema_version": "1.2.0",
     "generated_at": "2026-01-30T21:16:47Z",
     "snapshot_source": "output/snapshots/20260130-221500/output/",
     "generator": "tools/build_packet_from_snapshot.py",
diff --git a/UfileToFill/ufile_packet/prompts/PROMPT_BUILD_PACKET.md b/UfileToFill/ufile_packet/prompts/PROMPT_BUILD_PACKET.md
index 9ed70b5..9c21c16 100644
--- a/UfileToFill/ufile_packet/prompts/PROMPT_BUILD_PACKET.md
+++ b/UfileToFill/ufile_packet/prompts/PROMPT_BUILD_PACKET.md
@@ -73,7 +73,7 @@ Before finalizing, verify:
 1. Total Assets (2599) = Total L+E (3640) for each year
 2. RE End = RE Start + NI - Dividends +/- Other
 3. Net Income (9999) = Revenue (8299) - Expenses (9368)
-4. Schedule 1 line 400 = line 300 + additions - deductions
+4. Schedule 1 code C = code A + additions - deductions
 5. All GIFI codes exist in standard CRA GIFI list
 
 ## DO NOT
diff --git a/UfileToFill/ufile_packet/prompts/PROMPT_PRE_FILE_REVIEW.md b/UfileToFill/ufile_packet/prompts/PROMPT_PRE_FILE_REVIEW.md
index 1342714..6376942 100644
--- a/UfileToFill/ufile_packet/prompts/PROMPT_PRE_FILE_REVIEW.md
+++ b/UfileToFill/ufile_packet/prompts/PROMPT_PRE_FILE_REVIEW.md
@@ -27,7 +27,7 @@ For each fiscal year, verify:
 - [ ] Assets (2599) = Liabilities + Equity (3640)
 - [ ] Retained Earnings flow: Start + NI - Dividends +/- Other = End
 - [ ] Net Income: Revenue - Expenses = Net Income
-- [ ] Schedule 1: Line 300 + Add-backs - Deductions = Line 400
+- [ ] Schedule 1: Code A + Additions - Deductions = Code C
 - [ ] Gross profit: Revenue - COGS = Gross Profit
 
 ### B. Year-over-Year Consistency
diff --git a/UfileToFill/ufile_packet/schema/packet_schema.json b/UfileToFill/ufile_packet/schema/packet_schema.json
index 3fb623e..f8b7022 100644
--- a/UfileToFill/ufile_packet/schema/packet_schema.json
+++ b/UfileToFill/ufile_packet/schema/packet_schema.json
@@ -257,19 +257,69 @@
               }
             }
           },
-          "schedule_1": {
-            "type": "object",
-            "description": "Net Income Reconciliation for Tax Purposes",
-            "additionalProperties": {
-              "type": "object",
-              "required": ["amount"],
-              "properties": {
-                "amount": { "type": "integer" },
-                "label": { "type": "string" },
-                "calculation": { "type": ["string", "null"], "description": "How this was derived" }
-              }
-            }
-          },
+          "schedule_1": {
+            "type": "object",
+            "description": "Net Income Reconciliation for Tax Purposes",
+            "additionalProperties": {
+              "type": "object",
+              "required": ["amount"],
+              "properties": {
+                "amount": { "type": "integer" },
+                "label": { "type": "string" },
+                "calculation": { "type": ["string", "null"], "description": "How this was derived" }
+              }
+            }
+          },
+          "schedule_8": {
+            "type": "object",
+            "description": "Capital Cost Allowance (Schedule 8)",
+            "properties": {
+              "classes": {
+                "type": "object",
+                "additionalProperties": {
+                  "type": "object",
+                  "required": ["class", "opening_ucc", "additions", "cca_claim", "closing_ucc"],
+                  "properties": {
+                    "class": { "type": "string" },
+                    "description": { "type": ["string", "null"] },
+                    "rate": { "type": ["number", "null"] },
+                    "opening_ucc": { "type": "integer" },
+                    "additions": { "type": "integer" },
+                    "dispositions": { "type": "integer" },
+                    "half_year_base": { "type": "integer" },
+                    "cca_claim": { "type": "integer" },
+                    "closing_ucc": { "type": "integer" }
+                  }
+                }
+              },
+              "assets": {
+                "type": "array",
+                "items": {
+                  "type": "object",
+                  "properties": {
+                    "asset_id": { "type": "string" },
+                    "description": { "type": ["string", "null"] },
+                    "cca_class": { "type": ["string", "null"] },
+                    "available_for_use_date": { "type": ["string", "null"], "format": "date" },
+                    "total_cost_cents": { "type": ["integer", "null"] },
+                    "total_cost_dollars": { "type": ["integer", "null"] },
+                    "claim_percent_of_max": { "type": ["string", "null"] },
+                    "half_year_rule": { "type": ["string", "null"] },
+                    "source_breakdown": { "type": ["string", "null"] }
+                  }
+                }
+              },
+              "summary": {
+                "type": "object",
+                "properties": {
+                  "total_additions": { "type": "integer" },
+                  "total_cca_claim": { "type": "integer" },
+                  "classes_used": { "type": "array", "items": { "type": "string" } }
+                }
+              },
+              "note": { "type": ["string", "null"] }
+            }
+          },
           "positions": {
             "type": "object",
             "description": "Key tax positions and accounting policies for this year",
diff --git a/UfileToFill/ufile_packet/tools/build_packet_from_snapshot.py b/UfileToFill/ufile_packet/tools/build_packet_from_snapshot.py
index c35b228..59be5ec 100644
--- a/UfileToFill/ufile_packet/tools/build_packet_from_snapshot.py
+++ b/UfileToFill/ufile_packet/tools/build_packet_from_snapshot.py
@@ -85,15 +85,65 @@ def load_schedule_1_labels(path: Path) -> dict[str, str]:
     with path.open(newline="") as f:
         reader = csv.DictReader(f)
         for row in reader:
-            line = (row.get("Line") or row.get("line") or "").strip()
-            if not line:
+            code = (row.get("Code") or row.get("Line") or row.get("line") or "").strip()
+            if not code:
                 continue
-            d = (row.get("Description") or row.get("description") or "").strip()
+            d = (row.get("Label") or row.get("Description") or row.get("description") or "").strip()
             if d:
-                labels[line] = d
+                labels[code] = d
     return labels
 
 
+def load_schedule_8(path: Path) -> dict[str, dict]:
+    if not path.exists():
+        return {}
+    rows: dict[str, dict] = {}
+    with path.open(newline="") as f:
+        reader = csv.DictReader(f)
+        for row in reader:
+            class_code = str(row.get("Class") or row.get("class") or "").strip()
+            if not class_code:
+                continue
+            rows[class_code] = {
+                "class": class_code,
+                "description": str(row.get("Description") or "").strip(),
+                "rate": float(row.get("Rate") or 0),
+                "opening_ucc": int(row.get("Opening_UCC") or 0),
+                "additions": int(row.get("Additions") or 0),
+                "dispositions": int(row.get("Dispositions") or 0),
+                "half_year_base": int(row.get("Half_year_base") or 0),
+                "cca_claim": int(row.get("CCA_Claim") or 0),
+                "closing_ucc": int(row.get("Closing_UCC") or 0),
+            }
+    return rows
+
+
+def load_cca_assets(path: Path, fy: str) -> list[dict]:
+    if not path.exists():
+        return []
+    out: list[dict] = []
+    with path.open(newline="") as f:
+        reader = csv.DictReader(f)
+        for row in reader:
+            row_fy = str(row.get("fiscal_year") or "").strip()
+            if row_fy != fy:
+                continue
+            out.append(
+                {
+                    "asset_id": str(row.get("asset_id") or "").strip(),
+                    "description": str(row.get("description") or "").strip(),
+                    "cca_class": str(row.get("cca_class") or "").strip(),
+                    "available_for_use_date": str(row.get("available_for_use_date") or "").strip(),
+                    "total_cost_cents": int(row.get("total_cost_cents") or 0),
+                    "total_cost_dollars": int(row.get("total_cost_dollars") or 0),
+                    "claim_percent_of_max": str(row.get("claim_percent_of_max") or "").strip(),
+                    "half_year_rule": str(row.get("half_year_rule") or "").strip(),
+                    "source_breakdown": str(row.get("source_breakdown") or "").strip(),
+                }
+            )
+    return out
+
+
 def update_year_section(
     packet: dict,
     *,
@@ -121,7 +171,7 @@ def update_year_section(
     sch100 = load_csv_amounts(sch100_path, code_field_candidates=["gifi_code", "GIFI_Code"], amount_field_candidates=["amount", "Amount"])
     sch125 = load_csv_amounts(sch125_path, code_field_candidates=["gifi_code", "GIFI_Code"], amount_field_candidates=["amount", "Amount"])
     retained = load_csv_amounts(re_path, code_field_candidates=["gifi_code", "GIFI_Code"], amount_field_candidates=["amount", "Amount"])
-    sch1_amounts = load_csv_amounts(sch1_path, code_field_candidates=["Line", "line"], amount_field_candidates=["Amount", "amount"])
+    sch1_amounts = load_csv_amounts(sch1_path, code_field_candidates=["Code", "Line", "line"], amount_field_candidates=["Amount", "amount"])
     sch1_labels = load_schedule_1_labels(sch1_path)
 
     def merge_section(existing: dict, amounts: dict[str, int], labels: dict[str, str] | None = None) -> dict:
@@ -145,6 +195,28 @@ def update_year_section(
     year["retained_earnings"] = merge_section(year.get("retained_earnings", {}), retained)
     year["schedule_1"] = merge_section(year.get("schedule_1", {}), sch1_amounts, labels=sch1_labels)
 
+    schedule_8_path = snapshot_dir / f"schedule_8_{fy}.csv"
+    schedule_8_classes = load_schedule_8(schedule_8_path)
+    cca_assets_path = snapshot_dir / "cca_asset_register_resolved.csv"
+    cca_assets = load_cca_assets(cca_assets_path, fy)
+    if schedule_8_classes or cca_assets:
+        classes_used = sorted(schedule_8_classes.keys(), key=lambda x: int(x) if x.isdigit() else 10**9)
+        total_additions = sum(int(v.get("additions") or 0) for v in schedule_8_classes.values())
+        total_cca = sum(int(v.get("cca_claim") or 0) for v in schedule_8_classes.values())
+        schedule_8_note = f"Total CCA claimed: {total_cca}. Classes used: {', '.join(classes_used) if classes_used else 'none'}."
+        year["schedule_8"] = {
+            "classes": schedule_8_classes,
+            "assets": cca_assets,
+            "summary": {
+                "total_additions": int(total_additions),
+                "total_cca_claim": int(total_cca),
+                "classes_used": classes_used,
+            },
+            "note": schedule_8_note,
+        }
+    else:
+        year.pop("schedule_8", None)
+
     # --- Year-specific UFile screens derived from the schedules (no guessing) ---
     year_screens = year.get("ufile_screens", {})
     if not isinstance(year_screens, dict):
@@ -164,7 +236,9 @@ def update_year_section(
     if isinstance(prior_year, dict):
         prior_end = str(prior_year.get("fiscal_period", {}).get("end") or prior_end)
         try:
-            prior_taxable_income = int((prior_year.get("schedule_1", {}).get("400") or {}).get("amount") or 0)
+            prior_taxable_income = int(
+                (prior_year.get("schedule_1", {}).get("C") or prior_year.get("schedule_1", {}).get("400") or {}).get("amount") or 0
+            )
         except Exception:
             prior_taxable_income = 0
         try:
@@ -199,7 +273,7 @@ def update_year_section(
     corp_hist.setdefault(
         "note",
         "UFile Corporate History screen: typically only the 1st prior year row is needed. "
-        "Taxable income should match prior year Schedule 1 line 400; taxable paid-up capital usually matches share capital unless evidence indicates otherwise.",
+        "Taxable income should match prior year Schedule 1 code C; taxable paid-up capital usually matches share capital unless evidence indicates otherwise.",
     )
     year_screens["corporate_history"] = corp_hist
 
@@ -239,6 +313,34 @@ def update_year_section(
     )
     year_screens["general_rate_income_pool"] = grip
 
+    # CCA screen + position flags
+    cca_classes_used = []
+    total_cca_claim = 0
+    schedule_8 = year.get("schedule_8", {}) if isinstance(year.get("schedule_8"), dict) else {}
+    if isinstance(schedule_8.get("summary"), dict):
+        cca_classes_used = schedule_8.get("summary", {}).get("classes_used") or []
+        total_cca_claim = int(schedule_8.get("summary", {}).get("total_cca_claim") or 0)
+    has_cca = bool(cca_classes_used)
+
+    cca_screen = year_screens.get("capital_cost_allowance", {})
+    if not isinstance(cca_screen, dict):
+        cca_screen = {}
+    cca_screen["has_cca"] = has_cca
+    if has_cca:
+        cca_screen["note"] = f"CCA claimed per Schedule 8. Total CCA: {total_cca_claim}. Classes: {', '.join(cca_classes_used)}."
+    year_screens["capital_cost_allowance"] = cca_screen
+
+    positions = year.get("positions", {})
+    if not isinstance(positions, dict):
+        positions = {}
+    positions.setdefault("cca_required", {})
+    if not isinstance(positions.get("cca_required"), dict):
+        positions["cca_required"] = {}
+    positions["cca_required"]["value"] = has_cca
+    if has_cca:
+        positions["cca_required"]["note"] = f"CCA claimed per Schedule 8. Total CCA: {total_cca_claim}. Classes: {', '.join(cca_classes_used)}."
+    year["positions"] = positions
+
 
 def main() -> int:
     ap = argparse.ArgumentParser()
diff --git a/UfileToFill/ufile_packet/tools/build_year_artifacts.py b/UfileToFill/ufile_packet/tools/build_year_artifacts.py
index 801231f..eaf5ec7 100644
--- a/UfileToFill/ufile_packet/tools/build_year_artifacts.py
+++ b/UfileToFill/ufile_packet/tools/build_year_artifacts.py
@@ -28,6 +28,16 @@ def money(n: int) -> str:
     return f"{n:,}"
 
 
+def schedule_1_sort_key(code: str) -> tuple[int, object]:
+    if code == "A":
+        return (-2, 0)
+    if code == "C":
+        return (2, 0)
+    if code.isdigit():
+        return (0, int(code))
+    return (1, code)
+
+
 def build_year_packet(packet: dict, fy: str) -> dict:
     entity = packet["entity"]
     year = packet["years"][fy]
@@ -348,7 +358,9 @@ def build_year_guide(packet: dict, fy: str) -> str:
             prior_year = packet["years"].get(prior_fy)
             if prior_year:
                 prior_end = prior_year["fiscal_period"]["end"]
-                prior_taxable_income = int(prior_year["schedule_1"]["400"]["amount"])
+                prior_taxable_income = int(
+                    (prior_year["schedule_1"].get("C") or prior_year["schedule_1"].get("400") or {"amount": 0}).get("amount") or 0
+                )
                 prior_total_assets = int(prior_year.get("schedule_100", {}).get("2599", {}).get("amount") or 0)
                 # As a CCPC with active business income, prior year generally claims SBD (confirm in UFile).
                 prior_sbd_claimed = "Yes"
@@ -364,7 +376,7 @@ def build_year_guide(packet: dict, fy: str) -> str:
             ["Field", "Value", "Note"],
             [
                 ["1st prior year end date", prior_end, "UFile field: End date of prior tax year"],
-                ["1st prior year taxable income", money(prior_taxable_income), "UFile field: Taxable income (Schedule 1 line 400 of the prior year)"],
+                ["1st prior year taxable income", money(prior_taxable_income), "UFile field: Taxable income (Schedule 1 code C of the prior year)"],
                 [
                     "Eligible RDTOH at prior year-end",
                     money(int((corp_hist.get("eligible_rdtoh_end_prior_year") if isinstance(corp_hist, dict) else 0) or 0)),
@@ -405,7 +417,11 @@ def build_year_guide(packet: dict, fy: str) -> str:
         md_table(
             ["Field", "Value", "Note"],
             [
-                ["Net income as per financial statements", money(int(schedule_1["300"]["amount"])), "Should auto-fill from GIFI; otherwise enter from Schedule 1 line 300."],
+                [
+                    "Net income as per financial statements",
+                    money(int((schedule_1.get("A") or schedule_1.get("300") or {"amount": 0}).get("amount") or 0)),
+                    "Should auto-fill from GIFI; otherwise enter from Schedule 1 code A.",
+                ],
                 ["Total sales of corporation during this taxation year", money(gross_revenue), "Use total revenue (sum of revenue lines; typically matches trade sales 8000)."],
                 ["Total gross revenues", money(gross_revenue), "Usually same as total sales for your file."],
             ],
@@ -755,7 +771,7 @@ def build_year_guide(packet: dict, fy: str) -> str:
                 break
         blank_rows.append([label, yn(has_any) if has_any is not None else "No", str(obj.get("note") or "")])
 
-    parts.append("## Other UFile screens (expected blank / N/A)")
+    parts.append("## Other UFile screens (usually blank / check if applicable)")
     parts.append(md_table(["Screen", "Has entries?", "Note"], blank_rows))
     parts.append("")
 
@@ -836,12 +852,56 @@ def build_year_guide(packet: dict, fy: str) -> str:
     parts.append("## Schedule 1 (tax purposes)")
     parts.append(
         md_table(
-            ["Line", "Description", "Amount", "Calculation"],
-            [[line, obj.get("label", ""), money(int(obj["amount"])), obj.get("calculation","") or ""] for line, obj in sorted(schedule_1.items(), key=lambda kv: int(kv[0]))],
+            ["Code", "Description", "Amount", "Calculation"],
+            [
+                [line, obj.get("label", ""), money(int(obj["amount"])), obj.get("calculation", "") or ""]
+                for line, obj in sorted(schedule_1.items(), key=lambda kv: schedule_1_sort_key(kv[0]))
+            ],
         )
     )
     parts.append("")
 
+    schedule_8 = year.get("schedule_8", {}) if isinstance(year.get("schedule_8"), dict) else {}
+    if schedule_8 and isinstance(schedule_8.get("classes"), dict) and schedule_8["classes"]:
+        parts.append("## Schedule 8 / CCA")
+        classes = schedule_8.get("classes", {}) if isinstance(schedule_8.get("classes"), dict) else {}
+        class_rows = []
+        for class_code, obj in sorted(classes.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 10**9):
+            class_rows.append(
+                [
+                    class_code,
+                    str(obj.get("description") or ""),
+                    money(int(obj.get("opening_ucc") or 0)),
+                    money(int(obj.get("additions") or 0)),
+                    money(int(obj.get("cca_claim") or 0)),
+                    money(int(obj.get("closing_ucc") or 0)),
+                ]
+            )
+        parts.append(
+            md_table(
+                ["Class", "Description", "Opening UCC", "Additions", "CCA claim", "Closing UCC"],
+                class_rows,
+            )
+        )
+        parts.append("")
+
+        assets = schedule_8.get("assets", []) if isinstance(schedule_8.get("assets"), list) else []
+        if assets:
+            asset_rows = []
+            for asset in assets:
+                asset_rows.append(
+                    [
+                        str(asset.get("asset_id") or ""),
+                        str(asset.get("description") or ""),
+                        str(asset.get("available_for_use_date") or ""),
+                        str(asset.get("cca_class") or ""),
+                        money(int(asset.get("total_cost_dollars") or 0)),
+                    ]
+                )
+            parts.append("### Schedule 8 asset additions (audit trail)")
+            parts.append(md_table(["Asset ID", "Description", "Date", "Class", "Cost"], asset_rows))
+            parts.append("")
+
     # High-signal yes/no answers that differ year-to-year
     parts.append("## High-signal yes/no answers")
     pos = year.get("positions", {})
@@ -889,14 +949,14 @@ def write_year_tables(packet: dict, fy: str) -> None:
     def write_schedule_1(path: Path, schedule_1: dict) -> None:
         with path.open("w", newline="") as f:
             w = csv.writer(f)
-            w.writerow(["Line", "Description", "Amount", "Calculation"])
-            for line, obj in sorted(schedule_1.items(), key=lambda kv: int(kv[0])):
+            w.writerow(["Code", "Description", "Amount", "Calculation"])
+            for line, obj in sorted(schedule_1.items(), key=lambda kv: schedule_1_sort_key(kv[0])):
                 if not isinstance(obj, dict):
                     continue
                 desc = obj.get("label", "") or ""
                 amount = int(obj.get("amount", 0) or 0)
                 calc = obj.get("calculation", "") or ""
-                w.writerow([int(line), desc, amount, calc])
+                w.writerow([str(line), desc, amount, calc])
 
     write_schedule(TABLES_DIR / f"schedule_100_{fy}.csv", year.get("schedule_100", {}))
     write_schedule(TABLES_DIR / f"schedule_125_{fy}.csv", year.get("schedule_125", {}))
diff --git a/UfileToFill/ufile_packet/tools/validate_packet.py b/UfileToFill/ufile_packet/tools/validate_packet.py
index 31bb357..59f1b0c 100644
--- a/UfileToFill/ufile_packet/tools/validate_packet.py
+++ b/UfileToFill/ufile_packet/tools/validate_packet.py
@@ -71,19 +71,28 @@ def load_schedule_1_csv(path: Path) -> dict[str, int]:
     with path.open(newline="") as f:
         reader = csv.DictReader(f)
         for row in reader:
-            line = (row.get("Line") or row.get("line") or "").strip()
-            if not line:
+            code = (row.get("Code") or row.get("Line") or row.get("line") or "").strip()
+            if not code:
                 continue
             amount_raw = (row.get("Amount") or row.get("amount") or "").strip()
             if amount_raw == "":
                 continue
-            out[line] = int(Decimal(amount_raw))
+            out[code] = int(Decimal(amount_raw))
     return out
 
 
 def compare_dicts(label: str, a: dict[str, int], b: dict[str, int]) -> list[str]:
+    def sort_key(code: str) -> tuple[int, object]:
+        if code == "A":
+            return (-2, 0)
+        if code == "C":
+            return (2, 0)
+        if code.isdigit():
+            return (0, int(code))
+        return (1, code)
+
     issues: list[str] = []
-    all_keys = sorted(set(a) | set(b), key=lambda x: int(x))
+    all_keys = sorted(set(a) | set(b), key=sort_key)
     for k in all_keys:
         if a.get(k) != b.get(k):
             issues.append(f"{label}: {k}: snapshot={a.get(k)} packet={b.get(k)}")
@@ -167,6 +176,19 @@ def main() -> int:
                         if not isinstance(grip, dict) or "grip_end_prior_year" not in grip:
                             completeness.append(f"{fy}: eligible dividends portion > 0 but general_rate_income_pool is missing or incomplete.")
 
+            cca_screen = year_screens.get("capital_cost_allowance", {}) if isinstance(year_screens, dict) else {}
+            has_cca = cca_screen.get("has_cca") if isinstance(cca_screen, dict) else None
+            schedule_8 = year.get("schedule_8", {}) if isinstance(year, dict) else {}
+            classes = schedule_8.get("classes", {}) if isinstance(schedule_8, dict) else {}
+            if has_cca is True and not classes:
+                completeness.append(f"{fy}: capital_cost_allowance.has_cca is true but schedule_8 classes are missing/empty.")
+            if classes:
+                sch1 = year.get("schedule_1", {}) if isinstance(year, dict) else {}
+                if "206" not in sch1:
+                    completeness.append(f"{fy}: schedule_8 present but schedule_1 missing code 206 (capital items expensed).")
+                if "403" not in sch1:
+                    completeness.append(f"{fy}: schedule_8 present but schedule_1 missing code 403 (CCA claim).")
+
     for fy in ["FY2024", "FY2025"]:
         snap_100 = load_gifi_csv(snapshot_dir / f"gifi_schedule_100_{fy}.csv")
         pkt_100 = {k: int(v["amount"]) for k, v in packet["years"][fy]["schedule_100"].items()}
diff --git a/UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md b/UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md
index 975a363..cca5a1e 100644
--- a/UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md
+++ b/UfileToFill/ufile_packet/years/FY2024/UFILet2_FILL_GUIDE.md
@@ -63,7 +63,7 @@
 | Field | Value | Note |
 |---|---|---|
 | 1st prior year end date | 2023-05-31 | UFile field: End date of prior tax year |
-| 1st prior year taxable income | 0 | UFile field: Taxable income (Schedule 1 line 400 of the prior year) |
+| 1st prior year taxable income | 0 | UFile field: Taxable income (Schedule 1 code C of the prior year) |
 | Eligible RDTOH at prior year-end | 0 | Usually $0 for your file unless you have refundable dividend tax on hand |
 | Non-eligible RDTOH at prior year-end | 0 |  |
 | Eligible dividend refund (prior year) | 0 |  |
@@ -77,7 +77,7 @@
 ## Net income (UFile screen)
 | Field | Value | Note |
 |---|---|---|
-| Net income as per financial statements | 16,655 | Should auto-fill from GIFI; otherwise enter from Schedule 1 line 300. |
+| Net income as per financial statements | 16,655 | Should auto-fill from GIFI; otherwise enter from Schedule 1 code A. |
 | Total sales of corporation during this taxation year | 181,235 | Use total revenue (sum of revenue lines; typically matches trade sales 8000). |
 | Total gross revenues | 181,235 | Usually same as total sales for your file. |
 
@@ -223,13 +223,13 @@ There are transactions with shareholders (reimbursements/amounts due). For T2 di
 
 No eligible dividends expected; leave GRIP blank/zero unless UFile requires it.
 
-## Other UFile screens (expected blank / N/A)
+## Other UFile screens (usually blank / check if applicable)
 | Screen | Has entries? | Note |
 |---|---|---|
 | Loss carryforwards / carrybacks | No | No losses to carry forward/back. |
 | Charitable donations | No | No charitable donations claimed. |
 | Reserves | No | No reserves claimed. |
-| Capital cost allowance (CCA) | No | No CCA claimed; assets were expensed under capitalization threshold. |
+| Capital cost allowance (CCA) | Check | Use Schedule 8 outputs; if CCA is claimed, mark Yes and enter class details. |
 | Non-depreciable capital property | No | No non-depreciable capital property. |
 | Deferred income plans | No | No deferred income plans. |
 | Status change for the corporation | No | No status change for the corporation. |
@@ -294,12 +294,16 @@ No eligible dividends expected; leave GRIP blank/zero unless UFile requires it.
 | 3849 | Retained earnings/deficit - End | 16,656 | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |
 
 ## Schedule 1 (tax purposes)
-| Line | Description | Amount | Calculation |
+| Code | Description | Amount | Calculation |
 |---|---|---|---|
-| 117 | 50% of meals and entertainment | 259 | 518 * 50% = 259 |
-| 300 | Net income per financial statements | 16,655 |  |
-| 311 | Penalties and fines (CRA) | 71 |  |
-| 400 | Net income for tax purposes | 16,985 | 16655 + 259 + 71 = 16985 |
+| A | Net income (loss) per financial statements | 16,655 |  |
+| 121 | Non-deductible meals and entertainment (50%) | 259 | 518 * 50% = 259 |
+| 128 | Non-deductible fines and penalties | 71 |  |
+| 206 | Capital items expensed | 0 |  |
+| 500 | Total additions | 330 | 259 + 71 = 330 |
+| 403 | Capital cost allowance (Schedule 8) | 0 |  |
+| 510 | Total deductions | 0 |  |
+| C | Net income (loss) for tax purposes | 16,985 | 16655 + 330 - 0 = 16985 |
 
 ## High-signal yes/no answers
 | Question | Answer | Note |
@@ -307,4 +311,4 @@ No eligible dividends expected; leave GRIP blank/zero unless UFile requires it.
 | T2 line 070 (first year after incorporation) | No | 2023 stub T2 (2022-12-08 → 2023-05-31) already answered Incorporation=Yes and filed Schedule 24; FY2024 should be No. |
 | T2 line 180 (internet income/websites) | Yes | Shopify sales present; likely Yes for internet income/websites (Schedule 88). Confirm store domains in UFile. |
 | T2 line 201 (book vs tax net income differs) | Yes | Book vs tax differs due to meals 50% add-back and CRA penalties; Schedule 1 is attached. |
-| CCA required / capital assets | No | No capital assets capitalized in these years (below capitalization threshold; expensed). |
+| CCA required / capital assets | Check | CCA is determined by the asset register + Schedule 8 (tax-only layer). |
diff --git a/UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md b/UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md
index 99d7904..a6401b7 100644
--- a/UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md
+++ b/UfileToFill/ufile_packet/years/FY2025/UFILet2_FILL_GUIDE.md
@@ -64,7 +64,7 @@
 | Field | Value | Note |
 |---|---|---|
 | 1st prior year end date | 2024-05-31 | UFile field: End date of prior tax year |
-| 1st prior year taxable income | 16,985 | UFile field: Taxable income (Schedule 1 line 400 of the prior year) |
+| 1st prior year taxable income | 16,985 | UFile field: Taxable income (Schedule 1 code C of the prior year) |
 | Eligible RDTOH at prior year-end | 0 | Usually $0 for your file unless you have refundable dividend tax on hand |
 | Non-eligible RDTOH at prior year-end | 0 |  |
 | Eligible dividend refund (prior year) | 0 |  |
@@ -78,7 +78,7 @@
 ## Net income (UFile screen)
 | Field | Value | Note |
 |---|---|---|
-| Net income as per financial statements | 30,557 | Should auto-fill from GIFI; otherwise enter from Schedule 1 line 300. |
+| Net income as per financial statements | 30,557 | Should auto-fill from GIFI; otherwise enter from Schedule 1 code A. |
 | Total sales of corporation during this taxation year | 230,907 | Use total revenue (sum of revenue lines; typically matches trade sales 8000). |
 | Total gross revenues | 230,907 | Usually same as total sales for your file. |
 
@@ -234,13 +234,13 @@ Dividends declared per retained earnings schedule (GIFI 3700). Confirm eligible
 
 Unless you are designating eligible dividends, GRIP is typically $0 / not needed. If you mark any eligible dividends, you must complete this screen.
 
-## Other UFile screens (expected blank / N/A)
+## Other UFile screens (usually blank / check if applicable)
 | Screen | Has entries? | Note |
 |---|---|---|
 | Loss carryforwards / carrybacks | No | No losses to carry forward/back. |
 | Charitable donations | No | No charitable donations claimed. |
 | Reserves | No | No reserves claimed. |
-| Capital cost allowance (CCA) | No | No CCA claimed; assets were expensed under capitalization threshold. |
+| Capital cost allowance (CCA) | Check | Use Schedule 8 outputs; if CCA is claimed, mark Yes and enter class details. |
 | Non-depreciable capital property | No | No non-depreciable capital property. |
 | Deferred income plans | No | No deferred income plans. |
 | Status change for the corporation | No | No status change for the corporation. |
@@ -307,12 +307,16 @@ Unless you are designating eligible dividends, GRIP is typically $0 / not needed
 | 3849 | Retained earnings/deficit - End | 10,312 | Do NOT type if UFile auto-calculates (should equal 3660 + 3680 - 3700 + 3740) |
 
 ## Schedule 1 (tax purposes)
-| Line | Description | Amount | Calculation |
+| Code | Description | Amount | Calculation |
 |---|---|---|---|
-| 117 | 50% of meals and entertainment | 204 | 408 * 50% = 204 |
-| 300 | Net income per financial statements | 30,557 |  |
-| 311 | Penalties and fines (CRA) | 274 |  |
-| 400 | Net income for tax purposes | 31,035 | 28349 + 204 + 274 = 28827 |
+| A | Net income (loss) per financial statements | 30,557 |  |
+| 121 | Non-deductible meals and entertainment (50%) | 204 | 408 * 50% = 204 |
+| 128 | Non-deductible fines and penalties | 274 |  |
+| 206 | Capital items expensed | 0 |  |
+| 500 | Total additions | 478 | 204 + 274 = 478 |
+| 403 | Capital cost allowance (Schedule 8) | 0 |  |
+| 510 | Total deductions | 0 |  |
+| C | Net income (loss) for tax purposes | 31,035 | 30557 + 478 - 0 = 31035 |
 
 ## High-signal yes/no answers
 | Question | Answer | Note |
@@ -320,4 +324,4 @@ Unless you are designating eligible dividends, GRIP is typically $0 / not needed
 | T2 line 070 (first year after incorporation) | No | 2023 stub T2 already filed as first-year after incorporation (Schedule 24). FY2025 should be No. |
 | T2 line 180 (internet income/websites) | Yes | Shopify sales present; likely Yes for internet income/websites (Schedule 88). Confirm store domains in UFile. |
 | T2 line 201 (book vs tax net income differs) | Yes | Book vs tax differs due to meals 50% add-back and CRA penalties; Schedule 1 is attached. |
-| CCA required / capital assets | No | No capital assets capitalized in these years (below capitalization threshold; expensed). |
+| CCA required / capital assets | Check | CCA is determined by the asset register + Schedule 8 (tax-only layer). |
diff --git a/docs/T2_AUDIT_READINESS_FULL_SCOPE.md b/docs/T2_AUDIT_READINESS_FULL_SCOPE.md
index 04eb429..471bf6d 100644
--- a/docs/T2_AUDIT_READINESS_FULL_SCOPE.md
+++ b/docs/T2_AUDIT_READINESS_FULL_SCOPE.md
@@ -208,7 +208,7 @@ The mechanical pipeline is strong (bank coverage, deterministic imports, reprodu
 ## 5) Low‑Risk / Mostly Clean Items
 
 - Wave bill payment matching residuals are immaterial (net ~**$‑5.18**) (`output/readiness_report.md`).
-- No fixed‑asset balances appear on Schedule 100; CCA/depreciation is likely not required for these FYs (`output/readiness_report.md`, `output/trial_balance_FY2024.csv`, `output/trial_balance_FY2025.csv`).
+- No fixed‑asset balances appear on Schedule 100, but CCA must still be assessed via the tax asset register (Schedule 8) because capital items can be expensed in books (`overrides/cca_assets.yml`, `output/schedule_8_FY2024.csv`, `output/schedule_8_FY2025.csv`).
 - Cash float logic is explicit and reconciles:
   - float withdrawals total **$2,624.50**
   - float returned via cash deposits **$2,324.50**
diff --git a/overrides/cca_assets.yml b/overrides/cca_assets.yml
new file mode 100644
index 0000000..5c7c9c7
--- /dev/null
+++ b/overrides/cca_assets.yml
@@ -0,0 +1,16 @@
+version: 1
+policy:
+  default_claim_percent_of_max: 1.0
+  default_half_year_rule: true
+
+assets:
+  - asset_id: nayax_card_reader_2025_02_24
+    description: Nayax card reader for vending machine
+    cca_class: 8
+    available_for_use_date: "2025-02-24"
+    source_components:
+      - source_type: wave_bill_allocation
+        wave_bill_id: 628
+        account_code: "5300"
+        amount_cents: 55743
+    notes: "Reclass from merchant fees for tax/CCA only"
diff --git a/scripts/32_report_cca_candidates.py b/scripts/32_report_cca_candidates.py
new file mode 100644
index 0000000..9b5f332
--- /dev/null
+++ b/scripts/32_report_cca_candidates.py
@@ -0,0 +1,158 @@
+#!/usr/bin/env python3
+
+from __future__ import annotations
+
+import argparse
+import csv
+from decimal import Decimal
+from pathlib import Path
+
+from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest
+
+
+def cents_to_dollars(cents: int) -> str:
+    return f"{Decimal(cents) / Decimal(100):.2f}"
+
+
+def main() -> int:
+    ap = argparse.ArgumentParser()
+    ap.add_argument("--db", type=Path, default=DB_PATH)
+    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
+    ap.add_argument("--threshold", type=float, default=300.0, help="Minimum net amount in dollars to list as a candidate (default: 300).")
+    args = ap.parse_args()
+
+    manifest = load_manifest()
+    fys = fiscal_years_from_manifest(manifest)
+    if not fys:
+        raise SystemExit("No fiscal_years found in manifest/sources.yml")
+
+    scope_start = min(fy.start_date for fy in fys)
+    scope_end = max(fy.end_date for fy in fys)
+    threshold_cents = int(Decimal(str(args.threshold)) * Decimal(100))
+
+    args.out_dir.mkdir(parents=True, exist_ok=True)
+    out_csv = args.out_dir / "cca_candidates.csv"
+
+    flag_account_codes = {"5300"}
+
+    conn = connect_db(args.db)
+    try:
+        wave_rows = conn.execute(
+            """
+            SELECT id, invoice_date, vendor_raw, total_cents, tax_cents, net_cents
+            FROM wave_bills
+            WHERE invoice_date BETWEEN ? AND ?
+              AND CAST(net_cents AS INTEGER) >= ?
+            ORDER BY invoice_date, id
+            """,
+            (scope_start, scope_end, threshold_cents),
+        ).fetchall()
+
+        cc_rows = conn.execute(
+            """
+            SELECT je.id, je.entry_date, je.description,
+                   SUM(CAST(jel.debit_cents AS INTEGER)) AS debit_cents
+            FROM journal_entries je
+            JOIN journal_entry_lines jel ON jel.journal_entry_id = je.id
+            WHERE je.source_record_type = 'credit_card_purchases'
+              AND je.entry_date BETWEEN ? AND ?
+            GROUP BY je.id, je.entry_date, je.description
+            HAVING SUM(CAST(jel.debit_cents AS INTEGER)) >= ?
+            ORDER BY je.entry_date, je.id
+            """,
+            (scope_start, scope_end, threshold_cents),
+        ).fetchall()
+
+        with out_csv.open("w", newline="") as f:
+            w = csv.writer(f)
+            w.writerow(
+                [
+                    "source_type",
+                    "record_id",
+                    "date",
+                    "vendor",
+                    "total_cents",
+                    "total_dollars",
+                    "allocation_breakdown",
+                    "flags",
+                ]
+            )
+
+            for r in wave_rows:
+                allocs = conn.execute(
+                    """
+                    SELECT account_code, SUM(CAST(amount_cents AS INTEGER)) AS amount_cents
+                    FROM bill_allocations
+                    WHERE wave_bill_id = ?
+                    GROUP BY account_code
+                    ORDER BY ABS(SUM(CAST(amount_cents AS INTEGER))) DESC
+                    """,
+                    (int(r["id"]),),
+                ).fetchall()
+                breakdown = "; ".join(f"{a['account_code']}:{a['amount_cents']}" for a in allocs if a["account_code"])
+
+                flags = []
+                if any(a["account_code"] in flag_account_codes for a in allocs if a["account_code"]):
+                    flags.append("likely_equipment_account_code")
+                vendor_raw = str(r["vendor_raw"] or "")
+                if "nayax" in vendor_raw.lower():
+                    flags.append("vendor_keyword:nayax")
+
+                w.writerow(
+                    [
+                        "wave_bill",
+                        r["id"],
+                        r["invoice_date"],
+                        vendor_raw,
+                        int(r["net_cents"] or 0),
+                        cents_to_dollars(int(r["net_cents"] or 0)),
+                        breakdown,
+                        ",".join(flags),
+                    ]
+                )
+
+            for r in cc_rows:
+                lines = conn.execute(
+                    """
+                    SELECT account_code, SUM(CAST(debit_cents AS INTEGER)) AS amount_cents
+                    FROM journal_entry_lines
+                    WHERE journal_entry_id = ?
+                      AND CAST(debit_cents AS INTEGER) > 0
+                    GROUP BY account_code
+                    ORDER BY ABS(SUM(CAST(debit_cents AS INTEGER))) DESC
+                    """,
+                    (r["id"],),
+                ).fetchall()
+                breakdown = "; ".join(f"{a['account_code']}:{a['amount_cents']}" for a in lines if a["account_code"])
+
+                flags = []
+                if any(a["account_code"] in flag_account_codes for a in lines if a["account_code"]):
+                    flags.append("likely_equipment_account_code")
+                desc = str(r["description"] or "")
+                if "nayax" in desc.lower():
+                    flags.append("vendor_keyword:nayax")
+
+                w.writerow(
+                    [
+                        "cc_purchase",
+                        r["id"],
+                        r["entry_date"],
+                        desc,
+                        int(r["debit_cents"] or 0),
+                        cents_to_dollars(int(r["debit_cents"] or 0)),
+                        breakdown,
+                        ",".join(flags),
+                    ]
+                )
+    finally:
+        conn.close()
+
+    print("CCA CANDIDATE REPORT BUILT")
+    print(f"- out: {out_csv}")
+    print(f"- threshold: ${args.threshold:.2f}")
+    print(f"- scope: {scope_start} to {scope_end}")
+    return 0
+
+
+if __name__ == "__main__":
+    raise SystemExit(main())
diff --git a/scripts/82_build_readiness_report.py b/scripts/82_build_readiness_report.py
index 35396de..4711fa2 100644
--- a/scripts/82_build_readiness_report.py
+++ b/scripts/82_build_readiness_report.py
@@ -447,7 +447,10 @@ def main() -> int:
         if fixed_present:
             f.write("- Depreciation/CCA and any fixed-asset rollforward is not yet modeled here.\n")
         else:
-            f.write("- No fixed-asset balances detected (CCA/depreciation not required).\n")
+            f.write(
+                "- No fixed-asset balances detected on Schedule 100, but CCA must be assessed separately via the tax asset register "
+                "(`overrides/cca_assets.yml`) and Schedule 8 outputs.\n"
+            )
 
     print("READINESS REPORT BUILT")
     print(f"- out: {out_md}")
diff --git a/scripts/91_build_t2_schedule_exports.py b/scripts/91_build_t2_schedule_exports.py
index 2cc9c14..1a419ac 100644
--- a/scripts/91_build_t2_schedule_exports.py
+++ b/scripts/91_build_t2_schedule_exports.py
@@ -67,9 +67,31 @@ def write_schedule_1_csv(rows: list[tuple[str, str, int]], path: Path) -> None:
     path.parent.mkdir(parents=True, exist_ok=True)
     with path.open("w", encoding="utf-8", newline="") as f:
         w = csv.writer(f)
-        w.writerow(["Line", "Description", "Amount"])
-        for line, desc, amt in rows:
-            w.writerow([line, desc, str(int(amt))])
+        w.writerow(["Code", "Label", "Amount"])
+        for code, desc, amt in rows:
+            w.writerow([code, desc, str(int(amt))])
+
+
+def load_schedule_8_summary(path: Path) -> tuple[int, int, int]:
+    """
+    Returns (additions_total, cca_claim_total, class_rows).
+    If schedule 8 file is missing, returns zeros.
+    """
+
+    if not path.exists():
+        return 0, 0, 0
+    rows = list(csv.DictReader(path.open("r", encoding="utf-8", newline="")))
+    additions_total = 0
+    cca_total = 0
+    class_rows = 0
+    for r in rows:
+        class_val = str(r.get("Class") or r.get("class") or "").strip()
+        if not class_val:
+            continue
+        class_rows += 1
+        additions_total += int(r.get("Additions") or 0)
+        cca_total += int(r.get("CCA_Claim") or r.get("cca_claim") or 0)
+    return additions_total, cca_total, class_rows
 
 
 def load_gifi_descriptions() -> dict[str, str]:
@@ -309,18 +331,29 @@ def main() -> int:
             re_rows.append(("3740", f"{desc('3740', gifi_desc=gifi_desc)} (rounding)", retained_adjust))
         re_rows.append(("3849", desc("3849", gifi_desc=gifi_desc), retained_end))
 
-        # Schedule 1 (Net income for tax purposes): 50% M&E add-back.
+        # Schedule 1 (Net income for tax purposes) aligned to CRA T2SCH1 (2023+).
         meals_cents = meals_cents_from_tb(tb)
         meals_dollars = round_cents_to_dollar(meals_cents)
         meals_addback = round_to_dollar(Decimal(meals_dollars) / Decimal(2))
         penalties_dollars = round_cents_to_dollar(cra_penalties_cents_from_tb(tb))
         penalties_addback = penalties_dollars
-        taxable_income = net_income + meals_addback + penalties_addback
+
+        schedule8_path = args.out_dir / f"schedule_8_{fy.fy}.csv"
+        cca_additions, cca_claim, _ = load_schedule_8_summary(schedule8_path)
+
+        total_additions = meals_addback + penalties_addback + cca_additions
+        total_deductions = cca_claim
+        taxable_income = net_income + total_additions - total_deductions
+
         sch1_rows: list[tuple[str, str, int]] = [
-            ("300", "Net income per financial statements", net_income),
-            ("117", "50% of meals and entertainment", meals_addback),
-            ("311", "Penalties and fines (CRA)", penalties_addback),
-            ("400", "Net income for tax purposes", taxable_income),
+            ("A", "Net income (loss) per financial statements", net_income),
+            ("121", "Non-deductible meals and entertainment (50%)", meals_addback),
+            ("128", "Non-deductible fines and penalties", penalties_addback),
+            ("206", "Capital items expensed", cca_additions),
+            ("500", "Total additions", total_additions),
+            ("403", "Capital cost allowance (Schedule 8)", total_deductions),
+            ("510", "Total deductions", total_deductions),
+            ("C", "Net income (loss) for tax purposes", taxable_income),
         ]
 
         # Write outputs
diff --git a/scripts/91b_build_cca_schedule_8.py b/scripts/91b_build_cca_schedule_8.py
new file mode 100644
index 0000000..819eb6c
--- /dev/null
+++ b/scripts/91b_build_cca_schedule_8.py
@@ -0,0 +1,417 @@
+#!/usr/bin/env python3
+
+from __future__ import annotations
+
+import argparse
+import csv
+from dataclasses import dataclass
+from datetime import date
+from decimal import Decimal, ROUND_HALF_UP
+from pathlib import Path
+
+from _lib import DB_PATH, PROJECT_ROOT, connect_db, fiscal_years_from_manifest, load_manifest, load_yaml
+
+
+ASSET_REGISTER_PATH = PROJECT_ROOT / "overrides" / "cca_assets.yml"
+
+
+@dataclass(frozen=True)
+class AssetComponent:
+    source_type: str
+    wave_bill_id: int | None
+    account_code: str | None
+    amount_cents: int
+    notes: str | None
+
+
+@dataclass(frozen=True)
+class Asset:
+    asset_id: str
+    description: str
+    cca_class: str
+    available_for_use_date: str
+    source_components: list[AssetComponent]
+    claim_percent_of_max: Decimal
+    half_year_rule: bool
+    notes: str | None
+
+
+@dataclass(frozen=True)
+class ResolvedComponent:
+    source_type: str
+    wave_bill_id: int | None
+    account_code: str | None
+    amount_cents: int
+    invoice_date: str | None
+    vendor_raw: str | None
+    allocation_total_cents: int | None
+    notes: str | None
+
+
+@dataclass(frozen=True)
+class ResolvedAsset:
+    asset: Asset
+    fy: str
+    total_cost_cents: int
+    resolved_components: list[ResolvedComponent]
+
+
+def round_to_dollar(amount: Decimal) -> int:
+    return int(amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
+
+
+def round_cents_to_dollar(cents: int) -> int:
+    return round_to_dollar(Decimal(int(cents)) / Decimal(100))
+
+
+def load_assets(path: Path) -> tuple[dict, list[Asset]]:
+    data = load_yaml(path)
+    if not isinstance(data.get("assets"), list):
+        raise SystemExit("overrides/cca_assets.yml must include an assets list")
+
+    policy = data.get("policy") if isinstance(data.get("policy"), dict) else {}
+    default_claim = Decimal(str(policy.get("default_claim_percent_of_max", "1.0")))
+    default_half_year = bool(policy.get("default_half_year_rule", True))
+
+    assets: list[Asset] = []
+    seen_ids: set[str] = set()
+    for raw in data["assets"]:
+        if not isinstance(raw, dict):
+            continue
+        asset_id = str(raw.get("asset_id") or "").strip()
+        if not asset_id:
+            raise SystemExit("Every CCA asset must have asset_id")
+        if asset_id in seen_ids:
+            raise SystemExit(f"Duplicate asset_id in CCA register: {asset_id}")
+        seen_ids.add(asset_id)
+
+        desc = str(raw.get("description") or "").strip()
+        if not desc:
+            raise SystemExit(f"CCA asset {asset_id} missing description")
+
+        cca_class_raw = raw.get("cca_class")
+        if cca_class_raw is None:
+            raise SystemExit(f"CCA asset {asset_id} missing cca_class")
+        cca_class = str(cca_class_raw).strip()
+
+        afu = str(raw.get("available_for_use_date") or "").strip()
+        if not afu:
+            raise SystemExit(f"CCA asset {asset_id} missing available_for_use_date")
+
+        comp_list = raw.get("source_components") or []
+        if not isinstance(comp_list, list) or not comp_list:
+            raise SystemExit(f"CCA asset {asset_id} missing source_components")
+
+        claim_percent = Decimal(str(raw.get("claim_percent_of_max", default_claim)))
+        half_year_rule = bool(raw.get("half_year_rule", default_half_year))
+
+        comps: list[AssetComponent] = []
+        for comp in comp_list:
+            if not isinstance(comp, dict):
+                continue
+            source_type = str(comp.get("source_type") or "").strip()
+            if not source_type:
+                raise SystemExit(f"CCA asset {asset_id} has component missing source_type")
+            wave_bill_id = comp.get("wave_bill_id")
+            account_code = str(comp.get("account_code") or "").strip() or None
+            amount_cents = int(comp.get("amount_cents") or 0)
+            notes = str(comp.get("notes") or "").strip() or None
+            comps.append(
+                AssetComponent(
+                    source_type=source_type,
+                    wave_bill_id=int(wave_bill_id) if wave_bill_id is not None else None,
+                    account_code=account_code,
+                    amount_cents=amount_cents,
+                    notes=notes,
+                )
+            )
+
+        assets.append(
+            Asset(
+                asset_id=asset_id,
+                description=desc,
+                cca_class=cca_class,
+                available_for_use_date=afu,
+                source_components=comps,
+                claim_percent_of_max=claim_percent,
+                half_year_rule=half_year_rule,
+                notes=str(raw.get("notes") or "").strip() or None,
+            )
+        )
+
+    return data, assets
+
+
+def resolve_component(conn, asset_id: str, comp: AssetComponent) -> ResolvedComponent:
+    if comp.source_type == "wave_bill_allocation":
+        if comp.wave_bill_id is None or comp.account_code is None:
+            raise SystemExit(f"CCA asset {asset_id} wave_bill_allocation requires wave_bill_id + account_code")
+        bill = conn.execute(
+            "SELECT id, invoice_date, vendor_raw, total_cents, tax_cents, net_cents FROM wave_bills WHERE id = ?",
+            (int(comp.wave_bill_id),),
+        ).fetchone()
+        if not bill:
+            raise SystemExit(f"CCA asset {asset_id}: missing wave_bill_id={comp.wave_bill_id}")
+
+        alloc_row = conn.execute(
+            "SELECT SUM(CAST(amount_cents AS INTEGER)) AS total_cents FROM bill_allocations WHERE wave_bill_id = ? AND account_code = ?",
+            (int(comp.wave_bill_id), comp.account_code),
+        ).fetchone()
+        alloc_total = int(alloc_row["total_cents"] or 0)
+        if alloc_total < comp.amount_cents:
+            raise SystemExit(
+                "CCA asset {asset_id}: wave_bill_allocation mismatch for bill {bill_id} account {account} "
+                "(expected >= {expected} cents, found {found} cents).".format(
+                    asset_id=asset_id,
+                    bill_id=comp.wave_bill_id,
+                    account=comp.account_code,
+                    expected=comp.amount_cents,
+                    found=alloc_total,
+                )
+            )
+
+        return ResolvedComponent(
+            source_type=comp.source_type,
+            wave_bill_id=comp.wave_bill_id,
+            account_code=comp.account_code,
+            amount_cents=comp.amount_cents,
+            invoice_date=str(bill["invoice_date"] or ""),
+            vendor_raw=str(bill["vendor_raw"] or ""),
+            allocation_total_cents=alloc_total,
+            notes=comp.notes,
+        )
+
+    raise SystemExit(f"CCA asset {asset_id}: unsupported source_type {comp.source_type}")
+
+
+def fy_for_date(fys, dt: date) -> str:
+    for fy in fys:
+        start = date.fromisoformat(fy.start_date)
+        end = date.fromisoformat(fy.end_date)
+        if start <= dt <= end:
+            return fy.fy
+    raise SystemExit(f"Date {dt.isoformat()} does not fall within any fiscal year in manifest")
+
+
+def build_schedule_8(
+    resolved_assets: list[ResolvedAsset],
+    fys,
+) -> dict[str, dict[str, dict[str, int | str | float]]]:
+    class_rates = {
+        "8": 0.20,
+        "50": 0.55,
+    }
+    class_desc = {
+        "8": "General equipment",
+        "50": "Computer hardware and systems software",
+    }
+
+    assets_by_fy: dict[str, list[ResolvedAsset]] = {}
+    for asset in resolved_assets:
+        assets_by_fy.setdefault(asset.fy, []).append(asset)
+
+    schedule_by_fy: dict[str, dict[str, dict[str, int | str | float]]] = {}
+    opening_ucc_by_class: dict[str, int] = {}
+
+    for fy in fys:
+        fy_assets = assets_by_fy.get(fy.fy, [])
+        additions_by_class: dict[str, int] = {}
+        half_year_additions_by_class: dict[str, Decimal] = {}
+        claim_percent_by_class: dict[str, Decimal] = {}
+
+        for asset in fy_assets:
+            class_key = str(asset.asset.cca_class)
+            additions_by_class[class_key] = additions_by_class.get(class_key, 0) + asset.total_cost_cents
+            factor = Decimal("0.5") if asset.asset.half_year_rule else Decimal("1.0")
+            half_year_additions_by_class[class_key] = half_year_additions_by_class.get(class_key, Decimal("0")) + (
+                Decimal(asset.total_cost_cents) / Decimal(100)
+            ) * factor
+
+            if class_key in claim_percent_by_class:
+                if claim_percent_by_class[class_key] != asset.asset.claim_percent_of_max:
+                    raise SystemExit(
+                        f"CCA asset class {class_key} in {fy.fy} has mixed claim_percent_of_max values; "
+                        "set a consistent value per class/year."
+                    )
+            else:
+                claim_percent_by_class[class_key] = asset.asset.claim_percent_of_max
+
+        classes = sorted(set(opening_ucc_by_class) | set(additions_by_class), key=lambda x: int(x) if str(x).isdigit() else 10**9)
+        fy_rows: dict[str, dict[str, int | str | float]] = {}
+        closing_ucc_by_class: dict[str, int] = {}
+
+        for class_key in classes:
+            if class_key not in class_rates:
+                raise SystemExit(f"Unknown CCA class rate for class {class_key}. Add it to the class_rates map.")
+            opening = opening_ucc_by_class.get(class_key, 0)
+            additions_cents = additions_by_class.get(class_key, 0)
+            additions_dollars = round_cents_to_dollar(additions_cents)
+            half_year_additions = half_year_additions_by_class.get(class_key, Decimal("0"))
+            base = Decimal(opening) + half_year_additions
+            rate = Decimal(str(class_rates[class_key]))
+            claim_percent = claim_percent_by_class.get(class_key, Decimal("1.0"))
+
+            cca_claim = round_to_dollar(base * rate * claim_percent)
+            closing = opening + additions_dollars - cca_claim
+
+            fy_rows[class_key] = {
+                "class": class_key,
+                "description": class_desc.get(class_key, ""),
+                "rate": float(class_rates[class_key]),
+                "opening_ucc": int(opening),
+                "additions": int(additions_dollars),
+                "dispositions": 0,
+                "half_year_base": round_to_dollar(base),
+                "cca_claim": int(cca_claim),
+                "closing_ucc": int(closing),
+            }
+
+            closing_ucc_by_class[class_key] = closing
+
+        schedule_by_fy[fy.fy] = fy_rows
+        opening_ucc_by_class = closing_ucc_by_class
+
+    return schedule_by_fy
+
+
+def write_schedule_8_csv(rows: dict[str, dict[str, int | str | float]], path: Path) -> None:
+    path.parent.mkdir(parents=True, exist_ok=True)
+    with path.open("w", newline="") as f:
+        w = csv.writer(f)
+        w.writerow(
+            [
+                "Class",
+                "Description",
+                "Rate",
+                "Opening_UCC",
+                "Additions",
+                "Dispositions",
+                "Half_year_base",
+                "CCA_Claim",
+                "Closing_UCC",
+            ]
+        )
+        for class_key, row in sorted(rows.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else 10**9):
+            w.writerow(
+                [
+                    row.get("class"),
+                    row.get("description"),
+                    row.get("rate"),
+                    row.get("opening_ucc"),
+                    row.get("additions"),
+                    row.get("dispositions"),
+                    row.get("half_year_base"),
+                    row.get("cca_claim"),
+                    row.get("closing_ucc"),
+                ]
+            )
+
+
+def write_resolved_assets_csv(resolved: list[ResolvedAsset], path: Path) -> None:
+    path.parent.mkdir(parents=True, exist_ok=True)
+    with path.open("w", newline="") as f:
+        w = csv.writer(f)
+        w.writerow(
+            [
+                "asset_id",
+                "description",
+                "cca_class",
+                "fiscal_year",
+                "available_for_use_date",
+                "total_cost_cents",
+                "total_cost_dollars",
+                "claim_percent_of_max",
+                "half_year_rule",
+                "source_breakdown",
+            ]
+        )
+        for ra in resolved:
+            parts = []
+            for comp in ra.resolved_components:
+                if comp.source_type == "wave_bill_allocation":
+                    parts.append(
+                        "wave_bill_allocation: bill_id={bill_id} invoice_date={date} vendor={vendor} "
+                        "account={account} amount_cents={amount} alloc_total_cents={alloc}".format(
+                            bill_id=comp.wave_bill_id,
+                            date=comp.invoice_date,
+                            vendor=comp.vendor_raw,
+                            account=comp.account_code,
+                            amount=comp.amount_cents,
+                            alloc=comp.allocation_total_cents,
+                        )
+                    )
+                else:
+                    parts.append(f"{comp.source_type}: amount_cents={comp.amount_cents}")
+            w.writerow(
+                [
+                    ra.asset.asset_id,
+                    ra.asset.description,
+                    ra.asset.cca_class,
+                    ra.fy,
+                    ra.asset.available_for_use_date,
+                    ra.total_cost_cents,
+                    round_cents_to_dollar(ra.total_cost_cents),
+                    str(ra.asset.claim_percent_of_max),
+                    "yes" if ra.asset.half_year_rule else "no",
+                    " | ".join(parts),
+                ]
+            )
+
+
+def main() -> int:
+    ap = argparse.ArgumentParser()
+    ap.add_argument("--db", type=Path, default=DB_PATH)
+    ap.add_argument("--assets", type=Path, default=ASSET_REGISTER_PATH)
+    ap.add_argument("--out-dir", type=Path, default=PROJECT_ROOT / "output")
+    args = ap.parse_args()
+
+    manifest = load_manifest()
+    fys = fiscal_years_from_manifest(manifest)
+    if not fys:
+        raise SystemExit("No fiscal_years found in manifest/sources.yml")
+
+    _, assets = load_assets(args.assets)
+
+    conn = connect_db(args.db)
+    resolved: list[ResolvedAsset] = []
+    try:
+        for asset in assets:
+            resolved_components: list[ResolvedComponent] = []
+            total_cost = 0
+            for comp in asset.source_components:
+                resolved_comp = resolve_component(conn, asset.asset_id, comp)
+                resolved_components.append(resolved_comp)
+                total_cost += int(comp.amount_cents)
+
+            dt = date.fromisoformat(asset.available_for_use_date)
+            fy = fy_for_date(fys, dt)
+
+            resolved.append(
+                ResolvedAsset(
+                    asset=asset,
+                    fy=fy,
+                    total_cost_cents=total_cost,
+                    resolved_components=resolved_components,
+                )
+            )
+    finally:
+        conn.close()
+
+    schedule_by_fy = build_schedule_8(resolved, fys)
+
+    args.out_dir.mkdir(parents=True, exist_ok=True)
+    for fy in fys:
+        write_schedule_8_csv(schedule_by_fy.get(fy.fy, {}), args.out_dir / f"schedule_8_{fy.fy}.csv")
+
+    write_resolved_assets_csv(resolved, args.out_dir / "cca_asset_register_resolved.csv")
+
+    print("CCA SCHEDULE 8 BUILT")
+    print(f"- out_dir: {args.out_dir}")
+    for fy in fys:
+        print(f"- {fy.fy}: schedule_8_{fy.fy}.csv")
+    print("- asset register: cca_asset_register_resolved.csv")
+    return 0
+
+
+if __name__ == "__main__":
+    raise SystemExit(main())
