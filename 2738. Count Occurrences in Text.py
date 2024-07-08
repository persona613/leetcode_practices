"""
345 ms runtime beats 96.01%
65.64 MB memory beats 48.36%
"""
import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    reg1 = r".* bull .*"
    df1 = files[files["content"].str.contains(reg1, regex=True)]

    reg2 = r".* bear .*"
    df2 = files[files["content"].str.contains(reg2, regex=True)]

    columns = ["word", "count"]
    data = [["bull", df1.shape[0]], ["bear", df2.shape[0]]]
    return pd.DataFrame(data, columns=columns)