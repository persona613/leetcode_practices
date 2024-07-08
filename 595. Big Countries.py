"""
484 ms runtime beats 0%
68.17 MB memory beats 0%
"""
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    columns = ["name", "population", "area"]
    return world[(world["area"]>=3000000) | (world["population"]>=25000000)][columns]
    