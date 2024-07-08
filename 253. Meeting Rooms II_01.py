"""
72 ms runtime beats 70.28%
19.78 MB memory beats 97.96%
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = sorted(intervals)
        q = [] # store end time of meeting
        res = 0
        for st, nd in meetings:
            while q and q[0] <= st:
                heapq.heappop(q)
            heapq.heappush(q, nd)
            if len(q) > res:
                res = len(q)
        return res