"""
575 ms runtime beats 69.74%
19.52 MB memory beats 35.27%
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        ans = l = 0
        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            while cur >= k:
                cur //= nums[l]
                l += 1
            ans += i - l + 1
        return ans