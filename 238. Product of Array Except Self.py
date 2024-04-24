"""
159 ms runtime beats 85.53%
23.53 MB memory beats 94.34%
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        sm = 1
        for v in nums:
            sm *= v
            res.append(sm)
        sm = 1
        for i in range(len(nums) - 1, 0, -1):
            res[i] = res[i - 1] * sm
            sm *= nums[i]
        res[0] = sm
        return res
