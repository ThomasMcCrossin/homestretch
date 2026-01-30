# Claude Analysis Run — FY2025 UFile T2 Attempt

**Run ID:** run_20260129_163122
**Analyst:** Claude (Opus 4.5)
**Date:** 2026-01-29

---

## Summary

This analysis diagnosed why the FY2025 UFile T2 filing attempt produced diagnostics and non-balancing schedules.

**Conclusion:** **Category A — UFile Entry Mechanics Errors**

The project-expected values are correct. All discrepancies trace to data entry mistakes in UFile.

---

## Directory Structure

```
run_20260129_163122/
├── README.md                  # This file
├── inputs/                    # Evidence files (copies)
│   ├── meta.json             # Parse metadata
│   ├── verification_report.md # Parse validation
│   ├── diagnostics.csv       # Parsed diagnostics
│   ├── schedule_100.csv      # Parsed balance sheet
│   ├── schedule_125.csv      # Parsed income statement
│   ├── retained_earnings.csv # Parsed RE schedule
│   ├── packet_fy2025.json    # Project expected values
│   └── UFILet2_FILL_GUIDE.md # Entry instructions
├── outputs/                   # Analysis outputs
│   ├── ATTEMPT_DIAGNOSIS.md  # Main report
│   ├── diagnostics.md        # Diagnostics catalogue
│   ├── recalculations.md     # Show-your-work arithmetic
│   └── attempt_vs_project_comparison.csv
└── work/                      # (empty - no intermediate files needed)
```

---

## How to Reproduce

1. **Verify parse bundle is current:**
   ```bash
   cat T2Analysis/t2_attempts/FY2025/ufile/parses/latest/verification_report.md
   # Should show "50 OK, 0 Not OK"
   ```

2. **Compare evidence sources:**
   - Source PDF: `T2Analysis/t2_attempts/FY2025/ufile/exports/latest/ufile_return.pdf`
   - Parsed tables: `T2Analysis/t2_attempts/FY2025/ufile/parses/latest/tables/`
   - Project packet: `UfileToFill/ufile_packet/years/FY2025/packet.json`

3. **Review the analysis:**
   - Main report: `outputs/ATTEMPT_DIAGNOSIS.md`
   - Detailed arithmetic: `outputs/recalculations.md`
   - Field-by-field comparison: `outputs/attempt_vs_project_comparison.csv`

---

## Key Findings

| Issue | Root Cause |
|-------|------------|
| Balance sheet imbalance ($36,054) | RE Start wrong, dividends missing |
| OpEx mismatch ($8,170) | Manual entry on line 9367 |
| Duplicate expense ($465) | Both 9220 and 9225 populated |

---

## Fix Actions for Next UFile Attempt

1. Clear manual entry on 9367 (let UFile auto-calculate)
2. Remove 9220 (Utilities) entry; keep only 9225
3. Change 3660 (RE Start) from $8,104 to **$16,656**
4. Enter 3700 (Dividends) = **$36,900**
5. Enter 3740 (Rounding) = **-1**
6. Recalculate and verify diagnostics clear

---

## Files Modified

None. This is a read-only diagnostic run.

---

## Contact

For questions about this analysis, see the main report at `outputs/ATTEMPT_DIAGNOSIS.md`.
