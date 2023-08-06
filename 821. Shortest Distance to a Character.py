"""
44 ms runtime beats 98.36%
16.5 MB memory beats 34.58%
"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l, r = -1, s.find(c)
        res = [None] * len(s)
        i = 0
        while i < len(s):
            if i == r:
                l = r
                r = s.find(c, r+1)
            if l != -1:
                ld = i - l
            else:
                ld = float("inf")
            if r != -1:
                rd = r - i
            else:
                rd = float("inf")
            res[i] = min(ld, rd)
            i += 1
        return res