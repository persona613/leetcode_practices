"""
660 ms runtime beats 92.68%
41.51 MB memory beats 20.52%
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = sorted(zip(capital, profits))
        n = len(arr)
        take = i = 0
        q = []
        while take < k:
            while i < n and arr[i][0] <= w:
                heapq.heappush(q, -arr[i][1])
                i += 1
            if not q:
                break
            w -= heapq.heappop(q)
            take += 1
        return w