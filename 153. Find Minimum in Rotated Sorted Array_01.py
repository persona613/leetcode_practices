"""
69 ms runtime beats 68.60%
14.1 MB memory beats 63.58%
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r) // 2
        while l != r:            
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m
            m = (l+r) // 2
        return nums[m]