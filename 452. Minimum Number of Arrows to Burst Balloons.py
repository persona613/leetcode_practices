"""
978 ms runtime beats 97.45%
62.30 MB memory beats 89.85%
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pts = sorted(points, key = lambda x: x[1])
        cnt = 0 # burst by same arrow
        pre_end = pts[0][1]
        n = len(pts)
        for pt in pts[1:]:
            if pre_end >= pt[0]:
                cnt += 1
            else:
                pre_end = pt[1]
        return n - cnt