'''
runtime beats 68.25%
memory usage beats 63.11%
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        le = len(nums)
        while i < le:
            if nums[i] == val:
                nums.pop(i)
                le -= 1
                continue
            i += 1
                            
        return len(nums)