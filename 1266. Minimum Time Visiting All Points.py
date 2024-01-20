"""
74 ms runtime beats 11.69%
16.42 MB memory beats 30.54%
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        x, y = points[0]
        for pt in points[1:]:
            tx, ty = pt
            ans += max(abs(tx-x), abs(ty-y))
            x, y = tx, ty
        return ans