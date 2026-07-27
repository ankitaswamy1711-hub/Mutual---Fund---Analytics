import requests
import pandas as pd

schemes = {
    "HDFC_Top100_Direct": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for scheme_name, scheme_id in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_id}"

    print(f"Fetching {scheme_name}...")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{scheme_name}.csv"
        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:
        print(f"Failed to fetch {scheme_name}")

print("\nAll NAV data downloaded successfully!")