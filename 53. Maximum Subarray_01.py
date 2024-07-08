"""
Time Limit Exceed
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def suml(i, j):
            nonlocal ans

            if memo[j]:
                return memo[j]
            if i > j:
                return 0
                
            memo[j] = suml(i, j-1) + nums[j]
            if memo[j] > ans:
                ans = memo[j]
            return memo[j]

        ans = float("-inf")
        for i in range(len(nums)):
            memo = [None] * len(nums)
            suml(i, len(nums)-1)

        return ans
