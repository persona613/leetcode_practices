"""
522 ms runtime beats 0%
67.48 MB memory beats 0%
"""
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    if len(subjects) == 0 or len(examinations) == 0:
        return pd.DataFrame(columns=["student_id", "student_name", "subject_name", "attended_exams"])

    df1 = students.merge(subjects, how="cross")
    # print(df1)
    df2 = examinations.groupby(["student_id", "subject_name"]).size().reset_index(name="attended_exams")
    # print(df2)
    
    df = df1.merge(df2, on=["student_id", "subject_name"], how="left")
    df = df.sort_values(by=["student_id", "subject_name"])
    return df.fillna(value={"attended_exams": 0})