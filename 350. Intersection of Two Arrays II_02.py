'''
Runtime: 64 ms, faster than 80.80% of Python3 online submissions 
Memory Usage: 14 MB, less than 53.14% of Python3 online submissions
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
            elif nums[m] > key:
                r = m-1
        return False
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        # dict for search
        srdict = {}
        if len(nums1) < len(nums2):
            alist = nums1
            srlist = nums2
        else:
            alist = nums2
            srlist = nums1
            
        for d in srlist:
            srdict[d] = srdict.get(d, 0) + 1
        nums = list(srdict.keys())
        nums.sort()
        for d in alist:
            if self.bs(nums, d) is True:
                if srdict[d] > 0:
                    res.append(d)
                    srdict[d] -= 1
        return res