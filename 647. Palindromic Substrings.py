"""
109 ms runtime beats 46.26%
24.52 MB memory beats 15.28%
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # init
        for i in range(n):
            dp[i][i] = True

        ans = 1
        for i in range(1, n):
            ans += 1
            if s[i] == s[i - 1]:
                dp[i][i - 1] = True
                ans += 1
            for j in range(i - 2, -1, -1):
                if s[i] == s[j] and dp[i - 1][j + 1]:
                    dp[i][j] = True
                    ans += 1
        return ans