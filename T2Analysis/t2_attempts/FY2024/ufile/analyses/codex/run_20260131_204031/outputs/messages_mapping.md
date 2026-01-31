# UFile messages mapping

- FY: `FY2024`
- Attempt: `attempt_001`
- Source: `/home/clarencehub/t2-final-fy2024-fy2025/T2Analysis/t2_attempts/FY2024/ufile/analyses/codex/run_20260131_204031/inputs/messages.txt`

## Message: Depreciation has been entered but CCA class is missing - verify
**Likely screen(s):** Capital cost allowance / Schedule 8 (CCA classes).

**What it usually means:** a depreciation/CCA amount exists, but the CCA class for at least one asset/addition is not selected/filled.

**Project expectation for this FY:** project Schedule 8 exists and should be entered as:
- Total CCA claimed (Schedule 8): `330`; classes: `8`

**Next UI actions (most likely):**
- Go to **Capital cost allowance** screen and enter the class/additions/claim per the fill guide’s Schedule 8 table.
- If you already entered assets, ensure each asset/addition has a **CCA class** selected (e.g. Class 8) and that the claim rolls to Schedule 1 line 403.

## Message: There is no entry in the income source section; all income is considered as active business income
**Likely screen(s):** Income source.

**What it means:** UFile will treat all income as **active business income** unless you explicitly enter other sources.

**Next UI actions:**
- On **Income source**, confirm **Active business income** is selected and no other sources apply (property/foreign/etc.).

## Message: No instalments required since total tax instalments calculated are less than or equal to $3,000
**Likely screen(s):** Instalments paid / instalment requirement summary.

**Meaning:** informational; nothing to enter unless you actually made instalment payments.
