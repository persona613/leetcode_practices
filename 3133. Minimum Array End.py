"""
0 ms runtime beats 100.00%
16.64 MB memory beats 33.33%
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # merge n-1 bits into x
        ans = x
        k = n - 1
        p = 0
        while k > 0:
            # get bit of n-1
            bit = k & 1

            # search 0-bit position at x
            while ans & (1 << p):
                p += 1

            # fill bit into x
            if bit:
                ans |= (bit << p)
            p += 1

            # prepare next bit
            k >>= 1

        return ans