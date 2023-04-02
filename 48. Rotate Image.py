"""
47 ms runtime beats 31.94%
13.9 MB memory beats 66.85%
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seen = {i:[] for i in range(len(matrix))}
        tmp = None
        n = len(matrix)
        # linear transformation clockwise [[0,1],[-1,0]] 
        # [i, j] => [j, -i+2]
        for i in range(n):
            for j in range(n):
                # trans pos
                x, y = j, -i+(n-1)
                tmp = matrix[i][j]
                while y not in seen[x]:
                    matrix[x][y], tmp = tmp, matrix[x][y]
                    seen[x].append(y)
                    x, y = y, -x+(n-1)

