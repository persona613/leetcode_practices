"""
962 ms runtime beats 94.83%
24.21 MB memory beats 94.01%
"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp[i][difference] = length of array(d) end at i
        # colume: difference range [-500, 500] -> [0, 1000]
        n = len(nums)
        dp = [[1] * 1001 for _ in range(n)]

        for i in range(1, n):
            curr = nums[i]
            for p in range(i):
                pre = nums[p]
                d = curr - pre
                dp[i][d + 500] = dp[p][d + 500] + 1

        return max(max(row) for row in dp)