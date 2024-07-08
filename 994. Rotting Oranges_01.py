"""
44 ms runtime beats 89.95%
16.50 MB memory beats 78.04%
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        while q:
            ci, cj, t = q.popleft()
            if t > ans:
                ans = t
            
            for di, dj in dirs:
                ni = ci + di
                nj = cj + dj
                if 0 <= ni < m and 0 <= nj < n and \
                        grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj, t + 1))
        for row in grid:
            for a in row:
                if a == 1:
                    return -1
        return ans