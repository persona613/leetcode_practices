"""
984 ms runtime beats 10.49%
232.24 MB memory beats 6.96%
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:        
        @cache
        def dfs(i, hold):
            if i >= n:
                return 0
            # not change state of holding
            skip = dfs(i + 1, hold)
            if hold:
                # sell
                operate = prices[i] - fee + dfs(i + 1, not hold)
            else:
                # buy
                operate = -prices[i] + dfs(i + 1, not hold)
            return max(skip, operate)

        n = len(prices)
        return dfs(0, False)