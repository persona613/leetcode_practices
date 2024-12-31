"""
Wrong Answer
34 / 36 testcases passed

Editorial
Input
low =
50000
high =
100000
zero =
50000
one =
50000

Use Testcase
Output
999950014
Expected
6
"""
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            cnt = 0
            cnt += dfs(i - zero) if i - zero >= 0 else 0
            cnt += dfs(i - one) if i - one >= 0 else 0
            dp[i] = cnt % MOD
            return dp[i]

        MOD = 10 ** 9 + 7
        # dp[i] = count of strings which length == i
        dp = [-1] * (high + 1)
        dp[0] = 1
        dfs(high)
        return sum(dp[low:]) % MOD