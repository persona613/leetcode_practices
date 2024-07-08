"""
443 ms runtime beats 71.52%
65.64 MB memory beats 30.70%
"""
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    dic = {
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years"
    }
    return students.rename(columns=dic)