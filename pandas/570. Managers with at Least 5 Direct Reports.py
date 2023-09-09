import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame([],[],["name"])
    mainGroup = employee.groupby("managerId")

    for name, subGroup in mainGroup:
        managerId = subGroup.iloc[0, subGroup.columns.get_loc("managerId")]
        if subGroup.shape[0] >= 5:
            row = employee[employee.id == managerId]
            if row is not None and len(row["name"]) > 0:
                val = row["name"].values[0]
                result.loc[len(result)] = val

    return result

"""
Gotta get backto making this faster
"""
