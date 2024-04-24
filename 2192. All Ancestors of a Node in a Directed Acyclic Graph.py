"""
439 ms runtime beats 95.10%
31.32 MB memory beats 94.05%
"""
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def helper(i):
            if res[i] == None:
                tmp = set()
                for adj in g[i]:
                    tmp.add(adj)
                    tmp.update(helper(adj))
                res[i] = sorted(tmp)
            return res[i]

        res = [None] * n
        g = [set() for _ in range(n)]
        for u, v in edges:
            g[v].add(u)

        for i in range(n):
            helper(i)
        return res