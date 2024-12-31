"""
729 ms runtime beats 56.64%
31.22 MB memory beats 55.06%
"""
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = [-v for v in nums]
        heapq.heapify(q)
        score = 0
        for _ in range(k):
            mx = -heapq.heappop(q)
            score += mx
            heapq.heappush(q, -((mx + 2) // 3))
        return score