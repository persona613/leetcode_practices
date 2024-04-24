"""
1442 ms runtime beats 66.05%
31.25 MB memory beats 27.46%
"""
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        lo = time[0]
        hi = time[0] * totalTrips
        n = len(time)
        while lo <= hi:
            mid = (lo + hi) // 2
            trips = 0
            for bus_time in time:
                trips += mid // bus_time
            if trips >= totalTrips:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo