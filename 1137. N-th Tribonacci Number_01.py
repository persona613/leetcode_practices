"""
41 ms runtime beats 59.43%
16.3 MB memory beats 29.52%
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1
        memo = [1] * (n+1)
        memo[0] = 0
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]