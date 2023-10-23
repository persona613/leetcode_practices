"""
96 ms runtime beats 5.52%
28.79 MB memory beats 5.02%
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m==0: return True
        if n==0: return False
        dp = [[None for i in range(n)] for _ in range(m)]

        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j] != None:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = dfs(i-1,j-1) + 1
            else:
                dp[i][j] = max(dfs(i-1,j), dfs(i,j-1))
            return dp[i][j]

        return dfs(m-1,n-1) == m