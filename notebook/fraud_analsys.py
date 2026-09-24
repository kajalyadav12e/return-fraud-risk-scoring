import pandas as pd

df = pd.read_csv(r"C:\Users\kajal\Downloads\archive (14)\e_commerce_shopper_behaviour_and_lifestyle.csv")

# Step 1: Relevant columns select karo
selected_columns = [
    "user_id", "return_rate", "return_frequency",
    "weekly_purchases", "monthly_spend", "average_order_value",
    "cart_abandonment_rate", "impulse_purchases_per_month", "browse_to_buy_ratio",
    "coupon_usage_frequency", "preferred_payment_method",
    "loyalty_program_member", "account_age_months",
    "checkout_abandonments_per_month", "purchase_conversion_rate"
]
df_clean = df[selected_columns]

# Step 2: Target variable banao -- top 25% ko risky maano
df_clean["is_risky_return"] = (df_clean["return_rate"] >= 75).astype(int)

# Step 3: Check karo target sahi bana ya nahi
print("Risky customers:", df_clean["is_risky_return"].sum())
print("Risky %:", df_clean["is_risky_return"].mean() * 100)

# Step 4: Save karo processed data -- agla step (model training) isi file se hoga
df_clean.to_csv(r"data/processed_data.csv", index=False)
print("\nSaved to data/processed_data.csv")