class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if len(nums) < 1000:
            #iterate check
            for num in nums:
                if nums.count(num) > 1:
                    return num
        else:
            #quick check
            sumCheck = sum(nums) - sum(list(set(nums)))
            if sumCheck > 0:
                return sumCheck
"""
Best Runtime: 489ms (>99%)
Best Memory: 36.35MB (>8%) (Should work on fixing this part)
"""
