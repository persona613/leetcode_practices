"""
69 ms runtime beats 10.59%
13.9 MB memory beats 67.44%
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def square(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n == -1:
                return 1/x
            
            # n = {2,3,-2,-3}
            # p = n//2 = {0,1,0,-1}
            q = square(x, n//2)
            # r = {0,1,-1}
            r = square(x, n%2)
            
            return q * q * r
        
        return square(x, n)