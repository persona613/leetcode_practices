"""
357 ms runtime beats 0%
66.20 MB memory beats 0%
"""
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby("class")["student"].count().reset_index()
    return df[df["student"]>=5][["class"]]