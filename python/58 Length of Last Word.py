class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

#Runtime: 28ms (>91%)
#Memory: 16.66MB (>27%)
