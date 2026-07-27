import pandas as pd

df = pd.read_csv(
    "data/raw/NAVAll.txt",
    sep=";",
    engine="python"
)

fund_houses = []
categories = []

for value in df["Scheme Code"]:

    if pd.isna(value):
        continue

    value = str(value)

    # Scheme code is numeric
    if value.isdigit():
        continue

    # Mutual fund names
    if "Mutual Fund" in value:
        fund_houses.append(value)

    # Scheme category headings
    elif "Schemes" in value:
        categories.append(value)

print("\n========== UNIQUE FUND HOUSES ==========\n")
print(sorted(set(fund_houses)))

print("\n========== UNIQUE CATEGORIES ==========\n")
print(sorted(set(categories)))

print("\nTotal Fund Houses :", len(set(fund_houses)))
print("Total Categories :", len(set(categories)))