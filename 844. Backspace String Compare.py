"""
49 ms runtime beats 6.87%
16.3 MB memory beats 54.52%
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ks = []
        kt = []
        for c in s:
            if c != "#":
                ks.append(c)
            elif ks:
                ks.pop()
        for c in t:
            if c != "#":
                kt.append(c)
            elif kt:
                kt.pop()
        return ks == kt