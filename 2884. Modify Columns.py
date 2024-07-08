"""
375 ms runtime beats 0%
65.37 MB memory beats 0%
"""
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees