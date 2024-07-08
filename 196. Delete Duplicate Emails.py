"""
382 ms runtime beats 86.52%
66.22 MB memory beats 62.14%
"""
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", ascending=True, inplace=True)
    person.drop_duplicates(subset="email", inplace=True)