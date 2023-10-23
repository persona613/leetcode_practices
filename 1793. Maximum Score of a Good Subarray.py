"""
1036 ms runtime beats 63.27%
27.3 MB memory beats 46.94%
"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sc = mi = nums[k]
        l = r = k
        while l-1>=0 and r+1<n:
            if nums[r+1] >= nums[l-1]:
                mi = min(mi, nums[r+1])
                r += 1
            else:
                mi = min(mi, nums[l-1])
                l -= 1
            sc = max(sc, mi * (r-l+1))
        while l-1>=0:
            mi = min(mi, nums[l-1])
            l -= 1
            sc = max(sc, mi * (r-l+1))
        while r+1<n:
            mi = min(mi, nums[r+1])
            r += 1
            sc = max(sc, mi * (r-l+1))
        return sc
                    