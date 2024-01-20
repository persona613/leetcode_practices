"""
578 ms runtime beats 78.24%
19.50 MB memory beats 60.59%
"""
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.V = n
        self.G = [[] for _ in range(n)]
        for u, v, c in edges:
            self.G[u].append([v, c])

    def addEdge(self, edge: List[int]) -> None:
        self.G[edge[0]].append([edge[1], edge[2]])

    def shortestPath(self, node1: int, node2: int) -> int:
        cost = [inf] * self.V
        cost[node1] = 0
        pq = [[0, node1]]
        while pq:
            d, u = heapq.heappop(pq)
            if u == node2:
                return cost[u]
            for v, c in self.G[u]:
                if cost[v] > d + c:
                    cost[v] = d + c
                    heapq.heappush(pq, [cost[v], v])
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)