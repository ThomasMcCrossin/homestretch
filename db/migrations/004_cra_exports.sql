PRAGMA foreign_keys = ON;

-- CRA export tables (read-only external facts imported into SQLite for deterministic reports).

CREATE TABLE IF NOT EXISTS cra_hst_account_transactions (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER NOT NULL,
  source_row INTEGER NOT NULL,
  effective_date TEXT,
  period_end TEXT,
  period_end_raw TEXT,
  transaction_label TEXT NOT NULL,
  date_posted TEXT,
  amount_cents INTEGER NOT NULL,
  cr_dr TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source_file_id, source_row),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_cra_hst_period_end ON cra_hst_account_transactions(period_end);
CREATE INDEX IF NOT EXISTS idx_cra_hst_effective_date ON cra_hst_account_transactions(effective_date);

CREATE TABLE IF NOT EXISTS cra_payroll_account_transactions (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER NOT NULL,
  source_row INTEGER NOT NULL,
  date_posted TEXT,
  transaction_label TEXT NOT NULL,
  date_received TEXT,
  amount_cents INTEGER NOT NULL,
  cr_dr TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source_file_id, source_row),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_cra_payroll_date_posted ON cra_payroll_account_transactions(date_posted);

CREATE TABLE IF NOT EXISTS cra_arrears_account_transactions (
  id INTEGER PRIMARY KEY,
  source_file_id INTEGER NOT NULL,
  source_row INTEGER NOT NULL,
  date_posted TEXT,
  transaction_label TEXT NOT NULL,
  date_received TEXT,
  amount_cents INTEGER NOT NULL,
  cr_dr TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source_file_id, source_row),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_cra_arrears_date_posted ON cra_arrears_account_transactions(date_posted);
