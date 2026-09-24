import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Step 1: Data load karo
df = pd.read_csv(r"data/return_data.csv")

# Step 2: Categorical columns ko numbers mein convert karo
df = pd.get_dummies(df, columns=["payment_method", "preferred_category"], drop_first=True)

# Step 3: Features aur Target alag karo
X = df.drop(columns=["customer_id", "return_rate", "is_risky_return"])
y = df["is_risky_return"]

# Step 4: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 5: Model train karo
model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42, class_weight="balanced")
model.fit(X_train, y_train)

# Step 6: Test karo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 7: Save karo
joblib.dump(model, "models/risk_model.pkl")
print("\nModel saved to models/risk_model.pkl")
# Step 8: Feature importance dekho -- konsa feature sabse zyada matter karta hai
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop Features:")
print(importances.head(8))