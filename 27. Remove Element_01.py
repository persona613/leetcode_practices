'''
Runtime Error Message:
IndexError: list index out of range
    while nums[end] == val:
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        i = 0
        end = -1
        while i < n:
            while nums[end] == val:
                end -= 1
                n -= 1
                
            if nums[i] == val:
                    
                nums[i], nums[end] = nums[end], nums[i]
                
                
            i += 1
            count += 1
        return count
        return nums