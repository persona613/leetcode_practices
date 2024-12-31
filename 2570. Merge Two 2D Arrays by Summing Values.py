"""
61 ms runtime beats 52.95%
16.72 MB memory beats 38.20%
"""
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        res = []
        i = j = 0
        while i < m and j < n:
            if nums1[i][0] < nums2[j][0]:
                res.append(nums1[i][:])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                res.append(nums2[j][:])
                j += 1
            else:
                sm = nums1[i][1] + nums2[j][1]
                res.append([nums1[i][0], sm])
                i += 1
                j += 1
        if i < m:
            for k in range(i, m):
                res.append(nums1[k][:])
        else:
            for k in range(j, n):
                res.append(nums2[k][:])
        return res