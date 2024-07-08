"""
629 ms runtime beats 0%
67.65 MB memory beats 0%
"""
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(
        index = "month",
        columns = "city",
        values = "temperature",
        aggfunc = "max"
    )