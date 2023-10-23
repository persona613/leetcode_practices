"""
44 ms runtime beats 32.51%
16.3 MB memory beats 58.98%
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i == 2 or i == 3:
                memo[i] = i
                return i
            mx = i
            for j in range(2, i//2+1):
                p = dfs(j) * dfs(i-j)
                mx = max(mx, p)
            memo[i] = mx
            return mx
        return dfs(n)