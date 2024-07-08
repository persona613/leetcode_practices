"""
52 ms runtime beats 85.68%
17.89 MB memory beats 26.97%
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[0]: no stock, dp[1]: have stock
        dp = [0, -prices[0]]

        for p in prices[1:]:
            curr = [0, 0]            
            # curr no stock: (sell stock) or (pre no stock)
            curr[0] = max(dp[1] + p, dp[0])            
            # curr have stock: (pre have stock) or (buy stock)
            curr[1] = max(dp[1], dp[0] - p)

            dp = curr
        return dp[0]