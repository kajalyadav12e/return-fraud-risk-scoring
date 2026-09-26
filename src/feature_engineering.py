import pandas as pd


def load_data(path="data/return_data.csv") -> pd.DataFrame:
    """Load the raw customer dataset."""
    return pd.read_csv(path)


def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode the categorical columns."""
    return pd.get_dummies(df, columns=["payment_method", "preferred_category"], drop_first=True)


def get_features_and_target(df: pd.DataFrame):
    """
    Split the encoded dataframe into features (X) and target (y).

    Drops customer_id (identifier), return_rate (the column the label
    was derived from -- kept out to avoid data leakage), and the
    target column itself.
    """
    X = df.drop(columns=["customer_id", "return_rate", "is_risky_return"])
    y = df["is_risky_return"]
    return X, y