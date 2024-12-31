"""
1500 ms runtime beats 22.92%
41.71 MB memory beats 41.79%
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # longest common subsequence (s, revesred_s)
        rs = s[::-1]
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # one-index
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # last chars are equal
                if s[i - 1] == rs[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]
        