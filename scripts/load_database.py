from pathlib import Path
import sqlite3
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_DIR = BASE_DIR / "data" / "db"

DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "bluestock_mf.db"


def main():

    # Load processed NAV data
    csv_path = PROCESSED_DIR / "all_nav_history.csv"

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Processed CSV not found: {csv_path}"
        )

    df = pd.read_csv(csv_path)

    # Connect to SQLite
    connection = sqlite3.connect(DB_PATH)

    # Load schema
    schema_path = BASE_DIR / "sql" / "schema.sql"

    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    connection.executescript(schema)

    # Load data into SQLite
    df.to_sql(
        "nav_history",
        connection,
        if_exists="replace",
        index=False
    )

    # Check number of rows
    count = connection.execute(
        "SELECT COUNT(*) FROM nav_history"
    ).fetchone()[0]

    connection.close()

    print("========== DATABASE LOAD ==========")
    print(f"Database created: {DB_PATH}")
    print(f"Rows loaded: {count}")
    print("SQLite database created successfully!")


if __name__ == "__main__":
    main()