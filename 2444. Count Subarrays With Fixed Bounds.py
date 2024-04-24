"""
719 ms runtime beats 42.15%
31.12 MB memory beats 17.63%
"""
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mii = mxi = -1
        start = ans = 0
        n = len(nums)
        for i in range(n):
            a = nums[i]
            if a == minK:
                mii = i
            if a == maxK:
                mxi = i
            if a < minK or a > maxK:
                mii = mxk = -1
                start = i + 1
            ans += max(0, min(mii, mxi) - start + 1)
        return ans
            