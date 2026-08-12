CREATE TABLE IF NOT EXISTS nav_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme TEXT NOT NULL,
    date DATE NOT NULL,
    nav REAL NOT NULL,
    UNIQUE(scheme, date)
);

CREATE INDEX IF NOT EXISTS idx_nav_scheme
ON nav_history(scheme);

CREATE INDEX IF NOT EXISTS idx_nav_date
ON nav_history(date);