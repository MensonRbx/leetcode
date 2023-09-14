import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world["population"] >= 25000000) | (world["area"] >= 3000000)].drop(columns = ["gdp", "continent"])

"""
Best Runtime: 415ms (>29%)
Best Memory: 61.18MB (>98.66%)
"""
