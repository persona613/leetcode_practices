"""
117 ms runtime beats 20.26%
18.54 MB memory beats 21.47%
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j, island, seen):
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and grid[ni][nj] == 0 \
                    and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    island.add((ni, nj))
                    dfs(ni, nj, island, seen)
            return island

        m = len(grid)
        n = len(grid[0])
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))

        # find islands
        islands = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in seen:
                    seen.add((i, j))
                    island = dfs(i, j, {(i, j)}, seen)
                    islands.append(island)
        
        # minus corner islands
        cnt = 0
        for island in islands:
            for i, j in island:
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    break
            else:
                cnt += 1
        return cnt
        