"""
44 ms runtime beats 69.89%
13.9 MB memory beats 53.18%
"""
class Solution:
    def fib(self, n: int) -> int:
        
        cache = {}
        def recur_fib(n):
            if n in cache:
                return cache[n]
            if n < 2:
                return n
            res = recur_fib(n-1)+recur_fib(n-2)
            cache[n] = res
            return res
        
        return recur_fib(n)