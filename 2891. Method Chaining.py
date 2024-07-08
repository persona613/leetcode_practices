"""
516 ms runtime beats 0%
66.64 MB memory beats 0%
"""
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"]>100].sort_values(["weight"], ascending=False)[["name"]]