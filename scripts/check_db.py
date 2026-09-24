import sqlite3

conn = sqlite3.connect(r"data\db\bluestock_mf.db")

print("===== DATABASE ROW COUNTS =====")

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:
    count = conn.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table}: {count}")

conn.close()