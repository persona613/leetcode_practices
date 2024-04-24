"""
44 ms runtime beats 80.11%
16.66 MB memory beats 91.42%
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        res = []
        for v in nums1:
            d[v] = 1
        for v in nums2:
            if v in d and d[v] == 1:
                res.append(v)
                d[v] -= 1
        return res