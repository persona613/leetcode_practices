"""
29 ms runtime beats 92.58%
16.79 MB memory beats 18.82%
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # search and return weights product
        def dfs(start, target, seen):
            if start == target:
                return 1

            for adj in g[start]:
                if adj not in seen:
                    seen.add(adj)
                    ret = dfs(adj, target, seen)
                    if ret is not None:
                        return ret * g[start][adj]

        keys = set()
        for eq in equations:
            # keys = keys.union(eq)
            keys |= set(eq)
        uf = UnionFind(keys)
        
        g = defaultdict(lambda: defaultdict(int))
        for i in range(len(equations)):
            x, y = equations[i]
            g[x][y] = values[i]
            g[y][x] = 1 / values[i]
            uf.union(x, y)
        
        res = []
        for x, y in queries:
            if uf.connect(x, y):
                res.append(dfs(x, y, {x}))
            else:
                res.append(-1)
        return res            

class UnionFind:
    def __init__(self, keys):
        self.parent = dict()
        self.rank = dict()
        self.size = len(keys)
        for k in keys:
            self.parent[k] = k
            self.rank[k] = 1

    def find(self, x):
        if x not in self.parent:
            return ""
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
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == "" or rooty == "" or rootx != rooty:
            return False
        return True        