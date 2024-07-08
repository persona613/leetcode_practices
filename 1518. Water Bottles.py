"""
41 ms runtime beats 12.64%
16.49 MB memory beats 79.17%
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles
        while empty >= numExchange:
            q = empty // numExchange
            ans += q
            r = empty % numExchange
            empty = q + r
        return ans