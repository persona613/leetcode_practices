"""
42 ms runtime beats 52.64%
16.38 MB memory beats 11.44%
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
        mx = max(gain)
        return max(mx, 0)