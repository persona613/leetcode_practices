"""
410 ms runtime beats 60.89%
53.26 MB memory beats 5.31%
"""
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        memo = dict()
        md = 10**9 + 7
        def dfs(a, b, c):
            if a < 1 or b < 1 or c < 1:
                return 0
            if (a, b, c) in memo:
                return memo[(a, b, c)]
            if a==1 and c==1:
                memo[(a, b, c)] = b
                return b
            if b==1 and c==1:
                memo[(a, b, c)] = 1
                return 1
            # c not change: not take b
            rt1 = dfs(a, b-1, c)%md
            # c not change: take b
            rt2 = (dfs(a-1, b, c) - dfs(a-1, b-1, c))*b%md
            # c change
            rt3 = dfs(a-1, b-1, c-1)%md
            memo[(a, b, c)] = (rt1+rt2+rt3)%md
            return memo[(a, b, c)]

        return dfs(n, m, k)
