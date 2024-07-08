"""
74 ms runtime beats 42.81%
17.00 MB memory beats 37.85%
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        premin = premax = res = nums[0]
        for val in nums[1:]:
            p1 = val * premin
            p2 = val * premax
            currmax = max(val, p1, p2)
            currmin = min(val, p1, p2)

            res = max(res, currmax)
            premin = currmin
            premax = currmax
        return res