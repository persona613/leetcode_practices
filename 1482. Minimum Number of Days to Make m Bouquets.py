"""
825 ms runtime beats 56.21%
30.58 MB memory beats 23.96%
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def makebouquet(t):
            # adj_flower, bouquet
            aflower = bouquet = 0
            for d in bloomDay:
                if d <= t:
                    aflower += 1
                    if aflower >= k:
                        bouquet += 1
                        aflower = 0
                else:
                    aflower = 0
            return bouquet >= m

        n = len(bloomDay)
        if m * k > n:
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if makebouquet(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l