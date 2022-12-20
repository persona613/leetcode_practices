"""
61 ms runtime beats 72.89%
13.8 MB memory beats 57.12%
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        # left, right, root
        l = 1
        r = x
        t = (l+r) // 2
        # search space includ only head
        while l != t:
            if t * t > x:
                r = t
                t = (l+r) // 2
            else: # t*t <= x
                l = t
                t = (l+r) // 2
        return l
                
        