PRAGMA foreign_keys = ON;

-- Payroll exports imported from CSV working papers (employee-level and monthly rollups).

CREATE TABLE IF NOT EXISTS payroll_employee_pay_periods (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER NOT NULL,
  source_row INTEGER NOT NULL,
  employee_name TEXT NOT NULL,
  pay_period TEXT,
  pay_period_end TEXT NOT NULL,
  gross_pay_cents INTEGER NOT NULL DEFAULT 0,
  vacation_pay_cents INTEGER NOT NULL DEFAULT 0,
  federal_tax_cents INTEGER NOT NULL DEFAULT 0,
  provincial_tax_cents INTEGER NOT NULL DEFAULT 0,
  employee_cpp_cents INTEGER NOT NULL DEFAULT 0,
  employer_cpp_cents INTEGER NOT NULL DEFAULT 0,
  employee_ei_cents INTEGER NOT NULL DEFAULT 0,
  employer_ei_cents INTEGER NOT NULL DEFAULT 0,
  net_pay_cents INTEGER NOT NULL DEFAULT 0,
  our_remittance_cents INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source_file_id, source_row),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_payroll_employee_pay_periods_end ON payroll_employee_pay_periods(pay_period_end);
CREATE INDEX IF NOT EXISTS idx_payroll_employee_pay_periods_employee ON payroll_employee_pay_periods(employee_name);

CREATE TABLE IF NOT EXISTS payroll_monthly_totals (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER NOT NULL,
  source_row INTEGER NOT NULL,
  year INTEGER NOT NULL,
  month INTEGER NOT NULL, -- 1..12
  gross_pay_cents INTEGER NOT NULL DEFAULT 0,
  remittance_cents INTEGER NOT NULL DEFAULT 0,
  employer_taxes_cents INTEGER NOT NULL DEFAULT 0,
  net_pay_plus_tips_cents INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source_file_id, source_row),
  UNIQUE (year, month),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_payroll_monthly_totals_year_month ON payroll_monthly_totals(year, month);

