"""
85 ms runtime beats 92.01%
18.29 MB memory beats 80.32%
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            for vt in g[node]:
                if seen[vt] == False:
                    seen[vt] = True
                    dfs(vt)

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = [False] * n
        ans = 0
        for i in range(n):
            if seen[i] == False:
                ans += 1
                seen[i] = True
                dfs(i)
        return ans