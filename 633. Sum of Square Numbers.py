"""
83 ms runtime beats 80.51%
16.38 MB memory beats 96.81%
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            t = l ** 2 + r ** 2
            if t > c:
                r -= 1
            elif t < c:
                l += 1
            else:
                return True
        return False