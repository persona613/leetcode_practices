"""
1166 ms runtime beats 83.67%
62.84 MB memory beats 60.97%
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
            while mts and mts[0][0] <= curr_time:
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
