"""
42 ms runtime beats 27.32%
16.26 MB memory beats 50.00%
"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(t):
            if t == 0: return 0
            return helper(t//2)^(t%2)
        return helper(k-1)