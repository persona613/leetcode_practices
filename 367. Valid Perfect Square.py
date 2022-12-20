"""
36 ms runtime beats 86.79%
13.9 MB memory beats 57.3%
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 1
        r = num // 2
        while l <= r:
            m = (l+r) // 2
            if m*m == num:
                return True
            elif m*m > num:
                r = m-1
            elif m*m < num:
                l = m+1
        return False