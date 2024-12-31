"""
48 ms runtime beats 34.19%
16.70 MB memory beats 7.81%
"""
class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and ((stk[-1] == "A" and c == "B") or
                        (stk[-1] == "C" and c == "D")):
                stk.pop()
            else:
                stk.append(c)
        return len(stk)