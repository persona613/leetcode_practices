"""
38 ms runtime beats 89.18%
16.80 MB memory beats 24.11%
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[None for j in range(n)] for i in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0: return 0
            if dp[i][j] != None:
                return dp[i][j]
            if i == 0 and j== 0:
                dp[i][j] = 1
                return 1
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                return 0
            
            dp[i][j] = dfs(i-1, j) + dfs(i, j-1)
            return dp[i][j]
            
        if obstacleGrid[0][0] == 1:
            return 0
        return dfs(m-1, n-1)