import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PERFORMANCE_FILE = BASE_DIR / "data" / "raw" / "07_scheme_performance.csv"

RISK_MAP = {
    "low": ["Low"],
    "moderate": ["Moderate", "Moderately High"],
    "high": ["High", "Very High"]
}

def recommend_funds(risk_appetite: str = "Moderate", top_n: int = 3) -> pd.DataFrame:
    """Return top funds by Sharpe ratio for selected risk appetite."""
    df = pd.read_csv(PERFORMANCE_FILE)
    risk_key = str(risk_appetite).strip().lower()
    allowed_risks = RISK_MAP.get(risk_key, [risk_appetite])
    filtered = df[df["risk_grade"].isin(allowed_risks)].copy()
    if filtered.empty:
        raise ValueError(f"No funds found for risk appetite: {risk_appetite}")
    filtered["sharpe_ratio"] = pd.to_numeric(filtered["sharpe_ratio"], errors="coerce")
    cols = ["amfi_code", "scheme_name", "fund_house", "category", "risk_grade", "return_3yr_pct", "sharpe_ratio", "expense_ratio_pct", "aum_crore"]
    return filtered.sort_values("sharpe_ratio", ascending=False)[cols].head(top_n)

if __name__ == "__main__":
    appetite = input("Enter risk appetite (Low / Moderate / High): ").strip() or "Moderate"
    result = recommend_funds(appetite)
    print("\nTop Recommended Funds:\n")
    print(result.to_string(index=False))
