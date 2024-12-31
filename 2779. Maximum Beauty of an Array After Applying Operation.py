"""
230 ms runtime beats 50.43%
28.18 MB memory beats 34.13%
"""
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = l = 0
        for r in range(n):
            # shrink window
            while nums[r] - nums[l] > 2 * k:
                l += 1
            ans = max(ans, r - l + 1)
        return ans