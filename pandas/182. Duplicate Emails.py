import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person["email"].value_counts() 
    email_counts = email_counts[email_counts > 1]
    person["email"] = person["email"].drop_duplicates()
    
    del(person["id"])

    person = person[person["email"].isin(email_counts.index)]
    
    return person

"""
Best Runtime: 420ms (>85%)
Best Memory: 60MB (>85%)
"""
