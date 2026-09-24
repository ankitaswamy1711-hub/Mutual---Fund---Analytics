import pandas as pd
from pathlib import Path

BASE_DIR = Path(r"E:\Mutual Fund Blue")

RAW_DIR = BASE_DIR / "data" / "raw"
OUTPUT_FILE = RAW_DIR / "nav_history.csv"

files = [
    "Axis_Bluechip.csv",
    "HDFC_Top100_Direct.csv",
    "ICICI_Bluechip.csv",
    "Kotak_Bluechip.csv",
    "Nippon_Large_Cap.csv",
    "SBI_Bluechip.csv"
]

frames = []

for file in files:
    path = RAW_DIR / file

    df = pd.read_csv(path)

    # Add scheme name from filename
    df["scheme_name"] = path.stem

    frames.append(df)

combined = pd.concat(frames, ignore_index=True)

combined.to_csv(OUTPUT_FILE, index=False)

print("===== NAV HISTORY CREATED =====")
print("Files combined:", len(files))
print("Total rows:", len(combined))
print("Columns:", list(combined.columns))
print("Saved to:", OUTPUT_FILE)