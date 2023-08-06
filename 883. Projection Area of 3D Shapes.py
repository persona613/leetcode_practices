"""
90 ms runtime beats 44.55%
16.45 MB memory beats 37.62%
"""
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # xi=row, yj=colume
        jmax = [0] * n
        ans = 0
        for i in range(n):
            rmax = 0
            for j in range(n):
                if grid[i][j] != 0:
                    ans += 1
                    rmax = max(rmax, grid[i][j])
                    jmax[j] = max(jmax[j], grid[i][j])
            ans += rmax
        return ans + sum(jmax)