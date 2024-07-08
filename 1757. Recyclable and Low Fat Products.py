"""
407 ms runtime beats 0%
66.32 MB memory beats 0%
"""
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"]=="Y") & (products["recyclable"]=="Y")][["product_id"]]