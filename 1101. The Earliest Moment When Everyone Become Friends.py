"""
96 ms runtime beats 70.96%
16.78 MB memory beats 95.86%
"""
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        uf = UnionFind(n)
        k = n
        for time, a, b in logs:
            k -= uf.union(a, b)
            if k == 1:
                return time
        return -1

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
            
        rx = self.rank[rootx]
        ry = self.rank[rooty]
        if rx > ry:
            self.parent[rooty] = rootx
        elif rx < ry:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        return True