"""
593 ms runtime beats 37.15%
45.05 MB memory beats 5.26%
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pool = set(nums)
        arr = list(pool)
        uf = UnionFind(len(arr))
        
        # UnionFind finder
        fd = dict()
        for i, v in enumerate(arr):
            fd[v] = i

        for i, v in enumerate(arr):
            if v + 1 in pool:
                uf.union(i, fd[v + 1])
            if v - 1 in pool:
                uf.union(i, fd[v - 1])
        return max(uf.count)

class UnionFind:
    def __init__(self, ln):
        self.root = [i for i in range(ln)]
        self.count = [1] * ln
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        cx = self.count[rootx]
        cy = self.count[rooty]
        if cx >= cy:
            self.root[rooty] = rootx
            self.count[rooty] -= cy
            self.count[rootx] += cy
        else:
            self.root[rootx] = rooty
            self.count[rootx] -= cx
            self.count[rooty] += cx
