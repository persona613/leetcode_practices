'''
Runtime: 52 ms, faster than 38.34% of Python3 online submissions 
Memory Usage: 16.68 MB, less than 71.02% of Python3 online submissions
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for k in c1:
            if k in c2:
                res.extend([k] * min(c1[k], c2[k]))
        return res