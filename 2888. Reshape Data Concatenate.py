"""
446 ms runtime beats 0%
66.36 MB memory beats 0%
"""
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    concatenate = pd.concat([df1, df2])
    return concatenate