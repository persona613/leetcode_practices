"""
34 ms runtime beats 72.09%
16.50 MB memory beats 81.94%
"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ")":
                tmp = []
                while stk[-1] != "(":
                    tmp.append(stk.pop())
                stk.pop()
                stk.extend(tmp)
            else:
                stk.append(c)
        return "".join(stk)