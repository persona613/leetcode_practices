"""
438 ms runtime beats 0%
89.80 MB memory beats 0%
"""
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # is_valid serial => bool
    l = (accounts["income"] < 20000).sum()
    h = (accounts["income"] > 50000).sum()
    m = len(accounts) - l - h

    data = [["Low Salary", l], ["Average Salary", m], ["High Salary", h]]
    columns = ["category", "accounts_count"]
    return pd.DataFrame(data, columns=columns)