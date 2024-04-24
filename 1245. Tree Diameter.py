"""
159 ms runtime beats 35.50%
22.41 MB memory beats 38.19%
"""
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        q = deque([0])
        seen = {0}
        while q:
            n = len(q)
            bag = q.copy()
            for _ in range(n):
                curr = q.popleft()
                for adj in g[curr]:
                    if adj not in seen:
                        seen.add(adj)
                        q.append(adj)

        q = deque([bag[0]])
        seen = {q[0]}
        p = 0
        while q:
            n = len(q)
            p += 1
            for _ in range(n):
                curr = q.popleft()
                for adj in g[curr]:
                    if adj not in seen:
                        seen.add(adj)
                        q.append(adj)
        return p - 1