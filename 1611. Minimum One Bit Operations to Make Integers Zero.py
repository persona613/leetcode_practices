"""
40 ms runtime beats 59.09%
16.38 MB memory beats 27.27%
"""
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n <= 1:
            return n
        q = n
        p = 0
        while q > 1:
            p += 1
            q //= 2
        return 2**(p+1) - 1 - self.minimumOneBitOperations(n-2**p)
