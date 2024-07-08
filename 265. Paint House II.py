"""
122 ms runtime beats 52.78%
16.56 MB memory beats 92.21%
"""
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m = len(costs)
        n = len(costs[0])
        dp = [[None] * n for _ in range(m)]
        dp[0] = costs[0][:]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = costs[i][j] + \
                        min(min(dp[i - 1][:j], default = inf), 
                        min(dp[i - 1][j + 1:], default = inf))
        return min(dp[-1])