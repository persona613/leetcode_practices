"""
347 ms runtime beats 98.22%
18.65 MB memory beats 39.16%
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        gf = [[] for _ in range(n + 1)]
        for u, v, w in times:
            gf[u].append((v, w))

        # try dijkstra
        dtimes = [inf] * (n + 1)
        dtimes[k] = 0
        visited = set()
        # (accumulate time, idx)
        q = [(0, k)]
        while q and len(visited) < n:
            acctime, curr = heapq.heappop(q)
            for adj, dt in gf[curr]:
                if adj not in visited and \
                        acctime + dt < dtimes[adj]:
                    dtimes[adj] = acctime + dt
                    heapq.heappush(q, (dtimes[adj], adj))
            visited.add(curr)
        
        mx = max(dtimes[1:])
        return -1 if mx == inf else mx