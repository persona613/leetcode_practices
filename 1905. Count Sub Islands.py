"""
2515 ms runtime beats 14.49%
62.98 MB memory beats 21.57%
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        def dfs(i, j, seen, island):
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and grid2[ni][nj] == 1 \
                        and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    island.add((ni, nj))
                    dfs(ni, nj, seen, island)
        res = []
        seen = set()
        m = len(grid1)
        n = len(grid1[0])
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    island = {(i, j)}
                    dfs(i, j, seen, island)
                    res.append(island.copy())
        ans = 0
        for land in res:
            for i, j in land:
                if grid1[i][j] == 0:
                    break
            else:
                ans += 1
        return ans