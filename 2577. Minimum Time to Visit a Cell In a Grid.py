"""
699 ms runtime beats 82.30%
30.74 MB memory beats 78.47%
"""
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
            
        m = len(grid)
        n = len(grid[0])
        cost = [[float("inf")] * n for _ in range(m)]
        cost[0][0] = 0
        dirs = list(zip((0, 0, 1, -1), (1, -1, 0, 0)))
        # min heap: (curr time, ci, cj)
        q = [(0, 0, 0)]
        END = (m - 1, n - 1)
        while q:
            curr, ci, cj = heappop(q)
            if (ci, cj) == END:
                return curr
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue

                if curr >= grid[ni][nj]:
                    newtime = curr + 1
                else:
                    if (grid[ni][nj] - curr) % 2 == 1:
                        newtime = grid[ni][nj]
                    else:
                        newtime = grid[ni][nj] + 1

                if newtime < cost[ni][nj]:
                    cost[ni][nj] = newtime
                    heappush(q, (newtime, ni, nj))
        return cost[m - 1][n - 1]