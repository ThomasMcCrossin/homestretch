PRAGMA foreign_keys = ON;

-- Portability guardrail:
-- Mirror core curlys-books accounting primitives so we can export/import with minimal friction.

CREATE TABLE IF NOT EXISTS chart_of_accounts (
  account_code TEXT PRIMARY KEY,
  account_name TEXT NOT NULL,
  account_type TEXT NOT NULL,
  parent_code TEXT,
  gifi_code TEXT,
  t2125_line TEXT,
  is_active INTEGER,
  requires_receipt INTEGER,
  is_tax_account INTEGER,
  created_at TEXT,
  updated_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_chart_of_accounts_account_type ON chart_of_accounts(account_type);
CREATE INDEX IF NOT EXISTS idx_chart_of_accounts_gifi_code ON chart_of_accounts(gifi_code);
CREATE INDEX IF NOT EXISTS idx_chart_of_accounts_t2125_line ON chart_of_accounts(t2125_line);

CREATE TABLE IF NOT EXISTS journal_entries (
  id TEXT PRIMARY KEY,
  entity TEXT NOT NULL DEFAULT 'corp',
  entry_number TEXT,
  entry_date TEXT NOT NULL,
  entry_type TEXT NOT NULL,
  description TEXT,
  source_receipt_id TEXT,
  source_bank_line_id TEXT,
  source_bill_id TEXT,
  is_posted INTEGER NOT NULL DEFAULT 0,
  posted_at TEXT,
  posted_by TEXT,
  is_void INTEGER NOT NULL DEFAULT 0,
  void_reason TEXT,
  voided_at TEXT,
  voided_by TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  source_system TEXT,
  source_record_type TEXT,
  source_record_id TEXT,
  notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_journal_entries_entry_date ON journal_entries(entry_date);
CREATE INDEX IF NOT EXISTS idx_journal_entries_entity ON journal_entries(entity);
CREATE INDEX IF NOT EXISTS idx_journal_entries_source_record ON journal_entries(source_system, source_record_type, source_record_id);

CREATE TABLE IF NOT EXISTS journal_entry_lines (
  id TEXT PRIMARY KEY,
  journal_entry_id TEXT NOT NULL,
  line_number INTEGER NOT NULL,
  account_code TEXT NOT NULL,
  debit_cents INTEGER NOT NULL DEFAULT 0,
  credit_cents INTEGER NOT NULL DEFAULT 0,
  description TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (journal_entry_id) REFERENCES journal_entries(id) ON DELETE CASCADE,
  FOREIGN KEY (account_code) REFERENCES chart_of_accounts(account_code)
);

CREATE INDEX IF NOT EXISTS idx_journal_entry_lines_entry ON journal_entry_lines(journal_entry_id);
CREATE INDEX IF NOT EXISTS idx_journal_entry_lines_account ON journal_entry_lines(account_code);

