"""
Wrong Answer
11 / 18 testcases passed

Editorial
Input
Employee =
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 100    |
argument =
2

Use Testcase
Output
| getNthHighestSalary(2) |
| ---------------------- |
| 100                    |
Expected
| getNthHighestSalary(2) |
| ---------------------- |
| null                   |
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.sort_values(by="salary", ascending=False)
    num = df.iloc[N-1, 1] if N <= df.shape[0] else None
    return pd.DataFrame(data={f"getNthHighestSalary({N})": [num]})