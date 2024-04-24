"""
56 ms runtime beats 12.89%
16.71 MB memory beats 57.55%
"""
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        def bfs(u, v):
            if u == v:
                return True
            seen = {u}
            q = deque([u])
            while q:
                curr = q.popleft()
                if v in g[curr]:
                    g[u].add(v)
                    g[v].add(u)
                    return True
                for adj in g[curr]:
                    if adj not in seen:
                        seen.add(adj)
                        q.append(adj)
            return False
            
        g = defaultdict(set)
        for eq in equations:
            if eq[1] == "=":
                u = eq[0]
                v = eq[3]
                g[u].add(v)
                g[v].add(u)
        for eq in equations:
            if eq[1] == "!":
                if bfs(eq[0], eq[3]):
                    return False
        return True