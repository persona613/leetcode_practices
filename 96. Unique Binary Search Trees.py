"""
34 ms runtime beats 60.82%
16.59 MB memory beats 25.58%
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                # dp[left] * dp[right]
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        