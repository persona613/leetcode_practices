"""
454 ms runtime beats 0%
65.45 MB memory beats 0%
"""
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees