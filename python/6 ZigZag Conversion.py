class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_list = [[] for _ in range(numRows)]
        s = list(s)
        curr_row = 0
        increment_count = 1
        while len(s) != 0:
            row_list[curr_row].append(s.pop(0))
            if (curr_row + increment_count) >= len(row_list):
                increment_count = -1
            elif (curr_row + increment_count) < 0:
                increment_count = 1
            curr_row += increment_count
        final = "".join("".join(str_list) for str_list in row_list)
        return final
