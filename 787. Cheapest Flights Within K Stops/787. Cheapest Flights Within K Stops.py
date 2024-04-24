"""
196 ms runtime beats 17.44%
18.51 MB memory beats 38.62%
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(set)
        for u, v, w in flights:
            g[u].add((v, w))
        cost = [[inf] * (k + 2) for _ in range(n)]
        for i in range(k + 2):
            cost[src][i] = 0
        # (currcost, i, path)
        q = [(0, src, 0)]
        while q:
            currcost, u, p = heapq.heappop(q)
            if p + 1 <= k + 1:
                for v, w in g[u]:
                    if v == dst:
                        cost[v][p + 1] = min(cost[v][p + 1], currcost + w)
                    elif currcost + w < cost[v][p + 1]:
                        cost[v][p + 1] = currcost + w
                        heapq.heappush(q, (cost[v][p + 1], v, p + 1))
        ans = min(cost[dst])
        return ans if ans != inf else -1