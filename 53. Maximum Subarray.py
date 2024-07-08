"""
543 ms runtime beats 44.42%
30.94 MB memory beats 64.04%
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [None] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + max(0, dp[i - 1])

        return max(dp)