"""
182 ms runtime beats 16.57%
18.14 MB memory beats 36.53%
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        # collect island's cell
        def dfs(i, j, island, seen):
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and grid[ni][nj] == 1 \
                        and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    island.append([ni, nj])
                    dfs(ni, nj, island, seen)

        # cell id move to (0, 0) for distinct detect
        def translate(island):
            arr = sorted(island)

            # translate vector from (0, 0)
            vi, vj = arr[0][0], arr[0][1]
            for i in range(len(arr)):
                arr[i][0] -= vi
                arr[i][1] -= vj
            return tuple(tuple(p) for p in arr)

        m = len(grid)
        n = len(grid[0])
        seen = set()
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    island = [[i, j]]
                    dfs(i, j, island, seen)
                    res.add(translate(island))
        return len(res)