"""
40 ms runtime beats 16.20%
13.8 MB memory beats 43.56%
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for d in [2,3,5]:
            while n % d == 0:
                n = n // d
        return n == 1