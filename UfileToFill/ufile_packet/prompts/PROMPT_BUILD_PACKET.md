# Prompt: Build UFile T2 Filing Packet

Use this prompt to instruct an LLM to build or update `packet.json` from a given snapshot folder.

---

## Prompt

```
You are building a UFile T2 Filing Packet for Canadian corporate tax filing.

## CRITICAL RULES (NON-NEGOTIABLE)
1. DO NOT modify any existing accounting data or source files.
2. DO NOT invent, estimate, or hallucinate any numbers. If a value is missing, mark it explicitly as "TODO" with what evidence is needed.
3. All amounts must be sourced from the provided snapshot files. Cite the exact file path for every value.
4. Round all GIFI amounts to whole dollars (standard rounding).
5. Every judgment or estimate must be documented in the `known_judgments` array with evidence references.

## INPUT
Source snapshot folder: [SPECIFY PATH]

## FILES TO READ (in order)
1. `gifi_schedule_100_FY{YEAR}.csv` - Balance sheet GIFI codes
2. `gifi_schedule_125_FY{YEAR}.csv` - Income statement GIFI codes
3. `gifi_retained_earnings_FY{YEAR}.csv` - Retained earnings schedule
4. `schedule_1_FY{YEAR}.csv` - Net income reconciliation
5. `readiness_report.md` - Bank reconciliation and status
6. `SHAREHOLDER_EQUITY_POSITION.md` (in docs/) - Shareholder balances
7. `trial_balance_FY{YEAR}.csv` - For additional detail if needed

## OUTPUT
Generate `packet.json` following the schema at `schema/packet_schema.json`.

## REQUIRED SECTIONS

### 1. meta
- schema_version: "1.0.0"
- generated_at: Current ISO 8601 timestamp
- snapshot_source: Exact path to snapshot
- generator: "LLM: [model name]"

### 2. entity
- legal_name: From existing packet or corporate records
- bn: Business number (9 digits + RC + 4 digits)
- jurisdiction: Province code
- year_end_month_day: "MM-DD" format
- corp_type: "CCPC" for Canadian-controlled private corporations
- shareholders: Array of shareholders with 10%+ ownership

### 3. years
For each fiscal year (FY2024, FY2025, etc.):
- fiscal_period: start/end dates
- schedule_100: GIFI codes for balance sheet (only non-zero lines)
- schedule_125: GIFI codes for income statement (only non-zero lines)
- retained_earnings: GIFI 3660-3849
- schedule_1: Lines 300, 117, 311, 400 (and any other add-backs)
- positions: Key tax positions (IFRS, inventory method, etc.)
- cross_checks: Validation equations that must pass

### 4. evidence_index
List every source file used with category, path, and description.

### 5. known_judgments
Document any estimates, assumptions, or judgments with:
- area: Short identifier
- description: What the judgment is
- approach: How it was handled
- evidence: Path to supporting documentation
- risk_level: "low", "medium", or "high"

## VALIDATION REQUIREMENTS
Before finalizing, verify:
1. Total Assets (2599) = Total L+E (3640) for each year
2. RE End = RE Start + NI - Dividends +/- Other
3. Net Income (9999) = Revenue (8299) - Expenses (9368)
4. Schedule 1 code C = code A + additions - deductions
5. All GIFI codes exist in standard CRA GIFI list

## DO NOT
- Create new accounting entries
- Modify source CSV files
- Guess missing values
- Change amounts without evidence
- Include GIFI lines with $0 amounts (unless totals)
```

---

## Usage

1. Copy the prompt above
2. Replace `[SPECIFY PATH]` with the actual snapshot path
3. Replace `[model name]` with the LLM being used
4. Run the prompt with access to read the specified files
5. Review output for any "TODO" markers before using

---

## Post-Generation Checklist

- [ ] All GIFI amounts match source CSVs exactly
- [ ] Cross-checks all pass
- [ ] No TODO markers remain (or document why they're pending)
- [ ] evidence_index covers all major areas
- [ ] known_judgments documents any estimates
- [ ] JSON validates against schema
