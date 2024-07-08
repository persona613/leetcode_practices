"""
383 ms runtime beats 0%
67.19 MB memory beats 0%
"""
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on="id", right_on="customerId", how="left")
    df = df[df["customerId"].isnull()]
    return df[["name"]].rename(columns={"name": "Customers"})