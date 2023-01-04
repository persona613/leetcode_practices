"""
53 ms runtime beats 47.12%
13.9 MB memory beats 65.13%
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n == 1:
            return x        
        
        if n < 0:
            y = self.myPow(1/x, -n//2)
            if n % 2 == 0:
                return y*y
            else:
                return y*y*(1/x)
        else:
            y = self.myPow(x, n//2)
            if n % 2 == 0:
                return y*y
            else:
                return y*y*x