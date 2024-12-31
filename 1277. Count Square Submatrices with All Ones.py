"""
54 ms runtime beats 89.85%
19.40 MB memory beats 18.06%
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp(i, j): length of max square formed by adding cell(i, j)
        # dp(i, j) = 1 + min(dp(i-1, j-1), dp(i-1,j), dp(i, j-1))
        m = len(matrix)
        n = len(matrix[0])
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # prevent out of index
                    if i == 0 or j == 0:
                        mat[i][j] = 1
                    else:
                        mat[i][j] = 1 + min(
                            mat[i - 1][j - 1],
                            mat[i - 1][j],
                            mat[i][j - 1]
                        )
        return sum(sum(row) for row in mat)
        