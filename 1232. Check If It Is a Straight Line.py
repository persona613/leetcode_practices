"""
69 ms runtime beats 70.40%
16.71 MB memory beats 71.99%
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def line(dx, dy, pt):
            return dx*(pt[1]-y0) == dy*(pt[0]-x0)
        x0, y0 = coordinates.pop()
        x1, y1 = coordinates.pop()
        dx = x1-x0
        dy = y1-y0
        for pt in coordinates:
            if not line(dx, dy, pt):
                return False
        return True
        