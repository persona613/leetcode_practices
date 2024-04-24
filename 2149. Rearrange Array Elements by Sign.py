"""
1000 ms runtime beats 83.51%
47.29 MB memory beats 69.94%
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0, 1
        res = [0] * len(nums)
        for a in nums:
            if a > 0:
                res[pos] = a
                pos += 2
            else:
                res[neg] = a
                neg += 2
        return res
