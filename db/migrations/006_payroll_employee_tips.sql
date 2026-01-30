PRAGMA foreign_keys = ON;

-- Add tips to employee-level payroll exports (some CSVs include a Tips column).
ALTER TABLE payroll_employee_pay_periods ADD COLUMN tips_cents INTEGER NOT NULL DEFAULT 0;

