"""
529 ms runtime beats 0%
67.68 MB memory beats 0%
"""
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId").size().reset_index(name="count")

    df = df.merge(employee, left_on="managerId", right_on="id", how="right")
    # print(df)

    return df[df["count"]>=5][["name"]]