class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        startStr = strs[0]
        strs.pop(0)

        newStrsLen = len(strs)
        resultPrefix = ""

        for index, character in enumerate(startStr):

            currentPrefix = startStr[0: index + 1]

            matching = [word for word in strs if word.startswith(currentPrefix)]
            if not len(matching) == newStrsLen:
                return resultPrefix

            resultPrefix = currentPrefix

        return resultPrefix

"""
40 ms runtime, beat 75%
16Mb memory, beats 92%

"""
