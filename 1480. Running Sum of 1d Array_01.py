
'''
Runtime: 77 ms, faster than 24.35% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14 MB, less than 72.68% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

