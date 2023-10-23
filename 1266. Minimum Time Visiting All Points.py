"""
58 ms runtime beats 92.42%
16.28 MB memory beats 82.26%
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            ans += max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
        return ans


        # ans = 0
        # x, y = points[0]
        # for tx, ty in points[1:]:
        #     ans += max(abs(tx-x), abs(ty-y))
        #     x, y = tx, ty
        # return ans


        # ans = 0
        # x, y = points[0]
        # for i in range(1, len(points)):
        #     tx, ty = points[i]        
        #     ans += max(abs(tx-x), abs(ty-y))
        #     x, y = tx, ty
        # return ans