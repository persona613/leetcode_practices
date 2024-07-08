"""
33 ms runtime beats 76.14%
16.54 MB memory beats 65.36%
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1 << 31
        ans = 0
        for i in range(32):
            d = (mask & n)
            d >>= (32 - i - 1)
            ans += d << i
            mask >>= 1
        return ans