"""
49 ms runtime beats 14.32%
18.18 MB memory beats 17.80%
"""
class Solution:
    def numTilings(self, n: int) -> int:
        
        # dp[i] = dp[i-1]+dp[i-2] + 2*dp[i-3] + 2*dp[i-4] +... 2*dp[i-i]
        #       = 2*dp[i-1] + dp[i-3]
        @lru_cache(None)
        def dp(i):
            if i == 0 or i == 1:
                return 1
            if i < 0:
                return 0
            
            return (2 * dp(i - 1) % mod + dp(i - 3) % mod) % mod
        
        mod = 10 ** 9 + 7
        return dp(n)