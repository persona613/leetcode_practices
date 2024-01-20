"""
Runtime Error
3 / 98 testcases passed
IndexError: list index out of range

nums = [1,1,1]
k = 1
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        ans = l = 0
        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            while cur >= k:
                cur //= nums[l]
                l += 1
            ans += i - l + 1
        return ans