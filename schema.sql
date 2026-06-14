-- schema.sql
-- Database schema for the Interactive Arithmetic Desktop Application (Abacus Trainer)
-- Run automatically by database.py on first launch, included here as a
-- standalone reference / for manual setup with the sqlite3 CLI.

CREATE TABLE IF NOT EXISTS sessions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    difficulty      TEXT    NOT NULL,
    total_questions INTEGER NOT NULL,
    correct_answers INTEGER NOT NULL,
    accuracy        REAL    NOT NULL,
    timestamp       TEXT    NOT NULL
);

-- Index to speed up retrieving recent session history
CREATE INDEX IF NOT EXISTS idx_sessions_timestamp ON sessions (timestamp);
