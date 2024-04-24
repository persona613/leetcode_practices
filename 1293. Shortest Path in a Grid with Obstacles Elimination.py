"""
491 ms runtime beats 39.61%
24.63 MB memory beats 33.46%
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def valid(u, v):
            return 0 <= u < m and 0 <= v < n

        m = len(grid)
        n = len(grid[0])
        # node=(i,j,remain to remove,steps)
        q = deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            ln = len(q)
            for _ in range(ln):
                i, j, r, p = q.popleft()
                if i == m - 1 and j == n - 1:
                    return p
                for dx, dy in dirs:
                    ni = i + dx
                    nj = j + dy
                    if valid(ni, nj):
                        if grid[ni][nj] == 0:
                            if (ni, nj, r) not in seen:
                                seen.add((ni, nj, r))
                                q.append((ni, nj, r, p + 1))
                        else:
                            if r > 0 and ((ni, nj, r - 1)) not in seen:
                                seen.add((ni, nj, r - 1))
                                q.append((ni, nj, r - 1, p + 1))
        return -1