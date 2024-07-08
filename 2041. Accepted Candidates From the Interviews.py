"""
533 ms runtime beats 0%
68.52 MB memory beats 0%
"""
import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    scores = rounds.groupby("interview_id")["score"].sum().reset_index(name="total_score")
    df = candidates.merge(scores, on="interview_id", how="left")
    # print(df)

    df = df[(df["years_of_exp"]>=2) & (df["total_score"]>15)][["candidate_id"]]
    return df