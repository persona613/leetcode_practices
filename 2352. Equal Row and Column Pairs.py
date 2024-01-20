"""
447 ms runtime beats 63.08%
21.50 MB memory beats 46.74%
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rd = defaultdict(int)
        cd = defaultdict(int)
        for row in grid:
            t = tuple(row)
            rd[t] += 1
        for i in range(len(grid[0])):
            tmp = []
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            t = tuple(tmp)
            cd[t] += 1
        ans = 0
        for k in rd:
            if k in cd:
                ans += rd[k] * cd[k]
        return ans