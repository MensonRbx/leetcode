class Solution:
    def reverseWords(self, s: str) -> str:
        finalString = ""
        for word in s.split(" "):
            finalString += (word[::-1] + " ")
            
        return finalString.strip()

"""
Best Runtime: 37ms (>89%)
Best Memory: 17.03MB (>41%)
"""
