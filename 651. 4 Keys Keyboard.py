"""
42 ms runtime beats 25.00%
16.40 MB memory beats 96.21%
"""
class Solution:
    def maxA(self, n: int) -> int:
        # [A..] + [CC] + [V..] = n
        # CC: copy cost
        # V: paste time at right end
        # A: A's count at left end
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            # minus minimum copy cost = 2, remain moves
            r = i - 2
            p = 0
            for v in range(1, r):
                p = max(p ,dp[r - v] + dp[r - v] * v)
            dp[i] = max(p, dp[i - 1] + 1)
        return dp[-1]