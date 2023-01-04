"""
36 ms runtime beats 74.86%
13.8 MB memory beats 67.43%
"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # F(N,K) = F(N-1,K//2) + 1, if K%2==1
        i = 0
        def helper(n, k):
            nonlocal i
            # while k==0, n must be 1, bcz k-max=2^n-1
            # k decrease rapidly than n, so use k
            if k == 0: 
                return 
            if k % 2 == 1:
                i += 1                
            return helper(n-1, k//2)
        
        helper(n, k-1) # k change to 0-index
        return i % 2