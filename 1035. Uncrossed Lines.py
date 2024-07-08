"""
220 ms runtime beats 30.95%
60.43 MB memory beats 21.25%
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i == -1 or j == -1:
                return 0

            if nums1[i] == nums2[j]:
                return 1 + dp(i-1, j-1)
            else:
                return max(dp(i-1, j), dp(i, j-1))

        return dp(len(nums1)-1, len(nums2)-1)