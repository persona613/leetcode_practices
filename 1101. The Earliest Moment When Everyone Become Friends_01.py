"""
100 ms runtime beats 52.03%
17.02 MB memory beats 15.66%
"""
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for time, a, b in logs:
            k = uf.union(a, b)
            if k == 1:
                return time
        return -1

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
        return self.size