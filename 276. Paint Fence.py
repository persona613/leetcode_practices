"""
30 ms runtime beats 86.20%
16.54 MB memory beats 51.79%
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:

        # all cnt - 3-adj-same-color
        # i == i-1 == i-2 = 1*1*dp[i-2]
        # and i-2 must not equal i-3
        @lru_cache(None)
        def dp(i):
            if i <= 2:
                return k ** i
            if i == 3:
                return k ** 3 - k
            return dp(i - 1) * k - dp(i - 3) * (k - 1)

        if k == 1 and n > 2:
            return 0
        return dp(n)