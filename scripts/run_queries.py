import sqlite3
from pathlib import Path

BASE_DIR = Path(r"E:\Mutual Fund Blue")

DB_FILE = BASE_DIR / "data" / "db" / "bluestock_mf.db"
QUERIES_FILE = BASE_DIR / "sql" / "queries.sql"

conn = sqlite3.connect(DB_FILE)

with open(QUERIES_FILE, "r", encoding="utf-8") as f:
    sql = f.read()

queries = [q.strip() for q in sql.split(";") if q.strip()]

for i, query in enumerate(queries, start=1):
    print(f"\n===== QUERY {i} =====")
    print(query)

    try:
        result = conn.execute(query).fetchall()

        if result:
            for row in result[:10]:
                print(row)
        else:
            print("No data available.")

    except Exception as e:
        print("Query error:", e)

conn.close()