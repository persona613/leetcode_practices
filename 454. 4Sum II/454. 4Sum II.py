'''
Runtime: 774 ms, faster than 84.44% of Python3 online submissions 
Memory Usage: 14.1 MB, less than 97.51% of Python3 online submissions
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), defaultdict(int), 0
        for i in nums1:
            for j in nums2:
                hm[i+j] += 1
        for x in nums3:
            for y in nums4:
                res += hm[0 - (x+y)]
        return res
