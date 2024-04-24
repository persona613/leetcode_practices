"""
434 ms runtime beats 78.31%
18.02 MB memory beats 50.11%
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                (-1, 1), (1, 1), (-1, -1), (1, -1)]
        q = deque([(0, 0, 1)])
        seen = {(0, 0)}
        while q:
            i, j, step = q.popleft()
            if i == n - 1 and j == n - 1:
                return step
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n \
                and grid[ni][nj] == 0 \
                and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    q.append((ni, nj, step + 1))
        return -1