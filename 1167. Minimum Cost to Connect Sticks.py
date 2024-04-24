"""
243 ms runtime beats 14.24%
18.14 MB memory beats 13.00%
"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        q = []
        for s in sticks:
            heapq.heappush(q, s)

        ans = 0
        while len(q) > 1:
            top = heapq.heappop(q)
            ans += top + q[0]
            heapq.heapreplace(q, top + q[0])
        return ans