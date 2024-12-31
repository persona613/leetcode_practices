"""
179 ms runtime beats 96.83%
29.60 MB memory beats 100%
"""
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        # sort all cells with one-d positions
        order = sorted(range(m * n), key = lambda pos: grid[pos // n][pos % n])

        # record minin value had used at each row and col
        rows = [0] * m
        cols = [0] * n

        # replace values from small
        for pos in order:
            k = max(rows[pos // n], cols[pos % n])
            grid[pos // n][pos % n] = k + 1
            rows[pos // n] = k + 1
            cols[pos % n] = k + 1
        return grid
        