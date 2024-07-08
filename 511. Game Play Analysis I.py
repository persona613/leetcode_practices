"""
448 ms runtime beats 0%
67.80 MB memory beats 0%
"""
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby("player_id")["event_date"].min().reset_index()
    df.rename({"event_date": "first_login"}, axis=1, inplace=True)
    return df