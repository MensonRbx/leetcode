bracket_pairs = {
    "}": "{",
    ")": "(",
    "]": "["
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in bracket_pairs.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] != bracket_pairs[c]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(c)
        return len(stack) == 0
