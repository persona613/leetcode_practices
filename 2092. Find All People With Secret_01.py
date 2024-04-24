"""
Wrong Answer
32 / 55 testcases passed

Input
n = 6
meetings = [[0,2,1],[1,3,1],[4,5,1]]
firstPerson = 1

Use Testcase
Output [0,1,2,3,4,5]
Expected [0,1,2,3]
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
        g = defaultdict(set)
        for meet in meetings:
            g[meet[2]].update(meet[:2])

        ds = DisjointSet(n)
        ds.union_byrank(0, firstPerson)
        for time in sorted(g.keys()):
            mts = g[time]
            shared = False
            for a in mts:
                if ds.find(a) == firstPerson:
                    shared = True
                    break
            if shared:
                for a in mts:
                    ds.union_byrank(a, firstPerson)

        res = {0}
        for i in range(1, n):
            if ds.find(i) == firstPerson:
                res.add(i)
        return res