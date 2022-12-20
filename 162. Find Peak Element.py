"""
92 ms runtime beats 55.30%
13.9 MB memory beats 82.68%
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            elif nums[mid]<nums[mid-1]:
                r = mid
            else:
                return mid            
        return l