"""
64 ms runtime beats 98.84%
18.83 MB memory beats 76.01%
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def dfs(x, y, moves):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 1
            if dp[x][y][moves]:
                return dp[x][y][moves]
            if moves <= x and moves <= y \
                and moves < m - x \
                and moves < n - y:
                dp[x][y][moves] = 0
                return 0

            dp[x][y][moves] = (dfs(x, y - 1, moves - 1) \
                            + dfs(x, y + 1, moves - 1) \
                            + dfs(x - 1, y, moves - 1) \
                            + dfs(x + 1, y, moves -1)) % self.mod
            return dp[x][y][moves]
        
        dp = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        self.mod = 10 ** 9 + 7
        return dfs(startRow, startColumn , maxMove)