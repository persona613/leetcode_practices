"""
329 ms runtime beats 98.04%
35.53 MB memory beats 73.75%
"""
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        while i < m and j < n:
            a = nums1[i]
            b = nums2[j]
            if a == b:
                return nums1[i]
            elif a < b:
                i += 1
            else:
                j += 1
        return -1