class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowSums = [sum(row) for row in mat]
        
        result = []

        for i in range(k):
            currentMin = min(rowSums)
            minIndex = rowSums.index(currentMin)
            result.append(minIndex)

            #Hacky, set value to something which'll never be minimum 
            rowSums[minIndex] = 101     

        return result

"""
Best Runtime: 102ms (>80%)
Best Memory: 16.39MB (>99.87)
"""
