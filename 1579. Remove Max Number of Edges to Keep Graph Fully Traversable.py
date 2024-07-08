"""
1627 ms runtime beats 66.97%
56.58 MB memory beats 40.72%
"""
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # class edges type
        types = [[] for _ in range(4)]
        for i, e in enumerate(edges):
            types[e[0]].append((e[1], e[2]))

        # construct net with common edges
        # track add edge count
        count = 0
        uf1 = UnionFind(n)
        for u, v in types[3]:
            count += uf1.union(u, v)

        # prepare uf2 by copy uf1 
        uf2 = UnionFind(n, uf1)

        # Alice net
        for u, v in types[1]:
            count += uf1.union(u, v)
        if uf1.edgecnt + 1 != n:
            return -1
        
        # Bob net
        for u, v in types[2]:
            count += uf2.union(u, v)
        if uf2.edgecnt + 1 != n:
            return -1

        return len(edges) - count

class UnionFind:

    def __init__(self, n, uf=None):
        if uf:
            self.root = uf.root[:]
            self.size = uf.size[:]
            self.edgecnt = uf.edgecnt
            return
        self.root = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        self.edgecnt = 0
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        cx = self.size[rx]
        cy = self.size[ry]
        if cx >= cy:
            self.root[ry] = rx
            self.size[rx] += cy
            self.size[ry] = 0
        else:
            self.root[rx] = ry
            self.size[ry] += cx
            self.size[rx] = 0
        self.edgecnt += 1
        return True