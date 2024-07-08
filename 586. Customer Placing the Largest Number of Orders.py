"""
452 ms runtime beats 0%
66.19 MB memory beats 0%
"""
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customer_number").size().reset_index(name="count")
    mx = df["count"].max()
    return df[df["count"]==mx][["customer_number"]]