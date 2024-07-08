"""
413 ms runtime beats 84.26%
31.16 MB memory beats 10.59%
"""
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_used = [] # min-heap
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb > 0:
                heapq.heappush(ladder_used, climb)
            if len(ladder_used) > ladders:
                bricks -= heapq.heappop(ladder_used)
            if bricks < 0:
                return i
        return len(heights) - 1