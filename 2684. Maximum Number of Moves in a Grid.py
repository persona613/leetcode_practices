"""
324 ms runtime beats 24.24%
27.04 MB memory beats 92.93%
"""
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for c in range(n - 2, -1, -1):
            for r in range(m):
                curr = grid[r][c]
                if r > 0 and grid[r - 1][c + 1] > curr:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c + 1] + 1)
                if grid[r][c + 1] > curr:
                    dp[r][c] = max(dp[r][c], dp[r][c + 1] + 1)
                if r < m - 1 and grid[r + 1][c + 1] > curr:
                    dp[r][c] = max(dp[r][c], dp[r + 1][c + 1] + 1)
        return max(dp[r][0] for r in range(m))