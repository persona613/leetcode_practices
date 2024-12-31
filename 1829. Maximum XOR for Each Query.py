"""
27 ms runtime beats 95.54%
32.68 MB memory beats 79.65%
"""
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mx = 2 ** maximumBit - 1
        prefix = 0
        res = []
        for v in nums:
            prefix ^= v
            res.append(mx ^ prefix)
        return res[::-1]