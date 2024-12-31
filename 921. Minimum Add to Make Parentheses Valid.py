"""
38 ms runtime beats 35.01%
16.46 MB memory beats 71.14%
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and stk[-1] == "(" and c == ")":
                stk.pop()
            else:
                stk.append(c)
        return len(stk)