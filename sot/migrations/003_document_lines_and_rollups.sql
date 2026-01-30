PRAGMA foreign_keys = ON;

-- =========================
-- Document line provenance
-- =========================

ALTER TABLE document_lines ADD COLUMN notes TEXT;

-- =========================
-- Chart of accounts enrichment (curlys-books export compatibility)
-- =========================

ALTER TABLE chart_of_accounts ADD COLUMN parent_code TEXT;
ALTER TABLE chart_of_accounts ADD COLUMN t2125_line TEXT;
ALTER TABLE chart_of_accounts ADD COLUMN is_active INTEGER;
ALTER TABLE chart_of_accounts ADD COLUMN requires_receipt INTEGER;
ALTER TABLE chart_of_accounts ADD COLUMN is_tax_account INTEGER;

-- =========================
-- Account rollups (Wave-style normalization layer)
-- =========================

CREATE TABLE IF NOT EXISTS account_rollups (
  rollup_code TEXT PRIMARY KEY,
  rollup_name TEXT NOT NULL,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS account_rollup_members (
  id INTEGER PRIMARY KEY,
  account_code TEXT NOT NULL,
  rollup_code TEXT NOT NULL,
  method TEXT, -- MANUAL | AUTO_PARENT | AUTO_GIFI | OTHER
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(account_code, rollup_code),
  FOREIGN KEY(account_code) REFERENCES chart_of_accounts(account_code),
  FOREIGN KEY(rollup_code) REFERENCES account_rollups(rollup_code)
);

CREATE INDEX IF NOT EXISTS idx_account_rollup_members_rollup ON account_rollup_members(rollup_code);
CREATE INDEX IF NOT EXISTS idx_account_rollup_members_account ON account_rollup_members(account_code);

