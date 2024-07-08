"""
Wrong Answer
14 / 18 testcases passed

Editorial
Input
Employee =
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
argument =
-1

Use Testcase
Output
| getNthHighestSalary(-1) |
| ----------------------- |
| 200                     |
Expected
| getNthHighestSalary(-1) |
| ----------------------- |
| null                    |
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(subset=["salary"])
    df = df.sort_values(by="salary", ascending=False)
    num = df.iloc[N-1, 1] if N <= df.shape[0] else None
    return pd.DataFrame(data={f"getNthHighestSalary({N})": [num]})