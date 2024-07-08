"""
396 ms runtime beats 0%
64.27 MB memory beats 0%
"""
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id", "age"])