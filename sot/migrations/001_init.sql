PRAGMA foreign_keys = ON;

-- =========================
-- Schema metadata
-- =========================

CREATE TABLE IF NOT EXISTS schema_migrations (
  version INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  applied_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- =========================
-- Sources / entities / accounts
-- =========================

CREATE TABLE IF NOT EXISTS source_files (
  id INTEGER PRIMARY KEY,
  source_key TEXT NOT NULL UNIQUE,
  kind TEXT NOT NULL,
  path TEXT NOT NULL,
  sha256 TEXT,
  semantics TEXT,
  imported_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS entities (
  id INTEGER PRIMARY KEY,
  entity_key TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS accounts (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  account_key TEXT NOT NULL,
  account_type TEXT NOT NULL, -- BANK | CREDIT_CARD | DEBIT_CARD | CASH
  name TEXT NOT NULL,
  currency TEXT NOT NULL DEFAULT 'CAD',
  external_ref TEXT,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(entity_id, account_key),
  FOREIGN KEY(entity_id) REFERENCES entities(id)
);

CREATE INDEX IF NOT EXISTS idx_accounts_entity_type ON accounts(entity_id, account_type);

-- Canonical statement lines across *all* financial accounts (bank + cards + cash pseudo-account).
CREATE TABLE IF NOT EXISTS account_transactions (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  account_id INTEGER NOT NULL,
  txn_date TEXT NOT NULL,      -- YYYY-MM-DD
  posted_date TEXT,            -- optional
  description TEXT NOT NULL,
  amount_cents INTEGER NOT NULL,  -- signed: +inflow, -outflow (as represented on that account statement)
  debit_cents INTEGER,            -- optional (raw representation)
  credit_cents INTEGER,           -- optional (raw representation)
  txn_type TEXT,
  counterparty_raw TEXT,
  reference TEXT,
  source_system TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  source_file_id INTEGER,
  raw_json TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(source_system, source_record_id),
  FOREIGN KEY(entity_id) REFERENCES entities(id),
  FOREIGN KEY(account_id) REFERENCES accounts(id),
  FOREIGN KEY(source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_account_txn_account_date ON account_transactions(account_id, txn_date);
CREATE INDEX IF NOT EXISTS idx_account_txn_entity_date ON account_transactions(entity_id, txn_date);
CREATE INDEX IF NOT EXISTS idx_account_txn_amount ON account_transactions(amount_cents);

-- =========================
-- Counterparties / documents
-- =========================

CREATE TABLE IF NOT EXISTS counterparties (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  normalized_name TEXT NOT NULL,
  kind TEXT NOT NULL DEFAULT 'OTHER', -- VENDOR | PERSON | GOV | PLATFORM | OTHER
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(normalized_name, kind)
);

CREATE TABLE IF NOT EXISTS counterparty_aliases (
  id INTEGER PRIMARY KEY,
  counterparty_id INTEGER NOT NULL,
  alias_text TEXT NOT NULL,
  alias_normalized TEXT NOT NULL,
  source_system TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(counterparty_id, alias_normalized),
  FOREIGN KEY(counterparty_id) REFERENCES counterparties(id)
);

CREATE INDEX IF NOT EXISTS idx_counterparty_alias_norm ON counterparty_aliases(alias_normalized);

-- Generic “documents” (Wave bills, vendor invoices/credit memos, tax remittances, settlement statements, etc.).
CREATE TABLE IF NOT EXISTS documents (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  counterparty_id INTEGER,
  doc_type TEXT NOT NULL,     -- BILL | CREDIT_MEMO | SETTLEMENT | TAX | PAYROLL | ADJUSTMENT | OTHER
  doc_date TEXT,             -- YYYY-MM-DD
  due_date TEXT,             -- YYYY-MM-DD
  doc_number TEXT,           -- invoice number / reference
  currency TEXT NOT NULL DEFAULT 'CAD',
  total_cents INTEGER,
  tax_cents INTEGER,
  net_cents INTEGER,
  status TEXT,               -- OPEN | PAID | UNKNOWN
  source_system TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  source_file_id INTEGER,
  raw_json TEXT,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(source_system, source_record_id),
  FOREIGN KEY(entity_id) REFERENCES entities(id),
  FOREIGN KEY(counterparty_id) REFERENCES counterparties(id),
  FOREIGN KEY(source_file_id) REFERENCES source_files(id)
);

CREATE INDEX IF NOT EXISTS idx_documents_entity_date ON documents(entity_id, doc_date);
CREATE INDEX IF NOT EXISTS idx_documents_counterparty_number ON documents(counterparty_id, doc_number);

-- Optional category breakdown of a document (used for invoice parsing or vendor-profile estimates).
CREATE TABLE IF NOT EXISTS document_lines (
  id INTEGER PRIMARY KEY,
  document_id INTEGER NOT NULL,
  line_no INTEGER NOT NULL,
  description TEXT,
  account_code TEXT NOT NULL,     -- chart-of-accounts code used in this project (not necessarily curlys-books)
  amount_cents INTEGER NOT NULL,  -- signed: +charge, -credit
  tax_cents INTEGER,
  method TEXT NOT NULL,           -- PARSED | PROFILE_ESTIMATE | MANUAL
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(document_id, line_no),
  FOREIGN KEY(document_id) REFERENCES documents(id)
);

CREATE INDEX IF NOT EXISTS idx_document_lines_account ON document_lines(account_code);

-- =========================
-- Reconciliation layer (links are the “work”)
-- =========================

-- Multiple classifications can exist per txn from different namespaces/sources.
CREATE TABLE IF NOT EXISTS txn_classifications (
  id INTEGER PRIMARY KEY,
  txn_id INTEGER NOT NULL,
  namespace TEXT NOT NULL,   -- e.g. FRESHER_DEBIT | FRESHER_CREDIT | USER | IMPORTED_NOTE
  category TEXT NOT NULL,    -- e.g. VENDOR_PAD, CC_PAYMENT, HST_REMIT, SHOPIFY_PAYOUT, CASH_DEPOSIT, etc.
  counterparty_id INTEGER,
  explanation TEXT,
  confidence INTEGER,        -- 0..100
  is_verified INTEGER NOT NULL DEFAULT 0,
  role TEXT NOT NULL DEFAULT 'EVIDENCE', -- EVIDENCE | CANONICAL
  method TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(txn_id) REFERENCES account_transactions(id),
  FOREIGN KEY(counterparty_id) REFERENCES counterparties(id)
);

CREATE INDEX IF NOT EXISTS idx_txn_class_txn ON txn_classifications(txn_id);
CREATE INDEX IF NOT EXISTS idx_txn_class_cat ON txn_classifications(category);

-- Allocate an account transaction to one or more documents (splits supported).
-- Convention: allocation.amount_cents should have the same sign as the txn amount.
CREATE TABLE IF NOT EXISTS txn_document_allocations (
  id INTEGER PRIMARY KEY,
  txn_id INTEGER NOT NULL,
  document_id INTEGER NOT NULL,
  amount_cents INTEGER NOT NULL,
  allocation_type TEXT NOT NULL,  -- PAYMENT | REIMBURSEMENT | TRANSFER_COMPONENT | OTHER
  confidence INTEGER,             -- 0..100
  is_verified INTEGER NOT NULL DEFAULT 0,
  role TEXT NOT NULL DEFAULT 'EVIDENCE', -- EVIDENCE | CANONICAL
  method TEXT,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(txn_id) REFERENCES account_transactions(id),
  FOREIGN KEY(document_id) REFERENCES documents(id)
);

CREATE INDEX IF NOT EXISTS idx_txn_doc_alloc_txn ON txn_document_allocations(txn_id);
CREATE INDEX IF NOT EXISTS idx_txn_doc_alloc_doc ON txn_document_allocations(document_id);

-- Links between transactions (bank→card payment, card payment→purchase allocation, internal transfers, etc.).
CREATE TABLE IF NOT EXISTS txn_links (
  id INTEGER PRIMARY KEY,
  from_txn_id INTEGER NOT NULL,
  to_txn_id INTEGER NOT NULL,
  link_type TEXT NOT NULL, -- BANK_TO_CARD_PAYMENT | CARD_PAYMENT_TO_PURCHASE | INTERNAL_TRANSFER | OTHER
  amount_cents INTEGER NOT NULL,
  confidence INTEGER,
  is_verified INTEGER NOT NULL DEFAULT 0,
  role TEXT NOT NULL DEFAULT 'EVIDENCE', -- EVIDENCE | CANONICAL
  method TEXT,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(from_txn_id) REFERENCES account_transactions(id),
  FOREIGN KEY(to_txn_id) REFERENCES account_transactions(id)
);

CREATE INDEX IF NOT EXISTS idx_txn_links_from ON txn_links(from_txn_id);
CREATE INDEX IF NOT EXISTS idx_txn_links_to ON txn_links(to_txn_id);

-- =========================
-- Settlement statements (GFS EFT, Shopify payouts, etc.)
-- =========================

CREATE TABLE IF NOT EXISTS settlement_batches (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  counterparty_id INTEGER,
  settlement_type TEXT NOT NULL, -- GFS_EFT | SHOPIFY_PAYOUT | NAYAX_PAYOUT | OTHER
  statement_date TEXT,           -- YYYY-MM-DD
  due_date TEXT,                 -- YYYY-MM-DD
  total_cents INTEGER NOT NULL,
  currency TEXT NOT NULL DEFAULT 'CAD',
  source_system TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  source_file_id INTEGER,
  raw_text TEXT,
  raw_json TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(source_system, source_record_id),
  FOREIGN KEY(entity_id) REFERENCES entities(id),
  FOREIGN KEY(counterparty_id) REFERENCES counterparties(id),
  FOREIGN KEY(source_file_id) REFERENCES source_files(id)
);

CREATE TABLE IF NOT EXISTS settlement_lines (
  id INTEGER PRIMARY KEY,
  batch_id INTEGER NOT NULL,
  line_no INTEGER NOT NULL,
  external_doc_number TEXT,   -- invoice number / credit memo number
  line_type TEXT NOT NULL,    -- INVOICE | CREDIT_MEMO | FEE | OTHER
  amount_cents INTEGER NOT NULL,
  txn_date TEXT,
  due_date TEXT,
  description TEXT,
  linked_document_id INTEGER, -- optional (if we have a Wave bill / placeholder doc)
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(batch_id, line_no),
  FOREIGN KEY(batch_id) REFERENCES settlement_batches(id),
  FOREIGN KEY(linked_document_id) REFERENCES documents(id)
);

CREATE INDEX IF NOT EXISTS idx_settlement_lines_docno ON settlement_lines(external_doc_number);
CREATE INDEX IF NOT EXISTS idx_settlement_lines_linked_doc ON settlement_lines(linked_document_id);

CREATE TABLE IF NOT EXISTS settlement_batch_txn_links (
  id INTEGER PRIMARY KEY,
  batch_id INTEGER NOT NULL,
  txn_id INTEGER NOT NULL,
  link_type TEXT NOT NULL,  -- MATCHED_BY_DUE_DATE_AMOUNT | MANUAL | OTHER
  confidence INTEGER,
  is_verified INTEGER NOT NULL DEFAULT 0,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(batch_id, txn_id),
  FOREIGN KEY(batch_id) REFERENCES settlement_batches(id),
  FOREIGN KEY(txn_id) REFERENCES account_transactions(id)
);

-- =========================
-- Cash deposit expectations (credit-side)
-- =========================

CREATE TABLE IF NOT EXISTS cash_deposit_groups (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  group_date TEXT NOT NULL, -- YYYY-MM-DD
  effective_cash_deposit_cents INTEGER NOT NULL,
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(entity_id) REFERENCES entities(id)
);

CREATE TABLE IF NOT EXISTS cash_deposit_group_txns (
  id INTEGER PRIMARY KEY,
  cash_deposit_group_id INTEGER NOT NULL,
  txn_id INTEGER NOT NULL,
  role TEXT NOT NULL, -- DEPOSIT | CORRECTION | INTERNAL_TRANSFER_OUT | OTHER
  notes TEXT,
  UNIQUE(cash_deposit_group_id, txn_id, role),
  FOREIGN KEY(cash_deposit_group_id) REFERENCES cash_deposit_groups(id),
  FOREIGN KEY(txn_id) REFERENCES account_transactions(id)
);

-- Raw Shopify “Net payments by gateway” report data (for cash/PayPal expectations).
CREATE TABLE IF NOT EXISTS gateway_reports (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  report_start TEXT,
  report_end TEXT,
  report_name TEXT,
  source_system TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  source_file_id INTEGER,
  raw_json TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(source_system, source_record_id),
  FOREIGN KEY(entity_id) REFERENCES entities(id),
  FOREIGN KEY(source_file_id) REFERENCES source_files(id)
);

CREATE TABLE IF NOT EXISTS gateway_report_rows (
  id INTEGER PRIMARY KEY,
  report_id INTEGER NOT NULL,
  source_row TEXT,
  payment_gateway TEXT,
  net_payments_cents INTEGER,
  gross_payments_cents INTEGER,
  refunded_payments_cents INTEGER,
  raw_json TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(report_id) REFERENCES gateway_reports(id)
);

CREATE INDEX IF NOT EXISTS idx_gateway_rows_gateway ON gateway_report_rows(payment_gateway);

-- =========================
-- Accounting layer (for TB/GIFI downstream)
-- =========================

CREATE TABLE IF NOT EXISTS chart_of_accounts (
  account_code TEXT PRIMARY KEY,
  account_name TEXT NOT NULL,
  account_type TEXT,  -- asset/liability/equity/revenue/expense
  gifi_code TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS journal_entries (
  id INTEGER PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  entry_date TEXT NOT NULL,
  description TEXT NOT NULL,
  source_system TEXT,
  source_record_id TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY(entity_id) REFERENCES entities(id)
);

-- Only enforce uniqueness when a source pair is provided (allows multiple manual entries).
CREATE UNIQUE INDEX IF NOT EXISTS idx_journal_entries_source_unique
ON journal_entries(source_system, source_record_id)
WHERE source_system IS NOT NULL AND source_record_id IS NOT NULL;

CREATE TABLE IF NOT EXISTS journal_entry_lines (
  id INTEGER PRIMARY KEY,
  journal_entry_id INTEGER NOT NULL,
  account_code TEXT NOT NULL,
  debit_cents INTEGER NOT NULL DEFAULT 0,
  credit_cents INTEGER NOT NULL DEFAULT 0,
  memo TEXT,
  FOREIGN KEY(journal_entry_id) REFERENCES journal_entries(id),
  FOREIGN KEY(account_code) REFERENCES chart_of_accounts(account_code)
);

CREATE INDEX IF NOT EXISTS idx_jel_account ON journal_entry_lines(account_code);
