"""
396 ms runtime beats 0%
66.76 MB memory beats 0%
"""
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(["actor_id", "director_id"]) \
        .size().reset_index(name="count")
    return df[df["count"]>=3][df.columns[:2]]