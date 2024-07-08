"""
47 ms runtime beats 96.80%
18.48 MB memory beats 78.24%
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # get A ^ B
        mix = 0
        for val in nums:
            mix ^= val

        # detect 1-bit of mix
        for p in range(32):
            mask = 1 << p
            if mix & mask:
                break
        
        # seperate nums that 1-bit at p
        # xor all vals in group to get A
        group = 0
        for val in nums:
            if val & mask:
                group ^= val
        
        return [group, mix ^ group]