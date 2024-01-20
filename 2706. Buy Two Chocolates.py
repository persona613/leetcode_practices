"""
56 ms runtime beats 93.54%
17.21 MB memory beats 23.41%
"""
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left = money - prices[0] - prices[1]
        return left if left >= 0 else money