"""
94 ms runtime beats 20.03%
18.20 MB memory beats 88.07%
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[None] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                left = up = float("inf")
                if i + j == 0:
                    continue
                if i != 0:
                    up = dp[i - 1][j]
                if j != 0:
                    left = dp[i][j - 1]
                dp[i][j] = min(left, up) + curr
        return dp[-1][-1]