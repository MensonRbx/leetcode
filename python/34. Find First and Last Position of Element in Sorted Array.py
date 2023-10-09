class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not target in nums:
            return [-1, -1]

        return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]


"""
Best Runtime: 78ms (>88%)
Best Memory: 17.5MB (>99%)
"""
