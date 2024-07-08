"""
1120 ms runtime beats 40.23%
55.03 MB memory beats 87.39%
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # last_interval remain
        pre = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < pre[1]:
                ans += 1
                # remove the interval it's end at right most
                # remain the interval it's end at left most
                if pre[1] > curr[1]:
                    pre = curr
            else:
                pre = curr
        return ans