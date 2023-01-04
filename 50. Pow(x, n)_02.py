"""
Submission Result: Runtime Error 
Runtime Error Message:
OverflowError: (34, 'Numerical result out of range')
  [Previous line repeated 19 more times]
    return square(x, n//2)**2
Line 11 in square (Solution.py)
    return square(x, n//2)**2
Line 11 in square (Solution.py)
    return square(x, n//2)**2
Line 11 in square (Solution.py)
    return 1/square(x, -n)
Line 18 in myPow (Solution.py)
    ret = Solution().myPow(param_1, param_2)
Line 43 in _driver (Solution.py)
    _driver()
Line 54 in <module> (Solution.py)
Last executed input:
2.00000
-2147483648
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def square(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x            
            
            if n % 2 == 0:
                return square(x, n//2)**2
            else:
                return square(x, n//2)**2*x
        
        if n >= 0:
            return square(x, n)
        else:
            return 1/square(x, -n)