"""
194 ms runtime beats 23.33%
17.27 MB memory beats 83.94%
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)
        p = []
        for i in range(n):
            root = uf.find(i)
            if root not in p:
                p.append(root)
        return len(p)


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            xr = self.rank[rootx]
            yr = self.rank[rooty]
            if xr < yr:
                self.root[rootx] = rooty
            elif xr > yr:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

    def connect(self, x, y):
        return  self.find(x) == self.find(y)

