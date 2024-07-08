"""
804 ms runtime beats 88.84%
16.64 MB memory beats 93.63%
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [None] * n
        # init last row = nums1[m - 1]
        for j in range(n - 1, -1, -1):
            if nums1[m - 1] == nums2[j]:
                dp[j] = 1
            else:
                dp[j] = 0
        ans = max(dp)

        for i in range(m - 2, -1, -1):
            curr = [None] * n
            for j in range(n - 1, -1, -1):
                if nums1[i] != nums2[j]:
                    curr[j] = 0
                else:
                    if j == n - 1:
                        curr[j] = 1
                    else:
                        # dp[i][j] = 1 + dp[i + 1][j + 1]
                        curr[j] = 1 + dp[j + 1]
            dp = curr
            ans = max(ans, max(dp))
        return ans