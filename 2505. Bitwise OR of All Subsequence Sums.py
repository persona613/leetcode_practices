"""
388 ms runtime beats 53.57%
30.24 MB memory beats 7.14%
"""
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        presum = [nums[0]]
        for a in nums[1:]:
            presum.append(a + presum[-1])
        res = 0
        for a in nums:
            res |= a
        for a in presum:
            res |= a
        return res