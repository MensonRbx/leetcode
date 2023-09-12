class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        newList = []
        for subList in matrix:
            newList += list(set(subList))

        return target in newList

"""
Runtime: 44ms (>90%)
Memory: 16.75MS (>86%)
"""
