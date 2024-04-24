"""
193 ms runtime beats 40.45%
15.6 MB memory beats 29.25%
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            maps[i] = maps.setdefault(i, 0) + 1
            # maj
            if maps[i] == len(nums)//2 + 1:
                return i