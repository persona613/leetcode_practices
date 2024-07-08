"""
112 ms runtime beats 47.15%
17.80 MB memory beats 62.53%
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(set)
        for u, v, w in flights:
            g[u].add((v, w))

        # bellman ford's algorithm
        dp = [float("inf")] * n
        dp[src] = 0
        pre = dp.copy()
        # t = edges number used, at most use k + 1 edges
        for t in range(1, k + 2):
            for u in range(n):
                for v, w in g[u]:
                    if pre[u] + w < dp[v]:
                        dp[v] = pre[u] + w
            pre = dp.copy()
        
        return dp[dst] if dp[dst] != float("inf") else -1