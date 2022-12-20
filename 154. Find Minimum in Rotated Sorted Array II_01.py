"""
Submission Result: Wrong Answer 
Input:
[4,5,6,7,0,1,2]
Output:
2
Expected:
0
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def fmin(nums, l, r):
            # l = 0
            # r = len(nums)-1
            if nums[l] < nums[r]:
                return nums[l]

            while l < r:
                m = (l+r) // 2
                if nums[m] > nums[r] or nums[m] > nums[l]:
                    l = m+1
                elif nums[m] < nums[r] or nums[m] < nums[l]:
                    r = m
                else: # nums[m=l=r]
                    return min(fmin(nums,l,m), fmin(nums,m+1,r))
            return nums[l]
        
        return fmin(nums, 0, len(nums)-1)