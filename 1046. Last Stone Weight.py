"""
34 ms runtime beats 72.79%
16.48 MB memory beats 90.16%
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-i for i in stones]
        heapq.heapify(q)
        while len(q) > 1:
            x = heapq.heappop(q)
            y = heapq.heappop(q)
            if x != y:
                heapq.heappush(q, x - y)
        return -q[0] if q else 0