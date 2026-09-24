import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(r"E:\Mutual Fund Blue")

DB_FILE = BASE_DIR / "data" / "db" / "bluestock_mf.db"
NAV_FILE = BASE_DIR / "data" / "processed" / "nav_history_cleaned.csv"

df = pd.read_csv(NAV_FILE)

df["date"] = pd.to_datetime(df["date"])

conn = sqlite3.connect(DB_FILE)

# Create funds
funds = df[["scheme_name"]].drop_duplicates().reset_index(drop=True)
funds["fund_id"] = range(1, len(funds) + 1)

for _, row in funds.iterrows():
    conn.execute(
        """
        INSERT OR IGNORE INTO dim_fund (fund_id, scheme_name)
        VALUES (?, ?)
        """,
        (int(row["fund_id"]), row["scheme_name"])
    )

# Create dates
dates = df[["date"]].drop_duplicates().sort_values("date")

for _, row in dates.iterrows():
    d = row["date"]
    date_id = int(d.strftime("%Y%m%d"))

    conn.execute(
        """
        INSERT OR IGNORE INTO dim_date
        (date_id, date, year, month, quarter, day, day_of_week)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            date_id,
            d.strftime("%Y-%m-%d"),
            d.year,
            d.month,
            d.quarter,
            d.day,
            d.dayofweek
        )
    )

# Load NAV facts
for _, row in df.iterrows():
    fund_id = int(
        funds.loc[
            funds["scheme_name"] == row["scheme_name"],
            "fund_id"
        ].iloc[0]
    )

    date_id = int(row["date"].strftime("%Y%m%d"))

    conn.execute(
        """
        INSERT OR IGNORE INTO fact_nav
        (fund_id, date_id, nav)
        VALUES (?, ?, ?)
        """,
        (fund_id, date_id, float(row["nav"]))
    )

conn.commit()

print("NAV data loaded successfully.")

print("\nRow counts:")

for table in ["dim_fund", "dim_date", "fact_nav"]:
    count = conn.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table}: {count}")

conn.close()