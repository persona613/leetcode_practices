"""
Wrong Answer
4 / 9 testcases passed

Editorial
Input
Employee =
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 200    |

Use Testcase
Output
| SecondhighestSalary |
| ------------------- |
| 200                 |
Expected
| SecondHighestSalary |
| ------------------- |
| 100                 |
"""
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    dis = employee["salary"].drop_duplicates()
    if len(dis) < 2:
        return pd.DataFrame({"SecondhighestSalary": [None]})
    ans = dis.sort_values(ascending=False)[1]
    return pd.DataFrame({"SecondhighestSalary": [ans]})