"""
234 ms runtime beats 73.77%
17.92 MB memory beats 59.49%
"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            new = heappop(sticks) + heappop(sticks)
            ans += new
            heapq.heappush(sticks, new)
        return ans