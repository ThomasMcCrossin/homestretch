PRAGMA foreign_keys = ON;

-- Canonical payroll backfill data lives in curlys-books Postgres.
-- We mirror the key tables/fields here in SQLite for deterministic T2 work.

CREATE TABLE IF NOT EXISTS curlysbooks_pay_periods (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER,
  pay_period_id TEXT NOT NULL UNIQUE, -- uuid
  entity TEXT NOT NULL,
  tax_year INTEGER NOT NULL,
  period_number INTEGER,
  pay_frequency TEXT,
  start_date TEXT,
  end_date TEXT,
  pay_date TEXT,
  status TEXT,
  closed_at TEXT,
  created_at TEXT,
  imported_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_curlysbooks_pay_periods_entity_year ON curlysbooks_pay_periods(entity, tax_year);
CREATE INDEX IF NOT EXISTS idx_curlysbooks_pay_periods_end_date ON curlysbooks_pay_periods(end_date);
CREATE INDEX IF NOT EXISTS idx_curlysbooks_pay_periods_pay_date ON curlysbooks_pay_periods(pay_date);

CREATE TABLE IF NOT EXISTS curlysbooks_payroll_runs (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER,
  payroll_run_id TEXT NOT NULL UNIQUE, -- uuid
  pay_period_id TEXT NOT NULL, -- uuid
  run_number INTEGER,
  status TEXT,
  calculated_by TEXT,
  calculated_at TEXT,
  employee_count INTEGER,
  total_gross_cents INTEGER NOT NULL DEFAULT 0,
  total_vacation_pay_cents INTEGER NOT NULL DEFAULT 0,
  total_tips_cents INTEGER NOT NULL DEFAULT 0,
  total_cpp_cents INTEGER NOT NULL DEFAULT 0,
  total_cpp2_cents INTEGER NOT NULL DEFAULT 0,
  total_ei_cents INTEGER NOT NULL DEFAULT 0,
  total_federal_tax_cents INTEGER NOT NULL DEFAULT 0,
  total_provincial_tax_cents INTEGER NOT NULL DEFAULT 0,
  total_deductions_cents INTEGER NOT NULL DEFAULT 0,
  total_net_cents INTEGER NOT NULL DEFAULT 0,
  total_employer_cpp_cents INTEGER NOT NULL DEFAULT 0,
  total_employer_cpp2_cents INTEGER NOT NULL DEFAULT 0,
  total_employer_ei_cents INTEGER NOT NULL DEFAULT 0,
  total_employer_cost_cents INTEGER NOT NULL DEFAULT 0,
  imported_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id),
  FOREIGN KEY (pay_period_id) REFERENCES curlysbooks_pay_periods(pay_period_id)
);

CREATE INDEX IF NOT EXISTS idx_curlysbooks_payroll_runs_period ON curlysbooks_payroll_runs(pay_period_id);
CREATE INDEX IF NOT EXISTS idx_curlysbooks_payroll_runs_calculated_by ON curlysbooks_payroll_runs(calculated_by);

CREATE TABLE IF NOT EXISTS curlysbooks_ytd_accumulations (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER,
  accumulation_id TEXT NOT NULL UNIQUE, -- uuid
  employee_id TEXT NOT NULL, -- uuid
  employee_name TEXT,
  entity TEXT NOT NULL,
  tax_year INTEGER NOT NULL,
  gross_earnings_cents INTEGER NOT NULL DEFAULT 0,
  cpp_contributions_cents INTEGER NOT NULL DEFAULT 0,
  cpp2_contributions_cents INTEGER NOT NULL DEFAULT 0,
  ei_contributions_cents INTEGER NOT NULL DEFAULT 0,
  federal_tax_cents INTEGER NOT NULL DEFAULT 0,
  provincial_tax_cents INTEGER NOT NULL DEFAULT 0,
  employer_cpp_cents INTEGER NOT NULL DEFAULT 0,
  employer_cpp2_cents INTEGER NOT NULL DEFAULT 0,
  employer_ei_cents INTEGER NOT NULL DEFAULT 0,
  tips_received_cents INTEGER NOT NULL DEFAULT 0,
  vacation_pay_accrued_cents INTEGER NOT NULL DEFAULT 0,
  vacation_pay_taken_cents INTEGER NOT NULL DEFAULT 0,
  updated_at TEXT,
  imported_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_curlysbooks_ytd_entity_year ON curlysbooks_ytd_accumulations(entity, tax_year);

