"""
9728 ms runtime beats 5.36%
176.47 MB memory beats 5.05%
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(bk, wk):
            return abs(bikes[bk][0] - workers[wk][0]) \
                    + abs(bikes[bk][1] - workers[wk][1])

        def dfs(pos, mask, n, m):
            if (pos, mask) in memo:
                return memo[(pos, mask)]
            if mask + 1 == 2 ** n:
                memo[(pos, mask)] = 0
                return 0
            mi = inf
            for i in range(m):
                ps = pos ^ (1 << i)
                if ps > pos:
                    for j in range(n):
                        mk = mask ^ (1 << j)
                        if mk > mask:
                            dist = dic[i][j] + dfs(ps, mk, n, m)
                            mi = min(mi, dist)
            memo[(pos, mask)] = mi
            return memo[(pos, mask)]

        n = len(workers)
        m = len(bikes)
        memo = dict()
        dic = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dic[i][j] = distance(i, j)
        return dfs(0, 0, n, m)