"""
435 ms runtime beats 17.42%
29.78 MB memory beats 29.99%
"""
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        def cut(x):
            cnt = 0
            for rib in ribbons:
                cnt += rib // x
                if cnt >= k:
                    return True
            return False

        # binary search cutting length
        r = max(ribbons)
        l = 1
        while l <= r:
            mid = (l + r) // 2
            if cut(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r