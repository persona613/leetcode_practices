"""
37 ms runtime beats 81.03%
16.40 MB memory beats 98.46%
"""
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # all 8 magic square
        g = {
            (4,3,8,9,5,1,2,7,6),
            (2,9,4,7,5,3,6,1,8),
            (6,7,2,1,5,9,8,3,4),
            (8,1,6,3,5,7,4,9,2),
            (4,9,2,3,5,7,8,1,6),
            (8,3,4,1,5,9,6,7,2),
            (6,1,8,7,5,3,2,9,4),
            (2,7,6,9,5,1,4,3,8)
        }
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        # left-top corner
        for i in range(m - 2):
            for j in range(n - 2):
                a = []
                for r in range(i, i + 3):
                    a.extend(grid[r][j: j + 3])
                if tuple(a) in g:
                    cnt += 1
        return cnt