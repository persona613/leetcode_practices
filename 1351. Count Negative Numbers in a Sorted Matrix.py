"""
107 ms runtime beats 91.61%
17.4 MB memory beats 63.5%
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        i, j = 0, n-1
        while i<m and j>=0:
            if grid[i][j] >=0:
                i += 1
            else:
                ans += m-i
                j -= 1
        return ans