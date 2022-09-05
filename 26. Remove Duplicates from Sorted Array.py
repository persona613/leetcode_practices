'''
Runtime: 95 ms, faster than 90.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 63.78% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni = 0
        for i in range(len(nums)):
            if nums[uni] != nums[i]:
                uni += 1
                nums[uni] = nums[i]
        return uni+1        