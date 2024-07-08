"""
418 ms runtime beats 0%
66.37 MB memory beats 0%
"""
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]