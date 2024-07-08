"""
40 ms runtime beats 19.05%
16.40 MB memory beats 80.82%
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()