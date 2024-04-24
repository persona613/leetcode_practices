"""
1217 ms runtime beats 91.90%
31.24 MB memory beats 36.61%
"""
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        q = [-v for v in piles]
        heapq.heapify(q)
        for _ in range(k):
            x = heapq.heappop(q)
            heapq.heappush(q, x // 2)
        return -sum(q)