"""
567 ms runtime beats 0%
67.02 MB memory beats 0%
"""
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"]==views["viewer_id"]]
    df.drop_duplicates(subset="author_id", keep="first", inplace=True)
    df.rename(columns={"author_id": "id"}, inplace=True)
    return df[["id"]].sort_values(by="id", ascending=True)