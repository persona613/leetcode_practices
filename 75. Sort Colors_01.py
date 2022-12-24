"""
91 ms runtime beats 5.31%
13.9 MB memory beats 64.30%
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            mini = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[mini]:
                    mini = j
            nums[i], nums[mini] = nums[mini], nums[i]