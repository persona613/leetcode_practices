"""
42 ms runtime beats 15.07%
16.46 MB memory beats 90.10%
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        # n & (n - 1) flip least-significant 1-bit to 0
        while n != 0:
            ans += 1
            n &= n - 1
        return ans