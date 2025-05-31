import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df

def preprocess_data(df):
    df = df.drop(columns=["timestamp", "customer_id", "merchant_id"])  # IDs et timestamps inutiles pour la détection
    df = pd.get_dummies(df, columns=["transaction_type", "country"], drop_first=True)
    return df

def split_data(df, test_size=0.2):
    X = df.drop("is_fraud", axis=1)
    y = df["is_fraud"]
    return train_test_split(X, y, test_size=test_size, random_state=42)
