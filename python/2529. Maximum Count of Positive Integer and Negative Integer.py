class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # nums = [num for num in nums if num != 0]
        return max(
            len([num for num in nums if num > 0]),
            len([num for num in nums if num < 0])
        )
