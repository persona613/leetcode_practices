"""
107 ms runtime beats 68.31%
16.74 MB memory beats 77.07%
"""
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = set()
        ans = 0
        for a in nums:
            if -a in d:
                ans = max(ans, abs(a))
            d.add(a)
        return ans if ans else -1