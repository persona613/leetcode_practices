'''
Runtime: 54 ms, faster than 86.43% of Python3 online submissions 
Memory Usage: 14.1 MB, less than 69.66% of Python3 online submissions
'''

class Solution:
    def bs(self, nums, key):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == key:
                return True
            elif nums[m] < key:
                l = m+1
            else:
                r = m-1
        return False
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) < len(nums2):
            a = set(nums1)
            nums2.sort()
            for d in a:
                if self.bs(nums2, d) is True:
                    res.append(d)
        else:
            a = set(nums2)
            nums1.sort()
            for d in a:
                if self.bs(nums1, d) is True:
                    res.append(d)
        return res