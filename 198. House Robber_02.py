"""
39 ms runtime beats 54.78%
16.54 MB memory beats 56.96%
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # prevprev, prev
        pp = p = 0
        for v in nums:
            curr = max(p, v + pp)
            pp = p
            p = curr
        return p