"""
Wrong Answer
763 / 925 testcases passed

Editorial
Input
nums =
[40,22,15]

Use Testcase
Output
false
Expected
true
"""
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        mx = max(nums)
        bol = [False] * (mx + 1)
        for a in nums:
            bol[a] = True
        if bol[1]: return False

        dset = DisjointSet(mx + 1)
        # sieve: find prime factor
        sieve = [True] * (mx + 1)
        for i in range(2, mx + 1):
            if sieve[i]:
                for j in range(i + i, mx + 1, i):
                    sieve[j] = False
                    if bol[j]:
                        dset.unite(i, j)

        root = dset.parent[nums[0]]
        for i in range(2, mx + 1):
            if bol[i] and dset.parent[i] != root:
                return False
        return True
        
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        irk = self.rank[irep]
        jrk = self.rank[jrep]
        if irk > jrk:
            self.parent[jrep]  = irep
        elif irk < jrk:
            self.parent[irep] = jrep
        else:
            self.parent[jrep] = irep
            self.rank[irep] += 1