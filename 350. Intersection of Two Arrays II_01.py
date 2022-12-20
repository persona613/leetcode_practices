'''
Runtime: 156 ms, faster than 11.86% of Python3 online submissions 
Memory Usage: 14 MB, less than 52.17% of Python3 online submissions
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1) <= len(nums2):
            ns = nums1
            search = nums2
        else:
            ns = nums2
            search = nums1
        for n in ns:
            if n in search:
                ans.append(n)
                search.remove(n)
            else:
                continue
        return ans
            