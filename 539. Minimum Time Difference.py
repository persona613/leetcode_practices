"""
61 ms runtime beats 91.21%
19.56 MB memory beats 79.74%
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = n = 60 * 24
        timeline = [0] * n
        for time in timePoints:
            # convert to minutes
            ms = int(time[0:2]) * 60 + int(time[3:])
            if timeline[ms]:
                return 0
            timeline[ms] = 1

        total_ms = 0
        pre = None
        for i in range(n):
            if timeline[i]:
                if pre is None:
                    pre = i
                else:
                    dist = i - pre
                    res = min(res, dist)
                    total_ms += dist
                    pre = i
        return min(res, n - total_ms)
        