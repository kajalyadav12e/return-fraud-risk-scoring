import pandas as pd
import joblib

def score_customer(customer: dict) -> float:
    """
    Takes a single customer's details and returns a risk probability (0 to 1).

    Example input:
    {
        "account_age_days": 300, "total_orders": 10, "total_returns": 2,
        "avg_days_to_return": 5.0, "avg_order_value": 1500.0,
        "high_value_return_ratio": 0.2, "complaints_filed": 0,
        "refund_to_wallet_pref": 0, "payment_method": "UPI",
        "preferred_category": "Books"
    }
    """
    model = joblib.load("models/risk_model.pkl")

    # Convert the single customer dict into a one-row DataFrame
    input_df = pd.DataFrame([customer])

    # Encode categorical columns the same way they were encoded at training time
    input_encoded = pd.get_dummies(input_df, columns=["payment_method", "preferred_category"])

    # Align columns with what the model expects (fill any missing dummy columns with 0)
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_columns]

    risk_probability = model.predict_proba(input_encoded)[0][1]
    return risk_probability