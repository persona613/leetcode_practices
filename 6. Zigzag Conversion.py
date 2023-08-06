"""
68 ms runtime beats 81.38%
16.6 MB memory beats 31.94%
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = [[] for _ in range(numRows)]
        row, d = 0, 1
        for c in s:
            res[row].append(c)
            if row == 0: d = 1
            elif row == numRows-1: d = -1
            row += d
        return "".join(["".join(x) for x in res])