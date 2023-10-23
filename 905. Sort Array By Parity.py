'''
Runtime: 77 ms, faster than 54.41% of Python3 online submissions 
Memory Usage: 17 MB, less than 96.40% of Python3 online submissions 
'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l]%2 == 0:
                l += 1
            elif nums[r]%2 == 1:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums