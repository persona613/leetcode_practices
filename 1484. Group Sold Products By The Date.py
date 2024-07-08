"""
512 ms runtime beats 0%
68.49 MB memory beats 0%
"""
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df1 = activities.groupby("sell_date")["product"].nunique().reset_index(name="num_sold")
    df2 = activities.groupby("sell_date")["product"].apply(
        lambda x: ",".join(sorted(x.unique()))
    ).reset_index(name="products")

    df = df1.merge(df2, on="sell_date", how="left")
    df.sort_values(by="sell_date", ascending=True, inplace=True)
    return df