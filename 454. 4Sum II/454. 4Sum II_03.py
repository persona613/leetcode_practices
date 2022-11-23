"""
Submission Result: Time Limit Exceeded
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        bag1 = set(nums1)
        bag2 = set(nums2)
        bag3 = set(nums3)
        bag4 = set(nums4)
        ans = 0
        for i in bag1:
            for j in bag2:
                for k in bag3:
                    for l in bag4:
                        if i+k+j+l == 0:
                            ans += nums1.count(i)*nums2.count(j)*nums3.count(k)*nums4.count(l)
        return ans