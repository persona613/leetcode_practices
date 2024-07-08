"""
126 ms runtime beats 90.65%
17.46 MB memory beats 53.53%
"""
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7
        col = max(k + 1, target + 1)
        prev = [0] * col
        dp = prev.copy()
        # init
        for t in range(1, k + 1):
            prev[t] = 1
        for i in range(n - 1):
            for t in range(1, target + 1):
                start = max(0, t - k)
                dp[t] = sum(prev[start:t]) % mod
            prev, dp = dp, prev
        return prev[target]