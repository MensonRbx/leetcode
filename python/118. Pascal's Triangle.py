class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [[1]]
        for i in range(1, numRows):
            baseArray = [1, 1]
            lastArray = result[i-1]

            numOfTermsToCompute = i - 2
            for j in range(len(lastArray) - 1):
                print("Current Row:",i)
                print("Current Number Being Calculated:",j)
                num1 = lastArray[j]
                num2 = lastArray[j + 1]
                baseArray.insert(-1, num1 + num2)

            result.append(baseArray)

        return result

"""
Runtime: ~= 38ms (>86%) (don't really know how trustworthy this is but oh well)
Memory: 16.57 (>5%)
"""
