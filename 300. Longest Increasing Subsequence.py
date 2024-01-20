"""
53 ms runtime beats 97.46%
17.72 MB memory beats 14.10%
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for v in nums:
            i = bisect_left(res, v)
            if i == len(res):
                res.append(v)
            elif v < res[i]:
                res[i] = v
        return len(res)