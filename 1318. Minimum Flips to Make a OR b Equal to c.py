"""

36 ms runtime beats 47.28%
16.50 MB memory beats 43.35%
"""
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aorb = (a | b)
        # different bits
        xor = (aorb ^ c)
        ans = 0
        while xor:
            if xor & 1:
                if c & 1:
                    # c-bit is 1, open a-bit or b-bit
                    ans += 1
                else: 
                    # c-bit is 0, close a-bit and b-bit
                    ans += a & 1
                    ans += b & 1
            xor >>= 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans