"""
71 ms runtime beats 78.47%
19.85 MB memory beats 66.64%
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        # overlap: a[0] <= b[1] and b[0] <= a[1]
        a0, a1 = newInterval
        n = len(intervals)

        # overlap start index
        overlap_start = bisect.bisect_left(intervals, a0, key=lambda x: x[1])
        if overlap_start == n:
            return intervals + [newInterval]

        # overlap end index
        overlap_end = bisect.bisect_left(intervals, a1, key=lambda x: x[0])
        if overlap_end >= n:
            overlap_end -= 1

        # a[1] should >= b[0]
        if a1 < intervals[overlap_end][0]:
            overlap_end -= 1
        if overlap_end == -1:
            return [newInterval] + intervals

        # merge
        new_start = min(a0, intervals[overlap_start][0])
        new_end = max(a1, intervals[overlap_end][1])
        arr = intervals[:overlap_start]
        arr.append([new_start, new_end])
        arr.extend(intervals[overlap_end + 1:])
        return arr
