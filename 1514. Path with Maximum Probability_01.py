"""
556 ms runtime beats 51.13%
29.72 MB memory beats 19.43%
"""
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            g[u].append((v, succProb[i]))
            g[v].append((u, succProb[i]))

        pbs = [0] * n
        pbs[start_node] = 1
        # max heap
        q = [(-1, start_node)]
        while q:
            p, curr = heappop(q)
            p *= -1
            if curr == end_node:
                return p
            for adj, adj_pb in g[curr]:
                if p * adj_pb > pbs[adj]:
                    pbs[adj] = p * adj_pb
                    heappush(q, (-1 * pbs[adj], adj))
        return pbs[end_node]