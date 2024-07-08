"""
1752 ms runtime beats 5.08%
17.49 MB memory beats 36.44%
"""
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:        
        # dijk
        def buyapple(city):
            cost = [inf] * n
            cost[city] = 0
            q = [city]
            while q:
                curr = heapq.heappop(q)
                for adj in gf[curr]:
                    if cost[curr] + gf[curr][adj] < cost[adj]:
                        cost[adj] = cost[curr] + gf[curr][adj]
                        heapq.heappush(q, adj)
                        
            mincost = float("inf")
            for i in range(n):
                buycost = cost[i] * (1 + k) + appleCost[i]
                if buycost < mincost:
                    mincost = buycost
            return mincost

        gf = defaultdict(dict)
        for u, v, cost in roads:
            gf[u - 1][v - 1] = cost
            gf[v - 1][u - 1] = cost

        res = []
        for city in range(n):
            res.append(buyapple(city))
        return res