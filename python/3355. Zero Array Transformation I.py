class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        count = 0
        diff = list()
        for i in range(len(nums) + 1):
            diff.append(0)
        for query in queries:
            diff[query[0]] -= 1
            diff[query[1] + 1] += 1
        curr_deincr = 0
        for i, num in enumerate(nums):
            curr_deincr += diff[i]
            if num + curr_deincr > 0:
                return False

        return True
