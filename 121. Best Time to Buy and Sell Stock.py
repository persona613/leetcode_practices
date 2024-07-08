"""
809 ms runtime beats 10.10%
27.08 MB memory beats 97.68%
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        miprice = prices[0]
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - miprice)
            miprice = min(miprice, prices[i])
        return dp[-1]