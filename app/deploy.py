import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.score import score_customer

st.set_page_config(page_title="Return Risk Scoring", layout="centered")
st.title("🔍 Return Fraud & Risk Scoring System")
st.write("Enter a customer's order and return behavior to get their risk score.")

st.header("Customer Details")

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
    customer = {
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
    }

    risk_score = round(score_customer(customer) * 100, 1)
    st.subheader(f"Risk Score: {risk_score}%")
    if risk_score >= 50:
        st.error("⚠️ High Risk — Manual review recommended")
    else:
        st.success("✅ Low Risk — Normal customer")