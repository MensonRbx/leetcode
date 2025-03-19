class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        l, r = 0, len(height)-1
        while l < r:
            lVal, rVal = height[l], height[r]
            area = min(lVal, rVal) * (r-l)
            largest = max(largest, area)
            if lVal <= rVal:
                l += 1
            else:
                r -= 1
        return largest
        
