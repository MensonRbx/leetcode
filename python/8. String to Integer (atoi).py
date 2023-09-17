class Solution:
    def myAtoi(self, s: str) -> int:

        result = 0

        l_clamp = pow(-2, 31)
        h_clamp = pow(2, 31) - 1

        for index, char in enumerate(s):
            if char == " ":
                continue
            
            if char == "-" or char == "+" or char.isdigit():

                if len(s) == 1 or not s[index + 1].isdigit():
                    return 0 if not char.isdigit() else int(char)

                lastIndex = index + 1
                while lastIndex < len(s) and s[lastIndex].isdigit():
                    lastIndex += 1

                result = s[index:lastIndex]
                result = int(result)

                if result > h_clamp:
                    return h_clamp
                elif result < l_clamp:
                    return l_clamp
                return result

            elif not char.isdigit():
                return 0

        return 0
