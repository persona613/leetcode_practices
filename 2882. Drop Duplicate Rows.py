"""
427 ms runtime beats 0%
66.11 MB memory beats 0%
"""
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"], keep="first")