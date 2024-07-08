"""
424 ms runtime beats 0%
65.84 MB memory beats 0%
"""
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=["name"], inplace=True)
    return students