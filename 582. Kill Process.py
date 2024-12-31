"""
321 ms runtime beats 50.65%
26.61 MB memory beats 38.82%
"""
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        def dfs(g, node, res):
            res.append(node)
            for chi in g[node]:
                dfs(g, chi, res)
            return res

        g = defaultdict(list)
        for chi, par in zip(pid, ppid):
            g[par].append(chi)

        return dfs(g, kill, [])