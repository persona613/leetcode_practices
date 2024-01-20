"""
Wrong Answer
30 / 44 testcases passed

Input
workers =
[[239,904],[191,103],[260,117],[86,78],[747,62]]
bikes =
[[660,8],[431,772],[78,576],[894,481],[451,730],[155,28]]

Use Testcase
Output
2764
Expected
1886
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(bk, wk):
            return abs(bikes[bk][0] - workers[wk][0]) \
                    + abs(bikes[bk][1] - workers[wk][1])

        def dfs(i, mask, n):
            if (i, mask) in memo:
                return memo[(i, mask)]
            if mask + 1 == 2 ** n:
                return 0
            mi = inf
            for j in range(n):
                mk = mask ^ (1 << j)
                if mk > mask:
                    dist = distance(i, j) + dfs(i+1, mk, n)
                    mi = min(mi, dist)
            memo[(i, mask)] = mi
            return memo[(i, mask)]

        n = len(workers)
        memo = dict()
        return dfs(0, 0, n)