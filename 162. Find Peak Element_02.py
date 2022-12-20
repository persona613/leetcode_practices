"""
96 ms runtime beats 46.10%
13.9 MB memory beats 82.56%
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        while l <= r:
            mid = (l+r) // 2
            if mid+1<len(nums) and nums[mid]<nums[mid+1]:
                l = mid+1
            elif mid-1>=0 and nums[mid]<nums[mid-1]:
                r = mid
            else:
                return mid
            # elif mid+1>=len(nums) or mid-1<0:
            #     return mid            
            # elif nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
            #     return mid
        return -1