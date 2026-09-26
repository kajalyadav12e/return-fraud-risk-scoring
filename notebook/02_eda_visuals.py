import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt
import seaborn as sns
from src.feature_engineering import load_data

df = load_data()

# Chart 1: Return rate distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["return_rate"], bins=30, color="steelblue")
plt.title("Return Rate Distribution")
plt.xlabel("Return Rate")
plt.savefig("reports_return_rate_distribution.png")
plt.close()

# Chart 2: Days to return, split by risk label
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="is_risky_return", y="avg_days_to_return")
plt.xticks([0, 1], ["Not Risky", "Risky"])
plt.title("Days to Return by Risk Label")
plt.savefig("reports_days_to_return_by_risk.png")
plt.close()

print("Charts saved: reports_return_rate_distribution.png, reports_days_to_return_by_risk.png")