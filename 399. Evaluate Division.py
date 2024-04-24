"""
39 ms runtime beats 51.91%
16.52 MB memory beats 81.41%
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(lambda: defaultdict(int))
        for i in range(len(equations)):
            x, y = equations[i]
            g[x][y] = values[i]
            g[y][x] = 1 / values[i]
            
        res = []
        for x, y in queries:
            q = deque([(x, 1)])
            seen = {x}
            while q:
                curr, val = q.popleft()
                if y in g[curr]:
                    res.append(val * g[curr][y])
                    break
                for nxt in g[curr]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, val * g[curr][nxt]))
            else:
                res.append(-1)
        return res
