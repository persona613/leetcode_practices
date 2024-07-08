"""
573 ms runtime beats 0%
67.45 MB memory beats 0%
"""
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    groups = daily_sales.groupby(["date_id", "make_name"])
    df = groups.agg(
        unique_leads = ("lead_id", lambda x: len(set(x))),
        unique_partners = ("partner_id", "nunique")
    ).reset_index(drop=False)
    return df