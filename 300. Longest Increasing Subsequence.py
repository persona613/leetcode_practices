"""
761 ms runtime beats 76.77%
16.92 MB memory beats 44.20%
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        for i in range(n):
            a = nums[i]
            length = 0
            for j in range(i):
                if nums[j] < a and dp[j] > length:
                    length = dp[j]
            dp.append(length + 1)
        return max(dp)