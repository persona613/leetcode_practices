"""
599 ms runtime beats 55.99%
22.86 MB memory beats 77.33%
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for i in range(len(points)):
            d = abs(points[i][0]) ** 2 + abs(points[i][1]) ** 2
            heapq.heappush(maxheap, (-d, i))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [points[tp[1]] for tp in maxheap]