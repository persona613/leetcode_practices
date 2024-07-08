"""
620 ms runtime beats 21.93%
35.82 MB memory beats 13.43%
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mxq = []
        miq = []
        ans = l = 0
        for r in range(len(nums)):
            heappush(mxq, (-nums[r], r))
            heappush(miq, (nums[r], r))

            while -mxq[0][0] - miq[0][0] > limit:
                l = min(mxq[0][1], miq[0][1]) + 1

                while mxq and mxq[0][1] < l:
                    heappop(mxq)
                while miq and miq[0][1] < l:
                    heappop(miq)
            ans = max(ans, r - l + 1)
        return ans