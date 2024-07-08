"""
Wrong Answer
10 / 11 testcases passed

Editorial
Input
Employee =
| id  | name  | department | managerId |
| --- | ----- | ---------- | --------- |
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 100       |
| 103 | James | A          | 100       |
| 104 | Amy   | A          | 100       |
| 105 | Anne  | A          | 100       |
| 106 | Ron   | B          | 100       |

Use Testcase
Output
| name |
| ---- |
| null |
Expected
| name |
| ---- |
"""
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId").size().reset_index(name="count")

    df = df.merge(employee, left_on="managerId", right_on="id", how="left")

    return df[df["count"]>=5][["name"]]