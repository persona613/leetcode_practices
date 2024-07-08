"""
69 ms runtime beats 82.77%
19.79 MB memory beats 97.53%
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = sorted(intervals)
        q = [meetings[0][1]] # store end time of meeting
        for st, nd in meetings[1:]:
            if q[0] <= st:
                heapq.heappop(q)
            heapq.heappush(q, nd)
        return len(q)