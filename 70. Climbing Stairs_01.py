"""
35 ms runtime beats 75.79%
14 MB memory beats 11.61%
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        def recur_cs(n):
            if n in cache:
                return cache[n]
            if n < 3:
                return n
            res = recur_cs(n-1)+recur_cs(n-2)
            cache[n] = res
            return res
        
        return recur_cs(n)