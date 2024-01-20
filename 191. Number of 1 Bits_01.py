"""
47 ms runtime beats 62.6%
16.3 MB memory beats 60.39%
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        bs = bin(n)[2:]
        return bs.count("1")