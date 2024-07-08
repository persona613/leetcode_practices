"""
353 ms runtime beats 0%
66.68 MB memory beats 0%
"""
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby("teacher_id")["subject_id"].nunique().reset_index()
    df.rename(columns={"subject_id": "cnt"}, inplace=True)
    return df