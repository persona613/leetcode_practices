"""
140 ms runtime beats 45.73%
14.9 MB memory beats 27.56%
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zi, zj = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zi.add(i)
                    zj.add(j)
                    # back track row
                    for jb in range(j-1, -1, -1):
                        matrix[i][jb] = 0
                    # back track col
                    for ib in range(i-1, -1, -1):
                        matrix[ib][j] = 0
                elif i in zi or j in zj:
                    matrix[i][j] = 0     