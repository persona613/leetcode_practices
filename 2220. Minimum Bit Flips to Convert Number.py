"""
30 ms runtime beats 86.72%
16.49 MB memory beats 69.15%
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
        # return sum(int(i) for i in bin(start^goal)[2:])