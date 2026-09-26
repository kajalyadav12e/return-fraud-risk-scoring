# Return Fraud & Risk Scoring System

A machine learning system that scores e-commerce customers on how likely their
return behavior is high-risk (e.g. "wardrobing" — ordering, using, and
returning items) — so a trust & safety team can focus manual review on the
customers most worth reviewing, instead of every return.

**Live demo:** https://kajal-return-risk.streamlit.app

## Problem

Return policies check whether a single transaction is valid (unused, tags on,
within X days). They can't catch a customer who follows every rule on every
individual return but does this repeatedly as a pattern. This project solves
a different problem: does this customer's behavior *over time* look like
known risky patterns?

## Approach

- **Data**: 3,000 synthetic customer records. Real return-fraud labels aren't
  public, so this project generates data using explicit behavioral logic —
  each customer has a hidden "persona" (genuine / normal / habitual returner)
  driving correlated, realistic behavior across orders, return speed, and
  complaints. See `data/generate_data.py`.
- **Label**: `is_risky_return` = top 25% of customers by `return_rate` — a
  business decision (how much manual-review capacity a team realistically
  has), not a statistical one.
- **Leakage prevention**: The label is derived only from `return_rate`,
  which is excluded from the model's features.
- **Model**: Random Forest (`class_weight="balanced"`), evaluated on
  precision/recall/F1 since the risky class is a minority (~25%).

## Results

| Metric (risky class) | Score |
|---|---|
| Precision | 0.84 |
| Recall | 0.87 |
| F1-score | 0.86 |
| Overall accuracy | 0.93 |

**Top features:** `total_returns`, `avg_days_to_return`, `total_orders`,
`high_value_return_ratio`. Return *speed*, not just return count, is a
strong signal — consistent with how wardrobing behaves in practice.

## Project Structure