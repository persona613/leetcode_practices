"""
80 ms runtime beats 76.25%
16.84 MB memory beats 60.17%
"""
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # red=0, blue=1
        g = defaultdict(list)
        for u, v in redEdges:
            g[u].append((v, 0))
        for u, v in blueEdges:
            g[u].append((v, 1))

        res = [inf] * n
        seen = {(0, 0), (0, 1)}
        q = deque(seen)
        d = 0
        while q:
            ln = len(q)
            for _ in range(ln):
                curr, color = q.popleft()
                res[curr] = min(res[curr], d)

                for adj, acolor in g[curr]:
                    if acolor != color and (adj, acolor) not in seen:
                        seen.add((adj, acolor))
                        q.append((adj, acolor))
            d += 1

        return [x if x != inf else -1 for x in res]
