"""
59 ms runtime beats 82.48%
16.6 MB memory beats 94.58%
"""
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            fr = nums[i]
            v = nums[i+1]
            res += [v] * fr
        return res