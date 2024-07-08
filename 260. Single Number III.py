"""
56 ms runtime beats 68.47%
18.40 MB memory beats 88.94%
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # get A ^ B
        mix = 0
        for val in nums:
            mix ^= val

        # detect right most 1-bit of mix
        diff = mix & (-mix)

        # seperate nums that 1-bit at p
        # xor all vals in group to get A
        group = 0
        for val in nums:
            if val & diff:
                group ^= val
        
        return [group, mix ^ group]