"""
23 ms runtime beats 98.25%
16.52 MB memory beats 32.51%
"""
class Solution:
    def tribonacci(self, n: int) -> int:

        @cache
        def dp(i):
            if i <= 2:
                return 1 if i else 0
            return dp(i - 1) + dp(i - 2) + dp(i - 3)

        return dp(n)