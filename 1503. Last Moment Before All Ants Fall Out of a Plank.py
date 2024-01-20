"""
143 ms runtime beats 82.01%
17.26 MB memory beats 67.63%
"""
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        d1 = d2 = 0
        if left:
            d1 = max(left)
        if right:
            d2 = n - min(right)
        return max(d1, d2)