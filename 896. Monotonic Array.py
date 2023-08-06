"""
940 ms runtime beats 79.27%
30.46 MB memory beats 87.12%
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        minus, add = True, True
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                minus = False
            elif nums[i] < nums[i-1]:
                add = False
            if not minus and not add:
                return False
        return True