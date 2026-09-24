import sqlite3
from pathlib import Path

BASE_DIR = Path(r"E:\Mutual Fund Blue")

DB_FILE = BASE_DIR / "data" / "db" / "bluestock_mf.db"
SCHEMA_FILE = BASE_DIR / "sql" / "schema.sql"

conn = sqlite3.connect(DB_FILE)

with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
    schema = f.read()

conn.executescript(schema)
conn.commit()

print("Schema applied successfully.")

tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
).fetchall()

print("\nTables:")
for table in tables:
    print(table[0])

conn.close()