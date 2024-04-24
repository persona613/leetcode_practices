"""
39 ms runtime beats 31.52%
16.55 MB memory beats 57.46%
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        if n == 2 : return k * k
        if k == 1 and n > 2: return 0
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        dp[3] = dp[2] * k - k

        # dp[i-3] = pre two post having same color
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] * k - dp[i - 3] * (k - 1)
        return dp[-1]
