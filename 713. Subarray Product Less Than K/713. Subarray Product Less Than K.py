"""
593 ms runtime beats 5.09%
19.60 MB memory beats 16.13%
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        logk = math.log(k)

        # presum for log sum
        presum = [0]
        for v in nums:
            presum.append(presum[-1] + math.log(v))

        ans = 0
        for i, psm in enumerate(presum):
            j = bisect.bisect_left(presum, presum[i] + logk, i + 1)
            ans += j - (i + 1)
        return ans