"""
117 ms runtime beats 21.52%
22.23 MB memory beats 5.61%
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ri = []
        cj = []
        fs = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fs.add((i, j))
                    ri.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cj.append(j)
        # median
        ki = ri[len(ri)//2]
        kj = cj[len(cj)//2]
        ans = 0
        for i, j in fs:
            ans += abs(i - ki) + abs(j - kj)
        return ans