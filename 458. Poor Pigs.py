"""
36 ms runtime beats 68.85%
16.08 MB memory beats 96.72%
"""
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets==1: return 0
        t = minutesToTest/minutesToDie + 1
        x = 1
        while t**x < buckets:
            x += 1
        return x