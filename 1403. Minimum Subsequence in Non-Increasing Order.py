"""
63 ms runtime beats 73.63%
15.90 MB memory beats 100%
"""
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        lt = sorted(nums, reverse=True)
        sm = sum(lt)
        res, t = [], 0
        for n in lt:
            res.append(n)
            t += n
            sm -= n
            if t > sm:
                return res