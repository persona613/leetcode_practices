"""
42 ms runtime beats 74.04%
16.22 MB memory beats 36.79%
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        d = max(candies) - extraCandies
        return [True if cd>=d else False for cd in candies]