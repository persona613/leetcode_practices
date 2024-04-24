"""
146 ms runtime beats 32.15%
26.17 MB memory beats 17.13%
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if j < 0 or j >= m:
                return inf
            if i == n - 1:
                return matrix[i][j]
            
            return matrix[i][j] + min(dfs(i + 1, j - 1),
                    dfs(i + 1, j), dfs(i + 1, j + 1))

        n = len(matrix)
        m = len(matrix[0])
        ans = inf
        for k in range(m):
            ans = min(ans, dfs(0, k))
        return ans