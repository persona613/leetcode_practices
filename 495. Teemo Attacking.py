"""
249 ms runtime beats 86.22%
18 MB memory beats 10.6%
"""
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        endtime = -1
        ans = 0
        for i in timeSeries:
            ans += duration
            if i <= endtime:
                ans -= endtime - (i-1)
            endtime = i + duration - 1
        return ans