"""
35 ms runtime beats 54.36%
14.1 MB memory beats 9.7%
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[None for j in range(n)] for i in range(m)]
        def tp(i, j):
            if mat[i][j]:
                return mat[i][j]
            if i == 0 and j == 0:
                mat[i][j] = 1
                return mat[i][j]
            if i-1 < 0:
                mat[i][j] = tp(i, j-1)
            elif j-1 < 0:
                mat[i][j] = tp(i-1, j)
            else:
                mat[i][j] = tp(i-1, j) + tp(i, j-1)
            return mat[i][j]

        tp(m-1, n-1)
        return mat[m-1][n-1]