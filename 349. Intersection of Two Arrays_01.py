'''
Runtime: 89 ms, faster than 63.94% of Python3 online submissions 
Memory Usage: 14.3 MB, less than 0% of Python3 online submissions
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        return a & b