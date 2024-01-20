"""
1349 ms runtime beats 83.93%
51.87 MB memory beats 60.71%
"""
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rs, cs = [], []
        for row in grid:
            cnt = sum(row)
            rs.append(cnt - (n - cnt))
        for j in range(n):
            cnt = 0
            for i in range(m):
                cnt += grid[i][j]
            cs.append(cnt - (m - cnt))
        res = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = rs[i] + cs[j]
        return res