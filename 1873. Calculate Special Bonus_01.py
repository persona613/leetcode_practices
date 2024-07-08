"""
Wrong Answer
22 / 23 testcases passed

Editorial
Input
Employees =
| employee_id | name    | salary |
| ----------- | ------- | ------ |
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 9           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 7           | Kannon  | 7700   |

Use Testcase
Output
| employee_id | bonus |
| ----------- | ----- |
| 2           | 0     |
| 3           | 0     |
| 9           | 7400  |
| 8           | 0     |
| 7           | 7700  |

Expected
| employee_id | bonus |
| ----------- | ----- |
| 2           | 0     |
| 3           | 0     |
| 7           | 7700  |
| 8           | 0     |
| 9           | 7400  |
"""
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # have bonus
    is_valid = (employees["employee_id"]%2==1) & (~employees["name"].str.startswith("M"))
    employees["bonus"] = employees["salary"].where(is_valid, other=0)

    return employees[["employee_id", "bonus"]]
