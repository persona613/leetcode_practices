"""
91 ms runtime beats 73.12%
18.41 MB memory beats 70.96%
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            for vt in g[node]:
                if vt not in seen:
                    seen.add(vt)
                    dfs(vt)
                    
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        return ans