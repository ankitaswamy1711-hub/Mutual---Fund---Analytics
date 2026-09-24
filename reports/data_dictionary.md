# Bluestock Mutual Fund Analytics — Data Dictionary

## dim_fund

| Column | Type | Description |
|---|---|---|
| fund_id | INTEGER | Unique identifier for each fund |
| amfi_code | INTEGER | AMFI scheme code |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset management company |
| category | TEXT | Mutual fund category |

## dim_date

| Column | Type | Description |
|---|---|---|
| date_id | INTEGER | Unique date identifier |
| date | DATE | Calendar date |
| year | INTEGER | Year |
| month | INTEGER | Month number |
| quarter | INTEGER | Quarter number |
| day | INTEGER | Day of month |
| day_of_week | INTEGER | Day of week |

## fact_nav

| Column | Type | Description |
|---|---|---|
| nav_id | INTEGER | Unique NAV record |
| fund_id | INTEGER | Reference to dim_fund |
| date_id | INTEGER | Reference to dim_date |
| nav | REAL | Net Asset Value of the fund |

## fact_transactions

| Column | Type | Description |
|---|---|---|
| transaction_id | INTEGER | Unique transaction |
| fund_id | INTEGER | Reference to dim_fund |
| date_id | INTEGER | Reference to dim_date |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount | REAL | Transaction amount |
| state | TEXT | Investor state |
| kyc_status | TEXT | KYC verification status |

## fact_performance

| Column | Type | Description |
|---|---|---|
| performance_id | INTEGER | Unique performance record |
| fund_id | INTEGER | Reference to dim_fund |
| date_id | INTEGER | Reference to dim_date |
| return_value | REAL | Fund return |
| expense_ratio | REAL | Fund expense ratio |

## fact_aum

| Column | Type | Description |
|---|---|---|
| aum_id | INTEGER | Unique AUM record |
| fund_id | INTEGER | Reference to dim_fund |
| date_id | INTEGER | Reference to dim_date |
| aum | REAL | Assets Under Management |

## Source References

- NAV data: AMFI/MFAPI scheme data
- Fund identifiers: AMFI scheme codes
- Processed NAV data: `data/processed/nav_history_cleaned.csv`
- Database: `data/db/bluestock_mf.db`