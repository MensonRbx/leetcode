import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    result = pd.DataFrame([], [], ["SecondHighestSalary"])
    
    employee = employee["salary"].sort_values(ascending = False).unique() #ndarray
    result.loc[0] = employee[1] if len(employee) > 1 else None
 
    return result

"""
Beats 95.56% of programs in terms of memory.
Beats only 36.7% in terms of runtime.

Which is more important? Depends on what you're doing.

"""
