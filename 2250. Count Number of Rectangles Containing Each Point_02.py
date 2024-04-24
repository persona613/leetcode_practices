"""
Time Limit Exceeded
42 / 47 testcases passed
"""
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key = lambda r: r[1])
        res = []
        n = len(rectangles)
        for x, y in points:
            i = bisect.bisect_left(rectangles, y, key = lambda r: r[1])
            cnt = 0
            for j in range(i, n):
                if x <= rectangles[j][0]:
                    cnt += 1
            res.append(cnt)
        return res