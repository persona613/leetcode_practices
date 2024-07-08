"""
118 ms runtime beats 76.18%
17.11 MB memory beats 28.98%
"""
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[None] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                x = max(grid[i - 1][j - 1: j + 2])
                y = max(grid[i][j - 1: j + 2])
                z = max(grid[i + 1][j - 1: j + 2])
                res[i - 1][j - 1] = max(x, y, z)
        return res