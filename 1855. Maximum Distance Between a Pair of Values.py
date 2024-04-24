"""
1096 ms runtime beats 30.11%
34.71 MB memory beats 27.96%
"""
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            l = i
            r = len(nums2) - 1
            target = nums1[i]
            while l <= r:
                mid = (l + r) // 2
                if nums2[mid] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            if r < i:
                continue
            ans = max(ans, r - i)
        return ans