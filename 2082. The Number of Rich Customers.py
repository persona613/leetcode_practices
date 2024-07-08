"""
407 ms runtime beats 0%
66.14 MB memory beats 0%
"""
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store.loc[store["amount"]>500, ["customer_id"]]
    df.drop_duplicates(subset="customer_id", inplace=True)
    return pd.DataFrame({"rich_count": [df.shape[0]]})