'''
Runtime: 238 ms, faster than 68.44% of Python3 online submissions 
Memory Usage: 15.6 MB, less than 0% of Python3 online submissions 
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n], nums[i] = nums[i], nums[n]
                n += 1
        return nums