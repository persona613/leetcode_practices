"""
271 ms runtime beats 85.00%
18.26 MB memory beats 51.15%
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n

        def search():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return (i, j)

        def dfs(ci, cj):
            grid[ci][cj] = 2
            for di, dj in dirs:
                ni = ci + di
                nj = cj + dj
                if not valid(ni, nj) or grid[ni][nj] == 2:
                    continue
                if grid[ni][nj] == 1:
                    dfs(ni, nj)
                else:
                    source.append((ni, nj))

        def bfs():
            step = 0
            while source:
                for _ in range(len(source)):
                    ci, cj = source.popleft()
                    for di, dj in dirs:
                        ni = ci + di
                        nj = cj + dj
                        if not valid(ni, nj):
                            continue
                        if grid[ni][nj] == 2:
                            continue
                        # find second island
                        if grid[ni][nj] == 1:
                            return step + 1
                        if (ni, nj) not in seen_water:
                            seen_water.add((ni, nj))
                            source.append((ni, nj))
                step += 1

        n = len(grid)
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))

        # search first island and bridge source water cell
        ci, cj = search()
        source = deque()
        dfs(ci, cj)

        seen_water = set(source)
        return bfs()