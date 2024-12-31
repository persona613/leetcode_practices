"""
147 ms runtime beats 58.54%
47.33 MB memory beats 56.96%
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
        # some dp state could not be called before
        return sum(dfs(i) for i in range(low, high + 1)) % MOD