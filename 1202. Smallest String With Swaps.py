"""
476 ms runtime beats 89.69%
52.83 MB memory beats 76.22%
"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs: return s
        n = len(s)
        uf = UnionFind(n)
        for i, j in pairs:
            uf.union(i, j)

        # component: {root: [chars]}
        dic = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            dic[root].append(s[i])
        for k in dic:
            dic[k].sort(reverse = True)
        
        res = []
        for i in range(n):
            root = uf.find(i)
            res.append(dic[root].pop())
        return "".join(res)

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