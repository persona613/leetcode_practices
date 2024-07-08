"""
586 ms runtime beats 0%
67.50 MB memory beats 0%
"""
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    target = company[company["name"]=="RED"]
    if len(target) == 0:
        return sales_person[["name"]]

    target_id = company[company["name"]=="RED"].iloc[0, 0]
    # print(target_id)

    relate = orders[orders["com_id"]==target_id]["sales_id"].unique()
    # print(relate)
    
    df = sales_person[~sales_person["sales_id"].isin(relate)][["name"]]
    return df