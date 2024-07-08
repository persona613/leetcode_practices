"""
31 ms runtime beats 86.09%
16.40 MB memory beats 99.62%
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-i for i in stones]
        heapq.heapify(q)
        while q and len(q) > 1:
            x = heapq.heappop(q)
            y = heapq.heappop(q)
            if x < y:
                heapq.heappush(q, x - y)
        return 0 if not q else -q[0]