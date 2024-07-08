"""
31 ms runtime beats 86.48%
16.46 MB memory beats 68.04%
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0 and n-1 can't consider at the same time
        # if take 0 in consideration, n-1 must not taken in
        # if take n-1, 0 must not taken in
        def rb(dp):
            if len(dp) == 1:
                return dp[0]

            dp[1] = max(dp[0], dp[1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2]+dp[i])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        return max(rb(nums[1:]), rb(nums[:len(nums)-1]))