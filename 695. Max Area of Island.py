"""
117 ms runtime beats 59.62%
18.48 MB memory beats 43.15%
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(node):
            area = 1
            for dx, dy in dirs:
                ni = node[0] + dx
                nj = node[1] + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == 1 and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        area += dfs((ni, nj))
            return area

        n = len(grid)
        m = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    ans = max(ans, dfs((i, j)))
        return ans