class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True)[k - 1]

"""
Best Runtime: 492ms (> 50%)
Best Memory: 29.45 (> 62%)
"""
