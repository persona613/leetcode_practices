"""
433 ms runtime beats 42.68%
30.86 MB memory beats 98.58%
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1: return 0
        cost = 0
        h = list()
        n = len(heights)
        for i in range(1, n):
            if heights[i - 1] < heights[i]:
                diff = heights[i] - heights[i - 1]
                cost += diff
                heapq.heappush(h, -diff)
                if cost > bricks:
                    if not ladders:
                        return i - 1
                    else:
                        ladders -= 1
                        cost -= -heapq.heappop(h)
        return i
                