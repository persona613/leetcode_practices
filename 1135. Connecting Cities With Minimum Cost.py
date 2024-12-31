"""
483 ms runtime beats 88.02%
22.59 MB memory beats 66.96%
"""
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # minimum spanning tree: Kruskal's algorithm
        uf = UnionFind(n)
        edges = sorted(connections, key = lambda x: x[2])
        cost = 0
        for u, v, w in edges:
            # one-index to zero-index
            if uf.union(u - 1, v - 1):
                cost += w
        return cost if uf.components == 1 else -1

class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.height = [0] * size
        self.components = size

    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        if self.height[rx] == self.height[ry]:
            self.roots[ry] = self.roots[rx]
            self.height[rx] += 1
        elif self.height[rx] > self.height[ry]:
            self.roots[ry] = self.roots[rx]
        else:
            self.roots[rx] = self.roots[ry]

        self.components -= 1
        return True