"""
1743 ms runtime beats 33.11%
92.15 MB memory beats 5.30%
"""
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union_byrank(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        irank = self.rank[irep]
        jrank = self.rank[jrep]
        if irank < jrank:
            self.parent[irep] = jrep
        elif jrank > irank:
            self.parent[jrep] = irep
        else:
            self.parent[irep] = jrep
            self.rank[jrep] += 1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # g := {time: {i: adj}}
        g = defaultdict(lambda: defaultdict(set))
        for a, b, t in meetings:
            g[t][a].add(b)
            g[t][b].add(a)

        ds = DisjointSet(n)
        ds.union_byrank(0, firstPerson)
        for time in sorted(g.keys()):
            gf = g[time]
            seen = set()
            q = deque()
            for a in gf:
                if ds.find(a) == firstPerson:
                    q.append(a)
                    seen.add(a)
            while q:
                curr = q.popleft()
                for adj in gf[curr]:
                    if adj not in seen:
                        ds.union_byrank(adj, curr)
                        seen.add(adj)
                        q.append(adj)

        res = {0}
        for i in range(1, n):
            if ds.find(i) == firstPerson:
                res.add(i)
        return res