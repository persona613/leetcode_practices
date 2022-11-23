"""
Submission Result: Time Limit Exceeded
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    for l in nums4:
                        if i+j+k+l == 0:
                            ans += 1
        return ans