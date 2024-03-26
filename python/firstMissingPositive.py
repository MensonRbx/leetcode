class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort(reverse = False)
        count = 1
        nums = set(nums)
        while True:
            if count in nums:
                count += 1
            else:
                return count

# Runtime: 284ms (>72.80%)
# Memory: 34.98 (>22.47%)
