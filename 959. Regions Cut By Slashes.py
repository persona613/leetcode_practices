"""
125 ms runtime beats 57.31%
17.71 MB memory beats 31.23%
"""
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = n * 3
        mat = [[0] * m for _ in range(m)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    mi = i * 3
                    mj = j * 3
                    mat[mi][mj + 2] = 1
                    mat[mi + 1][mj + 1] = 1
                    mat[mi + 2][mj] = 1
                elif grid[i][j] == "\\":
                    mi = i * 3
                    mj = j * 3
                    mat[mi][mj] = 1
                    mat[mi + 1][mj + 1] = 1
                    mat[mi + 2][mj + 2] = 1

        dirs = list(zip((0,1,0,-1), (1,0,-1,0)))
        def dfs(i, j):
            for di, dj in dirs:
                ci = i + di
                cj = j + dj
                if 0 <= ci < m and 0 <= cj < m \
                        and mat[ci][cj] == 0:
                    mat[ci][cj] = 1
                    dfs(ci, cj)
        ans = 0
        for i in range(m):
            for j in range(m):
                if mat[i][j] == 0:
                    mat[i][j] = 1
                    dfs(i, j)
                    ans += 1
        return ans