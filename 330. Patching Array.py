"""
59 ms runtime beats 44.75%
16.76 MB memory beats 27.97%
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # [1,2,3] -> sum reach 6
        # next optimal int to make is 7, ref 1798.
        nxt = 1
        ln = len(nums)
        i = ans = 0
        while nxt <= n:
            if i < ln and nums[i] <= nxt:
                nxt += nums[i]
                i += 1
            else:
                nxt += nxt
                ans += 1
        return ans