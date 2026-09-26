import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

from src.feature_engineering import load_data, encode_categoricals, get_features_and_target

# Step 1: Load and prepare data
df = load_data()
df = encode_categoricals(df)
X, y = get_features_and_target(df)

# Step 2: Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 3: Train model
model = RandomForestClassifier(
    n_estimators=100, max_depth=8, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)

# Step 4: Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop Features:")
print(importances.head(8))

# Step 5: Save model
joblib.dump(model, "models/risk_model.pkl")
print("\nModel saved to models/risk_model.pkl")