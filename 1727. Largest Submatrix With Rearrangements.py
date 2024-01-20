"""
1059 ms runtime beats 91.67%
42.88 MB memory beats 18.06%
"""
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for j in range(m):
            for i in range(1, n):
                a = matrix[i][j]
                if a == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
        ans = 0
        for row in matrix:
            row.sort(reverse=True)
            for j, v in enumerate(row, 1):
                if j * v > ans:
                    ans = j * v
        return ans



