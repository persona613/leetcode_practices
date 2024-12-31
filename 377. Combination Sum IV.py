"""
39 ms runtime beats 66.31%
16.36 MB memory beats 97.90%
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for capacity in range(1, target + 1):
            for weight in nums:
                if weight <= capacity:
                    dp[capacity] += dp[capacity - weight]
        return dp[-1]