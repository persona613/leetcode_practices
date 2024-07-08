"""
50 ms runtime beats 7.33%
16.62 MB memory beats 18.53%
"""
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # flip most significal digit
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] ^= 1

        # sum of each col
        colsum = []
        for col_list in zip(*grid):
            colsum.append(sum(col_list))

        # filp col if 1's count < 0's
        res = 0
        for col in range(n):
            csum1 = colsum[col]
            if csum1 < m - csum1: # flip
                res += (1 << (n - 1 - col)) * (m - csum1)
            else:
                res += (1 << (n - 1 - col)) * csum1
        return res