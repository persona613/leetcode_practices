"""
Wrong Answer
12 / 14 testcases passed

Editorial
Input
Students =
| student_id | student_name |
| ---------- | ------------ |
| 1          | Alice        |
Subjects =
| subject_name |
| ------------ |
Examinations =
| student_id | subject_name |
| ---------- | ------------ |

Use Testcase
Output
| student_name | student_id | subject_name | attended_exams |
| ------------ | ---------- | ------------ | -------------- |
Expected
| student_id | student_name | subject_name | attended_exams |
| ---------- | ------------ | ------------ | -------------- |
"""
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df1 = students.merge(subjects, how="cross")
    df2 = examinations.groupby(["student_id", "subject_name"]).size().reset_index(name="attended_exams")

    df = df1.merge(df2, on=["student_id", "subject_name"], how="left")
    df = df.sort_values(by=["student_id", "subject_name"])
    return df.fillna(value={"attended_exams": 0})