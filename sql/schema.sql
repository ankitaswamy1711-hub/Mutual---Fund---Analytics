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
ON nav_history(date);-- Bluestock Mutual Fund Analytics
-- D2 Star Schema

CREATE TABLE IF NOT EXISTS dim_fund (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT NOT NULL,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    year INTEGER,
    month INTEGER,
    quarter INTEGER,
    day INTEGER,
    day_of_week INTEGER
);

CREATE TABLE IF NOT EXISTS fact_nav (
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    UNIQUE(fund_id, date_id)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    transaction_type TEXT,
    amount REAL,
    state TEXT,
    kyc_status TEXT,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    return_value REAL,
    expense_ratio REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    aum REAL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE INDEX IF NOT EXISTS idx_fact_nav_fund
ON fact_nav(fund_id);

CREATE INDEX IF NOT EXISTS idx_fact_nav_date
ON fact_nav(date_id);

CREATE INDEX IF NOT EXISTS idx_fact_transactions_fund
ON fact_transactions(fund_id);

CREATE INDEX IF NOT EXISTS idx_fact_performance_fund
ON fact_performance(fund_id);

CREATE INDEX IF NOT EXISTS idx_fact_aum_fund
ON fact_aum(fund_id);