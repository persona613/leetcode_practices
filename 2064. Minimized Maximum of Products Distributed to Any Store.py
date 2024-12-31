"""
552 ms runtime beats 80.54%
28.60 MB memory beats 89.84%
"""
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def canDistribute(k):
            stores = 0
            for q in quantities:
                stores += (q + k - 1) // k
            return stores <= n

        # k: max possible distributing products to each store
        r = max(quantities)
        m = len(quantities)
        if n == m:
            return r
        l = 1
        while l <= r:
            mid = (l + r) // 2
            if canDistribute(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        