"""
58 ms runtime beats 59.68%
17.92 MB memory beats 73.15%
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        cnt = k
        stk = []
        for c in num:
            while stk and stk[-1] > c and cnt:
                stk.pop()
                cnt -= 1
            stk.append(c)
            
        while cnt and stk:
            stk.pop()
            cnt -= 1
        res = "".join(stk).lstrip("0")
        return res if res else "0"