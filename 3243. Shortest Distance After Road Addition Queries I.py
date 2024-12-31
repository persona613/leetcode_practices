"""
462 ms runtime beats 69.93%
17.94 MB memory beats 8.31%
"""
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def bfs(g, st, nd):
            q = deque([0])
            seen = {0}
            step = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr == nd:
                        return step
                    for adj in g[curr]:
                        if adj not in seen:
                            seen.add(adj)
                            q.append(adj)
                step += 1

        g = defaultdict(list)
        for u in range(n - 1):
            g[u].append(u + 1)

        res = []
        for u, v in queries:
            g[u].append(v)
            res.append(bfs(g, 0, n - 1))
        return res
        