"""
1778 ms runtime beats 40.63%
16.88 MB memory beats 80.91%
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        for s in strs:
            nxt = [[0]*(n+1) for i in range(m+1)]
            b0 = s.count("0")
            b1 = s.count("1")
            for i in range(m+1):
                for j in range(n+1):
                    if b0<=i and b1<=j:
                        nxt[i][j] = max(dp[i][j], dp[i-b0][j-b1] + 1)
                    else:
                        nxt[i][j] = dp[i][j]
            dp = nxt
        return dp[-1][-1]