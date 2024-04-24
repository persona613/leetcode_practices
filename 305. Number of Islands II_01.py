"""
Wrong Answer
138 / 162 testcases passed

Editorial
Input
m =
3
n =
3
positions =
[[0,0],[0,1],[1,2],[1,2]]

Use Testcase
Output
[1,1,2,3]
Expected
[1,1,2,2]
"""
class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = dict()
        self.land = 0
    
    def find(self, id):
        if self.parent[id] != id:
            self.parent[id] = self.find(self.parent[id])
        return self.parent[id]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        rankx = self.rank[rootx]
        ranky = self.rank[rooty]
        if rankx > ranky:
            self.parent[rooty] = rootx
        elif rankx < ranky:
            self.parent[rootx] = rooty
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
        self.land -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]
        uf = UnionFind()
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        res = []
        for i, j in positions:
            grid[i][j] = 1
            id = m * i + j
            uf.parent[id] = id
            uf.rank[id] = 0
            uf.land += 1
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n \
                        and grid[ni][nj] == 1:
                        nid = m * ni + nj
                        uf.union(id, nid)
            res.append(uf.land)
        return res