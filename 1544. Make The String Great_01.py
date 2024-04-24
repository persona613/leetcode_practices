"""
38 ms runtime beats 77.0%
17.34 MB memory beats 7.92%
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if not stk:
                stk.append(c)
            else:
                p = stk[-1]
                if p.isupper() and p.lower()==c:
                    stk.pop()
                elif p.islower() and p.upper()==c:
                    stk.pop()
                else:
                    stk.append(c)
        return "".join(stk)