"""
274 ms runtime beats 46.17%
18.16 MB memory beats 58.50%
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(t):
            time = 0
            for p in piles:
                time += math.ceil(p / t)
            return time <= h
        
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l