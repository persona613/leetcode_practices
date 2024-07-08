"""
361 ms runtime beats 79.70%
21.81 MB memory beats 25.28%
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        mxdp = [None] * n
        mxdp[0] = nums[0]
        for i in range(1, n):
            mxdp[i] = max(mxdp[i - 1] + nums[i], nums[i])
        maxsum = max(mxdp)

        midp = [None] * n
        midp[0] = nums[0]
        for i in range(1, n):
            midp[i] = min(midp[i - 1] + nums[i], nums[i])
        minsum = min(midp)

        totalsum = sum(nums)
        if minsum == totalsum:
            return maxsum
        return max(maxsum, totalsum - minsum)