"""
205 ms runtime beats 93.34%
19.02 MB memory beats 65.66%
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[inf]*n for i in range(m)]
        # init
        dp[0][0] = nums1[0]*nums2[0]
        a = nums2[0]
        for i in range(1, m):
            dp[i][0] = max(dp[i-1][0], nums1[i]*a)
        a = nums1[0]
        for j in range(1, n):
            dp[0][j] = max(dp[0][j-1], nums2[j]*a)

        for i in range(1, m):
            for j in range(1, n):
                t = nums1[i]*nums2[j]
                if t >= 0:
                    dp[i][j] = max(t, dp[i-1][j], dp[i][j-1], t+dp[i-1][j-1])
                else:
                    dp[i][j] = max(t, dp[i-1][j], dp[i][j-1])
        # print(dp)
        return dp[-1][-1]               
