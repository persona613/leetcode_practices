"""
53 ms runtime beats 99.48%
17.04 MB memory beats 59.17%
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripend = []
        prs = 0
        arr = sorted(trips, key = lambda x: x[1])
        for pr, start, end in arr:
            while tripend and start >= tripend[0][0]:
                _, offcars = heapq.heappop(tripend)
                prs -= offcars

            prs += pr
            if prs > capacity:
                return False
            heapq.heappush(tripend, (end, pr))
        return True