"""
Wrong Answer
80 / 82 testcases passed
Input
n = 4
meetings =
[[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]

Use Testcase
Output 1
Expected 0
"""
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        arr = sorted(meetings, key = lambda x: x[0])
        freq = [0] * n
        rooms = list() # free rooms
        mts = list() # meetings happening
        for i in range(n):
            heapq.heappush(rooms, i)

        for m in arr:
            curr_time = m[0]
            while mts and mts[0][0] < curr_time:
                _, room = heapq.heappop(mts)
                heapq.heappush(rooms, room)
            if rooms:
                room = heapq.heappop(rooms)
                heapq.heappush(mts, (m[1], room))
            else:
                end_time, room = heapq.heappop(mts)
                heapq.heappush(mts, (end_time + m[1] - m[0], room))
            freq[room] += 1
        mx = max(freq)
        for i in range(n):
            if freq[i] == mx:
                return i
