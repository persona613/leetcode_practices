"""
719 ms runtime beats 81.71%
68.67 MB memory beats 88.80%
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def distance(u, v):
            x1, y1 = points[u][0], points[u][1]
            x2, y2 = points[v][0], points[v][1]
            return abs(x1 - x2) + abs(y1 - y2)

        # try prim's algorithm
        n = len(points)
        unvisited = set(range(1, n))
        visited = {0}
        curr = ans = 0
        q = []
        while len(visited) < n:
            for adj in unvisited:
                dis = distance(curr, adj)
                heapq.heappush(q, (dis, adj))
            # pick one pt from unvisited set
            uvpt = len(unvisited)
            while len(unvisited) == uvpt:
                dis, nxt = heapq.heappop(q)
                if nxt not in visited:
                    visited.add(nxt)
                    unvisited.remove(nxt)
                    ans += dis
                    curr = nxt
        return ans