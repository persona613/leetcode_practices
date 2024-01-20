"""
56 ms runtime beats 58.46%
16.45 MB memory beats 10.60%
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for v in nums:
            if v > a:
                b = a
                a = v
            elif v > b:
                b = v
        return (a - 1) * (b - 1)