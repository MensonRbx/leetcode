class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r = 0, 1
        longest_len = 1
        curr_len = 1 # Start at one, since min val is one len and array with 1 element
                     # is still valid
        while l < len(nums) and r < len(nums):
            curr_l = l
            fail_flag = False
            while curr_l != r:
                bit0 = nums[curr_l] & nums[r]
                if bit0 != 0:
                    fail_flag = True
                    break
                curr_l += 1
            if not fail_flag: # All valid bitwise
                curr_len += 1
                longest_len = max(curr_len, longest_len)
                r += 1
            else:
                l += 1
                r = l + 1
                curr_len = 1                    
        return longest_len
