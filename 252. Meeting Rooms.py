"""
70 ms runtime beats 71.41%
19.74 MB memory beats 81.46%
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        pre_end = 0
        for start, end in intervals:
            if start < pre_end:
                return False
            pre_end = end
        return True
        