"""
408 ms runtime beats 0%
65.72 MB memory beats 0%
"""
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students