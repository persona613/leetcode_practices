"""
Runtime: 1549 ms, faster than 47.66% of Python3 online submissions 
Memory Usage: 30.7 MB, less than 9.87% of Python3 online submissions 
"""

class Solution:
    def numSquares(self, n: int) -> int:
        m = int(n**0.5)
        if m**2 == n:
            return 1
        
        factors = [x**2 for x in range(m, 0, -1)]
        q = deque(factors)
        res = 2
        
        while q:
            pass
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                fd = n-curr
                if fd in factors:
                    return res
                
                for x in range(m, 0, -1):
                    if curr+x**2 <= n:
                        q.append(curr+x**2)
                    
            res += 1
            
        return n
        
        

        
        
        
        