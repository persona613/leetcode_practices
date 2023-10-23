"""
35 ms runtime beats 85.71%
16.1 MB memory beats 92.55%
"""
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1 or n == 2: return 1
        pn = 2 # prime numbers (2, 3)
        for i in range(4, n+1):
            for div in range(2, ((i+1)//2)+1):
                if i % div == 0:
                    break
            else:
                pn += 1
        ans = 1
        for x in range(1, pn+1):
            ans *= x
        for x in range(1, (n-pn)+1): # non-prime nums
            ans *= x
        return ans % (10**9+7)