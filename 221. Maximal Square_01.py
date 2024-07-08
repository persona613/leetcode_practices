"""
Wrong Answer
41 / 78 testcases passed
submitted at May 05, 2024 17:26

Editorial
Input
matrix =
[["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]

Use Testcase
Output
21
Expected
16
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0

            area = max(dp(i-1, j), dp(i, j-1))
            if matrix[i][j] == "0":
                return area

            else: # curr="1"
                area = max(area, 1)

                # compare back-square
                size = min(i, j)
                for d in range(1, size + 1):
                    ni = i-d
                    nj = j-d
                    if matrix[ni][nj] == "0":
                        break # early stop
                    if ni == 0 and nj == 0: # sentinel
                        area = max(area, A[i][j])
                        break
                    sq = A[i][j] - A[ni-1][j] - A[i][nj-1] \
                            + A[ni-1][nj-1]
                    area = max(area, sq)
                return area

        m = len(matrix)
        n = len(matrix[0])

        # 1's area: A(i,j)=A(i,j-1)+A(i-1,j)-A(i-1,j-1)
        A = [[0] * n for _ in range(m)]
        A[0][0] = int(matrix[0][0])
        for j in range(1, n):
            A[0][j] = int(matrix[0][j]) + A[0][j-1]
        for i in range(1, m):
            A[i][0] = int(matrix[i][0]) + A[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                A[i][j] = int(matrix[i][j]) + A[i][j-1] \
                        + A[i-1][j] - A[i-1][j-1]

        return dp(m-1, n-1)