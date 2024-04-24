"""
33 ms runtime beats 77.94%
16.38 MB memory beats 99.81%
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        # -x = ~x + 1
        return n & -n == n