'''
Runtime: 56 ms, faster than 42.02% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 0% of Python3 online submissions 
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notval = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[notval], nums[i] = nums[i], nums[notval]
                notval += 1
        
        return notval