"""
109 ms runtime beats 78.33%
16.76 MB memory beats 80.90%
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for j in range(amount+1)]
        # init
        dp[0] = 1
        # dp[i][j] = dp[i-1][j] + dp[i][j-coin]
        for i in range(1, n+1):
            co = coins[i-1]
            for j in range(amount+1):
                if co <= j:
                    dp[j] += dp[j-co]
        return dp[-1]