"""
439 ms runtime beats 0%
66.96 MB memory beats 0%
"""
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni, left_on="id", right_on="id", how="left")
    return df[["unique_id", "name"]]