"""
Runtime Error
1 / 14 testcases passed
KeyError: 'departmentId'
    raise KeyError(key)
Line 1778 in _get_label_or_level_values (/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py)
    left_keys.append(left._get_label_or_level_values(lk))
Line 1221 in _get_merge_keys (/usr/local/lib/python3.10/dist-packages/pandas/core/reshape/merge.py)
    ) = self._get_merge_keys()
Line 737 in __init__ (/usr/local/lib/python3.10/dist-packages/pandas/core/reshape/merge.py)
    op = _MergeOperation(
Line 148 in merge (/usr/local/lib/python3.10/dist-packages/pandas/core/reshape/merge.py)
    return merge(
Line 9843 in merge (/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py)
    df = df.merge(department, left_on="departmentId", right_on="id", how="left")
Line 18 in department_highest_salary (Solution.py)
    result_table = module.department_highest_salary(tables['Employee'], tables['Department'])
Line 41 in main (_driver.py)
    main()
Line 63 in <module> (_driver.py)
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

    # arrange columns position and name
    df = df.merge(department, left_on="departmentId", right_on="id", how="left")
    df = df[["name_y", "name_x", "salary"]]
    dic = {"name_y": "Department", "name_x": "Employee", "salary": "Salary"}
    return df.rename(columns=dic)