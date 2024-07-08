"""
Runtime Error
20 / 21 testcases passed
IndexError: index 0 is out of bounds for axis 0 with size 0
    newmask = self._mask[item]
Line 160 in __getitem__ (/usr/local/lib/python3.10/dist-packages/pandas/core/arrays/masked.py)
    return series._values[index]
Line 3868 in _get_value (/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py)
    return self.obj._get_value(*key, takeable=self._takeable)
Line 1096 in __getitem__ (/usr/local/lib/python3.10/dist-packages/pandas/core/indexing.py)
    target_id = company[company["name"]=="RED"].iloc[0, 0]
Line 4 in sales_person (Solution.py)
    result_table = module.sales_person(tables['SalesPerson'], tables['Company'], tables['Orders'])
Line 43 in main (_driver.py)
    main()
Line 65 in <module> (_driver.py)
"""
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    target_id = company[company["name"]=="RED"].iloc[0, 0]
    # print(target_id)
    
    relate = orders[orders["com_id"]==target_id]["sales_id"].unique()
    # print(relate)
    
    df = sales_person[~sales_person["sales_id"].isin(relate)][["name"]]
    return df