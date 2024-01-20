"""
1032 ms runtime beats 28.83%
167.15 MB memory beats 28.43%
"""
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(vt, res):
            for nt in g[vt]:
                if nt != res[-1]:
                    res.append(vt)
                    return dfs(nt, res)
            res.append(vt)

        g = defaultdict(list)
        for x, y in adjacentPairs:
            g[x].append(y)
            g[y].append(x)
        for k in g:
            if len(g[k]) == 1:
                a = k
                break
        res = [a]
        dfs(g[a][0], res)
        return res

