"""
560 ms runtime beats 93.01%
84.38 MB memory beats 63.87%
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # try kruskal's algorithm
        n = len(points)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        heapq.heapify(edges)
        uf = UnionFind(n)
        ans = 0
        # instead of edges num == n-1
        while uf.size > 1:
            d, u, v = heapq.heappop(edges)
            if uf.connect(u, v) is False:
                uf.union(u, v)
                ans += d
        return ans

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.size = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            rx = self.rank[rootx]
            ry = self.rank[rooty]
            if rx > ry:
                self.parent[rooty] = rootx
            elif rx < ry:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.size -= 1
    
    def connect(self, x, y):
        return self.find(x) == self.find(y)