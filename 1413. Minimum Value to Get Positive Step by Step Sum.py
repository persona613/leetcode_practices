"""
34 ms runtime beats 89.69%
16.38 MB memory beats 12.05%
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = [nums[0]]
        for v in nums[1:]:
            ps.append(v + ps[-1])
        return -min(min(ps), 0) + 1