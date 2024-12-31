"""
650 ms runtime beats 7.05%
28.68 MB memory beats 47.81%
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
        # bellman ford algorithm
        for _ in range(n - 1):
            has_update = 0
            for i in range(len(edges)):
                u, v = edges[i]
                p = succProb[i]
                if pbs[u] * p > pbs[v]:
                    pbs[v] = pbs[u] * p
                    has_update = 1
                if pbs[v] * p > pbs[u]:
                    pbs[u] = pbs[v] * p
                    has_update = 1
            if not has_update:
                break
        return pbs[end_node]