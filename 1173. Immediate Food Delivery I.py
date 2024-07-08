"""
408 ms runtime beats 0%
67.12 MB memory beats 0%
"""
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immd = delivery[
        delivery["order_date"] == delivery["customer_pref_delivery_date"]
    ]
    ans = round(immd.shape[0] / delivery.shape[0] * 100, 2)

    return pd.DataFrame({"immediate_percentage" : [ans]})