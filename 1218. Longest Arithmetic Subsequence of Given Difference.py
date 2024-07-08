"""
402 ms runtime beats 80.72%
30.04 MB memory beats 76.36%
"""
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = dict()
        ans = 1
        for curr in arr:
            pre = curr - difference
            if pre in dp:
                dp[curr] = dp[pre] + 1
                if dp[curr] > ans:
                    ans = dp[curr]
            else:
                dp[curr] = 1
        return ans