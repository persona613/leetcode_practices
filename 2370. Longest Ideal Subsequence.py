"""
1264 ms runtime beats 49.63%
21.24 MB memory beats 10.37%
"""
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n
        # dp[i] tail character position
        p = [-1] * 26

        for i in range(n):
            a = ord(s[i]) - 97
            left_range = max(0, a - k)
            right_range = min(25, a + k)
            mx_pre_dp = 0
            for j in range(left_range, right_range + 1):
                idx = p[j]
                if idx != -1:
                    mx_pre_dp = max(mx_pre_dp, dp[idx])
            dp[i] = mx_pre_dp + 1
            p[a] = i

        ans = 0
        for idx in p:
            ans = max(ans, dp[idx])
        return ans