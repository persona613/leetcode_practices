"""
Wrong Answer
754 / 759 testcases passed

Editorial
Input
grid =
[[1,1,1,1],[1,0,1,0],[0,0,0,0],[0,1,1,1],[1,1,0,1]]

Use Testcase
Output
1
Expected
2
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
                    island.add((ni, nj))
                    dfs(ni, nj, island, seen)

        # translate island cells to one-D serial
        def code(i, j):
            return i * n + j

        # cell id move to (0, 0) for distinct detect
        def translate(island):
            arr = sorted(island)

            # translate vector from (0, 0)
            vec = code(*arr[0])
            for i in range(len(arr)):
                arr[i] = str(code(*arr[i]) - vec)
            return " ".join(arr)

        m = len(grid)
        n = len(grid[0])
        seen = set()
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    island = {(i, j)}
                    dfs(i, j, island, seen)
                    res.add(translate(island))
        return len(res)