"""
546 ms runtime beats 0%
66.71 MB memory beats 0%
"""
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # have bonus
    is_valid = (employees["employee_id"]%2==1) & (~employees["name"].str.startswith("M"))
    employees["bonus"] = employees["salary"].where(is_valid, other=0)

    df = employees[["employee_id", "bonus"]]
    df.sort_values(by="employee_id", ascending=True, inplace=True)
    return df