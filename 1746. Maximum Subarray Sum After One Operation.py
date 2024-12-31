"""
907 ms runtime beats 21.23%
39.45 MB memory beats 18.49%
"""
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0] = max_sum no element squared
        # dp[i][1] = max_sum with one element squared
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = nums[0]
        # Kadane's algorithm, max_sum of subarray ending at ecah i
        for i in range(1, n):
            dp[i][0] = max(nums[i], nums[i] + dp[i - 1][0])

        dp[0][1] = nums[0] ** 2
        # max_sum of subarray ending at ecah i with one element squared
        for i in range(1, n):
            curr = nums[i]
            # not square curr (square pre elements)
            nsqc = max(curr, curr + dp[i - 1][1])
            # square curr
            curr *= curr
            sqc = max(curr, curr + dp[i - 1][0])
            dp[i][1] = max(nsqc, sqc)
        
        ans = float("-inf")
        for i in range(n):
            if dp[i][1] > ans:
                ans = dp[i][1]
        return ans