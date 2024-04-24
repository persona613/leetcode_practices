"""
473 ms runtime beats 73.42%
18.04 MB memory beats 99.22%
"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in [0, m - 1]:
            for j in range(n):
                if grid[i][j] == 1:
                    seen[i][j] = True
                    q.append((i, j))
        for i in range(1, m - 1):
            for j in [0, n - 1]:
                if grid[i][j] == 1:
                    seen[i][j] = True
                    q.append((i, j))
        while q:
            ci, cj = q.popleft()
            for dx, dy in dirs:
                ni, nj = ci + dx, cj + dy
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1 and seen[ni][nj] == False:
                        seen[ni][nj] = True
                        q.append((ni, nj))
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and seen[i][j] == False:
                    ans += 1
        return ans
