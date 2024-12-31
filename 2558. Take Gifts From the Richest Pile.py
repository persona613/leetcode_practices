"""
0 ms runtime beats 100.00%
17.61 MB memory beats 8.46%
"""
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gi = []
        for gift in gifts:
            gi.append(-gift)
        heapq.heapify(gi)
        for _ in range(k):
            curr = -heapq.heappop(gi)
            heapq.heappush(gi, -int(curr ** 0.5))
        return -sum(gi)