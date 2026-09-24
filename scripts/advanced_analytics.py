import pandas as pd
import numpy as np

df = pd.read_csv("data/processed/nav_history_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["scheme_name", "date"])

df["daily_return"] = df.groupby("scheme_name")["nav"].pct_change()

rf = 0.065
results = []

for scheme, g in df.groupby("scheme_name"):
    r = g["daily_return"].dropna()
    nav = g["nav"].dropna()

    sharpe = ((r.mean() * 252) - rf) / (r.std() * np.sqrt(252)) if r.std() != 0 else np.nan
    var95 = r.quantile(0.05)
    cvar95 = r[r <= var95].mean()
    max_dd = (nav / nav.cummax() - 1).min()

    results.append([scheme, sharpe, var95, cvar95, max_dd])

out = pd.DataFrame(results, columns=["scheme_name", "sharpe", "VaR_95", "CVaR_95", "max_drawdown"])
out.to_csv("data/processed/advanced_metrics.csv", index=False)

print(f"Advanced metrics generated for {len(out)} schemes")
