"""
513 ms runtime beats 86.77%
16.95 MB memory beats 23.47%
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # LIS length and frquency at index-i
        dp = [1] * n
        freq = [1] * n
        for i in range(n):
            curr = nums[i]
            for j in range(i):
                if nums[j] < curr:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        freq[i] = freq[j]
                    elif dp[j] + 1 == dp[i]:
                        freq[i] += freq[j]
        maxln = max(dp)
        return sum(freq[i] for i in range(n) if dp[i] == maxln)