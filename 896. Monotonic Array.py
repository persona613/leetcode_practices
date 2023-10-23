"""
801 ms runtime beats 89.33%
30.4 MB memory beats 95.58%
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # large, small
        l = s = 0
        for a, b in zip(nums, nums[1:]):
            if a > b:
                l = 1
            elif a < b:
                s = 1
        return False if l and s else True