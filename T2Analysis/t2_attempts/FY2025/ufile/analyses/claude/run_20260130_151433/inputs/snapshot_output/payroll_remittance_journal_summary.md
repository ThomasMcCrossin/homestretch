# Payroll remittance journals

- Scope: 2023-06-01 → 2025-05-31
- CRA payment journals posted: 18
- CRA rows skipped (non-payment or missing month): 1
- Reimbursement journals posted: 8

Notes:
- CRA `Payment <Month> <Year>` credits are allocated across CPP/EI/Tax using monthly payroll component ratios.
- If a CRA payment matches a bank txn categorized `PAYROLL_REMIT`, credit is bank.
- If it matches `PAYROLL_REIMBURSE` (or no bank match), credit is due-to-shareholder (default). Reimbursements clear that payable.
