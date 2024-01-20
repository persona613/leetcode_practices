"""
Wrong Answer
32 / 55 testcases passed
Input
n = 4
k = 4
Use Testcase
Output 1
Expected 0
"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        if n == 2:
            if k == 1: return 0
            else: return 1
        # pivot=len/2, len=2**(n-1)
        pv = 2**(n-1)//2
        if k < pv:
            return self.kthGrammar(n-1, k)
        else: # idx move forward and mirror
            return self.kthGrammar(n-1, (pv+1)-(k-pv))
