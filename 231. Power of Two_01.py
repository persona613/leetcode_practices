"""
30 ms runtime beats 83.36%
13.8 MB memory beats 38.60%
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 2 != 0: 
            return False
        return self.isPowerOfTwo(n // 2)