"""
1059 ms runtime beats 70.68%
25 MB memory beats 82.89%
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # daily chanlleng 2023.02.25
        minday = 0
        mp = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[minday]:
                minday = i
            # print("mday", minday)
            mp = max(mp, prices[i] - prices[minday])
            # print("mp", mp)
        return mp
    