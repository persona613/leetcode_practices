"""
44 ms runtime beats 27.29%
17.46 MB memory beats 5.57%
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        # seperate or connect prev digit
        # dp[i] = dp[i-1] + dp[i-2]
        n = len(s)
        dp = [0] * n
        # init
        dp[0] = 1
        if s[1] == "0":
            if s[0] <= "2":
                dp[1] = 1
            else:
                return 0
        elif s[:2] > "26":
            dp[1] = dp[0]
        else:
            dp[1] = dp[0] + 1
        for i in range(2, n):
            p, c = s[i-1], s[i]
            if c == "0":
                if p == "0" or p > "2":
                    return 0
                else:
                    dp[i] = dp[i-2]
            else:
                if p == "0":
                    dp[i] = dp[i-1]
                elif p + c > "26":
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]