"""
27 ms runtime beats 92.51%
16.49 MB memory beats 58.08%
"""
class Solution:
    def findComplement(self, num: int) -> int:
        # get left most 1 pos
        n = num
        k = 0
        while n:
            n >>= 1
            k += 1
        mask = (1 << k) - 1
        return num ^ mask