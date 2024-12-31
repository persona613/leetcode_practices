"""
45 ms runtime beats 68.91%
16.53 MB memory beats 61.96%
"""
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for f in range(2, int(i ** 0.5) + 1):
                if i % f == 0:
                    dp[i] = dp[f] + dp[i // f]
                    break
            else:
                # prime
                dp[i] = i

        return dp[-1]