"""
37 ms runtime beats 40.45%
16.53 MB memory beats 37.43%
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor:
            ans += 1
            xor = xor & (xor - 1)
        return ans