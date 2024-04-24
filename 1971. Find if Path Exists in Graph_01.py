"""
1675 ms runtime beats 52.69%
140.40 MB memory beats 24.48%
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(vt, destination):
            if vt == destination:
                return True
            seen.add(vt)
            for nt in g[vt]:
                if nt not in seen:
                    if dfs(nt, destination):
                        return True
            return False

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = set()
        return dfs(source, destination)