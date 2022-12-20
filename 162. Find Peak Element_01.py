"""
Submission Result: Wrong Answer 
Input:
[1,2]
Output:
0
Expected:
1
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if mid+1>=len(nums) or mid-1<0:
                return mid
            elif nums[mid]<nums[mid+1]:
                l = mid+1
            elif nums[mid]<nums[mid-1]:
                r = mid-1
            elif nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
        return -1
            