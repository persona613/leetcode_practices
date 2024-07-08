"""
438 ms runtime beats 0%
65.52 MB memory beats 0%
"""
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products