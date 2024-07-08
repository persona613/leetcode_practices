"""
462 ms runtime beats 0%
66.59 MB memory beats 0%
"""
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len() > 15][["tweet_id"]]