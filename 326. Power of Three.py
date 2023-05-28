"""
99 ms runtime beats 26.41%
16.3 MB memory beats 5.48%
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True