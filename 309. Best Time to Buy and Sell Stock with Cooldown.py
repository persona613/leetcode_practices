"""
45 ms runtime beats 56.90%
21.74 MB memory beats 5.87%
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold:0=free, 1=holding, 2=cooldown
        @cache
        def dfs(i, hold):
            if i >= n:
                return 0
            # free
            if hold == 0:
                skip = dfs(i + 1, hold)
                buy = -prices[i] + dfs(i + 1, 1)
                return max(skip, buy)

            # holding, if sell -> cooldown
            if hold == 1:
                skip = dfs(i + 1, hold)
                sell = prices[i] + dfs(i + 1, 2)
                return max(skip, sell)
                
            # cooldown -> free
            if hold == 2:
                return dfs(i + 1, 0)

        n = len(prices)
        return dfs(0, 0)