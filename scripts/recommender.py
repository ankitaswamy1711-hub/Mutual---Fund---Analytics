import pandas as pd

metrics = pd.read_csv("data/processed/advanced_metrics.csv")

metrics["risk_grade"] = pd.qcut(
    metrics["max_drawdown"].rank(method="first"),
    3,
    labels=["Low", "Medium", "High"]
)

def recommend(risk_appetite):
    return metrics[
        metrics["risk_grade"] == risk_appetite
    ].nlargest(3, "sharpe")[["scheme_name", "sharpe", "risk_grade"]]

if __name__ == "__main__":
    print(recommend("Low"))
