import pandas as pd
from pathlib import Path

BASE_DIR = Path(r"E:\Mutual Fund Blue")

INPUT_FILE = BASE_DIR / "data" / "raw" / "nav_history.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "nav_history_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

print("Original rows:", len(df))
print("Columns:", list(df.columns))

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Convert data types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Remove invalid dates and NAV values
df = df.dropna(subset=["date"])
df = df.dropna(subset=["nav"])

# NAV must be greater than 0
df = df[df["nav"] > 0]

# Remove duplicates
df = df.drop_duplicates()

# Sort by scheme and date
df = df.sort_values(["scheme_name", "date"])

# Forward-fill NAV within each scheme
df["nav"] = df.groupby("scheme_name")["nav"].ffill()

# Reset index
df = df.reset_index(drop=True)

# Create output folder
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print("\n===== NAV CLEANING COMPLETE =====")
print("Cleaned rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("Missing dates:", df["date"].isna().sum())
print("Missing NAV:", df["nav"].isna().sum())
print("NAV <= 0:", (df["nav"] <= 0).sum())

print("\nDate range:")
print(df["date"].min(), "to", df["date"].max())

print("\nOutput:")
print(OUTPUT_FILE)
