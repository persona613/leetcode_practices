"""
375 ms runtime beats 89.61%
66.01 MB memory beats 56.31%
"""
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(subset=["salary"])
    df = df.sort_values(by="salary", ascending=False)
    num = df.iloc[N-1, 1] if 0 < N <= df.shape[0] else None
    return pd.DataFrame(data={f"getNthHighestSalary({N})": [num]})