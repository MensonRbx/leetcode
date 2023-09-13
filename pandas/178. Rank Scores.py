import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    uniqueScoreList = list(set(scores["score"]))

    uniqueScoreList.sort(reverse=True)

    del(scores["id"])
    scores.sort_values(by="score", ascending=False, inplace=True)
    scores["rank"] = [uniqueScoreList.index(value) + 1 for value in scores["score"]]

    return scores

"""
Runtime: 438ms (>36%)  (gotta up this)
Memeory: 60.88mb (>95%)
"""
