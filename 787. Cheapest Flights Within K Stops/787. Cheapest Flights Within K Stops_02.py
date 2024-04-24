"""
Memory Limit Exceeded
28 / 53 testcases passed
Last Executed Input
Use Testcase
n = 17
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(set)
        for u, v, w in flights:
            g[u].add((v, w))
        ans = inf
        # (cost[i], i, path)
        q = deque([(0, src, 0)])
        while q:
            ct, u, p = q.popleft()
            if u == dst:
                ans = min(ans, ct)
            else:
                if p <= k:
                    for v, w in g[u]:
                        q.append((ct + w, v, p + 1))
        return ans if ans != inf else -1