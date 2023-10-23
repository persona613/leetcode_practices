"""
35 ms runtime beats 90.23%
16.2 MB memory beats 84.24%
"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ta = []
        for i in range(len(nums)):
            ta.insert(index[i], nums[i])
        return ta