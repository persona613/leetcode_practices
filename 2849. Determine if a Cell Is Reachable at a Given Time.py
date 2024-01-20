"""
36 ms runtime beats 79.94%
16.34 MB memory beats 42.87%
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy and t==1:
            return False
        # Chebyshev distance
        cd = max(abs(fx-sx), abs(fy-sy))
        return t >= cd
