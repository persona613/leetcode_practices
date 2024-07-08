"""
664 ms runtime beats 0%
67.81 MB memory beats 0%
"""
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    df = pd.pivot_table(
        employees, 
        index="event_day", 
        columns="emp_id", 
        values="total_time", 
        aggfunc="sum"
    ).reset_index()
    # print(df)

    df = df.melt(
        id_vars=["event_day"],
        value_vars=df.columns[1:],
        var_name="emp_id",
        value_name="total_time"
    )
    # print(df)

    df.dropna(
        subset=["total_time"], 
        axis=0, 
        inplace=True, 
        ignore_index=True
    )

    df.rename(columns={"event_day": "day"}, inplace=True)
    return df