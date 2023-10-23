"""
565 ms runtime beats 23.46%
108.3 MB memory beats 27.93%
"""
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        mo = 10**9+7
        def rec(sp, p, ln):
            if p<1 or p>ln:
                return 0
            if sp == 0:
                if p == 1: 
                    return 1
                else:
                    return 0
            if (sp, p) in memo:
                return memo[(sp,p)]
            m = rec(sp-1, p, ln)
            l = rec(sp-1, p+1, ln)
            r = rec(sp-1, p-1, ln)
            memo[(sp,p)] = (m+l+r) % mo
            return memo[(sp,p)]
        res = rec(steps, 1, arrLen)
        return res