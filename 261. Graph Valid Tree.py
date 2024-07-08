"""
91 ms runtime beats 30.47%
18.25 MB memory beats 79.49%
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.size == 1

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