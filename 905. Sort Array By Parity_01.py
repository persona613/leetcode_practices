'''
Runtime: 164 ms, faster than 14.13% of Python3 online submissions 
Memory Usage: 14.7 MB, less than 0% of Python3 online submissions 
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 ==0:
                nums[even], nums[i] = nums[i], nums[even]
                even += 1
        return nums