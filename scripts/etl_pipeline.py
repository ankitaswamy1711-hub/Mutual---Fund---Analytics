from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

# Create processed folder if it doesn't exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# NAV files
NAV_FILES = [
    "HDFC_Top100_Direct.csv",
    "SBI_Bluechip.csv",
    "ICICI_Bluechip.csv",
    "Nippon_Large_Cap.csv",
    "Axis_Bluechip.csv",
    "Kotak_Bluechip.csv"
]


def process_nav_file(filename):
    input_path = RAW_DIR / filename

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path}"
        )

    print(f"Processing: {filename}")

    df = pd.read_csv(input_path)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Check required columns
    required_columns = {"date", "nav"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"{filename} is missing columns: {missing_columns}"
        )

    # Convert date
    df["date"] = pd.to_datetime(
        df["date"],
        dayfirst=True,
        errors="coerce"
    )

    # Convert NAV to numeric
    df["nav"] = pd.to_numeric(
        df["nav"],
        errors="coerce"
    )

    # Remove invalid rows
    df = df.dropna(subset=["date", "nav"])

    # Remove duplicate dates
    df = df.drop_duplicates(subset=["date"])

    # Sort by date
    df = df.sort_values("date")

    # Add scheme name
    df["scheme"] = Path(filename).stem

    # Arrange columns
    df = df[["scheme", "date", "nav"]]

    # Save processed file
    output_path = PROCESSED_DIR / filename

    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")
    print(f"Rows: {len(df)}\n")

    return df


def main():
    print("========== NAV ETL PIPELINE ==========\n")

    processed_data = []

    for filename in NAV_FILES:
        try:
            df = process_nav_file(filename)
            processed_data.append(df)

        except Exception as error:
            print(f"ERROR processing {filename}: {error}")

    # Combine all schemes
    if processed_data:
        combined = pd.concat(
            processed_data,
            ignore_index=True
        )

        combined_path = (
            PROCESSED_DIR / "all_nav_history.csv"
        )

        combined.to_csv(
            combined_path,
            index=False
        )

        print(f"Combined dataset saved: {combined_path}")
        print(f"Total rows: {len(combined)}")

    print("\nETL pipeline completed successfully!")


if __name__ == "__main__":
    main()