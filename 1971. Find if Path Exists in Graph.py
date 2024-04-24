"""
8403 ms runtime beats 5.02%
107.38 MB memory beats 85.17%
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([source])
        seen = [False] * n
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            seen[curr] = True
            for v in g[curr]:
                if not seen[v]:
                    q.append(v)
        return False
        