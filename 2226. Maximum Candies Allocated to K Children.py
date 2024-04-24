"""
905 ms runtime beats 66.96%
29.86 MB memory beats 39.61%
"""
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def divide(cnt):
            piles = 0
            for ca in candies:
                piles += ca // cnt
            return piles >= k

        l = 1
        r = max(candies)
        while l <= r:
            mid = (l + r) // 2
            if divide(mid):
                l = mid + 1
            else:
                r = mid - 1 # r may jump to 0
        return r
