"""
52 ms runtime beats 69.99%
17.53 MB memory beats 20.88%
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stk = []
        for n in nums2:
            while stk and stk[-1] < n:
                mp[stk.pop()] = n
            stk.append(n)
        while stk:
            mp[stk.pop()] = -1
        res = []
        for n in nums1:
            res.append(mp[n])
        return res