-- SQLite schema for the standalone T2-final workspace.
-- Facts are imported once; allocations/classifications are stored separately.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS migrations (
  id INTEGER PRIMARY KEY,
  filename TEXT NOT NULL UNIQUE,
  applied_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS source_files (
  id INTEGER PRIMARY KEY,
  source_key TEXT NOT NULL UNIQUE,
  kind TEXT NOT NULL,
  path TEXT NOT NULL,
  sha256 TEXT,
  semantics TEXT,
  loaded_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS fiscal_years (
  fy TEXT PRIMARY KEY,
  start_date TEXT NOT NULL,
  end_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS wave_bills (
  id INTEGER PRIMARY KEY,
  invoice_date TEXT NOT NULL,
  vendor_raw TEXT NOT NULL,
  vendor_norm TEXT NOT NULL,
  vendor_key TEXT,
  invoice_number TEXT,
  total_cents INTEGER NOT NULL,
  tax_cents INTEGER NOT NULL DEFAULT 0,
  net_cents INTEGER NOT NULL DEFAULT 0,
  source_file_id INTEGER,
  source_row INTEGER,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_wave_bills_invoice_date ON wave_bills(invoice_date);
CREATE INDEX IF NOT EXISTS idx_wave_bills_vendor_key ON wave_bills(vendor_key);
CREATE INDEX IF NOT EXISTS idx_wave_bills_invoice_number ON wave_bills(invoice_number);

-- External receipt samples imported from curlys-books Postgres (read-only source).
CREATE TABLE IF NOT EXISTS external_receipts (
  id INTEGER PRIMARY KEY,
  source TEXT NOT NULL,
  source_receipt_id TEXT NOT NULL,
  entity TEXT NOT NULL,
  vendor TEXT,
  receipt_date TEXT NOT NULL,
  subtotal_cents INTEGER NOT NULL,
  tax_cents INTEGER NOT NULL,
  total_cents INTEGER NOT NULL,
  receipt_number TEXT,
  invoice_number TEXT,
  status TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (source, source_receipt_id)
);

CREATE INDEX IF NOT EXISTS idx_external_receipts_vendor ON external_receipts(vendor);
CREATE INDEX IF NOT EXISTS idx_external_receipts_date ON external_receipts(receipt_date);

CREATE TABLE IF NOT EXISTS external_receipt_line_items (
  id INTEGER PRIMARY KEY,
  receipt_id INTEGER NOT NULL,
  line_number INTEGER NOT NULL,
  description TEXT NOT NULL,
  line_total_cents INTEGER NOT NULL,
  account_code TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (receipt_id) REFERENCES external_receipts(id) ON DELETE CASCADE,
  UNIQUE (receipt_id, line_number)
);

CREATE INDEX IF NOT EXISTS idx_external_rli_account_code ON external_receipt_line_items(account_code);

-- Vendor profile derived from receipt samples (percent splits by account_code).
CREATE TABLE IF NOT EXISTS vendor_profiles (
  id INTEGER PRIMARY KEY,
  vendor_key TEXT NOT NULL,
  entity TEXT NOT NULL DEFAULT 'corp',
  method TEXT NOT NULL, -- e.g., CURB_PG_SAMPLE
  sample_receipts INTEGER NOT NULL,
  sample_line_items INTEGER NOT NULL,
  sample_total_cents INTEGER NOT NULL,
  sample_start_date TEXT,
  sample_end_date TEXT,
  uncategorized_cents INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_vendor_profiles_vendor_key ON vendor_profiles(vendor_key);

CREATE TABLE IF NOT EXISTS vendor_profile_splits (
  id INTEGER PRIMARY KEY,
  profile_id INTEGER NOT NULL,
  account_code TEXT NOT NULL,
  percent REAL NOT NULL,
  sample_amount_cents INTEGER NOT NULL,
  FOREIGN KEY (profile_id) REFERENCES vendor_profiles(id) ON DELETE CASCADE,
  UNIQUE (profile_id, account_code)
);

-- Optional: match Wave bills to detailed receipts when deterministically possible.
CREATE TABLE IF NOT EXISTS bill_detail_links (
  id INTEGER PRIMARY KEY,
  wave_bill_id INTEGER NOT NULL UNIQUE,
  receipt_id INTEGER NOT NULL,
  match_confidence TEXT NOT NULL,
  match_method TEXT NOT NULL,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (wave_bill_id) REFERENCES wave_bills(id) ON DELETE CASCADE,
  FOREIGN KEY (receipt_id) REFERENCES external_receipts(id) ON DELETE CASCADE
);

-- Final allocations for Wave bills into account_codes (detail or profile estimate).
CREATE TABLE IF NOT EXISTS bill_allocations (
  id INTEGER PRIMARY KEY,
  wave_bill_id INTEGER NOT NULL,
  account_code TEXT NOT NULL,
  amount_cents INTEGER NOT NULL,
  method TEXT NOT NULL, -- DETAIL_MATCH | VENDOR_PROFILE_ESTIMATE | TAX_ITC
  profile_id INTEGER,
  receipt_id INTEGER,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (wave_bill_id) REFERENCES wave_bills(id) ON DELETE CASCADE,
  FOREIGN KEY (profile_id) REFERENCES vendor_profiles(id) ON DELETE SET NULL,
  FOREIGN KEY (receipt_id) REFERENCES external_receipts(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_bill_allocations_bill ON bill_allocations(wave_bill_id);
CREATE INDEX IF NOT EXISTS idx_bill_allocations_account ON bill_allocations(account_code);

