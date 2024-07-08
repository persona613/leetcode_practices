"""
563 ms runtime beats 65.77%
67.00 MB memory beats 89.37%
"""
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # max salary each department
    mxsal = employee.sort_values(by="salary", ascending=False)
    mxsal = mxsal.drop_duplicates(subset="departmentId", keep="first").iloc[:, 2:]

    # filter
    df = pd.DataFrame()
    for sal, dpid in mxsal.values:
        row = employee.loc[
            (employee["departmentId"]==dpid) & (employee["salary"]==sal),
            employee.columns[1:]
        ]
        df = pd.concat([df, row], axis=0, ignore_index=True)

    if not len(df):
        return pd.DataFrame(columns=["Department","Employee", "Salary"])
        
    # arrange columns position and name
    df = df.merge(department, left_on="departmentId", right_on="id", how="left")
    df = df[["name_y", "name_x", "salary"]]
    dic = {"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    return df.rename(columns=dic)