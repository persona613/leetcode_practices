"""
1425 ms runtime beats 0%
66.56 MB memory beats 0%
"""
import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ids = ads["ad_id"].unique()
    data = []
    for i in ids:
        df = ads[ads["ad_id"] == i]
        # calculate click + view
        ignore = (df["action"] == "Ignored").sum()
        cv = len(df) - ignore
        # calculate click
        ck = (df["action"] == "Clicked").sum()

        # calculate ctr
        if cv == 0:
            ctr = 0
        else:
            ctr = round(ck / cv * 100, 2)
        data.append([i, ctr])
    
    df = pd.DataFrame(data, columns = ["ad_id", "ctr"])
    df = df.sort_values(by = ["ctr", "ad_id"], ascending = [False, True])
    return df