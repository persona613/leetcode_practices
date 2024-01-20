"""
720 ms runtime beats 94.35%
59.96 MB memory beats 6.69%
"""
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        ans = -inf
        for i in range(1, len(points)):
            w = points[i][0] - points[i-1][0]
            if w > ans:
                ans = w
        return ans