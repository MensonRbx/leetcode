class Solution:
    def myAtoi(self, s: str) -> int:
            
        lowest_possible_number = pow(-2, 31)
        highest_possible_number = pow(2, 31) - 1

        s = s.strip()

        for position, letter in enumerate(s):

            if letter == "-" or letter == "+" or letter.isdigit():

                result = 0     

                if len(s) == 1 or not s[position + 1].isdigit():
                    return 0 if not letter.isdigit() else int(letter)

                endPosition = position + 1
                while endPosition < len(s) and s[endPosition].isdigit():
                    endPosition += 1

                result = s[position:endPosition]
                result = int(result)

                if result > highest_possible_number:
                    return highest_possible_number
                elif result < lowest_possible_number:
                    return lowest_possible_number
                return result
            elif not letter.isdigit():
                return 0

        return 0

"""
Best Runtime: 42ms (~60%)
Best Memory: 16.06MB (~99%)
"""
