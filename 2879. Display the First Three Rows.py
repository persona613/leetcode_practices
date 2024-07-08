"""
482 ms runtime beats 0%
65.01 MB memory beats 0%
"""
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)