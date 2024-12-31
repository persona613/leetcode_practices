"""
Wrong Answer
35 / 36 testcases passed

Editorial
Input
low =
50000
high =
100000
zero =
2
one =
3

Use Testcase
Output
836173535
Expected
797774039
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
        return sum(v for v in dp[low:] if v != -1) % MOD