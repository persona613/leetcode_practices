"""
1163 ms runtime beats 76.54%
43.14 MB memory beats 54.57%
"""
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cost = [[float("inf")] * n for _ in range(m)]
        cost[0][0] = 0
        # min heap: (curr cost, i, j)
        q = [(0, 0, 0)]
        dirs = list(zip((0, 0, 1, -1), (1, -1, 0, 0)))
        while q:
            cc, ci, cj = heapq.heappop(q)
            if ci == m - 1 and cj == n - 1:
                return cc
            for di, dj in dirs:
                ni = ci + di
                nj = cj + dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if cc + grid[ni][nj] < cost[ni][nj]:
                    cost[ni][nj] = cc + grid[ni][nj]
                    heapq.heappush(q, (cost[ni][nj], ni, nj))
        return cost[m - 1][n - 1]