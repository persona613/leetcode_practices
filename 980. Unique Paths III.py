"""
69 ms runtime beats 17.92%
16.62 MB memory beats 23.78%
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def backtrack(i, j, sq):
            if (i, j) == end and sq == 0:
                return 1
            
            path = 0
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    path += backtrack(ni, nj, sq - 1)
                    grid[ni][nj] = 0
            return path

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        m = len(grid)
        n = len(grid[0])
        block = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    block += 1
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                    grid[i][j] = 0
        sq = m * n - block
        
        dirs = list(zip((0, 0, 1, -1), (1, -1, 0, 0)))
        return backtrack(start[0], start[1], sq - 1) # -1 for start square