"""
227 ms runtime beats 25.94%
80.03 MB memory beats 19.98%
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def dp(i: int, holding: bool, remain: int) -> int:
            # holding:bool represent the state After the buy/sell-decision made
            # remain calculate at sell-time
            # when remain==0, if holding==True, still can decide to buy
            # when remain==0, if holding==False, can't decide to sell anymore

            # another solution
            # if remain calculate at buy-time
            # base case contorl => if remain < 1: return 0
            if remain < 1 and holding == False:
                return 0
            if i == 0:
                if holding == True:
                    return -prices[0]
                return 0

            # sell or not sell
            if holding == False:
                # not sell
                ret1 = dp(i - 1, False, remain)
                # sell
                ret2 = dp(i - 1, True, remain - 1) + prices[i]
            
            # buy or not buy
            elif holding == True:
                # not buy
                ret1 = dp(i - 1, True, remain)
                # buy
                ret2 = dp(i - 1, False, remain) - prices[i]
            return max(ret1, ret2)

        return dp(len(prices) - 1, False, k)