"""
Wrong Answer
4 / 39 testcases passed

Editorial
Input
grid =
[[920212616,142237098,345501974,533487831,269413793,819692083,469106291,483049590,63489034,58052923]]

Use Testcase
Output
[[2,1,2,3,1,2,1,3,2,1]]
Expected
[[10,3,5,8,4,9,6,7,2,1]]
"""
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:

        # find max of neighbor cells that's smaller than (i, j)
        def get_max(i, j):
            mx = 0
            if i > 0 and grid[i - 1][j] < grid[i][j]:
                    mx = max(mx, grid[i - 1][j])
            if i < m - 1 and grid[i + 1][j] < grid[i][j]:
                    mx = max(mx, grid[i + 1][j])
            if j > 0 and grid[i][j - 1] < grid[i][j]:
                    mx = max(mx, grid[i][j - 1])
            if j < n - 1 and grid[i][j + 1] < grid[i][j]:
                    mx = max(mx, grid[i][j + 1])
            return mx

        m = len(grid)
        n = len(grid[0])

        # sort all cells
        order = sorted(range(m * n), key = lambda pos: grid[pos // n][pos % n])
        for pos in order:
            k = get_max(pos // n, pos % n)
            grid[pos // n][pos % n] = k + 1
        return grid