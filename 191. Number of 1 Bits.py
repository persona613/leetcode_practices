"""
51 ms runtime beats 5.22%
16.27 MB memory beats 32.07%
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                bit += 1
            mask <<= 1
        return bit