"""
2694 ms runtime beats 57.53%
16.62 MB memory beats 31.94%
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        def backtracking(i, j, g):
            if g > ans[0]:
                ans[0] = g
            
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and grid[ni][nj] != 0:
                    og = grid[ni][nj]
                    g += og
                    grid[ni][nj] = 0
                    backtracking(ni, nj, g)
                    g -= og
                    grid[ni][nj] = og

        m = len(grid)
        n = len(grid[0])
        dirs = list(zip((1,-1,0,0), (0,0,1,-1)))
        ans = [0]
        g = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    og = grid[i][j]
                    g += og
                    grid[i][j] = 0
                    backtracking(i, j, g)
                    g -= og
                    grid[i][j] = og
        return ans[0]