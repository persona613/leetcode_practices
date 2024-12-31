"""
567 ms runtime beats 24.27%
17.22 MB memory beats 71.81%
"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def findroot(x):
            if root[x] != x:
                root[x] = findroot(root[x])
            return root[x]

        clusters = n = len(stones)
        root = list(range(n))
        cnt = [1] * n
        for i in range(n):
            # pair of i stone
            pi = stones[i]
            for j in range(i + 1, n):
                pj = stones[j]
                # same row or same colume
                if pi[0] == pj[0] or pi[1] == pj[1]:
                    # union
                    rooti = findroot(i)
                    rootj = findroot(j)
                    if rooti != rootj:
                        root[rootj] = rooti
                        clusters -= 1
        return n - clusters