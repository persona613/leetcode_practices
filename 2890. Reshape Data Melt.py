"""
548 ms runtime beats 0%
66.84 MB memory beats 0%
"""
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        report,
        id_vars=['product'],
        value_vars=report.columns[1:],
        var_name="quarter",
        value_name="sales"
    )