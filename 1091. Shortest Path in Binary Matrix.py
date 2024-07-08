"""
485 ms runtime beats 37.04%
18.13 MB memory beats 40.12%
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def getnext(i, j):
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n \
                        and grid[ni][nj] == 0:
                    yield (ni, nj)

        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), 
                (-1, 1), (1, 1), (-1, -1), (1, -1)]
        q = deque([(0, 0, 1)])
        seen = {(0, 0)}
        while q:
            i, j, step = q.popleft()
            if i == n - 1 and j == n - 1:
                return step
            
            for nxtnode in getnext(i, j):
                if nxtnode not in seen:
                    seen.add(nxtnode)
                    q.append((*nxtnode, step + 1))
        return -1