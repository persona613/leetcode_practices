"""
Time Limit Exceeded
46 / 53 testcases passed
Last Executed Input
Use Testcase
n = 83
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(set)
        for u, v, w in flights:
            g[u].add((v, w))
        cost = [[inf] * (k + 1) for _ in range(n + 1)]
        cost[src][0] = 0
        # (currcost, i, path)
        q = deque([(0, src, -1)])
        while q:
            currcost, u, p = q.popleft()
            if p < k:
                for v, w in g[u]:
                    if v == dst:
                        cost[v][p] = min(cost[v][p], currcost + w)
                    elif currcost + w < cost[v][p]:
                        cost[v][p] = currcost + w
                        q.append((cost[v][p], v, p + 1))
        ans = min(cost[dst])
        return ans if ans != inf else -1