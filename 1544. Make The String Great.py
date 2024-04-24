"""
34 ms runtime beats 78.84%
16.58 MB memory beats 46.83%
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and abs(ord(c) - ord(stk[-1])) == 32:
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)