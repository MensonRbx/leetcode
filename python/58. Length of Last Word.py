class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

"""
Best Runtime: 32ms (>89%)
Best Memory: 16.19MB (>95%)
"""
