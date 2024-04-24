"""
108 ms runtime beats 96.83%
18.08 MB memory beats 61.34%
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = matrix[0]
        nxt = [None] * m
        
        for i in range(1, n):
            for j in range(m):
                if 0 < j:
                    nxt[j] = matrix[i][j] + min(dp[j-1:j+2])
                else:
                    nxt[j] = matrix[i][j] + min(dp[j:j+2])
            dp, nxt = nxt, dp
        return min(dp)