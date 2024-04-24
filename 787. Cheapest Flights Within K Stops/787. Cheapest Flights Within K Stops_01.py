"""
Wrong Answer
51 / 53 testcases passed
Input
n = 11
flights =
[[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src = 0
dst = 2
k = 4

Use Testcase
Output 103
Expected 11
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(set)
        for u, v, w in flights:
            g[u].add((v, w))
        cost = [inf] * (n + 1)
        cost[src] = 0
        # (cost[i], i, path)
        q = [(0, src, 0)]
        while q:
            if q[0][1] == dst:
                heapq.heappop(q)
            else:
                currcost, u, p = heapq.heappop(q)
                if p == k:
                    for v, w in g[u]:
                        if v == dst:
                            cost[dst] = min(cost[dst], currcost + w)
                elif p < k:
                    for v, w in g[u]:
                        if currcost + w < cost[v]:
                            cost[v] = currcost + w
                            heapq.heappush(q, (cost[v], v, p + 1))
        return cost[dst] if cost[dst] != inf else -1