"""
433 ms runtime beats 89.78%
67.30 MB memory beats 5.03%
"""
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = products.melt(
        id_vars=["product_id"],
        value_vars = ["store1", "store2", "store3"],
        var_name = "store",
        value_name = "price"
    )
    return df[~df["price"].isna()]