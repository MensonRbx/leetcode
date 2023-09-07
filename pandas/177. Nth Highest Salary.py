import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    uniqueSalaries = employee.salary.drop_duplicates().sort_values(ascending = False)

    if N > len(uniqueSalaries):
        return pd.DataFrame({"getNthHighestSalary("+str(N)+")": None}, index = [0])
    else:
        return pd.DataFrame({"getNthHighestSalary("+str(N)+")" :uniqueSalaries.values[N - 1]}, index = [0])

"""
So far lowest runtime of 419, don't know why everything else is so low, I even testing the fast code out on LeetCode and it was slower.
"""
