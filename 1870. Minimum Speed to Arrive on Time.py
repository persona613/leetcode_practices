"""
2043 ms runtime beats 41.45%
31.31 MB memory beats 15.08%
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1

        def check(k):
            t = 0
            for d in dist:
                t = math.ceil(t)
                t += (d / k)
            return t <= hour

        l = 1
        r = 10 ** 7
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
