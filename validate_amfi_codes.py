import pandas as pd

# Read fund master
fund_master = pd.read_csv(
    "data/raw/NAVAll.txt",
    sep=";",
    engine="python"
)

# Keep only rows where Scheme Code is numeric
fund_master = fund_master[
    fund_master["Scheme Code"].astype(str).str.isdigit()
]

# AMFI codes from fund master
master_codes = set(fund_master["Scheme Code"].astype(str))

# Codes for which NAV history was downloaded
nav_codes = {
    "125497",
    "119551",
    "120503",
    "118632",
    "119092",
    "120841"
}

print("===== VALIDATION =====\n")

for code in nav_codes:
    if code in master_codes:
        print(f"{code} : Present")
    else:
        print(f"{code} : Missing")

print("\nSummary")

print(f"Fund Master Codes : {len(master_codes)}")
print(f"NAV History Files : {len(nav_codes)}")

missing = nav_codes - master_codes

print(f"Missing Codes : {len(missing)}")