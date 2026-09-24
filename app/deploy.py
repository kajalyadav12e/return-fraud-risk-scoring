import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Return Risk Scoring", layout="centered")

# Model load karo
model = joblib.load("models/risk_model.pkl")

st.title("🔍 Return Fraud & Risk Scoring System")
st.write("Customer ka behavior daalo, risk score turant dekho.")

st.header("Customer Details Daalo")

total_orders = st.number_input("Total Orders", min_value=1, value=10)
total_returns = st.number_input("Total Returns", min_value=0, value=2)
avg_days_to_return = st.number_input("Average Days to Return", min_value=0.5, value=5.0)
avg_order_value = st.number_input("Average Order Value (₹)", min_value=0.0, value=1500.0)
high_value_return_ratio = st.slider("High Value Return Ratio", 0.0, 1.0, 0.2)
account_age_days = st.number_input("Account Age (days)", min_value=1, value=300)
complaints_filed = st.number_input("Complaints Filed", min_value=0, value=0)
refund_to_wallet_pref = st.selectbox("Refund to Wallet Preferred?", [0, 1])
payment_method = st.selectbox("Payment Method", ["COD", "Credit Card", "Debit Card", "UPI", "Wallet"])
preferred_category = st.selectbox("Preferred Category", ["Fashion", "Electronics", "Home & Kitchen", "Beauty", "Footwear", "Mobiles", "Books"])

if st.button("Check Risk Score"):
    # Input ko model ke format mein convert karo
    input_data = pd.DataFrame([{
        "account_age_days": account_age_days,
        "total_orders": total_orders,
        "total_returns": total_returns,
        "avg_days_to_return": avg_days_to_return,
        "avg_order_value": avg_order_value,
        "high_value_return_ratio": high_value_return_ratio,
        "complaints_filed": complaints_filed,
        "refund_to_wallet_pref": refund_to_wallet_pref,
        "payment_method": payment_method,
        "preferred_category": preferred_category
    }])

    # Same encoding jo training mein ki thi
    input_encoded = pd.get_dummies(input_data, columns=["payment_method", "preferred_category"])

    # Model ke expected columns se match karo (missing columns 0 se fill karo)
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_columns]

    # Prediction
    risk_prob = model.predict_proba(input_encoded)[0][1]
    risk_score = round(risk_prob * 100, 1)

    st.subheader(f"Risk Score: {risk_score}%")
    if risk_score >= 50:
        st.error("⚠️ High Risk — Manual review recommended")
    else:
        st.success("✅ Low Risk — Normal customer")