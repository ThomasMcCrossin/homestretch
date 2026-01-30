PRAGMA foreign_keys = ON;

-- Extend wave_bills with provenance fields so we can ingest reconciled “final” Wave bills
-- from Fresher snapshots without losing traceability.

ALTER TABLE wave_bills ADD COLUMN vendor_category TEXT;
ALTER TABLE wave_bills ADD COLUMN source_system TEXT;
ALTER TABLE wave_bills ADD COLUMN source_record_id TEXT;

CREATE INDEX IF NOT EXISTS idx_wave_bills_source_record_id ON wave_bills(source_record_id);

