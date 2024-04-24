"""
264 ms runtime beats 58.32%
24.89 MB memory beats 57.55%
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            arrow = abs(nums[i]) - 1 # pointer
            if nums[arrow] < 0:
                res.append(arrow + 1)
            else:
                nums[arrow] = -nums[arrow]
        return res