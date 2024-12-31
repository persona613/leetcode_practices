"""
121 ms runtime beats 81.28%
21.09 MB memory beats 81.57%
"""
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp[i] = count of strings which length == i
        dp = [0] * (high + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for length in range(1, high + 1):
            if zero <= length:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if one <= length:
                dp[length] = (dp[length] + dp[length - one]) % MOD
        res = 0
        for cnt in dp[low:]:
            res = (res + cnt) % MOD
        return res