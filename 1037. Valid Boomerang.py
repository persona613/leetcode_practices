"""
50 ms runtime beats 26.83%
16.32 MB memory beats 34.71%
"""
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        def sl(p1, p2): # slope
            if p1 == p2:
                return
            if p2[0] - p1[0] == 0:
                return float("inf")
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        points.sort(key=lambda p: p[0])
        m1 = sl(points[0], points[1])
        m2 = sl(points[1], points[2])
        if m1 == None or m2 == None:
            return False
        return m1 != m2