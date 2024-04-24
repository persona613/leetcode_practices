"""
802 ms runtime beats 94.34%
30.30 MB memory beats 65.82%
"""
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        arr = sorted(asteroids)
        m = mass
        for a in arr:
            if m < a:
                return False
            m += a
        return True