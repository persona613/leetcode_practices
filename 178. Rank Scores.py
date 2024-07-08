"""
382 ms runtime beats 86.12%
67.21 MB memory beats 50.78%
"""
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.sort_values(by="score", ascending=False)
    df["rank"] = df["score"].rank(method="dense", ascending=False)
    df.drop("id", axis=1, inplace=True)
    return df