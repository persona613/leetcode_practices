"""
283 ms runtime beats 8.58%
17.7 MB memory beats 38.41%
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sn = sorted(nums)
        return max(sn[0]*sn[1]*sn[-1], sn[-1]*sn[-2]*sn[-3])