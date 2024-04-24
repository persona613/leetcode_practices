"""
56 ms runtime beats 50.19%
16.66 MB memory beats 82.30%
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        # min-cost to stand on first step (1-index)
        dp[1] = cost[1 - 1]
        for i in range(2, n + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])
        return min(dp[n], dp[n - 1])
        