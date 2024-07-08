"""
39 ms runtime beats 29.62%
16.64 MB memory beats 7.09%
"""
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = 1
        idx = 1
        for _ in range(time):
            idx += d
            if idx == n or idx == 1:
                d *= -1
        return idx