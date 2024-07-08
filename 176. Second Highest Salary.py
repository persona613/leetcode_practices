"""
402 ms runtime beats 75.68%
66.05 MB memory beats 58.61%
"""
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    dis = employee["salary"].drop_duplicates()
    if len(dis) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    dis = dis.sort_values(ascending=False)
    ans = dis.iloc[1]
    return pd.DataFrame({"SecondHighestSalary": [ans]})