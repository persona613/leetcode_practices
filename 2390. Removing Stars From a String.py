"""
130 ms runtime beats 96.16%
19.07 MB memory beats 14.31%
"""
class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c == "*":
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)