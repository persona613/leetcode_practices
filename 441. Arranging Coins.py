"""
47 ms runtime beats 51.62%
16.1 MB memory beats 15.50%
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor(sqrt(2*n+0.25)-0.5)