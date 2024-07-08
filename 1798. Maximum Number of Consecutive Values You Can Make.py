"""
562 ms runtime beats 62.07%
22.22 MB memory beats 33.62%
"""
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # consective sum reach of coins
        reach = 0
        coins.sort()
        for coin in coins:
            if coin <= reach + 1:
                reach += coin
            else:
                break
        return reach + 1