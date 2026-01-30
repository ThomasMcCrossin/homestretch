PRAGMA foreign_keys = ON;

-- Explicit override/flag layer. This is where we record “data decisions” (e.g. duplicates)
-- without mutating raw evidence rows imported from the frozen snapshot.

CREATE TABLE IF NOT EXISTS document_flags (
  id INTEGER PRIMARY KEY,
  document_id INTEGER NOT NULL,
  flag TEXT NOT NULL, -- IGNORE | DUPLICATE | NEEDS_REVIEW | ...
  notes TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE(document_id, flag),
  FOREIGN KEY(document_id) REFERENCES documents(id)
);

CREATE INDEX IF NOT EXISTS idx_document_flags_flag ON document_flags(flag);

