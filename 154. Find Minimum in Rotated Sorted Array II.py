"""
67 ms runtime beats 77.30%
14.5 MB memory beats 10.61%
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
                if nums[m] > nums[r] or nums[m] > nums[0]:
                    l = m+1
                elif nums[m] < nums[r] or nums[m] < nums[0]:
                    r = m
                else: # nums[m=l=r]
                    return min(fmin(nums,l,m), fmin(nums,m+1,r))
            return nums[l]
        
        return fmin(nums, 0, len(nums)-1)