"""
698 ms runtime beats 51.17%
16.65 MB memory beats 92.02%
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tsum = sum(nums)
        if tsum % 2 == 1: return False

        k = tsum // 2
        dp = [0] * (k + 1)
        dp[0] = 1

        # take or not-take, to sum S
        # Q(i,s) = Q(i-1,s) or Q(i-1,s-nums[i])
        for i in range(n):
            curr = nums[i]
            # not-take could just pass value
            # no need next-dp array in reverse order
            for j in range(k, -1, -1):
                if curr <= j:
                    dp[j] = dp[j] or dp[j - curr]
        return dp[-1]