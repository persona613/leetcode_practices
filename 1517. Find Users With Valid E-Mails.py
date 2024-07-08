"""
432 ms runtime beats 0%
66.66 MB memory beats 0%
"""
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    reg = r"^[A-Za-z]+[A-Za-z0-9_.-]*@leetcode\.com$"
    return users[users["mail"].str.match(reg)]