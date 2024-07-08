"""
335 ms runtime beats 99.83%
22.18 MB memory beats 97.58%
"""
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n, wells)
        pps = sorted(pipes, key = lambda x: x[2])
        for pp in pps:
            uf.union(*pp)
        return uf.totalcost

class UnionFind:
    def __init__(self, size, wells):
        self.parent = [i for i in range(size + 1)]
        self.wellcost = [0] + wells[:]
        # self.size = size
        self.totalcost = sum(wells)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y, p):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            wx = self.wellcost[rootx]
            wy = self.wellcost[rooty]
            maxwell = max(wx, wy)
            minwell = min(wx, wy)
            if p <= maxwell:
                self.totalcost += p - maxwell
                if wx <= wy:
                    self.parent[rooty] = rootx
                    self.wellcost[rooty] = 0
                else:
                    self.parent[rootx] = rooty
                    self.wellcost[rootx] = 0
                # self.size -= 1