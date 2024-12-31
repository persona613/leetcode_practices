"""
2 ms runtime beats 63.12%
17.93 MB memory beats 10.22%
"""
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stk = []
        # find next small value
        for i in range(len(prices)):
            while stk and prices[stk[-1]] >= prices[i]:
                res[stk.pop()] -= prices[i]
            stk.append(i)
        return res