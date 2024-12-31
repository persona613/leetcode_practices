"""
2343 ms runtime beats 5.88%
59.61 MB memory beats 37.65%
"""
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        # build graph
        g = defaultdict(dict)
        for u, v, cost in highways:
            g[u][v] = cost
            g[v][u] = cost

        # cost = {node: {discounts left: cost default is inf)}}
        cost = defaultdict(lambda: defaultdict(lambda: float(inf)))

        # init start node
        cost[0][discounts] = 0

        # heap queue: (curr cost, discounts left, node)
        q = [(0, discounts, 0)]
        while q:
            currcost, d, node = heappop(q)
            if currcost > cost[node][d]:
                continue
            for adj in g[node]:
                # edge not use discount
                if currcost + g[node][adj] < cost[adj][d]:
                    cost[adj][d] = currcost + g[node][adj]
                    heappush(q, (cost[adj][d], d, adj))
                # edge use discount
                if d > 0 and currcost + g[node][adj] // 2 < cost[adj][d - 1]:
                    cost[adj][d - 1] = currcost + g[node][adj] // 2
                    heappush(q, (cost[adj][d - 1], d - 1, adj))
        if n - 1 not in cost:
            return -1
        return min(cost[n - 1].values())